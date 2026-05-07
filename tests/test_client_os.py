from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from dtp.cli import app
from dtp.commands.client_os import (
    ClientOsError,
    run_client_os_bridge_export,
    run_client_os_closeout,
    run_client_os_preflight,
    run_client_os_scaffold,
    run_client_os_status,
)
from dtp.config import DtpConfig


def test_client_os_preflight_passes_complete_fixture(tmp_path: Path) -> None:
    config = _config(tmp_path)
    root = _write_complete_fixture(tmp_path)
    (root / "meeting-notes-2026-05-08.md").write_text("# notes\n", encoding="utf-8")
    (root / "post-meeting-receipt-2026-05-08.md").write_text("# receipt\n", encoding="utf-8")

    result = run_client_os_preflight(
        config=config,
        client="Greg TheGrantApp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
    )

    assert result.ok is True
    assert any(
        check.severity == "ok" and "source index has real rows" in check.message
        for check in result.checks
    )


def test_client_os_preflight_fails_when_pilot_packet_missing(tmp_path: Path) -> None:
    config = _config(tmp_path)
    (tmp_path / "engagements" / "greg-thegrantapp" / "case-study-sprint").mkdir(
        parents=True
    )

    result = run_client_os_preflight(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
    )

    assert result.ok is False
    assert any(
        check.severity == "blocker" and "pilot packet missing" in check.message
        for check in result.checks
    )


def test_client_os_preflight_fails_when_source_index_has_no_rows(tmp_path: Path) -> None:
    config = _config(tmp_path)
    root = _write_complete_fixture(tmp_path)
    packet = root / "client-os-pilot-2026-05-08.md"
    packet.write_text(
        packet.read_text(encoding="utf-8").replace(
            (
                "| Discovery prep | discovery-session-prep.md | current | meeting prep | "
                "public proof |"
            ),
            "|  |  |  |  |  |",
        ),
        encoding="utf-8",
    )

    result = run_client_os_preflight(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
    )

    assert result.ok is False
    assert any(
        check.severity == "blocker" and "source index has no real rows" in check.message
        for check in result.checks
    )


def test_client_os_scaffold_creates_dated_files(tmp_path: Path) -> None:
    config = _config(tmp_path)
    root = _write_complete_fixture(tmp_path)

    result = run_client_os_scaffold(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
    )

    assert sorted(path.name for path in result.created) == [
        "meeting-notes-2026-05-08.md",
        "post-meeting-receipt-2026-05-08.md",
    ]
    assert "Automation authority: draft_only" in (
        root / "meeting-notes-2026-05-08.md"
    ).read_text(encoding="utf-8")
    assert "proof/*" in (root / "post-meeting-receipt-2026-05-08.md").read_text(
        encoding="utf-8"
    )


def test_client_os_scaffold_infra_creates_only_infra_files(tmp_path: Path) -> None:
    config = _config(tmp_path)
    root = _write_complete_fixture(tmp_path)
    notes = root / "meeting-notes-2026-05-08.md"
    receipt = root / "post-meeting-receipt-2026-05-08.md"
    notes.write_text("existing notes\n", encoding="utf-8")
    receipt.write_text("existing receipt\n", encoding="utf-8")

    result = run_client_os_scaffold(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
        profile="infra",
    )

    assert sorted(path.name for path in result.created) == [
        "bridge-queue-2026-05-08.md",
        "build-task-2026-05-08.md",
        "chain-run-2026-05-08.md",
        "meeting-brief-2026-05-08.md",
    ]
    assert notes.read_text(encoding="utf-8") == "existing notes\n"
    assert receipt.read_text(encoding="utf-8") == "existing receipt\n"


def test_client_os_scaffold_full_creates_all_artifacts(tmp_path: Path) -> None:
    config = _config(tmp_path)
    _write_complete_fixture(tmp_path)

    result = run_client_os_scaffold(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
        profile="full",
    )

    assert sorted(path.name for path in result.created) == [
        "bridge-queue-2026-05-08.md",
        "build-task-2026-05-08.md",
        "chain-run-2026-05-08.md",
        "meeting-brief-2026-05-08.md",
        "meeting-notes-2026-05-08.md",
        "post-meeting-receipt-2026-05-08.md",
    ]


def test_client_os_preflight_full_requires_infra_artifacts(tmp_path: Path) -> None:
    config = _config(tmp_path)
    _write_complete_fixture(tmp_path)

    result = run_client_os_preflight(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
        profile="full",
    )

    assert result.ok is False
    assert any(
        check.severity == "blocker" and "meeting brief missing" in check.message
        for check in result.checks
    )


def test_client_os_preflight_full_passes_complete_fixture(tmp_path: Path) -> None:
    config = _config(tmp_path)
    _write_complete_fixture(tmp_path)
    run_client_os_scaffold(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
        profile="full",
    )

    result = run_client_os_preflight(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
        profile="full",
    )

    assert result.ok is True


def test_client_os_scaffold_refuses_overwrite(tmp_path: Path) -> None:
    config = _config(tmp_path)
    _write_complete_fixture(tmp_path)
    run_client_os_scaffold(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
    )

    with pytest.raises(ClientOsError, match="refusing to overwrite"):
        run_client_os_scaffold(
            config=config,
            client="greg-thegrantapp",
            engagement="case-study-sprint",
            meeting_date="2026-05-08",
        )


