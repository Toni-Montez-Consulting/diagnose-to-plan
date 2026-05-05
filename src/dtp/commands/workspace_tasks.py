from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from dtp.commands.kaizen import (
    PRIVATE_SENSITIVITIES,
    KaizenRecord,
    read_kaizen_records,
)
from dtp.config import DtpConfig

ACTIVE_TASK_STATUSES = (
    "inbox",
    "now",
    "next",
    "waiting",
    "blocked",
    "parked",
    "decision_needed",
)
TERMINAL_TASK_STATUSES = ("done", "cancelled", "superseded", "discarded")
TASK_STATUSES = (*ACTIVE_TASK_STATUSES, *TERMINAL_TASK_STATUSES)
PRIVATE_TASK_SENSITIVITIES = {*PRIVATE_SENSITIVITIES, "private", "financial"}
DEFAULT_RECOVERY_JSON = "workspace-recovery-candidates.json"
DEFAULT_RECOVERY_MD = "workspace-recovery-candidates.md"
DEFAULT_NOTION_EXPORT = "notion-workspace-cockpit.json"


@dataclass(frozen=True)
class WorkspaceTask:
    id: str
    title: str
    repo: str
    lane: str
    status: str
    priority: str
    next_action: str
    blocked_by: str
    attention_reason: str
    source_refs: tuple[str, ...]
    evidence_refs: tuple[str, ...]
    sensitivity: str
    confidence: str
    last_seen_at: str
    closed_at: str = ""
    closure_reason: str = ""
    superseded_by: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "repo": self.repo,
            "lane": self.lane,
            "status": self.status,
            "priority": self.priority,
            "next_action": self.next_action,
            "blocked_by": self.blocked_by,
            "attention_reason": self.attention_reason,
            "source_refs": list(self.source_refs),
            "evidence_refs": list(self.evidence_refs),
            "sensitivity": self.sensitivity,
            "confidence": self.confidence,
            "last_seen_at": self.last_seen_at,
            "closed_at": self.closed_at,
            "closure_reason": self.closure_reason,
            "superseded_by": self.superseded_by,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> WorkspaceTask:
        title = str(data["title"]).strip()
        repo = str(data.get("repo", "diagnose-to-plan")).strip() or "diagnose-to-plan"
        status = normalize_task_status(str(data.get("status", "inbox")))
        return cls(
            id=str(data.get("id") or make_task_id(repo, title)),
            title=title,
            repo=repo,
            lane=str(data.get("lane", "")).strip(),
            status=status,
            priority=str(data.get("priority", "P2")).strip() or "P2",
            next_action=str(data.get("next_action", "")).strip(),
            blocked_by=str(data.get("blocked_by", "")).strip(),
            attention_reason=str(data.get("attention_reason", "")).strip(),
            source_refs=tuple(str(ref).strip() for ref in data.get("source_refs", ()) if ref),
            evidence_refs=tuple(str(ref).strip() for ref in data.get("evidence_refs", ()) if ref),
            sensitivity=str(data.get("sensitivity", "internal-only")).strip() or "internal-only",
            confidence=str(data.get("confidence", "medium")).strip() or "medium",
            last_seen_at=str(data.get("last_seen_at", "")).strip(),
            closed_at=str(data.get("closed_at", "")).strip(),
            closure_reason=str(data.get("closure_reason", "")).strip(),
            superseded_by=str(data.get("superseded_by", "")).strip(),
        )


@dataclass(frozen=True)
class WorkspaceRecoverResult:
    candidates: tuple[WorkspaceTask, ...]
    imported_count: int
    dry_run_json_path: Path | None
    dry_run_markdown_path: Path | None
    notion_export_path: Path | None
    ledger_path: Path


def workspace_task_ledger_path(config: DtpConfig) -> Path:
    return config.practice_os_dir / "workspace" / "task-ledger.jsonl"


def read_workspace_tasks(config: DtpConfig) -> tuple[WorkspaceTask, ...]:
    path = workspace_task_ledger_path(config)
    if not path.exists():
        return ()
    tasks: list[WorkspaceTask] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                tasks.append(WorkspaceTask.from_dict(json.loads(line)))
            except (KeyError, TypeError, json.JSONDecodeError) as error:
                msg = f"invalid workspace task at {path.as_posix()}:{line_number}"
                raise ValueError(msg) from error
    return tuple(tasks)


