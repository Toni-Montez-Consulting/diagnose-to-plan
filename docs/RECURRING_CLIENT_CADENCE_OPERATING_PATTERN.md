---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Recurring Client Cadence Operating Pattern

Status: active operating pattern for live consulting engagements with recurring meetings.

Owner: `diagnose-to-plan`

Purpose: keep live client work moving through a light, repeatable loop without turning Notion, chat memory, or a future hosted app into the source of truth.

## Cadence Model

| Relationship | Default cadence | Purpose | Current status |
|---|---|---|---|
| Cameron McKesson / SMB M&A platform | Weekly, 45 minutes | scope, valuation prototype, build decisions, data/IP/COI guardrails | active, first weekly time to confirm |
| Greg / TheGrantApp | Biweekly, 45 minutes | discovery, case-study permission, soft-launch planning, product feedback | pending Greg confirmation |
| CCAAP / Mom nonprofit | Monthly formal owner check-in | owner-approved inputs, review decisions, launch gates, proof/privacy decisions | waiting on owner inputs |
| Toni / Business Brain reset | Weekly, 30 minutes | reconcile DTP, Notion, blockers, next actions, proof gates, and stale work | active internal habit |

Casual conversations can produce facts, but they do not replace a formal owner-approved checkpoint. Capture casual CCAAP family updates only when they produce clear facts, decisions, or owner actions that can be reviewed.

## Source Of Truth Rule

DTP private kits and DTP roadmap artifacts remain authoritative.

Notion is the daily cockpit only. It may show sanitized status, cadence, waiting-on items, and next actions, but it must not store raw transcripts, private terms, client data, confidential employer/client context, payment/member/form records, or public proof claims.

When a reply or owner update arrives between meetings, use `docs/CLIENT_REPLY_INTAKE_OPERATING_PATTERN.md` and `practice-os/templates/client-reply-intake.md` before changing calendar state, Notion status, build scope, repo access, or proof posture.

## Pre-Meeting Loop

Before each recurring meeting, review the engagement kit in this order:

1. `diagnose.md`
2. `plan.md`
3. `decision-log.md`
4. `owner-action-items.md`
5. latest `meeting-notes*.md` or prior call note
6. `action-extraction.md`
7. any COI, data, IP, proof, or handoff checklist relevant to the meeting

The prep output should be a small agenda, not a new strategy document.

## Meeting Loop

Every meeting should produce one or more of:

- clarified scope;
- a decision;
- a waiting-on item;
- an owner action;
- a next build or planning task;
- a risk/gate update;
- a proof or case-study boundary update.

If the meeting produces no concrete action, record that too. Silence and waiting states are useful operational facts.

## Post-Meeting Loop

After each meeting, update the private kit first:

1. `meeting-notes*.md` for the checked summary, with any AI-generated notes marked as unverified until reviewed.
2. `action-extraction.md` for extracted facts, blockers, owner actions, Toni actions, and gates.
3. `decision-log.md` for explicit decisions only.
4. `owner-action-items.md` for waiting-on items and client-owned tasks.
5. `plan.md` for scope, next phase, and changed gates.

Then mirror only the sanitized daily-cockpit fields into Notion:

- `next_meeting`
- `waiting_on`
- `next_action`
- `blocked_by`
- `last_updated`

## Boundaries

- No Cam prototype repo, repo access, live financial data, signed terms, public proof, or unsupported valuation claim before COI/data/IP gates are clear.
- No Greg public case-study claim until permission is confirmed in writing.
- No CCAAP production launch until owner inputs, owner review, DNS/contact/payment/assets, and validation gates are ready.
- No Business Brain evals until real replies or meeting follow-ups produce examples worth testing.
- No site assistant code until the site manifest, approved source corpus, blocked source list, refusal/handoff behavior, logging/analytics policy, and launch gate are accepted.

## Weekly Business Brain Reset

Use a 30-minute reset to ask:

1. What changed in Cam, Greg, CCAAP, or consulting?
2. What private DTP kit needs updating before Notion?
3. What is waiting on someone else?
4. What is Toni's next action?
5. Which proof, COI, data, or launch gate is blocking progress?
6. What can be dropped, parked, or deferred?
7. Are any Notion cockpit items stale or too private?

The reset should end with no more than three active next actions.

The reset starts by checking for unprocessed replies. If a reply changes a waiting state, run the client reply intake loop before adding new work.
