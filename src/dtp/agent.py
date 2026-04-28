from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from dtp.skills_loader import Skill


@dataclass(frozen=True)
class AgentRequest:
    command: str
    input_text: str
    model: str
    skills: tuple[Skill, ...]


AgentRunner = Callable[[AgentRequest], str]


def run(request: AgentRequest, runner: AgentRunner | None = None) -> str:
    """Run the single harness agent loop.

    Phase 1 keeps a deterministic local fallback so the harness can be tested before Toni
    authors the real skills or connects an API key.
    """

    if runner is not None:
        return runner(request)
    return _phase1_draft_fallback(request)


def _phase1_draft_fallback(request: AgentRequest) -> str:
    skill_names = ", ".join(skill.name for skill in request.skills)
    note_preview = " ".join(request.input_text.split())[:240]
    return (
        "# Draft SOW\n\n"
        "## Scope\n\n"
        f"Phase 1 draft generated from the diagnose note. Skills loaded: {skill_names}.\n\n"
        f"Source signal: {note_preview}\n\n"
        "## Deliverables\n\n"
        "- Diagnose the current operating constraint.\n"
        "- Define the first useful artifact.\n"
        "- Package the work into a handoff Toni can refine.\n\n"
        "## Pricing\n\n"
        "Pricing is a placeholder until Toni authors the pricing skill.\n"
    )
