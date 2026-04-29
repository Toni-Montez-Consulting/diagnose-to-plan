from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from dtp.capture import render_markdown_with_frontmatter, slugify
from dtp.config import DtpConfig
from dtp.frontmatter_utils import split_frontmatter
from dtp.git_safety import resolve_inside_repo

KIT_KINDS = {"audit", "launch", "operating-system", "assistant"}


class KitError(ValueError):
    pass


@dataclass(frozen=True)
class KitCreateResult:
    client_id: str
    engagement_id: str
    root: Path
    created: tuple[Path, ...]
    existing: tuple[Path, ...]


@dataclass(frozen=True)
class KitStatus:
    client_id: str
    root: Path
    phase: str
    missing: tuple[str, ...]
    present: tuple[str, ...]
    metrics_ready: bool
    redaction_ready: bool
    handoff_ready: bool

    @property
    def ready(self) -> bool:
        return (
            not self.missing
            and self.metrics_ready
            and self.redaction_ready
            and self.handoff_ready
        )


def run_kit_new(
    *,
    config: DtpConfig,
    client: str,
    project: str,
    kind: str,
    clock: datetime | None = None,
) -> KitCreateResult:
    normalized_kind = kind.strip().lower()
    if normalized_kind not in KIT_KINDS:
        raise KitError(f"unknown kit kind: {kind}")

    client_id = slugify(client)
    engagement_id = slugify(project)
    now = clock or datetime.now(UTC)
    root = resolve_inside_repo(config.engagements_dir / client_id, config.repo_root)
    engagement = root / engagement_id

    metadata = _metadata(
        client_id=client_id,
        engagement_id=engagement_id,
        kind=normalized_kind,
        now=now,
    )
    files = {
        root / "client-context.md": _client_context(client_id),
        root / "data-inventory.md": _data_inventory(),
        root / "consent.md": _consent(),
        engagement / "diagnose.md": _diagnose(),
        engagement / "plan.md": _plan(),
        engagement / "build-log.md": _build_log(),
        engagement / "decision-log.md": _decision_log(),
        engagement / "command-room" / "fit-assessment.md": _command_room_fit_assessment(
            client_id, engagement_id
        ),
        engagement / "evals" / "log.md": _eval_log(),
        engagement / "handoff" / "checklist.md": _handoff_checklist(),
        engagement / "proof" / "asset-inventory.md": _asset_inventory(client_id, engagement_id),
        engagement / "proof" / "evidence-source-checklist.md": _evidence_source_checklist(
            client_id, engagement_id
        ),
        engagement / "proof" / "permission-reviewer-checklist.md": (
            _permission_reviewer_checklist(client_id, engagement_id)
        ),
        engagement / "proof" / "proof-packet.md": _proof_packet(client_id, engagement_id),
        engagement / "proof" / "public-claim-review.md": _public_claim_review(
            client_id, engagement_id
        ),
        engagement / "proof" / "redaction-queue-item.md": _redaction_queue_item(
            client_id, engagement_id
        ),
        engagement / "case-study" / "internal.md": _case_study_internal(),
        engagement / "case-study" / "redacted.md": _case_study_redacted(),
    }

    created: list[Path] = []
    existing: list[Path] = []
    for path, body in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            existing.append(path)
            continue
        path.write_text(render_markdown_with_frontmatter(metadata, body), encoding="utf-8")
        created.append(path)

    return KitCreateResult(
        client_id=client_id,
        engagement_id=engagement_id,
        root=root,
        created=tuple(created),
        existing=tuple(existing),
    )


def run_kit_status(*, config: DtpConfig, client: str | None = None) -> tuple[KitStatus, ...]:
    root = resolve_inside_repo(config.engagements_dir, config.repo_root)
    if not root.exists():
        return ()

    client_dirs = (
        [root / slugify(client)]
        if client
        else sorted(path for path in root.iterdir() if path.is_dir())
    )
    statuses: list[KitStatus] = []
    for client_dir in client_dirs:
        if not client_dir.exists() or not client_dir.is_dir():
            raise KitError(f"kit not found: {client or client_dir.name}")
        statuses.append(_status_for_client(client_dir))
    return tuple(statuses)


