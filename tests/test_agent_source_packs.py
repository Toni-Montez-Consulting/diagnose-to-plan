from __future__ import annotations

import json
from pathlib import Path


def test_agent_source_packs_v0_contract(repo_root: Path) -> None:
    path = repo_root / "practice-os" / "research" / "source-packs" / "agent-source-packs.v0.json"
    payload = json.loads(path.read_text(encoding="utf-8"))

    assert payload["schema_version"] == "agent-source-packs.v0"
    assert payload["authority_boundary"]["adds_authority"] is False
    assert payload["authority_boundary"]["allows_web_search"] is True
    assert payload["authority_boundary"]["allows_autonomous_actions"] is False
    assert payload["authority_boundary"]["requires_human_promotion"] is True
    assert payload["governing_rule"] == (
        "Search can inform every agent. Search cannot authorize action by itself."
    )

    role_ids = {pack["role_id"] for pack in payload["packs"]}
    assert role_ids == {
        "research-steward",
        "external-communications",
        "consulting-strategy",
        "software-architecture",
        "software-engineering",
        "qa-audit",
    }

    for pack in payload["packs"]:
        assert pack["status"] == "pilot_proven"
        assert pack["source_pack_version"]
        assert pack["last_reviewed_at"] == "2026-05-10"
        assert pack["pilot_artifacts"]
        assert pack["primary_sources"]
        assert pack["allowed_web_sources"]
        assert pack["search_posture"]["broad_web_confidence"]
        assert pack["blocked_sources"]
        assert pack["default_outputs"]
        assert pack["promotion_required_for"]
        assert pack["next_review_trigger"]

    external_comms = next(
        pack for pack in payload["packs"] if pack["role_id"] == "external-communications"
    )
    assert "sending" in external_comms["promotion_required_for"]
    assert "Gmail draft creation unless Toni asks" in external_comms["promotion_required_for"]

    consulting_strategy = next(
        pack for pack in payload["packs"] if pack["role_id"] == "consulting-strategy"
    )
    assert "public offer copy" in consulting_strategy["promotion_required_for"]
    assert any(
        source["id"] == "offer-strategy-source-policy-pilot"
        for source in consulting_strategy["primary_sources"]
    )

    software_architecture = next(
        pack for pack in payload["packs"] if pack["role_id"] == "software-architecture"
    )
    assert "runtime behavior" in software_architecture["promotion_required_for"]
    assert "schema or migration changes" in software_architecture["promotion_required_for"]
    assert any(
        source["id"] == "software-architecture-source-policy-pilot"
        for source in software_architecture["primary_sources"]
    )
    assert any(
        source["id"] == "vercel-production-checklist"
        for source in software_architecture["primary_sources"]
    )

    software_engineering = next(
        pack for pack in payload["packs"] if pack["role_id"] == "software-engineering"
    )
    assert "production writes" in software_engineering["promotion_required_for"]
    assert "deploys" in software_engineering["promotion_required_for"]
    assert "cross-repo orchestration" in software_engineering["promotion_required_for"]
    assert any(
        source["id"] == "software-engineering-source-policy-pilot"
        for source in software_engineering["primary_sources"]
    )
    assert any(
        source["id"] == "github-actions-workflow-syntax"
        for source in software_engineering["primary_sources"]
    )
    assert any(
        source["id"] == "pytest-getting-started"
        for source in software_engineering["primary_sources"]
    )

    qa_audit = next(pack for pack in payload["packs"] if pack["role_id"] == "qa-audit")
    assert "production release approval" in qa_audit["promotion_required_for"]
    assert "public proof movement" in qa_audit["promotion_required_for"]
    assert "client-facing claims or communication" in qa_audit["promotion_required_for"]
    assert any(
        source["id"] == "qa-audit-source-policy-pilot"
        for source in qa_audit["primary_sources"]
    )
    assert any(
        source["id"] == "playwright-best-practices"
        for source in qa_audit["primary_sources"]
    )
    assert any(
        source["id"] == "owasp-wstg" for source in qa_audit["primary_sources"]
    )
    assert any(source["id"] == "wcag-22" for source in qa_audit["primary_sources"])
