from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_copy_authenticity_scan_is_advisory_by_default(tmp_path: Path, repo_root: Path) -> None:
    path = tmp_path / "copy.md"
    path.write_text("We unlock AI-powered transformation.\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(repo_root / "scripts" / "copy_authenticity_scan.py"), str(path)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "review recommended" in result.stdout
    assert "AI-powered" in result.stdout


def test_copy_authenticity_scan_strict_fails_on_findings(
    tmp_path: Path, repo_root: Path
) -> None:
    path = tmp_path / "copy.md"
    path.write_text("This is a future-proof system.\n", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(repo_root / "scripts" / "copy_authenticity_scan.py"),
            str(path),
            "--strict",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 1
    assert "future-proof" in result.stdout

