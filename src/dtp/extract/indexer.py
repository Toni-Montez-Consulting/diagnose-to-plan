from __future__ import annotations

import json
import os
from collections import Counter
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from git import InvalidGitRepositoryError, Repo

from dtp.capture import slugify
from dtp.config import DtpConfig
from dtp.extract.signals import CODE_EXTENSIONS, detect_signals
from dtp.workspace import WorkspaceRepo, load_workspace

IGNORE_DIRS = {
    ".astro",
    ".cache",
    ".git",
    ".mypy_cache",
    ".next",
    ".playwright-mcp",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "target",
}

CONFIG_FILES = (
    "package.json",
    "astro.config.mjs",
    "next.config.js",
    "next.config.mjs",
    "tailwind.config.js",
    "tailwind.config.ts",
    "tsconfig.json",
    "pyproject.toml",
    "requirements.txt",
    "go.mod",
    "Cargo.toml",
    "Package.swift",
    "Gemfile",
)


class ExtractError(ValueError):
    pass


@dataclass(frozen=True)
class IndexResult:
    repo_slug: str
    json_path: Path
    markdown_path: Path
    fingerprint: dict[str, Any]


def index_repos(
    *,
    config: DtpConfig,
    repo: str | None = None,
    all_repos: bool = False,
    clock: datetime | None = None,
) -> tuple[IndexResult, ...]:
    workspace = load_workspace(config.workspace_file)
    selected = _select_repos(workspace.repos, repo=repo, all_repos=all_repos)
    return tuple(index_repo(config=config, workspace_repo=item, clock=clock) for item in selected)


def index_repo(
    *,
    config: DtpConfig,
    workspace_repo: WorkspaceRepo,
    clock: datetime | None = None,
) -> IndexResult:
    repo_path = workspace_repo.path.resolve()
    if not repo_path.exists() or not repo_path.is_dir():
        raise ExtractError(f"repo not found: {workspace_repo.name} ({repo_path})")

    files = tuple(_walk_files(repo_path))
    now = clock or datetime.now(UTC)
    repo_slug = slugify(workspace_repo.name or repo_path.name)
    fingerprint: dict[str, Any] = {
        "repo_slug": repo_slug,
        "repo_name": workspace_repo.name,
        "repo_path": _display_path(repo_path, config.repo_root),
        "indexed_at": _timestamp(now),
        "git": _git_stats(repo_path),
        "stack": _stack(files, repo_path),
        "tree": _tree(files, repo_path),
        "signals": [
            {"name": hit.name, "evidence": hit.evidence, "files": list(hit.files)}
            for hit in detect_signals(repo_path, files)
        ],
        "size": _size(files),
    }

    index_dir = config.extracts_dir / "index"
    index_dir.mkdir(parents=True, exist_ok=True)
    json_path = index_dir / f"{repo_slug}.json"
    markdown_path = index_dir / f"{repo_slug}.md"
    json_path.write_text(json.dumps(fingerprint, indent=2) + "\n", encoding="utf-8")
    markdown_path.write_text(_render_index_markdown(fingerprint), encoding="utf-8")
    return IndexResult(
        repo_slug=repo_slug,
        json_path=json_path,
        markdown_path=markdown_path,
        fingerprint=fingerprint,
    )


def load_index(config: DtpConfig, repo: str) -> dict[str, Any]:
    repo_slug = slugify(repo)
    path = config.extracts_dir / "index" / f"{repo_slug}.json"
    if not path.exists():
        workspace = load_workspace(config.workspace_file)
        matches = [
            item for item in workspace.repos if item.name == repo or slugify(item.name) == repo_slug
        ]
        if not matches:
            raise ExtractError(f"index not found and repo is not in workspace: {repo}")
        return index_repo(config=config, workspace_repo=matches[0]).fingerprint
    return json.loads(path.read_text(encoding="utf-8"))


def _select_repos(
    repos: tuple[WorkspaceRepo, ...],
    *,
    repo: str | None,
    all_repos: bool,
) -> tuple[WorkspaceRepo, ...]:
    if repo is None or all_repos:
        if not repos:
            raise ExtractError("no repos configured in .dtp/workspace.yaml")
        return repos

    repo_slug = slugify(repo)
    for item in repos:
        if item.name == repo or slugify(item.name) == repo_slug:
            return (item,)

    path = Path(repo).expanduser()
    if path.exists():
        return (WorkspaceRepo(name=path.name, path=path.resolve(), access="read"),)

    raise ExtractError(f"unknown repo: {repo}")


def _walk_files(repo_path: Path) -> Iterable[Path]:
    for directory, dirnames, filenames in os.walk(repo_path):
        dirnames[:] = [name for name in dirnames if name not in IGNORE_DIRS]
        root = Path(directory)
        for filename in filenames:
            path = root / filename
            if any(part in IGNORE_DIRS for part in path.relative_to(repo_path).parts):
                continue
            if not path.is_file():
                continue
            if path.suffix.lower() not in CODE_EXTENSIONS and path.name not in CONFIG_FILES:
                continue
            yield path


