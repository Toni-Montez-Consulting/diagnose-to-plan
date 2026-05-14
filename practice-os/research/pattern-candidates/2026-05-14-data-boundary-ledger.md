---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Research Pattern Candidate - Data boundary ledger

## Candidate Metadata

- Candidate id: 2026-05-14-data-boundary-ledger
- Created: 2026-05-14
- Source: Supabase RLS guidance, DTP hosted app governance, Hub/consulting data-boundary work
- Source type: tool_signal
- Sensitivity: internal-only
- Reviewer: Toni
- Status: draft

## Observation

- What was observed: Supabase makes Postgres and RLS accessible enough that data boundaries can be expressed directly in the application workflow, but that power needs explicit source-of-truth, exposure, and service-role rules.
- Where it showed up: Supabase RLS docs, Hosted DTP Phase 0 governance, Hub runtime records, and public-proof redaction gates.
- Why it caught attention: A clean app can still be unsafe or unhandoffable if data ownership, access, and public surface boundaries are implicit.
- Who or what type of operator it may apply to: Builders working with client data, proof assets, admin dashboards, auth, storage, or private operational rows.

## Underlying Principle

- What seems to be true: Data design is not complete until access, ownership, exposure, and proof boundaries are documented.
- What business or human behavior is underneath it: Fast builders often model tables before modeling responsibility.
- What would make the principle false: If the lane has no persistent data, private data, auth, storage, or client proof.

## Consulting Translation

- How this changes discovery: Ask what data exists, who owns it, who can see it, and what can ever be public.
- How this changes diagnosis: Treat unclear data boundaries as a launch and handoff risk.
- How this changes delivery or handoff: Add a data-boundary ledger before production, proof movement, or client handoff.
- How this changes messaging or client education: Make data ownership and access understandable without exposing internals.
- What Toni should watch for next time: Admin dashboards, proof screenshots, client metrics, and service-role operations.

## Possible Artifact

- Checklist
- Workflow map
- Blueprint section
- Practice pattern
- UAT receipt input

## Evidence Limits

- What evidence supports this: Supabase RLS guidance and multiple workspace lanes that separate private runtime truth from public proof.
- What is anecdotal or unproven: Whether every small Supabase app needs a full ledger.
- What cannot be claimed publicly: Do not claim compliance, security certification, or data safety beyond evidence.
- Privacy / proof / COI boundary: Internal only unless a client-safe version is explicitly prepared.

## Next Experiment

- Where to test this next: Omnexus release proof or a future Hub data cleanup lane.
- What signal would confirm it is useful: It prevents private data from leaking into public proof or admin surfaces.
- What signal would make us drop it: It becomes redundant with an existing repo's security checklist.

## Promotion Decision

- Recommended state: pattern_candidate
- Reviewer: Toni
- Approved state:
- Destination if promoted: practice-os/patterns/

## Notion Mirror Summary

Safe to mirror: no

If yes:

- Pattern name:
- Why it matters:
- Next action:
- DTP source path: practice-os/research/pattern-candidates/2026-05-14-data-boundary-ledger.md

## Notes

Use with Integrity Layer and proof/redaction gates.

