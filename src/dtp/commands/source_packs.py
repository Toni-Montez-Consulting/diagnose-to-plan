"""Validation helpers for Practice OS agent source packs."""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass
from datetime import UTC, date, datetime
from html import escape
from pathlib import Path
from typing import Any

from dtp.config import DtpConfig

DEFAULT_SOURCE_PACK_PATH = Path(
    "practice-os/research/source-packs/agent-source-packs.v0.json"
)
EXPECTED_SCHEMA_VERSION = "agent-source-packs.v0"
EXPECTED_EVIDENCE_TIERS = {0, 1, 2, 3, 4}
DEFAULT_SOURCE_PACK_DASHBOARD_PATH = Path("docs/source-pack-status-dashboard.html")


@dataclass(frozen=True)
class SourcePackValidationResult:
    """Result returned by the source-pack validator."""

    ok: bool
    path: Path
    checks: tuple[str, ...]
    problems: tuple[str, ...]
    role_ids: tuple[str, ...]


@dataclass(frozen=True)
class SourcePackRoleStatus:
    """Dashboard-ready role summary derived from the source pack."""

    role_id: str
    role_name: str
    status: str
    freshness: str
    last_reviewed_at: str
    review_age_days: int | None
    primary_source_count: int
    strong_source_count: int
    discovery_source_count: int
    allowed_web_source_count: int
    blocked_source_count: int
    promotion_gate_count: int
    pilot_artifact_count: int
    search_default: str
    broad_web_confidence: str
    next_review_trigger: str


@dataclass(frozen=True)
class SourcePackStatusResult:
    """Read-only status view of the source-pack system."""

    ok: bool
    path: Path
    validation: SourcePackValidationResult
    schema_version: str
    review_status: str
    updated_at: str
    role_statuses: tuple[SourcePackRoleStatus, ...]
    freshness_counts: dict[str, int]
    primary_source_count: int


@dataclass(frozen=True)
class SourcePackDashboardResult:
    """Generated source-pack dashboard artifact."""

    path: Path
    html: str
    role_count: int
    stale_or_review_count: int
    validation_ok: bool


