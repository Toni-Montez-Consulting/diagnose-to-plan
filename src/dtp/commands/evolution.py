from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from dtp.commands.kaizen import KaizenRecord, read_kaizen_records
from dtp.config import DtpConfig

EVOLUTION_KINDS = ("idea", "research-pattern")
IDEA_STATES = (
    "raw_capture",
    "working_memory",
    "decision_memory",
    "pattern_candidate",
    "pattern_memory",
    "playbook_memory",
    "parked",
    "superseded",
    "discarded",
)
RESEARCH_STATES = ("draft", "reviewed", "promoted", "parked", "rejected")


class EvolutionError(ValueError):
    """User-facing Practice Evolution command error."""


@dataclass(frozen=True)
class EvolutionDraft:
    path: Path
    kind: str
    title: str
    source_kaizen_id: str = ""


@dataclass(frozen=True)
class EvolutionStatus:
    idea_records: tuple[Path, ...]
    research_candidates: tuple[Path, ...]
    state_counts: dict[str, int]


def run_evolution_new(
    config: DtpConfig,
    *,
    title: str = "",
    kind: str = "idea",
    from_kaizen: str = "",
    lane: str = "diagnose-to-plan",
    sensitivity: str = "internal-only",
    state: str = "",
    source: str = "codex",
    created_at: datetime | None = None,
    force: bool = False,
) -> EvolutionDraft:
    normalized_kind = _normalize_kind(kind)
    kaizen_record = _find_kaizen_record(config, from_kaizen) if from_kaizen else None
    resolved_title = _resolve_title(title, kaizen_record)
    if not resolved_title:
        raise EvolutionError("evolution new requires a title or --from-kaizen record")

    created = created_at or datetime.now(UTC)
    destination = _destination_path(config, normalized_kind, resolved_title, created)
    if destination.exists() and not force:
        raise EvolutionError(f"evolution record already exists: {destination.as_posix()}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    body = (
        _render_research_candidate(
            title=resolved_title,
            record=kaizen_record,
            lane=lane,
            sensitivity=sensitivity,
            state=state or "draft",
            source=source,
            created=created,
            destination=destination,
            repo_root=config.repo_root,
        )
        if normalized_kind == "research-pattern"
        else _render_idea_record(
            title=resolved_title,
            record=kaizen_record,
            lane=lane,
            sensitivity=sensitivity,
            state=state or "raw_capture",
            source=source,
            created=created,
            destination=destination,
            repo_root=config.repo_root,
        )
    )
    destination.write_text(body, encoding="utf-8", newline="\n")
    return EvolutionDraft(
        path=destination,
        kind=normalized_kind,
        title=resolved_title,
        source_kaizen_id=kaizen_record.id if kaizen_record else "",
    )


def run_evolution_status(config: DtpConfig) -> EvolutionStatus:
    idea_records = tuple(sorted(_idea_records_dir(config).glob("*.md")))
    research_candidates = tuple(sorted(_research_candidates_dir(config).glob("*.md")))
    counts: Counter[str] = Counter()

    for path in idea_records:
        counts[_extract_value(path, "- Current state:") or "unknown"] += 1
    for path in research_candidates:
        counts[_extract_value(path, "- Status:") or "unknown"] += 1

    return EvolutionStatus(
        idea_records=idea_records,
        research_candidates=research_candidates,
        state_counts=dict(sorted(counts.items())),
    )


def render_evolution_new(result: EvolutionDraft, repo_root: Path) -> str:
    relative = result.path.relative_to(repo_root).as_posix()
    lines = [
        f"evolution draft created {relative}",
        f"  kind: {result.kind}",
        f"  title: {result.title}",
    ]
    if result.source_kaizen_id:
        lines.append(f"  source kaizen: {result.source_kaizen_id}")
    return "\n".join(lines) + "\n"


