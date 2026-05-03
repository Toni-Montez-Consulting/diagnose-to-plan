---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Steward Receipt: Memory Control Plane Priority

Date: 2026-05-02

Owner repo: `diagnose-to-plan`

## Trigger

Toni asked whether QuickBooks can be connected, noted Notion Premium was
upgraded, and asked for an honest answer about whether Codex can handle the
volume of ideas, planning, execution, client follow-ups, and infrastructure
without losing context.

## Honest Answer

Codex can handle the current load if the operating memory is artifact-first.

Codex should not be the only memory. Chat context, tool availability, live inbox
state, and repo state can drift. The practice needs DTP and Notion discipline
before more infrastructure.

## Decision

Make the memory control plane Priority 1 before more automation:

- DTP remains source of truth.
- Notion remains phone cockpit and idea inbox.
- QuickBooks stays gated as a future read-only financial input.
- New ideas, replies, meetings, decisions, blockers, and proof gates must become
  DTP artifacts before they become implementation or public claims.

## Implemented

- Added `docs/PRACTICE_MEMORY_CONTROL_PLANE.md`.
- Added `practice-os/templates/memory-control-checkpoint.md`.
- Updated the connector map with current Gmail, Calendar, Notion, GitHub, and
  QuickBooks boundaries.
- Added roadmap/backlog pointers so future sessions treat memory control as an
  operating requirement.

## Boundaries

- No QuickBooks OAuth was created.
- No QuickBooks credentials, realm IDs, exports, financial records, or tokens
  were stored.
- No Notion private data or raw client material was mirrored.
- No hosted DTP, two-way Notion sync, live command runner, or write-enabled
  financial connector was implemented.

## Next Gate

Use the memory control checkpoint on the next broad infrastructure session and
the next weekly Business Brain reset. After two reset cycles, decide whether the
remaining pain is human capture discipline or whether hosted DTP / connector
automation is justified.
