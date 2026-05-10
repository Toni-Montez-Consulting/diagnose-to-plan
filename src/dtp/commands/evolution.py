from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from datetime import UTC, datetime
from html import escape
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


@dataclass(frozen=True)
class EvolutionItem:
    path: Path
    kind: str
    title: str
    state: str
    sensitivity: str
    source: str
    created: str
    lane: str
    safe_to_mirror: str
    next_review_trigger: str


@dataclass(frozen=True)
class EvolutionDashboard:
    path: Path
    html: str
    item_count: int
    state_counts: dict[str, int]
    needs_review_count: int


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
    counts: Counter[str] = Counter(item.state for item in read_evolution_items(config))

    return EvolutionStatus(
        idea_records=idea_records,
        research_candidates=research_candidates,
        state_counts=dict(sorted(counts.items())),
    )


def read_evolution_items(config: DtpConfig) -> tuple[EvolutionItem, ...]:
    items: list[EvolutionItem] = []
    for path in sorted(_idea_records_dir(config).glob("*.md")):
        items.append(_read_evolution_item(path, kind="idea"))
    for path in sorted(_research_candidates_dir(config).glob("*.md")):
        items.append(_read_evolution_item(path, kind="research-pattern"))
    return tuple(sorted(items, key=lambda item: (item.created, item.title, item.kind)))


