from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

import frontmatter

from dtp.config import DtpConfig
from dtp.git_safety import resolve_inside_repo

Clock = Callable[[], datetime]


@dataclass(frozen=True)
class CaptureResult:
    path: Path
    relative_path: str


def append_note(
    text: str,
    config: DtpConfig,
    *,
    tags: tuple[str, ...] = (),
    clock: Clock | None = None,
) -> CaptureResult:
    now = (clock or _local_now)()
    destination = (
        config.repo_root
        / "journal"
        / now.strftime("%Y")
        / now.strftime("%m")
        / f"{now.strftime('%Y-%m-%d')}.md"
    )
    resolve_inside_repo(destination, config.repo_root)
    destination.parent.mkdir(parents=True, exist_ok=True)

    suffix = f" [tags: {', '.join(tags)}]" if tags else ""
    with destination.open("a", encoding="utf-8") as handle:
        handle.write(f"{now.strftime('%H:%M:%S')} — {text}{suffix}\n")

    return _capture_result(destination, config)


def create_story(
    title: str,
    config: DtpConfig,
    *,
    source: Path | None = None,
    clock: Clock | None = None,
) -> CaptureResult:
    now = (clock or _local_now)()
    source_path = _optional_source(source, config)
    destination = (
        config.repo_root
        / "omnexus"
        / "stories"
        / f"{now.strftime('%Y-%m-%d')}-{slugify(title)}.md"
    )
    resolve_inside_repo(destination, config.repo_root)
    destination.parent.mkdir(parents=True, exist_ok=True)

    metadata = _capture_metadata(
        command="story",
        created=now,
        inputs=_relative_inputs(config, source_path),
    ) | {"title": title}
    destination.write_text(
        render_markdown_with_frontmatter(metadata, _story_template(title, source_path, config)),
        encoding="utf-8",
    )
    return _capture_result(destination, config)


def create_mentor_log(
    what: str,
    config: DtpConfig,
    *,
    mentor: str | None = None,
    source: Path | None = None,
    clock: Clock | None = None,
) -> CaptureResult:
    now = (clock or _local_now)()
    source_path = _optional_source(source, config)
    destination = (
        config.repo_root / "mentor-log" / f"{now.strftime('%Y-%m-%d')}-{slugify(what)}.md"
    )
    resolve_inside_repo(destination, config.repo_root)
    destination.parent.mkdir(parents=True, exist_ok=True)

    metadata = _capture_metadata(
        command="mentor",
        created=now,
        inputs=_relative_inputs(config, source_path),
    ) | {"mentor": mentor or "", "topic": what}
    body = _mentor_template(what, mentor, source_path, config)
    destination.write_text(
        render_markdown_with_frontmatter(metadata, body),
        encoding="utf-8",
    )
    return _capture_result(destination, config)


def render_markdown_with_frontmatter(metadata: dict[str, object], body: str) -> str:
    rendered = frontmatter.dumps(
        frontmatter.Post(body.rstrip() + "\n", **metadata),
        sort_keys=False,
    )
    return rendered if rendered.endswith("\n") else f"{rendered}\n"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "capture"


def _capture_metadata(*, command: str, created: datetime, inputs: list[str]) -> dict[str, object]:
    return {
        "created": _timestamp(created),
        "command": command,
        "inputs": inputs,
        "confidential": False,
        "client": "",
    }


def _story_template(title: str, source_path: Path | None, config: DtpConfig) -> str:
    return "\n".join(
        [
            f"# {title}",
            "",
            "## Situation",
            "",
            "TODO",
            "",
            "## Decision",
            "",
            "TODO",
            "",
            "## Outcome",
            "",
            "TODO",
            "",
            "## Lesson",
            "",
            "TODO",
            "",
            *_source_lines(source_path, config),
        ]
    )


def _mentor_template(
    what: str,
    mentor: str | None,
    source_path: Path | None,
    config: DtpConfig,
) -> str:
    mentor_line = mentor or "Toni"
    return "\n".join(
        [
            f"# {what}",
            "",
            f"Mentor: {mentor_line}",
            "",
            "## Ask",
            "",
            what,
            "",
            "## Context",
            "",
            "TODO",
            "",
            "## Recommendation",
            "",
            "TODO",
            "",
            "## Decision",
            "",
            "TODO",
            "",
            "## Follow-up",
            "",
            "TODO",
            "",
            *_source_lines(source_path, config),
        ]
    )


def _source_lines(source_path: Path | None, config: DtpConfig) -> list[str]:
    if source_path is None:
        return []
    relative = source_path.relative_to(config.repo_root).as_posix()
    return ["## Source", "", relative, ""]


def _optional_source(source: Path | None, config: DtpConfig) -> Path | None:
    if source is None:
        return None
    source_path = resolve_inside_repo(source, config.repo_root)
    if not source_path.exists():
        raise FileNotFoundError(source_path)
    return source_path


def _relative_inputs(config: DtpConfig, source_path: Path | None) -> list[str]:
    if source_path is None:
        return []
    return [source_path.relative_to(config.repo_root).as_posix()]


def _capture_result(destination: Path, config: DtpConfig) -> CaptureResult:
    return CaptureResult(
        path=destination,
        relative_path=destination.relative_to(config.repo_root).as_posix(),
    )


def _timestamp(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=UTC)
    return value.astimezone(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def _local_now() -> datetime:
    return datetime.now().astimezone()
