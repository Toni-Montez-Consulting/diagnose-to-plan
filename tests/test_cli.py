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
    assert "validated 3 skills" in result.output
