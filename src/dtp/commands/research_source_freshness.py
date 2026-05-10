from __future__ import annotations

import html
import json
import re
from collections.abc import Callable
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import quote_plus, urlparse
from urllib.request import Request, urlopen

from dtp.config import DtpConfig

ALLOWED_FRESHNESS_STATES = {
    "unchanged",
    "changed_minor",
    "changed_meaningful",
    "stale_local_record",
    "source_unreachable",
    "blocked_source",
    "needs_manual_review",
}
ALLOWED_RECOMMENDED_ACTIONS = {
    "ignore",
    "watch",
    "create_research_decision_record",
    "create_research_pattern_candidate",
    "create_digest",
    "open_implementation_review",
    "update_source_list",
    "route_to_guardrail_review",
    "blocked",
}
SOURCE_FRESHNESS_OUTPUT_DIR = "research-source-freshness"
DEFAULT_BLOCKED_ACTIONS = (
    "public claims",
    "client communications",
    "Notion sync",
    "tool installs",
    "repo changes",
    "autonomous promotion",
)
OFFICIAL_SEARCH_DOMAINS = (
    "developers.openai.com",
    "platform.claude.com",
    "github.blog/changelog",
    "vercel.com/changelog",
    "supabase.com/changelog",
    "owasp.org",
)
SOURCE_SUBSET: dict[str, dict[str, str | int]] = {
    "dtp-repo-evidence": {
        "name": "DTP docs, receipts, Kaizen, evolution, research artifacts",
        "tier": 0,
        "url_or_path": "docs/; practice-os/",
    },
    "openai-api-codex-changelog": {
        "name": "OpenAI API and Codex changelog",
        "tier": 1,
        "url_or_path": "https://developers.openai.com/api/docs/changelog",
    },
    "openai-agents-sdk-docs": {
        "name": "OpenAI Agents SDK docs",
        "tier": 1,
        "url_or_path": "https://developers.openai.com/api/docs/guides/agents",
    },
    "anthropic-claude-release-notes": {
        "name": "Anthropic Claude release notes",
        "tier": 1,
        "url_or_path": "https://platform.claude.com/docs/en/release-notes/overview",
    },
    "github-copilot-changelog": {
        "name": "GitHub Copilot changelog",
        "tier": 1,
        "url_or_path": "https://github.blog/changelog/label/copilot/",
    },
    "vercel-changelog": {
        "name": "Vercel changelog",
        "tier": 1,
        "url_or_path": "https://vercel.com/changelog",
    },
    "supabase-changelog": {
        "name": "Supabase changelog",
        "tier": 1,
        "url_or_path": "https://supabase.com/changelog",
    },
    "owasp-genai": {
        "name": "OWASP GenAI Security Project",
        "tier": 2,
        "url_or_path": "https://owasp.org/www-project-top-10-for-large-language-model-applications/",
    },
}


class ResearchSourceFreshnessError(ValueError):
    pass


@dataclass(frozen=True)
class FetchedPage:
    url: str
    status: int
    text: str


FetchFunc = Callable[[str], FetchedPage]


@dataclass(frozen=True)
class SourceFreshnessItem:
    run_id: str
    source_id: str
    source_name: str
    source_tier: int
    source_url_or_path: str
    reviewed_at: str
    freshness_state: str
    change_summary: str
    why_it_matters: str
    evidence_limit: str
    recommended_action: str
    allowed_next_artifact: str
    blocked_actions: tuple[str, ...]
    review_owner: str
    next_review_trigger: str
    notes: tuple[str, ...]
    url_metadata: tuple[str, ...]
    search_queries: tuple[str, ...]
    evidence: tuple[dict[str, object], ...]


@dataclass(frozen=True)
class SourceFreshnessDryRunResult:
    item: SourceFreshnessItem
    jsonl_path: Path
    markdown_path: Path
    evidence_count: int
    wrote_files: bool


