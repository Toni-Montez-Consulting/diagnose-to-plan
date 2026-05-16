---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
created: '2026-05-15T00:00:00Z'
fixture: true
---

# Northline Business Memory OS Diagnostic

Northline Performance Studio is a fictional wellness/performance practice used
to test Toni's Business Memory OS diagnostic.

This is demo material, not a client claim.

## Business Snapshot

- Business: Northline Performance Studio.
- Owner / operator: Maya Ellis, founder and lead coach.
- Industry: local wellness, performance coaching, recovery, and small-group
  training.
- Team size: owner, two part-time coaches, one admin contractor.
- Main customer type: adults who want private coaching, performance assessment,
  recovery support, or small-group wellness programs.
- Current systems: website, Instagram DMs, Gmail, Calendly, Square/Stripe,
  Google Drive, Google Sheets, scattered owner notes.
- Primary pain: leads, services, pricing, follow-up, and client status are
  spread across tools and owner memory.
- Existing AI/tool usage: occasional ChatGPT copy drafts; no governed assistant
  or source-of-truth layer.

## Knowledge Map

| Knowledge area | Where it lives now | Trusted? | Owner | Freshness | Notes |
|---|---|---|---|---|---|
| Services / offers | Website, old Google Doc, owner memory | partial | Maya | changes often | Website is behind current packages. |
| Pricing / estimates | Square items, Google Sheet, owner memory | partial | Maya | changes often | Prices exist but packages are not explained consistently. |
| Customer intake | Instagram DMs, Gmail, intake form drafts | partial | Maya / admin | changes often | Intake answers are not centralized. |
| SOPs / process | Coach notes, text threads, owner memory | no | Maya | changes often | New coach/admin onboarding depends on verbal transfer. |
| Follow-up / sales | Gmail drafts, DMs, manual reminders | partial | Maya / admin | changes often | No single list of who needs a nudge. |
| Vendor/admin | Gmail, Drive, invoices | partial | admin | stable | Needs clear owner approval path for payments and renewals. |
| Metrics/reporting | Stripe/Square, Calendly, Google Sheet | no | Maya | changes often | No weekly owner view of pipeline, bookings, and follow-ups. |

## Recurring Question Inventory

| # | Question | Asked by | Answer lives where? | Owner | Changes how often? | Safe for AI? | After-answer action | Classification |
|---|---|---|---|---|---|---|---|---|
| 1 | Which service fits this new prospect? | owner | Intake notes, service doc, owner memory | Maya | often | maybe | Draft recommendation for owner review | draft |
| 2 | What are the current package options and prices? | customer | Website, Square, pricing sheet | Maya | often | yes | Return current options or flag stale conflict | search |
| 3 | Is this lead ready for a paid assessment or just a fit call? | owner | Intake answers, DM context | Maya | often | maybe | Draft next-step suggestion for owner | draft |
| 4 | Has this prospect been followed up with? | owner / admin | Gmail, DMs, sheet | admin | daily | yes | Add to follow-up queue | workflow |
| 5 | Did the payment come through? | owner / admin | Square/Stripe | admin | daily | yes | Mark status and alert if unpaid | workflow |
| 6 | Which intake answers are missing? | owner / admin | Intake form, DM, email | admin | daily | yes | Request missing information draft | workflow |
| 7 | What should I say to this Instagram inquiry? | owner | DM, service FAQ, pricing sheet | Maya | often | maybe | Draft reply for owner to edit/send | draft |
| 8 | What does a recovery consultation include? | customer | Service doc, website | Maya | stable | yes | Answer from approved service copy | search |
| 9 | Can this client reschedule? | customer / admin | Cancellation policy, Calendly | admin | stable | yes | Draft reschedule link response | draft |
| 10 | Which clients are due for package renewal? | owner | Payment records, session tracker | admin | weekly | yes | Add renewal reminders | workflow |
| 11 | Who still needs to sign a waiver? | owner / admin | Waiver tool, intake tracker | admin | daily | yes | Send waiver reminder draft | workflow |
| 12 | What should a client do before an assessment? | customer | Prep doc, owner memory | Maya | stable | yes | Send approved prep instructions | draft |
| 13 | What equipment is needed for small group this week? | employee | Program notes, calendar | coach lead | weekly | yes | Create prep checklist | workflow |
| 14 | Which package includes recovery work? | customer | Pricing sheet, service doc | Maya | often | yes | Answer if sources agree; flag conflict if not | search |
| 15 | What availability is open this week? | customer / admin | Calendly | admin | daily | yes | Share scheduling link or options | workflow |
| 16 | What are the cancellation and refund rules? | customer | Policy doc, owner memory | Maya | stable | yes | Answer from approved policy only | search |
| 17 | Which leads came from referrals? | owner | Intake form, notes, sheet | admin | weekly | yes | Add to weekly owner memo | workflow |
| 18 | What should we promote this week? | owner | Lead questions, package goals, calendar | Maya | weekly | maybe | Draft content themes for owner review | draft |
| 19 | What did this client decide in the last consult? | owner / coach | Session notes | Maya / coach | often | maybe | Summarize only if notes are approved for use | search |
| 20 | Who needs post-session follow-up? | owner / coach | Calendar, session notes, package tracker | admin | daily | yes | Draft follow-up task list | workflow |
| 21 | Can this vendor invoice be paid? | admin | Invoice, budget, owner approval | Maya | monthly | no | Route to human approval | human |
| 22 | Which existing content answers this common question? | owner / employee | Website, docs, old posts | Maya | weekly | yes | Suggest link/snippet to reuse | search |
| 23 | Does this injury/condition change what we recommend? | owner / coach | Intake notes, professional judgment | Maya / coach | often | no | Human review only | human |
| 24 | Which clients have gone inactive? | owner | Payment/session tracker | admin | weekly | yes | Add to reactivation list | workflow |
| 25 | What should be in the weekly owner memo? | owner | Pipeline, bookings, payments, follow-ups | admin | weekly | yes | Generate memo draft | workflow |