def write_workspace_tasks(config: DtpConfig, tasks: tuple[WorkspaceTask, ...]) -> Path:
    path = workspace_task_ledger_path(config)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(task.to_dict(), sort_keys=True) for task in tasks]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8", newline="\n")
    return path


def build_workspace_dashboard_tasks(config: DtpConfig) -> tuple[WorkspaceTask, ...]:
    return recover_workspace_task_candidates(
        config,
        include_codex_sessions=False,
        include_memory_registry=False,
    )


def build_workspace_recovery_inbox_tasks(config: DtpConfig) -> tuple[WorkspaceTask, ...]:
    dashboard_tasks = build_workspace_dashboard_tasks(config)
    dashboard_keys = {_task_key(task) for task in dashboard_tasks}
    all_candidates = recover_workspace_task_candidates(config)
    return tuple(
        task
        for task in all_candidates
        if _task_key(task) not in dashboard_keys
    )


def collect_workspace_task_source_candidates(
    config: DtpConfig,
    *,
    include_codex_sessions: bool = True,
    include_memory_registry: bool = True,
) -> tuple[WorkspaceTask, ...]:
    now = datetime.now(UTC).date().isoformat()
    candidates: list[WorkspaceTask] = [
        *read_workspace_tasks(config),
        *_tasks_from_kaizen(config, now),
        *_tasks_from_backlog(config, now),
        *_tasks_from_proof_queue(config, now),
        *_tasks_from_repo_local_boards(config, now),
    ]
    if include_codex_sessions:
        candidates.extend(_tasks_from_codex_session_index(now))
    if include_memory_registry:
        candidates.extend(_tasks_from_memory_registry(now))
    return tuple(candidates)


def run_workspace_task_add(
    config: DtpConfig,
    *,
    title: str,
    repo: str,
    status: str,
    priority: str,
    next_action: str,
    source_ref: str,
    sensitivity: str,
    confidence: str,
    lane: str = "Manual Workspace Task",
    blocked_by: str = "",
    attention_reason: str = "manual reviewed workspace task",
    evidence_ref: str = "",
    closed_at: str = "",
    closure_reason: str = "",
    superseded_by: str = "",
) -> WorkspaceTask:
    required = {
        "title": title,
        "repo": repo,
        "status": status,
        "priority": priority,
        "next_action": next_action,
        "source_ref": source_ref,
        "sensitivity": sensitivity,
        "confidence": confidence,
    }
    missing = [name for name, value in required.items() if not str(value).strip()]
    if missing:
        raise ValueError(f"workspace task add missing required field(s): {', '.join(missing)}")
    normalized_status = normalize_task_status(status)
    if normalized_status == "inbox" and status.strip().lower().replace("-", "_") != "inbox":
        raise ValueError(f"unsupported workspace task status: {status}")
    task = WorkspaceTask(
        id=make_task_id(repo, title),
        title=title.strip(),
        repo=repo.strip(),
        lane=lane.strip() or "Manual Workspace Task",
        status=normalized_status,
        priority=priority.strip().upper(),
        next_action=next_action.strip(),
        blocked_by=blocked_by.strip(),
        attention_reason=attention_reason.strip() or "manual reviewed workspace task",
        source_refs=_unique_refs((source_ref.strip(),)),
        evidence_refs=_unique_refs((evidence_ref.strip(),)),
        sensitivity=sensitivity.strip(),
        confidence=confidence.strip(),
        last_seen_at=datetime.now(UTC).date().isoformat(),
        closed_at=closed_at.strip(),
        closure_reason=closure_reason.strip(),
        superseded_by=superseded_by.strip(),
    )
    merged = dedupe_workspace_tasks((*read_workspace_tasks(config), task))
    write_workspace_tasks(config, merged)
    write_notion_cockpit_export(config, merged)
    return task


