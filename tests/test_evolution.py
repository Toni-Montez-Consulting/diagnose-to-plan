from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import pytest
from typer.testing import CliRunner

from dtp.cli import app
from dtp.commands.evolution import (
    EvolutionError,
    render_evolution_new,
    render_evolution_status,
    run_evolution_new,
    run_evolution_status,
)
from dtp.commands.kaizen import run_kaizen_capture
from dtp.config import DtpConfig


def test_evolution_new_creates_idea_record(tmp_path: Path) -> None:
    config = _config(tmp_path)

    result = run_evolution_new(
        config,
        title="Keep a working ledger during strategy threads",
        created_at=datetime(2026, 5, 10, 12, 0, tzinfo=UTC),
    )

    assert result.kind == "idea"
    assert result.path == (
        tmp_path
        / "practice-os"
        / "evolution"
        / "records"
        / "2026-05-10-keep-a-working-ledger-during-strategy-threads.md"
    )
    text = result.path.read_text(encoding="utf-8")
    assert "# Idea Evolution Record - Keep a working ledger during strategy threads" in text
    assert "- Current state: raw_capture" in text
    assert "Raw capture is not reusable playbook memory" in text
    assert "evolution draft created" in render_evolution_new(result, tmp_path)


def test_evolution_new_can_seed_from_kaizen_record(tmp_path: Path) -> None:
    config = _config(tmp_path)
    captured = run_kaizen_capture(
        config,
        "Messaging idea: explain owner bottlenecks before tools.",
        item_type="idea",
        status="done",
        sensitivity="internal-only",
        source="gmail",
        tags=("messaging",),
        captured_at=datetime(2026, 5, 10, 11, 0, tzinfo=UTC),
    )

    result = run_evolution_new(
        config,
        from_kaizen=captured.record.id,
        created_at=datetime(2026, 5, 10, 12, 0, tzinfo=UTC),
    )

    text = result.path.read_text(encoding="utf-8")
    assert f"- Source Kaizen id: {captured.record.id}" in text
    assert "- Source: gmail" in text
    assert "- Tags: messaging" in text
    assert "Messaging idea: explain owner bottlenecks before tools." in text


def test_evolution_new_creates_research_pattern_candidate(tmp_path: Path) -> None:
    config = _config(tmp_path)

    result = run_evolution_new(
        config,
        title="Owners buy clarity before automation",
        kind="research-pattern",
        source="field-note",
        created_at=datetime(2026, 5, 10, 12, 0, tzinfo=UTC),
    )

    assert result.path == (
        tmp_path
        / "practice-os"
        / "research"
        / "pattern-candidates"
        / "2026-05-10-owners-buy-clarity-before-automation.md"
    )
    text = result.path.read_text(encoding="utf-8")
    assert "# Research Pattern Candidate - Owners buy clarity before automation" in text
    assert "- Status: draft" in text
    assert "## Consulting Translation" in text


def test_evolution_status_counts_records(tmp_path: Path) -> None:
    config = _config(tmp_path)
    run_evolution_new(
        config,
        title="Ledger pattern",
        created_at=datetime(2026, 5, 10, 12, 0, tzinfo=UTC),
    )
    run_evolution_new(
        config,
        title="Field observation",
        kind="research-pattern",
        created_at=datetime(2026, 5, 10, 12, 1, tzinfo=UTC),
    )

    status = run_evolution_status(config)
    rendered = render_evolution_status(status, tmp_path)

    assert len(status.idea_records) == 1
    assert len(status.research_candidates) == 1
    assert status.state_counts == {"draft": 1, "raw_capture": 1}
    assert "Practice Evolution Status" in rendered
    assert "idea_records=1" in rendered
    assert "research_candidates=1" in rendered


def test_evolution_rejects_unknown_kind_and_state(tmp_path: Path) -> None:
    config = _config(tmp_path)

    with pytest.raises(EvolutionError, match="unknown evolution kind"):
        run_evolution_new(config, title="Bad kind", kind="weird")

    with pytest.raises(EvolutionError, match="unknown idea evolution state"):
        run_evolution_new(config, title="Bad state", state="approved")

    with pytest.raises(EvolutionError, match="unknown research pattern state"):
        run_evolution_new(
            config,
            title="Bad research state",
            kind="research-pattern",
            state="raw_capture",
        )


def test_evolution_cli_new_and_status(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    runner = CliRunner()

    created = runner.invoke(app, ["evolution", "new", "Do the useful thing again"])
    status = runner.invoke(app, ["evolution", "status"])

    assert created.exit_code == 0
    assert "evolution draft created" in created.output
    assert status.exit_code == 0
    assert "Practice Evolution Status" in status.output
    assert "idea_records=1" in status.output


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