def run_evolution_dashboard(
    config: DtpConfig,
    *,
    output_path: Path | None = None,
) -> EvolutionDashboard:
    items = read_evolution_items(config)
    path = _resolve_output_path(
        config.repo_root,
        output_path or Path("docs/practice-evolution-dashboard.html"),
    )
    html = render_evolution_dashboard(items, config.repo_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8", newline="\n")
    state_counts: Counter[str] = Counter(item.state for item in items)
    return EvolutionDashboard(
        path=path,
        html=html,
        item_count=len(items),
        state_counts=dict(sorted(state_counts.items())),
        needs_review_count=sum(1 for item in items if _needs_review(item)),
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


def render_evolution_dashboard(
    items: tuple[EvolutionItem, ...],
    repo_root: Path,
    *,
    generated_at: datetime | None = None,
) -> str:
    generated = (generated_at or datetime.now(UTC)).strftime("%Y-%m-%d %H:%M UTC")
    state_counts: Counter[str] = Counter(item.state for item in items)
    kind_counts: Counter[str] = Counter(item.kind for item in items)
    idea_count = kind_counts.get("idea", 0)
    research_count = kind_counts.get("research-pattern", 0)
    review_count = sum(1 for item in items if _needs_review(item))
    rows = "\n".join(_render_dashboard_row(item, repo_root) for item in items)
    if not rows:
        rows = (
            '<tr class="empty-row"><td colspan="8">'
            "No evolution records found yet.</td></tr>"
        )
    state_filters = "\n".join(
        _render_filter_button(state, count)
        for state, count in sorted(state_counts.items())
    )
    if not state_filters:
        state_filters = '<p class="muted">No states to filter yet.</p>'
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Practice Evolution Dashboard</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f7f8f5;
      --ink: #17201b;
      --muted: #5b645f;
      --panel: #ffffff;
      --line: #d9ded7;
      --green: #2f6d4f;
      --blue: #275d8c;
      --amber: #9b6828;
      --rose: #994c4c;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font: 15px/1.5 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: var(--bg);
      color: var(--ink);
    }}
    main {{
      width: min(1180px, calc(100vw - 32px));
      margin: 0 auto;
      padding: 32px 0 48px;
    }}
    header {{
      display: grid;
      gap: 12px;
      margin-bottom: 24px;
    }}
    h1, h2 {{
      margin: 0;
      line-height: 1.15;
      letter-spacing: 0;
    }}
    h1 {{ font-size: 2rem; }}
    h2 {{ font-size: 1.1rem; }}
    p {{ margin: 0; }}
    .muted {{ color: var(--muted); }}
    .summary {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
      gap: 12px;
      margin: 18px 0;
    }}
    .metric {{
      display: grid;
      gap: 4px;
      min-height: 92px;
      padding: 16px;
      border: 1px solid var(--line);
      background: var(--panel);
      border-radius: 8px;
    }}
    .metric strong {{ font-size: 1.85rem; }}
    .toolbar {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
      margin: 18px 0;
    }}
    input[type="search"] {{
      flex: 1 1 280px;
      min-height: 42px;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 8px 12px;
      font: inherit;
      background: var(--panel);
      color: var(--ink);
    }}
    button {{
      min-height: 42px;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 8px 12px;
      font: inherit;
      background: var(--panel);
      color: var(--ink);
      cursor: pointer;
    }}
    button.active {{
      border-color: var(--green);
      color: #fff;
      background: var(--green);
    }}
    section {{
      margin-top: 22px;
    }}
    .table-wrap {{
      overflow-x: auto;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
    }}
    table {{
      width: 100%;
      min-width: 920px;
      border-collapse: collapse;
    }}
    th, td {{
      padding: 12px;
      border-bottom: 1px solid var(--line);
      text-align: left;
      vertical-align: top;
    }}
    th {{
      font-size: 0.78rem;
      color: var(--muted);
      text-transform: uppercase;
    }}
    tr:last-child td {{ border-bottom: 0; }}
    a {{ color: var(--blue); }}
    .pill {{
      display: inline-flex;
      align-items: center;
      min-height: 26px;
      padding: 3px 8px;
      border: 1px solid var(--line);
      border-radius: 999px;
      color: var(--ink);
      background: #fafbf8;
      white-space: nowrap;
    }}
    .pill.review {{ border-color: #d9b26f; color: var(--amber); }}
    .pill.idea {{ border-color: #a9c8b7; color: var(--green); }}
    .pill.research {{ border-color: #a8bdd4; color: var(--blue); }}
    .path {{ font-size: 0.86rem; color: var(--muted); }}
    .empty-row {{ color: var(--muted); }}
    .boundary {{
      padding: 16px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
    }}
    .boundary ul {{
      margin: 8px 0 0;
      padding-left: 20px;
    }}
    @media (max-width: 720px) {{
      main {{ width: min(100vw - 20px, 1180px); padding-top: 20px; }}
      h1 {{ font-size: 1.55rem; }}
      .metric {{ min-height: 82px; }}
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <p class="muted">Generated {escape(generated)}</p>
      <h1>Practice Evolution Dashboard</h1>
      <p class="muted">
        Static status view for idea records, meta-patterns, and research-pattern
        candidates. It reads local DTP markdown only and does not publish,
        sync, mutate client data, or promote memory by itself.
      </p>
    </header>

    <section class="summary" aria-label="Evolution summary">
      <div class="metric"><span>Total records</span><strong>{len(items)}</strong></div>
      <div class="metric"><span>Idea records</span><strong>{idea_count}</strong></div>
      <div class="metric"><span>Research candidates</span><strong>{research_count}</strong></div>
      <div class="metric"><span>Needs review</span><strong>{review_count}</strong></div>
    </section>

    <section>
      <h2>State Filters</h2>
      <div class="toolbar" aria-label="Dashboard filters">
        <input id="evolution-search" type="search"
          placeholder="Search records, states, sources, lanes, and paths">
        <button type="button" class="active" data-state-filter="">All states</button>
        {state_filters}
      </div>
      <p id="filter-status" class="muted">Showing all evolution records.</p>
    </section>

    <section>
      <h2>Record Register</h2>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Record</th>
              <th>Kind</th>
              <th>State</th>
              <th>Created</th>
              <th>Source</th>
              <th>Lane</th>
              <th>Sensitivity</th>
              <th>Mirror</th>
            </tr>
          </thead>
          <tbody id="record-register">
            {rows}
          </tbody>
        </table>
      </div>
    </section>

    <section class="boundary">
      <h2>Scale Path</h2>
      <ul>
        <li>Status dashboard now: counts, filters, search, and source links.</li>
        <li>Review room later: promotion queue, reviewer decisions, and batch receipts.</li>
        <li>Mirror later: sanitized Notion cockpit only after explicit review.</li>
      </ul>
    </section>
  </main>
  <script>
    const rows = [...document.querySelectorAll("#record-register tr[data-state]")];
    const search = document.getElementById("evolution-search");
    const buttons = [...document.querySelectorAll("[data-state-filter]")];
    const status = document.getElementById("filter-status");
    let activeState = "";

    function applyFilters() {{
      const query = search.value.trim().toLowerCase();
      let shown = 0;
      rows.forEach((row) => {{
        const stateMatch = !activeState || row.dataset.state === activeState;
        const queryMatch = !query || row.dataset.search.includes(query);
        const visible = stateMatch && queryMatch;
        row.hidden = !visible;
        if (visible) shown += 1;
      }});
      status.textContent = `Showing ${{shown}} of ${{rows.length}} evolution records.`;
    }}

    buttons.forEach((button) => {{
      button.addEventListener("click", () => {{
        activeState = button.dataset.stateFilter || "";
        buttons.forEach((item) => item.classList.toggle("active", item === button));
        applyFilters();
      }});
    }});
    search.addEventListener("input", applyFilters);
  </script>
</body>
</html>
"""


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


def _resolve_output_path(repo_root: Path, output_path: Path) -> Path:
    return output_path if output_path.is_absolute() else repo_root / output_path


def _read_evolution_item(path: Path, *, kind: str) -> EvolutionItem:
    text = path.read_text(encoding="utf-8")
    if kind == "research-pattern":
        title = _extract_title(text, "# Research Pattern Candidate - ")
        state = _extract_text_value(text, "- Status:") or "unknown"
        next_review_trigger = _extract_text_value(
            text,
            "- What signal would confirm it is useful:",
        )
    else:
        title = _extract_title(text, "# Idea Evolution Record - ")
        state = _extract_text_value(text, "- Current state:") or "unknown"
        next_review_trigger = _extract_text_value(text, "- Next review trigger:")
    return EvolutionItem(
        path=path,
        kind=kind,
        title=title or path.stem,
        state=state,
        sensitivity=_extract_text_value(text, "- Sensitivity:") or "unknown",
        source=_extract_text_value(text, "- Source:") or "unknown",
        created=_extract_text_value(text, "- Created:") or "unknown",
        lane=_extract_text_value(text, "- Owning repo/lane:") or "unknown",
        safe_to_mirror=_extract_text_value(text, "Safe to mirror:") or "unknown",
        next_review_trigger=next_review_trigger,
    )


def _extract_title(text: str, prefix: str) -> str:
    for line in text.splitlines():
        if line.startswith(prefix):
            return line.removeprefix(prefix).strip()
    return ""


def _extract_text_value(text: str, prefix: str) -> str:
    for line in text.splitlines():
        if line.startswith(prefix):
            return line.removeprefix(prefix).strip()
    return ""


def _needs_review(item: EvolutionItem) -> bool:
    return item.state in {
        "raw_capture",
        "working_memory",
        "decision_memory",
        "pattern_candidate",
        "draft",
        "reviewed",
    }


def _render_filter_button(state: str, count: int) -> str:
    label = state.replace("_", " ").replace("-", " ").title()
    return (
        f'<button type="button" data-state-filter="{escape(state)}">'
        f"{escape(label)} ({count})</button>"
    )


def _render_dashboard_row(item: EvolutionItem, repo_root: Path) -> str:
    relative = item.path.relative_to(repo_root).as_posix()
    kind_label = "Research" if item.kind == "research-pattern" else "Idea"
    kind_class = "research" if item.kind == "research-pattern" else "idea"
    review = ' <span class="pill review">review</span>' if _needs_review(item) else ""
    search_text = " ".join(
        [
            item.title,
            item.kind,
            item.state,
            item.source,
            item.lane,
            item.sensitivity,
            item.safe_to_mirror,
            relative,
        ]
    ).lower()
    return f"""<tr data-state="{escape(item.state)}" data-kind="{escape(item.kind)}"
    data-search="{escape(search_text)}">
      <td>
        <a href="../{escape(relative)}">{escape(item.title)}</a>{review}
        <div class="path">{escape(relative)}</div>
      </td>
      <td><span class="pill {kind_class}">{escape(kind_label)}</span></td>
      <td><span class="pill">{escape(item.state)}</span></td>
      <td>{escape(item.created)}</td>
      <td>{escape(item.source)}</td>
      <td>{escape(item.lane)}</td>
      <td>{escape(item.sensitivity)}</td>
      <td>{escape(item.safe_to_mirror)}</td>
    </tr>"""


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
