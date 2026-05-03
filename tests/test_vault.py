from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from dtp.commands.kit import run_kit_new
from dtp.commands.vault import run_vault_init, run_vault_snapshot, run_vault_status
from dtp.config import DtpConfig


def test_vault_status_starts_as_local_files_only(tmp_path: Path) -> None:
    config = _config(tmp_path)
    config.engagements_dir.mkdir()

    status = run_vault_status(config)

    assert status.exists is True
    assert status.git_initialized is False
    assert status.ready is False


@pytest.mark.skipif(shutil.which("git") is None, reason="git is required for vault snapshots")
def test_vault_snapshot_commits_private_engagements(tmp_path: Path) -> None:
    config = _config(tmp_path)
    run_kit_new(config=config, client="Mom Nonprofit", project="site-rebuild", kind="launch")
    run_vault_init(config)

    result = run_vault_snapshot(config, message="Snapshot private artifacts")

    assert result.committed is True
    assert result.status.git_initialized is True
    assert result.status.head
    assert result.status.dirty is False


def _config(root: Path) -> DtpConfig:
    return DtpConfig(
        repo_root=root,
        inputs_dir=root / "inputs",
        outputs_dir=root / "outputs",
        skills_dir=root / "skills",
        extracts_dir=root / "extracts",
        practice_os_dir=root / "practice-os",
        engagements_dir=root / "engagements",
        workspace_file=root / ".dtp" / "workspace.yaml",
        agent_enabled=False,
    )
