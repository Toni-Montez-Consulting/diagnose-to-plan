---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Admin Surface Operating Room Pattern

Status: reusable internal pattern.

Pattern: public proof surface outside, protected operating room inside, handoff
record after shipping.

## When This Pattern Applies

Use this pattern when a site, app, or workflow has a public-facing surface but
the real owner value depends on private triage, task routing, operating notes,
proof state, launch gates, or recurring admin work.

Good candidates:

- owner/admin workflows after launch;
- intake triage and follow-up queues;
- launch readiness and proof gates;
- recurring booking, content, approval, or support routines;
- handoff rooms where someone else needs to operate the system.

Do not apply it just because an admin portal sounds impressive. Start with
`practice-os/templates/client-command-room-fit-assessment.md`.

## Current Evidence

| Surface | Role in the pattern | Boundary |
|---|---|---|
| `consulting` `/admin` | noindex launcher/status surface for Hub routing, intake triage, and DTP links | public-safe only; no private DTP records |
| Hub console | private runtime support for intake rows, prompts, captures, runs, and Supabase-backed operations | runtime support; not DTP source of truth |
| DeMario admin | owner-facing local-business operations reference | owner/private data redaction required before proof |
| CCAAP owner workflow | candidate nonprofit operating-kit path | blocked on owner inputs and permission |

## Reusable Shape

1. Public surface states the offer, proof, or intake path without private data.
2. Protected operating room keeps triage, private records, owner tasks, and
   runtime state out of public routes.
3. DTP records the decision, proof gates, redaction posture, and handoff notes.
4. Project repo owns implementation details for its app/site.
5. Handoff record names owner, operator, access, failure modes, next actions,
   and stale-after date.

## Build Checklist

- [ ] Fit assessment says recurring owner/admin work exists.
- [ ] Public/private boundary is named.
- [ ] Source of truth is named: project repo, DTP, Hub, or private kit.
- [ ] No private rows, payment details, credentials, or client records appear on
      the public side.
- [ ] Handoff record exists before claiming the system is operational.
- [ ] Proof movement goes through the proof promotion runbook.
- [ ] The operating room has a maintenance owner and a stale-after review date.

## Reuse Warning

This is a pattern, not a mandate. A checklist, spreadsheet, private markdown kit,
or one-off runbook can be the correct operating room if code would add more
maintenance than value.

