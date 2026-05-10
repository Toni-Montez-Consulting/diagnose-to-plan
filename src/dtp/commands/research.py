from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from dtp.commands.evolution import EvolutionItem, read_evolution_items
from dtp.commands.kaizen import KaizenRecord, read_kaizen_records
from dtp.config import DtpConfig

RESEARCH_STEWARD_BOUNDARY = (
    "research can recommend; it cannot authorize public claims, offer changes, "
    "tool installs, repo changes, client communication, or autonomous runtime"
)
RESEARCH_PATTERN_REVIEW_STATES = {"draft", "reviewed", "parked"}
RESEARCH_DIGEST_REVIEW_STATES = {"draft", "reviewed", "parked"}
KAIZEN_RESEARCH_STATUSES = {"inbox", "now", "next", "waiting", "blocked", "parked"}
RESEARCH_TAGS = {
    "research",
    "research-arm",
    "research-radar",
    "research-spike",
    "pattern-library",
    "ai-agents",
    "legal-mcp",
    "tooling-research",
}


@dataclass(frozen=True)
class ResearchStewardItem:
    title: str
    source_type: str
    state: str
    path: Path | None
    recommendation: str
    boundary: str = RESEARCH_STEWARD_BOUNDARY


@dataclass(frozen=True)
class ResearchStewardReview:
    items: tuple[ResearchStewardItem, ...]
    pattern_candidate_count: int
    kaizen_count: int
    digest_count: int
    research_arm_path: Path


@dataclass(frozen=True)
class ResearchDigest:
    title: str
    status: str
    path: Path


def run_research_steward_review(
    config: DtpConfig,
    *,
    limit: int = 10,
) -> ResearchStewardReview:
    items: list[ResearchStewardItem] = []

    pattern_items = [
        item
        for item in read_evolution_items(config)
        if item.kind == "research-pattern" and item.state in RESEARCH_PATTERN_REVIEW_STATES
    ]
    for item in pattern_items:
        items.append(_research_item_from_pattern(item))

    kaizen_records = [
        record
        for record in read_kaizen_records(config)
        if _is_research_kaizen_record(record) and record.status in KAIZEN_RESEARCH_STATUSES
    ]
    for record in kaizen_records:
        items.append(_research_item_from_kaizen(record, config.repo_root))

    digest_items = [
        digest
        for digest in _read_research_digests(config)
        if digest.status in RESEARCH_DIGEST_REVIEW_STATES
    ]
    for digest in digest_items:
        items.append(_research_item_from_digest(digest))

    ranked = sorted(items, key=_research_item_rank)[: max(limit, 0)]
    return ResearchStewardReview(
        items=tuple(ranked),
        pattern_candidate_count=len(pattern_items),
        kaizen_count=len(kaizen_records),
        digest_count=len(digest_items),
        research_arm_path=config.repo_root / "docs" / "RESEARCH_ARM_V0.md",
    )


def render_research_steward_review(review: ResearchStewardReview, repo_root: Path) -> str:
    lines = [
        "Research Steward Review",
        "mode: read-only recommendation",
        (
            "scope: research-pattern candidates, research-flavored Kaizen rows, "
            "and Research Arm digests"
        ),
        f"rule: {RESEARCH_STEWARD_BOUNDARY}",
        f"pattern_candidates_needing_review={review.pattern_candidate_count}",
        f"kaizen_research_items_needing_attention={review.kaizen_count}",
        f"research_digests_needing_attention={review.digest_count}",
        f"research_arm={review.research_arm_path.relative_to(repo_root).as_posix()}",
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


def _research_item_from_pattern(item: EvolutionItem) -> ResearchStewardItem:
    return ResearchStewardItem(
        title=item.title,
        source_type="research-pattern",
        state=item.state,
        path=item.path,
        recommendation=_pattern_recommendation(item),
    )


def _research_item_from_kaizen(record: KaizenRecord, repo_root: Path) -> ResearchStewardItem:
    path = repo_root / record.dtp_source_path if record.dtp_source_path else None
    title = record.title.strip() if record.title else record.id
    return ResearchStewardItem(
        title=title,
        source_type="kaizen",
        state=record.status,
        path=path,
        recommendation=_kaizen_recommendation(record),
    )


def _research_item_from_digest(digest: ResearchDigest) -> ResearchStewardItem:
    return ResearchStewardItem(
        title=digest.title,
        source_type="digest",
        state=digest.status,
        path=digest.path,
        recommendation=_digest_recommendation(digest),
    )


def _is_research_kaizen_record(record: KaizenRecord) -> bool:
    if record.item_type == "research":
        return True
    tags = {tag.strip().lower() for tag in record.tags}
    return bool(tags.intersection(RESEARCH_TAGS))


def _read_research_digests(config: DtpConfig) -> tuple[ResearchDigest, ...]:
    root = config.practice_os_dir / "research" / "digests"
    if not root.exists():
        return ()
    digests: list[ResearchDigest] = []
    for path in sorted(root.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        digests.append(
            ResearchDigest(
                title=_extract_title(text) or path.stem,
                status=(_extract_text_value(text, "Status:") or "unknown")
                .strip()
                .lower()
                .replace("_", "-"),
                path=path,
            )
        )
    return tuple(digests)


def _extract_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line.removeprefix("# ").strip()
    return ""


def _extract_text_value(text: str, prefix: str) -> str:
    for line in text.splitlines():
        if line.startswith(prefix):
            return line.removeprefix(prefix).strip()
    return ""


def _pattern_recommendation(item: EvolutionItem) -> str:
    if item.state == "draft":
        return "complete evidence limits, next experiment, and reviewer before promotion"
    if item.state == "reviewed":
        return "choose destination: pattern, template, digest, roadmap item, or park"
    if item.state == "promoted":
        return "verify destination exists and keep the public-claim citation boundary"
    if item.state == "parked":
        return "leave parked until the trigger changes, or reject explicitly if stale"
    return "review status and destination before reuse"


def _kaizen_recommendation(record: KaizenRecord) -> str:
    if record.status == "inbox":
        return "classify into digest, radar item, spike, pattern candidate, or park"
    if record.status in {"now", "next"}:
        return "turn accepted research work into a bounded artifact before implementation"
    if record.status == "waiting":
        return "keep waiting until source evidence, owner signal, or approval arrives"
    if record.status == "blocked":
        return "name the missing source, reviewer, gate, or stop condition"
    if record.status == "parked":
        return "leave parked unless an accepted research spike or roadmap story opens"
    return "review research queue state"


def _digest_recommendation(digest: ResearchDigest) -> str:
    if digest.status == "draft":
        return "finish sources, hype filter, classification, approval gate, and next action"
    if digest.status == "reviewed":
        return "decide whether it should create a radar item, spike, pattern, or artifact"
    if digest.status == "accepted":
        return "verify the accepted next artifact has an owner, boundary, and evidence path"
    if digest.status == "parked":
        return "leave parked until the source or market signal changes"
    return "review digest status and classification"


def _research_item_rank(item: ResearchStewardItem) -> tuple[int, str, str]:
    priority = {
        "draft": 0,
        "inbox": 0,
        "now": 1,
        "next": 2,
        "reviewed": 3,
        "accepted": 4,
        "blocked": 5,
        "waiting": 6,
        "promoted": 7,
        "parked": 8,
    }
    return (priority.get(item.state, 99), item.source_type, item.title.lower())
