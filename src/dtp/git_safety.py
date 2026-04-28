from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any

from claude_agent_sdk import PermissionResultAllow, PermissionResultDeny, ToolPermissionContext


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


def assert_not_protected_branch(
    repo_root: Path,
    protected: tuple[str, ...] = ("main", "master"),
) -> None:
    branch = current_branch(repo_root)
    if branch in protected:
        raise SafetyAbort(f"refusing protected branch operation on {branch}")


def make_repo_boundary_check(repo_root: Path):
    root = repo_root.resolve()

    async def _check(
        tool_name: str,
        tool_input: dict[str, Any],
        _ctx: ToolPermissionContext,
    ) -> PermissionResultAllow | PermissionResultDeny:
        return repo_boundary_decision(tool_name, tool_input, root)

    return _check


async def repo_boundary_check(
    tool_name: str,
    tool_input: dict[str, Any],
    _ctx: ToolPermissionContext,
) -> PermissionResultAllow | PermissionResultDeny:
    return repo_boundary_decision(tool_name, tool_input, Path.cwd().resolve())


def repo_boundary_decision(
    tool_name: str,
    tool_input: dict[str, Any],
    repo_root: Path,
) -> PermissionResultAllow | PermissionResultDeny:
    if not _is_write_tool(tool_name):
        return PermissionResultAllow()

    for candidate in _tool_paths(tool_input):
        target = candidate if candidate.is_absolute() else repo_root / candidate
        try:
            resolve_inside_repo(target, repo_root)
        except SafetyAbort:
            return PermissionResultDeny(
                message=f"blocked write outside repo root: {target}",
                interrupt=True,
            )

    return PermissionResultAllow()


def _is_write_tool(tool_name: str) -> bool:
    normalized = tool_name.split("__")[-1]
    return normalized in {"Write", "Edit", "MultiEdit", "NotebookEdit"}


def _tool_paths(tool_input: dict[str, Any]) -> tuple[Path, ...]:
    paths: list[Path] = []
    for key in ("file_path", "path", "notebook_path"):
        value = tool_input.get(key)
        if isinstance(value, str) and value.strip():
            paths.append(Path(value))
    return tuple(paths)
