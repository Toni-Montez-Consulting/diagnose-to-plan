from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import frontmatter

from dtp.commands.kit import render_status, run_kit_new, run_kit_status
from dtp.config import DtpConfig


def test_kit_new_creates_private_engagement_skeleton(tmp_path: Path) -> None:
    config = _config(tmp_path)

    result = run_kit_new(
        config=config,
        client="Mom Nonprofit",
        project="site-rebuild",
        kind="launch",
        clock=datetime(2026, 4, 29, 12, 0, tzinfo=UTC),
    )

    assert result.client_id == "mom-nonprofit"
    assert result.engagement_id == "site-rebuild"
    assert (tmp_path / "engagements" / "mom-nonprofit" / "client-context.md").exists()
    assert (
        tmp_path / "engagements" / "mom-nonprofit" / "site-rebuild" / "handoff" / "checklist.md"
    ).exists()
    assert (
        tmp_path
        / "engagements"
        / "mom-nonprofit"
        / "site-rebuild"
        / "command-room"
        / "fit-assessment.md"
    ).exists()
    assert (
        tmp_path
        / "engagements"
        / "mom-nonprofit"
        / "site-rebuild"
        / "proof"
        / "proof-packet.md"
    ).exists()
    assert (
        tmp_path
        / "engagements"
        / "mom-nonprofit"
        / "site-rebuild"
        / "proof"
        / "redaction-queue-item.md"
    ).exists()
    post = frontmatter.load(
        tmp_path / "engagements" / "mom-nonprofit" / "site-rebuild" / "diagnose.md"
    )
    assert post["data_class"] == "P2"
    assert post["confidential"] is True
    assert post["permission_level"] == "internal_only"
    proof = frontmatter.load(
        tmp_path / "engagements" / "mom-nonprofit" / "site-rebuild" / "proof" / "proof-packet.md"
    )
    assert proof["permission_level"] == "internal_only"
    assert "No public claim approved." in proof.content


def test_kit_status_reports_missing_readiness(tmp_path: Path) -> None:
    config = _config(tmp_path)
    run_kit_new(config=config, client="Fake Client", project="sample", kind="audit")

    (status,) = run_kit_status(config=config, client="fake-client")
    rendered = render_status((status,), tmp_path)

    assert status.client_id == "fake-client"
    assert status.missing == ()
    assert status.ready is False
    assert "metrics: needed" in rendered
    assert "redaction: needed" in rendered


def test_kit_status_default_skips_hidden_dirs_and_local_sample(tmp_path: Path) -> None:
    config = _config(tmp_path)
    run_kit_new(config=config, client="Fake Client", project="sample", kind="audit")
    run_kit_new(config=config, client="Real Client", project="pilot", kind="launch")
    (tmp_path / "engagements" / ".git").mkdir()
    (tmp_path / "engagements" / "real-client" / ".system").mkdir()

    statuses = run_kit_status(config=config)

    assert [status.client_id for status in statuses] == ["real-client"]


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
