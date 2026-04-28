from __future__ import annotations

from pathlib import Path

from dtp.agent import AgentRequest, build_agent_options
from dtp.skills_loader import Skill


def test_agent_options_include_repo_boundary_callback(repo_root: Path) -> None:
    skill = Skill(
        name="voice",
        description="Voice skill.",
        path=repo_root / "skills" / "voice" / "SKILL.md",
        body="# TODO: Toni authors this skill",
    )
    request = AgentRequest(
        command="draft",
        input_text="diagnose note",
        model="claude-sonnet-4-6",
        skills=(skill,),
        repo_root=repo_root,
    )

    options = build_agent_options(request)

    assert options.cwd == repo_root
    assert options.model == "claude-sonnet-4-6"
    assert options.skills == ["voice"]
    assert options.can_use_tool is not None
