---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Agent Memory Optimization Steward Receipt

Date: 2026-05-02

## Trigger

Toni asked whether Codex memory can be optimized and whether persistent storage
would help the practice operate better without losing ideas, planning, or
execution state.

## Decision

Use a staged memory strategy instead of jumping straight to a database or
vector store.

1. DTP remains the source of truth.
2. Notion remains the cockpit and inbox.
3. Session rehydration becomes an explicit checklist.
4. Local DTP recall/index stays the first retrieval improvement.
5. Hosted DTP/private storage waits for the accepted hosted-DTP implementation
   gate and real repeated pain.
6. Vector retrieval or MCP recall waits for approved corpora, redaction rules,
   refusal tests, and eval examples.

## Artifacts Added

- `docs/PRACTICE_MEMORY_OPTIMIZATION_PLAN.md`
- `practice-os/templates/session-rehydration-checklist.md`
- `practice-os/templates/memory-source-index.md`

## Artifacts Updated

- `docs/PRACTICE_MEMORY_CONTROL_PLANE.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/ROADMAP_EXECUTION_BACKLOG.md`

## Current Answer For Toni

Persistent storage is useful, but not as the first move. The practice should
optimize source-aware rehydration first, then use hosted/private records only
when markdown, git, steward receipts, ignored kits, Notion cockpit, and local
DTP recall are no longer enough.

## Gates

- No raw transcript memory store.
- No vector database before corpus ownership and redaction rules.
- No Notion source-of-truth promotion.
- No QuickBooks OAuth connector until the connector boundary is accepted.
- No private assistant/MCP recall until refusal tests and eval examples exist.

## Next Use

Use `practice-os/templates/session-rehydration-checklist.md` at the start of the
next broad infrastructure or multi-client session.
