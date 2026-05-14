---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Research Pattern Candidate - Hub-first intake with DTP source of truth

## Candidate Metadata

- Candidate id: 2026-05-14-hub-first-intake-dtp-source-of-truth
- Created: 2026-05-14
- Source: consulting live funnel closeout and Workspace OS pilot scan
- Source type: repo_evidence
- Sensitivity: internal-only
- Reviewer: Toni
- Status: draft
- Owning repo/lane: diagnose-to-plan / consulting / hub
- Source Kaizen id:

## Observation

- What was observed: The consulting `/start` path can submit to Hub while DTP remains the place where the submission is interpreted, routed, and turned into the next Practice OS artifact.
- Where it showed up: `practice-os/efficiency/consulting-evidence-index.md`, `practice-os/steward/2026-05-11-live-funnel-closeout-receipt.md`, `practice-os/steward/2026-05-11-live-intake-operator-workflow-receipt.md`, and `docs/CONSULTING_WORKSPACE_OS_V0.md`.
- Why it caught attention: It keeps the runtime useful without letting Hub become the CRM, the methodology owner, or the source of truth for practice decisions.
- Who or what type of operator it may apply to: Founder-operators and consultants who need lightweight runtime intake but want method, proof, and decisions to stay in a durable operating system.

## Underlying Principle

- What seems to be true: A runtime record is useful only after the operating system decides what it means and what should happen next.
- What business or human behavior is underneath it: People often confuse "the form works" with "the business process works"; this pattern separates storage from judgment.
- What would make the principle false: If Hub becomes the accepted source of truth for triage, proof, handoff, or client status without a DTP decision.

## Consulting Translation

- How this changes discovery: Ask where a submission lands, who interprets it, and what artifact proves the next decision.
- How this changes diagnosis: Treat "we collect leads" as incomplete until route, owner, approval gate, and follow-up artifact are named.
- How this changes delivery or handoff: Hand off both the runtime path and the DTP decision path, so operators know where records live and where decisions live.
- How this changes messaging or client education: Explain that the value is not the form alone; it is the intake-to-decision loop.
- What Toni should watch for next time: Any client system where a tool captures requests but no one owns triage, routing, follow-up, or proof boundaries.

## Implementation Notes

- Problem: A working public form can still leave the business with scattered follow-up and unclear ownership.
- Context: Consulting owns public `/start`; Hub owns runtime storage; DTP owns triage, proof, decisions, and reusable methodology.
- Solution: Keep Hub as intake/runtime support and use DTP artifacts to decide fit, route, next artifact, approval gates, and handoff.
- Tools and dependencies: consulting site, Hub intake runtime, DTP live-intake workflow, prospect-intake triage template.
- Verification: Live smoke receipts show synthetic intake reached Hub; the operator workflow receipt records the DTP-first decision model.
- Handoff notes: Future agents should not copy private Hub rows into tracked docs. Summarize fields only and route real prospects through DTP triage.

## Integrity Check

- What could go wrong if this pattern is misused: Hub could quietly become the CRM/source of truth and split decisions away from DTP.
- Does this create dependency on Toni: Moderate risk if only Toni knows how to interpret rows; reduced by triage templates and source boundaries.
- Does this increase clarity or complexity: It increases clarity when source-of-truth roles are documented; it adds complexity if every intake creates too many artifacts.
- Does this respect the user's time and data: Yes, if only necessary context is collected and private row details stay out of public/repo docs.
- What would prove this works: A real prospect intake can be summarized, routed, followed up, and reviewed without re-reading raw rows or chat history.
- What is the simpler version: A form plus a manual checklist.
- What is the safer version: DTP triage from summarized fields only, with no raw private row storage in tracked docs.
- What should be documented before this ships: Runtime owner, DTP owner, source-of-truth boundary, approval gates, and cleanup posture.

## Possible Artifact

- Practice pattern
- Workflow map
- Operator checklist
- Blueprint section

## Evidence Limits

- What evidence supports this: Production synthetic smoke receipts and DTP operator workflow artifacts.
- What is anecdotal or unproven: Real prospect conversion quality and long-term operator load are not proven yet.
- What cannot be claimed publicly: Do not claim client outcomes, conversion lift, CRM maturity, or automated cleanup.
- Privacy / proof / COI boundary: Internal-only; no private Hub row screenshots, raw submissions, or public proof claims.

## Next Experiment

- Where to test this next: The next real prospect intake or a controlled Business Brain weekly reset.
- What signal would confirm it is useful: Toni or a future agent can identify route, next action, and approval gates from the DTP artifact without opening raw Hub rows.
- What signal would make us drop it: The DTP artifact adds overhead without improving follow-up quality or decision clarity.

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
- DTP source path: practice-os/research/pattern-candidates/2026-05-14-hub-first-intake-dtp-source-of-truth.md

## Notes

Draft only. Promotion into public copy, client advice, offer language, pricing,
or playbook memory requires review.
