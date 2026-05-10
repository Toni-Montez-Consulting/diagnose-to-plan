from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from dtp.cli import app
from dtp.commands.evolution import run_evolution_new
from dtp.commands.kaizen import run_kaizen_capture
from dtp.commands.memory import (
    render_memory_status,
    render_memory_steward_review,
    run_memory_status,
    run_memory_steward_review,
)
from dtp.config import DtpConfig, load_config


def test_memory_status_requires_spine_docs_and_templates(repo_root: Path) -> None:
    result = run_memory_status(load_config(repo_root))
    text = render_memory_status(result, repo_root)

    assert result.ok is True
    assert "doc PRACTICE_MEMORY_CONTROL_PLANE.md" in text
    assert "template session-rehydration-checklist.md" in text
    assert "template correction-checklist-for-toni.md" in text
    assert "DTP is authoritative" in text
    assert "Notion is an inbox/mirror" in text


def test_memory_status_cli_outputs_text(repo_root: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(repo_root))

    result = CliRunner().invoke(app, ["memory", "status"])

    assert result.exit_code == 0
    assert "memory spine: ok" in result.output
    assert "recent receipts:" in result.output


def test_memory_steward_recommends_evolution_and_kaizen_items(tmp_path: Path) -> None:
    config = _config(tmp_path)
    run_evolution_new(
        config,
        title="Practice Evolution status dashboard V0",
        state="working_memory",
    )
    run_evolution_new(
        config,
        title="Review room later",
        state="parked",
    )
    run_kaizen_capture(
        config,
        "Inbox idea should be triaged.",
        status="inbox",
        item_type="idea",
        repo="diagnose-to-plan",
        sensitivity="internal-only",
    )

    result = run_memory_steward_review(config, limit=10)
    rendered = render_memory_steward_review(result, tmp_path)

    assert result.evolution_count == 1
    assert result.kaizen_count == 1
    assert "Memory Steward Review" in rendered
    assert "mode: read-only recommendation" in rendered
    assert "Practice Evolution status dashboard V0" in rendered
    assert "review after one more use" in rendered
    assert "Inbox idea should be triaged." in rendered
    assert "triage into now, next, waiting, parked, or evolution record" in rendered
    assert "docs/practice-evolution-dashboard.html" in rendered
    assert "do not promote memory automatically" in rendered


def test_memory_steward_cli_outputs_recommendations(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    runner = CliRunner()

    runner.invoke(app, ["evolution", "new", "Do the useful thing again"])
    result = runner.invoke(app, ["memory", "steward", "--limit", "1"])

    assert result.exit_code == 0
    assert "Memory Steward Review" in result.output
    assert "Do the useful thing again" in result.output


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
