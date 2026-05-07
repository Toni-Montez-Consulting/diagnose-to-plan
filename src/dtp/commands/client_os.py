from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, date, datetime
from pathlib import Path

from dtp.capture import render_markdown_with_frontmatter, slugify
from dtp.config import DtpConfig
from dtp.git_safety import resolve_inside_repo


class ClientOsError(ValueError):
    pass


@dataclass(frozen=True)
class ClientOsCheck:
    severity: str
    message: str


@dataclass(frozen=True)
class ClientOsPreflightResult:
    client_id: str
    engagement_id: str
    meeting_date: date
    root: Path
    pilot_packet: Path
    meeting_notes: Path
    post_meeting_receipt: Path
    checks: tuple[ClientOsCheck, ...]

    @property
    def ok(self) -> bool:
        return not any(check.severity == "blocker" for check in self.checks)


@dataclass(frozen=True)
class ClientOsScaffoldResult:
    client_id: str
    engagement_id: str
    meeting_date: date
    created: tuple[Path, ...]
    overwritten: tuple[Path, ...]


REQUIRED_PACKET_SECTIONS = (
    "Source Index",
    "Meeting Intent",
    "Permission And Privacy Notes",
    "Draft-Only Automation",
    "Open Loops",
    "Next-Action Packet",
)


def run_client_os_preflight(
    *,
    config: DtpConfig,
    client: str,
    engagement: str,
    meeting_date: str,
) -> ClientOsPreflightResult:
    parsed_date = _parse_date(meeting_date)
    client_id = slugify(client)
    engagement_id = slugify(engagement)
    root = _engagement_root(config, client_id, engagement_id)
    pilot_packet = root / f"client-os-pilot-{parsed_date.isoformat()}.md"
    meeting_notes = root / f"meeting-notes-{parsed_date.isoformat()}.md"
    post_meeting_receipt = root / f"post-meeting-receipt-{parsed_date.isoformat()}.md"

    checks: list[ClientOsCheck] = []
    if root.exists() and root.is_dir():
        checks.append(_ok(f"engagement root exists: {_display(config, root)}"))
    else:
        checks.append(_blocker(f"engagement root missing: {_display(config, root)}"))

    packet_text = ""
    if pilot_packet.exists() and pilot_packet.is_file():
        checks.append(_ok(f"pilot packet exists: {_display(config, pilot_packet)}"))
        packet_text = pilot_packet.read_text(encoding="utf-8")
        checks.extend(_packet_checks(packet_text))
    else:
        checks.append(_blocker(f"pilot packet missing: {_display(config, pilot_packet)}"))

    if meeting_notes.exists():
        checks.append(_ok(f"meeting notes scaffold exists: {_display(config, meeting_notes)}"))
    else:
        checks.append(
            _warning(f"meeting notes scaffold missing: {_display(config, meeting_notes)}")
        )

    if post_meeting_receipt.exists():
        checks.append(
            _ok(f"post-meeting receipt scaffold exists: {_display(config, post_meeting_receipt)}")
        )
    else:
        checks.append(
            _warning(
                "post-meeting receipt scaffold missing: "
                f"{_display(config, post_meeting_receipt)}"
            )
        )

    checks.append(_permission_check(config=config, root=root, packet_text=packet_text))

    return ClientOsPreflightResult(
        client_id=client_id,
        engagement_id=engagement_id,
        meeting_date=parsed_date,
        root=root,
        pilot_packet=pilot_packet,
        meeting_notes=meeting_notes,
        post_meeting_receipt=post_meeting_receipt,
        checks=tuple(checks),
    )


def run_client_os_scaffold(
    *,
    config: DtpConfig,
    client: str,
    engagement: str,
    meeting_date: str,
    force: bool = False,
) -> ClientOsScaffoldResult:
    parsed_date = _parse_date(meeting_date)
    client_id = slugify(client)
    engagement_id = slugify(engagement)
    root = _engagement_root(config, client_id, engagement_id)
    if not root.exists() or not root.is_dir():
        raise ClientOsError(f"engagement root missing: {_display(config, root)}")

    targets = {
        root / f"meeting-notes-{parsed_date.isoformat()}.md": _meeting_notes(
            client_id, engagement_id, parsed_date
        ),
        root / f"post-meeting-receipt-{parsed_date.isoformat()}.md": _post_meeting_receipt(
            client_id, engagement_id, parsed_date
        ),
    }

    existing = tuple(path for path in targets if path.exists())
    if existing and not force:
        files = ", ".join(_display(config, path) for path in existing)
        raise ClientOsError(f"refusing to overwrite existing scaffold: {files}")

    created: list[Path] = []
    overwritten: list[Path] = []
    for path, body in targets.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        metadata = _private_metadata(client_id, engagement_id, parsed_date)
        rendered = render_markdown_with_frontmatter(metadata, body)
        if path.exists():
            overwritten.append(path)
        else:
            created.append(path)
        path.write_text(rendered, encoding="utf-8")

    return ClientOsScaffoldResult(
        client_id=client_id,
        engagement_id=engagement_id,
        meeting_date=parsed_date,
        created=tuple(created),
        overwritten=tuple(overwritten),
    )


