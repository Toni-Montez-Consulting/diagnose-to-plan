from __future__ import annotations

from pathlib import Path

from dtp.config import find_repo_root, load_config


def test_load_config_points_at_repo(repo_root: Path) -> None:
    config = load_config(repo_root)

    assert config.repo_root == repo_root
    assert config.skills_dir == repo_root / "skills"
    assert config.outputs_dir == repo_root / "outputs"
    assert config.extracts_dir == repo_root / "extracts"
    assert config.practice_os_dir == repo_root / "practice-os"
    assert config.engagements_dir == repo_root / "engagements"


def test_find_repo_root_from_child(repo_root: Path) -> None:
    assert find_repo_root(repo_root / "src" / "dtp") == repo_root
