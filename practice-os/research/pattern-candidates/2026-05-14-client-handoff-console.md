---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Research Pattern Candidate - Client handoff console

## Candidate Metadata

- Candidate id: 2026-05-14-client-handoff-console
- Created: 2026-05-14
- Source: Vercel/Supabase dashboard ergonomics, CCAAP/DeMario/admin command-room patterns
- Source type: tool_signal
- Sensitivity: internal-only
- Reviewer: Toni
- Status: draft

## Observation

- What was observed: Strong platforms expose useful operating state without forcing users to read implementation guts. Workspace admin surfaces work best when they show decisions, tasks, ownership, and next action instead of raw schema.
- Where it showed up: Vercel project/deployment dashboards, Supabase Studio mental model, consulting noindex admin command room, DeMario admin surface, and CCAAP owner-handoff work.
- Why it caught attention: Client handoff quality depends on whether the client can operate the thing after launch.
- Who or what type of operator it may apply to: Small business owners, nonprofit operators, founders, and internal admins.

## Underlying Principle

- What seems to be true: Handoff surfaces should translate system state into operator decisions.
- What business or human behavior is underneath it: Clients do not want a database; they want confidence about what to do next.
- What would make the principle false: If the client already has a mature operating system and only needs technical docs.

## Consulting Translation

- How this changes discovery: Ask what the client must operate after Toni leaves.
- How this changes diagnosis: Identify whether the client needs a full portal, a lightweight console, or just a runbook.
- How this changes delivery or handoff: Build or document a task-based console only where it reduces dependency.
- How this changes messaging or client education: Position handoff as capability transfer, not hostage-taking support.
- What Toni should watch for next time: Requests for portals when the real need is a status page, checklist, or owner runbook.

## Possible Artifact

- Workflow map
- Operator checklist
- Client education note
- Practice pattern
- Blueprint section

## Evidence Limits

- What evidence supports this: Existing command-room and handoff patterns across consulting, CCAAP, and DeMario plus platform dashboard examples.
- What is anecdotal or unproven: The exact console shape for each client.
- What cannot be claimed publicly: Do not claim a reusable client portal product exists until it is built and proven.
- Privacy / proof / COI boundary: Keep internal admin/client data out of public surfaces.

## Next Experiment

- Where to test this next: CCAAP handoff after owner inputs or Greg post-meeting action plan if approved.
- What signal would confirm it is useful: Client can answer "what do I do next?" without Toni narrating the whole system.
- What signal would make us drop it: A simple checklist is enough and a console would overbuild.

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
- DTP source path: practice-os/research/pattern-candidates/2026-05-14-client-handoff-console.md

## Notes

Use the surface translation standard before anything becomes client-facing.