def render_preflight(result: ClientOsPreflightResult, repo_root: Path) -> str:
    state = "ok" if result.ok else "needs work"
    lines = [
        f"client-os preflight: {state}",
        f"  client: {result.client_id}",
        f"  engagement: {result.engagement_id}",
        f"  date: {result.meeting_date.isoformat()}",
    ]
    for check in result.checks:
        lines.append(f"  {check.severity}: {check.message}")
    return "\n".join(lines) + "\n"


def render_scaffold(result: ClientOsScaffoldResult, repo_root: Path) -> str:
    lines = [
        "client-os scaffold: ok",
        f"  client: {result.client_id}",
        f"  engagement: {result.engagement_id}",
        f"  date: {result.meeting_date.isoformat()}",
    ]
    lines.extend(f"  created: {path.relative_to(repo_root).as_posix()}" for path in result.created)
    lines.extend(
        f"  overwritten: {path.relative_to(repo_root).as_posix()}" for path in result.overwritten
    )
    return "\n".join(lines) + "\n"


def _packet_checks(text: str) -> tuple[ClientOsCheck, ...]:
    checks: list[ClientOsCheck] = []
    for section in REQUIRED_PACKET_SECTIONS:
        if _has_section(text, section):
            checks.append(_ok(f"packet section present: {section}"))
        else:
            checks.append(_blocker(f"packet section missing: {section}"))

    if _source_index_has_real_rows(text):
        checks.append(_ok("source index has real rows"))
    else:
        checks.append(_blocker("source index has no real rows"))

    has_draft_authority = (
        "automation authority: draft-only" in text.lower()
        or "draft-only automation" in text.lower()
    )
    if has_draft_authority:
        checks.append(_ok("draft-only automation boundary is present"))
    else:
        checks.append(_blocker("draft-only automation boundary missing"))

    return tuple(checks)


def _permission_check(*, config: DtpConfig, root: Path, packet_text: str) -> ClientOsCheck:
    consent = root.parent / "consent.md"
    consent_text = consent.read_text(encoding="utf-8") if consent.exists() else ""
    combined = f"{packet_text}\n{consent_text}".lower()
    if not combined.strip():
        return _warning("permission state not found; keep proof blocked")

    blocked_markers = (
        "pending written confirmation",
        "not approved",
        "internal_only",
        "internal only",
        "blocked",
        "pending_greg",
        "pending confirmation",
    )
    if any(marker in combined for marker in blocked_markers):
        return _ok("public proof permission is not assumed")

    if any(marker in combined for marker in ("approved", "yes", "confirmed")):
        if "written" in combined and "reviewer" in combined:
            return _warning("permission may be approved; verify written source and reviewer")
        return _blocker("permission appears approved without written source/reviewer")

    return _warning("permission state unclear; keep public proof blocked")


def _has_section(text: str, section: str) -> bool:
    return f"## {section}".lower() in text.lower()


def _source_index_has_real_rows(text: str) -> bool:
    section = _section_body(text, "Source Index")
    if not section:
        return False
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or "---" in stripped:
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) >= 5 and cells[0].lower() != "source" and any(cells):
            return True
    return False


def _section_body(text: str, section: str) -> str:
    marker = f"## {section}"
    lower = text.lower()
    start = lower.find(marker.lower())
    if start == -1:
        return ""
    next_start = lower.find("\n## ", start + len(marker))
    if next_start == -1:
        return text[start:]
    return text[start:next_start]