def run_workspace_recover(
    config: DtpConfig,
    *,
    apply: bool = False,
    approved_path: Path | None = None,
) -> WorkspaceRecoverResult:
    ledger_path = workspace_task_ledger_path(config)
    if apply:
        if approved_path is None:
            raise ValueError("workspace recover --apply requires --approved PATH")
        approved = _read_approved_tasks(_resolve_path(config.repo_root, approved_path))
        merged = dedupe_workspace_tasks((*read_workspace_tasks(config), *approved))
        write_workspace_tasks(config, merged)
        notion_path = write_notion_cockpit_export(config, merged)
        return WorkspaceRecoverResult(
            candidates=merged,
            imported_count=len(approved),
            dry_run_json_path=None,
            dry_run_markdown_path=None,
            notion_export_path=notion_path,
            ledger_path=ledger_path,
        )

    candidates = recover_workspace_task_candidates(config)
    json_path = _write_recovery_json(config, candidates)
    markdown_path = _write_recovery_markdown(config, candidates)
    notion_path = write_notion_cockpit_export(config, candidates)
    return WorkspaceRecoverResult(
        candidates=candidates,
        imported_count=0,
        dry_run_json_path=json_path,
        dry_run_markdown_path=markdown_path,
        notion_export_path=notion_path,
        ledger_path=ledger_path,
    )


def recover_workspace_task_candidates(
    config: DtpConfig,
    *,
    include_codex_sessions: bool = True,
    include_memory_registry: bool = True,
) -> tuple[WorkspaceTask, ...]:
    return dedupe_workspace_tasks(
        collect_workspace_task_source_candidates(
            config,
            include_codex_sessions=include_codex_sessions,
            include_memory_registry=include_memory_registry,
        )
    )


def dedupe_workspace_tasks(tasks: tuple[WorkspaceTask, ...]) -> tuple[WorkspaceTask, ...]:
    merged: dict[str, WorkspaceTask] = {}
    for task in tasks:
        key = _task_key(task)
        existing = merged.get(key)
        merged[key] = task if existing is None else _merge_task(existing, task)
    return tuple(sorted(merged.values(), key=_task_sort_key))


def normalize_task_status(status: str) -> str:
    normalized = status.strip().lower().replace("-", "_").replace(" ", "_")
    aliases = {
        "active_next": "now",
        "active": "now",
        "ready": "next",
        "review": "decision_needed",
        "later": "parked",
        "seeded": "next",
        "canceled": "cancelled",
    }
    normalized = aliases.get(normalized, normalized)
    if normalized not in TASK_STATUSES:
        return "inbox"
    return normalized


def make_task_id(repo: str, title: str) -> str:
    slug = _slug(f"{repo}-{title}")[:70] or "workspace-task"
    digest = hashlib.sha1(f"{repo}\n{title}".encode()).hexdigest()[:8]
    return f"wst-{slug}-{digest}"


def write_notion_cockpit_export(
    config: DtpConfig,
    tasks: tuple[WorkspaceTask, ...],
    *,
    path: Path | None = None,
) -> Path:
    output_path = _resolve_path(
        config.repo_root,
        path or config.outputs_dir / DEFAULT_NOTION_EXPORT,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "source": "diagnose-to-plan",
        "boundary": "notion mirror only; DTP remains source of truth",
        "views": [
            "Today",
            "Waiting On",
            "Decision Needed",
            "Proof Blocked",
            "Repo Health",
            "Archive",
            "Idea Inbox",
        ],
        "rows": [_notion_row(task) for task in tasks if _is_notion_safe(task)],
    }
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    return output_path


def _tasks_from_kaizen(config: DtpConfig, today: str) -> tuple[WorkspaceTask, ...]:
    return tuple(_task_from_kaizen(record, today) for record in read_kaizen_records(config))


def _task_from_kaizen(record: KaizenRecord, today: str) -> WorkspaceTask:
    status = normalize_task_status(record.status)
    source_refs = (f"practice-os/kaizen/intake.jsonl#{record.id}",)
    if record.dtp_source_path:
        source_refs = (record.dtp_source_path, *source_refs)
    return WorkspaceTask(
        id=make_task_id(record.repo, record.title),
        title=record.title,
        repo=record.repo,
        lane=record.item_type,
        status=status,
        priority=_priority_for_status(status),
        next_action=record.next_action,
        blocked_by="",
        attention_reason=_attention_reason(status, record.item_type, record.next_action),
        source_refs=_unique_refs(source_refs),
        evidence_refs=record.evidence_refs,
        sensitivity=record.sensitivity,
        confidence="high",
        last_seen_at=record.captured_at[:10] or today,
        closed_at=record.closed_at,
        closure_reason=record.closure_reason,
        superseded_by=record.superseded_by,
    )


