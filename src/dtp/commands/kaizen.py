from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Iterator
from dataclasses import dataclass, replace
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from dtp.config import DtpConfig

KAIZEN_DIR_NAME = "kaizen"
KAIZEN_INDEX_NAME = "intake.jsonl"
PRIVATE_INDEX_NAME = "private-intake.jsonl"
DEFAULT_STATUS_LIMIT = 5
DEFAULT_MIRROR_LIMIT = 100

ITEM_TYPES = (
    "ask",
    "blocker",
    "client_reply",
    "correction",
    "decision",
    "engagement",
    "feature",
    "idea",
    "process",
    "proof",
    "repo_issue",
    "research",
    "tooling",
)
STATUSES = ("inbox", "now", "next", "waiting", "blocked", "parked", "done")
ACTIVE_STATUSES = ("now", "next", "inbox", "waiting", "blocked", "parked")
SENSITIVITIES = ("auto", "public-safe", "internal-only", "private-client", "coi-gated")
PRIVATE_SENSITIVITIES = {"private-client", "coi-gated"}
MIRRORABLE_SENSITIVITIES = {"public-safe", "internal-only"}

BLOCKED_MIRROR_MARKERS = (
    "api key",
    "bank",
    "client private",
    "confidential",
    "ein",
    "invoice",
    "password",
    "payment",
    "private client",
    "raw transcript",
    "secret",
    "ssn",
    "token",
)
COI_MARKERS = ("coi", "dse", "microsoft confidential")
PRIVATE_MARKERS = (
    "cameron",
    "ccaap",
    "client reply",
    "engagement",
    "greg",
    "mom nonprofit",
    "owner input",
    "private kit",
)


class KaizenError(ValueError):
    """User-facing Kaizen command error."""


@dataclass(frozen=True)
class KaizenRecord:
    id: str
    captured_at: str
    title: str
    text: str
    item_type: str
    status: str
    sensitivity: str
    repo: str
    source: str
    dtp_source_path: str
    notion_target: str
    next_action: str
    tags: tuple[str, ...]
    raw_ref: str = ""

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] = {
            "id": self.id,
            "captured_at": self.captured_at,
            "title": self.title,
            "text": self.text,
            "item_type": self.item_type,
            "status": self.status,
            "sensitivity": self.sensitivity,
            "repo": self.repo,
            "source": self.source,
            "dtp_source_path": self.dtp_source_path,
            "notion_target": self.notion_target,
            "next_action": self.next_action,
            "tags": list(self.tags),
        }
        if self.raw_ref:
            data["raw_ref"] = self.raw_ref
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> KaizenRecord:
        return cls(
            id=str(data["id"]),
            captured_at=str(data["captured_at"]),
            title=str(data["title"]),
            text=str(data["text"]),
            item_type=str(data["item_type"]),
            status=str(data["status"]),
            sensitivity=str(data["sensitivity"]),
            repo=str(data["repo"]),
            source=str(data["source"]),
            dtp_source_path=str(data["dtp_source_path"]),
            notion_target=str(data["notion_target"]),
            next_action=str(data["next_action"]),
            tags=tuple(str(tag) for tag in data.get("tags", ())),
            raw_ref=str(data.get("raw_ref", "")),
        )


@dataclass(frozen=True)
class CaptureResult:
    record: KaizenRecord
    index_path: Path
    private_index_path: Path | None = None


@dataclass(frozen=True)
class UpdateResult:
    record: KaizenRecord
    index_path: Path
    private_index_path: Path | None = None


@dataclass(frozen=True)
class KaizenStatus:
    records: tuple[KaizenRecord, ...]
    counts: dict[str, int]
    status_filter: str | None
    limit: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "counts": self.counts,
            "status_filter": self.status_filter,
            "limit": self.limit,
            "records": [record.to_dict() for record in self.records],
        }


@dataclass(frozen=True)
class MirrorResult:
    mode: str
    generated_at: str
    allowed_rows: tuple[dict[str, Any], ...]
    blocked_rows: tuple[dict[str, Any], ...]
    skipped_done: int
    limit: int
    sync_state_path: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "mode": self.mode,
            "generated_at": self.generated_at,
            "allowed_rows": list(self.allowed_rows),
            "blocked_rows": list(self.blocked_rows),
            "skipped_done": self.skipped_done,
            "limit": self.limit,
            "sync_state_path": self.sync_state_path,
        }