## Classification Summary

| Classification | Count | What it means |
|---|---:|---|
| Search only | 6 | Approved answers can be found if sources are cleaned up. |
| Draft only | 6 | AI can help write, but owner/coach judgment stays in the loop. |
| Workflow | 11 | The biggest value is task routing, reminders, and owner visibility. |
| Do not automate | 2 | Finance approval and injury/condition judgment stay human. |

## Opportunity Score

| Candidate | Repetition | Pain | Source trust | AI safety | Business value | Score | Notes |
|---|---|---|---|---|---|---:|---|
| Intake and follow-up memory assistant | high | high | medium | medium | high | 23 | Best first assistant because it reduces owner drag without replacing judgment. |
| Service/package knowledge layer | high | high | medium | high | high | 22 | Needs source cleanup first; strong customer-facing clarity value. |
| Weekly owner memo | high | medium | medium | high | high | 20 | Good operating cockpit once source trackers are cleaned up. |

## Recommendation

- Best first assistant/workflow: intake and follow-up memory assistant.
- Why this one: it hits repeated owner pain, creates immediate operating value,
  and keeps all client recommendations under human review.
- What to clean up first: services, packages, pricing, cancellation policy,
  intake questions, follow-up statuses, and package tracker.
- What not to connect yet: payment writes, medical/injury recommendation logic,
  private session notes without a clear consent/source policy, and automatic DM
  sending.
- Human-review point: owner reviews service recommendation, health-sensitive
  notes, and every prospect/client message before send.
- Handoff/runbook needed: source owner list, weekly source update cadence,
  approved response snippets, escalation rules, follow-up queue rules, and
  weekly owner memo format.
- Suggested path:
  - [ ] no build yet
  - [x] Knowledge Layer Audit
  - [x] Business Memory Assistant
  - [ ] Business Memory OS
  - [ ] park

## What This Proves

This diagnostic makes the offer feel real without building software first.

The useful wedge is not "install an AI chatbot." The useful wedge is:

- map repeated business questions;
- find where the answers actually live;
- clean up stale or conflicting sources;
- separate search, drafting, workflow, and human-only decisions;
- build the smallest assistant/workflow that reduces owner drag.

For Northline, the right first build would not be a public AI assistant. It
would be a private owner/admin workflow that summarizes intake, drafts
follow-ups, tracks missing information, and produces a weekly owner memo.
