from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

from typer.testing import CliRunner

from dtp.cli import app
from dtp.commands.evolution import run_evolution_new
from dtp.commands.kaizen import run_kaizen_capture
from dtp.commands.research import render_research_steward_review, run_research_steward_review
from dtp.commands.research_source_freshness import (
    FetchedPage,
    run_research_source_freshness_dry_run,
)
from dtp.config import DtpConfig


def test_research_steward_recommends_patterns_kaizen_and_digests(tmp_path: Path) -> None:
    config = _config(tmp_path)
    run_evolution_new(
        config,
        title="Status visibility prevents lightweight capture drift",
        kind="research-pattern",
        state="draft",
    )
    run_kaizen_capture(
        config,
        "Harvey MCP could matter for future legal-work research.",
        status="inbox",
        item_type="research",
        repo="diagnose-to-plan",
        sensitivity="internal-only",
        tags=("legal-mcp",),
    )
    digest_dir = tmp_path / "practice-os" / "research" / "digests"
    digest_dir.mkdir(parents=True)
    digest_path = digest_dir / "2026-05-10-ai-operating-shift.md"
    digest_path.write_text(
        "# Research Arm Digest - AI operating shift\n\n"
        "Status: draft\n\n"
        "## Digest Summary\n\n"
        "A draft digest that still needs source and approval review.\n",
        encoding="utf-8",
        newline="\n",
    )

    result = run_research_steward_review(config, limit=10)
    rendered = render_research_steward_review(result, tmp_path)

    assert result.pattern_candidate_count == 1
    assert result.kaizen_count == 1
    assert result.digest_count == 1
    assert "Research Steward Review" in rendered
    assert "mode: read-only recommendation" in rendered
    assert "Status visibility prevents lightweight capture drift" in rendered
    assert "complete evidence limits" in rendered
    assert "Harvey MCP could matter" in rendered
    assert "classify into digest, radar item, spike, pattern candidate, or park" in rendered
    assert "Research Arm Digest - AI operating shift" in rendered
    assert "finish sources, hype filter" in rendered
    assert "cannot authorize public claims" in rendered
    assert "docs/RESEARCH_ARM_V0.md" in rendered