def run_kaizen_capture(
    config: DtpConfig,
    text: str,
    *,
    item_type: str = "auto",
    status: str = "inbox",
    sensitivity: str = "auto",
    repo: str = "diagnose-to-plan",
    source: str = "codex",
    dtp_source_path: str = "practice-os/kaizen/intake.jsonl",
    notion_target: str = "auto",
    next_action: str = "steward triage",
    tags: tuple[str, ...] = (),
    captured_at: datetime | None = None,
) -> CaptureResult:
    cleaned = _clean_text(text)
    if not cleaned:
        raise KaizenError("kaizen capture requires non-empty text")

    captured = captured_at or datetime.now(UTC)
    normalized_type = normalize_item_type(item_type, cleaned)
    normalized_status = normalize_status(status)
    normalized_sensitivity = enforce_sensitive_storage(
        normalize_sensitivity(sensitivity, cleaned),
        cleaned,
    )
    record_id = _build_id(cleaned, captured)
    raw_ref = _raw_ref(record_id) if _must_store_private(normalized_sensitivity, cleaned) else ""
    record = KaizenRecord(
        id=record_id,
        captured_at=captured.isoformat(timespec="seconds"),
        title=_stored_title(cleaned, normalized_type, normalized_sensitivity),
        text=_stored_text(cleaned, normalized_sensitivity),
        item_type=normalized_type,
        status=normalized_status,
        sensitivity=normalized_sensitivity,
        repo=repo.strip() or "diagnose-to-plan",
        source=source.strip() or "codex",
        dtp_source_path=dtp_source_path.strip() or "practice-os/kaizen/intake.jsonl",
        notion_target=normalize_notion_target(notion_target, normalized_type, normalized_status),
        next_action=next_action.strip() or "steward triage",
        tags=tuple(tag.strip() for tag in tags if tag.strip()),
        raw_ref=raw_ref,
    )

    index_path = kaizen_index_path(config)
    _append_jsonl(index_path, record.to_dict())
    private_path = _write_private_capture(config, record, cleaned) if raw_ref else None
    return CaptureResult(record=record, index_path=index_path, private_index_path=private_path)


def run_kaizen_update(
    config: DtpConfig,
    record_id: str,
    *,
    item_type: str | None = None,
    status: str | None = None,
    sensitivity: str | None = None,
    repo: str | None = None,
    source: str | None = None,
    dtp_source_path: str | None = None,
    notion_target: str | None = None,
    next_action: str | None = None,
    tags: tuple[str, ...] | None = None,
) -> UpdateResult:
    cleaned_id = record_id.strip()
    if not cleaned_id:
        raise KaizenError("kaizen update requires a record ID")

    index_path = kaizen_index_path(config)
    records = list(iter_kaizen_records(config))
    private_path: Path | None = None
    updated: KaizenRecord | None = None
    rewritten: list[KaizenRecord] = []
    for record in records:
        if record.id != cleaned_id:
            rewritten.append(record)
            continue

        new_type = normalize_item_type(item_type, record.text) if item_type else record.item_type
        new_status = normalize_status(status) if status else record.status
        new_sensitivity = (
            enforce_sensitive_storage(normalize_sensitivity(sensitivity, record.text), record.text)
            if sensitivity
            else enforce_sensitive_storage(record.sensitivity, record.text)
        )
        raw_ref = record.raw_ref
        if _must_store_private(new_sensitivity, record.text) and not raw_ref:
            raw_ref = _raw_ref(record.id)
            private_path = _write_private_capture(config, record, record.text)

        new_record = replace(
            record,
            item_type=new_type,
            status=new_status,
            sensitivity=new_sensitivity,
            repo=_optional_text(repo, record.repo),
            source=_optional_text(source, record.source),
            dtp_source_path=_optional_text(dtp_source_path, record.dtp_source_path),
            notion_target=normalize_notion_target(
                notion_target or "auto",
                new_type,
                new_status,
            )
            if notion_target or item_type or status
            else record.notion_target,
            next_action=_optional_text(next_action, record.next_action),
            tags=(
                tuple(tag.strip() for tag in tags if tag.strip())
                if tags is not None
                else record.tags
            ),
            title=_stored_title(record.text, new_type, new_sensitivity),
            text=_stored_text(record.text, new_sensitivity),
            raw_ref=raw_ref,
        )
        updated = new_record
        rewritten.append(new_record)

    if updated is None:
        raise KaizenError(f"unknown kaizen record: {record_id}")

    _write_index(index_path, rewritten)
    return UpdateResult(record=updated, index_path=index_path, private_index_path=private_path)


