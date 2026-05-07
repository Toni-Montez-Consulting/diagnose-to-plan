from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, date, datetime
from pathlib import Path

from dtp.capture import render_markdown_with_frontmatter, slugify
from dtp.config import DtpConfig
from dtp.git_safety import resolve_inside_repo


class ClientOsError(ValueError):
    pass


CLIENT_OS_PROFILES = ("base", "infra", "full")
BRIDGE_SURFACES = ("gmail", "calendar", "hub", "notion")
BLOCKING_BRIDGE_MARKERS = (
    "credential",
    "secret",
    "private payload",
    "private data",
    "raw transcript",
    "user record",
    "customer record",
    "admin data",
    "public proof",
    "publish",
    "external write",
)


@dataclass(frozen=True)
class ClientOsCheck:
    severity: str
    message: str


@dataclass(frozen=True)
class ClientOsArtifactSpec:
    key: str
    label: str
    filename: Callable[[date], str]
    body: Callable[[str, str, date], str]


@dataclass(frozen=True)
class ClientOsArtifactStatus:
    key: str
    label: str
    path: Path
    required: bool
    exists: bool

    def to_dict(self, repo_root: Path) -> dict[str, object]:
        return {
            "key": self.key,
            "label": self.label,
            "path": self.path.relative_to(repo_root).as_posix(),
            "required": self.required,
            "exists": self.exists,
        }


@dataclass(frozen=True)
class ClientOsPreflightResult:
    client_id: str
    engagement_id: str
    meeting_date: date
    profile: str
    root: Path
    pilot_packet: Path
    meeting_notes: Path
    post_meeting_receipt: Path
    artifacts: tuple[ClientOsArtifactStatus, ...]
    checks: tuple[ClientOsCheck, ...]

    @property
    def ok(self) -> bool:
        return not any(check.severity == "blocker" for check in self.checks)

    def to_dict(self, repo_root: Path) -> dict[str, object]:
        return {
            "client_id": self.client_id,
            "engagement_id": self.engagement_id,
            "meeting_date": self.meeting_date.isoformat(),
            "profile": self.profile,
            "ok": self.ok,
            "pilot_packet": self.pilot_packet.relative_to(repo_root).as_posix(),
            "artifacts": [artifact.to_dict(repo_root) for artifact in self.artifacts],
            "checks": [
                {"severity": check.severity, "message": check.message}
                for check in self.checks
            ],
        }


@dataclass(frozen=True)
class ClientOsScaffoldResult:
    client_id: str
    engagement_id: str
    meeting_date: date
    profile: str
    created: tuple[Path, ...]
    overwritten: tuple[Path, ...]


@dataclass(frozen=True)
class ClientOsCloseoutResult:
    client_id: str
    engagement_id: str
    meeting_date: date
    receipt: Path
    checks: tuple[ClientOsCheck, ...]

    @property
    def ok(self) -> bool:
        return not any(check.severity == "blocker" for check in self.checks)

    def to_dict(self, repo_root: Path) -> dict[str, object]:
        return {
            "client_id": self.client_id,
            "engagement_id": self.engagement_id,
            "meeting_date": self.meeting_date.isoformat(),
            "ok": self.ok,
            "receipt": self.receipt.relative_to(repo_root).as_posix(),
            "checks": [
                {"severity": check.severity, "message": check.message}
                for check in self.checks
            ],
        }


@dataclass(frozen=True)
class ClientOsStatusResult:
    client_id: str
    engagement_id: str
    meeting_date: date
    profile: str
    preflight: ClientOsPreflightResult
    closeout: ClientOsCloseoutResult

    @property
    def ok(self) -> bool:
        return self.preflight.ok

    def to_dict(self, repo_root: Path) -> dict[str, object]:
        return {
            "client_id": self.client_id,
            "engagement_id": self.engagement_id,
            "meeting_date": self.meeting_date.isoformat(),
            "profile": self.profile,
            "ready_for_meeting": self.preflight.ok,
            "post_meeting_closeout_ready": self.closeout.ok,
            "preflight": self.preflight.to_dict(repo_root),
            "closeout": self.closeout.to_dict(repo_root),
        }


