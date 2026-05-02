from __future__ import annotations

from pathlib import Path

from dtp.commands.practice import run_practice_doctor
from dtp.config import load_config


def test_practice_doctor_passes_repo_contract(repo_root: Path) -> None:
    result = run_practice_doctor(load_config(repo_root))

    assert result.ok is True
    assert any("policy data-classification.md" in check for check in result.checks)
    assert any("template activation-routing-map.md" in check for check in result.checks)
    assert any("template agentic-performance-gap-review.md" in check for check in result.checks)
    assert any("template contextual-idea-intake.md" in check for check in result.checks)
    assert any("template roadmap-steward-review.md" in check for check in result.checks)
    assert any("template story-activation-contract.md" in check for check in result.checks)
    assert any("template client-command-room-fit-assessment.md" in check for check in result.checks)
    assert any("template client-command-room-spec.md" in check for check in result.checks)
    assert any("template recurring-engagement-cadence.md" in check for check in result.checks)
    assert any("template client-reply-intake.md" in check for check in result.checks)
    assert any("template custom-interface-craft-brief.md" in check for check in result.checks)
    assert any("practice skill diagnose" in check for check in result.checks)
