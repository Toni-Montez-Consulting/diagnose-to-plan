from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from dtp.capture import render_markdown_with_frontmatter, slugify
from dtp.config import DtpConfig
from dtp.extract.indexer import ExtractError
from dtp.workspace import load_workspace


def run_lesson(
    *,
    config: DtpConfig,
    repo: str,
    pattern: str | None = None,
    kind: str = "lesson",
    source: Path | None = None,
    clock: datetime | None = None,
) -> Path:
    if kind not in {"lesson", "decision"}:
        raise ExtractError(f"invalid lesson type: {kind}")
    repo_slug = slugify(repo)
    now = clock or datetime.now(UTC)
    source_path = _resolve_source(config=config, repo=repo, source=source)
    slug_source = pattern or (source_path.stem if source_path else "operator-note")
    destination = (
        config.extracts_dir
        / "lessons"
        / f"{repo_slug}--{now.strftime('%Y-%m-%d')}-{slugify(slug_source)}.md"
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    metadata = {
        "repo": repo_slug,
        "pattern": pattern or "",
        "type": kind,
        "created": _timestamp(now),
        "source": _display_source(config, source_path),
        "promoted": False,
        "private_review_required": True,
    }
    destination.write_text(
        render_markdown_with_frontmatter(metadata, _body(repo_slug, pattern, kind, source_path)),
        encoding="utf-8",
    )
    return destination


def _resolve_source(config: DtpConfig, repo: str, source: Path | None) -> Path | None:
    if source is None:
        return None
    candidates: list[Path] = []
    if source.is_absolute():
        candidates.append(source)
    else:
        candidates.append(config.repo_root / source)
        workspace = load_workspace(config.workspace_file)
        for item in workspace.repos:
            if item.name == repo or slugify(item.name) == slugify(repo):
                candidates.append(item.path / source)
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved.exists() and resolved.is_file():
            return resolved
    raise ExtractError(f"lesson source not found: {source}")


def _body(repo: str, pattern: str | None, kind: str, source_path: Path | None) -> str:
    title = f"{repo} {pattern or kind}"
    source_text = ""
    if source_path is not None:
        source_text = source_path.read_text(encoding="utf-8", errors="ignore")
    return "\n".join(
        [
            f"# {title}",
            "",
            "## Lesson",
            "",
            "TODO: Write the operator lesson in plain English.",
            "",
            "## Reusable Pattern Impact",
            "",
            "TODO: Name what should change in future scopes because of this lesson.",
            "",
            "## Do Not Reuse Blindly",
            "",
            "TODO: Name the privacy, context, or client-specific boundary.",
            "",
            "## Source",
            "",
            source_text[:12000] if source_text else "No source file provided.",
            "",
        ]
    )


def _display_source(config: DtpConfig, source_path: Path | None) -> str:
    if source_path is None:
        return ""
    try:
        return source_path.relative_to(config.repo_root).as_posix()
    except ValueError:
        return str(source_path)


def _timestamp(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=UTC)
    return value.astimezone(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")