def run_research_source_freshness_dry_run(
    config: DtpConfig,
    *,
    source_id: str = "",
    source_name: str = "",
    source_tier: int | None = None,
    source_url_or_path: str = "",
    notes: tuple[str, ...] = (),
    urls: tuple[str, ...] = (),
    queries: tuple[str, ...] = (),
    fetch_urls: bool = False,
    search_web: bool = False,
    official_first: bool = True,
    freshness_state: str = "needs_manual_review",
    recommended_action: str = "watch",
    change_summary: str = "",
    why_it_matters: str = "",
    evidence_limit: str = "",
    allowed_next_artifact: str = (
        "research decision record, research pattern candidate, digest, or "
        "implementation review after human review"
    ),
    blocked_actions: tuple[str, ...] = DEFAULT_BLOCKED_ACTIONS,
    review_owner: str = "Research Steward",
    next_review_trigger: str = "Toni review, source change, or next source-freshness dry run",
    run_id: str = "",
    now: datetime | None = None,
    fetcher: FetchFunc | None = None,
) -> SourceFreshnessDryRunResult:
    clean_notes = _clean_tuple(notes)
    clean_urls = _clean_tuple(urls)
    clean_queries = _clean_tuple(queries)
    has_input = any(
        (clean_notes, clean_urls, clean_queries, source_id, source_name, source_url_or_path)
    )
    if not has_input:
        raise ResearchSourceFreshnessError(
            "source-freshness dry-run needs a source id/name/path, note, URL, or query"
        )

    resolved = _resolve_source(source_id, source_name, source_tier, source_url_or_path)
    _validate_item_options(freshness_state, recommended_action, resolved["source_tier"])

    timestamp = now or datetime.now(UTC)
    date_slug = timestamp.date().isoformat()
    reviewed_at = timestamp.isoformat(timespec="seconds")
    output_dir = config.outputs_dir / SOURCE_FRESHNESS_OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    jsonl_path = output_dir / f"source-freshness-{date_slug}.jsonl"
    markdown_path = output_dir / f"source-freshness-{date_slug}.md"
    resolved_run_id = run_id.strip() or _next_run_id(jsonl_path, date_slug)

    evidence = _collect_evidence(
        urls=clean_urls,
        queries=clean_queries,
        fetch_urls=fetch_urls,
        search_web=search_web,
        official_first=official_first,
        fetcher=fetcher or _default_fetcher,
    )
    item = SourceFreshnessItem(
        run_id=resolved_run_id,
        source_id=resolved["source_id"],
        source_name=resolved["source_name"],
        source_tier=resolved["source_tier"],
        source_url_or_path=resolved["source_url_or_path"],
        reviewed_at=reviewed_at,
        freshness_state=freshness_state,
        change_summary=change_summary.strip()
        or _default_change_summary(clean_notes, clean_urls, clean_queries),
        why_it_matters=why_it_matters.strip()
        or "Dry-run evidence needs human review before it can change practice guidance.",
        evidence_limit=evidence_limit.strip()
        or (
            "This dry run proves only that evidence was captured for review; it does "
            "not prove a public claim or authorize action."
        ),
        recommended_action=recommended_action,
        allowed_next_artifact=allowed_next_artifact.strip(),
        blocked_actions=tuple(action.strip() for action in blocked_actions if action.strip()),
        review_owner=review_owner.strip() or "Research Steward",
        next_review_trigger=next_review_trigger.strip()
        or "Toni review, source change, or next source-freshness dry run",
        notes=clean_notes,
        url_metadata=clean_urls,
        search_queries=clean_queries,
        evidence=tuple(evidence),
    )
    _append_jsonl(jsonl_path, item)
    _append_markdown(markdown_path, item)
    return SourceFreshnessDryRunResult(
        item=item,
        jsonl_path=jsonl_path,
        markdown_path=markdown_path,
        evidence_count=len(evidence),
        wrote_files=True,
    )


def render_source_freshness_dry_run(
    result: SourceFreshnessDryRunResult,
    repo_root: Path,
) -> str:
    item = result.item
    lines = [
        "Research Source Freshness Dry Run",
        "mode: internal dry-run queue",
        f"run_id: {item.run_id}",
        f"source: {item.source_id} - {item.source_name}",
        f"freshness_state: {item.freshness_state}",
        f"recommended_action: {item.recommended_action}",
        f"evidence_items: {result.evidence_count}",
        f"jsonl: {result.jsonl_path.relative_to(repo_root).as_posix()}",
        f"markdown: {result.markdown_path.relative_to(repo_root).as_posix()}",
        (
            "boundary: output is review evidence only; no public claims, client comms, "
            "Notion sync, tool installs, repo changes, or autonomous promotion"
        ),
    ]
    if item.search_queries:
        lines.append("search: captured query packet; broad search results require human review")
    if item.url_metadata:
        has_fetched_excerpt = any(e.get("kind") == "fetched_url" for e in item.evidence)
        fetch_note = "fetched excerpts" if has_fetched_excerpt else "metadata only"
        lines.append(f"urls: {fetch_note}")
    return "\n".join(lines) + "\n"


