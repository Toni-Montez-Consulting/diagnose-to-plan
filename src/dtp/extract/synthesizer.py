from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import frontmatter

from dtp.capture import render_markdown_with_frontmatter, slugify
from dtp.config import DtpConfig
from dtp.extract.indexer import ExtractError

CONFIDENCE_RANK = {"high": 3, "medium": 2, "low": 1}
SYNTHESIS_SOURCE_TYPES = {"pattern", "lesson", "decision"}


@dataclass(frozen=True)
class ExtractDoc:
    path: Path
    relative_path: str
    type: str
    repo: str
    group: str
    title: str
    content: str
    metadata: dict[str, Any]


@dataclass(frozen=True)
class SynthesisResult:
    path: Path
    group: str
    source_count: int
    canonical_repo: str


def synthesize(
    *,
    config: DtpConfig,
    kind: str | None = None,
    regroup: bool = False,
    no_confirm: bool = False,
    clock: datetime | None = None,
) -> tuple[SynthesisResult, ...]:
    validate_source_kind(kind)
    docs = _load_extract_docs(config=config, kind=kind)
    if not docs:
        raise ExtractError("no pattern, lesson, or decision extracts found to synthesize")

    grouped: dict[str, list[ExtractDoc]] = defaultdict(list)
    for doc in docs:
        grouped[doc.group].append(doc)

    synthesis_dir = config.extracts_dir / "synthesis"
    synthesis_dir.mkdir(parents=True, exist_ok=True)
    now = clock or datetime.now(UTC)
    results: list[SynthesisResult] = []
    for group, group_docs in sorted(grouped.items()):
        result = _write_synthesis(
            config=config,
            synthesis_dir=synthesis_dir,
            group=group,
            docs=tuple(group_docs),
            clock=now,
            regroup=regroup,
            no_confirm=no_confirm,
        )
        results.append(result)
    return tuple(results)


def _load_extract_docs(*, config: DtpConfig, kind: str | None) -> tuple[ExtractDoc, ...]:
    docs: list[ExtractDoc] = []
    for source_type, directory in _source_directories(config):
        if kind and source_type != kind:
            continue
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name.upper() == "README.MD":
                continue
            docs.append(_load_doc(config=config, path=path, source_type=source_type))
    return tuple(docs)


def _source_directories(config: DtpConfig) -> tuple[tuple[str, Path], ...]:
    return (
        ("pattern", config.extracts_dir / "patterns"),
        ("lesson", config.extracts_dir / "lessons"),
        ("decision", config.extracts_dir / "decisions"),
    )


def _load_doc(*, config: DtpConfig, path: Path, source_type: str) -> ExtractDoc:
    post = frontmatter.load(path)
    metadata = dict(post.metadata)
    doc_type = str(metadata.get("type") or source_type)
    if doc_type not in SYNTHESIS_SOURCE_TYPES:
        doc_type = source_type
    repo = str(metadata.get("repo") or metadata.get("repo_slug") or path.stem.split("--", 1)[0])
    group = _group_for(metadata=metadata, doc_type=doc_type, path=path)
    relative = path.relative_to(config.repo_root).as_posix()
    return ExtractDoc(
        path=path,
        relative_path=relative,
        type=doc_type,
        repo=repo,
        group=group,
        title=_title_from_content(post.content, path),
        content=post.content,
        metadata=metadata,
    )


def _group_for(*, metadata: dict[str, Any], doc_type: str, path: Path) -> str:
    if doc_type == "pattern":
        return slugify(str(metadata.get("signal") or metadata.get("pattern_slug") or path.stem))
    return slugify(str(metadata.get("pattern") or metadata.get("signal") or path.stem))


def _write_synthesis(
    *,
    config: DtpConfig,
    synthesis_dir: Path,
    group: str,
    docs: tuple[ExtractDoc, ...],
    clock: datetime,
    regroup: bool,
    no_confirm: bool,
) -> SynthesisResult:
    canonical = _canonical_doc(docs)
    repos = sorted({doc.repo for doc in docs})
    source_paths = [doc.relative_path for doc in docs]
    counts = {
        "patterns": sum(1 for doc in docs if doc.type == "pattern"),
        "lessons": sum(1 for doc in docs if doc.type == "lesson"),
        "decisions": sum(1 for doc in docs if doc.type == "decision"),
    }
    metadata = {
        "group": group,
        "synthesized_at": _timestamp(clock),
        "source_types": sorted({doc.type for doc in docs}),
        "source_paths": source_paths,
        "canonical_repo": canonical.repo,
        "canonical_repos": repos,
        "pattern_count": counts["patterns"],
        "lesson_count": counts["lessons"],
        "decision_count": counts["decisions"],
        "promoted": False,
        "private_review_required": True,
        "regrouped": regroup,
        "no_confirm": no_confirm,
    }
    body = _render_synthesis(group=group, docs=docs, canonical=canonical, counts=counts)
    destination = synthesis_dir / f"{group}.md"
    destination.write_text(render_markdown_with_frontmatter(metadata, body), encoding="utf-8")
    return SynthesisResult(
        path=destination,
        group=group,
        source_count=len(docs),
        canonical_repo=canonical.repo,
    )


