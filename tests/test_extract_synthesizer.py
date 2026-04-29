from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

import frontmatter
import pytest

from dtp.capture import render_markdown_with_frontmatter
from dtp.config import DtpConfig
from dtp.extract.indexer import ExtractError
from dtp.extract.synthesizer import synthesize


def test_synthesizer_groups_patterns_and_lessons(tmp_path: Path) -> None:
    config = _config(tmp_path)
    patterns = config.extracts_dir / "patterns"
    lessons = config.extracts_dir / "lessons"
    patterns.mkdir(parents=True)
    lessons.mkdir(parents=True)
    (patterns / "consulting--admin-command-room.md").write_text(
        render_markdown_with_frontmatter(
            {
                "repo": "consulting",
                "signal": "admin-surface",
                "pattern_slug": "admin-command-room",
                "confidence": "low",
                "files_read": ["src/pages/admin.astro"],
                "promoted": False,
            },
            "# Admin Command Room\n\nPublic command room outside, private Hub inside.",
        ),
        encoding="utf-8",
    )
    (patterns / "hub--admin-console.md").write_text(
        render_markdown_with_frontmatter(
            {
                "repo": "hub",
                "signal": "admin-surface",
                "pattern_slug": "admin-console",
                "confidence": "medium",
                "files_read": ["api/console/dashboard.ts", "apps/web/src/App.tsx"],
                "promoted": False,
            },
            "# Admin Console\n\nProtected console for private records.",
        ),
        encoding="utf-8",
    )
    (lessons / "consulting--2026-04-28-admin-surface.md").write_text(
        render_markdown_with_frontmatter(
            {
                "repo": "consulting",
                "pattern": "admin-surface",
                "type": "lesson",
                "created": "2026-04-28T12:00:00Z",
            },
            "# Consulting Admin Lesson\n\nKeep private rows in Hub.",
        ),
        encoding="utf-8",
    )

    (result,) = synthesize(
        config=config,
        no_confirm=True,
        clock=datetime(2026, 4, 29, 12, 0, 0, tzinfo=UTC),
    )

    post = frontmatter.load(result.path)
    assert result.group == "admin-surface"
    assert result.source_count == 3
    assert result.canonical_repo == "consulting"
    assert post.metadata["group"] == "admin-surface"
    assert post.metadata["canonical_repo"] == "consulting"
    assert post.metadata["source_types"] == ["lesson", "pattern"]
    assert post.metadata["private_review_required"] is True
    assert post.metadata["promoted"] is False
    assert "extracts/patterns/consulting--admin-command-room.md" in post.content
    assert "public-safe command room" in post.content


def test_synthesizer_rejects_invalid_source_type(tmp_path: Path) -> None:
    with pytest.raises(ExtractError, match="invalid synthesize type"):
        synthesize(config=_config(tmp_path), kind="index")


def _config(root: Path) -> DtpConfig:
    return DtpConfig(
        repo_root=root,
        inputs_dir=root / "inputs",
        outputs_dir=root / "outputs",
        skills_dir=root / "skills",
        extracts_dir=root / "extracts",
        practice_os_dir=root / "practice-os",
        engagements_dir=root / "engagements",
        workspace_file=root / ".dtp" / "workspace.yaml",
        agent_enabled=False,
    )
