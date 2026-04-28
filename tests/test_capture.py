from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import frontmatter

from dtp.capture import append_note, create_mentor_log, create_story
from dtp.config import DtpConfig


def test_append_note_creates_daily_journal(tmp_path: Path) -> None:
    config = _config(tmp_path)

    result = append_note(
        "Talked through the builder wedge.",
        config,
        tags=("builder", "sales"),
        clock=lambda: datetime(2026, 4, 28, 9, 8, 7, tzinfo=UTC),
    )

    assert result.relative_path == "journal/2026/04/2026-04-28.md"
    assert result.path.read_text(encoding="utf-8") == (
        "09:08:07 — Talked through the builder wedge. [tags: builder, sales]\n"
    )


def test_create_story_writes_template_with_frontmatter(tmp_path: Path) -> None:
    config = _config(tmp_path)
    source = tmp_path / "inputs" / "omnexus-chat.md"
    source.parent.mkdir(parents=True)
    source.write_text("app review notes", encoding="utf-8")

    result = create_story(
        "App Store Pressure",
        config,
        source=source,
        clock=lambda: datetime(2026, 4, 28, 12, 0, 0, tzinfo=UTC),
    )

    post = frontmatter.load(result.path)
    assert result.relative_path == "omnexus/stories/2026-04-28-app-store-pressure.md"
    assert post["command"] == "story"
    assert post["created"] == "2026-04-28T12:00:00Z"
    assert post["inputs"] == ["inputs/omnexus-chat.md"]
    assert post["confidential"] is False
    assert "## Situation" in post.content
    assert "## Lesson" in post.content
    assert "inputs/omnexus-chat.md" in post.content


def test_create_mentor_log_writes_template_with_frontmatter(tmp_path: Path) -> None:
    config = _config(tmp_path)

    result = create_mentor_log(
        "Should I productize the audit?",
        config,
        mentor="Operator Mentor",
        clock=lambda: datetime(2026, 4, 28, 13, 0, 0, tzinfo=UTC),
    )

    post = frontmatter.load(result.path)
    assert result.relative_path == "mentor-log/2026-04-28-should-i-productize-the-audit.md"
    assert post["command"] == "mentor"
    assert post["mentor"] == "Operator Mentor"
    assert post["topic"] == "Should I productize the audit?"
    assert "## Recommendation" in post.content
    assert "## Follow-up" in post.content


def _config(root: Path) -> DtpConfig:
    return DtpConfig(
        repo_root=root,
        inputs_dir=root / "inputs",
        outputs_dir=root / "outputs",
        skills_dir=root / "skills",
        workspace_file=root / ".dtp" / "workspace.yaml",
    )
