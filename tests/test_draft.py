from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from dtp.commands.draft import run_draft
from dtp.config import load_config


def test_run_draft_writes_sow_with_frontmatter(repo_root: Path) -> None:
    config = load_config(repo_root)
    destination = repo_root / "outputs" / "test-draft.md"
    if destination.exists():
        destination.unlink()

    result = run_draft(
        repo_root / "inputs" / "fixture-diagnose.md",
        config,
        out=destination,
        clock=lambda: datetime(2026, 4, 28, 12, 0, 0, tzinfo=UTC),
    )

    text = result.read_text(encoding="utf-8")
    assert result == destination
    assert "coi_verdict: not_run_phase1" in text
    assert "model: claude-sonnet-4-6" in text
    assert "  - voice" in text
    assert "  - pricing" in text
    assert "  - sow" in text
    assert "## Scope" in text
    assert "## Deliverables" in text
    assert "## Pricing" in text


def test_run_draft_supports_skip_coi(repo_root: Path) -> None:
    config = load_config(repo_root)
    destination = repo_root / "outputs" / "test-draft-skip.md"
    if destination.exists():
        destination.unlink()

    run_draft(
        repo_root / "inputs" / "fixture-diagnose.md",
        config,
        skip_coi=True,
        out=destination,
    )

    assert "coi_verdict: skipped" in destination.read_text(encoding="utf-8")