@dataclass(frozen=True)
class ClientOsBridgeRow:
    surface: str
    candidate_action: str
    payload_summary: str
    reviewer: str
    permission_gate: str
    risk: str
    status: str

    def to_dict(self) -> dict[str, str]:
        return {
            "surface": self.surface,
            "candidate_action": self.candidate_action,
            "payload_summary": self.payload_summary,
            "reviewer": self.reviewer,
            "permission_gate": self.permission_gate,
            "risk": self.risk,
            "status": self.status,
        }


@dataclass(frozen=True)
class ClientOsBridgeExportResult:
    client_id: str
    engagement_id: str
    meeting_date: date
    bridge_queue: Path
    rows: tuple[ClientOsBridgeRow, ...]
    checks: tuple[ClientOsCheck, ...]

    @property
    def ok(self) -> bool:
        return not any(check.severity == "blocker" for check in self.checks)

    def to_dict(self, repo_root: Path) -> dict[str, object]:
        return {
            "client_id": self.client_id,
            "engagement_id": self.engagement_id,
            "meeting_date": self.meeting_date.isoformat(),
            "ok": self.ok,
            "mode": "dry_run",
            "bridge_queue": self.bridge_queue.relative_to(repo_root).as_posix(),
            "rows": [row.to_dict() for row in self.rows],
            "checks": [
                {"severity": check.severity, "message": check.message}
                for check in self.checks
            ],
        }


REQUIRED_PACKET_SECTIONS = (
    "Source Index",
    "Meeting Intent",
    "Permission And Privacy Notes",
    "Draft-Only Automation",
    "Open Loops",
    "Next-Action Packet",
)

BASE_ARTIFACTS = (
    ClientOsArtifactSpec(
        key="meeting_notes",
        label="meeting notes scaffold",
        filename=lambda meeting_date: f"meeting-notes-{meeting_date.isoformat()}.md",
        body=lambda client_id, engagement_id, meeting_date: _meeting_notes(
            client_id, engagement_id, meeting_date
        ),
    ),
    ClientOsArtifactSpec(
        key="post_meeting_receipt",
        label="post-meeting receipt scaffold",
        filename=lambda meeting_date: f"post-meeting-receipt-{meeting_date.isoformat()}.md",
        body=lambda client_id, engagement_id, meeting_date: _post_meeting_receipt(
            client_id, engagement_id, meeting_date
        ),
    ),
)
INFRA_ARTIFACTS = (
    ClientOsArtifactSpec(
        key="meeting_brief",
        label="meeting brief",
        filename=lambda meeting_date: f"meeting-brief-{meeting_date.isoformat()}.md",
        body=lambda client_id, engagement_id, meeting_date: _meeting_brief(
            client_id, engagement_id, meeting_date
        ),
    ),
    ClientOsArtifactSpec(
        key="chain_run",
        label="chain-run",
        filename=lambda meeting_date: f"chain-run-{meeting_date.isoformat()}.md",
        body=lambda client_id, engagement_id, meeting_date: _chain_run(
            client_id, engagement_id, meeting_date
        ),
    ),
    ClientOsArtifactSpec(
        key="build_task",
        label="build task",
        filename=lambda meeting_date: f"build-task-{meeting_date.isoformat()}.md",
        body=lambda client_id, engagement_id, meeting_date: _build_task(
            client_id, engagement_id, meeting_date
        ),
    ),
    ClientOsArtifactSpec(
        key="bridge_queue",
        label="bridge queue",
        filename=lambda meeting_date: f"bridge-queue-{meeting_date.isoformat()}.md",
        body=lambda client_id, engagement_id, meeting_date: _bridge_queue(
            client_id, engagement_id, meeting_date
        ),
    ),
)


def run_client_os_preflight(
    *,
    config: DtpConfig,
    client: str,
    engagement: str,
    meeting_date: str,
    profile: str = "base",
) -> ClientOsPreflightResult:
    parsed_date = _parse_date(meeting_date)
    profile_id = _validate_profile(profile)
    client_id = slugify(client)
    engagement_id = slugify(engagement)
    root = _engagement_root(config, client_id, engagement_id)
    pilot_packet = root / f"client-os-pilot-{parsed_date.isoformat()}.md"
    artifacts = _artifact_statuses(config, root, parsed_date, profile_id)
    meeting_notes = root / BASE_ARTIFACTS[0].filename(parsed_date)
    post_meeting_receipt = root / BASE_ARTIFACTS[1].filename(parsed_date)

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

    checks.extend(_artifact_checks(config, artifacts, profile_id))
    checks.append(_permission_check(root=root, packet_text=packet_text))

    return ClientOsPreflightResult(
        client_id=client_id,
        engagement_id=engagement_id,
        meeting_date=parsed_date,
        profile=profile_id,
        root=root,
        pilot_packet=pilot_packet,
        meeting_notes=meeting_notes,
        post_meeting_receipt=post_meeting_receipt,
        artifacts=artifacts,
        checks=tuple(checks),
    )


