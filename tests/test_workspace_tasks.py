from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

from dtp.cli import app
from dtp.commands.kaizen import run_kaizen_capture
from dtp.commands.workspace_tasks import (
    WorkspaceTask,
    build_workspace_recovery_inbox_tasks,
    dedupe_workspace_tasks,
    read_workspace_tasks,
    run_workspace_recover,
    run_workspace_task_add,
    workspace_task_ledger_path,
    write_notion_cockpit_export,
    write_workspace_tasks,
)
from dtp.config import DtpConfig


def test_workspace_task_ledger_round_trips_active_and_terminal_statuses(
    tmp_path: Path,
) -> None:
    config = _config(tmp_path)
    now = _task("Active recovered task", status="now")
    cancelled = _task(
        "Cancelled recovered task",
        status="cancelled",
        closed_at="2026-05-05",
        closure_reason="operator rejected the older path",
    )

    path = write_workspace_tasks(config, (now, cancelled))

    assert path == tmp_path / "practice-os" / "workspace" / "task-ledger.jsonl"
    assert read_workspace_tasks(config) == (now, cancelled)


def test_recovery_extracts_structured_sources_and_dedupes(tmp_path: Path) -> None:
    config = _config(tmp_path)
    _write_backlog(tmp_path)
    _write_proof_queue(tmp_path)
    _write_repo_board(tmp_path)
    _write_workspace_yaml(tmp_path)
    run_kaizen_capture(
        config,
        "Older backlog story should appear.",
        item_type="feature",
        status="now",
        sensitivity="internal-only",
        repo="diagnose-to-plan",
        next_action="merge evidence refs from duplicate sources",
    )

    result = run_workspace_recover(config)
    titles = {task.title for task in result.candidates}
    duplicate = next(
        task for task in result.candidates if task.title == "Older backlog story should appear."
    )

    assert "Older backlog story should appear." in titles
    assert "DeMario launch-feedback social packet" in titles
    assert "Architected Strength local board story" in titles
    assert len([task for task in result.candidates if task.title == duplicate.title]) == 1
    assert any("ROADMAP_EXECUTION_BACKLOG" in ref for ref in duplicate.source_refs)
    assert any("practice-os/kaizen/intake.jsonl" in ref for ref in duplicate.source_refs)


def test_recovery_dry_run_writes_outputs_without_mutating_ledger(tmp_path: Path) -> None:
    config = _config(tmp_path)
    _write_backlog(tmp_path)

    result = run_workspace_recover(config)

    assert result.dry_run_json_path == tmp_path / "outputs" / "workspace-recovery-candidates.json"
    assert result.dry_run_markdown_path == tmp_path / "outputs" / "workspace-recovery-candidates.md"
    assert result.notion_export_path == tmp_path / "outputs" / "notion-workspace-cockpit.json"
    assert result.dry_run_json_path.exists()
    assert result.dry_run_markdown_path.exists()
    assert result.notion_export_path.exists()
    assert not workspace_task_ledger_path(config).exists()


def test_recovery_apply_imports_reviewed_candidates(tmp_path: Path) -> None:
    config = _config(tmp_path)
    approved_path = tmp_path / "outputs" / "approved.json"
    approved_path.parent.mkdir(parents=True, exist_ok=True)
    approved = [_task("Approved recovery task", status="waiting").to_dict()]
    approved_path.write_text(json.dumps({"candidates": approved}), encoding="utf-8")

    result = run_workspace_recover(config, apply=True, approved_path=approved_path)

    assert result.imported_count == 1
    assert workspace_task_ledger_path(config).exists()
    assert read_workspace_tasks(config)[0].title == "Approved recovery task"
    assert result.notion_export_path == tmp_path / "outputs" / "notion-workspace-cockpit.json"


def test_dedupe_merges_evidence_without_losing_terminal_closure() -> None:
    left = _task(
        "Same thing",
        status="superseded",
        source_refs=("docs/old.md",),
        closed_at="2026-05-05",
        superseded_by="docs/new.md",
    )
    right = _task("Same thing", status="next", source_refs=("docs/new.md",))

    (merged,) = dedupe_workspace_tasks((left, right))

    assert merged.status == "next"
    assert merged.closed_at == "2026-05-05"
    assert merged.superseded_by == "docs/new.md"
    assert merged.source_refs == ("docs/new.md", "docs/old.md")


def test_private_or_coi_rows_are_not_exported_raw_to_notion(tmp_path: Path) -> None:
    config = _config(tmp_path)
    private = _task(
        "Private client payment timing",
        status="waiting",
        sensitivity="private-client",
    )
    public_stub = _task(
        "[redacted private-client task]",
        status="waiting",
        sensitivity="private-client",
    )

    path = write_notion_cockpit_export(config, (private, public_stub))
    payload = path.read_text(encoding="utf-8")

    assert "Private client payment timing" not in payload
    assert "[redacted private-client task]" in payload


