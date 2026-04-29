from __future__ import annotations

import os
import subprocess
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field


class DtpConfig(BaseModel):
    """Runtime paths and switches for the local harness."""

    model_config = ConfigDict(frozen=True)

    repo_root: Path
    inputs_dir: Path = Field()
    outputs_dir: Path = Field()
    skills_dir: Path = Field()
    extracts_dir: Path = Field()
    practice_os_dir: Path = Field()
    engagements_dir: Path = Field()
    workspace_file: Path = Field()
    agent_enabled: bool = False


def load_config(repo_root: Path | None = None) -> DtpConfig:
    root = (repo_root or _env_repo_root() or find_repo_root()).resolve()
    agent_enabled = os.environ.get("DTP_ENABLE_AGENT", "").strip().lower() in {"1", "true", "yes"}
    return DtpConfig(
        repo_root=root,
        inputs_dir=root / "inputs",
        outputs_dir=root / "outputs",
        skills_dir=root / "skills",
        extracts_dir=root / "extracts",
        practice_os_dir=root / "practice-os",
        engagements_dir=root / "engagements",
        workspace_file=root / ".dtp" / "workspace.yaml",
        agent_enabled=agent_enabled,
    )


def find_repo_root(start: Path | None = None) -> Path:
    """Find the git root, falling back to the nearest pyproject directory."""

    cwd = (start or Path.cwd()).resolve()
    git_root = _git_root(cwd)
    if git_root is not None:
        return git_root

    for candidate in [cwd, *cwd.parents]:
        if (candidate / "pyproject.toml").exists():
            return candidate

    raise RuntimeError(f"Could not find dtp repo root from {cwd}")


def _env_repo_root() -> Path | None:
    value = os.environ.get("DTP_HOME")
    return Path(value).expanduser() if value else None


def _git_root(cwd: Path) -> Path | None:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=cwd,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return None
    text = result.stdout.strip()
    return Path(text) if text else None
