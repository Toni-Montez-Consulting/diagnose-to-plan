from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from dtp.config import DtpConfig

CANONICAL_REPOS = (
    "consulting",
    "diagnose-to-plan",
    "hub",
    "engineering-playbook",
    "hub-prompts",
    "hub-registry",
    "fitness-app",
    "FamilyTrips",
    "demario-pickleball-1",
    "dse-content",
    "tm-skills",
)


@dataclass(frozen=True)
class VerificationRow:
    lane: str
    date: str
    result: str
    commit: str
    artifact: str

    def to_dict(self) -> dict[str, str]:
        return {
            "lane": self.lane,
            "date": self.date,
            "result": self.result,
            "commit": self.commit,
            "artifact": self.artifact,
        }


@dataclass(frozen=True)
class RepoReport:
    repo: str
    manifest_status: str
    evidence_status: str
    owner_lane: str
    local_gate: str
    ci_gate: str
    manual_gate: str
    next_action: str
    blocker: str
    latest_verification: tuple[VerificationRow, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "repo": self.repo,
            "manifest_status": self.manifest_status,
            "evidence_status": self.evidence_status,
            "owner_lane": self.owner_lane,
            "local_gate": self.local_gate,
            "ci_gate": self.ci_gate,
            "manual_gate": self.manual_gate,
            "next_action": self.next_action,
            "blocker": self.blocker,
            "latest_verification": [row.to_dict() for row in self.latest_verification],
        }


@dataclass(frozen=True)
class WorkspaceReport:
    boundary: str
    live_status: str
    command_center_spec_present: bool
    repos: tuple[RepoReport, ...]
    blockers: tuple[str, ...]

    @property
    def missing_coverage(self) -> tuple[RepoReport, ...]:
        return tuple(
            repo
            for repo in self.repos
            if repo.manifest_status != "ok" or repo.evidence_status != "ok"
        )

    def to_dict(self) -> dict[str, object]:
        return {
            "boundary": self.boundary,
            "live_status": self.live_status,
            "command_center_spec_present": self.command_center_spec_present,
            "repos": [repo.to_dict() for repo in self.repos],
            "missing_coverage": [repo.to_dict() for repo in self.missing_coverage],
            "blockers": list(self.blockers),
        }


def run_workspace_report(config: DtpConfig) -> WorkspaceReport:
    efficiency_dir = config.practice_os_dir / "efficiency"
    docs_dir = config.repo_root / "docs"
    command_center_spec = _read_optional(docs_dir / "WORKSPACE_COMMAND_CENTER_V0.md")
    manifests = _read_artifacts(efficiency_dir, "-repo-manifest.md")
    evidence_indexes = _read_artifacts(efficiency_dir, "-evidence-index.md")
    canonical_by_slug = {_slug(repo): repo for repo in CANONICAL_REPOS}
    repo_slugs = [*_slugged(CANONICAL_REPOS)]
    extra_slugs = sorted((set(manifests) | set(evidence_indexes)) - set(repo_slugs))
    repos = [
        _build_repo_report(
            repo=canonical_by_slug.get(slug, slug),
            manifest=manifests.get(slug),
            evidence=evidence_indexes.get(slug),
        )
        for slug in [*repo_slugs, *extra_slugs]
    ]
    return WorkspaceReport(
        boundary="read_only_recorded_dtp_artifacts",
        live_status="not_checked_v0_no_repo_commands_or_github_calls",
        command_center_spec_present=bool(command_center_spec.strip()),
        repos=tuple(repos),
        blockers=_extract_active_queue_blockers(docs_dir / "ROADMAP_EXECUTION_BACKLOG.md"),
    )


