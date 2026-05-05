from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from enum import StrEnum
from html import escape
from pathlib import Path

from dtp.commands.kaizen import KaizenRecord, read_kaizen_records
from dtp.commands.workspace_report import RepoReport, WorkspaceReport, run_workspace_report
from dtp.config import DtpConfig

STATUS_ORDER = ("now", "next", "waiting", "blocked", "parked")
STATUS_LABELS = {
    "now": "Now",
    "next": "Next",
    "waiting": "Waiting",
    "blocked": "Blocked",
    "parked": "Parked",
}


class DashboardSurface(StrEnum):
    browser = "browser"
    vscode = "vscode"


@dataclass(frozen=True)
class ProofQueueRow:
    candidate: str
    lane: str
    status: str
    next_action: str
    gates: str


@dataclass(frozen=True)
class WorkspaceDashboardResult:
    path: Path
    html: str
    repo_count: int
    active_item_count: int
    proof_candidate_count: int


def run_workspace_dashboard(
    config: DtpConfig,
    *,
    output_path: Path | None = None,
    surface: DashboardSurface | str = DashboardSurface.browser,
) -> WorkspaceDashboardResult:
    surface = DashboardSurface(surface)
    report = run_workspace_report(config)
    records = read_kaizen_records(config)
    proof_queue = read_proof_queue(config)
    generated_at = datetime.now(UTC).isoformat(timespec="seconds")
    html = render_workspace_dashboard(
        report=report,
        records=records,
        proof_queue=proof_queue,
        generated_at=generated_at,
        surface=surface,
    )
    path = _resolve_output_path(config.repo_root, output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8", newline="\n")
    return WorkspaceDashboardResult(
        path=path,
        html=html,
        repo_count=len(report.repos),
        active_item_count=sum(1 for record in records if record.status in STATUS_ORDER),
        proof_candidate_count=len(proof_queue),
    )


def render_workspace_dashboard(
    *,
    report: WorkspaceReport,
    records: tuple[KaizenRecord, ...],
    proof_queue: tuple[ProofQueueRow, ...],
    generated_at: str,
    surface: DashboardSurface | str = DashboardSurface.browser,
) -> str:
    surface = DashboardSurface(surface)
    records_by_status = {
        status: tuple(record for record in records if record.status == status)
        for status in STATUS_ORDER
    }
    repo_rows = sorted(report.repos, key=_repo_sort_key)
    counts = {status: len(records_by_status[status]) for status in STATUS_ORDER}
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Practice Work Dashboard</title>
  <style>
    {_dashboard_style(surface)}
  </style>
</head>
<body class="{escape(surface.value)}">
  <header>
    <h1>Practice Work Dashboard</h1>
    <p class="meta">Generated {escape(generated_at)} from DTP read-only artifacts.
    This view shows what is active, waiting, blocked, and proof-gated without
    running live repo, cloud, or GitHub commands.</p>
    <div class="summary">
      {_metric("Now", counts["now"])}
      {_metric("Next", counts["next"])}
      {_metric("Waiting", counts["waiting"])}
      {_metric("Blocked", counts["blocked"])}
      {_metric("Repos", len(repo_rows))}
      {_metric("Proof Candidates", len(proof_queue))}
    </div>
  </header>
  <main>
    <div class="grid">
      <div class="stack">
        <section>
          <h2>Current Work</h2>
          <div class="status-grid">
            {''.join(_status_lane(status, records_by_status[status]) for status in STATUS_ORDER)}
          </div>
        </section>
        <section>
          <h2>Proof Queue</h2>
          {_proof_table(proof_queue)}
        </section>
      </div>
      <div class="stack">
        <section>
          <h2>Repo Coverage</h2>
          {_repo_table(repo_rows)}
        </section>
        <section>
          <h2>Open Gates</h2>
          {_blocker_list(report.blockers)}
          <div class="boundary">
            Boundary: {escape(report.boundary)}. Live status: {escape(report.live_status)}.
            This dashboard does not publish proof, read secrets, mutate repos,
            send client communications, or replace repo-local validation.
          </div>
        </section>
      </div>
    </div>
  </main>
</body>
</html>
"""
    return html


def read_proof_queue(config: DtpConfig) -> tuple[ProofQueueRow, ...]:
    path = config.repo_root / "docs" / "PRACTICE_PROOF_QUEUE_INDEX.md"
    if not path.exists():
        return ()
    lines = path.read_text(encoding="utf-8").splitlines()
    rows: list[ProofQueueRow] = []
    in_section = False
    for line in lines:
        stripped = line.strip()
        if stripped == "## Current Proof Candidates":
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            break
        if not in_section or not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) < 7 or cells[0].lower() == "candidate" or set(cells[0]) == {"-"}:
            continue
        rows.append(
            ProofQueueRow(
                candidate=_clean_cell(cells[0]),
                lane=_clean_cell(cells[1]),
                status=_clean_cell(cells[4]),
                next_action=_clean_cell(cells[5]),
                gates=_clean_cell(cells[6]),
            )
        )
    return tuple(rows)


def _resolve_output_path(repo_root: Path, output_path: Path | None) -> Path:
    path = output_path or Path("docs/workspace-dashboard.html")
    if not path.is_absolute():
        path = repo_root / path
    return path.resolve()


def _dashboard_style(surface: DashboardSurface) -> str:
    base = """
    :root {
      color-scheme: light;
      --ink: #1f2933;
      --muted: #5f6b7a;
      --line: #d8dee8;
      --paper: #f6f4ef;
      --panel: #ffffff;
      --accent: #315f72;
      --ok: #1f7a57;
      --warn: #a15c12;
      --risk: #9c2f3f;
      --hold: #665c92;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system,
        BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: var(--paper);
      color: var(--ink);
      line-height: 1.45;
    }
    header, main { width: min(1480px, calc(100vw - 32px)); margin: 0 auto; }
    header { padding: 28px 0 18px; border-bottom: 1px solid var(--line); }
    h1 { margin: 0; font-size: clamp(28px, 4vw, 48px); letter-spacing: 0; }
    h2 { margin: 0 0 12px; font-size: 18px; letter-spacing: 0; }
    h3 { margin: 0 0 6px; font-size: 15px; letter-spacing: 0; }
    p { margin: 0; }
    a { color: var(--accent); }
    .meta { color: var(--muted); margin-top: 6px; max-width: 900px; }
    .summary {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
      gap: 10px;
      margin: 18px 0 0;
    }
    .metric {
      min-height: 82px;
      padding: 12px;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
    }
    .metric strong { display: block; font-size: 26px; line-height: 1; margin-bottom: 8px; }
    .metric span { color: var(--muted); font-size: 13px; }
    .grid {
      display: grid;
      grid-template-columns: minmax(0, 1.05fr) minmax(360px, .95fr);
      gap: 16px;
      align-items: start;
      margin: 18px 0 36px;
    }
    section {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 16px;
      overflow: hidden;
    }
    .stack { display: grid; gap: 12px; }
    .status-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 12px;
    }
    .lane {
      border-left: 4px solid var(--accent);
      padding: 10px 10px 12px;
      background: #fdfbf7;
      min-height: 170px;
    }
    .lane.now { border-color: var(--ok); }
    .lane.next { border-color: var(--accent); }
    .lane.waiting { border-color: var(--warn); }
    .lane.blocked { border-color: var(--risk); }
    .lane.parked { border-color: var(--hold); }
    .item { padding: 10px 0; border-top: 1px solid var(--line); }
    .item:first-of-type { border-top: 0; }
    .title { font-weight: 700; }
    .small { color: var(--muted); font-size: 12px; margin-top: 4px; }
    table { width: 100%; border-collapse: collapse; table-layout: fixed; }
    th, td {
      padding: 9px 8px;
      border-top: 1px solid var(--line);
      text-align: left;
      vertical-align: top;
      overflow-wrap: anywhere;
      font-size: 13px;
    }
    th { color: var(--muted); font-weight: 700; border-top: 0; }
    .status-pill {
      display: inline-block;
      padding: 2px 7px;
      border-radius: 999px;
      border: 1px solid var(--line);
      background: #f8fafc;
      color: var(--muted);
      font-size: 12px;
      font-weight: 700;
    }
    .boundary {
      margin-top: 12px;
      padding: 12px;
      background: #fdfbf7;
      border: 1px solid var(--line);
      border-radius: 8px;
      color: var(--muted);
      font-size: 13px;
    }
    @media (max-width: 900px) {
      header, main { width: min(100% - 20px, 1480px); }
      .grid { grid-template-columns: 1fr; }
      section { padding: 12px; }
      th, td { font-size: 12px; }
    }
