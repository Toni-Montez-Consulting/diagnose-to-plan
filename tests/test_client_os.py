from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from dtp.cli import app
from dtp.commands.client_os import (
    ClientOsError,
    run_client_os_preflight,
    run_client_os_scaffold,
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


def test_client_os_cli_help_lists_commands() -> None:
    result = CliRunner().invoke(app, ["practice", "client-os", "--help"])

    assert result.exit_code == 0
    assert "preflight" in result.output
    assert "scaffold" in result.output


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