def render_evolution_status(result: EvolutionStatus, repo_root: Path) -> str:
    lines = [
        "Practice Evolution Status",
        f"idea_records={len(result.idea_records)}",
        f"research_candidates={len(result.research_candidates)}",
    ]
    if result.state_counts:
        counts = ", ".join(f"{key}={value}" for key, value in result.state_counts.items())
        lines.append(f"states: {counts}")
    else:
        lines.append("states: none")

    lines.append("")
    lines.append("Idea Records")
    if result.idea_records:
        lines.extend(f"- {path.relative_to(repo_root).as_posix()}" for path in result.idea_records)
    else:
        lines.append("- none")

    lines.append("")
    lines.append("Research Pattern Candidates")
    if result.research_candidates:
        lines.extend(
            f"- {path.relative_to(repo_root).as_posix()}"
            for path in result.research_candidates
        )
    else:
        lines.append("- none")
    return "\n".join(lines) + "\n"


def _normalize_kind(kind: str) -> str:
    normalized = kind.strip().lower().replace("_", "-")
    if normalized not in EVOLUTION_KINDS:
        raise EvolutionError(f"unknown evolution kind: {kind}")
    return normalized


def _normalize_idea_state(state: str) -> str:
    normalized = state.strip().lower().replace("-", "_")
    if normalized not in IDEA_STATES:
        raise EvolutionError(f"unknown idea evolution state: {state}")
    return normalized


def _normalize_research_state(state: str) -> str:
    normalized = state.strip().lower().replace("_", "-")
    if normalized not in RESEARCH_STATES:
        raise EvolutionError(f"unknown research pattern state: {state}")
    return normalized


def _find_kaizen_record(config: DtpConfig, record_id: str) -> KaizenRecord:
    cleaned = record_id.strip()
    for record in read_kaizen_records(config):
        if record.id == cleaned:
            return record
    raise EvolutionError(f"unknown kaizen record: {record_id}")


def _resolve_title(title: str, record: KaizenRecord | None) -> str:
    cleaned = _clean(title)
    if cleaned:
        return cleaned
    if not record:
        return ""
    return record.title if not record.title.startswith("[redacted ") else record.id


def _destination_path(config: DtpConfig, kind: str, title: str, created: datetime) -> Path:
    directory = (
        _research_candidates_dir(config)
        if kind == "research-pattern"
        else _idea_records_dir(config)
    )
    return directory / f"{created.strftime('%Y-%m-%d')}-{_slug(title)}.md"


def _idea_records_dir(config: DtpConfig) -> Path:
    return config.practice_os_dir / "evolution" / "records"


def _research_candidates_dir(config: DtpConfig) -> Path:
    return config.practice_os_dir / "research" / "pattern-candidates"


