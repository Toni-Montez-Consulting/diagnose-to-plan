---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Prospect Follow-Up Drafting Playbook V0

Status: internal operating pattern for turning a completed prospect intake
triage into a draft Toni can review.

Owner repo: `diagnose-to-plan`

Primary input: `practice-os/templates/prospect-intake-triage.md`

Drafting role: `practice-os/agents/external-communications.md`

## Purpose

The live intake workflow decides what an inquiry means. This playbook decides
what Toni says next.

The goal is not to automate sales replies or replace judgment with a booking
page. The goal is to make the first follow-up useful, specific, and bounded:

- acknowledge the prospect's real situation;
- name the clearest next decision;
- route to the right offer path;
- avoid over-promising scope, timeline, price, or results;
- preserve Toni's builder-led voice;
- keep all send, proof, pricing, and client-data gates human-reviewed.

Public label: use `Diagnostic Call`.

Internal route value: keep `fit-call` as the route vocabulary until a later
schema/template pass changes it. The public call is a diagnostic conversation:
the intake does the first assessment, and the call confirms the problem,
constraints, trust fit, and next artifact.

## Business Value

Good follow-up protects the practice at the moment trust is easiest to lose.

| Value area | What changes |
|---|---|
| Conversion quality | High-fit prospects get a clear next step instead of a generic "let's chat." |
| Scope control | Blueprint, fit-call, implementation, advisory, parked, and decline paths stay distinct. |
| Time leverage | Toni reviews a draft built from triage instead of rewriting from scratch. |
| Trust | Prospects see that their specific problem was understood. |
| Risk control | No send, price, proof, legal, or production commitments happen by accident. |
| Momentum | Qualified prospects can book after intake without manual scheduling drag. |

## Innovation Thesis

The useful innovation is a follow-up loop that connects intake, diagnosis, and
implementation judgment without turning the practice into a chatbot funnel.

The internal system can use squad lenses and source-aware reasoning, but the
prospect-facing message should stay simple:

1. "Here is what I heard."
2. "Here is what I think the next useful step is."
3. "Here is what I need from you, if anything."
4. "Here is what this does and does not commit us to."

Keep the reasoning machinery internal. Translate it into a practical next step.

## Required Inputs

Before drafting, confirm:

- a prospect intake triage exists or can be summarized safely;
- the recommended route is selected;
- sensitive fields are classified;
- at most three clarifying questions are identified;
- the send channel is known;
- Toni has not already answered the prospect elsewhere;
- no pricing, proof, legal, or delivery promise is being invented.

If those inputs are missing, draft with placeholders or route back to triage.

## Route Selection

| Triage route | Default follow-up artifact | Use when |
|---|---|---|
| `fit-call` | `practice-os/templates/prospect-fit-call-follow-up.md` | the problem looks relevant, but scope, urgency, access, or buyer fit needs a Diagnostic Call |
| `paid-blueprint` | `practice-os/templates/prospect-paid-blueprint-follow-up.md` | the problem is meaningful but needs diagnosis, value case, roadmap, and SOW shaping before build |
| `fast-track` | fit-call or work-item draft | the scope looks clear, small, and implementation-ready, but acceptance and timeline still need review |
| `custom-sow` | Blueprint or fit-call draft | the work looks larger than a quick build and needs decision-ready scoping |
| `advisory` | fit-call draft | the likely value is judgment, review, prioritization, or operating cadence more than immediate build |
| `no-build-yet` | `practice-os/templates/prospect-park-or-decline-follow-up.md` | the prospect may need clarity, inputs, budget, timing, or ownership before implementation |
| `parked` | `practice-os/templates/prospect-park-or-decline-follow-up.md` | the timing or fit is not right, but the door should stay open |
| `bad-fit` | `practice-os/templates/prospect-park-or-decline-follow-up.md` | the work does not match Toni's practice, ethics, scope, risk, or desired client profile |

## Drafting Sequence

1. Summarize the prospect message for Toni using the External Communications
   required format.
2. Confirm the selected route from the triage record.
3. Choose exactly one follow-up template unless Toni asks for variants.
4. Fill only facts that are present in the source or approved by Toni.
5. Mark placeholders for pricing, scheduling links, commitments, and attachments.
6. Record the approval gates before any send action.
7. If Toni asks for a Gmail draft and the connector supports it, create the
   draft and record the draft id. Do not send.

## Booking Link Policy

Use one approved `Diagnostic Call` booking link for qualified prospect intake.

Default public behavior:

1. The prospect submits `/start` intake first.
2. The post-submit confirmation can show the booking link.
3. The confirmation copy should say Toni reviews the intake before the call so
   the time is useful.
4. Manual scheduling is not the default unless the booking link is unavailable
   or the route is sensitive.

Do not show the booking link before intake submission. The intake is the first
assessment layer.

Do not show the booking link for:

- `bad-fit`;
- `parked`;
- sensitive inquiries that need human review before scheduling;
- cases where the booking URL is not configured;
- cases where the public page cannot safely distinguish post-submit state.

Recommended booking shape:

- Label: `Diagnostic Call`.
- Duration: 30 minutes.
- Booking questions: business context, broken workflow or friction, what has
  already been tried, and what must stay private.
- Buffers and reminders: maintain in Google Calendar.
- Availability: limited windows Toni approves.

## Voice Standard

The draft should sound like Toni:

- direct;
- warm;
- practical;
- specific to their problem;
- confident about the process, not artificially certain about the outcome;
- builder-led without oversharing internal methodology;
- helpful even if the answer is "not yet" or "not a fit."

Avoid:

- generic AI-consultant language;
- "unlock your potential" filler;
- unsupported ROI or growth claims;
- fake urgency;
- exact pricing unless approved;
- implying a build starts before diagnosis, access, or scope is accepted;
- revealing internal scoring, squad analysis, private proof, or raw intake rows.

## Approval Gates

| Gate | Default | Notes |
|---|---|---|
| Send | pending Toni review | no auto-send |
| Gmail draft | pending Toni request | allowed only as a draft when requested and supported |
| Calendar invite | booking link allowed after intake; direct event creation blocked until time and attendees are confirmed | fit-call language can include an approved Diagnostic Call link |
| Pricing | pending Toni approval | no exact price unless approved |
| Proof | blocked until proof promotion gates pass | no screenshots, metrics, testimonials, or client names unless approved |
| Legal / contract | pending General Counsel review if present | contracts, terms, liability, data handling, or permission language escalates |
| Production work | blocked until scoped | no promise to change production systems from an intake alone |

## Done Signal

A prospect follow-up is operationally handled when:

- the triage record is linked or summarized;
- the selected follow-up path is explicit;
- a draft exists or is intentionally skipped;
- unresolved decisions are visible as placeholders or questions;
- send, proof, pricing, calendar, and production gates are visible;
- the next action is clear without reading the original raw intake.