def test_research_steward_cli_outputs_recommendations(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    runner = CliRunner()

    runner.invoke(
        app,
        [
            "evolution",
            "new",
            "Research signal should become a pattern",
            "--kind",
            "research-pattern",
        ],
    )
    result = runner.invoke(app, ["research", "steward", "--limit", "1"])

    assert result.exit_code == 0
    assert "Research Steward Review" in result.output
    assert "Research signal should become a pattern" in result.output
    assert "read-only recommendation" in result.output


def test_research_steward_omits_accepted_digests_and_promoted_patterns(
    tmp_path: Path,
) -> None:
    config = _config(tmp_path)
    run_evolution_new(
        config,
        title="Promoted research pattern should not stay in the active queue",
        kind="research-pattern",
        state="promoted",
    )
    digest_dir = tmp_path / "practice-os" / "research" / "digests"
    digest_dir.mkdir(parents=True)
    digest_path = digest_dir / "2026-05-10-accepted-digest.md"
    digest_path.write_text(
        "# Research Arm Digest - Accepted digest\n\n"
        "Status: accepted\n\n"
        "## Digest Summary\n\n"
        "Accepted internal research.\n",
        encoding="utf-8",
        newline="\n",
    )

    result = run_research_steward_review(config, limit=10)
    rendered = render_research_steward_review(result, tmp_path)

    assert result.pattern_candidate_count == 0
    assert result.digest_count == 0
    assert "Promoted research pattern should not stay" not in rendered
    assert "Accepted digest" not in rendered
    assert "Recommendations\n- none" in rendered


def test_source_freshness_dry_run_writes_operator_url_and_query_queue(
    tmp_path: Path,
) -> None:
    config = _config(tmp_path)
    result = run_research_source_freshness_dry_run(
        config,
        source_id="openai-api-codex-changelog",
        notes=("Check whether agent tooling guidance changed.",),
        urls=("https://developers.openai.com/api/docs/changelog",),
        queries=("OpenAI Codex changelog agents evals",),
        now=datetime(2026, 5, 10, 12, 0, tzinfo=UTC),
    )

    assert result.jsonl_path == (
        tmp_path / "outputs" / "research-source-freshness" / "source-freshness-2026-05-10.jsonl"
    )
    assert result.markdown_path.exists()
    payload = json.loads(result.jsonl_path.read_text(encoding="utf-8").splitlines()[0])

    assert payload["run_id"] == "rsf-2026-05-10-001"
    assert payload["source_id"] == "openai-api-codex-changelog"
    assert payload["source_tier"] == 1
    assert payload["freshness_state"] == "needs_manual_review"
    assert payload["recommended_action"] == "watch"
    assert payload["notes"] == ["Check whether agent tooling guidance changed."]
    evidence_kinds = [entry["kind"] for entry in payload["evidence"]]
    assert evidence_kinds == ["url_metadata", "search_query"]
    search_urls = payload["evidence"][1]["search_urls"]
    assert any("site%3Adevelopers.openai.com" in url for url in search_urls)
    assert "public claims" in payload["blocked_actions"][0]


def test_source_freshness_can_fetch_public_url_excerpt(tmp_path: Path) -> None:
    config = _config(tmp_path)

    def fake_fetcher(url: str) -> FetchedPage:
        return FetchedPage(
            url=url,
            status=200,
            text=(
                "<html><title>Agent release notes</title>"
                "<body>New guardrail detail.</body></html>"
            ),
        )

    result = run_research_source_freshness_dry_run(
        config,
        source_id="manual-source",
        urls=("https://example.com/release-notes",),
        fetch_urls=True,
        now=datetime(2026, 5, 10, 12, 30, tzinfo=UTC),
        fetcher=fake_fetcher,
    )
    payload = json.loads(result.jsonl_path.read_text(encoding="utf-8").splitlines()[0])

    assert payload["evidence"][1]["kind"] == "fetched_url"
    assert payload["evidence"][1]["title"] == "Agent release notes"
    assert "New guardrail detail" in payload["evidence"][1]["excerpt"]


def test_source_freshness_can_capture_search_results(tmp_path: Path) -> None:
    config = _config(tmp_path)

    def fake_fetcher(url: str) -> FetchedPage:
        return FetchedPage(
            url=url,
            status=200,
            text=(
                '<a class="result__a" href="https://example.com/result">'
                "Useful source result</a>"
            ),
        )

    result = run_research_source_freshness_dry_run(
        config,
        source_name="Manual search packet",
        queries=("agent source freshness",),
        search_web=True,
        now=datetime(2026, 5, 10, 12, 45, tzinfo=UTC),
        fetcher=fake_fetcher,
    )
    payload = json.loads(result.jsonl_path.read_text(encoding="utf-8").splitlines()[0])

    assert payload["evidence"][0]["kind"] == "search_query"
    assert payload["evidence"][1]["kind"] == "search_results"
    assert payload["evidence"][1]["results"] == [
        {"title": "Useful source result", "url": "https://example.com/result"}
    ]


def test_source_freshness_blocks_private_url_fetch(tmp_path: Path) -> None:
    config = _config(tmp_path)
    result = run_research_source_freshness_dry_run(
        config,
        source_name="Unsafe local source",
        urls=("http://localhost:3000/private",),
        fetch_urls=True,
        now=datetime(2026, 5, 10, 13, 0, tzinfo=UTC),
    )
    payload = json.loads(result.jsonl_path.read_text(encoding="utf-8").splitlines()[0])

    assert payload["evidence"][1]["kind"] == "blocked_url"
    assert "local or private hosts are blocked" in payload["evidence"][1]["reason"]


def test_source_freshness_cli_writes_dry_run_queue(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setenv("DTP_HOME", str(tmp_path))
    runner = CliRunner()

    result = runner.invoke(
        app,
        [
            "research",
            "source-freshness",
            "--source-id",
            "supabase-changelog",
            "--note",
            "Check auth/runtime changes.",
            "--query",
            "Supabase changelog auth runtime",
        ],
    )

    assert result.exit_code == 0
    assert "Research Source Freshness Dry Run" in result.output
    assert "mode: internal dry-run queue" in result.output
    assert (tmp_path / "outputs" / "research-source-freshness").exists()


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
    )