def run_client_os_scaffold(
    *,
    config: DtpConfig,
    client: str,
    engagement: str,
    meeting_date: str,
    force: bool = False,
    profile: str = "base",
) -> ClientOsScaffoldResult:
    parsed_date = _parse_date(meeting_date)
    profile_id = _validate_profile(profile)
    client_id = slugify(client)
    engagement_id = slugify(engagement)
    root = _engagement_root(config, client_id, engagement_id)
    if not root.exists() or not root.is_dir():
        raise ClientOsError(f"engagement root missing: {_display(config, root)}")

    targets = {
        root / spec.filename(parsed_date): spec.body(client_id, engagement_id, parsed_date)
        for spec in _artifact_specs(profile_id)
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
        profile=profile_id,
        created=tuple(created),
        overwritten=tuple(overwritten),
    )


def run_client_os_status(
    *,
    config: DtpConfig,
    client: str,
    engagement: str,
    meeting_date: str,
    profile: str = "full",
) -> ClientOsStatusResult:
    preflight = run_client_os_preflight(
        config=config,
        client=client,
        engagement=engagement,
        meeting_date=meeting_date,
        profile=profile,
    )
    closeout = run_client_os_closeout(
        config=config,
        client=client,
        engagement=engagement,
        meeting_date=meeting_date,
    )
    return ClientOsStatusResult(
        client_id=preflight.client_id,
        engagement_id=preflight.engagement_id,
        meeting_date=preflight.meeting_date,
        profile=preflight.profile,
        preflight=preflight,
        closeout=closeout,
    )


def run_client_os_closeout(
    *,
    config: DtpConfig,
    client: str,
    engagement: str,
    meeting_date: str,
) -> ClientOsCloseoutResult:
    parsed_date = _parse_date(meeting_date)
    client_id = slugify(client)
    engagement_id = slugify(engagement)
    root = _engagement_root(config, client_id, engagement_id)
    receipt = root / f"post-meeting-receipt-{parsed_date.isoformat()}.md"
    checks = _closeout_checks(config, receipt)
    return ClientOsCloseoutResult(
        client_id=client_id,
        engagement_id=engagement_id,
        meeting_date=parsed_date,
        receipt=receipt,
        checks=checks,
    )


def run_client_os_bridge_export(
    *,
    config: DtpConfig,
    client: str,
    engagement: str,
    meeting_date: str,
) -> ClientOsBridgeExportResult:
    parsed_date = _parse_date(meeting_date)
    client_id = slugify(client)
    engagement_id = slugify(engagement)
    root = _engagement_root(config, client_id, engagement_id)
    bridge_queue = root / f"bridge-queue-{parsed_date.isoformat()}.md"
    checks: list[ClientOsCheck] = []
    rows: tuple[ClientOsBridgeRow, ...] = ()

    if not bridge_queue.exists():
        checks.append(_blocker(f"bridge queue missing: {_display(config, bridge_queue)}"))
    else:
        text = bridge_queue.read_text(encoding="utf-8")
        rows = _bridge_rows(text)
        if rows:
            checks.append(_ok(f"bridge queue rows found: {len(rows)}"))
        else:
            checks.append(_blocker("bridge queue has no action rows"))
        checks.extend(_bridge_checks(rows))

    return ClientOsBridgeExportResult(
        client_id=client_id,
        engagement_id=engagement_id,
        meeting_date=parsed_date,
        bridge_queue=bridge_queue,
        rows=rows,
        checks=tuple(checks),
    )


def render_preflight(result: ClientOsPreflightResult, repo_root: Path) -> str:
    state = "ok" if result.ok else "needs work"
    lines = [
        f"client-os preflight: {state}",
        f"  client: {result.client_id}",
        f"  engagement: {result.engagement_id}",
        f"  date: {result.meeting_date.isoformat()}",
        f"  profile: {result.profile}",
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
        f"  profile: {result.profile}",
    ]
    lines.extend(f"  created: {path.relative_to(repo_root).as_posix()}" for path in result.created)
    lines.extend(
        f"  overwritten: {path.relative_to(repo_root).as_posix()}" for path in result.overwritten
    )
    return "\n".join(lines) + "\n"


