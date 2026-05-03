from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from claude_agent_sdk import ClaudeAgentOptions

from dtp.git_safety import make_repo_boundary_check
from dtp.skills_loader import Skill


@dataclass(frozen=True)
class AgentRequest:
    command: str
    input_text: str
    model: str
    skills: tuple[Skill, ...]
    repo_root: Path
    add_dirs: tuple[Path, ...] = ()


AgentRunner = Callable[[AgentRequest], str]


def run(request: AgentRequest, runner: AgentRunner | None = None) -> str:
    """Run the single harness agent loop.

    The harness keeps a deterministic local fallback so tests do not need API access.
    """

    if runner is not None:
        return runner(request)
    return _phase1_draft_fallback(request)


def build_agent_options(request: AgentRequest) -> ClaudeAgentOptions:
    return ClaudeAgentOptions(
        cwd=request.repo_root,
        add_dirs=list(request.add_dirs),
        model=request.model,
        skills=[skill.name for skill in request.skills],
        can_use_tool=make_repo_boundary_check(request.repo_root),
    )


def _phase1_draft_fallback(request: AgentRequest) -> str:
    skill_names = ", ".join(skill.name for skill in request.skills)
    note_preview = " ".join(request.input_text.split())[:240]
    pattern_references = _pattern_references(request)
    pattern_section = ""
    if pattern_references:
        pattern_section = (
            "\n## Pattern References\n\n"
            + "\n".join(f"- `{path}`" for path in pattern_references)
            + "\n"
        )
    return (
        "# Draft SOW\n\n"
        "## Scope\n\n"
        f"Phase 1 draft generated from the diagnose note. Skills loaded: {skill_names}.\n\n"
        f"Source signal: {note_preview}\n\n"
        f"{pattern_section}"
        "## Deliverables\n\n"
        "- Diagnose the current operating constraint.\n"
        "- Define the first useful artifact.\n"
        "- Package the work into a handoff Toni can refine.\n\n"
        "## Pricing\n\n"
        "Pricing is a placeholder until Toni authors the pricing skill.\n"
    )


def _pattern_references(request: AgentRequest) -> tuple[str, ...]:
    if "build-patterns" not in {skill.name for skill in request.skills}:
        return ()

    synthesis_dir = request.repo_root / "extracts" / "synthesis"
    if not synthesis_dir.exists():
        return ()

    query_terms = _terms(request.input_text)
    matches: list[str] = []
    for path in sorted(synthesis_dir.glob("*.md")):
        relative = path.relative_to(request.repo_root).as_posix()
        text = f"{relative}\n{path.read_text(encoding='utf-8', errors='ignore')}"
        if query_terms and query_terms.intersection(_terms(text)):
            matches.append(relative)
    return tuple(matches[:5])


def _terms(value: str) -> set[str]:
    stop_words = {
        "and",
        "for",
        "from",
        "into",
        "that",
        "the",
        "this",
        "with",
        "without",
    }
    return {
        term
        for term in "".join(char.lower() if char.isalnum() else " " for char in value).split()
        if len(term) >= 4 and term not in stop_words
    }
