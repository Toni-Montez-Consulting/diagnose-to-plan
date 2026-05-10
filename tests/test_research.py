from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from dtp.cli import app
from dtp.commands.evolution import run_evolution_new
from dtp.commands.kaizen import run_kaizen_capture
from dtp.commands.research import render_research_steward_review, run_research_steward_review
from dtp.config import DtpConfig


def test_research_steward_recommends_patterns_kaizen_and_digests(tmp_path: Path) -> None:
    config = _config(tmp_path)
    run_evolution_new(
        config,
        title="Status visibility prevents lightweight capture drift",
        kind="research-pattern",
        state="draft",
    )
    run_kaizen_capture(
        config,
        "Harvey MCP could matter for future legal-work research.",
        status="inbox",
        item_type="research",
        repo="diagnose-to-plan",
        sensitivity="internal-only",
        tags=("legal-mcp",),
    )
    digest_dir = tmp_path / "practice-os" / "research" / "digests"
    digest_dir.mkdir(parents=True)
    digest_path = digest_dir / "2026-05-10-ai-operating-shift.md"
    digest_path.write_text(
        "# Research Arm Digest - AI operating shift\n\n"
        "Status: draft\n\n"
        "## Digest Summary\n\n"
        "A draft digest that still needs source and approval review.\n",
        encoding="utf-8",
        newline="\n",
    )

    result = run_research_steward_review(config, limit=10)
    rendered = render_research_steward_review(result, tmp_path)

    assert result.pattern_candidate_count == 1
    assert result.kaizen_count == 1
    assert result.digest_count == 1
    assert "Research Steward Review" in rendered
    assert "mode: read-only recommendation" in rendered
    assert "Status visibility prevents lightweight capture drift" in rendered
    assert "complete evidence limits" in rendered
    assert "Harvey MCP could matter" in rendered
    assert "classify into digest, radar item, spike, pattern candidate, or park" in rendered
    assert "Research Arm Digest - AI operating shift" in rendered
    assert "finish sources, hype filter" in rendered
    assert "cannot authorize public claims" in rendered
    assert "docs/RESEARCH_ARM_V0.md" in rendered


def test_research_steward_cli_outputs_recommendations(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    runner = CliRunner()

    runner.invoke(
        app,
        [
            "evolution",
            "new",
            "Research signal should become a pattern",
            "--kind",
            "research-pattern",
        ],
    )
    result = runner.invoke(app, ["research", "steward", "--limit", "1"])

    assert result.exit_code == 0
    assert "Research Steward Review" in result.output
    assert "Research signal should become a pattern" in result.output
    assert "read-only recommendation" in result.output


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
