---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Idea Evolution Record - Practice Evolution status dashboard V0

## Record Metadata

- Record id: 2026-05-10-practice-evolution-status-dashboard-v0
- Created: 2026-05-10
- Updated: 2026-05-10
- Source: codex
- Source date: 2026-05-10T01:55:48+00:00
- Owner: Toni
- Owning repo/lane: diagnose-to-plan
- Sensitivity: internal-only
- Current state: working_memory
- Source Kaizen id: 
- Tags: practice-evolution, dashboard, status, internal-os

## Original Signal

- Original wording / summary: Toni chose a status dashboard for now and asked for it to scale naturally if the dashboard needs to grow later.
- Source path / email / meeting / repo evidence: Current Practice Evolution implementation thread
- What prompted the idea: The V0 system had capture and status commands, but no easy visual way to see what had been captured, promoted, parked, or left for review.

## Current Interpretation

- What this really means: Add a local static status dashboard generated from DTP evolution records.
- Why it matters: It turns the system from "capture exists" into "captured work is visible and reviewable."
- What it could improve: Reduces the chance that lightweight captures stay invisible, stale, or disconnected from later decisions.
- What should not be inferred: This is not a hosted app, Notion sync, autonomous promotion engine, public site surface, or client communication channel.

## Usefulness Test

| Question | Answer |
|---|---|
| Does this solve a real recurring problem? | Yes. Valuable ideas were being captured, but Toni needed a visible place to see the state of those ideas. |
| Does this compound across projects or clients? | Yes. The same capture -> review -> promote path can govern consulting, client lessons, messaging, research, and agent behavior. |
| Does this preserve Toni's ambition and judgment? | Yes. It keeps ambitious ideas visible while keeping promotion human-gated. |
| Does this reduce future confusion, rework, or missed context? | Yes. It gives future agents a concrete register before deciding what to build next. |
| What would make this worth building ambitiously? | Repeated use that proves dashboard filters, review states, batch promotion, and mirror-safe summaries are needed. |

## Review Lenses

- [ ] Consulting Strategy
- [ ] External Communications
- [ ] Product Strategy
- [x] UX / Design
- [ ] Software Architecture
- [x] Software Engineering
- [ ] DevOps / Infrastructure
- [x] QA / Audit
- [ ] General Counsel
- [x] COO
- [ ] Controller

## Boundary Check

- Public proof risk: Low if kept internal and generated from sanitized DTP records only.
- Client privacy risk: Low for this first slice; no raw client facts should enter dashboard records.
- Legal / COI / compliance risk: Low; dashboard must not publish proof or create client-facing claims.
- Security / credential risk: Low; dashboard must not read secrets, credentials, connectors, or live systems.
- Money movement or commitment risk: None.
- What requires Toni approval: Hosted dashboard, Notion mirror, client-facing view, automated promotion, or cross-repo write behavior.

## Promotion Review

- Recommended promotion level: working_memory
- Evidence supporting promotion: Toni explicitly selected the status-dashboard-first path and asked for natural scale potential.
- Evidence limits: This has not yet been used across multiple weeks or with client-derived records.
- Reviewer: Toni
- Approved level: working_memory
- Next review trigger: After the generated dashboard is used in at least one additional evolution review or batch capture session.

## Next Artifact

- None
- Message / pitch candidate
- Research pattern candidate
- Practice pattern
- Template update
- Agent/skill instruction update
- Roadmap/backlog item
- Client-delivery artifact
- Public-copy brief
- Implementation plan

## Close / Supersede Condition

- Close when: The CLI can generate a readable dashboard from multiple evolution records and tests cover the command.
- Supersede when: A richer review room becomes the accepted cockpit.
- Park if: The record workflow does not generate enough usage to justify a dashboard.

## Notion Mirror Summary

Safe to mirror: no

If yes:

- Topic:
- State:
- Next action:
- DTP source path: practice-os/evolution/records/2026-05-10-practice-evolution-status-dashboard-v0.md

## Notes

Raw capture is not reusable playbook memory. Promote only after review.
