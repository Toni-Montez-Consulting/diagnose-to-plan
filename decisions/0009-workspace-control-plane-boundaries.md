# 0009: Workspace Control Plane Boundaries

Status: accepted

Date: 2026-05-05

## Context

The consulting workspace now spans public site work, private engagement kits, runtime intake infrastructure, prompt/routing repos, global agent skills, and adjacent project/product repos. A repo-by-repo report is useful, but it can be mistaken for a code review, client roadmap, public positioning asset, or permission to activate too many lanes at once.

The practice needs a firmer internal control-plane boundary: one place to decide lane ownership, proof movement, stability criteria, allowed work, and no-touch areas without turning Hub, consulting, or project repos into the source of truth.

## Decision

DTP is the practice source of truth for roadmap sequencing, proof governance, Business Brain, Kaizen, steward receipts, and workspace reporting.

`diagnose-to-plan/engagements` is the private nested client-truth lane. Public DTP docs may summarize status, blockers, and gates, but raw private client material stays in the private lane.

Hub is runtime and intake support. It may own runtime records, console behavior, webhook/cron support, prompt execution evidence, and Supabase runtime state. It is not the practice CRM, DTP replacement, proof owner, accounting system, or client portal by default.

Consulting is the public storefront and cleared proof surface. It receives only proof and copy that passed DTP evidence, permission, redaction, reviewer, and caveat gates.

Public assistants remain gated until their source corpus, refusal behavior, logging/analytics boundary, handoff path, route smoke, and proof posture are accepted. Assistant QA can prepare the gate, but it does not authorize runtime or retrieval work.

Write-enabled cross-repo runners remain parked. The Workspace Command Center and workspace reports stay read-only until a separate accepted decision authorizes live git/CI reads or command execution.

## Consequences

- The workspace report can act as an internal control plane without becoming a client deliverable.
- Repo-local roadmaps remain authoritative for implementation details inside their lanes.
- DTP remains the promotion path for proof, client truth summaries, and cross-repo prioritization.
- Hub expansion must justify itself as runtime support, not as default business infrastructure.
- Public proof and assistant behavior remain human-reviewed and gate-driven.
- Future agents have a firm boundary before proposing automation, CRM behavior, public proof movement, or cross-repo mutation.
