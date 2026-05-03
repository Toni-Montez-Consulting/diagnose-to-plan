from __future__ import annotations

from pathlib import Path

from dtp.workspace import load_workspace


def test_load_workspace(repo_root: Path) -> None:
    workspace = load_workspace(repo_root / ".dtp" / "workspace.yaml")

    assert [repo.name for repo in workspace.repos][:3] == [
        "consulting",
        "architected-strength",
        "hub",
    ]
    assert workspace.repos[0].access == "read"
    assert workspace.repos[0].path == repo_root.parent.parent / "consulting"
    assert workspace.repos[0].path.exists()