def run_source_pack_validation(
    config: DtpConfig,
    *,
    path: Path | None = None,
) -> SourcePackValidationResult:
    """Validate the agent source-pack contract without external dependencies."""

    repo_root = config.repo_root
    source_pack_path = _resolve_path(repo_root, path or DEFAULT_SOURCE_PACK_PATH)
    checks: list[str] = []
    problems: list[str] = []
    role_ids: list[str] = []

    display_path = _display_path(repo_root, source_pack_path)
    if not source_pack_path.exists():
        problems.append(f"missing source pack file: {display_path}")
        return SourcePackValidationResult(
            ok=False,
            path=source_pack_path,
            checks=tuple(checks),
            problems=tuple(problems),
            role_ids=tuple(role_ids),
        )
    checks.append(f"source pack schema file exists: {display_path}")

    try:
        payload = json.loads(source_pack_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        problems.append(f"invalid JSON in source pack: {exc.msg} at line {exc.lineno}")
        return SourcePackValidationResult(
            ok=False,
            path=source_pack_path,
            checks=tuple(checks),
            problems=tuple(problems),
            role_ids=tuple(role_ids),
        )

    root = _expect_mapping(payload, "$", problems)
    if root is None:
        return SourcePackValidationResult(
            ok=False,
            path=source_pack_path,
            checks=tuple(checks),
            problems=tuple(problems),
            role_ids=tuple(role_ids),
        )

    schema_version = _require_non_empty_str(root, "schema_version", "$", problems)
    if schema_version == EXPECTED_SCHEMA_VERSION:
        checks.append(f"source pack schema version: {EXPECTED_SCHEMA_VERSION}")
    elif schema_version:
        problems.append(
            "$.schema_version expected "
            f"{EXPECTED_SCHEMA_VERSION!r}, found {schema_version!r}"
        )

    for key in (
        "review_status",
        "owner_repo",
        "created_at",
        "updated_at",
        "policy_doc",
        "governing_rule",
    ):
        _require_non_empty_str(root, key, "$", problems)

    policy_doc = root.get("policy_doc")
    if isinstance(policy_doc, str) and policy_doc.strip():
        policy_doc_path = repo_root / policy_doc
        if policy_doc_path.exists():
            checks.append(f"source pack policy doc exists: {policy_doc}")
        else:
            problems.append(f"$.policy_doc points to missing file: {policy_doc}")

    _validate_authority_boundary(root, checks, problems)
    evidence_tiers = _validate_evidence_tiers(root, checks, problems)
    _validate_packs(root, repo_root, evidence_tiers, role_ids, checks, problems)

    return SourcePackValidationResult(
        ok=not problems,
        path=source_pack_path,
        checks=tuple(checks),
        problems=tuple(problems),
        role_ids=tuple(role_ids),
    )


def render_source_pack_validation(
    result: SourcePackValidationResult,
    repo_root: Path,
) -> str:
    """Render a validation result for CLI output."""

    status = "ok" if result.ok else "failed"
    lines = [f"source-pack validation: {status}"]
    lines.append(f"path: {_display_path(repo_root, result.path)}")

    if result.checks:
        lines.append("")
        lines.append("checks:")
        for check in result.checks:
            lines.append(f"- {check}")

    if result.role_ids:
        lines.append("")
        lines.append("roles:")
        for role_id in result.role_ids:
            lines.append(f"- {role_id}")

    if result.problems:
        lines.append("")
        lines.append("problems:")
        for problem in result.problems:
            lines.append(f"- {problem}")

    return "\n".join(lines) + "\n"


def run_source_pack_status(
    config: DtpConfig,
    *,
    path: Path | None = None,
    today: date | None = None,
) -> SourcePackStatusResult:
    """Build a read-only status model from the source pack and validator."""

    validation = run_source_pack_validation(config, path=path)
    payload = _read_source_pack_payload(validation.path)
    status_today = today or datetime.now(UTC).date()
    role_statuses = _build_role_statuses(payload, status_today)
    freshness_counts = dict(sorted(Counter(role.freshness for role in role_statuses).items()))
    primary_source_count = sum(role.primary_source_count for role in role_statuses)

    return SourcePackStatusResult(
        ok=validation.ok and bool(role_statuses),
        path=validation.path,
        validation=validation,
        schema_version=_as_str(payload.get("schema_version")) if payload else "",
        review_status=_as_str(payload.get("review_status")) if payload else "",
        updated_at=_as_str(payload.get("updated_at")) if payload else "",
        role_statuses=role_statuses,
        freshness_counts=freshness_counts,
        primary_source_count=primary_source_count,
    )


def render_source_pack_status(result: SourcePackStatusResult, repo_root: Path) -> str:
    """Render the source-pack status result for terminal use."""

    freshness = ", ".join(
        f"{key}={value}" for key, value in result.freshness_counts.items()
    )
    lines = [
        "Source Pack Status",
        f"path: {_display_path(repo_root, result.path)}",
        f"validation: {'ok' if result.validation.ok else 'needs work'}",
        f"schema: {result.schema_version or 'unknown'}",
        f"review_status: {result.review_status or 'unknown'}",
        f"updated_at: {result.updated_at or 'unknown'}",
        f"roles: {len(result.role_statuses)}",
        f"primary_sources: {result.primary_source_count}",
        f"freshness: {freshness or 'none'}",
        "",
        "Role Status",
    ]

    if not result.role_statuses:
        lines.append("- none")
    for role in result.role_statuses:
        age = "unknown age" if role.review_age_days is None else f"{role.review_age_days}d"
        lines.append(
            "- "
            f"{role.role_id}: {role.freshness}; "
            f"reviewed {role.last_reviewed_at or 'unknown'} ({age}); "
            f"sources={role.primary_source_count}; "
            f"promotion_gates={role.promotion_gate_count}; "
            f"next={role.next_review_trigger or 'not recorded'}"
        )

    if result.validation.problems:
        lines.append("")
        lines.append("Validation Problems")
        lines.extend(f"- {problem}" for problem in result.validation.problems)

    lines.append("")
    lines.append(
        "Boundary: source packs inform roles; they do not authorize actions, "
        "public claims, sends, or runtime changes."
    )
    return "\n".join(lines) + "\n"


def run_source_pack_dashboard(
    config: DtpConfig,
    *,
    path: Path | None = None,
    output_path: Path | None = None,
    today: date | None = None,
) -> SourcePackDashboardResult:
    """Render the source-pack status dashboard as a local HTML artifact."""

    status = run_source_pack_status(config, path=path, today=today)
    html = render_source_pack_dashboard(status, config.repo_root)
    destination = _resolve_path(
        config.repo_root,
        output_path or DEFAULT_SOURCE_PACK_DASHBOARD_PATH,
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(html, encoding="utf-8", newline="\n")
    stale_or_review_count = sum(
        1
        for role in status.role_statuses
        if role.freshness in {"review_soon", "stale", "date_missing"}
    )
    return SourcePackDashboardResult(
        path=destination,
        html=html,
        role_count=len(status.role_statuses),
        stale_or_review_count=stale_or_review_count,
        validation_ok=status.validation.ok,
    )


def render_source_pack_dashboard(
    result: SourcePackStatusResult,
    repo_root: Path,
    *,
    generated_at: datetime | None = None,
) -> str:
    """Render source-pack status as a static dashboard."""

    generated = (generated_at or datetime.now(UTC)).strftime("%Y-%m-%d %H:%M UTC")
    freshness_counts = ", ".join(
        f"{key}: {value}" for key, value in result.freshness_counts.items()
    )
    role_rows = "\n".join(_render_role_row(role) for role in result.role_statuses)
    if not role_rows:
        role_rows = '<tr><td colspan="10">No role packs found.</td></tr>'
    problem_rows = "\n".join(
        f"<li>{escape(problem)}</li>" for problem in result.validation.problems
    )
    if not problem_rows:
        problem_rows = "<li>No validation problems.</li>"
    display_path = escape(_display_path(repo_root, result.path))
    validation_class = "ok" if result.validation.ok else "needs-work"
    validation_label = "ok" if result.validation.ok else "needs work"
    role_count = len(result.role_statuses)
    updated_at = escape(result.updated_at or "unknown")
    freshness_label = escape(freshness_counts or "none")

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Source Pack Status Dashboard</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f6f7f2;
      --ink: #18211c;
      --muted: #5d675f;
      --panel: #ffffff;
      --line: #dce2da;
      --green: #28664a;
      --amber: #8a6424;
      --red: #944040;
      --blue: #285c84;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system,
        BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.45;
    }}
    main {{ max-width: 1180px; margin: 0 auto; padding: 28px; }}
    header {{
      display: flex;
      flex-wrap: wrap;
      gap: 18px;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 20px;
    }}
    h1 {{ font-size: 30px; margin: 0 0 6px; }}
    h2 {{ font-size: 18px; margin: 0 0 12px; }}
    p {{ margin: 0; }}
    .muted {{ color: var(--muted); }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
      margin-bottom: 16px;
    }}
    .metric, section {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
    }}
    .metric {{ padding: 14px; }}
    .metric strong {{ display: block; font-size: 24px; }}
    section {{ padding: 16px; margin-top: 14px; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
    th, td {{
      text-align: left;
      vertical-align: top;
      padding: 10px;
      border-bottom: 1px solid var(--line);
    }}
    th {{
      color: var(--muted);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: .04em;
    }}
    .pill {{
      display: inline-block;
      border-radius: 999px;
      padding: 3px 8px;
      font-size: 12px;
      font-weight: 700;
    }}
    .current {{ background: #dfeee5; color: var(--green); }}
    .review_soon {{ background: #f5ead4; color: var(--amber); }}
    .stale, .date_missing {{ background: #f5dddd; color: var(--red); }}
    .ok {{ color: var(--green); font-weight: 700; }}
    .needs-work {{ color: var(--red); font-weight: 700; }}
    code {{
      background: #eef1ec;
      border: 1px solid var(--line);
      border-radius: 4px;
      padding: 2px 5px;
    }}
    ul {{ margin: 0; padding-left: 20px; }}
    @media (max-width: 800px) {{
      main {{ padding: 18px; }}
      .grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
      table {{ display: block; overflow-x: auto; white-space: nowrap; }}
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <div>
        <h1>Source Pack Status Dashboard</h1>
        <p class="muted">
          Generated {escape(generated)} from <code>{display_path}</code>.
        </p>
      </div>
      <p class="{validation_class}">validation: {validation_label}</p>
    </header>

    <div class="grid">
      <div class="metric">
        <span class="muted">Roles</span><strong>{role_count}</strong>
      </div>
      <div class="metric">
        <span class="muted">Primary Sources</span>
        <strong>{result.primary_source_count}</strong>
      </div>
      <div class="metric">
        <span class="muted">Updated</span><strong>{updated_at}</strong>
      </div>
      <div class="metric">
        <span class="muted">Freshness</span><strong>{freshness_label}</strong>
      </div>
    </div>

    <section>
      <h2>Role Status</h2>
      <table>
        <thead>
          <tr>
            <th>Role</th>
            <th>Freshness</th>
            <th>Reviewed</th>
            <th>Sources</th>
            <th>Strong</th>
            <th>Discovery</th>
            <th>Web</th>
            <th>Blocked</th>
            <th>Gates</th>
            <th>Next Review Trigger</th>
          </tr>
        </thead>
        <tbody>
          {role_rows}
        </tbody>
      </table>
    </section>

    <section>
      <h2>Validation Problems</h2>
      <ul>
        {problem_rows}
      </ul>
    </section>

    <section>
      <h2>Operating Boundary</h2>
      <p>
        Source packs inform roles. They do not authorize actions, public
        claims, sends, legal/finance/compliance assurances, repo mutation,
        production deployment, or autonomous runtime behavior.
      </p>
    </section>
  </main>
</body>
</html>
"""


def _validate_authority_boundary(
    root: dict[str, Any],
    checks: list[str],
    problems: list[str],
) -> None:
    boundary = _require_mapping(root, "authority_boundary", "$", problems)
    if boundary is None:
        return

    expected_flags = {
        "adds_authority": False,
        "allows_web_search": True,
        "allows_autonomous_actions": False,
        "requires_human_promotion": True,
    }
    for key, expected in expected_flags.items():
        value = boundary.get(key)
        if value is expected:
            continue
        if key not in boundary:
            problems.append(f"$.authority_boundary missing field: {key}")
        else:
            problems.append(
                f"$.authority_boundary.{key} expected {expected!r}, found {value!r}"
            )

    if not any(problem.startswith("$.authority_boundary") for problem in problems):
        checks.append("source pack authority boundary locked")


def _validate_evidence_tiers(
    root: dict[str, Any],
    checks: list[str],
    problems: list[str],
) -> set[int]:
    tiers = _require_non_empty_list(root, "evidence_tiers", "$", problems)
    found: set[int] = set()
    if tiers is None:
        return found

    for index, item in enumerate(tiers):
        pointer = f"$.evidence_tiers[{index}]"
        tier = _expect_mapping(item, pointer, problems)
        if tier is None:
            continue
        tier_value = tier.get("tier")
        if isinstance(tier_value, int):
            found.add(tier_value)
        else:
            problems.append(f"{pointer}.tier must be an integer")
        _require_non_empty_str(tier, "label", pointer, problems)
        _require_non_empty_str(tier, "confidence_posture", pointer, problems)

    if found == EXPECTED_EVIDENCE_TIERS:
        checks.append("source pack evidence tiers: 0-4")
    else:
        problems.append(
            "$.evidence_tiers expected tiers "
            f"{sorted(EXPECTED_EVIDENCE_TIERS)}, found {sorted(found)}"
        )

    return found


def _validate_packs(
    root: dict[str, Any],
    repo_root: Path,
    evidence_tiers: set[int],
    role_ids: list[str],
    checks: list[str],
    problems: list[str],
) -> None:
    packs = _require_non_empty_list(root, "packs", "$", problems)
    if packs is None:
        return

    seen_roles: set[str] = set()
    for index, item in enumerate(packs):
        pointer = f"$.packs[{index}]"
        pack = _expect_mapping(item, pointer, problems)
        if pack is None:
            continue

        role_id = _require_non_empty_str(pack, "role_id", pointer, problems)
        if role_id:
            role_ids.append(role_id)
            if role_id in seen_roles:
                problems.append(f"{pointer}.role_id duplicate role id: {role_id}")
            seen_roles.add(role_id)

        for key in (
            "role_name",
            "source_pack_version",
            "status",
            "last_reviewed_at",
            "next_review_trigger",
        ):
            _require_non_empty_str(pack, key, pointer, problems)

        _require_string_list(pack, "allowed_web_sources", pointer, problems)
        _require_string_list(pack, "blocked_sources", pointer, problems)
        _require_string_list(pack, "default_outputs", pointer, problems)
        _require_string_list(pack, "promotion_required_for", pointer, problems)

        pilot_artifacts = _require_string_list(
            pack,
            "pilot_artifacts",
            pointer,
            problems,
        )
        if pilot_artifacts:
            _validate_local_artifacts(
                repo_root,
                pilot_artifacts,
                f"{pointer}.pilot_artifacts",
                problems,
            )

        _validate_primary_sources(pack, pointer, evidence_tiers, problems)
        _validate_search_posture(pack, pointer, problems)

    if len(role_ids) == len(seen_roles) and role_ids:
        checks.append("source pack role ids unique")
    checks.append(f"source pack packs validated: {len(role_ids)}")


def _validate_primary_sources(
    pack: dict[str, Any],
    pointer: str,
    evidence_tiers: set[int],
    problems: list[str],
) -> None:
    sources = _require_non_empty_list(pack, "primary_sources", pointer, problems)
    if sources is None:
        return

    seen_sources: set[str] = set()
    for index, item in enumerate(sources):
        source_pointer = f"{pointer}.primary_sources[{index}]"
        source = _expect_mapping(item, source_pointer, problems)
        if source is None:
            continue

        source_id = _require_non_empty_str(source, "id", source_pointer, problems)
        if source_id:
            if source_id in seen_sources:
                problems.append(
                    f"{source_pointer}.id duplicate primary source id: {source_id}"
                )
            seen_sources.add(source_id)

        tier = source.get("tier")
        if not isinstance(tier, int):
            problems.append(f"{source_pointer}.tier must be an integer")
        elif evidence_tiers and tier not in evidence_tiers:
            problems.append(f"{source_pointer}.tier references unknown tier: {tier}")

        for key in ("type", "path_or_url", "use", "evidence_limit"):
            _require_non_empty_str(source, key, source_pointer, problems)


def _validate_search_posture(
    pack: dict[str, Any],
    pointer: str,
    problems: list[str],
) -> None:
    posture = _require_mapping(pack, "search_posture", pointer, problems)
    if posture is None:
        return

    _require_non_empty_str(posture, "default", f"{pointer}.search_posture", problems)
    _require_non_empty_str(
        posture,
        "broad_web_confidence",
        f"{pointer}.search_posture",
        problems,
    )
    _require_string_list(
        posture,
        "preferred_queries",
        f"{pointer}.search_posture",
        problems,
    )


def _validate_local_artifacts(
    repo_root: Path,
    artifacts: list[str],
    pointer: str,
    problems: list[str],
) -> None:
    for index, artifact in enumerate(artifacts):
        if artifact.startswith(("http://", "https://")):
            continue
        artifact_path = repo_root / artifact
        if not artifact_path.exists():
            problems.append(f"{pointer}[{index}] points to missing file: {artifact}")


def _require_mapping(
    mapping: dict[str, Any],
    key: str,
    pointer: str,
    problems: list[str],
) -> dict[str, Any] | None:
    if key not in mapping:
        problems.append(f"{pointer} missing field: {key}")
        return None
    return _expect_mapping(mapping[key], f"{pointer}.{key}", problems)


def _expect_mapping(
    value: Any,
    pointer: str,
    problems: list[str],
) -> dict[str, Any] | None:
    if isinstance(value, dict):
        return value
    problems.append(f"{pointer} must be an object")
    return None


def _require_non_empty_list(
    mapping: dict[str, Any],
    key: str,
    pointer: str,
    problems: list[str],
) -> list[Any] | None:
    if key not in mapping:
        problems.append(f"{pointer} missing field: {key}")
        return None
    value = mapping[key]
    if not isinstance(value, list):
        problems.append(f"{pointer}.{key} must be a list")
        return None
    if not value:
        problems.append(f"{pointer}.{key} must not be empty")
        return None
    return value


def _require_string_list(
    mapping: dict[str, Any],
    key: str,
    pointer: str,
    problems: list[str],
) -> list[str] | None:
    values = _require_non_empty_list(mapping, key, pointer, problems)
    if values is None:
        return None

    strings: list[str] = []
    for index, value in enumerate(values):
        if isinstance(value, str) and value.strip():
            strings.append(value)
        else:
            problems.append(f"{pointer}.{key}[{index}] must be a non-empty string")
    return strings


def _require_non_empty_str(
    mapping: dict[str, Any],
    key: str,
    pointer: str,
    problems: list[str],
) -> str | None:
    if key not in mapping:
        problems.append(f"{pointer} missing field: {key}")
        return None
    value = mapping[key]
    if isinstance(value, str) and value.strip():
        return value
    problems.append(f"{pointer}.{key} must be a non-empty string")
    return None


def _resolve_path(repo_root: Path, path: Path) -> Path:
    if path.is_absolute():
        return path
    return repo_root / path


def _display_path(repo_root: Path, path: Path) -> str:
    try:
        return path.relative_to(repo_root).as_posix()
    except ValueError:
        return str(path)


def _read_source_pack_payload(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    if isinstance(payload, dict):
        return payload
    return {}


def _build_role_statuses(
    payload: dict[str, Any],
    today: date,
) -> tuple[SourcePackRoleStatus, ...]:
    roles: list[SourcePackRoleStatus] = []
    for pack in _mapping_list(payload.get("packs")):
        primary_sources = _mapping_list(pack.get("primary_sources"))
        allowed_web_sources = _string_list(pack.get("allowed_web_sources"))
        blocked_sources = _string_list(pack.get("blocked_sources"))
        promotion_gates = _string_list(pack.get("promotion_required_for"))
        pilot_artifacts = _string_list(pack.get("pilot_artifacts"))
        search_posture = pack.get("search_posture")
        if not isinstance(search_posture, dict):
            search_posture = {}
        last_reviewed = _as_str(pack.get("last_reviewed_at"))
        age_days = _review_age_days(last_reviewed, today)
        roles.append(
            SourcePackRoleStatus(
                role_id=_as_str(pack.get("role_id")),
                role_name=_as_str(pack.get("role_name")),
                status=_as_str(pack.get("status")),
                freshness=_freshness(age_days),
                last_reviewed_at=last_reviewed,
                review_age_days=age_days,
                primary_source_count=len(primary_sources),
                strong_source_count=sum(
                    1
                    for source in primary_sources
                    if isinstance(source.get("tier"), int) and source["tier"] <= 2
                ),
                discovery_source_count=sum(
                    1
                    for source in primary_sources
                    if isinstance(source.get("tier"), int) and source["tier"] >= 3
                ),
                allowed_web_source_count=len(allowed_web_sources),
                blocked_source_count=len(blocked_sources),
                promotion_gate_count=len(promotion_gates),
                pilot_artifact_count=len(pilot_artifacts),
                search_default=_as_str(search_posture.get("default")),
                broad_web_confidence=_as_str(search_posture.get("broad_web_confidence")),
                next_review_trigger=_as_str(pack.get("next_review_trigger")),
            )
        )
    return tuple(roles)


def _render_role_row(role: SourcePackRoleStatus) -> str:
    age = "" if role.review_age_days is None else f" ({role.review_age_days}d)"
    role_label = escape(role.role_name or role.role_id)
    role_id = escape(role.role_id)
    freshness = escape(role.freshness)
    freshness_label = escape(role.freshness.replace("_", " "))
    reviewed = escape(role.last_reviewed_at or "unknown")
    next_review = escape(role.next_review_trigger or "not recorded")
    return f"""<tr>
  <td><strong>{role_label}</strong><br><span class="muted">{role_id}</span></td>
  <td><span class="pill {freshness}">{freshness_label}</span></td>
  <td>{reviewed}{escape(age)}</td>
  <td>{role.primary_source_count}</td>
  <td>{role.strong_source_count}</td>
  <td>{role.discovery_source_count}</td>
  <td>{role.allowed_web_source_count}</td>
  <td>{role.blocked_source_count}</td>
  <td>{role.promotion_gate_count}</td>
  <td>{next_review}</td>
</tr>"""


def _review_age_days(value: str, today: date) -> int | None:
    if not value:
        return None
    try:
        reviewed = date.fromisoformat(value)
    except ValueError:
        return None
    return (today - reviewed).days


def _freshness(age_days: int | None) -> str:
    if age_days is None:
        return "date_missing"
    if age_days <= 30:
        return "current"
    if age_days <= 90:
        return "review_soon"
    return "stale"


def _mapping_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str) and item.strip()]


def _as_str(value: Any) -> str:
    if isinstance(value, str):
        return value.strip()
    return ""
