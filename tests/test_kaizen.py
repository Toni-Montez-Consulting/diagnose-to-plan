from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import pytest
from typer.testing import CliRunner

from dtp.cli import app
from dtp.commands.kaizen import (
    KaizenError,
    classify_text,
    mirror_blocker,
    private_kaizen_index_path,
    read_kaizen_records,
    render_mirror,
    render_status,
    run_kaizen_capture,
    run_kaizen_mirror,
    run_kaizen_status,
    run_kaizen_update,
)
from dtp.config import DtpConfig


def test_capture_creates_stable_jsonl_record(tmp_path: Path) -> None:
    config = _config(tmp_path)

    result = run_kaizen_capture(
        config,
        "Add a Hub intake check before route work.",
        item_type="auto",
        status="now",
        sensitivity="internal-only",
        repo="hub",
        captured_at=datetime(2026, 5, 4, 12, 0, tzinfo=UTC),
    )

    assert result.record.id.startswith("kzn-20260504-add-a-hub-intake-check-before")
    assert result.record.item_type == "feature"
    assert result.record.status == "now"
    assert result.index_path == tmp_path / "practice-os" / "kaizen" / "intake.jsonl"
    assert read_kaizen_records(config) == (result.record,)


@pytest.mark.parametrize(
    ("text", "expected"),
    (
        ("Maybe there is a better launch offer path.", "idea"),
        ("Build the new owner dashboard feature.", "feature"),
        ("Cameron engagement packet needs follow-up.", "engagement"),
        ("This proof candidate could become a case study.", "proof"),
        ("The repo issue is an open PR with failing checks.", "repo_issue"),
        ("Waiting on owner input is blocking this lane.", "blocker"),
        ("Correction: I forgot the brand update.", "correction"),
    ),
)
def test_classifier_routes_common_inputs(text: str, expected: str) -> None:
    assert classify_text(text) == expected


def test_mirror_dry_run_blocks_sensitive_and_unreviewed_proof(tmp_path: Path) -> None:
    config = _config(tmp_path)
    run_kaizen_capture(
        config,
        "Add slogan rollout to the consulting roadmap.",
        item_type="feature",
        status="now",
        sensitivity="internal-only",
        captured_at=datetime(2026, 5, 4, 9, 0, tzinfo=UTC),
    )
    private = run_kaizen_capture(
        config,
        "Cameron private client reply includes payment timing.",
        item_type="client_reply",
        status="waiting",
        sensitivity="private-client",
        captured_at=datetime(2026, 5, 4, 9, 1, tzinfo=UTC),
    )
    proof = run_kaizen_capture(
        config,
        "Proof candidate for public case study.",
        item_type="proof",
        status="inbox",
        sensitivity="public-safe",
        captured_at=datetime(2026, 5, 4, 9, 2, tzinfo=UTC),
    )
    manual_private_marker = run_kaizen_capture(
        config,
        "Greg owner reply should still stay out of Notion.",
        item_type="ask",
        status="inbox",
        sensitivity="internal-only",
        captured_at=datetime(2026, 5, 4, 9, 3, tzinfo=UTC),
    )

    result = run_kaizen_mirror(config)

    assert len(result.allowed_rows) == 1
    assert result.allowed_rows[0]["notion_surface"] == "Today"
    blocked_ids = {row["source_id"] for row in result.blocked_rows}
    assert private.record.id in blocked_ids
    assert proof.record.id in blocked_ids
    assert manual_private_marker.record.id in blocked_ids
    assert mirror_blocker(private.record) == "sensitivity is private-client"
    assert "proof item is not reviewed" in mirror_blocker(proof.record)
    assert '"allowed_rows"' in render_mirror(result)


def test_private_capture_writes_only_redacted_stub_to_committed_index(tmp_path: Path) -> None:
    config = _config(tmp_path)

    result = run_kaizen_capture(
        config,
        "Cameron private client reply includes payment timing.",
        item_type="client_reply",
        status="waiting",
        sensitivity="private-client",
        captured_at=datetime(2026, 5, 4, 9, 1, tzinfo=UTC),
    )

    committed_text = result.index_path.read_text(encoding="utf-8")
    private_text = private_kaizen_index_path(config).read_text(encoding="utf-8")
    record = read_kaizen_records(config)[0]

    assert "Cameron private client reply" not in committed_text
    assert "payment timing" not in committed_text
    assert "[redacted private-client client_reply capture]" in committed_text
    assert "Cameron private client reply includes payment timing." in private_text
    assert result.private_index_path == private_kaizen_index_path(config)
    assert record.raw_ref.startswith(".dtp/kaizen/private-intake.jsonl#")
    assert mirror_blocker(record) == "sensitivity is private-client"


def test_coi_capture_writes_only_redacted_stub_to_committed_index(tmp_path: Path) -> None:
    config = _config(tmp_path)

    run_kaizen_capture(
        config,
        "DSE COI follow-up should stay private.",
        item_type="repo_issue",
        status="blocked",
        sensitivity="internal-only",
        captured_at=datetime(2026, 5, 4, 9, 4, tzinfo=UTC),
    )

    committed_text = (config.practice_os_dir / "kaizen" / "intake.jsonl").read_text(
        encoding="utf-8"
    )
    private_text = private_kaizen_index_path(config).read_text(encoding="utf-8")

    assert "DSE COI follow-up" not in committed_text
    assert "[redacted coi-gated repo_issue capture]" in committed_text
    assert "DSE COI follow-up should stay private." in private_text