def run_kaizen_status(
    config: DtpConfig,
    *,
    status_filter: str | None = None,
    limit: int = DEFAULT_STATUS_LIMIT,
) -> KaizenStatus:
    normalized_filter = normalize_status(status_filter) if status_filter else None
    normalized_limit = _normalize_limit(limit)
    counts = {status: 0 for status in STATUSES}
    counts["total"] = 0
    selected: list[KaizenRecord] = []

    for record in iter_kaizen_records(config):
        counts["total"] += 1
        counts[record.status] = counts.get(record.status, 0) + 1
        if normalized_filter and record.status != normalized_filter:
            continue
        if not normalized_filter and record.status not in ACTIVE_STATUSES:
            continue
        selected.append(record)

    if normalized_filter:
        selected = selected[-normalized_limit:]
    else:
        selected = _limit_per_status(selected, normalized_limit)
    return KaizenStatus(
        records=tuple(selected),
        counts=counts,
        status_filter=normalized_filter,
        limit=normalized_limit,
    )


def run_kaizen_mirror(
    config: DtpConfig,
    *,
    apply: bool = False,
    include_done: bool = False,
    limit: int = DEFAULT_MIRROR_LIMIT,
) -> MirrorResult:
    if apply:
        raise KaizenError(
            "live Notion apply is gated: review --dry-run output, confirm Notion auth, "
            "then record a steward receipt before enabling writes"
        )

    normalized_limit = _normalize_limit(limit)
    allowed: list[dict[str, Any]] = []
    blocked: list[dict[str, Any]] = []
    skipped_done = 0
    for record in iter_kaizen_records(config):
        if record.status == "done" and not include_done:
            skipped_done += 1
            continue
        if len(allowed) + len(blocked) >= normalized_limit:
            break
        reason = mirror_blocker(record)
        if reason:
            blocked.append(
                {
                    "source_id": record.id,
                    "title": record.title,
                    "status": record.status,
                    "sensitivity": record.sensitivity,
                    "blocked_reason": reason,
                    "dtp_source_path": record.dtp_source_path,
                }
            )
            continue
        allowed.append(_mirror_row(record))

    return MirrorResult(
        mode="dry-run",
        generated_at=datetime.now(UTC).isoformat(timespec="seconds"),
        allowed_rows=tuple(allowed),
        blocked_rows=tuple(blocked),
        skipped_done=skipped_done,
        limit=normalized_limit,
        sync_state_path=".dtp/kaizen/notion-sync-state.json",
    )


def iter_kaizen_records(config: DtpConfig) -> Iterator[KaizenRecord]:
    index_path = kaizen_index_path(config)
    if not index_path.exists():
        return
    with index_path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                data = json.loads(line)
                yield KaizenRecord.from_dict(data)
            except (KeyError, TypeError, json.JSONDecodeError) as error:
                raise KaizenError(
                    f"invalid kaizen record at {index_path.as_posix()}:{line_number}"
                ) from error


def read_kaizen_records(config: DtpConfig) -> tuple[KaizenRecord, ...]:
    return tuple(iter_kaizen_records(config))


def render_capture(result: CaptureResult, repo_root: Path) -> str:
    lines = _render_record_action("kaizen captured", result.record, result.index_path, repo_root)
    if result.private_index_path:
        private_path = result.private_index_path.relative_to(repo_root).as_posix()
        lines.append(f"  private raw: {private_path}")
    return "\n".join(lines) + "\n"


def render_update(result: UpdateResult, repo_root: Path) -> str:
    lines = _render_record_action("kaizen updated", result.record, result.index_path, repo_root)
    if result.private_index_path:
        private_path = result.private_index_path.relative_to(repo_root).as_posix()
        lines.append(f"  private raw: {private_path}")
    return "\n".join(lines) + "\n"


