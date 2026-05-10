from __future__ import annotations

import json
from collections.abc import Callable
from datetime import date
from pathlib import Path
from typing import Any

from dtp.commands.source_packs import (
    render_source_pack_dashboard,
    render_source_pack_status,
    render_source_pack_validation,
    run_source_pack_dashboard,
    run_source_pack_status,
    run_source_pack_validation,
)
from dtp.config import load_config


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
        "devops-infrastructure",
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

    devops = next(
        pack for pack in payload["packs"] if pack["role_id"] == "devops-infrastructure"
    )
    assert "production deploys" in devops["promotion_required_for"]
    assert (
        "cloud, hosting, DNS, OAuth, billing, database, CI/CD permission, webhook, "
        "integration, or secret mutation"
    ) in devops["promotion_required_for"]
    assert "production readiness claims" in devops["promotion_required_for"]
    assert any(
        source["id"] == "devops-infrastructure-source-policy-pilot"
        for source in devops["primary_sources"]
    )
    assert any(
        source["id"] == "vercel-production-checklist"
        for source in devops["primary_sources"]
    )
    assert any(
        source["id"] == "supabase-database-migrations"
        for source in devops["primary_sources"]
    )
    assert any(source["id"] == "nist-csf" for source in devops["primary_sources"])


def test_source_pack_validator_accepts_current_contract(repo_root: Path) -> None:
    result = run_source_pack_validation(load_config(repo_root))

    assert result.ok is True
    assert result.role_ids == (
        "research-steward",
        "external-communications",
        "consulting-strategy",
        "software-architecture",
        "software-engineering",
        "qa-audit",
        "devops-infrastructure",
    )
    assert any("source pack authority boundary locked" in check for check in result.checks)
    assert any("source pack packs validated: 7" in check for check in result.checks)
    assert "source-pack validation: ok" in render_source_pack_validation(
        result,
        repo_root,
    )


def test_source_pack_status_summarizes_role_freshness(repo_root: Path) -> None:
    result = run_source_pack_status(load_config(repo_root), today=date(2026, 5, 10))

    assert result.ok is True
    assert result.freshness_counts == {"current": 7}
    assert result.primary_source_count >= 7
    assert result.role_statuses[0].role_id == "research-steward"
    assert result.role_statuses[0].freshness == "current"

    rendered = render_source_pack_status(result, repo_root)
    assert "Source Pack Status" in rendered
    assert "research-steward: current" in rendered
    assert "source packs inform roles" in rendered


def test_source_pack_status_marks_stale_role(repo_root: Path, tmp_path: Path) -> None:
    def mutate(payload: dict[str, Any]) -> None:
        payload["packs"][0]["last_reviewed_at"] = "2025-01-01"

    path = _write_mutated_source_pack(repo_root, tmp_path, mutate)

    result = run_source_pack_status(
        load_config(repo_root),
        path=path,
        today=date(2026, 5, 10),
    )

    assert result.role_statuses[0].freshness == "stale"
    assert result.freshness_counts["stale"] == 1


def test_source_pack_dashboard_writes_internal_html(
    repo_root: Path,
    tmp_path: Path,
) -> None:
    result = run_source_pack_dashboard(
        load_config(repo_root),
        output_path=tmp_path / "source-pack-status-dashboard.html",
        today=date(2026, 5, 10),
    )

    assert result.validation_ok is True
    assert result.role_count == 7
    assert result.path.exists()
    assert "Source Pack Status Dashboard" in result.html
    assert "research-steward" in result.html
    assert "Source packs inform roles" in result.html

    status = run_source_pack_status(load_config(repo_root), today=date(2026, 5, 10))
    assert "current" in render_source_pack_dashboard(status, repo_root)


def test_source_pack_validator_rejects_missing_required_top_level_field(
    repo_root: Path,
    tmp_path: Path,
) -> None:
    def mutate(payload: dict[str, Any]) -> None:
        payload.pop("governing_rule")

    path = _write_mutated_source_pack(repo_root, tmp_path, mutate)

    result = run_source_pack_validation(load_config(repo_root), path=path)

    assert result.ok is False
    assert any("$ missing field: governing_rule" in problem for problem in result.problems)


def test_source_pack_validator_rejects_duplicate_role_id(
    repo_root: Path,
    tmp_path: Path,
) -> None:
    def mutate(payload: dict[str, Any]) -> None:
        payload["packs"][1]["role_id"] = payload["packs"][0]["role_id"]

    path = _write_mutated_source_pack(repo_root, tmp_path, mutate)

    result = run_source_pack_validation(load_config(repo_root), path=path)

    assert result.ok is False
    assert any("duplicate role id" in problem for problem in result.problems)


def test_source_pack_validator_rejects_incomplete_primary_source(
    repo_root: Path,
    tmp_path: Path,
) -> None:
    def mutate(payload: dict[str, Any]) -> None:
        payload["packs"][0]["primary_sources"][0].pop("evidence_limit")

    path = _write_mutated_source_pack(repo_root, tmp_path, mutate)

    result = run_source_pack_validation(load_config(repo_root), path=path)

    assert result.ok is False
    assert any("missing field: evidence_limit" in problem for problem in result.problems)


def _write_mutated_source_pack(
    repo_root: Path,
    tmp_path: Path,
    mutate: Callable[[dict[str, Any]], None],
) -> Path:
    source = (
        repo_root
        / "practice-os"
        / "research"
        / "source-packs"
        / "agent-source-packs.v0.json"
    )
    payload = json.loads(source.read_text(encoding="utf-8"))
    mutate(payload)
    path = tmp_path / "agent-source-packs.v0.json"
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path
