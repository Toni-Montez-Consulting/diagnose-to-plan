---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice Knowledge Base V1

Status: markdown-first knowledge base design for the Practice OS.

Owner repo: `diagnose-to-plan`

## Position

Knowledge Base V1 is not a vector database. It is the source discipline that
makes vector retrieval useful later.

Knowledge-base maintenance starts with event-based markdown updates, not
autonomous agents. Use `docs/KNOWLEDGE_BASE_EVENT_WORKFLOWS_V0.md` when a
research signal, memory pattern, operating workflow, client reply, project
execution lesson, or agent-system miss should update, refine, expand, park, or
supersede a knowledge surface.

V1 should help a future agent answer:

- what is authoritative;
- what changed recently;
- what is private or blocked;
- what gate controls action;
- what prior work is reusable;
- where the handoff receipt lives.

## Core Object Types

| Object | Purpose | Public DTP location | Private location |
|---|---|---|---|
| Source Index | names authoritative sources, freshness, blocked sources | templates and sanitized receipts | private engagement kits |
| Client OS Packet | meeting/prep/receipt loop | sanitized lane map | private engagement kit |
| Business Justification Scorecard | explains why a work item matters | templates and non-sensitive receipts | private engagement kit if client-specific |
| Approval Gate | records allowed action and stop conditions | templates and sanitized receipts | private engagement kit if sensitive |
| Handoff Receipt | makes the session recoverable | steward receipt when public-safe | private engagement kit when sensitive |
| Architecture Review Packet | maps systems, ownership, risks, and next sequence | DTP system docs | repo-local docs if implementation-specific |
| Automation Authority Matrix | clarifies draft/read/write/act boundaries | DTP docs and templates | private runbooks when sensitive |
| Memory Promotion Record | promotes raw facts into reusable patterns | DTP steward/pattern docs | private vault for sensitive examples |
| Knowledge Base Event Record | explains why a knowledge surface changed or did not change after a meaningful event | `practice-os/templates/knowledge-base-event-record.md` outputs and steward receipts | private vault when the trigger is client-sensitive |

## Minimum Metadata

Every V1 record should carry:

- `data_class`;
- `confidential`;
- `permission_level`;
- `review_status`;
- owner repo or vault;
- source freshness;
- next review trigger;
- blocked sources;
- action authority.
- event trigger and decision record when a knowledge-base update is source- or
  workflow-driven.

## Validation Rules

The first validation pass should detect:

- source index missing from a squad-run work item;
- receipt missing owner or next action;
- approval gate left `pending` while public proof is being considered;
- stale roadmap pointer to moved docs;
- private source referenced from public DTP without a sanitized boundary;
- hosted/vector/memory work proposed without the persistence ladder.

## Hosted DTP Path

Hosted DTP should model the markdown shapes after repeated use. V1 should not
force a schema before the Greg, CCAAP, and Cam loops reveal the real friction.

Recommended sequence:

1. Manual markdown loops.
2. Add doctor/status checks for missing records.
3. Test one Hosted DTP Phase 0.2 round trip with markdown fallback.
4. Reconcile schema fields from repeated records.
5. Persist hosted records only after import/export and RLS behavior are clear.

## Do Not Do Yet

- Do not ingest private client data into a public vector store.
- Do not treat chat memory as source of truth.
- Do not make Notion the knowledge base.
- Do not add autonomous memory promotion.
- Do not design hosted schema from one example.

