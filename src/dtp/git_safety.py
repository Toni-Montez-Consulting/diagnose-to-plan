from __future__ import annotations

import subprocess
from pathlib import Path


class SafetyAbort(RuntimeError):
    """Raised when a command would cross a repo or branch safety boundary."""


def resolve_inside_repo(path: Path, repo_root: Path) -> Path:
    resolved = path.expanduser().resolve()
    root = repo_root.expanduser().resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise SafetyAbort(f"path is outside repo root: {resolved}") from exc
    return resolved


def assert_cwd_is_repo_root(cwd: Path, repo_root: Path) -> None:
    if cwd.resolve() != repo_root.resolve():
        raise SafetyAbort(f"git operation must run from repo root: {repo_root}")


def current_branch(repo_root: Path) -> str:
    result = subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise SafetyAbort(result.stderr.strip() or "could not read current branch")
    return result.stdout.strip()


def assert_not_protected_branch(repo_root: Path, protected: tuple[str, ...] = ("main",)) -> None:
    branch = current_branch(repo_root)
    if branch in protected:
        raise SafetyAbort(f"refusing protected branch operation on {branch}")
