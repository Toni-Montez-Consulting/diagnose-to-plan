from __future__ import annotations

import json
from pathlib import Path


def test_consulting_intelligence_eval_seed_is_safe_and_complete(repo_root: Path) -> None:
    path = repo_root / "practice-os" / "fixtures" / "consulting-intelligence" / "eval-cases.json"
    data = json.loads(path.read_text(encoding="utf-8"))

    families = {case["family"] for case in data["cases"]}

    assert data["data_class"] == "P0"
    assert data["permission_level"] == "internal_only"
    assert len(data["cases"]) >= 6
    assert {
        "diagnosis_quality",
        "proof_safety",
        "follow_up_quality",
        "handoff_quality",
        "coi_permission_routing",
        "evidence_dossier_depth",
    }.issubset(families)
    assert any(case.get("seeded_from_misfire") for case in data["cases"])

    raw_text = path.read_text(encoding="utf-8").lower()
    for blocked in ("gmail_message_id", "gmail_thread_id", "tax returns", "ein records"):
        assert blocked not in raw_text