"""
    if surface != DashboardSurface.vscode:
        return base
    return (
        base
        + """
    :root {
      color-scheme: light dark;
      --ink: var(--vscode-foreground, #1f2933);
      --muted: var(--vscode-descriptionForeground, #5f6b7a);
      --line: var(--vscode-panel-border, #3c3c3c);
      --paper: var(--vscode-editor-background, #1e1e1e);
      --panel: var(--vscode-sideBar-background, #252526);
      --accent: var(--vscode-textLink-foreground, #4ea3d8);
      --ok: var(--vscode-charts-green, #4caf50);
      --warn: var(--vscode-charts-yellow, #cca700);
      --risk: var(--vscode-charts-red, #f14c4c);
      --hold: var(--vscode-charts-purple, #c586c0);
    }
    body {
      font-family: var(--vscode-font-family, "Segoe UI", sans-serif);
      font-size: var(--vscode-font-size, 13px);
    }
    header, main { width: min(100% - 24px, 1540px); }
    header { padding: 18px 0 14px; }
    h1 { font-size: 26px; }
    h2 { font-size: 16px; }
    h3 { font-size: 13px; text-transform: uppercase; color: var(--muted); }
    .meta { max-width: 980px; }
    .summary { grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); }
    .metric { min-height: 66px; background: var(--panel); }
    .metric strong { font-size: 22px; }
    .grid { grid-template-columns: minmax(0, 1.18fr) minmax(360px, .82fr); }
    section { background: var(--panel); }
    .lane, .boundary { background: var(--vscode-editorWidget-background, var(--panel)); }
    .status-pill {
      background: var(--vscode-badge-background, #4d4d4d);
      color: var(--vscode-badge-foreground, #ffffff);
    }
    th, td { font-size: 12px; }
"""
    )


def _metric(label: str, value: int) -> str:
    return (
        '<div class="metric">'
        f"<strong>{escape(str(value))}</strong>"
        f"<span>{escape(label)}</span>"
        "</div>"
    )


def _status_lane(status: str, records: tuple[KaizenRecord, ...]) -> str:
    label = STATUS_LABELS[status]
    items = "".join(_kaizen_item(record) for record in records[-6:])
    if not items:
        items = '<p class="small">Nothing recorded.</p>'
    return f'<div class="lane {escape(status)}"><h3>{escape(label)}</h3>{items}</div>'


def _kaizen_item(record: KaizenRecord) -> str:
    return (
        '<div class="item">'
        f'<p class="title">{escape(record.title)}</p>'
        f'<p class="small">{escape(record.repo)} · {escape(record.item_type)}</p>'
        f'<p class="small">Next: {escape(record.next_action)}</p>'
        "</div>"
    )


def _proof_table(rows: tuple[ProofQueueRow, ...]) -> str:
    if not rows:
        return '<p class="small">No proof candidates recorded.</p>'
    body = "".join(
        "<tr>"
        f"<td>{escape(row.candidate)}</td>"
        f"<td>{escape(row.lane)}</td>"
        f'<td><span class="status-pill">{escape(row.status)}</span></td>'
        f"<td>{escape(row.next_action)}</td>"
        f"<td>{escape(row.gates)}</td>"
        "</tr>"
        for row in rows
    )
    return (
        "<table>"
        "<thead><tr><th>Candidate</th><th>Lane</th><th>Status</th>"
        "<th>Next</th><th>Gate</th></tr></thead>"
        f"<tbody>{body}</tbody>"
        "</table>"
    )


def _repo_table(rows: list[RepoReport]) -> str:
    body = "".join(
        "<tr>"
        f"<td>{escape(row.repo)}</td>"
        f"<td>{escape(row.owner_lane or 'unknown')}</td>"
        f'<td><span class="status-pill">{escape(_coverage_status(row))}</span></td>'
        f"<td>{escape(_latest(row))}</td>"
        f"<td>{escape(row.next_action or 'not recorded')}</td>"
        f"<td>{escape(row.blocker or 'none')}</td>"
        "</tr>"
        for row in rows
    )
    return (
        "<table>"
        "<thead><tr><th>Repo</th><th>Lane</th><th>Coverage</th><th>Latest</th>"
        "<th>Next</th><th>Gate</th></tr></thead>"
        f"<tbody>{body}</tbody>"
        "</table>"
    )


def _blocker_list(blockers: tuple[str, ...]) -> str:
    if not blockers:
        return '<p class="small">No active gates recorded in the workspace report.</p>'
    items = "".join(f"<li>{escape(blocker)}</li>" for blocker in blockers)
    return f"<ul>{items}</ul>"


def _coverage_status(row: RepoReport) -> str:
    if row.manifest_status == "ok" and row.evidence_status == "ok":
        return "recorded"
    return "missing"


def _latest(row: RepoReport) -> str:
    if not row.latest_verification:
        return "not recorded"
    latest = row.latest_verification[0]
    return f"{latest.lane}: {latest.result} ({latest.date})"


def _repo_sort_key(row: RepoReport) -> tuple[int, str]:
    has_gate = 0 if row.blocker else 1
    return (has_gate, row.repo.lower())


def _clean_cell(value: str) -> str:
    return value.replace("`", "").replace("<br>", " ").strip()
