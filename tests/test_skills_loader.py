from __future__ import annotations

from pathlib import Path

import pytest

from dtp.skills_loader import (
    SkillValidationError,
    load_required_skills,
    load_skill,
    validate_skills,
)


def test_validate_placeholder_skills(repo_root: Path) -> None:
    skills = validate_skills(repo_root / "skills")

    assert [skill.name for skill in skills] == ["build-patterns", "pricing", "sow", "voice"]


def test_load_required_skills_preserves_requested_order(repo_root: Path) -> None:
    skills = load_required_skills(
        repo_root / "skills",
        ("voice", "pricing", "sow", "build-patterns"),
    )

    assert [skill.name for skill in skills] == ["voice", "pricing", "sow", "build-patterns"]


def test_invalid_skill_reports_diagnostic(tmp_path: Path) -> None:
    path = tmp_path / "SKILL.md"
    path.write_text("no frontmatter", encoding="utf-8")

    with pytest.raises(SkillValidationError):
        load_skill(path)
