from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from dtp.config import DtpConfig
from dtp.frontmatter_utils import split_frontmatter
from dtp.git_safety import resolve_inside_repo

REDACT_PROFILES = {"practice", "client", "case-study"}
SECRET_PATTERNS = {
    "anthropic/openai style key": re.compile(r"\bsk-(?:ant|proj|live|test)-[A-Za-z0-9_-]{12,}"),
    "aws access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "jwt-like token": re.compile(
        r"\beyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b"
    ),
    "supabase service role": re.compile(
        r"SUPABASE_SERVICE_ROLE\s*=|service[_-]?role\s*[:=]",
        re.I,
    ),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}
IDENTIFIER_PATTERNS = {
    "email address": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "phone number": re.compile(r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}\b"),
}
FINANCIAL_PATTERN = re.compile(r"\$\s?\d[\d,]*(?:\.\d{2})?")


class RedactionError(ValueError):
    pass


@dataclass(frozen=True)
class RedactionFinding:
    path: Path
    message: str


def run_redact_check(
    *,
    config: DtpConfig,
    path: Path,
    profile: str,
) -> tuple[RedactionFinding, ...]:
    normalized = profile.strip().lower()
    if normalized not in REDACT_PROFILES:
        raise RedactionError(f"unknown redaction profile: {profile}")

    target = resolve_inside_repo(path, config.repo_root)
    if not target.exists():
        raise RedactionError(f"path not found: {target}")

    findings: list[RedactionFinding] = []
    for markdown in _markdown_files(target):
        findings.extend(_findings_for_file(markdown, config=config, profile=normalized))
    return tuple(findings)


def _markdown_files(path: Path) -> tuple[Path, ...]:
    if path.is_file():
        return (path,) if path.suffix.lower() == ".md" else ()
    return tuple(sorted(item for item in path.rglob("*.md") if item.is_file()))


def _findings_for_file(path: Path, *, config: DtpConfig, profile: str) -> list[RedactionFinding]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    metadata, _body = split_frontmatter(path)
    findings: list[RedactionFinding] = []

    for label, pattern in SECRET_PATTERNS.items():
        if pattern.search(text):
            findings.append(RedactionFinding(path, f"possible secret: {label}"))

    if profile in {"practice", "case-study"}:
        for label, pattern in IDENTIFIER_PATTERNS.items():
            if pattern.search(text):
                findings.append(RedactionFinding(path, f"unredacted identifier: {label}"))

    if profile == "case-study" and FINANCIAL_PATTERN.search(text):
        findings.append(RedactionFinding(path, "financial specific requires explicit approval"))

    if profile == "practice":
        data_class = str(metadata.get("data_class") or "").upper()
        if data_class in {"P2", "P3", "P4"}:
            findings.append(
                RedactionFinding(path, f"{data_class} material cannot live in practice-os")
            )
        if metadata.get("confidential") is True:
            findings.append(
                RedactionFinding(path, "confidential artifact cannot live in practice-os")
            )

    if profile == "case-study":
        permission = str(metadata.get("permission_level") or "").strip().lower()
        status = str(metadata.get("review_status") or "").strip().lower()
        if permission == "internal_only":
            findings.append(RedactionFinding(path, "case study is still internal_only"))
        if status not in {"reviewed", "approved"}:
            findings.append(RedactionFinding(path, "case study has not passed redaction review"))
        _check_claim_contract(path, text, findings)

    return findings


def _check_claim_contract(path: Path, text: str, findings: list[RedactionFinding]) -> None:
    required = (
        "## Claim",
        "## Evidence source",
        "## Baseline",
        "## After",
        "## Measurement caveats",
        "## Permission level",
        "## Redaction status",
        "## Reviewer",
    )
    for heading in required:
        if heading not in text:
            findings.append(RedactionFinding(path, f"missing case-study section: {heading}"))
