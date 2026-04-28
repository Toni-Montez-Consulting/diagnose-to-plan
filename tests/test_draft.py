from __future__ import annotations

from datetime import UTC, datetime
from io import StringIO
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


def test_run_draft_warns_when_real_input_loads_todo_skills(repo_root: Path) -> None:
    config = load_config(repo_root)
    source = repo_root / "inputs" / "warning-real.md"
    destination = repo_root / "outputs" / "warning-real.md"
    stderr = StringIO()
    source.write_text("# Diagnose\n\nA real client note.", encoding="utf-8")
    if destination.exists():
        destination.unlink()

    try:
        run_draft(
            source,
            config,
            out=destination,
            stderr=stderr,
        )
    finally:
        source.unlink(missing_ok=True)

    assert stderr.getvalue() == (
        "WARNING: skills with TODO bodies were loaded — output will lack practice-specific "
        "voice/pricing/structure. Author skill bodies before using output for client work.\n"
    )


def test_run_draft_suppresses_todo_warning_for_fixture(repo_root: Path) -> None:
    config = load_config(repo_root)
    destination = repo_root / "outputs" / "fixture-warning-check.md"
    stderr = StringIO()
    if destination.exists():
        destination.unlink()

    run_draft(
        repo_root / "inputs" / "fixture-diagnose.md",
        config,
        out=destination,
        stderr=stderr,
    )

    assert stderr.getvalue() == ""
