---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Research Pattern Candidate - Status visibility prevents lightweight capture drift

## Candidate Metadata

- Candidate id: 2026-05-10-status-visibility-prevents-lightweight-capture-drift
- Created: 2026-05-10
- Source: codex
- Source type: research
- Sensitivity: internal-only
- Reviewer: Toni
- Status: promoted
- Owning repo/lane: diagnose-to-plan
- Source Kaizen id: 

## Observation

- What was observed: Status visibility prevents lightweight capture drift.
- Where it showed up: Practice Evolution V0 moved from templates and CLI records into a generated status dashboard.
- Why it caught attention: Toni correctly noticed that lightweight first slices can remain shallow if the system never returns to build on them.
- Who or what type of operator it may apply to: Founder-operators, consultants, product builders, and anyone using AI-assisted planning across many workstreams.

## Underlying Principle

- What seems to be true: Capture only becomes durable when the operator can see state, next review, and promotion path.
- What business or human behavior is underneath it: People trust systems more when they can inspect what is waiting, what is active, and what is intentionally parked.
- What would make the principle false: If the dashboard becomes stale, too noisy, or disconnected from actual decisions.

## Consulting Translation

- How this changes discovery: Ask where ideas and decisions will be visible after the conversation ends.
- How this changes diagnosis: Look for invisible queues, stale drafts, and unclear promotion criteria as operating-system risks.
- How this changes delivery or handoff: Include status surfaces with enough fields to keep future work from disappearing.
- How this changes messaging or client education: Explain that the value is not just capturing ideas, but turning them into visible, reviewable operating memory.
- What Toni should watch for next time: Moments where a client says "we talked about this before" but no one knows where the decision lives.

## Possible Artifact

- None
- Discovery question
- Checklist
- Workflow map
- Blueprint section
- Offer component
- Client education note
- Visual / infographic
- Practice pattern
- Template update
- Research digest
- Roadmap item

## Evidence Limits

- What evidence supports this: Toni's repeated concern that ideas and meta-patterns should not be forgotten, plus the decision to add a status dashboard.
- What is anecdotal or unproven: The dashboard has not yet been used long enough to prove retention or execution lift.
- What cannot be claimed publicly: Do not claim measured productivity, retention, or client outcomes.
- Privacy / proof / COI boundary: Keep examples sanitized and internal unless proof is explicitly cleared.

## Next Experiment

- Where to test this next: Practice Evolution reviews, Research Arm patterns, Opportunity OS records, and later client-delivery mini dashboards.
- What signal would confirm it is useful: Toni or a future agent can quickly see captured items, open states, and the correct next action without re-reading chat.
- What signal would make us drop it: The dashboard adds upkeep without improving recall, decision quality, or follow-through.

## Promotion Decision

- Recommended state: promoted
- Reviewer: Toni
- Approved state: promoted
- Destination if promoted: practice-os/patterns/status-surface-before-scale.md

## Notion Mirror Summary

Safe to mirror: no

If yes:

- Pattern name:
- Why it matters:
- Next action:
- DTP source path: practice-os/research/pattern-candidates/2026-05-10-status-visibility-prevents-lightweight-capture-drift.md

## Notes

Promoted internally on 2026-05-10 as
`practice-os/patterns/status-surface-before-scale.md`.

This remains internal-only. It can later become a high-level client explanation,
but public copy, claims, examples, and proof require the normal review gates.