def test_status_renders_active_buckets(tmp_path: Path) -> None:
    config = _config(tmp_path)
    for status in ("inbox", "now", "waiting", "blocked", "parked"):
        run_kaizen_capture(
            config,
            f"Capture {status} item.",
            status=status,
            sensitivity="internal-only",
            captured_at=datetime(2026, 5, 4, 10, 0, tzinfo=UTC),
        )

    status = run_kaizen_status(config)
    rendered = render_status(status)

    assert status.counts["total"] == 5
    assert "inbox=1" in rendered
    assert "now=1" in rendered
    assert "waiting=1" in rendered
    assert "blocked=1" in rendered
    assert "parked=1" in rendered


def test_update_changes_status_and_next_action(tmp_path: Path) -> None:
    config = _config(tmp_path)
    captured = run_kaizen_capture(
        config,
        "Add a repo health item.",
        status="inbox",
        sensitivity="internal-only",
        captured_at=datetime(2026, 5, 4, 10, 0, tzinfo=UTC),
    )

    updated = run_kaizen_update(
        config,
        captured.record.id,
        status="blocked",
        repo="hub",
        next_action="wait for Tailwind migration plan",
    )

    assert updated.record.status == "blocked"
    assert updated.record.repo == "hub"
    assert updated.record.next_action == "wait for Tailwind migration plan"
    assert read_kaizen_records(config)[0].status == "blocked"


def test_update_invalid_id_raises(tmp_path: Path) -> None:
    config = _config(tmp_path)

    with pytest.raises(KaizenError, match="unknown kaizen record"):
        run_kaizen_update(config, "missing", status="done")


def test_status_limit_and_filter(tmp_path: Path) -> None:
    config = _config(tmp_path)
    for index in range(7):
        run_kaizen_capture(
            config,
            f"Inbox item {index}",
            status="inbox",
            sensitivity="internal-only",
            captured_at=datetime(2026, 5, 4, 10, index, tzinfo=UTC),
        )

    status = run_kaizen_status(config, status_filter="inbox", limit=3)
    rendered = render_status(status)

    assert len(status.records) == 3
    assert "Inbox item 0" not in rendered
    assert "Inbox item 6" in rendered


def test_mirror_skips_done_by_default_and_can_include_done(tmp_path: Path) -> None:
    config = _config(tmp_path)
    run_kaizen_capture(
        config,
        "Done safe item.",
        status="done",
        sensitivity="internal-only",
        captured_at=datetime(2026, 5, 4, 10, 0, tzinfo=UTC),
    )
    run_kaizen_capture(
        config,
        "Now safe item.",
        status="now",
        sensitivity="internal-only",
        captured_at=datetime(2026, 5, 4, 10, 1, tzinfo=UTC),
    )

    default = run_kaizen_mirror(config)
    include_done = run_kaizen_mirror(config, include_done=True)

    assert default.skipped_done == 1
    assert [row["name"] for row in default.allowed_rows] == ["Now safe item."]
    assert {row["name"] for row in include_done.allowed_rows} == {
        "Done safe item.",
        "Now safe item.",
    }


def test_kaizen_cli_capture_status_and_mirror(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    runner = CliRunner()

    capture = runner.invoke(
        app,
        [
            "kaizen",
            "capture",
            "Add a roadmap feature from chat.",
            "--status",
            "now",
            "--repo",
            "diagnose-to-plan",
        ],
    )
    status = runner.invoke(app, ["kaizen", "status", "--status", "now", "--limit", "2"])
    mirror = runner.invoke(app, ["kaizen", "mirror", "--dry-run"])

    assert capture.exit_code == 0
    assert "kaizen captured" in capture.output
    assert status.exit_code == 0
    assert "Kaizen Kanban Status" in status.output
    assert mirror.exit_code == 0
    assert '"mode": "dry-run"' in mirror.output


def test_kaizen_cli_update(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    runner = CliRunner()
    capture = runner.invoke(app, ["kaizen", "capture", "Add updateable item.", "--json"])
    record_id = capture.output.split('"id": "')[1].split('"')[0]

    update = runner.invoke(
        app,
        [
            "kaizen",
            "update",
            record_id,
            "--status",
            "waiting",
            "--next-action",
            "wait on owner",
        ],
    )

    assert update.exit_code == 0
    assert "kaizen updated" in update.output
    assert "waiting" in update.output


def test_kaizen_cli_status_preserves_redacted_titles(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    runner = CliRunner()

    capture = runner.invoke(
        app,
        [
            "kaizen",
            "capture",
            "Cameron private client reply should be redacted.",
            "--type",
            "client_reply",
            "--sensitivity",
            "private-client",
            "--status",
            "waiting",
        ],
    )
    status = runner.invoke(app, ["kaizen", "status", "--status", "waiting"])

    assert capture.exit_code == 0
    assert status.exit_code == 0
    assert "[redacted private-client client_reply capture]" in status.output


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
    )