def _resolve_source(
    source_id: str,
    source_name: str,
    source_tier: int | None,
    source_url_or_path: str,
) -> dict[str, str | int]:
    clean_id = source_id.strip() or "manual-source"
    defaults = SOURCE_SUBSET.get(clean_id, {})
    return {
        "source_id": clean_id,
        "source_name": source_name.strip() or str(defaults.get("name") or clean_id),
        "source_tier": int(source_tier if source_tier is not None else defaults.get("tier", 1)),
        "source_url_or_path": source_url_or_path.strip()
        or str(defaults.get("url_or_path") or "operator supplied"),
    }


def _validate_item_options(freshness_state: str, recommended_action: str, source_tier: int) -> None:
    if freshness_state not in ALLOWED_FRESHNESS_STATES:
        raise ResearchSourceFreshnessError(f"unknown freshness state: {freshness_state}")
    if recommended_action not in ALLOWED_RECOMMENDED_ACTIONS:
        raise ResearchSourceFreshnessError(f"unknown recommended action: {recommended_action}")
    if source_tier not in {0, 1, 2, 3, 4}:
        raise ResearchSourceFreshnessError("source tier must be 0, 1, 2, 3, or 4")


def _collect_evidence(
    *,
    urls: tuple[str, ...],
    queries: tuple[str, ...],
    fetch_urls: bool,
    search_web: bool,
    official_first: bool,
    fetcher: FetchFunc,
) -> list[dict[str, object]]:
    evidence: list[dict[str, object]] = []
    for url in urls:
        evidence.append({"kind": "url_metadata", "url": url})
        if fetch_urls:
            evidence.append(_fetch_url_evidence(url, fetcher))

    for query in queries:
        search_urls = _search_urls(query, official_first=official_first)
        evidence.append(
            {
                "kind": "search_query",
                "query": query,
                "official_first": official_first,
                "search_urls": search_urls,
                "confidence": "low until reviewed against primary sources",
            }
        )
        if search_web:
            evidence.append(_search_result_evidence(query, fetcher))
    return evidence


def _fetch_url_evidence(url: str, fetcher: FetchFunc) -> dict[str, object]:
    block_reason = _blocked_fetch_reason(url)
    if block_reason:
        return {"kind": "blocked_url", "url": url, "reason": block_reason}
    try:
        page = fetcher(url)
    except Exception as exc:  # pragma: no cover - exercised through default fetcher variability
        return {"kind": "fetch_error", "url": url, "error": str(exc)}
    return {
        "kind": "fetched_url",
        "url": page.url,
        "status": page.status,
        "title": _extract_title(page.text),
        "excerpt": _excerpt(page.text),
    }


def _search_result_evidence(query: str, fetcher: FetchFunc) -> dict[str, object]:
    search_url = _duckduckgo_search_url(query)
    try:
        page = fetcher(search_url)
    except Exception as exc:  # pragma: no cover - exercised through default fetcher variability
        return {"kind": "search_error", "query": query, "search_url": search_url, "error": str(exc)}
    return {
        "kind": "search_results",
        "query": query,
        "search_url": search_url,
        "status": page.status,
        "results": _extract_search_results(page.text),
        "confidence": "low until each result is reviewed against primary sources",
    }


def _default_fetcher(url: str) -> FetchedPage:
    request = Request(
        url,
        headers={
            "User-Agent": (
                "diagnose-to-plan-source-freshness/0.1 "
                "(internal dry-run; contact owner before reuse)"
            )
        },
    )
    with urlopen(request, timeout=12) as response:  # noqa: S310 - guarded public dry-run fetch
        raw = response.read(500_000)
        charset = response.headers.get_content_charset() or "utf-8"
        text = raw.decode(charset, errors="replace")
        status = int(getattr(response, "status", 0) or 0)
        final_url = str(getattr(response, "url", url) or url)
    return FetchedPage(url=final_url, status=status, text=text)