def render_status(result: ClientOsStatusResult, repo_root: Path) -> str:
    state = "ready" if result.preflight.ok else "needs work"
    closeout_state = "ready" if result.closeout.ok else "open"
    lines = [
        f"client-os status: {state}",
        f"  client: {result.client_id}",
        f"  engagement: {result.engagement_id}",
        f"  date: {result.meeting_date.isoformat()}",
        f"  profile: {result.profile}",
        f"  post-meeting closeout: {closeout_state}",
        "  artifacts:",
    ]
    for artifact in result.preflight.artifacts:
        marker = "ok" if artifact.exists else "missing"
        required = "required" if artifact.required else "optional"
        lines.append(
            "    "
            f"{marker}: {artifact.label} ({required}) "
            f"{artifact.path.relative_to(repo_root).as_posix()}"
        )
    lines.append("  preflight checks:")
    for check in result.preflight.checks:
        lines.append(f"    {check.severity}: {check.message}")
    lines.append("  closeout checks:")
    for check in result.closeout.checks:
        lines.append(f"    {check.severity}: {check.message}")
    return "\n".join(lines) + "\n"


def render_closeout(result: ClientOsCloseoutResult, repo_root: Path) -> str:
    state = "ok" if result.ok else "needs work"
    lines = [
        f"client-os closeout: {state}",
        f"  client: {result.client_id}",
        f"  engagement: {result.engagement_id}",
        f"  date: {result.meeting_date.isoformat()}",
        f"  receipt: {result.receipt.relative_to(repo_root).as_posix()}",
    ]
    for check in result.checks:
        lines.append(f"  {check.severity}: {check.message}")
    return "\n".join(lines) + "\n"


def render_bridge_export(result: ClientOsBridgeExportResult, repo_root: Path) -> str:
    state = "ok" if result.ok else "blocked"
    lines = [
        f"client-os bridge-export: {state}",
        "  mode: dry-run",
        f"  client: {result.client_id}",
        f"  engagement: {result.engagement_id}",
        f"  date: {result.meeting_date.isoformat()}",
        f"  bridge queue: {result.bridge_queue.relative_to(repo_root).as_posix()}",
    ]
    for check in result.checks:
        lines.append(f"  {check.severity}: {check.message}")
    if result.rows:
        lines.append("  rows:")
    for row in result.rows:
        lines.append(
            "    "
            f"{row.surface}: {row.candidate_action} | reviewer={row.reviewer} "
            f"| permission={row.permission_gate} | status={row.status}"
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
        or "automation authority: draft_only" in text.lower()
        or "draft-only automation" in text.lower()
    )
    if has_draft_authority:
        checks.append(_ok("draft-only automation boundary is present"))
    else:
        checks.append(_blocker("draft-only automation boundary missing"))

    return tuple(checks)


def _artifact_checks(
    config: DtpConfig,
    artifacts: tuple[ClientOsArtifactStatus, ...],
    profile: str,
) -> tuple[ClientOsCheck, ...]:
    checks: list[ClientOsCheck] = []
    for artifact in artifacts:
        if artifact.exists:
            checks.append(_ok(f"{artifact.label} exists: {_display(config, artifact.path)}"))
            continue
        if artifact.required:
            checks.append(_blocker(f"{artifact.label} missing: {_display(config, artifact.path)}"))
        else:
            checks.append(_warning(f"{artifact.label} missing: {_display(config, artifact.path)}"))
    if profile in {"infra", "full"}:
        checks.append(_ok(f"profile {profile} requires Client OS infrastructure artifacts"))
    return tuple(checks)


def _permission_check(*, root: Path, packet_text: str) -> ClientOsCheck:
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


