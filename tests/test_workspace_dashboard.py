from __future__ import annotations

import re
from pathlib import Path

from typer.testing import CliRunner

from dtp.cli import app
from dtp.commands.kaizen import run_kaizen_capture
from dtp.commands.workspace_dashboard import (
    DashboardSurface,
    read_proof_queue,
    read_sweep_coverage,
    run_workspace_dashboard,
    run_workspace_dashboard_validation,
)
from dtp.commands.workspace_tasks import WorkspaceTask, write_workspace_tasks
from dtp.config import load_config


def test_workspace_dashboard_writes_viewable_html(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    _write_manifest(tmp_path, "consulting", repo="consulting", owner_lane="public site")
    _write_evidence(tmp_path, "consulting", lane="local", result="pass")
    _write_backlog(tmp_path)
    _write_proof_queue(tmp_path)
    _write_sweep_ledger(tmp_path)
    _write_recovery_sources(tmp_path)
    config = load_config(tmp_path)
    run_kaizen_capture(
        config,
        "Omnexus subscription review needs resubmission.",
        item_type="repo_issue",
        status="now",
        sensitivity="internal-only",
        repo="fitness-app",
        next_action="prepare version plus subscriptions checklist",
    )
    run_kaizen_capture(
        config,
        "Legacy live command runner idea was superseded by the read-only dashboard.",
        item_type="tooling",
        status="superseded",
        sensitivity="internal-only",
        repo="diagnose-to-plan",
        closure_reason="read-only dashboard boundary accepted",
        superseded_by="docs/WORKSPACE_DASHBOARD_READONLY.md",
    )
    run_kaizen_capture(
        config,
        "Transcript export dump was cancelled for privacy.",
        item_type="process",
        status="cancelled",
        sensitivity="internal-only",
        repo="diagnose-to-plan",
        closure_reason="summaries only",
    )

    result = run_workspace_dashboard(config)

    assert result.path == tmp_path / "docs" / "workspace-dashboard.html"
    assert result.path.exists()
    assert "Practice Work Dashboard" in result.html
    assert "Omnexus subscription review needs resubmission." in result.html
    assert "Accounting Summary" in result.html
    assert "Reviewed rows" in result.html
    assert "Recovery Inbox rows" in result.html
    assert "Total detected" in result.html
    assert "Reviewed closed" in result.html
    assert "not completed work" in result.html
    assert "Needs Attention" in result.html
    assert "Decision Needed" in result.html
    assert result.html.count('class="metric"') == 6
    expected_metrics = {
        "Needs Attention": ("register", "attention"),
        "Waiting On Toni/Owner": ("register", "status:waiting"),
        "Blocked": ("register", "status:blocked"),
        "Decision Needed": ("register", "status:decision_needed"),
        "Proof Blocked": ("register", "proof-risk"),
        "Recently Closed": ("register", "closed"),
    }
    for label, (target, filter_key) in expected_metrics.items():
        assert (
            f'<a class="metric" href="#{target}" data-tab-target="{target}" '
            f'data-dashboard-filter="{filter_key}" '
        ) in result.html
        assert f'aria-label="{_metric_count(result.html, label)} {label}"' in result.html
        assert label in result.html
    assert _metric_count(result.html, "Recently Closed") == result.closed_item_count
    assert 'id="dashboard-search"' in result.html
    assert 'id="filter-status"' in result.html
    assert 'id="clear-dashboard-filter"' in result.html
    assert 'id="orientation-panel"' in result.html
    assert 'id="orientation-filter"' in result.html
    assert 'id="jump-register"' in result.html
    assert 'data-empty-state="today"' in result.html
    assert 'data-tab-target="today"' in result.html
    assert 'data-tab-target="register"' in result.html
    assert 'data-tab-target="recovery"' in result.html
    assert 'role="tab"' in result.html
    assert 'role="tabpanel"' in result.html
    assert 'tabindex="0"' in result.html
    assert 'tabindex="-1"' in result.html
    assert 'tabindex="-1"' in result.html
    assert 'aria-controls="today"' in result.html
    assert 'aria-labelledby="tab-today"' in result.html
    assert 'window.location.hash' in result.html
    assert 'document.body.classList.add("js-enabled")' in result.html
    assert ".js-enabled .tab-panel" in result.html
    assert "function moveToPanel" in result.html
    assert "ArrowLeft" in result.html
    assert "ArrowRight" in result.html
    assert "Home" in result.html
    assert "End" in result.html
    assert "scrollIntoView" in result.html
    assert "focus({ preventScroll: true })" in result.html
    assert "Item Register" in result.html
    assert "Reviewed workspace item register" in result.html
    assert "Sources and metadata" in result.html
    assert "Recovery Inbox" in result.html
    assert "High-confidence import" in result.html
    assert "Merge/duplicate review" in result.html
    assert "Codex-session lead" in result.html
    assert "Memory pointer" in result.html
    assert "Private/COI gated" in result.html
    assert "Likely discard" in result.html
    assert 'data-recovery-bucket="' in result.html
    assert 'data-recovery-bucket-chip="' in result.html
    assert "Approved JSON starter" in result.html
    assert 'id="register-status"' in result.html
    assert 'data-task-id="' in result.html
    assert 'data-status="now"' in result.html
    assert 'data-attention="true"' in result.html
    assert 'data-proof-risk="true"' in result.html
    assert 'data-closed="true"' in result.html
    assert 'data-repo="fitness-app"' in result.html
    assert 'data-panel="today"' in result.html
    assert 'data-section-role="daily-action"' in result.html
    assert 'data-section-role="preview"' in result.html
    assert 'data-panel="register" data-section-role="register"' in result.html
    assert 'data-panel="recovery" data-section-role="recovery"' in result.html
    assert _register_count(result.html, "closed") == result.closed_item_count
    assert result.html.count('data-closed="true"') >= result.closed_item_count
    assert result.html.index("Today") < result.html.index("Repos")
    assert "Proof Queue" in result.html
    assert "Archive" in result.html
    assert "Sweep Coverage" in result.html
    assert "Older backlog story should appear." in result.html
    assert "Legacy live command runner idea was superseded" in result.html
    assert "Transcript export dump was cancelled" in result.html
    assert "13 repos" in result.html
    assert "DeMario launch-feedback social packet" in result.html
    assert (tmp_path / "outputs" / "notion-workspace-cockpit.json").exists()
    assert result.active_item_count >= 3
    assert result.closed_item_count == 2
    assert result.recovery_inbox_count == 2
    assert result.proof_candidate_count == 1
    assert result.sweep_scope_count == 2


def _metric_count(html: str, label: str) -> int:
    pattern = re.compile(
        r'<a class="metric"[^>]*><strong>(\d+)</strong><span>'
        + re.escape(label)
        + r"</span></a>"
    )
    match = pattern.search(html)
    assert match is not None
    return int(match.group(1))


def _register_count(html: str, status: str) -> int:
    status_pattern = (
        rf'data-status="{re.escape(status)}"'
        if status != "closed"
        else r'data-closed="true"'
    )
    return len(
        re.findall(
            r'<tr class="register-row search-item [^"]+"[^>]*'
            + status_pattern
            + r'[^>]*data-panel="register" data-section-role="register"',
            html,
        )
    )


def test_read_proof_queue_parses_current_candidates(tmp_path: Path) -> None:
    _write_proof_queue(tmp_path)

    rows = read_proof_queue(load_config(tmp_path))

    assert len(rows) == 1
    assert rows[0].candidate == "DeMario launch-feedback social packet"
    assert rows[0].status == "candidate_intake"


def test_read_sweep_coverage_parses_ledger(tmp_path: Path) -> None:
    _write_sweep_ledger(tmp_path)

    rows = read_sweep_coverage(load_config(tmp_path))

    assert len(rows) == 2
    assert rows[0].scope == "Workspace repos"
    assert rows[0].coverage == "13 repos"


def test_workspace_dashboard_cli_writes_default_output(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    _write_manifest(tmp_path, "tm-skills", repo="tm-skills", owner_lane="skills")
    _write_evidence(tmp_path, "tm-skills", lane="local", result="pass")
    _write_backlog(tmp_path)

    result = CliRunner().invoke(app, ["workspace", "dashboard"])

    assert result.exit_code == 0
    assert "workspace dashboard written" in result.output
    assert (tmp_path / "docs" / "workspace-dashboard.html").exists()
    assert (tmp_path / "outputs" / "notion-workspace-cockpit.json").exists()


def test_workspace_dashboard_vscode_surface_uses_theme_tokens(tmp_path: Path) -> None:
    _write_manifest(
        tmp_path,
        "architected-strength",
        repo="architected-strength",
        owner_lane="site",
    )
    _write_evidence(tmp_path, "architected-strength", lane="local", result="pass")
    _write_backlog(tmp_path)
    config = load_config(tmp_path)

    result = run_workspace_dashboard(
        config,
        output_path=Path("outputs/workspace-dashboard.html"),
        surface=DashboardSurface.vscode,
    )

    assert result.path == tmp_path / "outputs" / "workspace-dashboard.html"
    assert 'class="vscode"' in result.html
    assert "--vscode-foreground" in result.html
    assert "--soft: var(--vscode-input-background" in result.html
    assert "background: var(--paper);" in result.html
    assert ".accounting-summary" in result.html
    assert "background: var(--panel);" in result.html
    assert ".accounting-card" in result.html
    assert "var(--vscode-editorWidget-background, var(--panel))" in result.html


def test_workspace_dashboard_cli_accepts_vscode_surface(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    _write_manifest(tmp_path, "demario", repo="demario-pickleball-1", owner_lane="launch")
    _write_evidence(tmp_path, "demario", lane="local", result="pass")
    _write_backlog(tmp_path)

    result = CliRunner().invoke(
        app,
        [
            "workspace",
            "dashboard",
            "--surface",
            "vscode",
            "--out",
            "outputs/workspace-dashboard.html",
        ],
    )

    assert result.exit_code == 0
    dashboard = tmp_path / "outputs" / "workspace-dashboard.html"
    assert dashboard.exists()
    assert 'class="vscode"' in dashboard.read_text(encoding="utf-8")


def test_workspace_dashboard_validation_reports_missing_sources(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    config = load_config(tmp_path)
    write_workspace_tasks(
        config,
        (
            WorkspaceTask(
                id="wst-missing-source",
                title="Missing source fixture",
                repo="diagnose-to-plan",
                lane="tests",
                status="now",
                priority="P1",
                next_action="fix source",
                blocked_by="",
                attention_reason="test",
                source_refs=("docs/missing-source.md",),
                evidence_refs=(),
                sensitivity="internal-only",
                confidence="high",
                last_seen_at="2026-05-05",
            ),
        ),
    )

    result = run_workspace_dashboard_validation(config)

    assert not result.ok
    assert result.summary["categories"]["source_missing"] == 1
    assert "duplicate_task_ids" in result.summary["categories"]
    assert "register_metric_counts" in result.summary
    assert "recovery_bucket_counts" in result.summary
    assert "duplicate_task_ids" in result.summary
    assert result.json_path.exists()
    assert result.markdown_path.exists()


def _write_manifest(root: Path, slug: str, *, repo: str, owner_lane: str) -> None:
    _write(
        root / "practice-os" / "efficiency" / f"{slug}-repo-manifest.md",
        "\n".join(
            [
                f"# Repo Manifest: {repo}",
                "",
                "## Identity",
                "",
                f"- Repo: `{repo}`",
                f"- Owner lane: {owner_lane}",
                "",
                "## Gates",
                "",
                "- Local gate: local gate",
                "- CI gate: ci gate",
                "- Manual gate: manual gate",
                "",
                "## Next Touch",
                "",
                "- Blocker: none",
                "- Next action: keep current",
            ]
        ),
    )


def _write_evidence(root: Path, slug: str, *, lane: str, result: str) -> None:
    _write(
        root / "practice-os" / "efficiency" / f"{slug}-evidence-index.md",
        "\n".join(
            [
                "# Evidence Index",
                "",
                "## Latest Verification",
                "",
                "| Lane | Date | Result | Commit | Artifact |",
                "|---|---|---|---|---|",
                f"| {lane} | 2026-05-05 | {result} | abc123 | local gate |",
            ]
        ),
    )


def _write_backlog(root: Path) -> None:
    _write(
        root / "docs" / "ROADMAP_EXECUTION_BACKLOG.md",
        "\n".join(
            [
                "# Backlog",
                "",
                "## Epic 1",
                "",
                "| Story | Repo | Status | Done gate | Next action |",
                "|---|---|---|---|---|",
                "| Older backlog story should appear. | diagnose-to-plan | Ready | "
                "fixture gate | review fixture row |",
                "",
                "## Current Active Next Queue",
                "",
                "1. Keep Omnexus subscription review visible.",
                "2. Keep Hub parked.",
                "",
                "## Later",
            ]
        ),
    )


def _write_proof_queue(root: Path) -> None:
    _write(
        root / "docs" / "PRACTICE_PROOF_QUEUE_INDEX.md",
        "\n".join(
            [
                "# Practice Proof Queue Index",
                "",
                "## Current Proof Candidates",
                "",
                "| Candidate | Lane | Source pointer | Offer supported | Status | "
                "Next proof action | Hard gates |",
                "|---|---|---|---|---|---|---|",
                "| DeMario launch-feedback social packet | demario-pickleball-1 | "
                "evidence-index | Launch Sprint | candidate_intake | draft social copy | "
                "owner permission |",
                "",
                "## Next Review Queue",
            ]
        ),
    )


def _write_sweep_ledger(root: Path) -> None:
    _write(
        root / "docs" / "WORKSPACE_DOCS_AND_CHAT_SWEEP_LEDGER_2026-05-05.md",
        "\n".join(
            [
                "# Workspace Docs And Chat Sweep Ledger",
                "",
                "## Sweep Coverage",
                "",
                "| Scope | Coverage | Notes |",
                "|---|---:|---|",
                "| Workspace repos | 13 repos | all workspace repos inventoried |",
                "| Codex sessions | 88 files | session index plus active and archived JSONL |",
                "",
                "## Recovered Tracker Rows",
            ]
        ),
    )


def _write_recovery_sources(root: Path) -> None:
    _write(
        root / ".codex" / "session_index.jsonl",
        (
            '{"id":"session-1","thread_name":"Dashboard recovery candidate",'
            '"updated_at":"2026-05-05T00:00:00Z"}\n'
        ),
    )
    _write(
        root / ".codex" / "memories" / "MEMORY.md",
        "# Task Group: dashboard memory recovery candidate\n",
    )


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
