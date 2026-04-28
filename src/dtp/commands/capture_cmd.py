from __future__ import annotations

from pathlib import Path

from dtp.capture import CaptureResult, append_note, create_mentor_log, create_story
from dtp.config import DtpConfig


def run_note(
    text: str,
    config: DtpConfig,
    *,
    tags: tuple[str, ...] = (),
) -> CaptureResult:
    return append_note(text, config, tags=tags)


def run_story(
    title: str,
    config: DtpConfig,
    *,
    source: Path | None = None,
) -> CaptureResult:
    return create_story(title, config, source=source)


def run_mentor(
    what: str,
    config: DtpConfig,
    *,
    mentor: str | None = None,
    source: Path | None = None,
) -> CaptureResult:
    return create_mentor_log(what, config, mentor=mentor, source=source)