def _blocked_fetch_reason(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return "only public http/https URLs can be fetched"
    host = (parsed.hostname or "").lower()
    if not host:
        return "URL host is missing"
    if host in {"localhost", "127.0.0.1", "::1"} or host.endswith(".local"):
        return "local or private hosts are blocked"
    if _looks_private_ip(host):
        return "private network addresses are blocked"
    return ""


def _looks_private_ip(host: str) -> bool:
    parts = host.split(".")
    if len(parts) != 4 or not all(part.isdigit() for part in parts):
        return False
    first = int(parts[0])
    second = int(parts[1])
    return (
        first == 10
        or first == 127
        or first == 0
        or (first == 172 and 16 <= second <= 31)
        or (first == 192 and second == 168)
    )


def _search_urls(query: str, *, official_first: bool) -> list[str]:
    urls: list[str] = []
    if official_first:
        urls.extend(
            _duckduckgo_search_url(f"site:{domain} {query}")
            for domain in OFFICIAL_SEARCH_DOMAINS
        )
    urls.append(_duckduckgo_search_url(query))
    return urls


def _duckduckgo_search_url(query: str) -> str:
    return f"https://duckduckgo.com/html/?q={quote_plus(query.strip())}"


def _extract_search_results(text: str) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for match in re.finditer(
        r'<a[^>]+class="result__a"[^>]+href="(?P<url>[^"]+)"[^>]*>(?P<title>.*?)</a>',
        text,
        re.IGNORECASE | re.DOTALL,
    ):
        results.append(
            {
                "title": _clean_html(match.group("title"))[:180],
                "url": html.unescape(match.group("url")),
            }
        )
        if len(results) >= 5:
            break
    return results


def _extract_title(text: str) -> str:
    match = re.search(r"<title[^>]*>(.*?)</title>", text, re.IGNORECASE | re.DOTALL)
    if not match:
        return ""
    return _clean_html(match.group(1))[:180]


def _excerpt(text: str) -> str:
    body = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", text)
    return _clean_html(body)[:700]


def _clean_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def _default_change_summary(
    notes: tuple[str, ...],
    urls: tuple[str, ...],
    queries: tuple[str, ...],
) -> str:
    parts: list[str] = []
    if notes:
        parts.append(f"{len(notes)} operator note(s)")
    if urls:
        parts.append(f"{len(urls)} URL(s)")
    if queries:
        parts.append(f"{len(queries)} search query packet(s)")
    subject = ", ".join(parts) if parts else "source metadata"
    return f"Captured {subject} for source-freshness human review."


def _next_run_id(jsonl_path: Path, date_slug: str) -> str:
    count = 0
    if jsonl_path.exists():
        count = sum(
            1 for line in jsonl_path.read_text(encoding="utf-8").splitlines() if line.strip()
        )
    return f"rsf-{date_slug}-{count + 1:03d}"


def _append_jsonl(path: Path, item: SourceFreshnessItem) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = asdict(item)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(payload, ensure_ascii=True, sort_keys=True) + "\n")


def _append_markdown(path: Path, item: SourceFreshnessItem) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        if path.stat().st_size == 0:
            handle.write("# Research Source Freshness Dry-Run Queue\n\n")
        handle.write(_render_markdown_item(item))


def _render_markdown_item(item: SourceFreshnessItem) -> str:
    evidence_lines = "\n".join(
        f"- `{evidence.get('kind', 'evidence')}`: {_render_evidence_line(evidence)}"
        for evidence in item.evidence
    )
    notes = "\n".join(f"- {note}" for note in item.notes) or "- none"
    queries = "\n".join(f"- {query}" for query in item.search_queries) or "- none"
    urls = "\n".join(f"- {url}" for url in item.url_metadata) or "- none"
    blocked = ", ".join(item.blocked_actions)
    return (
        f"## {item.run_id} - {item.source_id}\n\n"
        f"- Source: {item.source_name}\n"
        f"- Tier: {item.source_tier}\n"
        f"- URL or path: {item.source_url_or_path}\n"
        f"- Reviewed at: {item.reviewed_at}\n"
        f"- Freshness state: {item.freshness_state}\n"
        f"- Recommended action: {item.recommended_action}\n"
        f"- Review owner: {item.review_owner}\n"
        f"- Blocked actions: {blocked}\n\n"
        "### Change Summary\n\n"
        f"{item.change_summary}\n\n"
        "### Why It Matters\n\n"
        f"{item.why_it_matters}\n\n"
        "### Evidence Limit\n\n"
        f"{item.evidence_limit}\n\n"
        "### Notes\n\n"
        f"{notes}\n\n"
        "### URL Metadata\n\n"
        f"{urls}\n\n"
        "### Search Queries\n\n"
        f"{queries}\n\n"
        "### Evidence\n\n"
        f"{evidence_lines or '- none'}\n\n"
        "### Next Review Trigger\n\n"
        f"{item.next_review_trigger}\n\n"
    )


def _render_evidence_line(evidence: dict[str, object]) -> str:
    if evidence.get("kind") == "search_query":
        return str(evidence.get("query", ""))
    if evidence.get("kind") == "search_results":
        return f"{evidence.get('query', '')} ({len(evidence.get('results', []))} result(s))"
    if evidence.get("kind") in {"fetched_url", "url_metadata", "blocked_url", "fetch_error"}:
        return str(evidence.get("url", ""))
    return str(evidence)


def _clean_tuple(values: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(value.strip() for value in values if value.strip())
