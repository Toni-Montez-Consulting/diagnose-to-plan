from __future__ import annotations

from pathlib import Path

import pytest

from dtp.git_safety import SafetyAbort, resolve_inside_repo


def test_resolve_inside_repo_accepts_repo_path(repo_root: Path) -> None:
    path = resolve_inside_repo(repo_root / "inputs" / "fixture-diagnose.md", repo_root)

    assert path == repo_root / "inputs" / "fixture-diagnose.md"


def test_resolve_inside_repo_rejects_sibling(repo_root: Path) -> None:
    with pytest.raises(SafetyAbort):
        resolve_inside_repo(repo_root.parent / "consulting" / "README.md", repo_root)
