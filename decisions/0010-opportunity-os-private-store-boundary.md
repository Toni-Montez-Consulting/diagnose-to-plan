# 0010: Opportunity OS Private Store Boundary

Status: accepted

Date: 2026-05-09

## Context

Opportunity OS is meant to help Toni notice and manage high-trust consulting
opportunities without turning relationship-building into cold outbound,
generic CRM work, or an overbuilt automation system.

The records can become sensitive quickly. Real opportunity notes may include
personal relationships, referral paths, private business problems, budget
signals, client replies, meeting context, contact details, compensation/IP
signals, COI concerns, and timing information.

DTP now owns the Opportunity OS method, data contract, scoring posture,
sanitized pilot records, and Notion mirror design. That is not the same as
owning the raw private relationship ledger.

## Decision

Do not create a new CRM, database, Notion source of truth, or raw private
relationship ledger yet.

For V0:

- DTP owns the Opportunity OS method, templates, scoring rules, sanitized
  examples, mirror contracts, steward receipts, and future store decision
  gates.
- `diagnose-to-plan/engagements` owns private client-truth records once an
  opportunity becomes an active or recurring client engagement lane.
- Gmail, Calendar, and meeting transcripts remain source evidence for
  communication history until a reviewed summary is promoted into the right
  DTP or private engagement artifact.
- Notion may mirror sanitized opportunity posture for phone-friendly review,
  but it must not hold raw private notes, contact details, sensitive referral
  context, or final authority.
- The public/deploy-adjacent consulting repo must never hold raw opportunity or
  relationship records.
- Hub/Supabase can become a future private runtime store only after the manual
  DTP loop proves the fields, access model, and retention needs.
- A dedicated CRM is deferred until opportunity volume, follow-up complexity,
  or reporting needs justify it.

## V0 Storage Ladder

Use the lightest responsible storage surface:

| Stage | Storage Surface | Allowed Content | Gate |
|---|---|---|---|
| Raw signal | Gmail, Calendar, meeting notes, personal context | original evidence in its source system | summarize before acting |
| Sanitized method record | DTP tracked docs | generic labels, fit bands, capacity posture, source pointers | no private details |
| Active client lane | private `engagements` vault | private client facts, owner actions, meeting receipts, scoped work | active engagement or explicit client lane |
| Phone cockpit | Notion mirror | sanitized status, next touch, review date, DTP source path | DTP remains authoritative |
| Future durable store | hosted DTP, private Hub/Supabase, or approved CRM | structured private opportunity records | separate accepted decision |

## Promotion Rules

A raw opportunity signal can become a durable record only when it has:

- a reason to be tracked;
- a sensitivity label;
- a next human action or review date;
- a clear owner;
- a storage surface that matches the privacy level;
- no unsupported public claim;
- no automated outreach behavior.

If the signal is not actionable, keep it as source-system context or park it as
a sanitized DTP note.

## Future Store Selection Criteria

Choose a stronger private store only when at least one of these becomes true:

- Toni has enough concurrent warm opportunities that markdown review becomes
  hard to trust.
- follow-up timing is being missed because records are scattered.
- multiple clients or prospects need structured privacy boundaries.
- the same fields keep repeating across real opportunities.
- reporting, retention, or pipeline review needs exceed Notion mirror value.
- client intake and opportunity tracking need to connect to Hub runtime records.

Preferred future direction, if those gates are met:

1. hosted DTP private tables for canonical structured records;
2. Notion as a sanitized cockpit/mirror;
3. Hub/Supabase only for runtime intake or operational console needs;
4. CRM only if sales-pipeline workflow becomes the bottleneck.

## Consequences

- Opportunity OS can start now without overbuilding.
- Toni gets capacity protection and relationship visibility without creating a
  fragile or invasive private ledger.
- Notion stays useful without becoming dangerous.
- DTP remains the methodology source while private truth stays in the proper
  private lane.
- Future automation remains gated until manual records prove the shape.

## Non-Goals

- No cold outreach engine.
- No automatic follow-up messages.
- No raw relationship records in the consulting repo.
- No Notion source-of-truth shift.
- No CRM choice yet.
- No Hub/Supabase schema yet.
- No public proof or named relationship claims.
