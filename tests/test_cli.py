from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from typer.testing import CliRunner

from dtp.cli import app


def test_cli_help() -> None:
    result = CliRunner().invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "draft" in result.output
    assert "note" in result.output
    assert "story" in result.output
    assert "mentor" in result.output
    assert "index" in result.output
    assert "detect" in result.output
    assert "lesson" in result.output
    assert "recall" in result.output
    assert "synthesize" in result.output
    assert "kit" in result.output
    assert "redact" in result.output
    assert "practice" in result.output
    assert "kaizen" in result.output
    assert "evolution" in result.output
    assert "research" in result.output
    assert "vault" in result.output
    assert "workspace" in result.output
    assert "web" in result.output


def test_python_module_help(repo_root: Path) -> None:
    result = subprocess.run(
        [sys.executable, "-m", "dtp", "--help"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "skills" in result.stdout


def test_skills_validate_command() -> None:
    result = CliRunner().invoke(app, ["skills", "--validate"])

    assert result.exit_code == 0
    assert "validated 4 skills" in result.output


def test_practice_source_packs_validate_command() -> None:
    result = CliRunner().invoke(app, ["practice", "source-packs", "validate"])

    assert result.exit_code == 0
    assert "source-pack validation: ok" in result.output
    assert "source pack packs validated: 7" in result.output


def test_draft_accepts_output_alias(repo_root: Path) -> None:
    destination = repo_root / "outputs" / "cli-output-alias.md"
    if destination.exists():
        destination.unlink()

    result = CliRunner().invoke(
        app,
        [
            "draft",
            str(repo_root / "inputs" / "fixture-diagnose.md"),
            "--output",
            str(destination),
        ],
    )

    assert result.exit_code == 0
    assert destination.exists()
    assert "wrote outputs" in result.output


def test_note_command_writes_under_dtp_home(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))

    result = CliRunner().invoke(app, ["note", "Capture the sales call.", "--tag", "sales"])

    assert result.exit_code == 0
    assert "wrote journal/" in result.output
    journal_files = list((tmp_path / "journal").rglob("*.md"))
    assert len(journal_files) == 1
    assert "Capture the sales call. [tags: sales]" in journal_files[0].read_text(
        encoding="utf-8"
    )


def test_index_invalid_repo_exits_1(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    (tmp_path / ".dtp").mkdir()
    (tmp_path / ".dtp" / "workspace.yaml").write_text("repos:\n", encoding="utf-8")

    result = CliRunner().invoke(app, ["index", "missing-repo"])

    assert result.exit_code == 1
    assert "unknown repo" in result.output