def _status_for_client(root: Path) -> KitStatus:
    required = (
        "client-context.md",
        "data-inventory.md",
        "consent.md",
    )
    engagement_dirs = sorted(
        path for path in root.iterdir() if path.is_dir() and path.name not in {"deliverable"}
    )
    latest = engagement_dirs[-1] if engagement_dirs else None
    if latest:
        required += tuple(
            f"{latest.name}/{path}"
            for path in (
                "diagnose.md",
                "plan.md",
                "build-log.md",
                "decision-log.md",
                "command-room/fit-assessment.md",
                "evals/log.md",
                "handoff/checklist.md",
                "proof/asset-inventory.md",
                "proof/evidence-source-checklist.md",
                "proof/permission-reviewer-checklist.md",
                "proof/proof-packet.md",
                "proof/public-claim-review.md",
                "proof/redaction-queue-item.md",
                "case-study/internal.md",
                "case-study/redacted.md",
            )
        )

    present = tuple(item for item in required if (root / item).exists())
    missing = tuple(item for item in required if item not in present)
    phase = _phase(root, latest)
    metrics_ready = latest is not None and _has_metric_placeholders_filled(
        latest / "evals" / "log.md"
    )
    redaction_ready = (
        latest is not None
        and _review_status(latest / "case-study" / "redacted.md") in {"reviewed", "approved"}
    )
    handoff_ready = latest is not None and _handoff_ready(latest / "handoff" / "checklist.md")
    return KitStatus(
        client_id=root.name,
        root=root,
        phase=phase,
        missing=missing,
        present=present,
        metrics_ready=metrics_ready,
        redaction_ready=redaction_ready,
        handoff_ready=handoff_ready,
    )


def render_status(statuses: Iterable[KitStatus], repo_root: Path) -> str:
    lines: list[str] = []
    for status in statuses:
        relative = status.root.relative_to(repo_root).as_posix()
        state = "ready" if status.ready else "needs work"
        lines.extend(
            [
                f"{status.client_id} [{state}]",
                f"  path: {relative}",
                f"  phase: {status.phase}",
                f"  missing: {', '.join(status.missing) if status.missing else 'none'}",
                f"  metrics: {'ready' if status.metrics_ready else 'needed'}",
                f"  redaction: {'reviewed' if status.redaction_ready else 'needed'}",
                f"  handoff: {'ready' if status.handoff_ready else 'needed'}",
            ]
        )
    return "\n".join(lines) + ("\n" if lines else "")


def _metadata(*, client_id: str, engagement_id: str, kind: str, now: datetime) -> dict[str, object]:
    return {
        "created": now.astimezone(UTC).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "command": "kit new",
        "client_id": client_id,
        "engagement_id": engagement_id,
        "kit_kind": kind,
        "data_class": "P2",
        "confidential": True,
        "permission_level": "internal_only",
        "review_status": "draft",
    }


def _client_context(client_id: str) -> str:
    return "\n".join(
        [
            f"# Client Context: {client_id}",
            "",
            "## What This Organization Does",
            "",
            "## Current Bottleneck",
            "",
            "## Owner Constraints",
            "",
            "## Systems Of Record",
            "",
            "## Approval Rules",
            "",
            "## Voice And Language Notes",
            "",
            "## Data Sensitivity",
            "",
            "## Do Not Do",
            "",
        ]
    )


def _data_inventory() -> str:
    return "\n".join(
        [
            "# Data Inventory",
            "",
            "| System | Data touched | Owner | Data class | Fallback path |",
            "|---|---|---|---|---|",
            "| TBD | TBD | TBD | P2 | TBD |",
            "",
        ]
    )


def _consent() -> str:
    return "\n".join(
        [
            "# Consent And Public Use",
            "",
            "## Permission Level",
            "",
            "- internal only until explicitly changed in writing",
            "",
            "## Named Use",
            "",
            "- not approved",
            "",
            "## Anonymous External Use",
            "",
            "- not approved",
            "",
            "## COI / Conflict Screen",
            "",
            "- not reviewed",
            "",
            "## Proof Promotion Gate",
            "",
            "- no public proof until permission, redaction, reviewer, evidence, and caveat pass",
            "",
        ]
    )


def _diagnose() -> str:
    return "\n".join(
        [
            "# Diagnose",
            "",
            "## Trigger",
            "",
            "## Current Workflow",
            "",
            "## What Breaks",
            "",
            "## Non-AI Fix First",
            "",
            "## Success Criteria",
            "",
        ]
    )


def _plan() -> str:
    return "\n".join(
        [
            "# Plan",
            "",
            "## Phase 1",
            "",
            "## Not This Phase",
            "",
            "## Budget And Tools",
            "",
            "## Risks",
            "",
            "## Acceptance Criteria",
            "",
        ]
    )