def _closeout_checks(config: DtpConfig, receipt: Path) -> tuple[ClientOsCheck, ...]:
    checks: list[ClientOsCheck] = []
    if not receipt.exists():
        return (_blocker(f"post-meeting receipt missing: {_display(config, receipt)}"),)
    checks.append(_ok(f"post-meeting receipt exists: {_display(config, receipt)}"))
    text = receipt.read_text(encoding="utf-8")
    rows = _markdown_table_rows(text, "Required Updates")
    if not rows:
        checks.append(_blocker("receipt required-updates table missing or empty"))
        return tuple(checks)

    for row in rows:
        artifact = row.get("Artifact", "").strip() or "unnamed artifact"
        status = row.get("Updated?", "").strip().lower()
        if not status or "pending" in status:
            checks.append(_blocker(f"receipt row pending: {artifact}"))
        elif any(marker in status for marker in ("complete", "done", "updated", "not_applicable")):
            checks.append(_ok(f"receipt row complete: {artifact}"))
        elif "blocked" in status and artifact == "proof/*":
            checks.append(_ok("proof row remains blocked by gate"))
        else:
            checks.append(_warning(f"receipt row status needs review: {artifact} = {status}"))
    return tuple(checks)


def _bridge_checks(rows: tuple[ClientOsBridgeRow, ...]) -> tuple[ClientOsCheck, ...]:
    checks: list[ClientOsCheck] = []
    for row in rows:
        label = f"{row.surface}: {row.candidate_action}"
        surface = row.surface.strip().lower()
        if surface not in BRIDGE_SURFACES:
            checks.append(_blocker(f"unsupported bridge surface: {label}"))
        if _is_blank_or_tbd(row.reviewer):
            checks.append(_blocker(f"missing manual reviewer: {label}"))
        if _is_blank_or_tbd(row.permission_gate) or "unclear" in row.permission_gate.lower():
            checks.append(_blocker(f"unclear permission gate: {label}"))
        risk = row.risk.strip().lower()
        if _is_blank_or_tbd(row.risk) or not any(
            marker in risk for marker in ("low", "status-only")
        ):
            checks.append(_blocker(f"bridge risk is not low: {label}"))
        if any(
            marker in row.status.lower()
            for marker in ("blocked", "pending", "hold", "needs review")
        ):
            checks.append(_blocker(f"bridge row is not ready for dry-run export: {label}"))
        combined = " ".join(
            (
                row.candidate_action,
                row.payload_summary,
                row.permission_gate,
                row.risk,
                row.status,
            )
        ).lower()
        if any(marker in combined for marker in BLOCKING_BRIDGE_MARKERS):
            checks.append(_blocker(f"unsafe bridge payload or action: {label}"))
        if not any(check.message.endswith(label) for check in checks):
            checks.append(_ok(f"bridge row dry-run safe: {label}"))
    return tuple(checks)


def _bridge_rows(text: str) -> tuple[ClientOsBridgeRow, ...]:
    rows: list[ClientOsBridgeRow] = []
    for row in _markdown_table_rows(text, "Bridge Queue"):
        rows.append(
            ClientOsBridgeRow(
                surface=row.get("Surface", "").strip(),
                candidate_action=row.get("Candidate action", "").strip(),
                payload_summary=row.get("Payload summary", "").strip(),
                reviewer=row.get("Reviewer", "").strip(),
                permission_gate=row.get("Permission gate", "").strip(),
                risk=row.get("Risk", "").strip(),
                status=row.get("Status", "").strip(),
            )
        )
    return tuple(rows)


def _markdown_table_rows(text: str, section: str) -> tuple[dict[str, str], ...]:
    body = _section_body(text, section)
    headers: list[str] = []
    rows: list[dict[str, str]] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if all(set(cell) <= {"-", ":"} for cell in cells if cell):
            continue
        if not headers:
            headers = cells
            continue
        if len(cells) < len(headers):
            cells.extend([""] * (len(headers) - len(cells)))
        if any(cells):
            rows.append(dict(zip(headers, cells, strict=False)))
    return tuple(rows)


def _has_section(text: str, section: str) -> bool:
    return f"## {section}".lower() in text.lower()


def _source_index_has_real_rows(text: str) -> bool:
    for row in _markdown_table_rows(text, "Source Index"):
        source = row.get("Source", "").strip()
        if source and source.lower() not in {"source", "tbd"}:
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


def _artifact_statuses(
    config: DtpConfig,
    root: Path,
    meeting_date: date,
    profile: str,
) -> tuple[ClientOsArtifactStatus, ...]:
    statuses: list[ClientOsArtifactStatus] = []
    for spec in _artifact_specs(profile):
        path = root / spec.filename(meeting_date)
        statuses.append(
            ClientOsArtifactStatus(
                key=spec.key,
                label=spec.label,
                path=path,
                required=_artifact_required(spec, profile),
                exists=path.exists(),
            )
        )
    return tuple(statuses)


