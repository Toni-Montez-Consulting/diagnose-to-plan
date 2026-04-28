from __future__ import annotations

import sys
from collections.abc import Callable
from datetime import UTC, datetime
from pathlib import Path
from typing import TextIO

from dtp.agent import AgentRequest, AgentRunner, run
from dtp.capture import render_markdown_with_frontmatter, slugify
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
        repo_root=config.repo_root,
    )
    body = run(request, runner=runner)
    now = (clock or _utc_now)()
    destination = _destination_path(
        input_path=source_path,
        config=config,
        client=client,
        out=out,
        now=now,
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    rendered = render_markdown_with_frontmatter(
        {
            "created": _created_at(now),
            "command": "draft",
            "inputs": [source_path.relative_to(config.repo_root).as_posix()],
            "coi_verdict": "skipped" if skip_coi else "not_run_phase1",
            "model": model,
            "skills_loaded": [skill.name for skill in skills],
            "source": source_path.relative_to(config.repo_root).as_posix(),
            "client": client or "",
            "confidential": False,
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
        slug = slugify(client)
        return config.repo_root / "clients" / slug / "sow.md"

    timestamp = now.strftime("%Y%m%d-%H%M%S")
    return config.outputs_dir / f"{timestamp}-{slugify(input_path.stem)}.md"


def _utc_now() -> datetime:
    return datetime.now(UTC)


def _created_at(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=UTC)
    return value.astimezone(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def user_facing_error(error: Exception) -> tuple[str, int]:
    if isinstance(error, SafetyAbort | SkillValidationError):
        return str(error), 2
    if isinstance(error, FileNotFoundError):
        return f"input not found: {error}", 1
    return str(error), 3
