---
title: "Practice OS source material is preserved and integrated additively"
date: 2026-05-02
status: accepted
---

# Decision: New Practice OS source docs do not replace current DTP architecture

## Context

Toni added new source material for the Practice OS and AI/software
implementation layer:

- `docs/source/practice_os_build_spec_v0_1.md`
- `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md`
- `database/schema/practice_os_schema_v0_1.sql`

The material sharpens the product thesis, core loop, module names, memory
levels, and starter schema. DTP already has an accepted local-first architecture
with private engagement kits, steward receipts, proof/redaction governance,
memory control, and a gated hosted-DTP Phase 0 boundary.

## Decision

Preserve the new documents as additive source material and integrate them
through source indexing, integration mapping, concept registry, conflict
tracking, and reprioritization logs.

Do not replace the existing DTP architecture with the new source material.

## Consequences

- The source docs keep their strategic nuance.
- DTP remains local-first and markdown-first until hosted implementation is
  explicitly opened.
- The SQL file is a schema starter, not a runnable migration.
- Hosted DTP schema/app work remains gated by `docs/HOSTED_DTP_PHASE_0.md`.
- Client-facing portal work remains deferred until repeated client patterns
  justify it.
- Autonomous agents and unmanaged self-learning remain blocked.
- Durable reusable memory remains human-approved.

## Follow-Up

- Create additive templates for Thought Inbox, Input Studio, Context Pack,
  Opportunity Score, Exception Register, Value Ledger, and Memory Review Queue.
- Reconcile the starter schema against Hosted DTP Phase 0 before database work.
