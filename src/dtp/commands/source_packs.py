"""Validation helpers for Practice OS agent source packs."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from dtp.config import DtpConfig

DEFAULT_SOURCE_PACK_PATH = Path(
    "practice-os/research/source-packs/agent-source-packs.v0.json"
)
EXPECTED_SCHEMA_VERSION = "agent-source-packs.v0"
EXPECTED_EVIDENCE_TIERS = {0, 1, 2, 3, 4}


@dataclass(frozen=True)
class SourcePackValidationResult:
    """Result returned by the source-pack validator."""

    ok: bool
    path: Path
    checks: tuple[str, ...]
    problems: tuple[str, ...]
    role_ids: tuple[str, ...]


def run_source_pack_validation(
    config: DtpConfig,
    *,
    path: Path | None = None,
) -> SourcePackValidationResult:
    """Validate the agent source-pack contract without external dependencies."""

    repo_root = config.repo_root
    source_pack_path = _resolve_path(repo_root, path or DEFAULT_SOURCE_PACK_PATH)
    checks: list[str] = []
    problems: list[str] = []
    role_ids: list[str] = []

    display_path = _display_path(repo_root, source_pack_path)
    if not source_pack_path.exists():
        problems.append(f"missing source pack file: {display_path}")
        return SourcePackValidationResult(
            ok=False,
            path=source_pack_path,
            checks=tuple(checks),
            problems=tuple(problems),
            role_ids=tuple(role_ids),
        )
    checks.append(f"source pack schema file exists: {display_path}")

    try:
        payload = json.loads(source_pack_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        problems.append(f"invalid JSON in source pack: {exc.msg} at line {exc.lineno}")
        return SourcePackValidationResult(
            ok=False,
            path=source_pack_path,
            checks=tuple(checks),
            problems=tuple(problems),
            role_ids=tuple(role_ids),
        )

    root = _expect_mapping(payload, "$", problems)
    if root is None:
        return SourcePackValidationResult(
            ok=False,
            path=source_pack_path,
            checks=tuple(checks),
            problems=tuple(problems),
            role_ids=tuple(role_ids),
        )

    schema_version = _require_non_empty_str(root, "schema_version", "$", problems)
    if schema_version == EXPECTED_SCHEMA_VERSION:
        checks.append(f"source pack schema version: {EXPECTED_SCHEMA_VERSION}")
    elif schema_version:
        problems.append(
            "$.schema_version expected "
            f"{EXPECTED_SCHEMA_VERSION!r}, found {schema_version!r}"
        )

    for key in (
        "review_status",
        "owner_repo",
        "created_at",
        "updated_at",
        "policy_doc",
        "governing_rule",
    ):
        _require_non_empty_str(root, key, "$", problems)

    policy_doc = root.get("policy_doc")
    if isinstance(policy_doc, str) and policy_doc.strip():
        policy_doc_path = repo_root / policy_doc
        if policy_doc_path.exists():
            checks.append(f"source pack policy doc exists: {policy_doc}")
        else:
            problems.append(f"$.policy_doc points to missing file: {policy_doc}")

    _validate_authority_boundary(root, checks, problems)
    evidence_tiers = _validate_evidence_tiers(root, checks, problems)
    _validate_packs(root, repo_root, evidence_tiers, role_ids, checks, problems)

    return SourcePackValidationResult(
        ok=not problems,
        path=source_pack_path,
        checks=tuple(checks),
        problems=tuple(problems),
        role_ids=tuple(role_ids),
    )


def render_source_pack_validation(
    result: SourcePackValidationResult,
    repo_root: Path,
) -> str:
    """Render a validation result for CLI output."""

    status = "ok" if result.ok else "failed"
    lines = [f"source-pack validation: {status}"]
    lines.append(f"path: {_display_path(repo_root, result.path)}")

    if result.checks:
        lines.append("")
        lines.append("checks:")
        for check in result.checks:
            lines.append(f"- {check}")

    if result.role_ids:
        lines.append("")
        lines.append("roles:")
        for role_id in result.role_ids:
            lines.append(f"- {role_id}")

    if result.problems:
        lines.append("")
        lines.append("problems:")
        for problem in result.problems:
            lines.append(f"- {problem}")

    return "\n".join(lines) + "\n"


def _validate_authority_boundary(
    root: dict[str, Any],
    checks: list[str],
    problems: list[str],
) -> None:
    boundary = _require_mapping(root, "authority_boundary", "$", problems)
    if boundary is None:
        return

    expected_flags = {
        "adds_authority": False,
        "allows_web_search": True,
        "allows_autonomous_actions": False,
        "requires_human_promotion": True,
    }
    for key, expected in expected_flags.items():
        value = boundary.get(key)
        if value is expected:
            continue
        if key not in boundary:
            problems.append(f"$.authority_boundary missing field: {key}")
        else:
            problems.append(
                f"$.authority_boundary.{key} expected {expected!r}, found {value!r}"
            )

    if not any(problem.startswith("$.authority_boundary") for problem in problems):
        checks.append("source pack authority boundary locked")


def _validate_evidence_tiers(
    root: dict[str, Any],
    checks: list[str],
    problems: list[str],
) -> set[int]:
    tiers = _require_non_empty_list(root, "evidence_tiers", "$", problems)
    found: set[int] = set()
    if tiers is None:
        return found

    for index, item in enumerate(tiers):
        pointer = f"$.evidence_tiers[{index}]"
        tier = _expect_mapping(item, pointer, problems)
        if tier is None:
            continue
        tier_value = tier.get("tier")
        if isinstance(tier_value, int):
            found.add(tier_value)
        else:
            problems.append(f"{pointer}.tier must be an integer")
        _require_non_empty_str(tier, "label", pointer, problems)
        _require_non_empty_str(tier, "confidence_posture", pointer, problems)

    if found == EXPECTED_EVIDENCE_TIERS:
        checks.append("source pack evidence tiers: 0-4")
    else:
        problems.append(
            "$.evidence_tiers expected tiers "
            f"{sorted(EXPECTED_EVIDENCE_TIERS)}, found {sorted(found)}"
        )

    return found


def _validate_packs(
    root: dict[str, Any],
    repo_root: Path,
    evidence_tiers: set[int],
    role_ids: list[str],
    checks: list[str],
    problems: list[str],
) -> None:
    packs = _require_non_empty_list(root, "packs", "$", problems)
    if packs is None:
        return

    seen_roles: set[str] = set()
    for index, item in enumerate(packs):
        pointer = f"$.packs[{index}]"
        pack = _expect_mapping(item, pointer, problems)
        if pack is None:
            continue

        role_id = _require_non_empty_str(pack, "role_id", pointer, problems)
        if role_id:
            role_ids.append(role_id)
            if role_id in seen_roles:
                problems.append(f"{pointer}.role_id duplicate role id: {role_id}")
            seen_roles.add(role_id)

        for key in (
            "role_name",
            "source_pack_version",
            "status",
            "last_reviewed_at",
            "next_review_trigger",
        ):
            _require_non_empty_str(pack, key, pointer, problems)

        _require_string_list(pack, "allowed_web_sources", pointer, problems)
        _require_string_list(pack, "blocked_sources", pointer, problems)
        _require_string_list(pack, "default_outputs", pointer, problems)
        _require_string_list(pack, "promotion_required_for", pointer, problems)

        pilot_artifacts = _require_string_list(
            pack,
            "pilot_artifacts",
            pointer,
            problems,
        )
        if pilot_artifacts:
            _validate_local_artifacts(
                repo_root,
                pilot_artifacts,
                f"{pointer}.pilot_artifacts",
                problems,
            )

        _validate_primary_sources(pack, pointer, evidence_tiers, problems)
        _validate_search_posture(pack, pointer, problems)

    if len(role_ids) == len(seen_roles) and role_ids:
        checks.append("source pack role ids unique")
    checks.append(f"source pack packs validated: {len(role_ids)}")


def _validate_primary_sources(
    pack: dict[str, Any],
    pointer: str,
    evidence_tiers: set[int],
    problems: list[str],
) -> None:
    sources = _require_non_empty_list(pack, "primary_sources", pointer, problems)
    if sources is None:
        return

    seen_sources: set[str] = set()
    for index, item in enumerate(sources):
        source_pointer = f"{pointer}.primary_sources[{index}]"
        source = _expect_mapping(item, source_pointer, problems)
        if source is None:
            continue

        source_id = _require_non_empty_str(source, "id", source_pointer, problems)
        if source_id:
            if source_id in seen_sources:
                problems.append(
                    f"{source_pointer}.id duplicate primary source id: {source_id}"
                )
            seen_sources.add(source_id)

        tier = source.get("tier")
        if not isinstance(tier, int):
            problems.append(f"{source_pointer}.tier must be an integer")
        elif evidence_tiers and tier not in evidence_tiers:
            problems.append(f"{source_pointer}.tier references unknown tier: {tier}")

        for key in ("type", "path_or_url", "use", "evidence_limit"):
            _require_non_empty_str(source, key, source_pointer, problems)


def _validate_search_posture(
    pack: dict[str, Any],
    pointer: str,
    problems: list[str],
) -> None:
    posture = _require_mapping(pack, "search_posture", pointer, problems)
    if posture is None:
        return

    _require_non_empty_str(posture, "default", f"{pointer}.search_posture", problems)
    _require_non_empty_str(
        posture,
        "broad_web_confidence",
        f"{pointer}.search_posture",
        problems,
    )
    _require_string_list(
        posture,
        "preferred_queries",
        f"{pointer}.search_posture",
        problems,
    )


def _validate_local_artifacts(
    repo_root: Path,
    artifacts: list[str],
    pointer: str,
    problems: list[str],
) -> None:
    for index, artifact in enumerate(artifacts):
        if artifact.startswith(("http://", "https://")):
            continue
        artifact_path = repo_root / artifact
        if not artifact_path.exists():
            problems.append(f"{pointer}[{index}] points to missing file: {artifact}")


def _require_mapping(
    mapping: dict[str, Any],
    key: str,
    pointer: str,
    problems: list[str],
) -> dict[str, Any] | None:
    if key not in mapping:
        problems.append(f"{pointer} missing field: {key}")
        return None
    return _expect_mapping(mapping[key], f"{pointer}.{key}", problems)


def _expect_mapping(
    value: Any,
    pointer: str,
    problems: list[str],
) -> dict[str, Any] | None:
    if isinstance(value, dict):
        return value
    problems.append(f"{pointer} must be an object")
    return None


def _require_non_empty_list(
    mapping: dict[str, Any],
    key: str,
    pointer: str,
    problems: list[str],
) -> list[Any] | None:
    if key not in mapping:
        problems.append(f"{pointer} missing field: {key}")
        return None
    value = mapping[key]
    if not isinstance(value, list):
        problems.append(f"{pointer}.{key} must be a list")
        return None
    if not value:
        problems.append(f"{pointer}.{key} must not be empty")
        return None
    return value


def _require_string_list(
    mapping: dict[str, Any],
    key: str,
    pointer: str,
    problems: list[str],
) -> list[str] | None:
    values = _require_non_empty_list(mapping, key, pointer, problems)
    if values is None:
        return None

    strings: list[str] = []
    for index, value in enumerate(values):
        if isinstance(value, str) and value.strip():
            strings.append(value)
        else:
            problems.append(f"{pointer}.{key}[{index}] must be a non-empty string")
    return strings


def _require_non_empty_str(
    mapping: dict[str, Any],
    key: str,
    pointer: str,
    problems: list[str],
) -> str | None:
    if key not in mapping:
        problems.append(f"{pointer} missing field: {key}")
        return None
    value = mapping[key]
    if isinstance(value, str) and value.strip():
        return value
    problems.append(f"{pointer}.{key} must be a non-empty string")
    return None


def _resolve_path(repo_root: Path, path: Path) -> Path:
    if path.is_absolute():
        return path
    return repo_root / path


def _display_path(repo_root: Path, path: Path) -> str:
    try:
        return path.relative_to(repo_root).as_posix()
    except ValueError:
        return str(path)
