from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

from dtp.cli import app
from dtp.commands.workspace_report import render_workspace_report, run_workspace_report
from dtp.config import load_config


def test_workspace_report_discovers_artifacts_and_missing_coverage(tmp_path: Path) -> None:
    _write_manifest(
        tmp_path,
        "consulting",
        repo="consulting",
        owner_lane="public proof/storefront",
        local_gate="npm run build, npm run security:secrets",
        ci_gate="build and secrets",
        manual_gate="proof permission",
        blocker="proof gates",
        next_action="public-safe updates only",
    )
    _write_evidence(tmp_path, "consulting", lane="local", result="pass")
    _write_backlog(tmp_path)

    report = run_workspace_report(load_config(tmp_path))

    consulting = _repo(report, "consulting")
    assert consulting.manifest_status == "ok"
    assert consulting.evidence_status == "ok"
    assert consulting.owner_lane == "public proof/storefront"
    assert consulting.local_gate == "npm run build, npm run security:secrets"
    assert consulting.latest_verification[0].lane == "local"
    assert consulting.latest_verification[0].result == "pass"

    hub_prompts = _repo(report, "hub-prompts")
    assert hub_prompts.manifest_status == "manifest_missing"
    assert hub_prompts.evidence_status == "evidence_missing"
    assert any("Mom nonprofit" in blocker for blocker in report.blockers)
    assert any("DSE" in blocker for blocker in report.blockers)


def test_workspace_report_render_includes_boundary_and_missing_items(tmp_path: Path) -> None:
    _write_manifest(tmp_path, "FamilyTrips", repo="FamilyTrips", owner_lane="privacy-first")
    _write_backlog(tmp_path)

    report = run_workspace_report(load_config(tmp_path))
    text = render_workspace_report(report)

    assert "Workspace Command Center V0 Report" in text
    assert "Boundary: read_only_recorded_dtp_artifacts" in text
    assert "Live status: not_checked_v0_no_repo_commands_or_github_calls" in text
    assert "hub-prompts: manifest_missing, evidence_missing" in text
    assert "V0 does not execute checks, call GitHub, mutate repos" in text


def test_workspace_report_cli_outputs_text(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    _write_manifest(tmp_path, "tm-skills", repo="tm-skills", owner_lane="global SDLC skills")
    _write_evidence(tmp_path, "tm-skills", lane="local", result="pass")
    _write_backlog(tmp_path)

    result = CliRunner().invoke(app, ["workspace", "report"])

    assert result.exit_code == 0
    assert "Workspace Command Center V0 Report" in result.output
    assert "tm-skills: manifest=ok; evidence=ok" in result.output


def test_workspace_report_cli_outputs_json(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    _write_manifest(tmp_path, "tm-skills", repo="tm-skills", owner_lane="global SDLC skills")
    _write_evidence(tmp_path, "tm-skills", lane="local", result="pass")
    _write_backlog(tmp_path)

    result = CliRunner().invoke(app, ["workspace", "report", "--json"])

    assert result.exit_code == 0
    data = json.loads(result.output)
    assert data["boundary"] == "read_only_recorded_dtp_artifacts"
    assert data["live_status"] == "not_checked_v0_no_repo_commands_or_github_calls"
    assert any(repo["repo"] == "tm-skills" for repo in data["repos"])
    assert any(repo["repo"] == "hub-prompts" for repo in data["missing_coverage"])


def _write_manifest(
    root: Path,
    slug: str,
    *,
    repo: str,
    owner_lane: str,
    local_gate: str = "",
    ci_gate: str = "",
    manual_gate: str = "",
    blocker: str = "",
    next_action: str = "",
) -> None:
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
                f"- Local gate: {local_gate}",
                f"- CI gate: {ci_gate}",
                f"- Manual gate: {manual_gate}",
                "",
                "## Next Touch",
                "",
                f"- Blocker: {blocker}",
                f"- Next action: {next_action}",
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
                f"| {lane} | 2026-04-30 | {result} | abc123 | local gate |",
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
                "## Current Active Next Queue",
                "",
                "1. Collect Mom nonprofit owner-confirmed facts.",
                "2. Keep DSE blocked until the active branch is clean.",
                "3. Park routine maintenance.",
                "",
                "## Later",
            ]
        ),
    )


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _repo(report, name: str):
    return next(repo for repo in report.repos if repo.repo == name)
