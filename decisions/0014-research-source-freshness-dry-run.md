# Decision 0014: Research Source Freshness Dry-Run V0

Date: 2026-05-10

Status: Accepted

## Context

The first autonomy-readiness review selected Research source freshness as the
first internal Practice OS workflow that can move toward A4 bounded scheduled
workflow behavior, but only as a dry-run design candidate.

DTP already has a Research Arm source list, Research Steward, decision
templates, research pattern candidates, and a Practice Operating Review Loop.
The missing piece is a queue shape that lets the practice review source changes
without creating a crawler, public-claim feed, or autonomous updater.

## Decision

Add `docs/RESEARCH_SOURCE_FRESHNESS_DRY_RUN_V0.md` as the required dry-run spec.

Add `practice-os/templates/research-source-freshness-item.md` for promoted,
reviewed queue items.

Add `practice-os/research/source-freshness/README.md` as the folder boundary
for reviewed source-freshness records.

## Consequences

- Research source freshness has a concrete next build path.
- Raw dry-run output stays ignored under `outputs/research-source-freshness/`.
- Reviewed, sanitized items can be promoted into DTP.
- No scheduled job, crawler, Notion sync, public claim, client communication,
  tool install, or repo mutation is approved.

## Non-Goals

- No autonomous runtime.
- No live public-source browsing command yet.
- No scheduled sweep.
- No digest publication.
- No public consulting copy or proof movement.
- No source-of-truth shift away from DTP.

## Follow-Up

The next implementation candidate is a local dry-run command or script that
accepts source snapshots/operator notes and emits schema-validated queue items
under `outputs/research-source-freshness/`.
