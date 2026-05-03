from __future__ import annotations

from pathlib import Path

from dtp.commands.redact import run_redact_check
from dtp.config import DtpConfig


def test_redact_check_passes_clean_practice_artifact(tmp_path: Path) -> None:
    config = _config(tmp_path)
    path = tmp_path / "practice-os" / "patterns" / "clean.md"
    path.parent.mkdir(parents=True)
    path.write_text(
        "---\ndata_class: P1\nconfidential: false\npermission_level: internal_only\n"
        "review_status: reviewed\n---\n# Clean\n\nRedacted workflow category only.\n",
        encoding="utf-8",
    )

    assert run_redact_check(config=config, path=path, profile="practice") == ()


def test_redact_check_blocks_secrets_and_private_practice_data(tmp_path: Path) -> None:
    config = _config(tmp_path)
    path = tmp_path / "practice-os" / "patterns" / "unsafe.md"
    path.parent.mkdir(parents=True)
    path.write_text(
        "---\ndata_class: P2\nconfidential: true\npermission_level: internal_only\n"
        "review_status: draft\n---\n# Unsafe\n\nAPI key sk-ant-1234567890abcdef\n",
        encoding="utf-8",
    )

    findings = run_redact_check(config=config, path=path, profile="practice")

    assert any("possible secret" in finding.message for finding in findings)
    assert any("P2 material" in finding.message for finding in findings)
    assert any("confidential artifact" in finding.message for finding in findings)


def test_case_study_requires_external_permission_and_review(tmp_path: Path) -> None:
    config = _config(tmp_path)
    path = tmp_path / "engagements" / "fake" / "case-study" / "redacted.md"
    path.parent.mkdir(parents=True)
    path.write_text(
        "---\ndata_class: P1\nconfidential: false\npermission_level: internal_only\n"
        "review_status: draft\n---\n# Case\n\n## Claim\n\n## Evidence source\n\n"
        "## Baseline\n\n## After\n\n## Measurement caveats\n\n## Permission level\n\n"
        "## Redaction status\n\n## Reviewer\n\n",
        encoding="utf-8",
    )

    findings = run_redact_check(config=config, path=path, profile="case-study")

    assert any("internal_only" in finding.message for finding in findings)
    assert any("has not passed" in finding.message for finding in findings)


def _config(root: Path) -> DtpConfig:
    return DtpConfig(
        repo_root=root,
        inputs_dir=root / "inputs",
        outputs_dir=root / "outputs",
        skills_dir=root / "skills",
        extracts_dir=root / "extracts",
        practice_os_dir=root / "practice-os",
        engagements_dir=root / "engagements",
        workspace_file=root / ".dtp" / "workspace.yaml",
        agent_enabled=False,
    )
