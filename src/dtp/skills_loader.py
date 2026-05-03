from __future__ import annotations

from pathlib import Path
from typing import TextIO

from pydantic import BaseModel, ConfigDict

TODO_SKILL_BODY = "# TODO: Toni authors this skill"
TODO_SKILL_WARNING = (
    "WARNING: skills with TODO bodies were loaded — output will lack practice-specific "
    "voice/pricing/structure. Author skill bodies before using output for client work."
)


class Skill(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str
    description: str
    path: Path
    body: str


class SkillValidationError(ValueError):
    pass


def load_skill(path: Path) -> Skill:
    metadata, body = _split_frontmatter(path)
    name = metadata.get("name", "").strip()
    description = metadata.get("description", "").strip()

    problems: list[str] = []
    if not name:
        problems.append("missing frontmatter field: name")
    if not description:
        problems.append("missing frontmatter field: description")
    if not body.strip():
        problems.append("missing skill body")

    if problems:
        joined = "; ".join(problems)
        raise SkillValidationError(f"{path}: {joined}")

    return Skill(name=name, description=description, path=path, body=body.strip())


def discover_skills(skills_dir: Path) -> tuple[Skill, ...]:
    if not skills_dir.exists():
        return ()
    skill_paths = sorted(skills_dir.glob("*/SKILL.md"))
    return tuple(load_skill(path) for path in skill_paths)


def load_required_skills(skills_dir: Path, names: tuple[str, ...]) -> tuple[Skill, ...]:
    loaded = {skill.name: skill for skill in discover_skills(skills_dir)}
    missing = [name for name in names if name not in loaded]
    if missing:
        raise SkillValidationError(f"missing required skills: {', '.join(missing)}")
    return tuple(loaded[name] for name in names)


def validate_skills(skills_dir: Path) -> tuple[Skill, ...]:
    return discover_skills(skills_dir)


def skills_with_todo_bodies(skills: tuple[Skill, ...]) -> tuple[Skill, ...]:
    return tuple(skill for skill in skills if skill.body.strip() == TODO_SKILL_BODY)


def warn_if_todo_skills_loaded(
    skills: tuple[Skill, ...],
    *,
    input_path: Path,
    repo_root: Path,
    stderr: TextIO,
) -> None:
    if not skills_with_todo_bodies(skills):
        return
    if _is_fixture_input(input_path=input_path, repo_root=repo_root):
        return
    stderr.write(f"{TODO_SKILL_WARNING}\n")


def _split_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise SkillValidationError(f"{path}: missing YAML frontmatter")

    end = text.find("\n---", 4)
    if end == -1:
        raise SkillValidationError(f"{path}: unclosed YAML frontmatter")

    raw_metadata = text[4:end]
    body = text[end + 4 :].strip()
    metadata: dict[str, str] = {}
    for line in raw_metadata.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise SkillValidationError(f"{path}: invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"')
    return metadata, body


def _is_fixture_input(*, input_path: Path, repo_root: Path) -> bool:
    try:
        relative = input_path.resolve().relative_to(repo_root.resolve())
    except ValueError:
        return False
    return relative.as_posix() == "inputs/fixture-diagnose.md"