def _build_log() -> str:
    return "# Build Log\n\n## Entries\n\n"


def _decision_log() -> str:
    return "# Decision Log\n\n| Date | Decision | Why | Revisit trigger |\n|---|---|---|---|\n"


def _command_room_fit_assessment(client_id: str, engagement_id: str) -> str:
    return "\n".join(
        [
            "# Client Command Room Fit Assessment",
            "",
            (
                "Use this before proposing or building a private owner surface. The default is "
                "the smallest operating surface that helps the owner run the workflow after "
                "delivery."
            ),
            "",
            "## Project",
            "",
            f"- Client/project: {client_id}",
            f"- Engagement: {engagement_id}",
            "- Date: TBD",
            "- Assessor: TBD",
            "- Related pattern: docs/CLIENT_COMMAND_ROOM_PATTERN.md",
            "",
            "## Workflow Pain",
            "",
            "| Workflow | Current home | Frequency | Owner pain | Business risk | Evidence |",
            "|---|---|---:|---|---|---|",
            "| TBD | memory / text / email / sheet / app | TBD | TBD | TBD | TBD |",
            "",
            "## Recurring Operating Decisions",
            "",
            "| Decision | Who decides | Inputs needed | Output | Deadline or cadence |",
            "|---|---|---|---|---|",
            "| TBD | TBD | TBD | TBD | TBD |",
            "",
            "## Existing Tool Check",
            "",
            "| Existing tool | Already used? | Gap | Keep / replace / augment |",
            "|---|---|---|---|",
            "| Notion/Airtable/Sheets | TBD | TBD | TBD |",
            "| Existing CRM/admin | TBD | TBD | TBD |",
            "| Email or form inbox | TBD | TBD | TBD |",
            "| Calendar/scheduler | TBD | TBD | TBD |",
            "| Payment processor dashboard | TBD | TBD | TBD |",
            "",
            "## Decision",
            "",
            "- [ ] Build a Client Command Room",
            "- [ ] Create a handoff checklist instead",
            "- [ ] No private surface",
            "- [x] Defer until the workflow pain is proven",
            "",
            "## Support And Verification Readiness",
            "",
            "| Evidence source | Exists? | Artifact path or command | Hard / advisory / manual |",
            "|---|---|---|---|",
            "| Build/deploy status | TBD | TBD | hard |",
            "| Intake/form health | TBD | TBD | hard |",
            "| Auth/owner access | TBD | TBD | manual |",
            "| Redaction/permission status | yes | proof/ | hard |",
            "",
            "## Proof Potential",
            "",
            "- Baseline: TBD",
            "- After-state: TBD",
            "- Useful screenshot or walkthrough: TBD",
            "- Metric: TBD",
            "- Caveat: TBD",
            "- Permission level: internal_only",
            "- Redaction reviewer: TBD",
            "",
            "## Recommendation",
            "",
            "- Recommended path: decide after diagnose and owner workflow evidence",
            "- Why: avoid building a portal before there is recurring operational pain",
            (
                "- Smallest useful first version: handoff checklist unless the assessment "
                "proves otherwise"
            ),
            (
                "- What stays manual on purpose: permission, redaction, proof approval, and "
                "owner account access"
            ),
            "- Next review date: TBD",
            "",
        ]
    )


def _eval_log() -> str:
    return "\n".join(
        [
            "# Eval Log",
            "",
            "## Primary Metric",
            "",
            "- name: TBD",
            "- baseline: TBD",
            "- target: TBD",
            "- after: TBD",
            "",
            "## Secondary Metric",
            "",
            "- name: TBD",
            "- baseline: TBD",
            "- target: TBD",
            "- after: TBD",
            "",
        ]
    )


def _handoff_checklist() -> str:
    return "\n".join(
        [
            "# Handoff Checklist",
            "",
            "- [ ] Client can describe what the system does.",
            "- [ ] Client can find the runbook.",
            "- [ ] Client can run the main workflow.",
            "- [ ] Client knows what not to touch.",
            "- [ ] Client knows how to disable automations or routines.",
            "- [ ] Client knows who owns each account and subscription.",
            "- [ ] Handoff recording captured.",
            "",
        ]
    )


