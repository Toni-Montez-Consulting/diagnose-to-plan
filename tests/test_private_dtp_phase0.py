from __future__ import annotations

import json
from pathlib import Path


def test_private_dtp_phase0_schema_has_core_tables_and_rls(repo_root: Path) -> None:
    sql = (
        repo_root
        / "apps"
        / "private-dtp"
        / "supabase"
        / "migrations"
        / "0001_private_dtp_phase0.sql"
    ).read_text(encoding="utf-8")

    for table in (
        "private_dtp_engagements",
        "private_dtp_artifacts",
        "private_dtp_artifact_versions",
        "private_dtp_evidence_runs",
        "private_dtp_redaction_reviews",
        "private_dtp_proof_candidates",
        "private_dtp_decisions",
        "private_dtp_steward_items",
        "private_dtp_research_items",
        "private_dtp_import_export_receipts",
    ):
        assert f"create table if not exists {table}" in sql
        assert f"alter table {table} enable row level security" in sql

    assert "operator_id uuid not null default auth.uid()" in sql
    assert "with check (operator_id = auth.uid())" in sql
    assert "foreign key (engagement_id, operator_id)" in sql
    assert "foreign key (artifact_id, operator_id)" in sql
    assert "status <> 'approved'" in sql
    assert "create index if not exists private_dtp_proof_candidates_queue_idx" in sql
    assert "create index if not exists private_dtp_evidence_runs_repo_lane_idx" in sql
    assert "on delete set null" not in sql.lower()


def test_private_dtp_phase0_app_shell_names_required_screens(repo_root: Path) -> None:
    path = repo_root / "apps" / "private-dtp" / "src" / "screens.json"
    data = json.loads(path.read_text(encoding="utf-8"))

    screen_ids = {screen["id"] for screen in data["screens"]}

    assert data["operatorModel"] == "single-operator-private"
    assert {
        "engagements",
        "engagement_detail",
        "artifact_inventory",
        "evidence",
        "redaction_queue",
        "proof_queue",
        "decisions",
    }.issubset(screen_ids)


def test_private_dtp_phase01_has_deployable_app_contract(repo_root: Path) -> None:
    app_root = repo_root / "apps" / "private-dtp"
    package = json.loads((app_root / "package.json").read_text(encoding="utf-8"))
    app_source = (app_root / "src" / "App.tsx").read_text(encoding="utf-8")
    import_export = (app_root / "src" / "importExport.ts").read_text(encoding="utf-8")

    assert package["scripts"]["build"] == "tsc --noEmit && vite build"
    assert package["scripts"]["test"] == "vitest run"
    assert "@supabase/supabase-js" in package["dependencies"]
    assert "VITE_SUPABASE_URL" in (app_root / ".env.example").read_text(encoding="utf-8")
    assert "signInWithPassword" in app_source
    assert "private_dtp_import_export_receipts" in app_source
    assert "validateProofApproval" in import_export
    assert "raw private logs" in import_export.lower()