def _render_idea_record(
    *,
    title: str,
    record: KaizenRecord | None,
    lane: str,
    sensitivity: str,
    state: str,
    source: str,
    created: datetime,
    destination: Path,
    repo_root: Path,
) -> str:
    normalized_state = _normalize_idea_state(state)
    source_value = record.source if record else source
    lane_value = record.repo if record else lane
    sensitivity_value = record.sensitivity if record else sensitivity
    source_path = record.dtp_source_path if record else ""
    original = record.text if record else title
    record_id = destination.stem
    created_date = created.strftime("%Y-%m-%d")
    relative_path = destination.relative_to(repo_root).as_posix()
    tags = ", ".join(record.tags) if record and record.tags else ""
    return f"""---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Idea Evolution Record - {title}

## Record Metadata

- Record id: {record_id}
- Created: {created_date}
- Updated:
- Source: {source_value}
- Source date: {record.captured_at if record else created.isoformat(timespec="seconds")}
- Owner: Toni
- Owning repo/lane: {lane_value}
- Sensitivity: {sensitivity_value}
- Current state: {normalized_state}
- Source Kaizen id: {record.id if record else ""}
- Tags: {tags}

## Original Signal

- Original wording / summary: {original}
- Source path / email / meeting / repo evidence: {source_path}
- What prompted the idea:

## Current Interpretation

- What this really means:
- Why it matters:
- What it could improve:
- What should not be inferred:

## Usefulness Test

| Question | Answer |
|---|---|
| Does this solve a real recurring problem? |  |
| Does this compound across projects or clients? |  |
| Does this preserve Toni's ambition and judgment? |  |
| Does this reduce future confusion, rework, or missed context? |  |
| What would make this worth building ambitiously? |  |

## Review Lenses

- [ ] Consulting Strategy
- [ ] External Communications
- [ ] Product Strategy
- [ ] UX / Design
- [ ] Software Architecture
- [ ] Software Engineering
- [ ] DevOps / Infrastructure
- [ ] QA / Audit
- [ ] General Counsel
- [ ] COO
- [ ] Controller

## Boundary Check

- Public proof risk:
- Client privacy risk:
- Legal / COI / compliance risk:
- Security / credential risk:
- Money movement or commitment risk:
- What requires Toni approval:

## Promotion Review

- Recommended promotion level:
- Evidence supporting promotion:
- Evidence limits:
- Reviewer:
- Approved level:
- Next review trigger:

## Next Artifact

- None
- Message / pitch candidate
- Research pattern candidate
- Practice pattern
- Template update
- Agent/skill instruction update
- Roadmap/backlog item
- Client-delivery artifact
- Public-copy brief
- Implementation plan

## Close / Supersede Condition

- Close when:
- Supersede when:
- Park if:

## Notion Mirror Summary

Safe to mirror: no

If yes:

- Topic:
- State:
- Next action:
- DTP source path: {relative_path}

## Notes

Raw capture is not reusable playbook memory. Promote only after review.
"""


def _render_research_candidate(
    *,
    title: str,
    record: KaizenRecord | None,
    lane: str,
    sensitivity: str,
    state: str,
    source: str,
    created: datetime,
    destination: Path,
    repo_root: Path,
) -> str:
    normalized_state = _normalize_research_state(state)
    source_value = record.source if record else source
    sensitivity_value = record.sensitivity if record else sensitivity
    original = record.text if record else title
    candidate_id = destination.stem
    created_date = created.strftime("%Y-%m-%d")
    relative_path = destination.relative_to(repo_root).as_posix()
    return f"""---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Research Pattern Candidate - {title}

## Candidate Metadata

- Candidate id: {candidate_id}
- Created: {created_date}
- Source: {source_value}
- Source type: research
- Sensitivity: {sensitivity_value}
- Reviewer:
- Status: {normalized_state}
- Owning repo/lane: {record.repo if record else lane}
- Source Kaizen id: {record.id if record else ""}

## Observation

- What was observed: {original}
- Where it showed up:
- Why it caught attention:
- Who or what type of operator it may apply to:

## Underlying Principle

- What seems to be true:
- What business or human behavior is underneath it:
- What would make the principle false:

## Consulting Translation

- How this changes discovery:
- How this changes diagnosis:
- How this changes delivery or handoff:
- How this changes messaging or client education:
- What Toni should watch for next time:

## Possible Artifact

- None
- Discovery question
- Checklist
- Workflow map
- Blueprint section
- Offer component
- Client education note
- Visual / infographic
- Practice pattern
- Template update
- Research digest
- Roadmap item

## Evidence Limits

- What evidence supports this:
- What is anecdotal or unproven:
- What cannot be claimed publicly:
- Privacy / proof / COI boundary:

## Next Experiment

- Where to test this next:
- What signal would confirm it is useful:
- What signal would make us drop it:

## Promotion Decision

- Recommended state:
- Reviewer:
- Approved state:
- Destination if promoted:

## Notion Mirror Summary

Safe to mirror: no

If yes:

- Pattern name:
- Why it matters:
- Next action:
- DTP source path: {relative_path}

## Notes

Promote only reviewed, redacted, reusable judgment into
`practice-os/patterns/`.
"""


def _extract_value(path: Path, prefix: str) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith(prefix):
            return line.removeprefix(prefix).strip()
    return ""


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _slug(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return re.sub(r"-+", "-", slug)[:64] or "record"