def _asset_inventory(client_id: str, engagement_id: str) -> str:
    return "\n".join(
        [
            "# Asset Inventory",
            "",
            "## Engagement / Project",
            "",
            f"- Name: {client_id}/{engagement_id}",
            "- Owner: TBD",
            "- Reviewer: TBD",
            "- Last updated: TBD",
            "",
            "## Assets",
            "",
            "| Asset | Type | Source | Sensitivity | Permission | Redaction | Proof use |",
            "|---|---|---|---|---|---|---|",
            (
                "| TBD | screenshot / document / walkthrough / report | TBD | P2 | "
                "internal_only | not_reviewed | candidate |"
            ),
            "",
            "## Missing Assets",
            "",
            "- Baseline screenshot or walkthrough.",
            "- After-state screenshot or walkthrough.",
            "- Verification receipt.",
            "",
            "## Restricted Assets",
            "",
            "- None recorded.",
            "",
            "## Public-Safe Assets",
            "",
            "- None recorded.",
            "",
            "## Next Action",
            "",
            (
                "Do not move an asset into public proof until permission, redaction, "
                "reviewer, evidence source, and caveat are recorded."
            ),
            "",
        ]
    )


def _evidence_source_checklist(client_id: str, engagement_id: str) -> str:
    return "\n".join(
        [
            "# Evidence Source Checklist",
            "",
            "## Evidence",
            "",
            f"- Engagement/project: {client_id}/{engagement_id}",
            "- Repo: TBD",
            "- Branch: TBD",
            "- Commit: TBD",
            "- Artifact path: TBD",
            "- CI/run link: TBD",
            "- Reviewer: TBD",
            "",
            "## Source Quality",
            "",
            "- Local gate result: TBD",
            "- CI gate result: TBD",
            "- Release/support gate result: TBD",
            "- Manual gate result: TBD",
            "- Reproducible command: TBD",
            "- Date captured: TBD",
            "",
            "## Proof Fitness",
            "",
            "- Supports which claim: TBD",
            "- Baseline present: no",
            "- After-state present: no",
            "- Metric present: no",
            "- Caveat present: no",
            "- Screenshot/walkthrough present: no",
            "- Redaction status: not_reviewed",
            "- Permission status: internal_only",
            "",
            "## Decision",
            "",
            "- Use as proof source: later",
            "- Reason: evidence has not been captured or reviewed yet",
            "- Next action: capture baseline, after-state, verification receipt, and caveat",
            "",
        ]
    )


def _permission_reviewer_checklist(client_id: str, engagement_id: str) -> str:
    return "\n".join(
        [
            "# Permission / Reviewer Checklist",
            "",
            "## Item",
            "",
            f"- Engagement/project: {client_id}/{engagement_id}",
            "- Artifact or claim: TBD",
            "- Intended use: internal",
            "- Reviewer: TBD",
            "",
            "## Permission",
            "",
            "- Owner permission: not_requested",
            "- Client/customer permission: not_requested",
            "- Platform/store permission: not_applicable",
            "- Microsoft/COI screen: not_reviewed",
            "- Family/private data approval: not_applicable",
            "",
            "## Reviewer Checks",
            "",
            "- [ ] Evidence source is named.",
            "- [ ] Baseline and after-state are accurate.",
            "- [ ] Caveat is included.",
            "- [ ] Redaction status is acceptable.",
            "- [ ] Public claim does not overstate the result.",
            "- [ ] Sensitive data is removed or intentionally restricted.",
            "- [ ] Screenshots/walkthroughs are approved for intended use.",
            "",
            "## Decision",
            "",
            "- Status: parked",
            "- Notes: keep internal until the evidence and permission gates are complete",
            "- Next action: complete the evidence source checklist and redaction queue item",
            "",
        ]
    )


def _proof_packet(client_id: str, engagement_id: str) -> str:
    return "\n".join(
        [
            "# Proof Packet",
            "",
            "## Proof Candidate",
            "",
            f"- Engagement/project: {client_id}/{engagement_id}",
            "- Public-safe title: TBD",
            "- Claim: TBD",
            "- Audience: internal",
            "- Reviewer: TBD",
            "",
            "## Baseline",
            "",
            "TBD",
            "",
            "## After-State",
            "",
            "TBD",
            "",
            "## Evidence",
            "",
            "- Source artifact: TBD",
            "- Verification receipt: TBD",
            "- Screenshot/walkthrough: TBD",
            "- Metric: TBD",
            "- Caveat: TBD",
            "",
            "## Permission",
            "",
            "- Permission level: internal_only",
            "- Permission source: not_requested",
            "- Reviewer: TBD",
            "- Review date: TBD",
            "",
            "## Redaction",
            "",
            "- Redaction status: not_reviewed",
            "- Redacted assets: none",
            "- Remaining private material: TBD",
            "",
            "## Public Claim Draft",
            "",
            "No public claim approved.",
            "",
            "## What Stayed Manual On Purpose",
            "",
            "- Permission review.",
            "- Redaction review.",
            "- Reviewer approval.",
            "",
            "## Publish Decision",
            "",
            "- Status: parked",
            "- Next action: collect source evidence before drafting public proof",
            "",
        ]
    )


