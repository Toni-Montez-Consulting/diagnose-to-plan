from __future__ import annotations

from pathlib import Path

from dtp.commands.kit import run_kit_new
from dtp.commands.web import build_workbench_state, render_workbench_html
from dtp.config import DtpConfig


def test_workbench_state_reports_kits_and_contracts(tmp_path: Path) -> None:
    config = _config(tmp_path)
    _seed_practice_os(config)
    run_kit_new(config=config, client="Mom Nonprofit", project="site-rebuild", kind="launch")

    state = build_workbench_state(config)

    assert state["contracts"]["storage"] == "markdown-first"
    assert state["engagements"]["kits"][0]["client_id"] == "mom-nonprofit"
    assert state["engagements"]["kits"][0]["redaction_ready"] is False
    assert state["vault"]["ready"] is False


def test_workbench_html_renders_primary_actions(tmp_path: Path) -> None:
    config = _config(tmp_path)
    _seed_practice_os(config)

    html = render_workbench_html(build_workbench_state(config))

    assert "DTP Workbench" in html
    assert "Create a kit" in html
    assert "Private vault" in html
    assert "Redaction check" in html


def _seed_practice_os(config: DtpConfig) -> None:
    for folder, name in (
        ("policies", "data-classification.md"),
        ("templates", "diagnose-memo.md"),
        ("patterns", "index.md"),
    ):
        path = config.practice_os_dir / folder
        path.mkdir(parents=True, exist_ok=True)
        (path / name).write_text("# Seed\n", encoding="utf-8")


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
        agent_enabled=False,
    )
