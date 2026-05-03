---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice OS Source Integration Map

This map integrates the 2026-05-02 source material without replacing existing
DTP architecture.

## Existing Repo Summary

`diagnose-to-plan` is already the internal Practice OS source of truth. It is a
local-first Python CLI and local Workbench backed by markdown artifacts,
private ignored engagement kits, redaction/proof governance, steward receipts,
Business Brain command contracts, and a gated hosted-DTP roadmap.

The new source material reinforces the current direction. It does not require
an immediate app rewrite, client portal, autonomous agent system, unmanaged
self-learning loop, or runtime schema migration.

## Reinforcements

| Source idea | Existing DTP support |
|---|---|
| Practice OS as internal operating system | `CLAUDE.md`, `docs/PRACTICE_PRODUCTION_ROADMAP.md`, `practice-os/`, `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md` |
| Local/manual first before hosted product | `README.md`, `docs/01-architecture.md`, `docs/HOSTED_DTP_PHASE_0.md` |
| No generic SaaS dashboard | `decisions/0004-hosted-dtp-private-practice-os-boundary.md`, hosted-DTP docs |
| Human-approved durable memory | `docs/PRACTICE_MEMORY_CONTROL_PLANE.md`, `docs/PRACTICE_MEMORY_OPTIMIZATION_PLAN.md` |
| Client-specific private work stays private | ignored `engagements/`, `dtp vault`, `decisions/0005-private-engagement-durability.md` |
| Clarify -> plan -> build -> handoff loop | Practice OS templates, Client Operating Kits, recurring cadence, reply intake |
| Proof and claims need review | proof/redaction templates, public-claim review, permission reviewer checklist |
| Agents assist but do not act autonomously | `CLAUDE.md`, Business Brain role specs, roadmap autonomy gates |

## New Or Sharpened Concepts

| Concept | What the source adds | Additive DTP move |
|---|---|---|
| Thought Inbox | A named raw-input capture surface for fleeting ideas, notes, transcripts, lessons, and observations. | Manual template exists; later wire to CLI/workbench if repeated use proves value. |
| Input Studio | A named transformation layer from raw human input into structured context without losing voice. | Manual template exists and should map to Business Brain command contracts during real use. |
| Context Pack | The complete-enough package that lets AI/code agents produce useful work. | Manual template exists and references source-aware context, facts, decisions, and waiting states. |
| Opportunity Scorer | Explicit score factors for prioritizing workflow opportunities. | Manual scoring template exists before spreadsheet/app behavior. |
| Anti-Slop Reviewer | Named review layer for business accuracy, user intent, specificity, assumptions, and risk. | Map into review-checklist/business fixtures and future eval garden. |
| Exception Register | Debug log for workflow/system failures that can become pattern memory. | Manual template exists; later connect to value ledger and memory review after real misses. |
| Value Ledger | Core record of time, revenue, quality, strategic, and trust value. | Manual template exists; use manually before hosted metrics. |
| Memory Review Queue | Human approval path from raw note to reusable memory. | Manual queue template exists and keeps durable memory gates explicit. |
| Reprioritization Loop | Backlog changes after meaningful events. | Use `docs/integration/reprioritization_log.md` plus roadmap steward reviews. |

## Schema Reconciliation Notes

`database/schema/practice_os_schema_v0_1.sql` is useful source material, but it
is not a migration yet.

Before schema implementation:

- Start from `docs/integration/schema_reconciliation_v0.md`, then reconcile table
  names and relationships with `docs/HOSTED_DTP_PHASE_0.md` in a merged schema
  design.
- Add private auth/RLS/storage posture from Hosted DTP Phase 0.
- Preserve local markdown import/export.
- Add redaction, proof review, evidence, artifact, and permission concepts that
  are stronger in current DTP docs than in the starter schema.
- Decide whether `value_metrics` should align with proof/evidence records or
  stay as an internal value ledger table.

## Additive-First Sequence

1. Preserve source files verbatim.
2. Create source index, integration map, concept registry, conflict register,
   reprioritization log, and ADR.
3. Add manual templates for the sharpened modules. Done as of 2026-05-02.
4. Use templates on Cam, Greg, CCAAP, or Toni's weekly reset.
5. Only then consider CLI/workbench support.
6. Hosted app/schema implementation remains a separate gated slice.

## Non-Goals

- Do not build a client-facing portal now.
- Do not build autonomous agents.
- Do not build unmanaged self-learning.
- Do not apply the SQL file as a migration.
- Do not replace current DTP architecture with a Next.js/Supabase app from the
  source docs until hosted-DTP implementation is explicitly opened.
