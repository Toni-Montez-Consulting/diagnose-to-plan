from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from enum import StrEnum
from html import escape
from pathlib import Path
from typing import Any

from dtp.commands.workspace_report import RepoReport, WorkspaceReport, run_workspace_report
from dtp.commands.workspace_tasks import (
    ACTIVE_TASK_STATUSES,
    PRIVATE_TASK_SENSITIVITIES,
    TERMINAL_TASK_STATUSES,
    WorkspaceTask,
    build_workspace_dashboard_tasks,
    build_workspace_recovery_inbox_tasks,
    collect_workspace_task_source_candidates,
    recover_workspace_task_candidates,
    write_notion_cockpit_export,
)
from dtp.config import DtpConfig

STATUS_ORDER = ("now", "next", "waiting", "blocked", "parked", "decision_needed", "inbox")
CLOSED_STATUS_ORDER = TERMINAL_TASK_STATUSES
STATUS_LABELS = {
    "inbox": "Inbox",
    "now": "Now",
    "next": "Next",
    "waiting": "Waiting",
    "blocked": "Blocked",
    "parked": "Parked",
    "decision_needed": "Decision Needed",
    "done": "Done",
    "cancelled": "Cancelled",
    "superseded": "Superseded",
    "discarded": "Discarded",
}
RECOVERY_BUCKETS = (
    "high_confidence_import",
    "merge_review",
    "codex_session_lead",
    "memory_pointer",
    "private_coi_gated",
    "likely_discard",
)
RECOVERY_BUCKET_LABELS = {
    "high_confidence_import": "High-confidence import",
    "merge_review": "Merge/duplicate review",
    "codex_session_lead": "Codex-session lead",
    "memory_pointer": "Memory pointer",
    "private_coi_gated": "Private/COI gated",
    "likely_discard": "Likely discard",
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
class SweepCoverageRow:
    scope: str
    coverage: str
    notes: str


@dataclass(frozen=True)
class WorkspaceDashboardResult:
    path: Path
    html: str
    repo_count: int
    active_item_count: int
    closed_item_count: int
    recovery_inbox_count: int
    proof_candidate_count: int
    sweep_scope_count: int


@dataclass(frozen=True)
class WorkspaceDashboardValidationResult:
    ok: bool
    summary: dict[str, Any]
    json_path: Path
    markdown_path: Path


def run_workspace_dashboard(
    config: DtpConfig,
    *,
    output_path: Path | None = None,
    surface: DashboardSurface | str = DashboardSurface.browser,
) -> WorkspaceDashboardResult:
    surface = DashboardSurface(surface)
    report = run_workspace_report(config)
    proof_queue = read_proof_queue(config)
    sweep_coverage = read_sweep_coverage(config)
    tasks = build_workspace_dashboard_tasks(config)
    recovery_inbox = build_workspace_recovery_inbox_tasks(config)
    generated_at = datetime.now(UTC).isoformat(timespec="seconds")
    html = render_workspace_dashboard(
        report=report,
        tasks=tasks,
        recovery_inbox=recovery_inbox,
        proof_queue=proof_queue,
        sweep_coverage=sweep_coverage,
        generated_at=generated_at,
        surface=surface,
    )
    path = _resolve_output_path(config.repo_root, output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8", newline="\n")
    write_notion_cockpit_export(config, tasks)
    return WorkspaceDashboardResult(
        path=path,
        html=html,
        repo_count=len(report.repos),
        active_item_count=sum(1 for task in tasks if task.status in ACTIVE_TASK_STATUSES),
        closed_item_count=sum(1 for task in tasks if task.status in TERMINAL_TASK_STATUSES),
        recovery_inbox_count=len(recovery_inbox),
        proof_candidate_count=len(proof_queue),
        sweep_scope_count=len(sweep_coverage),
    )


def run_workspace_dashboard_validation(config: DtpConfig) -> WorkspaceDashboardValidationResult:
    report = run_workspace_report(config)
    proof_queue = read_proof_queue(config)
    sweep_coverage = read_sweep_coverage(config)
    dashboard_source_rows = collect_workspace_task_source_candidates(
        config,
        include_codex_sessions=False,
        include_memory_registry=False,
    )
    all_source_rows = collect_workspace_task_source_candidates(config)
    tasks = recover_workspace_task_candidates(
        config,
        include_codex_sessions=False,
        include_memory_registry=False,
    )
    all_candidates = recover_workspace_task_candidates(config)
    recovery_inbox = build_workspace_recovery_inbox_tasks(config)
    html = render_workspace_dashboard(
        report=report,
        tasks=tasks,
        recovery_inbox=recovery_inbox,
        proof_queue=proof_queue,
        sweep_coverage=sweep_coverage,
        generated_at=datetime.now(UTC).isoformat(timespec="seconds"),
    )
    expected_metrics = {
        "Needs Attention": len(_attention_tasks(tasks)),
        "Waiting On Toni/Owner": sum(1 for task in tasks if task.status == "waiting"),
        "Blocked": sum(1 for task in tasks if task.status == "blocked"),
        "Decision Needed": sum(1 for task in tasks if task.status == "decision_needed"),
        "Proof Blocked": len(_proof_blocked_tasks(tasks)),
        "Recently Closed": sum(1 for task in tasks if task.status in CLOSED_STATUS_ORDER),
    }
    metric_mismatches = [
        f"{label}: expected {expected}, rendered {_rendered_metric_count(html, label)}"
        for label, expected in expected_metrics.items()
        if _rendered_metric_count(html, label) != expected
    ]
    register_metric_counts = {
        "Needs Attention": _rendered_register_filter_count(html, "attention"),
        "Waiting On Toni/Owner": _rendered_register_filter_count(html, "status:waiting"),
        "Blocked": _rendered_register_filter_count(html, "status:blocked"),
        "Decision Needed": _rendered_register_filter_count(html, "status:decision_needed"),
        "Proof Blocked": _rendered_register_filter_count(html, "proof-risk"),
        "Recently Closed": _rendered_register_filter_count(html, "closed"),
    }
    register_mismatches = [
        f"{label} register rows: expected {expected}, rendered {register_metric_counts[label]}"
        for label, expected in expected_metrics.items()
        if register_metric_counts[label] != expected
    ]
    rendered_counts = {
        "register_rows": _rendered_attr_count(
            html,
            'data-panel="register" data-section-role="register"',
        ),
        "archive_rows": _rendered_attr_count(
            html,
            'data-panel="archive" data-section-role="lane"',
        ),
        "recovery_rows": _rendered_attr_count(
            html,
            'data-panel="recovery" data-section-role="recovery"',
        ),
    }
    count_mismatches = list(metric_mismatches)
    if rendered_counts["register_rows"] != len(tasks):
        count_mismatches.append(
            f"register rows: expected {len(tasks)}, rendered {rendered_counts['register_rows']}"
        )
    closed_count = sum(1 for task in tasks if task.status in CLOSED_STATUS_ORDER)
    if rendered_counts["archive_rows"] != closed_count:
        count_mismatches.append(
            f"archive rows: expected {closed_count}, rendered {rendered_counts['archive_rows']}"
        )
    if rendered_counts["recovery_rows"] != len(recovery_inbox):
        count_mismatches.append(
            "recovery rows: expected "
            f"{len(recovery_inbox)}, rendered {rendered_counts['recovery_rows']}"
        )
    count_mismatches.extend(register_mismatches)
    missing_sources = _missing_source_refs(config, (*tasks, *recovery_inbox))
    duplicate_task_ids = _duplicate_task_ids((*tasks, *recovery_inbox))
    recovery_bucket_counts = _recovery_bucket_counts(recovery_inbox)
    redaction_rows = [
        task
        for task in (*tasks, *recovery_inbox)
        if task.sensitivity in PRIVATE_TASK_SENSITIVITIES or task.title.startswith("[redacted")
    ]
    unsafe_private_rows = [
        task
        for task in (*tasks, *recovery_inbox)
        if task.sensitivity in PRIVATE_TASK_SENSITIVITIES
        and not task.title.startswith("[redacted")
    ]
    summary: dict[str, Any] = {
        "generated_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "ok": not count_mismatches and not missing_sources and not duplicate_task_ids,
        "categories": {
            "in_dashboard": len(tasks),
            "recovery_inbox": len(recovery_inbox),
            "excluded_or_redacted": len(redaction_rows),
            "duplicate_merged": len(all_source_rows) - len(all_candidates),
            "source_missing": len(missing_sources),
            "count_mismatch": len(count_mismatches),
            "duplicate_task_ids": len(duplicate_task_ids),
        },
        "reviewed_operating_rows": len(tasks),
        "closed_rows": closed_count,
        "dry_run_candidates": len(all_candidates),
        "total_accounted_for": len(tasks) + len(recovery_inbox),
        "raw_source_rows": {
            "dashboard_sources": len(dashboard_source_rows),
            "all_sources": len(all_source_rows),
        },
        "rendered_counts": rendered_counts,
        "expected_metrics": expected_metrics,
        "register_metric_counts": register_metric_counts,
        "recovery_bucket_counts": recovery_bucket_counts,
        "count_mismatches": count_mismatches,
        "missing_sources": missing_sources,
        "duplicate_task_ids": duplicate_task_ids,
        "unsafe_private_rows": [
            {"id": task.id, "title": task.title, "sensitivity": task.sensitivity}
            for task in unsafe_private_rows
        ],
    }
    json_path = config.outputs_dir / "workspace-dashboard-validation.json"
    markdown_path = config.outputs_dir / "workspace-dashboard-validation.md"
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    markdown_path.write_text(_validation_markdown(summary), encoding="utf-8", newline="\n")
    return WorkspaceDashboardValidationResult(
        ok=bool(summary["ok"]),
        summary=summary,
        json_path=json_path,
        markdown_path=markdown_path,
    )


def render_workspace_dashboard(
    *,
    report: WorkspaceReport,
    tasks: tuple[WorkspaceTask, ...],
    recovery_inbox: tuple[WorkspaceTask, ...],
    proof_queue: tuple[ProofQueueRow, ...],
    sweep_coverage: tuple[SweepCoverageRow, ...],
    generated_at: str,
    surface: DashboardSurface | str = DashboardSurface.browser,
) -> str:
    surface = DashboardSurface(surface)
    tasks_by_status = {
        status: tuple(task for task in tasks if task.status == status)
        for status in STATUS_ORDER
    }
    closed_by_status = {
        status: tuple(task for task in tasks if task.status == status)
        for status in CLOSED_STATUS_ORDER
    }
    repo_rows = sorted(report.repos, key=_repo_sort_key)
    counts = {status: len(tasks_by_status[status]) for status in STATUS_ORDER}
    attention_tasks = _attention_tasks(tasks)
    proof_blocked = _proof_blocked_tasks(tasks)
    waiting_tasks = tuple(task for task in tasks if task.status == "waiting")
    decision_tasks = tuple(task for task in tasks if task.status == "decision_needed")
    closed_tasks = tuple(task for task in tasks if task.status in CLOSED_STATUS_ORDER)
    register_tasks = tuple(sorted(tasks, key=_task_card_sort_key))
    total_detected = len(tasks) + len(recovery_inbox)
    recovery_bucket_counts = _recovery_bucket_counts(recovery_inbox)
    data_warnings = _data_health_warnings(tasks, sweep_coverage)
    workstream_lanes = "".join(
        _status_lane(status, tasks_by_status[status], panel="workstreams")
        for status in STATUS_ORDER
    )
    archive_lanes = "".join(
        _status_lane(status, closed_by_status[status], panel="archive")
        for status in CLOSED_STATUS_ORDER
    )
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
    This daily cockpit shows what needs attention, what is waiting, what is
    blocked, and what has been recovered without running live repo, cloud, or
    GitHub commands.</p>
    {_accounting_summary(len(tasks), len(recovery_inbox), total_detected, len(closed_tasks))}
    <div class="summary">
      {_metric("Needs Attention", len(attention_tasks), "register", "attention")}
      {_metric("Waiting On Toni/Owner", len(waiting_tasks), "register", "status:waiting")}
      {_metric("Blocked", counts["blocked"], "register", "status:blocked")}
      {_metric("Decision Needed", len(decision_tasks), "register", "status:decision_needed")}
      {_metric("Proof Blocked", len(proof_blocked), "register", "proof-risk")}
      {_metric("Recently Closed", len(closed_tasks), "register", "closed")}
    </div>
    <p class="metric-note">The six cards are navigation filters into the Item Register.
    Total detected means reviewed rows plus Recovery Inbox candidates, not completed work.</p>
    <div class="toolbar">
      <input id="dashboard-search" type="search" placeholder="Search tasks, repos, gates, sources">
      <div class="tabs" role="tablist" aria-label="Dashboard views">
        {_tab_button("today", "Today", True, len(attention_tasks))}
        {_tab_button("workstreams", "Workstreams", False, sum(counts.values()))}
        {_tab_button("proof", "Proof", False, len(proof_blocked))}
        {_tab_button("register", "Register", False, len(register_tasks))}
        {_tab_button("recovery", "Recovery Inbox", False, len(recovery_inbox))}
        {_tab_button("repos", "Repos", False, len(repo_rows))}
        {_tab_button("archive", "Archive", False, len(closed_tasks))}
        {_tab_button("coverage", "Coverage", False, len(sweep_coverage))}
      </div>
    </div>
    <div class="filter-bar" aria-live="polite" aria-label="Dashboard orientation">
      <span class="orientation-chip">View: <strong id="orientation-panel">Today</strong></span>
      <span class="orientation-chip">Filter:
        <strong id="orientation-filter">All rows</strong></span>
      <span id="filter-status">Showing all dashboard rows.</span>
      <button id="clear-dashboard-filter" type="button" hidden>Clear filter</button>
      <button id="jump-register" type="button">Open Register</button>
    </div>
  </header>
  <main>
    <section id="today" class="tab-panel active" data-panel="today" tabindex="-1"
      role="tabpanel" aria-labelledby="tab-today">
      <div class="cockpit-grid">
        <section class="subsection">
          <h2>Today</h2>
          <p class="small">Action cards are sorted for daily review.
          Terminal archive rows stay out of this list.</p>
          <div class="task-list">
            {_task_cards(attention_tasks, panel="today", section_role="daily-action")}
          </div>
          {_empty_state("today")}
        </section>
        <aside class="stack">
          <section class="subsection">
            <h2>Data Health</h2>
            {_warning_list(data_warnings)}
          </section>
          <section class="subsection">
            <h2>Repo Snapshot</h2>
            {_repo_snapshot(repo_rows)}
          </section>
          <section class="subsection">
            <h2>Proof Risks</h2>
            <div class="task-list compact">
              {_task_cards(proof_blocked[:5], panel="today", section_role="preview")}
            </div>
          </section>
        </aside>
      </div>
    </section>
    <section id="workstreams" class="tab-panel" data-panel="workstreams" tabindex="-1"
      role="tabpanel" aria-labelledby="tab-workstreams">
      <h2>Workstreams</h2>
      <div class="status-grid">
        {workstream_lanes}
      </div>
      {_empty_state("workstreams")}
    </section>
    <section id="proof" class="tab-panel" data-panel="proof" tabindex="-1"
      role="tabpanel" aria-labelledby="tab-proof">
      <h2>Proof</h2>
      <div class="task-list">
        {_task_cards(proof_blocked, panel="proof", section_role="proof")}
      </div>
      {_empty_state("proof")}
      <details open>
        <summary>Proof Queue Table</summary>
        {_proof_table(proof_queue)}
      </details>
    </section>
    <section id="register" class="tab-panel" data-panel="register" tabindex="-1"
      role="tabpanel" aria-labelledby="tab-register">
      <h2>Item Register</h2>
      <p id="register-status" class="register-status">
        Showing {len(register_tasks)} of {len(register_tasks)} reviewed dashboard rows.
      </p>
      {_task_register_table(register_tasks, panel="register")}
      {_empty_state("register")}
    </section>
    <section id="recovery" class="tab-panel" data-panel="recovery" tabindex="-1"
      role="tabpanel" aria-labelledby="tab-recovery">
      <h2>Recovery Inbox</h2>
      <p class="small">Unreviewed candidates are visible here so the {total_detected} dry-run
      candidates are accounted for without mixing low-confidence session or
      memory pointers into the daily operating lanes.</p>
      {_recovery_bucket_summary(recovery_bucket_counts)}
      <div class="boundary">
        Review candidates, copy the approved JSON starter, save the reviewed
        subset as <code>outputs/workspace-recovery-approved.json</code>, then run
        <code>.\\.venv\\Scripts\\python.exe -m dtp workspace recover --apply --approved
        outputs/workspace-recovery-approved.json</code>.
        The dashboard cannot write files or run commands.
      </div>
      {_recovery_inbox_table(recovery_inbox)}
      {_approved_json_template(recovery_inbox)}
      {_empty_state("recovery")}
    </section>
    <section id="repos" class="tab-panel" data-panel="repos" tabindex="-1"
      role="tabpanel" aria-labelledby="tab-repos">
      <h2>Repos</h2>
      {_repo_table(repo_rows)}
    </section>
    <section id="archive" class="tab-panel" data-panel="archive" tabindex="-1"
      role="tabpanel" aria-labelledby="tab-archive">
      <h2>Archive</h2>
      <div class="status-grid closed-grid">
        {archive_lanes}
      </div>
      {_empty_state("archive")}
    </section>
    <section id="coverage" class="tab-panel" data-panel="coverage" tabindex="-1"
      role="tabpanel" aria-labelledby="tab-coverage">
      <div class="grid">
        <section class="subsection">
          <h2>Sweep Coverage</h2>
          {_sweep_table(sweep_coverage)}
        </section>
        <section class="subsection">
          <h2>Open Gates</h2>
          {_blocker_list(report.blockers)}
          <div class="boundary">
            Boundary: {escape(report.boundary)}. Live status: {escape(report.live_status)}.
            This dashboard does not publish proof, read secrets, mutate repos,
            send client communications, or replace repo-local validation.
          </div>
        </section>
      </div>
    </section>
  </main>
  <script>
    {_dashboard_script()}
  </script>
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
        if len(cells) < 7 or cells[0].lower() == "candidate" or _is_markdown_rule(cells):
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


def read_sweep_coverage(config: DtpConfig) -> tuple[SweepCoverageRow, ...]:
    path = config.repo_root / "docs" / "WORKSPACE_DOCS_AND_CHAT_SWEEP_LEDGER_2026-05-05.md"
    if not path.exists():
        return ()
    lines = path.read_text(encoding="utf-8").splitlines()
    rows: list[SweepCoverageRow] = []
    in_section = False
    for line in lines:
        stripped = line.strip()
        if stripped == "## Sweep Coverage":
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            break
        if not in_section or not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) < 3 or cells[0].lower() == "scope" or _is_markdown_rule(cells):
            continue
        rows.append(
            SweepCoverageRow(
                scope=_clean_cell(cells[0]),
                coverage=_clean_cell(cells[1]),
                notes=_clean_cell(cells[2]),
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
      --line: #d7dde6;
      --paper: #f4f6f8;
      --panel: #ffffff;
      --accent: #315f72;
      --ok: #1f7a57;
      --warn: #a15c12;
      --risk: #9c2f3f;
      --hold: #665c92;
      --soft: #eef4f7;
      --warm: #faf7f1;
      --panel-strong: #f8fbfc;
      --shadow: 0 18px 45px rgb(31 41 51 / 9%);
      --focus: 0 0 0 3px rgb(49 95 114 / 20%);
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: Aptos, "Segoe UI Variable", "Segoe UI", ui-sans-serif, system-ui,
        sans-serif;
      background:
        linear-gradient(180deg, #f8fafb 0, var(--paper) 320px),
        var(--paper);
      color: var(--ink);
      line-height: 1.45;
    }
    header, main { width: min(1480px, calc(100vw - 32px)); margin: 0 auto; }
    header { padding: 28px 0 10px; border-bottom: 1px solid var(--line); }
    h1 { margin: 0; font-size: clamp(28px, 4vw, 48px); letter-spacing: 0; }
    h2 { margin: 0 0 12px; font-size: 18px; letter-spacing: 0; }
    h3 { margin: 0 0 6px; font-size: 15px; letter-spacing: 0; }
    p { margin: 0; }
    a { color: var(--accent); }
    .meta { color: var(--muted); margin-top: 6px; max-width: 900px; }
    .accounting-summary {
      margin-top: 16px;
      padding: 14px;
      border-color: #c8d5dd;
      background: linear-gradient(135deg, #ffffff 0%, #f2f7f9 100%);
      box-shadow: var(--shadow);
    }
    .accounting-grid {
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 10px;
      margin-top: 10px;
    }
    .accounting-card {
      min-height: 92px;
      padding: 12px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: rgb(255 255 255 / 72%);
    }
    .accounting-card strong {
      display: block;
      font-size: 28px;
      line-height: 1;
      font-variant-numeric: tabular-nums;
    }
    .accounting-card span {
      display: block;
      margin-top: 7px;
      font-weight: 800;
    }
    .accounting-card em {
      display: block;
      margin-top: 4px;
      color: var(--muted);
      font-size: 12px;
      font-style: normal;
    }
    .summary {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
      gap: 10px;
      margin: 18px 0 0;
    }
    .metric {
      display: block;
      min-height: 82px;
      padding: 12px;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      color: var(--ink);
      cursor: pointer;
      text-decoration: none;
      transition: border-color .15s ease, box-shadow .15s ease, transform .15s ease;
    }
    .metric:hover,
    .metric:focus-visible {
      border-color: var(--accent);
      box-shadow: var(--focus);
      outline: 0;
      transform: translateY(-1px);
    }
    .metric.active {
      border-color: var(--accent);
      background: var(--soft);
      box-shadow: inset 0 0 0 1px var(--accent);
    }
    .metric strong { display: block; font-size: 26px; line-height: 1; margin-bottom: 8px; }
    .metric span { color: var(--muted); font-size: 13px; }
    .metric-note {
      margin-top: 8px;
      color: var(--muted);
      font-size: 12px;
    }
    .toolbar {
      display: grid;
      grid-template-columns: minmax(240px, 420px) 1fr;
      gap: 12px;
      align-items: center;
      margin-top: 16px;
    }
    .filter-bar {
      position: sticky;
      top: 0;
      z-index: 20;
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
      margin-top: 12px;
      padding: 8px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: rgb(255 255 255 / 94%);
      box-shadow: 0 10px 28px rgb(31 41 51 / 7%);
      color: var(--muted);
      font-size: 12px;
      backdrop-filter: blur(10px);
    }
    .orientation-chip {
      padding: 5px 9px;
      border: 1px solid var(--line);
      border-radius: 999px;
      background: var(--soft);
      color: var(--muted);
    }
    .orientation-chip strong { color: var(--accent); }
    .filter-bar button {
      min-height: 30px;
      padding: 0 10px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      color: var(--ink);
      cursor: pointer;
      font: inherit;
      font-weight: 700;
    }
    .filter-bar button:hover,
    .filter-bar button:focus-visible {
      border-color: var(--accent);
      box-shadow: var(--focus);
      outline: 0;
    }
    input[type="search"] {
      width: 100%;
      min-height: 42px;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 0 12px;
      background: var(--panel);
      color: var(--ink);
      font: inherit;
    }
    input[type="search"]:focus-visible {
      border-color: var(--accent);
      box-shadow: var(--focus);
      outline: 0;
    }
    .tabs { display: flex; flex-wrap: wrap; gap: 8px; justify-content: flex-end; }
    .tab-button {
      min-height: 38px;
      padding: 0 12px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      color: var(--ink);
      font: inherit;
      font-weight: 700;
      cursor: pointer;
    }
    .tab-button.active {
      border-color: var(--accent);
      background: var(--soft);
      color: var(--accent);
      box-shadow: inset 0 -2px 0 var(--accent);
    }
    .tab-button:focus-visible {
      border-color: var(--accent);
      box-shadow: var(--focus);
      outline: 0;
    }
    .tab-panel { display: block; margin: 18px 0 36px; }
    .tab-panel:focus { outline: 0; }
    .tab-panel:focus-visible { box-shadow: var(--focus); }
    .js-enabled .tab-panel { display: none; }
    .js-enabled .tab-panel.active { display: block; }
    .count-badge {
      display: inline-block;
      min-width: 24px;
      margin-left: 6px;
      padding: 1px 6px;
      border-radius: 999px;
      border: 1px solid var(--line);
      background: var(--soft);
      color: var(--accent);
      font-size: 11px;
      font-weight: 800;
      text-align: center;
    }
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
    .subsection {
      background: transparent;
      border: 0;
      border-radius: 0;
      padding: 0;
      overflow: visible;
    }
    .cockpit-grid {
      display: grid;
      grid-template-columns: minmax(0, 1.25fr) minmax(340px, .75fr);
      gap: 16px;
      align-items: start;
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
      background: var(--panel-strong);
      min-height: 170px;
    }
    .lane h3 {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }
    .lane.now { border-color: var(--ok); }
    .lane.next { border-color: var(--accent); }
    .lane.waiting { border-color: var(--warn); }
    .lane.blocked { border-color: var(--risk); }
    .lane.parked { border-color: var(--hold); }
    .lane.decision_needed { border-color: var(--warn); }
    .lane.inbox { border-color: var(--muted); }
    .lane.done { border-color: var(--ok); }
    .lane.cancelled { border-color: var(--risk); }
    .lane.superseded { border-color: var(--accent); }
    .lane.discarded { border-color: var(--hold); }
    .item { padding: 10px 0; border-top: 1px solid var(--line); }
    .item:first-of-type { border-top: 0; }
    .title { font-weight: 700; }
    .small { color: var(--muted); font-size: 12px; margin-top: 4px; }
    .task-list { display: grid; gap: 10px; }
    .task-list.compact { gap: 8px; }
    .task-card {
      border: 1px solid var(--line);
      border-left: 4px solid var(--accent);
      border-radius: 8px;
      background: var(--panel-strong);
      padding: 12px;
    }
    .task-card[data-section-role="preview"] {
      background: var(--warm);
    }
    .task-card.now { border-left-color: var(--ok); }
    .task-card.waiting, .task-card.decision_needed { border-left-color: var(--warn); }
    .task-card.blocked { border-left-color: var(--risk); }
    .task-card.parked, .task-card.discarded { border-left-color: var(--hold); }
    .task-card.done { border-left-color: var(--ok); }
    .task-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin: 8px 0;
    }
    .source-links { margin-top: 8px; display: flex; flex-wrap: wrap; gap: 8px; }
    .source-links a, .source-links span { font-size: 12px; }
    .warning-list { display: grid; gap: 8px; padding-left: 18px; margin: 0; }
    details { margin-top: 14px; }
    summary { cursor: pointer; font-weight: 700; margin-bottom: 10px; }
    .table-wrap {
      width: 100%;
      overflow-x: auto;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
    }
    table { width: 100%; border-collapse: collapse; table-layout: fixed; }
    caption {
      padding: 8px;
      text-align: left;
      color: var(--muted);
      font-size: 12px;
      font-weight: 800;
    }
    th, td {
      padding: 9px 8px;
      border-top: 1px solid var(--line);
      text-align: left;
      vertical-align: top;
      overflow-wrap: anywhere;
      font-size: 13px;
    }
    th {
      position: sticky;
      top: 0;
      z-index: 2;
      color: var(--muted);
      font-weight: 800;
      border-top: 0;
      background: var(--panel);
    }
    .register-table th:first-child,
    .register-table td:first-child,
    .recovery-table th:first-child,
    .recovery-table td:first-child {
      width: 52px;
      text-align: right;
      color: var(--muted);
      font-variant-numeric: tabular-nums;
    }
    .register-table th:nth-child(2),
    .register-table td:nth-child(2) { width: 118px; }
    .register-table th:nth-child(3),
    .register-table td:nth-child(3) { width: 150px; }
    .register-table th:nth-child(4),
    .register-table td:nth-child(4) { width: 84px; }
    .register-table th:nth-child(5),
    .register-table td:nth-child(5) { width: 27%; }
    .register-table th:nth-child(6),
    .register-table td:nth-child(6) { width: 26%; }
    .recovery-table th:nth-child(2),
    .recovery-table td:nth-child(2) { width: 130px; }
    .recovery-table th:nth-child(3),
    .recovery-table td:nth-child(3) { width: 110px; }
    .recovery-table th:nth-child(4),
    .recovery-table td:nth-child(4) { width: 130px; }
    .recovery-table th:nth-child(5),
    .recovery-table td:nth-child(5) { width: 120px; }
    .recovery-table th:nth-child(6),
    .recovery-table td:nth-child(6) { width: 100px; }
    .register-status {
      margin: 0 0 12px;
      padding: 10px 12px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--soft);
      color: var(--accent);
      font-weight: 800;
    }
    .row-details summary {
      min-height: 30px;
      margin: 0;
      color: var(--accent);
      font-size: 12px;
    }
    .detail-stack {
      display: grid;
      gap: 7px;
      margin-top: 8px;
      padding: 8px;
      border-radius: 8px;
      background: var(--soft);
    }
    .detail-row {
      display: grid;
      grid-template-columns: 92px minmax(0, 1fr);
      gap: 8px;
      color: var(--muted);
      font-size: 12px;
    }
    .detail-row strong { color: var(--ink); }
    .bucket-summary {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 12px 0 0;
    }
    .bucket-chip {
      display: inline-flex;
      gap: 5px;
      align-items: center;
      padding: 5px 9px;
      border: 1px solid var(--line);
      border-radius: 999px;
      background: var(--soft);
      color: var(--muted);
      font-size: 12px;
      font-weight: 700;
    }
    .bucket-chip strong { color: var(--accent); }
    .recovery-buckets {
      display: grid;
      gap: 12px;
      margin-top: 14px;
    }
    .recovery-bucket {
      padding: 12px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel-strong);
    }
    .copy-panel {
      margin-top: 14px;
      display: grid;
      gap: 8px;
    }
    .copy-panel textarea {
      width: 100%;
      min-height: 180px;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 10px;
      font: 12px ui-monospace, SFMono-Regular, Consolas, monospace;
      color: var(--ink);
      background: #fbfcfd;
    }
    .copy-button {
      justify-self: start;
      min-height: 34px;
      padding: 0 12px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: var(--panel);
      color: var(--ink);
      cursor: pointer;
      font: inherit;
      font-weight: 800;
    }
    .copy-button:hover,
    .copy-button:focus-visible {
      border-color: var(--accent);
      box-shadow: 0 0 0 3px rgb(49 95 114 / 16%);
      outline: 0;
    }
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
    .now .status-pill:first-child { color: var(--ok); }
    .waiting .status-pill:first-child,
    .decision_needed .status-pill:first-child { color: var(--warn); }
    .blocked .status-pill:first-child,
    .cancelled .status-pill:first-child { color: var(--risk); }
    .done .status-pill:first-child { color: var(--ok); }
    .boundary {
      margin-top: 12px;
      padding: 12px;
      background: var(--warm);
      border: 1px solid var(--line);
      border-radius: 8px;
      color: var(--muted);
      font-size: 13px;
    }
    .empty-state {
      margin-top: 12px;
      padding: 12px;
      border: 1px dashed var(--line);
      border-radius: 8px;
      color: var(--muted);
      background: var(--panel);
      font-size: 13px;
    }
    @media (max-width: 900px) {
      header, main { width: min(100% - 20px, 1480px); }
      .grid, .cockpit-grid, .toolbar { grid-template-columns: 1fr; }
      .accounting-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
      .tabs { justify-content: flex-start; }
      section { padding: 12px; }
      th, td { font-size: 12px; }
    }
    @media (max-width: 600px) {
      header { padding-top: 18px; }
      h1 { font-size: 28px; }
      .meta { font-size: 13px; }
      .accounting-summary {
        margin-top: 12px;
        padding: 10px;
      }
      .accounting-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 6px;
      }
      .accounting-card {
        min-height: 76px;
        padding: 9px;
      }
      .accounting-card strong { font-size: 22px; }
      .accounting-card span { font-size: 12px; }
      .accounting-card em { display: none; }
      .summary {
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 6px;
        margin-top: 12px;
      }
      .metric {
        min-height: 58px;
        padding: 8px;
      }
      .metric strong {
        font-size: 20px;
        margin-bottom: 4px;
      }
      .metric span {
        display: block;
        font-size: 11px;
        line-height: 1.15;
      }
      .toolbar {
        gap: 8px;
        margin-top: 10px;
      }
      input[type="search"] { min-height: 38px; }
      .tabs {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 6px;
      }
      .tab-button {
        min-height: 34px;
        padding: 0 8px;
        font-size: 12px;
      }
      table {
        width: 760px;
        min-width: 760px;
        table-layout: auto;
      }
      .register-table {
        width: 900px;
        min-width: 900px;
      }
      .recovery-table {
        width: 1280px;
        min-width: 1280px;
      }
      .table-wrap {
        max-width: calc(100vw - 48px);
        min-width: 0;
      }
      .recovery-bucket,
      details {
        min-width: 0;
      }
      .filter-bar { margin-top: 8px; }
      .orientation-chip { padding: 4px 7px; }
      .detail-row { grid-template-columns: 1fr; }
    }
