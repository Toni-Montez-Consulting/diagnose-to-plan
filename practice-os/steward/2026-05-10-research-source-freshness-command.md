---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Steward Receipt - Research Source Freshness Local Command

Date: 2026-05-10

Status: accepted local dry-run implementation

## Trigger

After the dry-run spec merged, Toni clarified that the first implementation
should handle operator notes, pasted URL/source metadata, and searching for
information.

## Decision Captured

- Add `dtp research source-freshness` as a local dry-run command.
- Support notes, URL metadata, optional public URL fetching, search query
  packets, and optional public search-result-page capture.
- Keep official-source-first search URLs as the default search posture.
- Treat broad web search results as low-confidence until a human reviews them
  against primary sources.
- Write output only to ignored `outputs/research-source-freshness/`.

## Artifacts Added

- `src/dtp/commands/research_source_freshness.py`
- `decisions/0015-research-source-freshness-local-command.md`

## Artifacts Updated

- `src/dtp/cli.py`
- `tests/test_research.py`
- `docs/02-commands.md`
- `docs/RESEARCH_SOURCE_FRESHNESS_DRY_RUN_V0.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`
- `practice-os/templates/activation-routing-map.md`

## Operating Boundary

The command does not approve:

- scheduled source sweeps;
- autonomous source monitoring;
- source-list or KB updates;
- Notion sync;
- client communications;
- public claims;
- tool installs;
- repo mutations from research findings.

## Next Use

Run a small real dry run against a few approved sources, review the evidence
queue, and decide whether the next iteration needs source configs,
deduplication, saved snapshots, or richer search parsing.