def test_client_os_status_returns_text_and_json(tmp_path: Path) -> None:
    config = _config(tmp_path)
    _write_complete_fixture(tmp_path)
    run_client_os_scaffold(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
        profile="full",
    )

    result = run_client_os_status(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
        profile="full",
    )

    data = result.to_dict(tmp_path)
    assert result.ok is True
    assert data["ready_for_meeting"] is True
    assert data["profile"] == "full"

    cli_result = CliRunner().invoke(
        app,
        [
            "practice",
            "client-os",
            "status",
            "greg-thegrantapp",
            "--engagement",
            "case-study-sprint",
            "--date",
            "2026-05-08",
            "--profile",
            "full",
            "--json",
        ],
        env={"DTP_HOME": str(tmp_path)},
    )
    assert cli_result.exit_code == 0
    assert '"ready_for_meeting": true' in cli_result.output


def test_client_os_closeout_fails_pending_receipt_rows(tmp_path: Path) -> None:
    config = _config(tmp_path)
    _write_complete_fixture(tmp_path)
    run_client_os_scaffold(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
        profile="full",
    )

    result = run_client_os_closeout(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
    )

    assert result.ok is False
    assert any(
        check.severity == "blocker" and "receipt row pending" in check.message
        for check in result.checks
    )


def test_client_os_closeout_passes_completed_receipt(tmp_path: Path) -> None:
    config = _config(tmp_path)
    root = _write_complete_fixture(tmp_path)
    run_client_os_scaffold(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
        profile="full",
    )
    receipt = root / "post-meeting-receipt-2026-05-08.md"
    receipt.write_text(_completed_receipt(), encoding="utf-8")

    result = run_client_os_closeout(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
    )

    assert result.ok is True


def test_client_os_bridge_export_blocks_unsafe_rows(tmp_path: Path) -> None:
    config = _config(tmp_path)
    root = _write_complete_fixture(tmp_path)
    run_client_os_scaffold(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
        profile="infra",
    )
    (root / "bridge-queue-2026-05-08.md").write_text(
        _bridge_queue(
            "| Gmail | Draft follow-up | status-only next action |  | internal_only | low | ready |"
        ),
        encoding="utf-8",
    )

    result = run_client_os_bridge_export(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
    )

    assert result.ok is False
    assert any(
        check.severity == "blocker" and "missing manual reviewer" in check.message
        for check in result.checks
    )


def test_client_os_bridge_export_passes_safe_dry_run_rows(tmp_path: Path) -> None:
    config = _config(tmp_path)
    root = _write_complete_fixture(tmp_path)
    run_client_os_scaffold(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
        profile="infra",
    )
    (root / "bridge-queue-2026-05-08.md").write_text(
        _bridge_queue(
            "| Gmail | Draft follow-up | status-only next action | Toni | "
            "internal_only | low | ready |"
        ),
        encoding="utf-8",
    )

    result = run_client_os_bridge_export(
        config=config,
        client="greg-thegrantapp",
        engagement="case-study-sprint",
        meeting_date="2026-05-08",
    )

    assert result.ok is True
    assert len(result.rows) == 1


def test_client_os_cli_help_lists_commands() -> None:
    result = CliRunner().invoke(app, ["practice", "client-os", "--help"])

    assert result.exit_code == 0
    assert "bridge-export" in result.output
    assert "closeout" in result.output
    assert "preflight" in result.output
    assert "scaffold" in result.output
    assert "status" in result.output


def _write_complete_fixture(root: Path) -> Path:
    client_root = root / "engagements" / "greg-thegrantapp"
    engagement_root = client_root / "case-study-sprint"
    engagement_root.mkdir(parents=True)
    (client_root / "consent.md").write_text(
        "# Consent\n\n- internal_only until written permission is captured\n",
        encoding="utf-8",
    )
    (engagement_root / "client-os-pilot-2026-05-08.md").write_text(
        "\n".join(
            [
                "# Greg Client OS Pilot",
                "",
                "## Pilot Metadata",
                "",
                "- Automation authority: draft-only",
                "",
                "## Source Index",
                "",
                "| Source | Location | Freshness | Allowed use | Blocked use |",
                "|---|---|---|---|---|",
                (
                    "| Discovery prep | discovery-session-prep.md | current | "
                    "meeting prep | public proof |"
                ),
                "",
                "## Meeting Intent",
                "",
                "- Clarify launch readiness.",
                "",
                "## Permission And Privacy Notes",
                "",
                "- Proof permission: pending written confirmation.",
                "",
                "## Draft-Only Automation",
                "",
                "- Allowed: notes and drafts.",
                "",
                "## Open Loops",
                "",
                "| Loop | Owner | Gate | Due/review trigger | Status |",
                "|---|---|---|---|---|",
                "| Permission | Greg | written confirmation | post-call | pending |",
                "",
                "## Next-Action Packet",
                "",
                "- Toni next action: run the meeting.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return engagement_root


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


def _completed_receipt() -> str:
    return "\n".join(
        [
            "# Post-Meeting Receipt - 2026-05-08",
            "",
            "## Required Updates",
            "",
            "| Artifact | Updated? | Notes |",
            "|---|---|---|",
            "| meeting-notes-2026-05-08.md | complete | captured |",
            "| action-extraction.md | complete | captured |",
            "| owner-action-items.md | complete | captured |",
            "| source-material-index.md | complete | captured |",
            "| consent.md | not_applicable | no proof approval captured |",
            "| diagnose.md | complete | captured |",
            "| plan.md | complete | captured |",
            "| decision-log.md | complete | captured |",
            "| proof/* | blocked | proof gate remains blocked |",
            "",
        ]
    )


def _bridge_queue(row: str) -> str:
    return "\n".join(
        [
            "# Bridge Queue - 2026-05-08",
            "",
            "## Bridge Queue",
            "",
            (
                "| Surface | Candidate action | Payload summary | Reviewer | "
                "Permission gate | Risk | Status |"
            ),
            "|---|---|---|---|---|---|---|",
            row,
            "",
        ]
    )