def test_workspace_recover_cli_dry_run(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    _write_backlog(tmp_path)

    result = CliRunner().invoke(app, ["workspace", "recover", "--dry-run"])

    assert result.exit_code == 0
    assert "workspace recovery dry-run" in result.output
    assert (tmp_path / "outputs" / "workspace-recovery-candidates.json").exists()
    assert not (tmp_path / "practice-os" / "workspace" / "task-ledger.jsonl").exists()


def test_recovery_inbox_accounts_for_unreviewed_session_and_memory_candidates(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.setattr(Path, "home", lambda: tmp_path)
    config = _config(tmp_path)
    _write_backlog(tmp_path)
    _write_recovery_sources(tmp_path)

    inbox = build_workspace_recovery_inbox_tasks(config)

    titles = {task.title for task in inbox}
    assert "Review Codex session: Dashboard recovery candidate" in titles
    assert "Memory pointer: dashboard memory recovery candidate" in titles


def test_workspace_task_add_appends_reviewed_row(tmp_path: Path) -> None:
    config = _config(tmp_path)

    task = run_workspace_task_add(
        config,
        title="Manual reviewed task",
        repo="diagnose-to-plan",
        status="waiting",
        priority="P1",
        next_action="wait for owner input",
        source_ref="docs/source.md",
        sensitivity="internal-only",
        confidence="high",
    )

    assert task.status == "waiting"
    assert read_workspace_tasks(config)[0].title == "Manual reviewed task"
    assert (tmp_path / "outputs" / "notion-workspace-cockpit.json").exists()


def test_workspace_task_add_rejects_incomplete_rows(tmp_path: Path) -> None:
    config = _config(tmp_path)

    try:
        run_workspace_task_add(
            config,
            title="",
            repo="diagnose-to-plan",
            status="now",
            priority="P1",
            next_action="review",
            source_ref="docs/source.md",
            sensitivity="internal-only",
            confidence="high",
        )
    except ValueError as error:
        assert "missing required field" in str(error)
    else:
        raise AssertionError("expected workspace task add to reject incomplete rows")


def test_workspace_task_add_cli(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))

    result = CliRunner().invoke(
        app,
        [
            "workspace",
            "task",
            "add",
            "--title",
            "CLI reviewed task",
            "--repo",
            "diagnose-to-plan",
            "--status",
            "now",
            "--priority",
            "P1",
            "--next-action",
            "review from dashboard",
            "--source-ref",
            "docs/source.md",
            "--sensitivity",
            "internal-only",
            "--confidence",
            "high",
        ],
    )

    assert result.exit_code == 0
    assert "workspace task added" in result.output
    assert (tmp_path / "practice-os" / "workspace" / "task-ledger.jsonl").exists()


def _task(
    title: str,
    *,
    status: str,
    source_refs: tuple[str, ...] = ("docs/source.md",),
    sensitivity: str = "internal-only",
    closed_at: str = "",
    closure_reason: str = "",
    superseded_by: str = "",
) -> WorkspaceTask:
    return WorkspaceTask(
        id=f"wst-test-{title.lower().replace(' ', '-')}",
        title=title,
        repo="diagnose-to-plan",
        lane="tests",
        status=status,
        priority="P2",
        next_action="review",
        blocked_by="",
        attention_reason="test fixture",
        source_refs=source_refs,
        evidence_refs=(),
        sensitivity=sensitivity,
        confidence="high",
        last_seen_at="2026-05-05",
        closed_at=closed_at,
        closure_reason=closure_reason,
        superseded_by=superseded_by,
    )


def _config(root: Path) -> DtpConfig:
    return DtpConfig(
        repo_root=root,
        inputs_dir=root / "inputs",
        outputs_dir=root / "outputs",
        skills_dir=root / "skills",
        extracts_dir=root / "extracts",
        practice_os_dir=root / "practice-os",
        engagements_dir=root / "engagements",
        workspace_file=root / ".dtp" / "workspace.yaml",
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
                "fixture gate | backlog next action |",
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
            ]
        ),
    )


def _write_repo_board(root: Path) -> None:
    _write(
        root / "architected-strength" / "docs" / "roadmap" / "kanban-board.md",
        "\n".join(
            [
                "# Kanban",
                "",
                "## Ready",
                "",
                "| ID | Priority | Epic | Story | Verification |",
                "|---|---|---|---|---|",
                "| AS-1 | P1 | Site | Architected Strength local board story | "
                "local board proof |",
            ]
        ),
    )


def _write_workspace_yaml(root: Path) -> None:
    _write(
        root / ".dtp" / "workspace.yaml",
        "\n".join(
            [
                "repos:",
                "  - name: architected-strength",
                "    path: ../architected-strength",
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