def _public_claim_review(client_id: str, engagement_id: str) -> str:
    return "\n".join(
        [
            "# Public Claim Review",
            "",
            "## Claim",
            "",
            "- Draft claim: TBD",
            "- Public surface: consulting",
            "- Audience: TBD",
            "- Reviewer: TBD",
            "",
            "## Evidence",
            "",
            f"- Proof packet: engagements/{client_id}/{engagement_id}/proof/proof-packet.md",
            "- Evidence source: TBD",
            "- Baseline: TBD",
            "- After-state: TBD",
            "- Caveat: TBD",
            "",
            "## Risk Checks",
            "",
            "- Overclaim risk: unknown",
            "- Private/client data risk: yes until redacted",
            "- COI/Microsoft-adjacent risk: not_reviewed",
            "- Revenue/customer metric risk: unknown",
            "- App Store/platform claim risk: not_applicable",
            "- Security/privacy claim risk: unknown",
            "",
            "## Approved Wording",
            "",
            "None.",
            "",
            "## Decision",
            "",
            "- Status: parked",
            (
                "- Notes: public wording requires evidence, caveat, permission, redaction, "
                "and reviewer approval"
            ),
            "- Next action: complete proof packet and permission/reviewer checklist",
            "",
        ]
    )


def _redaction_queue_item(client_id: str, engagement_id: str) -> str:
    return "\n".join(
        [
            "# Redaction Queue Item",
            "",
            "## Target",
            "",
            f"- Engagement/project: {client_id}/{engagement_id}",
            "- Target type: proof_candidate",
            "- Target pointer: proof/proof-packet.md",
            "- Reviewer: TBD",
            "",
            "## Sensitivity",
            "",
            "- Data class: P2",
            "- Contains client/private data: unknown",
            "- Contains customer data: unknown",
            "- Contains Microsoft/customer-adjacent material: unknown",
            "- Contains secrets or credentials: unknown",
            "",
            "## Review",
            "",
            "- Status: not_started",
            "- Permission level: internal_only",
            "- Required changes: identify private details, remove identifiers, record caveats",
            "",
            "## Replacement / Redacted Version",
            "",
            "- Redacted pointer: case-study/redacted.md",
            "- Summary safe to reuse: none yet",
            "",
            "## Decision",
            "",
            "- Reviewer: TBD",
            "- Review date: TBD",
            "- Next action: complete evidence checklist before public claim review",
            "",
        ]
    )


def _case_study_internal() -> str:
    return "\n".join(
        [
            "# Internal Case Study Notes",
            "",
            "## Before",
            "",
            "## Intervention",
            "",
            "## After",
            "",
            "## Evidence",
            "",
            "## Caveats",
            "",
        ]
    )


def _case_study_redacted() -> str:
    return "\n".join(
        [
            "# Redacted Case Study Packet",
            "",
            "## Claim",
            "",
            "## Evidence source",
            "",
            "## Baseline",
            "",
            "## After",
            "",
            "## Measurement caveats",
            "",
            "## Permission level",
            "",
            "internal_only",
            "",
            "## Redaction status",
            "",
            "draft",
            "",
            "## Reviewer",
            "",
        ]
    )


def _phase(root: Path, latest: Path | None) -> str:
    if latest is None:
        return "client-context"
    if not (latest / "plan.md").exists():
        return "diagnose"
    if not (latest / "handoff" / "checklist.md").exists():
        return "build"
    return "handoff"


def _has_metric_placeholders_filled(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    return "TBD" not in text and "baseline:" in text and "after:" in text


def _review_status(path: Path) -> str:
    if not path.exists():
        return ""
    metadata, body = split_frontmatter(path)
    status = str(metadata.get("review_status") or "").strip().lower()
    if status:
        return status
    marker = "## Redaction status"
    if marker not in body:
        return ""
    return body.split(marker, 1)[1].strip().splitlines()[0].strip().lower()


def _handoff_ready(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    return "- [ ]" not in text and "Handoff recording captured" in text