def render_workspace_report(report: WorkspaceReport) -> str:
    lines = [
        "Workspace Command Center V0 Report",
        f"Boundary: {report.boundary}",
        f"Live status: {report.live_status}",
        f"Command Center spec: {'present' if report.command_center_spec_present else 'missing'}",
        "",
        "Repo Coverage",
    ]
    for repo in report.repos:
        latest = _summarize_verification(repo.latest_verification)
        gate = repo.local_gate or repo.ci_gate or repo.manual_gate or "manifest_missing"
        lines.append(
            f"- {repo.repo}: manifest={repo.manifest_status}; evidence={repo.evidence_status}; "
            f"lane={repo.owner_lane or 'unknown'}; latest={latest}; gate={gate}; "
            f"blocker={repo.blocker or 'none'}; next={repo.next_action or 'not recorded'}"
        )

    lines.append("")
    lines.append("Missing Coverage")
    if report.missing_coverage:
        for repo in report.missing_coverage:
            missing = []
            if repo.manifest_status != "ok":
                missing.append(repo.manifest_status)
            if repo.evidence_status != "ok":
                missing.append(repo.evidence_status)
            lines.append(f"- {repo.repo}: {', '.join(missing)}")
    else:
        lines.append("- none")

    lines.append("")
    lines.append("Open Blockers / Manual Gates")
    if report.blockers:
        lines.extend(f"- {blocker}" for blocker in report.blockers)
    else:
        lines.append("- none recorded in active queue")

    lines.append("")
    lines.append(
        "V0 does not execute checks, call GitHub, mutate repos, install skills, publish proof, "
        "touch production systems, touch DSE, or build FAOS."
    )
    return "\n".join(lines) + "\n"


def _build_repo_report(
    repo: str,
    manifest: str | None,
    evidence: str | None,
) -> RepoReport:
    return RepoReport(
        repo=_repo_label(repo, manifest),
        manifest_status="ok" if manifest is not None else "manifest_missing",
        evidence_status="ok" if evidence is not None else "evidence_missing",
        owner_lane=_bullet_value(manifest, "Owner lane"),
        local_gate=_bullet_value(manifest, "Local gate"),
        ci_gate=_bullet_value(manifest, "CI gate"),
        manual_gate=_bullet_value(manifest, "Manual gate"),
        next_action=_bullet_value(manifest, "Next action"),
        blocker=_bullet_value(manifest, "Blocker"),
        latest_verification=_latest_verification(evidence),
    )


def _read_artifacts(root: Path, suffix: str) -> dict[str, str]:
    if not root.exists():
        return {}
    artifacts: dict[str, str] = {}
    for path in sorted(root.glob(f"*{suffix}")):
        name = path.name.removesuffix(suffix)
        artifacts[_slug(name)] = path.read_text(encoding="utf-8")
    return artifacts


def _read_optional(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _bullet_value(text: str | None, label: str) -> str:
    if not text:
        return ""
    pattern = re.compile(rf"^- {re.escape(label)}:\s*(.+)$")
    for line in text.splitlines():
        match = pattern.match(line.strip())
        if match:
            return _clean_inline_markdown(match.group(1))
    return ""


def _repo_label(default: str, manifest: str | None) -> str:
    repo = _bullet_value(manifest, "Repo")
    return repo or default


def _latest_verification(text: str | None) -> tuple[VerificationRow, ...]:
    if not text:
        return ()
    rows: list[VerificationRow] = []
    in_section = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## Latest Verification"):
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            break
        if not in_section or not stripped.startswith("|"):
            continue
        cells = [_clean_inline_markdown(cell.strip()) for cell in stripped.strip("|").split("|")]
        if len(cells) != 5 or cells[0].lower() == "lane" or set(cells[0]) == {"-"}:
            continue
        rows.append(
            VerificationRow(
                lane=cells[0],
                date=cells[1],
                result=cells[2],
                commit=cells[3],
                artifact=cells[4],
            )
        )
    return tuple(rows[:4])


def _extract_active_queue_blockers(path: Path) -> tuple[str, ...]:
    if not path.exists():
        return ()
    text = path.read_text(encoding="utf-8")
    lines: list[str] = []
    in_section = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped == "## Current Active Next Queue":
            in_section = True
            continue
        if in_section and stripped.startswith("## "):
            break
        if in_section and re.match(r"^\d+\.", stripped):
            lines.append(re.sub(r"^\d+\.\s*", "", stripped))
    keywords = ("Mom", "DSE", "tm-skills", "proof", "FAOS", "Hub", "smoke")
    return tuple(line for line in lines if any(keyword in line for keyword in keywords))


def _summarize_verification(rows: tuple[VerificationRow, ...]) -> str:
    if not rows:
        return "not recorded"
    return "; ".join(f"{row.lane}={row.result} ({row.date})" for row in rows[:3])


def _slugged(values: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(_slug(value) for value in values)


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def _clean_inline_markdown(value: str) -> str:
    return value.replace("`", "").strip()