def _canonical_doc(docs: tuple[ExtractDoc, ...]) -> ExtractDoc:
    repo_docs: dict[str, list[ExtractDoc]] = defaultdict(list)
    for doc in docs:
        repo_docs[doc.repo].append(doc)
    canonical_repo = sorted(
        repo_docs,
        key=lambda repo: _canonical_repo_score(tuple(repo_docs[repo])),
        reverse=True,
    )[0]
    return sorted(repo_docs[canonical_repo], key=_canonical_doc_score, reverse=True)[0]


def _canonical_repo_score(docs: tuple[ExtractDoc, ...]) -> tuple[int, int, int, int, int]:
    promoted = max(1 if bool(doc.metadata.get("promoted")) else 0 for doc in docs)
    human_reviewed = sum(1 for doc in docs if doc.type in {"lesson", "decision"})
    confidence = max(
        CONFIDENCE_RANK.get(str(doc.metadata.get("confidence", "")).lower(), 0)
        for doc in docs
    )
    file_count = sum(_file_count(doc) for doc in docs)
    return (promoted, human_reviewed, confidence, len(docs), file_count)


def _canonical_doc_score(doc: ExtractDoc) -> tuple[int, int, int, int]:
    promoted = 1 if bool(doc.metadata.get("promoted")) else 0
    human_reviewed = 1 if doc.type in {"lesson", "decision"} else 0
    confidence = CONFIDENCE_RANK.get(str(doc.metadata.get("confidence", "")).lower(), 0)
    return (promoted, human_reviewed, confidence, _file_count(doc))


def _file_count(doc: ExtractDoc) -> int:
    files_read = doc.metadata.get("files_read", ())
    return len(files_read) if isinstance(files_read, list | tuple) else 0


def _render_synthesis(
    *,
    group: str,
    docs: tuple[ExtractDoc, ...],
    canonical: ExtractDoc,
    counts: dict[str, int],
) -> str:
    evidence = "\n".join(
        f"- `{doc.relative_path}` ({doc.type}, repo: `{doc.repo}`): {doc.title}" for doc in docs
    )
    reusable_shape = _reusable_shape(group)
    varies = _what_varies(group)
    private_boundary = _private_boundary(group)
    source_notes = "\n".join(f"- {_source_note(doc)}" for doc in docs)
    return "\n".join(
        [
            f"# {_title(group)}",
            "",
            "## Synthesis",
            "",
            f"This synthesis combines {len(docs)} extract sources: "
            f"{counts['patterns']} pattern(s), {counts['lessons']} lesson(s), "
            f"and {counts['decisions']} decision(s). The current canonical repo is "
            f"`{canonical.repo}`, based on promoted status, captured lessons/decisions, "
            "detector confidence, and evidence breadth.",
            "",
            "## Canonical Evidence",
            "",
            evidence or "- No evidence sources.",
            "",
            "## Reusable Shape",
            "",
            reusable_shape,
            "",
            "## What Varies",
            "",
            varies,
            "",
            "## Do Not Reuse Blindly",
            "",
            private_boundary,
            "",
            "## Drafting Use",
            "",
            f"When a diagnose note asks for `{group}`-adjacent work, cite this synthesis "
            "as prior operating evidence, then name which parts are being reused and which "
            "parts must be adapted for the client.",
            "",
            "## Source Notes",
            "",
            source_notes or "- No source notes.",
            "",
            "## Review Checklist",
            "",
            "- No secrets or credentials.",
            "- No raw intake records.",
            "- No private client notes.",
            "- No service-role values.",
            "- `promoted` remains false until this synthesis helps real work.",
            "",
        ]
    )


def _reusable_shape(group: str) -> str:
    if "admin" in group:
        return (
            "Use a two-layer operating pattern: a public-safe command room for status, "
            "links, triage, work orders, and runbook boundaries; and a protected private "
            "console for records, notes, workflow state, and owner decisions."
        )
    return (
        "Reuse the operating role, file boundaries, and integration shape proven by the "
        "source extracts. Keep implementation details tied to cited evidence."
    )


def _what_varies(group: str) -> str:
    if "admin" in group:
        return (
            "Domain language, triage stages, record schema, auth level, health checks, "
            "and the public/private boundary should vary by client and deployment risk."
        )
    return "Copy, data model, brand tokens, auth requirements, and privacy rules vary by client."


def _private_boundary(group: str) -> str:
    if "admin" in group:
        return (
            "Do not copy private rows, client notes, service-role behavior, raw intake "
            "content, or workflow records into a public surface. Reuse the boundary, not "
            "the private data."
        )
    return (
        "Do not treat detector output as a reusable asset until the cited files have been "
        "reviewed for private or client-specific details."
    )


def _source_note(doc: ExtractDoc) -> str:
    if doc.type == "pattern":
        confidence = doc.metadata.get("confidence", "unknown")
        return f"`{doc.relative_path}` is a `{confidence}` confidence pattern candidate."
    return f"`{doc.relative_path}` records a {doc.type} for `{doc.group}`."


def _title_from_content(content: str, path: Path) -> str:
    for line in content.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def _title(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("-"))


def _timestamp(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=UTC)
    return value.astimezone(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def validate_source_kind(kind: str | None) -> None:
    if kind is None:
        return
    if kind not in SYNTHESIS_SOURCE_TYPES:
        raise ExtractError(f"invalid synthesize type: {kind}")
