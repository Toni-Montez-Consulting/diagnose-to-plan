from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import frontmatter

from dtp.config import DtpConfig
from dtp.extract.indexer import ExtractError


@dataclass(frozen=True)
class RecallResult:
    path: Path
    relative_path: str
    type: str
    repo: str
    title: str
    score: int
    snippet: str
    metadata: dict[str, Any]


def recall(
    *,
    config: DtpConfig,
    query: str,
    repo: str | None = None,
    kind: str | None = None,
    since: str | None = None,
    rebuild_index: bool = False,
) -> tuple[RecallResult, ...]:
    if rebuild_index or not _db_path(config).exists():
        rebuild_recall_index(config)
    rows = _query_db(config=config, query=query, repo=repo, kind=kind, since=since)
    return tuple(_row_to_result(config, row, query) for row in rows)


def rebuild_recall_index(config: DtpConfig) -> None:
    config.extracts_dir.mkdir(parents=True, exist_ok=True)
    db_path = _db_path(config)
    connection = sqlite3.connect(db_path)
    try:
        connection.execute("DROP TABLE IF EXISTS extracts")
        connection.execute(
            """
            CREATE TABLE extracts (
              path TEXT PRIMARY KEY,
              type TEXT NOT NULL,
              repo TEXT NOT NULL,
              repos TEXT NOT NULL,
              title TEXT NOT NULL,
              created TEXT NOT NULL,
              metadata TEXT NOT NULL,
              content TEXT NOT NULL
            )
            """
        )
        for path in _extract_files(config.extracts_dir):
            item = _index_item(config, path)
            connection.execute(
                """
                INSERT OR REPLACE INTO extracts
                (path, type, repo, repos, title, created, metadata, content)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item["path"],
                    item["type"],
                    item["repo"],
                    ",".join(item["repos"]),
                    item["title"],
                    item["created"],
                    json.dumps(item["metadata"], sort_keys=True),
                    item["content"],
                ),
            )
        connection.commit()
    finally:
        connection.close()


def results_to_json(results: tuple[RecallResult, ...]) -> str:
    payload = [
        {
            "path": result.relative_path,
            "type": result.type,
            "repo": result.repo,
            "title": result.title,
            "score": result.score,
            "snippet": result.snippet,
            "metadata": result.metadata,
        }
        for result in results
    ]
    return json.dumps(payload, indent=2) + "\n"


def _query_db(
    *,
    config: DtpConfig,
    query: str,
    repo: str | None,
    kind: str | None,
    since: str | None,
) -> list[sqlite3.Row]:
    connection = sqlite3.connect(_db_path(config))
    connection.row_factory = sqlite3.Row
    try:
        clauses = ["LOWER(content || ' ' || title || ' ' || metadata) LIKE ?"]
        params: list[str] = [f"%{query.lower()}%"]
        if repo:
            clauses.append("(repo = ? OR (',' || repos || ',') LIKE ?)")
            params.extend([repo, f"%,{repo},%"])
        if kind:
            clauses.append("type = ?")
            params.append(kind)
        if since:
            clauses.append("created >= ?")
            params.append(since)
        sql = "SELECT * FROM extracts WHERE " + " AND ".join(clauses)
        rows = list(connection.execute(sql, params))
    finally:
        connection.close()
    return sorted(rows, key=lambda row: _score(row, query), reverse=True)


def _row_to_result(config: DtpConfig, row: sqlite3.Row, query: str) -> RecallResult:
    metadata = json.loads(row["metadata"])
    relative = row["path"]
    return RecallResult(
        path=config.repo_root / relative,
        relative_path=relative,
        type=row["type"],
        repo=row["repo"],
        title=row["title"],
        score=_score(row, query),
        snippet=_snippet(row["content"]),
        metadata=metadata,
    )


def _score(row: sqlite3.Row, query: str) -> int:
    haystack = f"{row['title']}\n{row['metadata']}\n{row['content']}".lower()
    terms = [term for term in query.lower().split() if term]
    base = sum(haystack.count(term) for term in terms) if terms else 1
    if row["type"] == "pattern":
        base += 3
    if "promoted" in row["metadata"]:
        base += 1
    return base


def _extract_files(extracts_dir: Path) -> tuple[Path, ...]:
    if not extracts_dir.exists():
        return ()
    return tuple(
        sorted(
            path
            for path in extracts_dir.rglob("*")
            if path.is_file() and path.suffix.lower() in {".md", ".json"}
        )
    )


def _index_item(config: DtpConfig, path: Path) -> dict[str, Any]:
    relative = path.relative_to(config.repo_root).as_posix()
    kind = _kind(path)
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        content = json.dumps(data, indent=2)
        metadata = data
        title = f"{data.get('repo_name', data.get('repo_slug', path.stem))} index"
        repo = str(data.get("repo_slug", path.stem))
        repos = (repo,)
        created = str(data.get("indexed_at", ""))
    else:
        post = frontmatter.load(path)
        metadata = dict(post.metadata)
        content = post.content
        title = _title_from_content(content, path)
        repos = _repos_for_metadata(metadata, path)
        repo = repos[0]
        created = str(
            metadata.get("detected_at")
            or metadata.get("synthesized_at")
            or metadata.get("created")
            or ""
        )
        kind = str(metadata.get("type") or kind)
    if not created:
        created = date.fromtimestamp(path.stat().st_mtime).isoformat()
    return {
        "path": relative,
        "type": kind,
        "repo": repo,
        "repos": repos,
        "title": title,
        "created": created,
        "metadata": metadata,
        "content": content,
    }


def _kind(path: Path) -> str:
    parent = path.parent.name
    if parent == "index":
        return "index"
    if parent == "patterns":
        return "pattern"
    if parent == "synthesis":
        return "synthesis"
    if parent == "lessons":
        return "lesson"
    if parent == "decisions":
        return "decision"
    return parent


def _title_from_content(content: str, path: Path) -> str:
    for line in content.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def _repo_from_name(path: Path) -> str:
    return path.stem.split("--", 1)[0]


def _repos_for_metadata(metadata: dict[str, Any], path: Path) -> tuple[str, ...]:
    candidates: list[str] = []
    for key in ("repo", "repo_slug", "canonical_repo"):
        value = metadata.get(key)
        if isinstance(value, str) and value:
            candidates.append(value)
    canonical_repos = metadata.get("canonical_repos")
    if isinstance(canonical_repos, list):
        candidates.extend(str(item) for item in canonical_repos if item)
    if not candidates:
        candidates.append(_repo_from_name(path))
    return tuple(dict.fromkeys(candidates))


def _snippet(content: str) -> str:
    text = " ".join(content.split())
    return text[:240]


def _db_path(config: DtpConfig) -> Path:
    return config.extracts_dir / ".recall.db"


def validate_kind(kind: str | None) -> None:
    if kind is None:
        return
    allowed = {"index", "pattern", "synthesis", "lesson", "decision"}
    if kind not in allowed:
        raise ExtractError(f"invalid recall type: {kind}")
