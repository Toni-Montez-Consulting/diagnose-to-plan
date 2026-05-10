from __future__ import annotations

from pathlib import Path

from dtp.commands.practice import run_practice_doctor
from dtp.config import load_config


def test_practice_doctor_passes_repo_contract(repo_root: Path) -> None:
    result = run_practice_doctor(load_config(repo_root))

    assert result.ok is True
    assert any("policy authentic-voice-and-anti-slop.md" in check for check in result.checks)
    assert any("policy data-classification.md" in check for check in result.checks)
    assert any("template activation-routing-map.md" in check for check in result.checks)
    assert any("template agentic-performance-gap-review.md" in check for check in result.checks)
    assert any("template copy-authenticity-audit.md" in check for check in result.checks)
    assert any("template contextual-idea-intake.md" in check for check in result.checks)
    assert any("template roadmap-steward-review.md" in check for check in result.checks)
    assert any("template story-activation-contract.md" in check for check in result.checks)
    assert any("template client-command-room-fit-assessment.md" in check for check in result.checks)
    assert any("template client-command-room-spec.md" in check for check in result.checks)
    assert any("template client-os-bridge-queue.md" in check for check in result.checks)
    assert any("template client-os-build-task.md" in check for check in result.checks)
    assert any("template client-os-chain-run.md" in check for check in result.checks)
    assert any("template client-os-meeting-brief.md" in check for check in result.checks)
    assert any("template client-os-meeting-notes.md" in check for check in result.checks)
    assert any("template client-os-pilot-packet.md" in check for check in result.checks)
    assert any("template client-os-post-meeting-receipt.md" in check for check in result.checks)
    assert any("template recurring-engagement-cadence.md" in check for check in result.checks)
    assert any("template client-reply-intake.md" in check for check in result.checks)
    assert any("template custom-interface-craft-brief.md" in check for check in result.checks)
    assert any("template session-rehydration-checklist.md" in check for check in result.checks)
    assert any("template memory-review-queue.md" in check for check in result.checks)
    assert any("template notion-cockpit-audit.md" in check for check in result.checks)
    assert any("template correction-checklist-for-toni.md" in check for check in result.checks)
    assert any(
        "template business-brain-weekly-operating-packet.md" in check
        for check in result.checks
    )
    assert any("template knowledge-base-event-record.md" in check for check in result.checks)
    assert any("template research-decision-record.md" in check for check in result.checks)
    assert any("doc PRACTICE_KAIZEN_KANBAN_SYSTEM.md" in check for check in result.checks)
    assert any("doc RESEARCH_ARM_SOURCE_LIST_V0.md" in check for check in result.checks)
    assert any("doc KNOWLEDGE_BASE_EVENT_WORKFLOWS_V0.md" in check for check in result.checks)
    assert any("kaizen README.md" in check for check in result.checks)
    assert any("kaizen intake.jsonl" in check for check in result.checks)
    assert any("practice skill diagnose" in check for check in result.checks)
