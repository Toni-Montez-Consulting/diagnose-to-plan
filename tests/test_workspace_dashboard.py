from __future__ import annotations

from pathlib import Path

from typer.testing import CliRunner

from dtp.cli import app
from dtp.commands.kaizen import run_kaizen_capture
from dtp.commands.workspace_dashboard import (
    DashboardSurface,
    read_proof_queue,
    run_workspace_dashboard,
)
from dtp.config import load_config


def test_workspace_dashboard_writes_viewable_html(tmp_path: Path) -> None:
    _write_manifest(tmp_path, "consulting", repo="consulting", owner_lane="public site")
    _write_evidence(tmp_path, "consulting", lane="local", result="pass")
    _write_backlog(tmp_path)
    _write_proof_queue(tmp_path)
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

    result = run_workspace_dashboard(config)

    assert result.path == tmp_path / "docs" / "workspace-dashboard.html"
    assert result.path.exists()
    assert "Practice Work Dashboard" in result.html
    assert "Omnexus subscription review needs resubmission." in result.html
    assert "Repo Coverage" in result.html
    assert "Proof Queue" in result.html
    assert "DeMario launch-feedback social packet" in result.html
    assert result.active_item_count == 1
    assert result.proof_candidate_count == 1


def test_read_proof_queue_parses_current_candidates(tmp_path: Path) -> None:
    _write_proof_queue(tmp_path)

    rows = read_proof_queue(load_config(tmp_path))

    assert len(rows) == 1
    assert rows[0].candidate == "DeMario launch-feedback social packet"
    assert rows[0].status == "candidate_intake"


def test_workspace_dashboard_cli_writes_default_output(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    _write_manifest(tmp_path, "tm-skills", repo="tm-skills", owner_lane="skills")
    _write_evidence(tmp_path, "tm-skills", lane="local", result="pass")
    _write_backlog(tmp_path)

    result = CliRunner().invoke(app, ["workspace", "dashboard"])

    assert result.exit_code == 0
    assert "workspace dashboard written" in result.output
    assert (tmp_path / "docs" / "workspace-dashboard.html").exists()


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


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
