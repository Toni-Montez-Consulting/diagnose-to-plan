---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Steward Receipt: Tooling Steward Idea Capture

Date: 2026-05-02

Owner repo: `diagnose-to-plan`

## Trigger

Toni asked whether there should be a manager for connected plugins and tools
that evaluates usefulness, missing tools, omitted tools, additions, removals,
and overall fit.

## Decision

Yes. Add a Tooling Steward pattern as a sibling to the Practice Memory Control
Plane.

The Tooling Steward should periodically evaluate tool usefulness, auth state,
data risk, source-of-truth fit, maintenance burden, verification maturity, and
whether a tool should be active, manual, researched, piloted, parked, removed,
or blocked.

## Implemented

- Added `docs/PRACTICE_TOOLING_STEWARD.md`.
- Added `practice-os/templates/tooling-steward-review.md`.
- Updated the Practice Memory Control Plane to call out tool review as part of
  the weekly/monthly operating rhythm.
- Updated the roadmap/backlog with a Tooling Steward review story.

## Boundaries

- No tools were installed.
- No tool permissions were changed.
- No accounts were connected or revoked.
- No credentials, tokens, account IDs, or private vendor data were stored.

## Next Gate

Run the first full Tooling Steward review after two Business Brain reset cycles,
or earlier if Toni wants to evaluate a specific connector such as QuickBooks,
Canva, Vercel, Supabase, or a Notion Premium feature.