"""
    if surface != DashboardSurface.vscode:
        return base
    return (
        base
        + """
    :root {
      color-scheme: light dark;
      --ink: var(--vscode-foreground, #d4d4d4);
      --muted: var(--vscode-descriptionForeground, #a8b0ba);
      --line: var(--vscode-panel-border, #3c3c3c);
      --paper: var(--vscode-editor-background, #1e1e1e);
      --panel: var(--vscode-sideBar-background, #252526);
      --accent: var(--vscode-textLink-foreground, #4ea3d8);
      --ok: var(--vscode-charts-green, #4caf50);
      --warn: var(--vscode-charts-yellow, #cca700);
      --risk: var(--vscode-charts-red, #f14c4c);
      --hold: var(--vscode-charts-purple, #c586c0);
      --soft: var(--vscode-input-background, #313131);
      --warm: var(--vscode-editorWidget-background, #252526);
      --panel-strong: var(--vscode-editorWidget-background, var(--panel));
      --shadow: none;
      --focus: 0 0 0 2px var(--vscode-focusBorder, #007fd4);
    }
    body {
      font-family: var(--vscode-font-family, "Segoe UI", sans-serif);
      font-size: var(--vscode-font-size, 13px);
      background: var(--paper);
    }
    header, main { width: min(100% - 24px, 1540px); }
    header { padding: 18px 0 14px; }
    h1 { font-size: 26px; }
    h2 { font-size: 16px; }
    h3 { font-size: 13px; text-transform: uppercase; color: var(--muted); }
    .meta { max-width: 980px; }
    .summary { grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); }
    .accounting-summary {
      background: var(--panel);
      border-color: var(--line);
      box-shadow: none;
    }
    .accounting-card {
      background: var(--vscode-editorWidget-background, var(--panel));
      border-color: var(--line);
      color: var(--ink);
    }
    .filter-bar {
      background: var(--vscode-editorWidget-background, var(--panel));
      box-shadow: none;
    }
    .copy-panel textarea,
    .detail-stack,
    .recovery-bucket,
    .table-wrap {
      background: var(--vscode-editorWidget-background, var(--panel));
    }
    .tab-button.active {
      background: var(--vscode-button-background, #0e639c);
      color: var(--vscode-button-foreground, #ffffff);
    }
    .metric { min-height: 66px; background: var(--panel); }
    .metric strong { font-size: 22px; }
    .grid { grid-template-columns: minmax(0, 1.18fr) minmax(360px, .82fr); }
    section { background: var(--panel); }
    .lane,
    .boundary,
    .task-card {
      background: var(--vscode-editorWidget-background, var(--panel));
    }
    .status-pill {
      background: var(--vscode-badge-background, #4d4d4d);
      color: var(--vscode-badge-foreground, #ffffff);
    }
    th, td { font-size: 12px; }
"""
    )


def _accounting_summary(
    reviewed_count: int,
    recovery_count: int,
    total_detected: int,
    closed_count: int,
) -> str:
    items = (
        ("Reviewed rows", reviewed_count, "first-class operating rows in the dashboard"),
        ("Recovery Inbox rows", recovery_count, "unreviewed candidates awaiting import review"),
        ("Total detected", total_detected, "reviewed rows plus recovery candidates"),
        ("Reviewed closed", closed_count, "done, cancelled, superseded, or discarded rows"),
    )
    cards = "".join(
        '<div class="accounting-card">'
        f"<strong>{escape(str(value))}</strong>"
        f"<span>{escape(label)}</span>"
        f"<em>{escape(note)}</em>"
        "</div>"
        for label, value, note in items
    )
    return (
        '<section class="accounting-summary" aria-label="Dashboard accounting summary">'
        "<h2>Accounting Summary</h2>"
        '<p class="small">This separates what is reviewed from what was merely recovered.</p>'
        f'<div class="accounting-grid">{cards}</div>'
        "</section>"
    )


def _metric(label: str, value: int, target_panel: str, filter_key: str) -> str:
    aria_label = f"{value} {label}"
    return (
        f'<a class="metric" href="#{escape(target_panel)}" '
        f'data-tab-target="{escape(target_panel)}" '
        f'data-dashboard-filter="{escape(filter_key)}" '
        f'aria-label="{escape(aria_label)}">'
        f"<strong>{escape(str(value))}</strong>"
        f"<span>{escape(label)}</span>"
        "</a>"
    )


def _status_lane(
    status: str,
    tasks: tuple[WorkspaceTask, ...],
    *,
    panel: str,
) -> str:
    label = STATUS_LABELS[status]
    items = _task_cards(tasks, panel=panel, section_role="lane")
    if not items:
        items = '<p class="small">Nothing recorded.</p>'
    return (
        f'<div class="lane {escape(status)}"><h3>{escape(label)}'
        f'<span class="count-badge">{len(tasks)}</span></h3>{items}</div>'
    )


def _task_cards(
    tasks: tuple[WorkspaceTask, ...],
    *,
    panel: str,
    section_role: str,
) -> str:
    if not tasks:
        return '<p class="small">Nothing recorded.</p>'
    return "".join(
        _task_card(task, panel=panel, section_role=section_role)
        for task in tasks
    )


def _task_card(
    task: WorkspaceTask,
    *,
    panel: str,
    section_role: str,
) -> str:
    gate = (
        f'<p class="small">Gate: {escape(task.blocked_by)}</p>'
        if task.blocked_by
        else ""
    )
    closed = (
        f'<p class="small">Closed: {escape(task.closed_at)} {escape(task.closure_reason)}</p>'
        if task.closed_at or task.closure_reason
        else ""
    )
    return (
        f'<article class="task-card search-item {escape(task.status)}" '
        f"{_task_data_attrs(task, panel=panel, section_role=section_role)}>"
        f'<p class="title">{escape(task.title)}</p>'
        '<div class="task-meta">'
        f'<span class="status-pill">{escape(STATUS_LABELS.get(task.status, task.status))}</span>'
        f'<span class="status-pill">{escape(task.priority)}</span>'
        f'<span class="status-pill">{escape(task.repo)}</span>'
        "</div>"
        f'<p class="small">{escape(task.lane or "workspace task")} · '
        f"{escape(task.confidence)} confidence · "
        f'last seen {escape(task.last_seen_at or "unknown")}</p>'
        f'<p class="small">Next: {escape(task.next_action or "triage source refs")}</p>'
        f"{gate}"
        f"{closed}"
        f"{_source_links(task.source_refs)}"
        "</article>"
    )


def _task_register_table(tasks: tuple[WorkspaceTask, ...], *, panel: str) -> str:
    if not tasks:
        return '<p class="small">No reviewed dashboard rows.</p>'
    rows = "".join(
        _task_register_row(index, task, panel=panel)
        for index, task in enumerate(tasks, 1)
    )
    return (
        '<div class="table-wrap"><table class="register-table">'
        "<caption>Reviewed workspace item register</caption>"
        "<thead><tr><th>#</th><th>Status</th><th>Repo</th><th>Priority</th>"
        "<th>Item</th><th>Next / Last Seen</th><th>Details</th></tr></thead>"
        f"<tbody>{rows}</tbody></table></div>"
    )


def _task_register_row(index: int, task: WorkspaceTask, *, panel: str) -> str:
    closed = " ".join(part for part in (task.closed_at, task.closure_reason) if part)
    return (
        f'<tr class="register-row search-item {escape(task.status)}" '
        f"{_task_data_attrs(task, panel=panel, section_role='register')}>"
        f'<td><span data-row-number>{index}</span></td>'
        '<td><span class="status-pill">'
        f"{escape(STATUS_LABELS.get(task.status, task.status))}</span></td>"
        f"<td>{escape(task.repo)}</td>"
        f"<td>{escape(task.priority)}</td>"
        f"<td><strong>{escape(task.title)}</strong><br>"
        f'<span class="small">{escape(task.lane)}</span></td>'
        f"<td>{escape(task.next_action or 'triage source refs')}<br>"
        f'<span class="small">Last seen {escape(task.last_seen_at or "unknown")}</span></td>'
        f"<td>{_task_detail_disclosure(task, closed)}</td>"
        "</tr>"
    )


def _task_detail_disclosure(task: WorkspaceTask, closed: str) -> str:
    closed_label = closed or (
        "terminal; closure date not recorded"
        if task.status in CLOSED_STATUS_ORDER
        else "open"
    )
    rows = [
        '<div class="detail-row"><strong>Source refs:</strong> '
        f"{_source_refs_inline(task.source_refs) or '<span>none</span>'}</div>",
        '<div class="detail-row"><strong>Evidence refs:</strong> '
        f"{_source_refs_inline(task.evidence_refs) or '<span>none</span>'}</div>",
        '<div class="detail-row"><strong>Attention:</strong> '
        f"<span>{escape(task.attention_reason or 'not recorded')}</span></div>",
        '<div class="detail-row"><strong>Blocked by:</strong> '
        f"<span>{escape(task.blocked_by or 'not blocked')}</span></div>",
        '<div class="detail-row"><strong>Closed:</strong> '
        f"<span>{escape(closed_label)}</span></div>",
    ]
    if task.superseded_by:
        rows.append(
            '<div class="detail-row"><strong>Superseded by:</strong> '
            f"<span>{escape(task.superseded_by)}</span></div>"
        )
    return (
        '<details class="row-details">'
        "<summary>Sources and metadata</summary>"
        f'<div class="detail-stack">{"".join(rows)}</div>'
        "</details>"
    )


def _recovery_inbox_table(tasks: tuple[WorkspaceTask, ...]) -> str:
    if not tasks:
        return '<p class="small">No unreviewed recovery candidates.</p>'
    sections: list[str] = []
    running_index = 1
    for bucket in RECOVERY_BUCKETS:
        bucket_tasks = tuple(task for task in tasks if _recovery_bucket(task) == bucket)
        if not bucket_tasks:
            continue
        rows = "".join(
            _recovery_inbox_row(index, task)
            for index, task in enumerate(bucket_tasks, running_index)
        )
        running_index += len(bucket_tasks)
        label = RECOVERY_BUCKET_LABELS[bucket]
        sections.append(
            '<details class="recovery-bucket" open '
            f'data-recovery-bucket-section="{escape(bucket)}">'
            f"<summary>{escape(label)}"
            f'<span class="count-badge">{len(bucket_tasks)}</span></summary>'
            '<div class="table-wrap"><table class="recovery-table">'
            f"<caption>{escape(label)} recovery candidates</caption>"
            "<thead><tr><th>#</th><th>Source Type</th><th>Status</th><th>Repo</th>"
            "<th>Sensitivity</th><th>Confidence</th><th>Title</th><th>Review Hint</th>"
            "<th>Why Here</th><th>Source</th></tr></thead>"
            f"<tbody>{rows}</tbody></table></div>"
            "</details>"
        )
    return '<div class="recovery-buckets">' + "".join(sections) + "</div>"


def _recovery_inbox_row(index: int, task: WorkspaceTask) -> str:
    source_type = _recovery_source_type(task)
    bucket = _recovery_bucket(task)
    return (
        f'<tr class="recovery-row search-item {escape(task.status)}" '
        f'{_task_data_attrs(task, panel="recovery", section_role="recovery")} '
        f'data-source-type="{escape(source_type)}" '
        f'data-recovery-bucket="{escape(bucket)}">'
        f'<td><span data-row-number>{index}</span></td>'
        f"<td>{escape(source_type)}</td>"
        '<td><span class="status-pill">'
        f"{escape(STATUS_LABELS.get(task.status, task.status))}</span></td>"
        f"<td>{escape(task.repo)}</td>"
        f"<td>{escape(task.sensitivity)}</td>"
        f"<td>{escape(task.confidence)}</td>"
        f"<td><strong>{escape(task.title)}</strong></td>"
        f"<td>{escape(_recovery_review_hint(task))}</td>"
        f"<td>{escape(_recovery_reason(task))}</td>"
        f"<td>{_source_refs_inline(task.source_refs)}</td>"
        "</tr>"
    )


def _approved_json_template(tasks: tuple[WorkspaceTask, ...]) -> str:
    payload = {"candidates": [task.to_dict() for task in tasks]}
    text = json.dumps(payload, indent=2, sort_keys=True)
    return (
        '<div class="copy-panel">'
        '<label for="approved-json-template"><strong>Approved JSON starter</strong></label>'
        '<textarea id="approved-json-template" readonly>'
        f"{escape(text)}"
        "</textarea>"
        '<button class="copy-button" type="button" data-copy-target="approved-json-template">'
        "Copy approved JSON starter</button>"
        "</div>"
    )


def _task_data_attrs(task: WorkspaceTask, *, panel: str, section_role: str) -> str:
    attention_statuses = {"now", "waiting", "blocked", "decision_needed"}
    is_attention = "true" if task.status in attention_statuses else "false"
    is_proof_risk = "true" if _is_proof_risk(task) else "false"
    is_closed = "true" if task.status in CLOSED_STATUS_ORDER else "false"
    return (
        f'data-task-id="{escape(task.id)}" '
        f'data-search="{escape(_task_search_text(task))}" '
        f'data-status="{escape(task.status)}" '
        f'data-attention="{is_attention}" '
        f'data-proof-risk="{is_proof_risk}" '
        f'data-closed="{is_closed}" '
        f'data-repo="{escape(task.repo)}" '
        f'data-panel="{escape(panel)}" '
        f'data-section-role="{escape(section_role)}"'
    )


def _task_search_text(task: WorkspaceTask) -> str:
    return " ".join(
        (
            task.title,
            task.repo,
            task.lane,
            task.status,
            task.priority,
            task.next_action,
            task.blocked_by,
            task.attention_reason,
            task.sensitivity,
            task.confidence,
            " ".join(task.source_refs),
        )
    )


def _empty_state(panel: str) -> str:
    return (
        f'<p class="empty-state" data-empty-state="{escape(panel)}" hidden>'
        "No matching task rows in this view.</p>"
    )


def _attention_tasks(tasks: tuple[WorkspaceTask, ...]) -> tuple[WorkspaceTask, ...]:
    spotlight = {"now", "waiting", "blocked", "decision_needed"}
    active = tuple(task for task in tasks if task.status in spotlight)
    return tuple(sorted(active, key=_task_card_sort_key))


def _proof_blocked_tasks(tasks: tuple[WorkspaceTask, ...]) -> tuple[WorkspaceTask, ...]:
    proof_tasks = [task for task in tasks if _is_proof_risk(task)]
    return tuple(sorted(proof_tasks, key=_task_card_sort_key))


def _is_proof_risk(task: WorkspaceTask) -> bool:
    proof_statuses = {"now", "waiting", "blocked", "decision_needed", "parked"}
    text = f"{task.title} {task.lane} {task.attention_reason} {task.blocked_by}".lower()
    return "proof" in text and task.status in proof_statuses


def _task_card_sort_key(task: WorkspaceTask) -> tuple[int, int, str, str]:
    status_rank = {
        "now": 0,
        "decision_needed": 1,
        "blocked": 2,
        "waiting": 3,
        "next": 4,
        "inbox": 5,
        "parked": 6,
        "done": 7,
        "superseded": 8,
        "cancelled": 9,
        "discarded": 10,
    }
    priority_rank = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    return (
        status_rank.get(task.status, 99),
        priority_rank.get(task.priority.upper(), 9),
        task.repo.lower(),
        task.title.lower(),
    )


def _source_links(refs: tuple[str, ...]) -> str:
    if not refs:
        return ""
    links = "".join(_source_link(ref) for ref in refs[:3])
    return f'<div class="source-links">{links}</div>'


def _source_refs_inline(refs: tuple[str, ...]) -> str:
    if not refs:
        return ""
    return '<div class="source-links">' + "".join(_source_link(ref) for ref in refs[:2]) + "</div>"


def _source_link(ref: str) -> str:
    display = ref.split("#", 1)[0]
    local_prefixes = ("docs/", "practice-os/", "prompts/", "decisions/")
    if ref.startswith(local_prefixes):
        href = "../" + display.replace("\\", "/")
        return f'<a href="{escape(href)}">{escape(display)}</a>'
    return f"<span>{escape(ref)}</span>"


def _recovery_source_type(task: WorkspaceTask) -> str:
    refs = " ".join(task.source_refs)
    if "codex-session:" in refs:
        return "codex-session"
    if "MEMORY.md:" in refs:
        return "memory-pointer"
    if "practice-os/kaizen" in refs:
        return "kaizen"
    if "ROADMAP_EXECUTION_BACKLOG" in refs:
        return "roadmap"
    return "structured-source"


def _recovery_bucket_counts(tasks: tuple[WorkspaceTask, ...]) -> dict[str, int]:
    return {
        bucket: sum(1 for task in tasks if _recovery_bucket(task) == bucket)
        for bucket in RECOVERY_BUCKETS
    }


def _recovery_bucket_summary(counts: dict[str, int]) -> str:
    items = "".join(
        '<span class="bucket-chip" '
        f'data-recovery-bucket-chip="{escape(bucket)}">'
        f"{escape(RECOVERY_BUCKET_LABELS[bucket])}: "
        f"<strong>{escape(str(counts.get(bucket, 0)))}</strong></span>"
        for bucket in RECOVERY_BUCKETS
    )
    return (
        '<div class="bucket-summary" aria-label="Recovery Inbox bucket counts">'
        f"{items}</div>"
    )


def _recovery_bucket(task: WorkspaceTask) -> str:
    source_type = _recovery_source_type(task)
    sensitivity = task.sensitivity.lower()
    text = f"{task.title} {task.attention_reason} {task.closure_reason}".lower()
    if task.sensitivity in PRIVATE_TASK_SENSITIVITIES or "coi" in sensitivity:
        return "private_coi_gated"
    if source_type == "codex-session":
        return "codex_session_lead"
    if source_type == "memory-pointer":
        return "memory_pointer"
    if task.status in {"cancelled", "discarded"} or task.confidence.lower() == "low":
        return "likely_discard"
    if task.status == "superseded" or "duplicate" in text or "superseded" in text:
        return "merge_review"
    if task.confidence.lower() == "high":
        return "high_confidence_import"
    return "merge_review"


def _recovery_review_hint(task: WorkspaceTask) -> str:
    bucket = _recovery_bucket(task)
    if bucket == "high_confidence_import":
        return "Review source refs, then approve/import if still useful."
    if bucket == "merge_review":
        return "Check whether this should merge into an existing dashboard row."
    if bucket == "codex_session_lead":
        return "Use as a lead only; verify against repo files or reviewed docs."
    if bucket == "memory_pointer":
        return "Refresh from live repo/DTP evidence before promotion."
    if bucket == "private_coi_gated":
        return "Keep metadata-only unless redacted and explicitly approved."
    return "Discard unless a durable source proves current value."


def _recovery_reason(task: WorkspaceTask) -> str:
    source_type = _recovery_source_type(task)
    if source_type == "codex-session":
        return "Session-index candidate; review source pointers before promotion."
    if source_type == "memory-pointer":
        return "Saved-memory pointer; verify against live repo/DTP docs before promotion."
    return "Recovered candidate is not in the reviewed operating dashboard yet."


def _data_health_warnings(
    tasks: tuple[WorkspaceTask, ...],
    sweep_coverage: tuple[SweepCoverageRow, ...],
) -> tuple[str, ...]:
    warnings: list[str] = []
    has_ledger_rows = any(
        "practice-os/workspace/task-ledger" in ref
        for task in tasks
        for ref in task.source_refs
    )
    if not has_ledger_rows:
        warnings.append(
            "No applied workspace task ledger rows found; this view is enriched from source docs."
        )
    if not any(ref.startswith("codex-session:") for task in tasks for ref in task.source_refs):
        warnings.append(
            "Historical Codex sessions are reviewed by `dtp workspace recover --dry-run`, "
            "not normal dashboard refresh."
        )
    if not sweep_coverage:
        warnings.append("No sweep coverage ledger was found.")
    if not warnings:
        warnings.append(
            "Structured DTP sources are present and the Notion mirror export is refreshed."
        )
    return tuple(warnings)


def _warning_list(warnings: tuple[str, ...]) -> str:
    if not warnings:
        return '<p class="small">No data-health warnings.</p>'
    items = "".join(f"<li>{escape(warning)}</li>" for warning in warnings)
    return f'<ul class="warning-list">{items}</ul>'


def _repo_snapshot(rows: list[RepoReport]) -> str:
    blocked = sum(1 for row in rows if row.blocker)
    missing = sum(1 for row in rows if _coverage_status(row) != "recorded")
    candidates = rows[:5]
    if not candidates:
        return '<p class="small">No repo manifest rows recorded.</p>'
    items = "".join(
        "<li>"
        f"<strong>{escape(row.repo)}</strong>: "
        f"{escape(row.blocker or row.next_action or 'recorded')}"
        "</li>"
        for row in candidates
    )
    return (
        f'<p class="small">{len(rows)} repos recorded; {blocked} carry gates; '
        f"{missing} need manifest/evidence coverage.</p>"
        f"<ul>{items}</ul>"
    )


def _tab_button(panel: str, label: str, active: bool, count: int | None = None) -> str:
    active_class = " active" if active else ""
    selected = "true" if active else "false"
    badge = f'<span class="count-badge">{count}</span>' if count is not None else ""
    return (
        f'<button id="tab-{escape(panel)}" class="tab-button{active_class}" '
        f'type="button" role="tab" data-tab-target="{escape(panel)}" '
        f'aria-selected="{selected}" aria-controls="{escape(panel)}" '
        f'tabindex="{"0" if active else "-1"}">'
        f"{escape(label)}{badge}</button>"
    )


def _dashboard_script() -> str:
    return """
const tabButtons = document.querySelectorAll(".tab-button[data-tab-target]");
const metricCards = document.querySelectorAll(".metric[data-dashboard-filter]");
const panels = document.querySelectorAll("[data-panel]");
const taskRows = document.querySelectorAll(".search-item[data-task-id]");
const search = document.getElementById("dashboard-search");
const filterStatus = document.getElementById("filter-status");
const clearFilter = document.getElementById("clear-dashboard-filter");
const registerStatus = document.getElementById("register-status");
const orientationPanel = document.getElementById("orientation-panel");
const orientationFilter = document.getElementById("orientation-filter");
const jumpRegister = document.getElementById("jump-register");
const copyButtons = document.querySelectorAll("[data-copy-target]");
let activeFilter = "";

document.body.classList.add("js-enabled");

const filterLabels = {
  attention: "needs attention",
  "status:waiting": "waiting on Toni/owner",
  "status:blocked": "blocked",
  "status:decision_needed": "decision needed",
  "proof-risk": "proof blocked",
  closed: "recently closed",
};

const panelLabels = {
  today: "Today",
  workstreams: "Workstreams",
  proof: "Proof",
  register: "Register",
  recovery: "Recovery Inbox",
  repos: "Repos",
  archive: "Archive",
  coverage: "Coverage",
};

const panelOrder = [
  "today",
  "workstreams",
  "proof",
  "register",
  "recovery",
  "repos",
  "archive",
  "coverage",
];
const panelNames = new Set(Array.from(panels).map((panel) => panel.dataset.panel));

function currentPanel() {
  return document.querySelector(".tab-panel.active")?.dataset.panel || "today";
}

function moveToPanel(target) {
  const panel = document.getElementById(target);
  if (!panel) return;
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  panel.scrollIntoView({
    behavior: prefersReducedMotion ? "auto" : "smooth",
    block: "start",
  });
  panel.focus({ preventScroll: true });
}

function setPanel(target, options = {}) {
  const safeTarget = panelNames.has(target) ? target : "today";
  const updateHash = options.updateHash !== false;
  tabButtons.forEach((item) => {
    const selected = item.getAttribute("data-tab-target") === safeTarget;
    item.classList.toggle("active", selected);
    item.setAttribute("aria-selected", selected ? "true" : "false");
    item.setAttribute("tabindex", selected ? "0" : "-1");
  });
  panels.forEach((panel) => {
    const selected = panel.getAttribute("data-panel") === safeTarget;
    panel.classList.toggle("active", selected);
    panel.setAttribute("aria-hidden", selected ? "false" : "true");
  });
  if (updateHash && window.history) {
    window.history.replaceState(null, "", `#${safeTarget}`);
  }
  if (options.scroll === true) {
    moveToPanel(safeTarget);
  }
  updateOrientation();
}

function updateOrientation() {
  const panelName = currentPanel();
  if (orientationPanel) {
    orientationPanel.textContent = panelLabels[panelName] || panelName;
  }
  if (orientationFilter) {
    orientationFilter.textContent = activeFilter
      ? filterLabels[activeFilter] || activeFilter
      : "All rows";
  }
}

function rowMatchesFilter(row) {
  if (!activeFilter) return true;
  if (activeFilter === "attention") return row.dataset.attention === "true";
  if (activeFilter === "proof-risk") return row.dataset.proofRisk === "true";
  if (activeFilter === "closed") return row.dataset.closed === "true";
  if (activeFilter.startsWith("status:")) {
    return row.dataset.status === activeFilter.split(":")[1];
  }
  return true;
}

function rowMatchesQuery(row, query) {
  if (!query) return true;
  const text = (row.getAttribute("data-search") || row.textContent || "").toLowerCase();
  return text.includes(query);
}

function rowIsCountable(row) {
  return row.dataset.sectionRole !== "preview";
}

function rowMatches(row, query) {
  return rowMatchesFilter(row) && rowMatchesQuery(row, query);
}

function uniqueTaskCount(rows) {
  const ids = new Set();
  rows.forEach((row) => ids.add(row.dataset.taskId));
  return ids.size;
}

function countRowsForPanel(panelName, query, options = {}) {
  const ignoreQuery = options.ignoreQuery || false;
  const rows = Array.from(taskRows).filter((row) => {
    if (row.dataset.panel !== panelName || !rowIsCountable(row)) return false;
    if (!rowMatchesFilter(row)) return false;
    return ignoreQuery || rowMatchesQuery(row, query);
  });
  return uniqueTaskCount(rows);
}

function bestPanelForQuery(query) {
  for (const panelName of panelOrder) {
    const count = countRowsForPanel(panelName, query);
    if (count > 0) return panelName;
  }
  return "";
}

function updateEmptyStates(panelCounts) {
  document.querySelectorAll("[data-empty-state]").forEach((item) => {
    const panelName = item.getAttribute("data-empty-state");
    const active = currentPanel() === panelName;
    item.hidden = !active || (panelCounts.get(panelName) || 0) > 0;
  });
}

function updateRowNumbers(panelName) {
  let index = 1;
  taskRows.forEach((row) => {
    if (row.dataset.panel !== panelName || row.style.display === "none") return;
    const number = row.querySelector("[data-row-number]");
    if (number) {
      number.textContent = String(index);
      index += 1;
    }
  });
}

function updateRows({ allowRoute = false } = {}) {
  const query = search ? search.value.trim().toLowerCase() : "";
  if (allowRoute && query && !activeFilter) {
    const activeCount = countRowsForPanel(currentPanel(), query);
    if (activeCount === 0) {
      const nextPanel = bestPanelForQuery(query);
      if (nextPanel) setPanel(nextPanel, { scroll: true });
    }
  }

  const panelCounts = new Map();
  taskRows.forEach((row) => {
    const focused = Boolean(activeFilter || query);
    const show = rowMatches(row, query) && (!focused || rowIsCountable(row));
    row.style.display = show ? "" : "none";
  });

  panels.forEach((panel) => {
    const panelName = panel.dataset.panel;
    panelCounts.set(panelName, countRowsForPanel(panelName, query));
  });
  updateEmptyStates(panelCounts);
  updateRowNumbers("register");
  updateRowNumbers("recovery");

  if (filterStatus) {
    const panelName = currentPanel();
    const visible = panelCounts.get(panelName) || 0;
    const total = countRowsForPanel(panelName, query, { ignoreQuery: true });
    const label = activeFilter
      ? filterLabels[activeFilter] || activeFilter
      : panelLabels[panelName] || "dashboard";
    const searchLabel = query ? ` matching "${query}"` : "";
    if (total > 0 || visible > 0) {
      filterStatus.textContent = `Showing ${visible} of ${total} ${label} records${searchLabel}.`;
    } else {
      filterStatus.textContent = query
        ? `No ${label} task records match "${query}".`
        : `Showing ${label} content.`;
    }
  }
  if (registerStatus) {
    const visible = panelCounts.get("register") || 0;
    const total = countRowsForPanel("register", query, { ignoreQuery: true });
    const label = activeFilter ? filterLabels[activeFilter] || activeFilter : "reviewed dashboard";
    const searchLabel = query ? ` matching "${query}"` : "";
    registerStatus.textContent = `Showing ${visible} of ${total} ${label} rows${searchLabel}.`;
  }
  if (clearFilter) {
    clearFilter.hidden = !activeFilter && !query;
  }
  updateOrientation();
}

function setMetricFilter(card) {
  activeFilter = card.getAttribute("data-dashboard-filter") || "";
  if (search) search.value = "";
  metricCards.forEach((item) => item.classList.toggle("active", item === card));
  updateRows();
}

function clearDashboardFilter() {
  activeFilter = "";
  metricCards.forEach((item) => item.classList.remove("active"));
  if (search) search.value = "";
  updateRows();
}

tabButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const target = button.getAttribute("data-tab-target");
    setPanel(target, { scroll: true });
    clearDashboardFilter();
  });
  button.addEventListener("keydown", (event) => {
    const keys = ["ArrowLeft", "ArrowRight", "Home", "End"];
    if (!keys.includes(event.key)) return;
    event.preventDefault();
    const buttons = Array.from(tabButtons);
    const index = buttons.indexOf(button);
    let nextIndex = index;
    if (event.key === "ArrowLeft") nextIndex = index <= 0 ? buttons.length - 1 : index - 1;
    if (event.key === "ArrowRight") nextIndex = index >= buttons.length - 1 ? 0 : index + 1;
    if (event.key === "Home") nextIndex = 0;
    if (event.key === "End") nextIndex = buttons.length - 1;
    const nextButton = buttons[nextIndex];
    const target = nextButton.getAttribute("data-tab-target");
    setPanel(target, { scroll: true });
    clearDashboardFilter();
    nextButton.focus();
  });
});

metricCards.forEach((card) => {
  card.addEventListener("click", (event) => {
    event.preventDefault();
    const target = card.getAttribute("data-tab-target");
    setPanel(target, { scroll: true });
    setMetricFilter(card);
  });
});

if (search) {
  search.addEventListener("input", () => updateRows({ allowRoute: true }));
}

if (clearFilter) {
  clearFilter.addEventListener("click", clearDashboardFilter);
}

if (jumpRegister) {
  jumpRegister.addEventListener("click", () => {
    setPanel("register", { scroll: true });
    updateRows();
  });
}

copyButtons.forEach((button) => {
  button.addEventListener("click", async () => {
    const targetId = button.getAttribute("data-copy-target");
    const target = targetId ? document.getElementById(targetId) : null;
    if (!target) return;
    try {
      await navigator.clipboard.writeText(target.value || target.textContent || "");
      button.textContent = "Copied";
      setTimeout(() => {
        button.textContent = "Copy approved JSON starter";
      }, 1400);
    } catch {
      target.focus();
      target.select?.();
    }
  });
});

window.addEventListener("hashchange", () => {
  const target = window.location.hash.slice(1);
  if (panelNames.has(target)) {
    setPanel(target, { updateHash: false, scroll: true });
    clearDashboardFilter();
  }
});

const initialPanel = window.location.hash.slice(1);
setPanel(panelNames.has(initialPanel) ? initialPanel : "today", { updateHash: false });
updateRows();
""".strip()


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


def _sweep_table(rows: tuple[SweepCoverageRow, ...]) -> str:
    if not rows:
        return '<p class="small">No sweep ledger recorded.</p>'
    body = "".join(
        "<tr>"
        f"<td>{escape(row.scope)}</td>"
        f'<td><span class="status-pill">{escape(row.coverage)}</span></td>'
        f"<td>{escape(row.notes)}</td>"
        "</tr>"
        for row in rows
    )
    return (
        "<table>"
        "<thead><tr><th>Scope</th><th>Coverage</th><th>Notes</th></tr></thead>"
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


def _is_markdown_rule(cells: list[str]) -> bool:
    return all(cell.replace("-", "").replace(":", "").strip() == "" for cell in cells)


def _rendered_metric_count(html: str, label: str) -> int:
    pattern = re.compile(
        r'<a class="metric"[^>]*><strong>(\d+)</strong><span>'
        + re.escape(label)
        + r"</span></a>"
    )
    match = pattern.search(html)
    return int(match.group(1)) if match else -1


def _rendered_attr_count(html: str, needle: str) -> int:
    return html.count(needle)


def _rendered_register_filter_count(html: str, filter_key: str) -> int:
    rows = re.findall(r'<tr class="register-row search-item [^"]+"([^>]*)>', html)
    ids: set[str] = set()
    for attrs in rows:
        if 'data-panel="register"' not in attrs or 'data-section-role="register"' not in attrs:
            continue
        if filter_key == "attention" and 'data-attention="true"' not in attrs:
            continue
        if filter_key == "proof-risk" and 'data-proof-risk="true"' not in attrs:
            continue
        if filter_key == "closed" and 'data-closed="true"' not in attrs:
            continue
        if filter_key.startswith("status:"):
            status = filter_key.split(":", 1)[1]
            if f'data-status="{status}"' not in attrs:
                continue
        match = re.search(r'data-task-id="([^"]+)"', attrs)
        if match:
            ids.add(match.group(1))
    return len(ids)


def _duplicate_task_ids(tasks: tuple[WorkspaceTask, ...]) -> list[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for task in tasks:
        if task.id in seen:
            duplicates.add(task.id)
        seen.add(task.id)
    return sorted(duplicates)


def _missing_source_refs(
    config: DtpConfig,
    tasks: tuple[WorkspaceTask, ...],
) -> list[dict[str, str]]:
    missing: list[dict[str, str]] = []
    local_prefixes = ("docs/", "practice-os/", "prompts/", "decisions/")
    for task in tasks:
        for ref in task.source_refs:
            ref_path = ref.split("#", 1)[0]
            if not ref_path.startswith(local_prefixes):
                continue
            if not (config.repo_root / ref_path).exists():
                missing.append({"task_id": task.id, "title": task.title, "source_ref": ref})
    return missing


def _validation_markdown(summary: dict[str, Any]) -> str:
    categories = summary["categories"]
    lines = [
        "# Workspace Dashboard Validation",
        "",
        f"Generated: {summary['generated_at']}",
        f"Status: {'ok' if summary['ok'] else 'needs attention'}",
        "",
        "| Category | Count |",
        "|---|---:|",
    ]
    for key in (
        "in_dashboard",
        "recovery_inbox",
        "excluded_or_redacted",
        "duplicate_merged",
        "source_missing",
        "count_mismatch",
        "duplicate_task_ids",
    ):
        lines.append(f"| {key} | {categories[key]} |")
    lines.extend(
        [
            "",
            f"- Reviewed operating rows: {summary['reviewed_operating_rows']}",
            f"- Closed rows: {summary['closed_rows']}",
            f"- Dry-run candidates: {summary['dry_run_candidates']}",
            "- Total accounted for in dashboard + recovery inbox: "
            f"{summary['total_accounted_for']}",
            "",
            "## Count Mismatches",
            "",
        ]
    )
    if summary["count_mismatches"]:
        lines.extend(f"- {item}" for item in summary["count_mismatches"])
    else:
        lines.append("- None")
    lines.extend(["", "## Recovery Bucket Counts", ""])
    for bucket, count in summary["recovery_bucket_counts"].items():
        lines.append(f"- {RECOVERY_BUCKET_LABELS.get(bucket, bucket)}: {count}")
    lines.extend(["", "## Duplicate Task IDs", ""])
    if summary["duplicate_task_ids"]:
        lines.extend(f"- {task_id}" for task_id in summary["duplicate_task_ids"][:50])
    else:
        lines.append("- None")
    lines.extend(["", "## Missing Local Source Refs", ""])
    if summary["missing_sources"]:
        lines.extend(
            f"- {item['title']}: {item['source_ref']}"
            for item in summary["missing_sources"][:50]
        )
    else:
        lines.append("- None")
    lines.extend(["", "## Private/COI Rows Requiring Redaction Review", ""])
    if summary["unsafe_private_rows"]:
        lines.extend(
            f"- {item['title']} ({item['sensitivity']})"
            for item in summary["unsafe_private_rows"][:50]
        )
    else:
        lines.append("- None")
    return "\n".join(lines) + "\n"
