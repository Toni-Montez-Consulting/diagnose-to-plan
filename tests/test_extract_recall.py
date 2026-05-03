from __future__ import annotations

import json
from pathlib import Path

from dtp.capture import render_markdown_with_frontmatter
from dtp.config import DtpConfig
from dtp.extract.recall import rebuild_recall_index, recall, results_to_json


def test_recall_ranking_filters_and_json_output(tmp_path: Path) -> None:
    config = _config(tmp_path)
    patterns = config.extracts_dir / "patterns"
    lessons = config.extracts_dir / "lessons"
    patterns.mkdir(parents=True)
    lessons.mkdir(parents=True)
    (patterns / "consulting--admin-command-room.md").write_text(
        render_markdown_with_frontmatter(
            {
                "repo": "consulting",
                "signal": "admin-surface",
                "pattern_slug": "admin-command-room",
                "detected_at": "2026-04-28T10:00:00Z",
                "promoted": False,
            },
            "# Admin Command Room\n\nadmin admin command room for consulting /admin.",
        ),
        encoding="utf-8",
    )
    (patterns / "hub--admin-console.md").write_text(
        render_markdown_with_frontmatter(
            {
                "repo": "hub",
                "signal": "admin-surface",
                "pattern_slug": "admin-console",
                "detected_at": "2026-04-28T10:00:00Z",
                "promoted": False,
            },
            "# Admin Console\n\nHub console pattern evidence for admin operations.",
        ),
        encoding="utf-8",
    )
    (lessons / "consulting--2026-04-28-admin-surface.md").write_text(
        render_markdown_with_frontmatter(
            {
                "repo": "consulting",
                "pattern": "admin-surface",
                "type": "decision",
                "created": "2026-04-28T11:00:00Z",
            },
            "# Consulting Admin Decision\n\nKeep private rows in Hub.",
        ),
        encoding="utf-8",
    )
    synthesis = config.extracts_dir / "synthesis"
    synthesis.mkdir(parents=True)
    (synthesis / "admin-surface.md").write_text(
        render_markdown_with_frontmatter(
            {
                "group": "admin-surface",
                "canonical_repo": "consulting",
                "canonical_repos": ["consulting", "hub"],
                "synthesized_at": "2026-04-28T12:00:00Z",
            },
            "# Admin Surface\n\nadmin synthesis for command rooms.",
        ),
        encoding="utf-8",
    )

    rebuild_recall_index(config)
    pattern_results = recall(config=config, query="admin", kind="pattern")
    decision_results = recall(config=config, query="private", kind="decision", repo="consulting")
    synthesis_results = recall(config=config, query="admin", kind="synthesis")
    hub_synthesis_results = recall(config=config, query="admin", kind="synthesis", repo="hub")
    recent_results = recall(config=config, query="admin", since="2026-04-28")

    assert [result.type for result in pattern_results] == ["pattern", "pattern"]
    assert {result.repo for result in pattern_results} == {"consulting", "hub"}
    assert pattern_results[0].score >= pattern_results[1].score
    assert len(decision_results) == 1
    assert decision_results[0].type == "decision"
    assert len(synthesis_results) == 1
    assert synthesis_results[0].type == "synthesis"
    assert len(hub_synthesis_results) == 1
    assert hub_synthesis_results[0].metadata["canonical_repos"] == ["consulting", "hub"]
    assert len(recent_results) == 4

    payload = json.loads(results_to_json(pattern_results))
    assert payload[0]["path"].startswith("extracts/patterns/")
    assert payload[0]["type"] == "pattern"


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