def _artifact_required(spec: ClientOsArtifactSpec, profile: str) -> bool:
    if profile == "base":
        return False
    if profile == "infra":
        return spec in INFRA_ARTIFACTS
    if profile == "full":
        return True
    raise ClientOsError(f"unsupported profile: {profile}")


def _artifact_specs(profile: str) -> tuple[ClientOsArtifactSpec, ...]:
    profile_id = _validate_profile(profile)
    if profile_id == "base":
        return BASE_ARTIFACTS
    if profile_id == "infra":
        return INFRA_ARTIFACTS
    return BASE_ARTIFACTS + INFRA_ARTIFACTS


def _validate_profile(profile: str) -> str:
    profile_id = profile.strip().lower()
    if profile_id not in CLIENT_OS_PROFILES:
        raise ClientOsError(
            f"invalid Client OS profile: {profile}; expected one of {', '.join(CLIENT_OS_PROFILES)}"
        )
    return profile_id


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


def _meeting_brief(client_id: str, engagement_id: str, meeting_date: date) -> str:
    return "\n".join(
        [
            f"# Meeting Brief - {meeting_date.isoformat()}",
            "",
            "## Brief Metadata",
            "",
            f"- Client/lane: {client_id}",
            f"- Engagement: {engagement_id}",
            f"- Meeting date: {meeting_date.isoformat()}",
            "- Automation authority: draft_only",
            "- External actions: none",
            "",
            "## Source Pack",
            "",
            "| Source | Use in meeting | Risk / boundary |",
            "|---|---|---|",
            "| client-os-pilot packet | Run-of-show and gates | Do not treat as public proof |",
            "| source-material-index.md | Source handling | Do not collect private records |",
            "| owner-action-items.md | Open loops | Do not send without Toni review |",
            "",
            "## Meeting Thesis",
            "",
            "- What this meeting should make true:",
            "- What decision the meeting should support:",
            "- What must stay out of scope:",
            "",
            "## Talk Track",
            "",
            "1. Confirm current launch state and what changed since the last touch.",
            "2. Walk the product from a first-user trust/onboarding perspective.",
            "3. Identify the smallest useful sprint or next action.",
            "4. Ask permission boundaries explicitly before any proof or public story.",
            "5. Close with owner actions, Toni actions, and review timing.",
            "",
            "## Ask Directly",
            "",
            "- What is the one thing this soft launch needs to prove?",
            "- What still feels risky, confusing, or unfinished?",
            "- What source material is approved for private planning?",
            "- Is any public proof allowed? If yes, who reviews it first?",
            "",
            "## Do Not Collect",
            "",
            "- Credentials, raw logs, private user/admin records, private contact lists.",
            "- Screenshots, metrics, names, or testimonials without written permission.",
            "- Commitments that imply production ownership beyond the accepted scope.",
            "",
        ]
    )


def _chain_run(client_id: str, engagement_id: str, meeting_date: date) -> str:
    return "\n".join(
        [
            f"# Chain Run - {meeting_date.isoformat()}",
            "",
            "## Chain Metadata",
            "",
            f"- Client/lane: {client_id}",
            f"- Engagement: {engagement_id}",
            f"- Meeting date: {meeting_date.isoformat()}",
            "- Automation authority: draft_only",
            "- Chain status: pre_meeting",
            "",
            "## Run Sequence",
            "",
            "| Step | Owner | Input | Output | Gate | Status |",
            "|---|---|---|---|---|---|",
            (
                "| Preflight | Agent | pilot packet + scaffolds | readiness report | "
                "no blockers | pending |"
            ),
            "| Meeting brief | Toni | meeting-brief | live conversation | Toni review | pending |",
            "| Notes capture | Toni/Agent | meeting | meeting notes | private only | pending |",
            (
                "| Receipt | Agent | notes + kit | post-meeting receipt | "
                "no unresolved owner | pending |"
            ),
            "| Build task | Agent | receipt decisions | bounded task | Toni review | pending |",
            (
                "| Bridge queue | Agent | receipt + build task | dry-run actions | "
                "no live writes | pending |"
            ),
            "",
            "## Authority Matrix",
            "",
            "| Action | Allowed now? | Required gate |",
            "|---|---|---|",
            "| Update private kit files | yes | Toni review before relying on claims |",
            "| Draft follow-up after meeting | yes | actual meeting facts first |",
            "| Send email | no | explicit Toni approval |",
            "| Calendar changes | no | explicit Toni approval |",
            "| Hub/Notion mirror | dry-run only | sanitized payload + reviewer |",
            "| Public proof/copy | no | permission, redaction, reviewer, evidence, caveat |",
            "",
            "## Evidence Receipt",
            "",
            "| Evidence | Location | Captured? | Notes |",
            "|---|---|---|---|",
            "| Preflight output | console | pending |  |",
            "| Meeting notes | meeting-notes file | pending |  |",
            "| Receipt | post-meeting receipt | pending |  |",
            "| Bridge export | dry-run output | pending | no external writes |",
            "",
            "## Stop Conditions",
            "",
            "- Permission is unclear but public proof is requested.",
            "- A row would expose private records, credentials, or raw client data.",
            "- A proposed action would send, schedule, publish, or mutate externally.",
            "- Scope expands beyond the accepted engagement without Toni review.",
            "",
        ]
    )


