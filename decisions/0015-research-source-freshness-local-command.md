# Decision 0015: Research Source Freshness Local Command

Date: 2026-05-10

Status: Accepted

## Context

After the dry-run spec landed, Toni clarified that the Research source freshness
workflow should support all intake modes:

- operator notes;
- pasted source URL or metadata;
- searching for information.

The command still needs to preserve the human-gated source-freshness boundary:
no autonomous promotion, no public claims, no client communication, no Notion
sync, no tool installs, and no tracked repo mutation from research findings.

## Decision

Add `dtp research source-freshness` as the first local dry-run command.

The command writes ignored JSONL and Markdown queue files under
`outputs/research-source-freshness/` and supports:

- `--note` for operator notes;
- `--url` for source URL metadata;
- `--fetch-url` for optional public URL excerpts;
- `--query` for search packets;
- `--search-web` for optional public search-result-page capture;
- official-source-first search URL generation by default.

## Consequences

- Research source freshness now has a usable local operator tool.
- Search and fetched-page evidence stay low-confidence until reviewed.
- Local/private URL fetches are blocked.
- Output remains ignored until a human promotes a reviewed, sanitized item to
  `practice-os/research/source-freshness/reviews/`.

## Non-Goals

- No scheduled sweep.
- No crawler.
- No source diffing yet.
- No automatic KB/source-list update.
- No Notion mirror.
- No public proof, client deliverable, or external communication.
- No autonomous research agent.

## Follow-Up

Run the first real source-freshness dry run against a small approved source set,
review the noise level, then decide whether the next iteration should add
structured source configs, deduplication, source snapshots, or richer search
result parsing.