def _tasks_from_backlog(config: DtpConfig, today: str) -> tuple[WorkspaceTask, ...]:
    path = config.repo_root / "docs" / "ROADMAP_EXECUTION_BACKLOG.md"
    if not path.exists():
        return ()
    tasks: list[WorkspaceTask] = []
    heading = "Roadmap"
    in_story_table = False
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            heading = stripped.removeprefix("## ").strip()
            in_story_table = False
            continue
        if not stripped.startswith("|"):
            in_story_table = False
            continue
        cells = [_clean_cell(cell) for cell in stripped.strip("|").split("|")]
        lower = [cell.lower() for cell in cells]
        if len(cells) >= 5 and lower[:5] == [
            "story",
            "repo",
            "status",
            "done gate",
            "next action",
        ]:
            in_story_table = True
            continue
        if not in_story_table or _is_markdown_rule(cells) or len(cells) < 5:
            continue
        title, repo, raw_status, done_gate, next_action = cells[:5]
        status = normalize_task_status(raw_status)
        tasks.append(
            WorkspaceTask(
                id=make_task_id(repo, title),
                title=title,
                repo=repo or "diagnose-to-plan",
                lane=heading,
                status=status,
                priority=_priority_for_status(status),
                next_action=next_action,
                blocked_by=done_gate if status in {"blocked", "waiting", "decision_needed"} else "",
                attention_reason=_attention_reason(status, heading, next_action),
                source_refs=(f"docs/ROADMAP_EXECUTION_BACKLOG.md#{_slug(title)}",),
                evidence_refs=(done_gate,) if status == "done" and done_gate else (),
                sensitivity=_sensitivity_for_repo(repo),
                confidence="high",
                last_seen_at=today,
            )
        )
    return tuple(tasks)


def _tasks_from_proof_queue(config: DtpConfig, today: str) -> tuple[WorkspaceTask, ...]:
    path = config.repo_root / "docs" / "PRACTICE_PROOF_QUEUE_INDEX.md"
    if not path.exists():
        return ()
    rows: list[WorkspaceTask] = []
    in_section = False
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped == "## Current Proof Candidates":
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            break
        if not in_section or not stripped.startswith("|"):
            continue
        cells = [_clean_cell(cell) for cell in stripped.strip("|").split("|")]
        if len(cells) < 7 or cells[0].lower() == "candidate" or _is_markdown_rule(cells):
            continue
        title, lane, source_pointer, _offer, raw_status, next_action, gates = cells[:7]
        status = _status_from_proof_status(raw_status)
        source_refs = _split_source_refs(source_pointer)
        rows.append(
            WorkspaceTask(
                id=make_task_id(lane, title),
                title=title,
                repo=_repo_from_lane(lane),
                lane="Proof Queue",
                status=status,
                priority="P1",
                next_action=next_action,
                blocked_by=gates,
                attention_reason=f"proof gate: {raw_status}",
                source_refs=_unique_refs(("docs/PRACTICE_PROOF_QUEUE_INDEX.md", *source_refs)),
                evidence_refs=source_refs,
                sensitivity=_sensitivity_for_repo(lane),
                confidence="high",
                last_seen_at=today,
            )
        )
    return tuple(rows)


def _tasks_from_repo_local_boards(config: DtpConfig, today: str) -> tuple[WorkspaceTask, ...]:
    tasks: list[WorkspaceTask] = []
    for repo_name, repo_path in _workspace_repo_paths(config).items():
        board = repo_path / "docs" / "roadmap" / "kanban-board.md"
        if not board.exists():
            continue
        tasks.extend(_parse_repo_kanban(repo_name, board, today))
    return tuple(tasks)


