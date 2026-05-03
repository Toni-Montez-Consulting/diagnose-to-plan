from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from dtp.cli import app
from dtp.commands.memory import render_memory_status, run_memory_status
from dtp.config import load_config


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