def _build_task(client_id: str, engagement_id: str, meeting_date: date) -> str:
    return "\n".join(
        [
            f"# Build Task - {meeting_date.isoformat()}",
            "",
            "## Task Metadata",
            "",
            f"- Client/lane: {client_id}",
            f"- Engagement: {engagement_id}",
            f"- Source meeting: {meeting_date.isoformat()}",
            "- Automation authority: draft_only",
            "- Task status: waiting_for_meeting_evidence",
            "",
            "## Candidate Task",
            "",
            "- Problem to solve:",
            "- User/client impact:",
            "- Smallest useful deliverable:",
            "- Not included:",
            "",
            "## Source Requirements",
            "",
            "| Required source | Current state | Owner | Gate |",
            "|---|---|---|---|",
            "| Meeting facts | pending | Toni | post-meeting notes |",
            "| Owner decision | pending | Client/operator | receipt evidence |",
            "| Permission state | pending | Client/operator | written confirmation if proof |",
            "| Review boundary | pending | Toni | no external action before review |",
            "",
            "## Acceptance",
            "",
            "- Task can be completed from private-kit evidence.",
            "- Public proof remains blocked unless every proof gate passes.",
            "- Follow-up remains draft-only until Toni approves sending.",
            "- No connector, calendar, Hub, Notion, or repo mutation is implied.",
            "",
            "## Post-Meeting Fill",
            "",
            "- Final task title:",
            "- Owner:",
            "- Due/review trigger:",
            "- Verification:",
            "- Handoff:",
            "",
        ]
    )


def _bridge_queue(client_id: str, engagement_id: str, meeting_date: date) -> str:
    return "\n".join(
        [
            f"# Bridge Queue - {meeting_date.isoformat()}",
            "",
            "## Queue Metadata",
            "",
            f"- Client/lane: {client_id}",
            f"- Engagement: {engagement_id}",
            f"- Meeting date: {meeting_date.isoformat()}",
            "- Automation authority: draft_only",
            "- Mode: dry_run_only",
            "- External writes: blocked",
            "",
            "## Bridge Queue",
            "",
            (
                "| Surface | Candidate action | Payload summary | Reviewer | "
                "Permission gate | Risk | Status |"
            ),
            "|---|---|---|---|---|---|---|",
            (
                "| Gmail | Draft follow-up after meeting facts exist | TBD | Toni | "
                "post-meeting evidence | medium | pending |"
            ),
            (
                "| Calendar | No automatic calendar changes | none | Toni | "
                "explicit approval only | low | blocked |"
            ),
            (
                "| Hub | Draft internal status mirror only | status-only TBD | Toni | "
                "sanitized payload | low | pending |"
            ),
            (
                "| Notion | Draft sanitized cockpit row only | status-only TBD | Toni | "
                "sanitized payload | low | pending |"
            ),
            "",
            "## Export Rules",
            "",
            "- `dtp practice client-os bridge-export` is dry-run only.",
            "- Do not send, schedule, publish, sync, or mutate external systems.",
            "- Rows without reviewer, clear permission gate, and low-risk payload stay blocked.",
            "- Public proof, private records, credentials, and raw transcripts are blocked.",
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


def _is_blank_or_tbd(value: str) -> bool:
    normalized = value.strip().lower()
    return not normalized or normalized in {"tbd", "pending", "none", "n/a"}
