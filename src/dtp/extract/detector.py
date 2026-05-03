from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from dtp.capture import render_markdown_with_frontmatter, slugify
from dtp.config import DtpConfig
from dtp.extract.indexer import ExtractError, load_index
from dtp.models import DEFAULT_MODEL

MAX_FULL_LINES = 320
HEAD_LINES = 200
TAIL_LINES = 50
SECRET_KEYWORDS = re.compile(
    r"api[_-]?key|secret|token|password|private[_-]?key|service[_-]?role|client_secret|bearer",
    re.IGNORECASE,
)
SECRET_SHAPES = re.compile(
    r"=|authorization|x-[a-z0-9_-]*(?:secret|token|key)|sk-[a-z0-9_-]+|"
    r"<[a-z0-9 _-]*(?:key|secret|token)[a-z0-9 _-]*>",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class DetectionResult:
    path: Path
    repo_slug: str
    signal: str
    pattern_slug: str
    confidence: str


@dataclass(frozen=True)
class FileSlice:
    path: str
    total_lines: int
    included_ranges: tuple[tuple[int, int], ...]
    text: str
    truncated: bool


def detect_patterns(
    *,
    config: DtpConfig,
    repo: str,
    signal: str | None = None,
    all_signals: bool = False,
    force: bool = False,
    clock: datetime | None = None,
) -> tuple[DetectionResult, ...]:
    index = load_index(config, repo)
    signals = index.get("signals", [])
    selected = _select_signals(signals, signal=signal, all_signals=all_signals)
    if not selected:
        raise ExtractError(f"no signals to detect for repo: {repo}")
    return tuple(
        detect_signal(
            config=config,
            index=index,
            signal_data=item,
            force=force,
            clock=clock,
        )
        for item in selected
    )


def detect_signal(
    *,
    config: DtpConfig,
    index: dict[str, Any],
    signal_data: dict[str, Any],
    force: bool = False,
    clock: datetime | None = None,
) -> DetectionResult:
    repo_slug = str(index["repo_slug"])
    signal_name = str(signal_data["name"])
    repo_path = Path(str(index["repo_path"]))
    if not repo_path.is_absolute():
        repo_path = (config.repo_root / repo_path).resolve()
    if not repo_path.exists():
        raise ExtractError(f"indexed repo path does not exist: {repo_path}")

    pattern_slug = _pattern_slug(signal_name, tuple(signal_data.get("files", ())))
    patterns_dir = config.extracts_dir / "patterns"
    patterns_dir.mkdir(parents=True, exist_ok=True)
    destination = patterns_dir / f"{repo_slug}--{pattern_slug}.md"
    if destination.exists() and not force:
        raise ExtractError(f"pattern already exists; pass --force to overwrite: {destination}")

    files = _prioritized_files(
        signal_name,
        [path for path in signal_data.get("files", []) if isinstance(path, str)],
    )
    slices = tuple(_slice_file(repo_path / path, path) for path in files[:12])
    citations = _citations(signal_name, slices)
    truncated = any(item.truncated for item in slices)
    confidence = _confidence(slices=slices, citations=citations)
    now = clock or datetime.now(UTC)
    metadata = {
        "repo": repo_slug,
        "signal": signal_name,
        "pattern_slug": pattern_slug,
        "detected_at": _timestamp(now),
        "model": DEFAULT_MODEL,
        "files_read": [item.path for item in slices],
        "confidence": confidence,
        "truncated": truncated,
        "promoted": False,
        "private_review_required": True,
    }
    body = _render_pattern(
        repo_slug=repo_slug,
        signal_name=signal_name,
        evidence=str(signal_data.get("evidence", "")),
        pattern_slug=pattern_slug,
        slices=slices,
        citations=citations,
    )
    destination.write_text(render_markdown_with_frontmatter(metadata, body), encoding="utf-8")
    return DetectionResult(
        path=destination,
        repo_slug=repo_slug,
        signal=signal_name,
        pattern_slug=pattern_slug,
        confidence=confidence,
    )


def build_constrained_prompt(
    *,
    signal_name: str,
    evidence: str,
    slices: tuple[FileSlice, ...],
) -> str:
    files = "\n\n".join(
        f"## File: {item.path}\nIncluded ranges: {item.included_ranges}\n\n{item.text}"
        for item in slices
    )
    return (
        "Describe the pattern present in these files. Cite specific file paths and line "
        "ranges for every claim. If you cannot tell from the files what the pattern is, "
        "say so. Do not extrapolate from filenames or imports to functionality you did "
        "not see. The agent gets no filesystem tools; only this embedded content is in "
        "scope.\n\n"
        f"Signal: {signal_name}\nEvidence: {evidence}\n\n{files}"
    )


def _select_signals(
    signals: list[dict[str, Any]],
    *,
    signal: str | None,
    all_signals: bool,
) -> tuple[dict[str, Any], ...]:
    if signal:
        matches = [item for item in signals if item.get("name") == signal]
        if not matches:
            raise ExtractError(f"signal not found in index: {signal}")
        return tuple(matches)
    if all_signals:
        return tuple(signals)
    return tuple(signals)


def _slice_file(path: Path, display_path: str) -> FileSlice:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    if len(lines) <= MAX_FULL_LINES:
        included = ((1, len(lines)),) if lines else ()
        return FileSlice(
            path=display_path,
            total_lines=len(lines),
            included_ranges=included,
            text="\n".join(_numbered(lines, 1)),
            truncated=False,
        )

    head = lines[:HEAD_LINES]
    tail_start = len(lines) - TAIL_LINES + 1
    tail = lines[-TAIL_LINES:]
    included_ranges = ((1, HEAD_LINES), (tail_start, len(lines)))
    sliced = [*_numbered(head, 1), "... [truncated] ...", *_numbered(tail, tail_start)]
    return FileSlice(
        path=display_path,
        total_lines=len(lines),
        included_ranges=included_ranges,
        text="\n".join(sliced),
        truncated=True,
    )


def _numbered(lines: list[str], start: int) -> list[str]:
    return [
        f"{index}: {_redact_secret_line(line)}"
        for index, line in enumerate(lines, start=start)
    ]


def _redact_secret_line(line: str) -> str:
    if SECRET_KEYWORDS.search(line) and SECRET_SHAPES.search(line):
        indentation = line[: len(line) - len(line.lstrip())]
        return f"{indentation}[redacted secret-bearing line]"
    return line


def _prioritized_files(signal_name: str, files: list[str]) -> list[str]:
    return sorted(files, key=lambda path: _file_priority(signal_name, path))


def _file_priority(signal_name: str, path: str) -> tuple[int, str]:
    lowered = path.lower()
    score = 0
    if lowered.endswith((".md", ".mdx", ".txt")):
        score += 50
    if "__tests__" in lowered or ".test." in lowered or ".spec." in lowered:
        score += 20
    if signal_name == "admin-surface":
        admin_markers = (
            "/admin/",
            "admin.",
            "admin/",
            "/console/",
            "console/",
            "console.",
            "dashboard.",
            "dashboard/",
        )
        if any(marker in lowered for marker in admin_markers):
            score -= 20
        if lowered.startswith("api/console") or "/api/console" in lowered:
            score -= 15
        if lowered.endswith((".astro", ".tsx", ".ts", ".jsx", ".js")):
            score -= 5
    return (score, lowered)


def _citations(signal_name: str, slices: tuple[FileSlice, ...]) -> tuple[str, ...]:
    citations: list[str] = []
    keywords = _keywords(signal_name)
    for item in slices:
        for keyword in keywords:
            match = _first_line_with_keyword(item.text, keyword)
            if match is not None:
                citations.append(f"{item.path}:{match}-{match}")
        if not keywords and item.included_ranges:
            start, end = item.included_ranges[0]
            citations.append(f"{item.path}:{start}-{min(end, start + 20)}")
    if len(citations) < 2:
        for item in slices[:4]:
            if item.included_ranges:
                start, end = item.included_ranges[0]
                citations.append(f"{item.path}:{start}-{min(end, start + 20)}")
    return tuple(dict.fromkeys(citations))


def _keywords(signal_name: str) -> tuple[str, ...]:
    if signal_name == "admin-surface":
        return (
            "console",
            "admin",
            "dashboard",
            "intake",
            "runbook",
            "statusRows",
            "commandLinks",
            "triageRows",
            "workOrders",
        )
    if signal_name == "component-library":
        return ("type Props", "interface", "class=", "export")
    if signal_name == "api-surface":
        return ("request", "response", "handler", "export")
    return ()


def _first_line_with_keyword(text: str, keyword: str) -> int | None:
    pattern = re.compile(r"^(\d+): .*" + re.escape(keyword), re.IGNORECASE)
    for line in text.splitlines():
        match = pattern.search(line)
        if match:
            return int(match.group(1))
    return None


def _confidence(*, slices: tuple[FileSlice, ...], citations: tuple[str, ...]) -> str:
    if not slices:
        return "low"
    full_ratio = sum(1 for item in slices if not item.truncated) / len(slices)
    if full_ratio >= 0.8 and len(citations) >= 4:
        return "high"
    if full_ratio >= 0.5 and len(citations) >= 2:
        return "medium"
    return "low"


def _render_pattern(
    *,
    repo_slug: str,
    signal_name: str,
    evidence: str,
    pattern_slug: str,
    slices: tuple[FileSlice, ...],
    citations: tuple[str, ...],
) -> str:
    file_list = "\n".join(f"- `{item.path}`" for item in slices) or "- No files read."
    citation_list = "\n".join(f"- {citation}" for citation in citations) or "- No citations."
    prompt = build_constrained_prompt(
        signal_name=signal_name,
        evidence=evidence,
        slices=slices,
    )
    return "\n".join(
        [
            f"# {_title(pattern_slug)}",
            "",
            "## What this is",
            "",
            f"`{repo_slug}` exposes a `{signal_name}` pattern evidenced by {evidence}. "
            "This detector only used the indexed files listed below, so the pattern is "
            "a grounded extraction candidate rather than a full architectural claim.",
            "",
            "## Where it lives",
            "",
            file_list,
            "",
            "## Reusable shape",
            "",
            _reusable_shape(signal_name),
            "",
            "## Review notes",
            "",
            "- `promoted` starts false until Toni confirms this pattern helped real work.",
            "- `private_review_required` starts true so private details are checked before reuse.",
            "- Treat this as a pattern candidate; use citations before carrying it into a SOW.",
            "",
            "## Citations",
            "",
            citation_list,
            "",
            "## Constrained Prompt",
            "",
            "```text",
            prompt[:8000],
            "```",
            "",
        ]
    )


def _reusable_shape(signal_name: str) -> str:
    if signal_name == "admin-surface":
        return (
            "Public proof or entry surfaces should route into a private operating room. "
            "Reusable pieces include intake status, command links, triage state, work orders, "
            "health checks, and handoff/runbook boundaries. Client-specific pieces should vary "
            "by domain language, record schema, auth requirements, and privacy rules."
        )
    if signal_name == "component-library":
        return (
            "Reusable pieces are component boundaries, prop contracts, token usage, and layout "
            "patterns. Copy, data, and brand tokens should vary per engagement."
        )
    return (
        "Reusable pieces are the file shape, operating role, and integration boundary. "
        "Confirm client-specific data, privacy, and ownership before reuse."
    )


def _pattern_slug(signal_name: str, files: tuple[str, ...]) -> str:
    if signal_name == "admin-surface":
        if any("Console" in path or "/console" in path.lower() for path in files):
            return "admin-console"
        return "admin-command-room"
    return slugify(signal_name)


def _title(slug: str) -> str:
    return " ".join(word.capitalize() for word in slug.split("-"))


def _timestamp(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=UTC)
    return value.astimezone(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")