def _parse_repo_kanban(repo: str, path: Path, today: str) -> tuple[WorkspaceTask, ...]:
    tasks: list[WorkspaceTask] = []
    section = ""
    in_table = False
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            section = stripped.removeprefix("## ").strip()
            in_table = False
            continue
        if not stripped.startswith("|"):
            in_table = False
            continue
        cells = [_clean_cell(cell) for cell in stripped.strip("|").split("|")]
        if len(cells) >= 5 and [cell.lower() for cell in cells[:5]] == [
            "id",
            "priority",
            "epic",
            "story",
            "verification",
        ]:
            in_table = True
            continue
        if not in_table or _is_markdown_rule(cells) or len(cells) < 5:
            continue
        task_id, priority, epic, story, verification = cells[:5]
        status = _status_from_board_section(section)
        tasks.append(
            WorkspaceTask(
                id=make_task_id(repo, story),
                title=story,
                repo=repo,
                lane=epic or section,
                status=status,
                priority=priority or _priority_for_status(status),
                next_action=verification if status != "done" else "preserve local board evidence",
                blocked_by=verification if status in {"blocked", "waiting"} else "",
                attention_reason=f"repo-local board: {section}",
                source_refs=(f"{repo}:{path.name}#{task_id}",),
                evidence_refs=(verification,) if status == "done" else (),
                sensitivity="internal-only",
                confidence="high",
                last_seen_at=today,
            )
        )
    return tuple(tasks)


def _tasks_from_codex_session_index(today: str) -> tuple[WorkspaceTask, ...]:
    path = Path.home() / ".codex" / "session_index.jsonl"
    if not path.exists():
        return ()
    tasks: list[WorkspaceTask] = []
    keywords = re.compile(
        r"roadmap|dashboard|kanban|recover|audit|implement|launch|update|add|fix|review|plan",
        re.IGNORECASE,
    )
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                continue
            thread_name = str(data.get("thread_name", "")).strip()
            if not thread_name or not keywords.search(thread_name):
                continue
            session_id = str(data.get("id", "")).strip()
            tasks.append(
                WorkspaceTask(
                    id=make_task_id("codex", thread_name),
                    title=f"Review Codex session: {thread_name}",
                    repo="codex",
                    lane="Codex session index",
                    status="inbox",
                    priority="P3",
                    next_action="review source pointers before promoting into DTP task ledger",
                    blocked_by="",
                    attention_reason="session-index recovery candidate",
                    source_refs=(f"codex-session:{session_id}",),
                    evidence_refs=(),
                    sensitivity="internal-only",
                    confidence="low",
                    last_seen_at=str(data.get("updated_at", ""))[:10] or today,
                )
            )
    return tuple(tasks)


def _tasks_from_memory_registry(today: str) -> tuple[WorkspaceTask, ...]:
    path = Path.home() / ".codex" / "memories" / "MEMORY.md"
    if not path.exists():
        return ()
    tasks: list[WorkspaceTask] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("# Task Group:"):
            continue
        title = line.removeprefix("# Task Group:").strip()
        if not title:
            continue
        tasks.append(
            WorkspaceTask(
                id=make_task_id("memory", title),
                title=f"Memory pointer: {title}",
                repo="memory",
                lane="Codex saved memory",
                status="parked",
                priority="P3",
                next_action="verify against live DTP/repo source before promoting",
                blocked_by="",
                attention_reason="memory registry pointer",
                source_refs=(f"MEMORY.md:{line_number}",),
                evidence_refs=(),
                sensitivity="internal-only",
                confidence="memory-pointer",
                last_seen_at=today,
            )
        )
    return tuple(tasks)


def _read_approved_tasks(path: Path) -> tuple[WorkspaceTask, ...]:
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data.get("candidates", data) if isinstance(data, dict) else data
    if not isinstance(rows, list):
        raise ValueError("approved workspace recovery file must contain a candidate list")
    return tuple(WorkspaceTask.from_dict(row) for row in rows)


def _write_recovery_json(config: DtpConfig, candidates: tuple[WorkspaceTask, ...]) -> Path:
    path = config.outputs_dir / DEFAULT_RECOVERY_JSON
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(UTC).isoformat(timespec="seconds"),
        "candidate_count": len(candidates),
        "candidates": [task.to_dict() for task in candidates],
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    return path


