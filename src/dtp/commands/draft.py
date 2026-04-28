from __future__ import annotations

import re
import sys
from collections.abc import Callable
from datetime import UTC, datetime
from pathlib import Path
from typing import TextIO

from dtp.agent import AgentRequest, AgentRunner, run
from dtp.config import DtpConfig
from dtp.git_safety import SafetyAbort, resolve_inside_repo
from dtp.models import DEEP_DRAFT_MODEL, DEFAULT_MODEL, PHASE1_DRAFT_SKILLS
from dtp.skills_loader import SkillValidationError, load_required_skills, warn_if_todo_skills_loaded

Clock = Callable[[], datetime]


def run_draft(
    input_path: Path,
    config: DtpConfig,
    *,
    client: str | None = None,
    deep: bool = False,
    skip_coi: bool = False,
    out: Path | None = None,
    runner: AgentRunner | None = None,
    clock: Clock | None = None,
    stderr: TextIO | None = None,
) -> Path:
    source_path = resolve_inside_repo(input_path, config.repo_root)
    if not source_path.exists():
        raise FileNotFoundError(source_path)

    skills = load_required_skills(config.skills_dir, PHASE1_DRAFT_SKILLS)
    warn_if_todo_skills_loaded(
        skills,
        input_path=source_path,
        repo_root=config.repo_root,
        stderr=stderr or sys.stderr,
    )
    model = DEEP_DRAFT_MODEL if deep else DEFAULT_MODEL
    request = AgentRequest(
        command="draft",
        input_text=source_path.read_text(encoding="utf-8"),
        model=model,
        skills=skills,
    )
    body = run(request, runner=runner)
    destination = _destination_path(
        input_path=source_path,
        config=config,
        client=client,
        out=out,
        now=(clock or _utc_now)(),
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    rendered = _with_frontmatter(
        {
            "coi_verdict": "skipped" if skip_coi else "not_run_phase1",
            "model": model,
            "skills_loaded": [skill.name for skill in skills],
            "source": source_path.relative_to(config.repo_root).as_posix(),
            "command": "draft",
        },
        body,
    )
    destination.write_text(rendered, encoding="utf-8")
    return destination


def _destination_path(
    *,
    input_path: Path,
    config: DtpConfig,
    client: str | None,
    out: Path | None,
    now: datetime,
) -> Path:
    if out is not None:
        return resolve_inside_repo(out, config.repo_root)
    if client:
        slug = _slug(client)
        return config.repo_root / "clients" / slug / "sow.md"

    timestamp = now.strftime("%Y%m%d-%H%M%S")
    return config.outputs_dir / f"{timestamp}-{_slug(input_path.stem)}.md"


def _with_frontmatter(metadata: dict[str, object], body: str) -> str:
    lines = ["---"]
    for key, value in metadata.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            lines.extend(f"  - {item}" for item in value)
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines) + "\n\n" + body.rstrip() + "\n"


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "draft"


def _utc_now() -> datetime:
    return datetime.now(UTC)


def user_facing_error(error: Exception) -> tuple[str, int]:
    if isinstance(error, SafetyAbort | SkillValidationError):
        return str(error), 2
    if isinstance(error, FileNotFoundError):
        return f"input not found: {error}", 1
    return str(error), 3
