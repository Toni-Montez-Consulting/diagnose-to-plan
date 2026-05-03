from __future__ import annotations

import asyncio
from pathlib import Path

import pytest
from claude_agent_sdk import ToolPermissionContext

from dtp.git_safety import (
    SafetyAbort,
    make_repo_boundary_check,
    repo_boundary_decision,
    resolve_inside_repo,
)


def test_resolve_inside_repo_accepts_repo_path(repo_root: Path) -> None:
    path = resolve_inside_repo(repo_root / "inputs" / "fixture-diagnose.md", repo_root)

    assert path == repo_root / "inputs" / "fixture-diagnose.md"


def test_resolve_inside_repo_rejects_sibling(repo_root: Path) -> None:
    with pytest.raises(SafetyAbort):
        resolve_inside_repo(repo_root.parent / "tonimontez.co" / "index.md", repo_root)


def test_repo_boundary_decision_allows_reads(repo_root: Path) -> None:
    result = repo_boundary_decision(
        "Read",
        {"file_path": str(repo_root.parent / "tonimontez.co" / "index.md")},
        repo_root,
    )

    assert result.behavior == "allow"


def test_repo_boundary_decision_denies_sibling_write(repo_root: Path) -> None:
    result = repo_boundary_decision(
        "Write",
        {"file_path": str(repo_root.parent / "tonimontez.co" / "index.md")},
        repo_root,
    )

    assert result.behavior == "deny"
    assert "outside repo root" in result.message


def test_repo_boundary_callback_denies_sibling_write(repo_root: Path) -> None:
    callback = make_repo_boundary_check(repo_root)

    result = asyncio.run(
        callback(
            "Write",
            {"file_path": str(repo_root.parent / "tonimontez.co" / "index.md")},
            ToolPermissionContext(),
        )
    )

    assert result.behavior == "deny"