def render_status(status: KaizenStatus) -> str:
    lines = [
        "Kaizen Kanban Status",
        (
            "Counts: "
            f"inbox={status.counts.get('inbox', 0)}, "
            f"now={status.counts.get('now', 0)}, "
            f"next={status.counts.get('next', 0)}, "
            f"waiting={status.counts.get('waiting', 0)}, "
            f"blocked={status.counts.get('blocked', 0)}, "
            f"parked={status.counts.get('parked', 0)}, "
            f"done={status.counts.get('done', 0)}, "
            f"total={status.counts.get('total', 0)}"
        ),
        f"Limit: {status.limit}",
    ]
    statuses = (status.status_filter,) if status.status_filter else ACTIVE_STATUSES
    for record_status in statuses:
        records = [record for record in status.records if record.status == record_status]
        lines.append("")
        lines.append(_status_label(record_status))
        if not records:
            lines.append("- none")
            continue
        for record in records[-status.limit :]:
            lines.append(
                f"- {record.id}: {record.title} "
                f"({record.item_type}, {record.repo}) -> {record.next_action}"
            )
    return "\n".join(lines) + "\n"


def render_mirror(result: MirrorResult) -> str:
    return json.dumps(result.to_dict(), indent=2, sort_keys=True) + "\n"


def normalize_item_type(item_type: str, text: str) -> str:
    normalized = item_type.strip().lower().replace("-", "_")
    if normalized == "auto":
        return classify_text(text)
    if normalized not in ITEM_TYPES:
        raise KaizenError(f"unknown kaizen type: {item_type}")
    return normalized


def normalize_sensitivity(sensitivity: str, text: str) -> str:
    normalized = sensitivity.strip().lower().replace("_", "-")
    if normalized not in SENSITIVITIES:
        raise KaizenError(f"unknown kaizen sensitivity: {sensitivity}")
    if normalized != "auto":
        return normalized

    lowered = text.lower()
    if any(marker in lowered for marker in COI_MARKERS):
        return "coi-gated"
    if any(marker in lowered for marker in (*PRIVATE_MARKERS, *BLOCKED_MIRROR_MARKERS)):
        return "private-client"
    return "internal-only"


def enforce_sensitive_storage(sensitivity: str, text: str) -> str:
    lowered = text.lower()
    if any(marker in lowered for marker in COI_MARKERS):
        return "coi-gated"
    if any(marker in lowered for marker in (*PRIVATE_MARKERS, *BLOCKED_MIRROR_MARKERS)):
        return "private-client"
    return sensitivity


def normalize_status(status: str) -> str:
    normalized = status.strip().lower().replace("-", "_")
    if normalized not in STATUSES:
        raise KaizenError(f"unknown kaizen status: {status}")
    return normalized


def normalize_notion_target(notion_target: str, item_type: str, status: str) -> str:
    target = notion_target.strip()
    if target and target.lower() != "auto":
        return target
    if status == "now":
        return "Today"
    if item_type == "proof":
        return "Proof Queue"
    if item_type == "repo_issue":
        return "Repo Health"
    if item_type in {"blocker", "client_reply", "engagement"} or status in {"waiting", "blocked"}:
        return "Waiting On"
    if item_type in {"feature", "process", "ask", "correction", "decision"}:
        return "Roadmap Stories"
    return "Ideas"


def classify_text(text: str) -> str:
    lowered = text.lower()
    if any(word in lowered for word in ("blocker", "blocked", "waiting on", "stuck")):
        return "blocker"
    if any(word in lowered for word in ("proof", "case study", "testimonial", "public claim")):
        return "proof"
    if any(word in lowered for word in ("client reply", "gmail reply", "owner replied")):
        return "client_reply"
    if any(word in lowered for word in ("engagement", "cameron", "ccaap", "greg")):
        return "engagement"
    if any(word in lowered for word in ("bug", "dirty repo", "failing", "open pr", "repo issue")):
        return "repo_issue"
    if any(word in lowered for word in ("correction", "forgot", "forgetting", "wrong")):
        return "correction"
    if any(word in lowered for word in ("research", "investigate", "look up")):
        return "research"
    if any(word in lowered for word in ("tool", "plugin", "mcp", "connector")):
        return "tooling"
    if any(word in lowered for word in ("feature", "build", "implement", "add", "ship")):
        return "feature"
    if any(word in lowered for word in ("idea", "maybe", "what if", "could we")):
        return "idea"
    if any(word in lowered for word in ("process", "loop", "kanban", "kaizen", "sprint")):
        return "process"
    return "ask"


def mirror_blocker(record: KaizenRecord) -> str:
    lowered = record.text.lower()
    if record.sensitivity not in MIRRORABLE_SENSITIVITIES:
        return f"sensitivity is {record.sensitivity}"
    if record.raw_ref:
        return "raw private capture exists outside committed index"
    if any(marker in lowered for marker in (*PRIVATE_MARKERS, *BLOCKED_MIRROR_MARKERS)):
        return "text contains private/secret marker"
    if record.item_type == "proof" and record.status not in {"done", "parked"}:
        return "proof item is not reviewed for public-safe mirroring"
    return ""


