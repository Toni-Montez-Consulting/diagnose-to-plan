from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from dtp.config import DtpConfig

REQUIRED_MEMORY_DOCS = (
    "PRACTICE_MEMORY_CONTROL_PLANE.md",
    "PRACTICE_MEMORY_OPTIMIZATION_PLAN.md",
    "PRACTICE_INTELLIGENCE_CONTROL_PLANE.md",
    "NOTION_MIRROR_V0.md",
)
REQUIRED_MEMORY_TEMPLATES = (
    "session-rehydration-checklist.md",
    "memory-control-checkpoint.md",
    "memory-review-queue.md",
    "memory-source-index.md",
    "correction-checklist-for-toni.md",
)
MEMORY_STEWARD_KEYWORDS = (
    "memory",
    "intelligence-control",
    "business-brain",
)


@dataclass(frozen=True)
class MemoryStatus:
    ok: bool
    checks: tuple[str, ...]
    warnings: tuple[str, ...]
    problems: tuple[str, ...]
    recent_receipts: tuple[Path, ...]


def run_memory_status(config: DtpConfig) -> MemoryStatus:
    checks: list[str] = []
    warnings: list[str] = []
    problems: list[str] = []
    docs_dir = config.repo_root / "docs"
    templates_dir = config.practice_os_dir / "templates"

    _check_files(docs_dir, REQUIRED_MEMORY_DOCS, "doc", checks, problems)
    _check_files(templates_dir, REQUIRED_MEMORY_TEMPLATES, "template", checks, problems)

    receipts = _recent_memory_receipts(config.practice_os_dir / "steward")
    if receipts:
        checks.append(f"recent memory steward receipts: {len(receipts)}")
    else:
        warnings.append("no recent memory/intelligence steward receipts found")

    checks.append("source rule: DTP is authoritative; Codex memory must be verified")
    checks.append("mirror rule: Notion is an inbox/mirror, not source of truth")
    checks.append("promotion rule: durable memory requires human approval")

    return MemoryStatus(
        ok=not problems,
        checks=tuple(checks),
        warnings=tuple(warnings),
        problems=tuple(problems),
        recent_receipts=receipts,
    )


def render_memory_status(status: MemoryStatus, repo_root: Path) -> str:
    lines = ["memory spine: ok" if status.ok else "memory spine: needs work"]
    lines.extend(f"  ok: {item}" for item in status.checks)
    lines.extend(f"  warning: {item}" for item in status.warnings)
    lines.extend(f"  problem: {item}" for item in status.problems)
    if status.recent_receipts:
        lines.append("  recent receipts:")
        for receipt in status.recent_receipts[:5]:
            lines.append(f"    - {receipt.relative_to(repo_root).as_posix()}")
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
            problems.append(f"missing memory {label}: {path.as_posix()}")


def _recent_memory_receipts(root: Path) -> tuple[Path, ...]:
    if not root.exists():
        return ()
    candidates = [
        path
        for path in root.glob("*.md")
        if any(keyword in path.name.lower() for keyword in MEMORY_STEWARD_KEYWORDS)
    ]
    return tuple(sorted(candidates, reverse=True)[:8])