def _git_stats(repo_path: Path) -> dict[str, Any]:
    try:
        repo = Repo(repo_path)
    except InvalidGitRepositoryError:
        return {
            "first_commit_date": "",
            "last_commit_date": "",
            "total_commits": 0,
            "active_branches": [],
            "current_head": "",
            "uncommitted_changes": 0,
        }

    commits = list(repo.iter_commits("--all", max_count=5000))
    dates = [datetime.fromtimestamp(commit.committed_date, UTC) for commit in commits]
    branches = sorted(head.name for head in repo.heads)
    head = repo.head.commit.hexsha[:8] if not repo.head.is_detached else repo.head.commit.hexsha[:8]
    return {
        "first_commit_date": min(dates).date().isoformat() if dates else "",
        "last_commit_date": max(dates).date().isoformat() if dates else "",
        "total_commits": len(commits),
        "active_branches": branches,
        "current_head": head,
        "uncommitted_changes": len(repo.index.diff(None)) + len(repo.untracked_files),
    }


def _stack(files: tuple[Path, ...], repo_path: Path) -> dict[str, Any]:
    relative_names = {path.relative_to(repo_path).as_posix() for path in files}
    config_files = [name for name in CONFIG_FILES if name in relative_names]
    frameworks: set[str] = set()
    managers: set[str] = set()

    if "package.json" in relative_names:
        managers.add("npm")
        package = repo_path / "package.json"
        try:
            text = package.read_text(encoding="utf-8", errors="ignore").lower()
        except OSError:
            text = ""
        framework_terms = {
            "astro": "Astro",
            "next": "Next.js",
            "react": "React",
            "vite": "Vite",
            "tailwind": "Tailwind",
        }
        for term, label in framework_terms.items():
            if term in text:
                frameworks.add(label)
    if "pnpm-lock.yaml" in relative_names:
        managers.add("pnpm")
    if "pyproject.toml" in relative_names:
        managers.add("pip")
        frameworks.add("Python")
    if "Package.swift" in relative_names:
        frameworks.add("Swift")

    return {
        "primary_language": _primary_language(files),
        "frameworks": sorted(frameworks),
        "package_managers": sorted(managers),
        "config_files": sorted(config_files),
    }


def _tree(files: tuple[Path, ...], repo_path: Path) -> dict[str, Any]:
    dirs: set[str] = set()
    notable: list[str] = []
    for path in files:
        relative = path.relative_to(repo_path)
        parts = relative.parts
        if len(parts) >= 1:
            dirs.add(f"{parts[0]}/")
        if len(parts) >= 2:
            dirs.add(f"{parts[0]}/{parts[1]}/")
        is_doc = relative.name in {"README.md", "AGENTS.md", "CLAUDE.md"}
        if is_doc or relative.as_posix().startswith("docs/"):
            notable.append(relative.as_posix())
    return {
        "depth_2_dirs": sorted(dirs)[:120],
        "notable_files": sorted(notable)[:80],
    }


def _size(files: tuple[Path, ...]) -> dict[str, int]:
    total_loc = 0
    code_files = 0
    for path in files:
        if path.suffix.lower() in CODE_EXTENSIONS:
            code_files += 1
        try:
            total_loc += len(path.read_text(encoding="utf-8", errors="ignore").splitlines())
        except OSError:
            continue
    return {
        "total_files": len(files),
        "code_files": code_files,
        "total_loc": total_loc,
    }


def _primary_language(files: tuple[Path, ...]) -> str:
    counts = Counter(path.suffix.lower() for path in files)
    language_by_extension = {
        ".ts": "TypeScript",
        ".tsx": "TypeScript",
        ".js": "JavaScript",
        ".jsx": "JavaScript",
        ".astro": "Astro",
        ".py": "Python",
        ".swift": "Swift",
        ".sql": "SQL",
    }
    for extension, _count in counts.most_common():
        if extension in language_by_extension:
            return language_by_extension[extension]
    return "Unknown"


def _render_index_markdown(fingerprint: dict[str, Any]) -> str:
    signals = fingerprint["signals"]
    lines = [
        f"# {fingerprint['repo_name']} index",
        "",
        f"- Repo slug: `{fingerprint['repo_slug']}`",
        f"- Repo path: `{fingerprint['repo_path']}`",
        f"- Indexed at: `{fingerprint['indexed_at']}`",
        f"- Primary language: `{fingerprint['stack']['primary_language']}`",
        f"- Files: `{fingerprint['size']['total_files']}`",
        "",
        "## Signals",
        "",
    ]
    if signals:
        for signal in signals:
            lines.append(
                f"- `{signal['name']}`: {signal['evidence']} "
                f"({len(signal['files'])} files)"
            )
    else:
        lines.append("- No signals detected.")
    lines.extend(["", "## JSON", "", "```json", json.dumps(fingerprint, indent=2), "```", ""])
    return "\n".join(lines)


def _display_path(path: Path, repo_root: Path) -> str:
    try:
        return path.relative_to(repo_root).as_posix()
    except ValueError:
        return str(path)


def _timestamp(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=UTC)
    return value.astimezone(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")
