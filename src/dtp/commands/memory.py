from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from dtp.commands.evolution import EvolutionItem, read_evolution_items
from dtp.commands.kaizen import KaizenRecord, read_kaizen_records
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
MEMORY_REVIEW_STATES = {
    "raw_capture",
    "working_memory",
    "decision_memory",
    "pattern_candidate",
    "draft",
    "reviewed",
}
KAIZEN_STEWARD_STATUSES = {"inbox", "now", "next", "waiting", "blocked", "parked"}


@dataclass(frozen=True)
class MemoryStatus:
    ok: bool
    checks: tuple[str, ...]
    warnings: tuple[str, ...]
    problems: tuple[str, ...]
    recent_receipts: tuple[Path, ...]


@dataclass(frozen=True)
class MemoryStewardItem:
    title: str
    source_type: str
    state: str
    path: Path | None
    recommendation: str
    boundary: str


@dataclass(frozen=True)
class MemoryStewardReview:
    items: tuple[MemoryStewardItem, ...]
    evolution_count: int
    kaizen_count: int
    dashboard_path: Path


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


def run_memory_steward_review(config: DtpConfig, *, limit: int = 10) -> MemoryStewardReview:
    items: list[MemoryStewardItem] = []
    for item in read_evolution_items(config):
        if item.state in MEMORY_REVIEW_STATES:
            items.append(_memory_item_from_evolution(item))

    for record in read_kaizen_records(config):
        if record.status in KAIZEN_STEWARD_STATUSES:
            items.append(_memory_item_from_kaizen(record, config.repo_root))

    ranked = sorted(items, key=_memory_item_rank)[: max(limit, 0)]
    return MemoryStewardReview(
        items=tuple(ranked),
        evolution_count=sum(1 for item in items if item.source_type == "evolution"),
        kaizen_count=sum(1 for item in items if item.source_type == "kaizen"),
        dashboard_path=config.repo_root / "docs" / "practice-evolution-dashboard.html",
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


def render_memory_steward_review(review: MemoryStewardReview, repo_root: Path) -> str:
    lines = [
        "Memory Steward Review",
        "mode: read-only recommendation",
        (
            "scope: evolution records, research candidates, and active/parked "
            "Kaizen rows"
        ),
        (
            "rule: suggest capture, review, promotion, parking, or supersession; "
            "do not promote memory automatically"
        ),
        f"evolution_items_needing_review={review.evolution_count}",
        f"kaizen_items_needing_attention={review.kaizen_count}",
        f"dashboard={review.dashboard_path.relative_to(repo_root).as_posix()}",
        "",
        "Recommendations",
    ]
    if not review.items:
        lines.append("- none")
        return "\n".join(lines) + "\n"

    for item in review.items:
        location = item.path.relative_to(repo_root).as_posix() if item.path else "none"
        lines.extend(
            [
                f"- {item.title}",
                f"  source: {item.source_type}",
                f"  state: {item.state}",
                f"  path: {location}",
                f"  recommendation: {item.recommendation}",
                f"  boundary: {item.boundary}",
            ]
        )
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


def _memory_item_from_evolution(item: EvolutionItem) -> MemoryStewardItem:
    return MemoryStewardItem(
        title=item.title,
        source_type="evolution",
        state=item.state,
        path=item.path,
        recommendation=_evolution_recommendation(item),
        boundary=(
            "human review required before promotion; no public/client/runtime "
            "action"
        ),
    )


def _memory_item_from_kaizen(record: KaizenRecord, repo_root: Path) -> MemoryStewardItem:
    path = repo_root / record.dtp_source_path if record.dtp_source_path else None
    title = record.title.strip() if record.title else ""
    return MemoryStewardItem(
        title=title or record.id,
        source_type="kaizen",
        state=record.status,
        path=path,
        recommendation=_kaizen_recommendation(record),
        boundary=(
            "capture can become evolution only after source, sensitivity, and "
            "owner intent are clear"
        ),
    )


def _evolution_recommendation(item: EvolutionItem) -> str:
    if item.state == "raw_capture":
        return "decide whether this stays raw, becomes working memory, or parks"
    if item.state == "working_memory":
        return "review after one more use; promote, park, or supersede explicitly"
    if item.state == "decision_memory":
        return "verify decision owner and drift trigger before reusing broadly"
    if item.state == "pattern_candidate":
        return "test the pattern again before pattern_memory promotion"
    if item.state == "draft":
        return "complete evidence limits and next experiment before promotion"
    if item.state == "reviewed":
        return "record approved destination or park the candidate"
    return "review status and destination"


def _kaizen_recommendation(record: KaizenRecord) -> str:
    if record.status == "inbox":
        return "triage into now, next, waiting, parked, or evolution record"
    if record.status in {"now", "next"}:
        return "confirm whether active work needs an evolution record or receipt"
    if record.status == "waiting":
        return "keep waiting unless new evidence changes the next action"
    if record.status == "blocked":
        return "name blocker evidence and stop condition before reopening"
    if record.status == "parked":
        return "leave parked or create an evolution record if the pattern matters"
    return "review queue state"


def _memory_item_rank(item: MemoryStewardItem) -> tuple[int, str, str]:
    priority = {
        "raw_capture": 0,
        "inbox": 0,
        "working_memory": 1,
        "pattern_candidate": 2,
        "decision_memory": 3,
        "draft": 4,
        "reviewed": 5,
        "now": 6,
        "next": 7,
        "blocked": 8,
        "waiting": 9,
        "parked": 10,
    }
    return (priority.get(item.state, 99), item.source_type, item.title.lower())
