from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest


@pytest.mark.skipif(shutil.which("bash") is None, reason="bash is required for hook scripts")
def test_block_sibling_writes_hook_denies_outside_path(repo_root: Path) -> None:
    env = os.environ.copy()

    result = subprocess.run(
        ["bash", ".claude/hooks/block-sibling-writes.sh"],
        cwd=repo_root,
        env=env,
        input='{"file_path":"../tonimontez.co/index.md"}',
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 2
    assert "outside repo root" in result.stderr


@pytest.mark.skipif(shutil.which("bash") is None, reason="bash is required for hook scripts")
def test_block_protected_branch_hook_denies_commit_on_main(
    tmp_path: Path,
    repo_root: Path,
) -> None:
    _init_repo(tmp_path, branch="main")
    shutil.copy(
        repo_root / ".claude" / "hooks" / "block-protected-branch.sh",
        tmp_path / "block-protected-branch.sh",
    )
    env = os.environ.copy()

    result = subprocess.run(
        ["bash", "block-protected-branch.sh"],
        cwd=tmp_path,
        env=env,
        input='{"command":"git commit -m test"}',
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 2
    assert "protected branch: main" in result.stderr


@pytest.mark.skipif(shutil.which("bash") is None, reason="bash is required for hook scripts")
def test_pre_commit_hook_blocks_confidential_frontmatter(
    tmp_path: Path,
    repo_root: Path,
) -> None:
    _init_repo(tmp_path, branch="feature/test")
    (tmp_path / ".dtp").mkdir()
    shutil.copy(repo_root / "scripts" / "pre-commit.sh", tmp_path / "pre-commit.sh")
    shutil.copy(repo_root / ".dtp" / "scrub-patterns.txt", tmp_path / ".dtp" / "scrub-patterns.txt")
    client_file = tmp_path / "clients" / "acme" / "note.md"
    client_file.parent.mkdir(parents=True)
    client_file.write_text("---\nconfidential: true\n---\n\nPrivate note.\n", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)

    result = subprocess.run(
        ["bash", "pre-commit.sh"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 1
    assert "blocked confidential staged artifact" in result.stderr


def _init_repo(path: Path, *, branch: str) -> None:
    subprocess.run(["git", "init", "-b", branch], cwd=path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.name", "Test User"], cwd=path, check=True)
