---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Research Pattern Candidate - Post-submit Diagnostic Call gating

## Candidate Metadata

- Candidate id: 2026-05-14-post-submit-diagnostic-call-gating
- Created: 2026-05-14
- Source: consulting live funnel closeout and Workspace OS pilot scan
- Source type: repo_evidence
- Sensitivity: internal-only
- Reviewer: Toni
- Status: draft
- Owning repo/lane: diagnose-to-plan / consulting
- Source Kaizen id:

## Observation

- What was observed: The public `/start` path hides the Diagnostic Call CTA until after intake submission, then shows the approved scheduling path after the prospect has provided context.
- Where it showed up: `practice-os/steward/2026-05-11-live-funnel-closeout-receipt.md`, `docs/LIVE_INTAKE_TO_PRACTICE_OS_WORKFLOW_V0.md`, and `docs/CONSULTING_WORKSPACE_OS_V0.md`.
- Why it caught attention: It keeps the call from becoming a generic booking route and makes the intake form do the first qualification pass.
- Who or what type of operator it may apply to: Consultants, service businesses, and founder-operators who need qualification before scheduling.

## Underlying Principle

- What seems to be true: A meeting link is stronger after context capture because the call can confirm a path instead of starting from zero.
- What business or human behavior is underneath it: Easy scheduling can create low-context calls, weak fit, and avoidable follow-up friction.
- What would make the principle false: If the intake is too long, confusing, or blocks serious buyers who already know what they need.

## Consulting Translation

- How this changes discovery: Ask what the call is supposed to decide and what context must exist before booking.
- How this changes diagnosis: Separate "needs a conversation" from "needs a route decision after minimal context."
- How this changes delivery or handoff: Document the public label, internal route value, and post-submit conditions.
- How this changes messaging or client education: Explain that the form protects the buyer's time by making the call useful.
- What Toni should watch for next time: Prospects who need a direct relationship path, referral path, or urgent bypass.

## Implementation Notes

- Problem: Public booking links can create vague calls and make the first conversation do too much basic intake.
- Context: Consulting uses `Diagnostic Call` as the public label and `fit-call` as an internal route value.
- Solution: Hide booking before submission; show the approved call path only after the prospect submits context.
- Tools and dependencies: consulting `/start`, Hub intake, DTP follow-up drafting playbook, prospect triage template.
- Verification: Live browser smoke confirmed normal `/start` hid the booking CTA and post-submit state showed it.
- Handoff notes: Do not create calendar events or send follow-ups automatically. Follow-up remains human-reviewed.

## Integrity Check

- What could go wrong if this pattern is misused: It could become a gatekeeping gimmick or hide the next step from serious buyers.
- Does this create dependency on Toni: Low to moderate; the route logic is documented, but judgment still matters for fit and urgency.
- Does this increase clarity or complexity: It increases clarity when the intake is short and the post-submit next action is obvious.
- Does this respect the user's time and data: Yes, if the intake asks only for what is needed to make the call useful.
- What would prove this works: Real prospects submit enough context that the Diagnostic Call can decide route, artifact, or no-fit faster.
- What is the simpler version: Public booking link plus a required pre-call questionnaire.
- What is the safer version: Keep a manual bypass path for referrals, urgent cases, or known buyers.
- What should be documented before this ships: Public label, internal route, post-submit behavior, follow-up owner, and no-auto-send boundary.

## Possible Artifact

- Discovery question
- Operator checklist
- Practice pattern
- Client education note

## Evidence Limits

- What evidence supports this: Public flow behavior was smoke-tested with synthetic data.
- What is anecdotal or unproven: Real conversion quality and buyer reaction are not proven yet.
- What cannot be claimed publicly: Do not claim higher conversion, better buyer fit, or reduced sales time without evidence.
- Privacy / proof / COI boundary: Internal-only until real prospect evidence is reviewed and sanitized.

## Next Experiment

- Where to test this next: The first real prospect who submits `/start` and books through the post-submit path.
- What signal would confirm it is useful: The call starts with a clear route hypothesis and fewer basic discovery questions.
- What signal would make us drop it: Qualified prospects abandon because they cannot easily schedule.

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
- DTP source path: practice-os/research/pattern-candidates/2026-05-14-post-submit-diagnostic-call-gating.md

## Notes

Draft only. Promotion into public copy, client advice, offer language, pricing,
or playbook memory requires review.
