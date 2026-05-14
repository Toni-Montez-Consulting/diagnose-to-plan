---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Research Pattern Candidate - Preview-to-production ladder

## Candidate Metadata

- Candidate id: 2026-05-14-preview-to-production-ladder
- Created: 2026-05-14
- Source: Vercel deployment model, DTP Workspace OS, consulting/Hub release history
- Source type: tool_signal
- Sensitivity: internal-only
- Reviewer: Toni
- Status: draft

## Observation

- What was observed: Vercel's Local, Preview, and Production environment model makes review state explicit and gives every deployment a URL or evidence point.
- Where it showed up: Vercel deployment docs, consulting production smoke receipts, Hub intake deployment work, and UAT Kit claim-level language.
- Why it caught attention: Toni likes the feeling of Vercel because it turns deployment into a visible workflow instead of an invisible infrastructure chore.
- Who or what type of operator it may apply to: Builders and clients who need to know whether a change is local-only, preview-ready, production-ready, operator-ready, or public-proof-ready.

## Underlying Principle

- What seems to be true: Work feels safer when every readiness claim has an environment and evidence level.
- What business or human behavior is underneath it: People blur "I saw it work" with "it is ready"; named levels reduce that drift.
- What would make the principle false: If the labels become ceremony and no one verifies the actual environment.

## Consulting Translation

- How this changes discovery: Ask what level of readiness the client needs before deciding scope.
- How this changes diagnosis: Separate demo readiness, production readiness, owner readiness, and public proof.
- How this changes delivery or handoff: Record the environment, URL, commit, checks, caveats, and rollback path.
- How this changes messaging or client education: Explain progress as "preview-ready" or "production-ready" instead of vague "almost done."
- What Toni should watch for next time: Any request that tries to skip from local confidence to public or client-facing claims.

## Possible Artifact

- Checklist
- UAT receipt mode
- Practice pattern
- Client education note
- Operator checklist

## Evidence Limits

- What evidence supports this: Official Vercel docs and repeated workspace deployment receipts.
- What is anecdotal or unproven: Whether every client lane needs a full preview receipt.
- What cannot be claimed publicly: Do not imply Vercel is required or that a preview proves business outcome.
- Privacy / proof / COI boundary: Internal operating pattern only.

## Next Experiment

- Where to test this next: Hub cleanup PR follow-through or Omnexus release proof.
- What signal would confirm it is useful: Future agents can name claim level and evidence before saying "ready."
- What signal would make us drop it: The receipt duplicates UAT without changing decisions.

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
- DTP source path: practice-os/research/pattern-candidates/2026-05-14-preview-to-production-ladder.md

## Notes

Keep draft until tested on one more non-consulting or runtime lane.