def kaizen_index_path(config: DtpConfig) -> Path:
    return config.practice_os_dir / KAIZEN_DIR_NAME / KAIZEN_INDEX_NAME


def private_kaizen_index_path(config: DtpConfig) -> Path:
    return config.repo_root / ".dtp" / KAIZEN_DIR_NAME / PRIVATE_INDEX_NAME


def _render_record_action(
    action: str,
    record: KaizenRecord,
    index_path: Path,
    repo_root: Path,
) -> list[str]:
    return [
        f"{action} {record.id}",
        f"  type: {record.item_type}",
        f"  status: {record.status}",
        f"  sensitivity: {record.sensitivity}",
        f"  notion target: {record.notion_target}",
        f"  index: {index_path.relative_to(repo_root).as_posix()}",
    ]


def _append_jsonl(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(data, sort_keys=True) + "\n")


def _write_index(path: Path, records: list[KaizenRecord]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [json.dumps(record.to_dict(), sort_keys=True) for record in records]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def _write_private_capture(config: DtpConfig, record: KaizenRecord, raw_text: str) -> Path:
    private_path = private_kaizen_index_path(config)
    raw_record = record.to_dict()
    raw_record["raw_text"] = raw_text
    raw_record["text"] = raw_text
    raw_record["private_storage"] = "ignored_local_state"
    _append_jsonl(private_path, raw_record)
    return private_path


def _mirror_row(record: KaizenRecord) -> dict[str, Any]:
    return {
        "source_id": record.id,
        "notion_surface": record.notion_target,
        "name": record.title,
        "classification": record.item_type,
        "status": record.status,
        "owning_repo": record.repo,
        "sensitivity": record.sensitivity,
        "dtp_source_path": record.dtp_source_path,
        "next_action": record.next_action,
        "captured_at": record.captured_at,
        "safe_summary": _safe_summary(record.text),
    }


def _build_id(text: str, captured_at: datetime) -> str:
    date = captured_at.strftime("%Y%m%d")
    slug = _slug(_title_for(text))[:34].strip("-") or "item"
    digest = hashlib.sha1(f"{captured_at.isoformat()}:{text}".encode()).hexdigest()[:8]
    return f"kzn-{date}-{slug}-{digest}"


def _stored_title(text: str, item_type: str, sensitivity: str) -> str:
    if sensitivity in PRIVATE_SENSITIVITIES:
        return f"[redacted {sensitivity} {item_type} capture]"
    return _title_for(text)


def _stored_text(text: str, sensitivity: str) -> str:
    if sensitivity in PRIVATE_SENSITIVITIES:
        return (
            f"[redacted {sensitivity} capture; raw text stored only in ignored "
            ".dtp/kaizen/private-intake.jsonl when captured locally]"
        )
    return text


def _raw_ref(record_id: str) -> str:
    return f".dtp/kaizen/private-intake.jsonl#{record_id}"


def _must_store_private(sensitivity: str, text: str) -> bool:
    return sensitivity in PRIVATE_SENSITIVITIES or sensitivity != enforce_sensitive_storage(
        sensitivity,
        text,
    )


def _title_for(text: str) -> str:
    cleaned = _clean_text(text)
    first_sentence = re.split(r"(?<=[.!?])\s+", cleaned, maxsplit=1)[0]
    if len(first_sentence) <= 96:
        return first_sentence
    return first_sentence[:93].rstrip() + "..."


def _safe_summary(text: str) -> str:
    cleaned = _clean_text(text)
    if len(cleaned) <= 180:
        return cleaned
    return cleaned[:177].rstrip() + "..."


def _clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _optional_text(value: str | None, fallback: str) -> str:
    if value is None:
        return fallback
    return value.strip() or fallback


def _normalize_limit(limit: int) -> int:
    if limit < 1:
        raise KaizenError("kaizen limit must be at least 1")
    return limit


def _limit_per_status(records: list[KaizenRecord], limit: int) -> list[KaizenRecord]:
    limited: list[KaizenRecord] = []
    for status in ACTIVE_STATUSES:
        bucket = [record for record in records if record.status == status]
        limited.extend(bucket[-limit:])
    return limited


def _status_label(status: str) -> str:
    return status.replace("_", " ").title()


def _slug(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return re.sub(r"-+", "-", slug)