def _write_recovery_markdown(config: DtpConfig, candidates: tuple[WorkspaceTask, ...]) -> Path:
    path = config.outputs_dir / DEFAULT_RECOVERY_MD
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Workspace Recovery Candidates",
        "",
        f"Generated: {datetime.now(UTC).isoformat(timespec='seconds')}",
        "",
        "| Title | Repo | Status | Priority | Confidence | Next Action | Source |",
        "|---|---|---|---|---|---|---|",
    ]
    for task in candidates:
        lines.append(
            "| "
            + " | ".join(
                _md_cell(value)
                for value in (
                    task.title,
                    task.repo,
                    task.status,
                    task.priority,
                    task.confidence,
                    task.next_action,
                    "; ".join(task.source_refs[:3]),
                )
            )
            + " |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return path


def _notion_row(task: WorkspaceTask) -> dict[str, str]:
    return {
        "name": _safe_mirror_title(task),
        "repo": task.repo,
        "status": task.status,
        "next_action": task.next_action,
        "dtp_link": task.source_refs[0] if task.source_refs else "",
        "blocker_class": _blocker_class(task),
        "priority": task.priority,
        "last_verified": task.last_seen_at,
    }


def _is_notion_safe(task: WorkspaceTask) -> bool:
    return task.sensitivity not in PRIVATE_TASK_SENSITIVITIES or task.title.startswith("[redacted")


def _safe_mirror_title(task: WorkspaceTask) -> str:
    if task.sensitivity in PRIVATE_TASK_SENSITIVITIES and not task.title.startswith("[redacted"):
        return "[redacted private workspace task]"
    return task.title


def _blocker_class(task: WorkspaceTask) -> str:
    text = f"{task.status} {task.blocked_by} {task.attention_reason}".lower()
    if "proof" in text:
        return "proof"
    if "owner" in text or "toni" in text or "human" in text:
        return "human"
    if "coi" in text:
        return "coi"
    if "private" in text:
        return "privacy"
    if task.status == "blocked":
        return "repo_or_process"
    return ""


def _merge_task(left: WorkspaceTask, right: WorkspaceTask) -> WorkspaceTask:
    primary = _choose_primary(left, right)
    secondary = right if primary is left else left
    status = _choose_status(primary.status, secondary.status)
    return WorkspaceTask(
        id=primary.id,
        title=primary.title,
        repo=primary.repo,
        lane=primary.lane or secondary.lane,
        status=status,
        priority=_choose_priority(primary.priority, secondary.priority),
        next_action=primary.next_action or secondary.next_action,
        blocked_by=primary.blocked_by or secondary.blocked_by,
        attention_reason=primary.attention_reason or secondary.attention_reason,
        source_refs=_unique_refs((*primary.source_refs, *secondary.source_refs)),
        evidence_refs=_unique_refs((*primary.evidence_refs, *secondary.evidence_refs)),
        sensitivity=_choose_sensitivity(primary.sensitivity, secondary.sensitivity),
        confidence=_choose_confidence(primary.confidence, secondary.confidence),
        last_seen_at=max(primary.last_seen_at, secondary.last_seen_at),
        closed_at=primary.closed_at or secondary.closed_at,
        closure_reason=primary.closure_reason or secondary.closure_reason,
        superseded_by=primary.superseded_by or secondary.superseded_by,
    )


def _choose_primary(left: WorkspaceTask, right: WorkspaceTask) -> WorkspaceTask:
    left_score = _confidence_rank(left.confidence) + _status_rank(left.status)
    right_score = _confidence_rank(right.confidence) + _status_rank(right.status)
    return left if left_score >= right_score else right


def _choose_status(left: str, right: str) -> str:
    return left if _status_rank(left) >= _status_rank(right) else right


def _choose_priority(left: str, right: str) -> str:
    ranks = {"P0": 4, "P1": 3, "P2": 2, "P3": 1}
    return left if ranks.get(left.upper(), 0) >= ranks.get(right.upper(), 0) else right


def _choose_confidence(left: str, right: str) -> str:
    return left if _confidence_rank(left) >= _confidence_rank(right) else right


def _choose_sensitivity(left: str, right: str) -> str:
    ranks = {"coi-gated": 4, "private-client": 3, "financial": 3, "internal-only": 2}
    return left if ranks.get(left, 1) >= ranks.get(right, 1) else right


def _status_rank(status: str) -> int:
    ranks = {
        "now": 80,
        "decision_needed": 75,
        "blocked": 70,
        "waiting": 65,
        "next": 55,
        "inbox": 45,
        "parked": 35,
        "done": 25,
        "superseded": 20,
        "cancelled": 15,
        "discarded": 10,
    }
    return ranks.get(status, 0)


def _confidence_rank(confidence: str) -> int:
    ranks = {"high": 30, "medium": 20, "memory-pointer": 10, "low": 5}
    return ranks.get(confidence, 0)


def _task_sort_key(task: WorkspaceTask) -> tuple[int, str, str]:
    return (-_status_rank(task.status), task.repo.lower(), task.title.lower())


def _task_key(task: WorkspaceTask) -> str:
    return f"{_slug(task.repo)}::{_slug(task.title)}"


def _priority_for_status(status: str) -> str:
    if status in {"now", "blocked", "decision_needed"}:
        return "P1"
    if status in {"next", "waiting"}:
        return "P2"
    return "P3"


def _attention_reason(status: str, lane: str, next_action: str) -> str:
    text = f"{lane} {next_action}".lower()
    if status == "now":
        return "active now"
    if status == "waiting":
        return "waiting on human/input"
    if status == "blocked":
        return "blocked by gate"
    if status == "decision_needed":
        return "decision needed"
    if "proof" in text and status in {"next", "parked"}:
        return "proof review candidate"
    return ""


def _status_from_proof_status(raw_status: str) -> str:
    text = raw_status.lower()
    if "parked" in text:
        return "parked"
    if "review" in text:
        return "decision_needed"
    if any(word in text for word in ("need", "restricted", "blocked", "permission")):
        return "blocked"
    return "now"


def _status_from_board_section(section: str) -> str:
    text = section.lower()
    if "done" in text:
        return "done"
    if "ready" in text:
        return "next"
    if "blocked" in text:
        return "blocked"
    if "waiting" in text:
        return "waiting"
    if "parked" in text or "backlog" in text:
        return "parked"
    return "inbox"


def _sensitivity_for_repo(value: str) -> str:
    text = value.lower()
    if "dse" in text:
        return "coi-gated"
    if "engagement" in text or "ccaap" in text or "client" in text:
        return "private-client"
    return "internal-only"


def _repo_from_lane(lane: str) -> str:
    first = lane.split(",", 1)[0].strip()
    return first or "diagnose-to-plan"


def _workspace_repo_paths(config: DtpConfig) -> dict[str, Path]:
    if not config.workspace_file.exists():
        return {}
    repos: dict[str, Path] = {}
    name = ""
    for line in config.workspace_file.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("- name:"):
            name = stripped.split(":", 1)[1].strip()
            continue
        if stripped.startswith("path:") and name:
            raw_path = stripped.split(":", 1)[1].strip()
            repos[name] = (config.workspace_file.parent / raw_path).resolve()
            name = ""
    return repos


def _resolve_path(repo_root: Path, path: Path) -> Path:
    return path if path.is_absolute() else (repo_root / path).resolve()


def _clean_cell(value: str) -> str:
    return value.replace("`", "").replace("<br>", " ").strip()


def _is_markdown_rule(cells: list[str]) -> bool:
    return all(cell.replace("-", "").replace(":", "").strip() == "" for cell in cells)


def _unique_refs(refs: tuple[str, ...]) -> tuple[str, ...]:
    seen: set[str] = set()
    values: list[str] = []
    for ref in refs:
        cleaned = str(ref).strip()
        if not cleaned or cleaned in seen:
            continue
        seen.add(cleaned)
        values.append(cleaned)
    return tuple(values)


def _split_source_refs(value: str) -> tuple[str, ...]:
    return tuple(part.strip() for part in value.split(";") if part.strip())


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def _md_cell(value: str) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ").strip()