def _meeting_notes(client_id: str, engagement_id: str, meeting_date: date) -> str:
    return "\n".join(
        [
            f"# Meeting Notes - {meeting_date.isoformat()}",
            "",
            "## Meeting Metadata",
            "",
            f"- Client/lane: {client_id}",
            f"- Engagement: {engagement_id}",
            f"- Date: {meeting_date.isoformat()}",
            "- Automation authority: draft_only",
            (
                "- Public proof posture: blocked until written permission, redaction, "
                "reviewer, evidence, and caveat pass"
            ),
            "",
            "## Source Index Updates",
            "",
            "| Source | Location | Freshness | Allowed use | Blocked use |",
            "|---|---|---|---|---|",
            "|  |  |  |  |  |",
            "",
            "## Confirmed Facts",
            "",
            "| Fact | Source | Confidence | Public use? |",
            "|---|---|---|---|",
            "|  |  | provisional / confirmed | no |",
            "",
            "## Decisions",
            "",
            "| Decision | Owner | Evidence | Revisit trigger |",
            "|---|---|---|---|",
            "|  |  |  |  |",
            "",
            "## Launch / Product Notes",
            "",
            "- First user segment:",
            "- Soft-launch goal:",
            "- Blockers:",
            "- Trust gaps:",
            "- Next useful artifact:",
            "",
            "## Permission And Privacy Notes",
            "",
            "- Naming permission:",
            "- Screenshot/media permission:",
            "- Metrics/admin permission:",
            "- Reviewer:",
            "- Explicitly blocked material:",
            "",
            "## Open Loops",
            "",
            "| Loop | Owner | Gate | Due/review trigger | Status |",
            "|---|---|---|---|---|",
            "|  |  |  |  | pending |",
            "",
            "## Draft Follow-Up Points",
            "",
            "-",
            "",
            "## Do Not Do",
            "",
            "- Do not send follow-up without Toni review.",
            "- Do not publish public proof.",
            "- Do not collect credentials, raw logs, user records, or private contact lists.",
            "- Do not change public consulting copy from these notes.",
            "",
        ]
    )


def _post_meeting_receipt(client_id: str, engagement_id: str, meeting_date: date) -> str:
    return "\n".join(
        [
            f"# Post-Meeting Receipt - {meeting_date.isoformat()}",
            "",
            "## Receipt Metadata",
            "",
            f"- Client/lane: {client_id}",
            f"- Engagement: {engagement_id}",
            f"- Meeting date: {meeting_date.isoformat()}",
            "- Automation authority: draft_only",
            "- Receipt status: draft",
            "",
            "## Required Updates",
            "",
            "| Artifact | Updated? | Notes |",
            "|---|---|---|",
            f"| meeting-notes-{meeting_date.isoformat()}.md | pending |  |",
            "| action-extraction.md | pending |  |",
            "| owner-action-items.md | pending |  |",
            "| source-material-index.md | pending |  |",
            "| consent.md | pending / not_applicable |  |",
            "| diagnose.md | pending |  |",
            "| plan.md | pending |  |",
            "| decision-log.md | pending |  |",
            "| proof/* | pending / blocked |  |",
            "",
            "## Decisions Captured",
            "",
            "| Decision | Owner | Evidence | Revisit trigger |",
            "|---|---|---|---|",
            "|  |  |  |  |",
            "",
            "## Open Loops",
            "",
            "| Loop | Owner | Gate | Due/review trigger | Status |",
            "|---|---|---|---|---|",
            "|  |  |  |  | pending |",
            "",
            "## Next-Action Packet",
            "",
            "- Toni next action:",
            "- Client/operator next action:",
            "- Agent next draft:",
            "- Next review:",
            "",
            "## Proof Gate",
            "",
            "- Public naming: blocked / pending / approved",
            "- Screenshots/media: blocked / pending / approved",
            "- Metrics/admin detail: blocked / pending / approved",
            "- Reviewer:",
            "- Evidence source:",
            "- Caveat:",
            "- Publish decision: blocked until every gate passes",
            "",
            "## Handoff",
            "",
            "- Current state:",
            "- Blockers:",
            "- Parked ideas:",
            "- Do not touch:",
            "- Sanitized Notion mirror needed:",
            "",
        ]
    )


def _private_metadata(client_id: str, engagement_id: str, meeting_date: date) -> dict[str, object]:
    return {
        "created": _timestamp(),
        "client_id": client_id,
        "engagement_id": engagement_id,
        "kit_kind": "client-os-pilot",
        "meeting_date": meeting_date.isoformat(),
        "data_class": "P2",
        "confidential": True,
        "permission_level": "internal_only",
        "review_status": "draft",
    }


def _engagement_root(config: DtpConfig, client_id: str, engagement_id: str) -> Path:
    return resolve_inside_repo(config.engagements_dir / client_id / engagement_id, config.repo_root)


def _parse_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ClientOsError(f"invalid date, expected YYYY-MM-DD: {value}") from exc


def _timestamp() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def _display(config: DtpConfig, path: Path) -> str:
    return path.relative_to(config.repo_root).as_posix()


def _ok(message: str) -> ClientOsCheck:
    return ClientOsCheck("ok", message)


def _warning(message: str) -> ClientOsCheck:
    return ClientOsCheck("warning", message)


def _blocker(message: str) -> ClientOsCheck:
    return ClientOsCheck("blocker", message)
