from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from dtp.config import DtpConfig
from dtp.skills_loader import SkillValidationError, load_skill

REQUIRED_POLICIES = (
    "authentic-voice-and-anti-slop.md",
    "data-classification.md",
    "coi-screen.md",
    "redaction-policy.md",
    "kill-switch.md",
    "no-secrets-in-git.md",
    "client-consent-checklist.md",
)
REQUIRED_TEMPLATES = (
    "activation-routing-map.md",
    "agentic-performance-gap-review.md",
    "copy-authenticity-audit.md",
    "contextual-idea-intake.md",
    "diagnose-memo.md",
    "plan-roadmap.md",
    "roadmap-steward-review.md",
    "story-activation-contract.md",
    "work-item-spec.md",
    "client-operating-kit.md",
    "client-command-room-fit-assessment.md",
    "client-command-room-spec.md",
    "recurring-engagement-cadence.md",
    "client-reply-intake.md",
    "custom-interface-craft-brief.md",
    "connector-map.md",
    "runbook.md",
    "case-study-capture.md",
    "session-rehydration-checklist.md",
    "memory-control-checkpoint.md",
    "memory-review-queue.md",
    "memory-source-index.md",
    "correction-checklist-for-toni.md",
    "business-brain-weekly-operating-packet.md",
)
REQUIRED_SKILLS = (
    "diagnose",
    "plan-roadmap",
    "client-context-draft",
    "proposal-draft",
    "handoff-runbook",
    "coi-screen",
    "redact",
)


@dataclass(frozen=True)
class DoctorResult:
    ok: bool
    checks: tuple[str, ...]
    problems: tuple[str, ...]


def run_practice_doctor(config: DtpConfig) -> DoctorResult:
    checks: list[str] = []
    problems: list[str] = []
    root = config.practice_os_dir

    if not root.exists():
        problems.append("missing practice-os/")
    else:
        checks.append("practice-os exists")

    _check_files(root / "policies", REQUIRED_POLICIES, "policy", checks, problems)
    _check_files(root / "templates", REQUIRED_TEMPLATES, "template", checks, problems)
    _check_practice_skills(root / "skills", checks, problems)
    _check_gitignore(config.repo_root / ".gitignore", checks, problems)

    return DoctorResult(ok=not problems, checks=tuple(checks), problems=tuple(problems))


def render_doctor(result: DoctorResult) -> str:
    lines = ["practice doctor: ok" if result.ok else "practice doctor: needs work"]
    lines.extend(f"  ok: {item}" for item in result.checks)
    lines.extend(f"  problem: {item}" for item in result.problems)
    return "\n".join(lines) + "\n"


def _check_files(
    root: Path,
    names: tuple[str, ...],
    label: str,
    checks: list[str],
    problems: list[str],
) -> None:
    for name in names:
        path = root / name
        if path.exists() and path.is_file():
            checks.append(f"{label} {name}")
        else:
            problems.append(f"missing {label}: {path.as_posix()}")


def _check_practice_skills(root: Path, checks: list[str], problems: list[str]) -> None:
    for name in REQUIRED_SKILLS:
        path = root / name / "SKILL.md"
        if not path.exists():
            problems.append(f"missing practice skill: {path.as_posix()}")
            continue
        try:
            load_skill(path)
        except SkillValidationError as error:
            problems.append(str(error))
            continue
        checks.append(f"practice skill {name}")


def _check_gitignore(path: Path, checks: list[str], problems: list[str]) -> None:
    if not path.exists():
        problems.append("missing .gitignore")
        return
    text = path.read_text(encoding="utf-8")
    required = ("engagements/*", "!engagements/README.md")
    for item in required:
        if item in text:
            checks.append(f".gitignore keeps {item}")
        else:
            problems.append(f".gitignore missing {item}")
