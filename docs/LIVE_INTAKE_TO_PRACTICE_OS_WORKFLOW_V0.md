---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Live Intake To Practice OS Workflow V0

Status: internal operating pattern for turning a live `tonimontez.co/start`
submission into a Practice OS decision, artifact path, and human-reviewed next
action.

Owner repo: `diagnose-to-plan`

Runtime support: `hub`

Public surface: `consulting`

## Purpose

The live intake path now works technically. This workflow makes it useful as a
business system.

The goal is not to collect leads into a generic CRM. The goal is to turn a
messy operator signal into:

- a clear fit decision;
- a practical offer route;
- useful clarifying questions;
- a source-aware Practice OS artifact;
- a human-approved follow-up path;
- a durable handoff receipt.

This is the bridge from "a form was submitted" to "Toni knows what to do next
and why it matters."

## Business Value

This workflow creates value by increasing the quality of the first decision.

| Value area | What changes |
|---|---|
| Speed | Toni can review a submission without rereading raw form context several times. |
| Fit | Bad-fit, unclear, and high-potential inquiries separate early. |
| Trust | Follow-up is based on stated context, not a generic sales reply. |
| Scope control | Blueprint, Fast Track, Custom SOW, advisory, and parked paths stay distinct. |
| Proof safety | Nothing from a private intake becomes public proof without DTP proof gates. |
| Practice learning | Repeated patterns can later become reviewed offer, template, or memory candidates. |

## Innovation Thesis

The useful innovation is not "AI answers contact forms."

The useful innovation is a builder-led operating loop:

1. capture high-resolution context;
2. preserve the human operator's intent;
3. classify the business problem;
4. route the work to the right offer or artifact;
5. use agents only as bounded reasoning and drafting support;
6. keep approval, proof, privacy, and implementation authority explicit.

This makes AI part of the implementation workflow instead of a surface-level
chatbot or automation gimmick.

## Source And Ownership Boundary

| Layer | Owns | Does not own |
|---|---|---|
| `consulting` | public `/start` route, public copy, form UX, Hub-first endpoint path | private engagement records, DTP decisions, proof approval |
| `hub` | runtime intake record, private console support, Supabase storage, health/CORS evidence | DTP methodology, CRM replacement, public proof |
| `diagnose-to-plan` | triage, fit decision, Practice OS artifacts, proof gates, steward receipt | public form rendering, runtime row storage |

Hub can show that an intake exists. DTP decides what the intake means.

## Trigger

Use this workflow when:

- a real prospect submits `/start`;
- Toni manually adds a prospect inquiry from email, call notes, or a referral;
- a synthetic live-intake smoke proves the path but also reveals process gaps;
- an old inquiry is being rehydrated into Practice OS state.

Do not use this workflow for raw transcript dumping, public proof promotion, or
client communication that has not been reviewed.

## Step 1: Confirm Runtime Evidence

Start from the lightest evidence needed.

| Check | Source | Result to record |
|---|---|---|
| Public route exists | `https://tonimontez.co/start` or latest deployment evidence | route status and endpoint path |
| Hub health is available | `https://onhand.dev/health` | status and storage mode |
| Intake row exists | Hub private console or approved Supabase query | summarized row fields only |
| Test cleanup, if synthetic | Hub console or approved Supabase query | deleted, archived, or clearly labeled |

Use `practice-os/templates/live-intake-receipt.md` for smoke tests. For real
prospects, do not paste raw private rows into tracked DTP docs.

## Step 2: Create A Triage Record

Use `practice-os/templates/prospect-intake-triage.md`.

The triage record should answer:

- What problem did they bring?
- What outcome do they want?
- What business stage are they in?
- How urgent is it?
- What budget/readiness signal did they provide?
- What is sensitive or blocked?
- What is the recommended route?

Default route values:

- `no-build-yet`
- `fit-call`
- `paid-blueprint`
- `fast-track`
- `custom-sow`
- `advisory`
- `parked`
- `bad-fit`

## Step 3: Apply Squad Lenses

Use the Agent Squads + Knowledge Base V0 model without spawning agents unless
Toni explicitly asks for delegated or parallel agent work.

| Squad / role lens | Question |
|---|---|
| Business Justification Squad | Is this worth time now, and what operator value could it create? |
| Delivery Squad | Is the likely implementation path real, bounded, and verifiable? |
| Consulting Strategy role | Which offer route fits the buyer problem and trust posture? |
| External Communications role | What concise follow-up would be useful and human? |
| Research Steward role | Is current outside evidence needed before making a recommendation? |
| Memory Steward role | Is this a one-off inquiry, a repeated pattern, or a memory candidate? |

## Step 4: Pick The Next Artifact

Choose one primary artifact. Do not create all of them by default.

| Situation | Next artifact | Why |
|---|---|---|
| High intent but unclear scope | `business-systems-blueprint.md` | turns messy context into roadmap, value case, workflow map, and SOW bridge |
| Not enough resolution | `input-studio.md` | preserves intent and asks up to three useful questions |
| Needs shared context before planning | `context-pack.md` | gives Toni/future agents the current facts and constraints |
| Clear small implementation | `work-item-spec.md` | scopes build, acceptance, and verification |
| Possible command-room/admin system | `client-command-room-fit-assessment.md` | prevents building a portal before operator pain is proven |
| Needs proof movement | proof packet plus redaction queue | blocks unsafe public claims |
| Not a fit | triage record only | preserves why it was declined or parked |

## Step 5: Decide The Follow-Up Path

No message is sent automatically.

Use `docs/PROSPECT_FOLLOW_UP_DRAFTING_PLAYBOOK_V0.md` after triage when a
prospect-facing draft is needed.

Allowed next paths:

- draft a reply for Toni to review;
- create a Gmail draft only when the Gmail connector is available and Toni asks
  for email drafting;
- prepare a fit-call agenda;
- prepare a paid Blueprint outline;
- ask up to three clarifying questions;
- park with a reason;
- decline politely.

Every follow-up should name the next concrete decision, not just "let's chat."

Default draft templates:

| Follow-up path | Template |
|---|---|
| fit call / advisory conversation | `practice-os/templates/prospect-fit-call-follow-up.md` |
| paid Blueprint / diagnostic path | `practice-os/templates/prospect-paid-blueprint-follow-up.md` |
| no-build-yet / parked / bad-fit | `practice-os/templates/prospect-park-or-decline-follow-up.md` |

## Step 6: Capture Approval Gates

Use `practice-os/templates/approval-gate.md` when the intake could lead to:

- client communication;
- pricing or public offer changes;
- public proof;
- production writes;
- private data handling;
- live integrations;
- repo mutation;
- write-enabled automation.

Default approval posture:

| Gate | Default |
|---|---|
| Client communication | pending until Toni reviews |
| Public proof | blocked until proof promotion runbook passes |
| Production write | blocked until scoped and explicitly approved |
| Pricing / offer posture | pending if the intake changes public offer language |
| Private data handling | pending unless sensitivity is already classified |

## Step 7: Leave A Handoff Receipt

Use `practice-os/templates/squad-handoff-receipt.md` when the triage leads to
work beyond a single note.

The receipt should record:

- sources used;
- route decision;
- business value;
- chosen artifact;
- approval gates;
- next action;
- parked ideas;
- what not to touch.

## Done Signal

An intake is operationally handled when:

- Hub runtime evidence is sufficient for the situation;
- DTP has a triage record or receipt;
- the recommended route is explicit;
- the next artifact is created or intentionally skipped;
- follow-up is drafted, scheduled, parked, or declined with a reason;
- proof/privacy/client communication gates are visible;
- a future agent can resume without raw chat context.

## Non-Goals

- No automatic lead scoring.
- No public proof publication.
- No auto-send emails.
- No client portal.
- No CRM replacement.
- No hosted DTP expansion.
- No autonomous agents.
- No raw private Hub row copies in tracked DTP docs.

## Revisit Triggers

Revisit this workflow when:

- three real prospect intakes have used the triage template;
- Hub console review becomes the bottleneck;
- the same intake pattern repeats enough to become a reviewed offer or memory
  candidate;
- Toni wants Gmail/Calendar/Notion actions connected to the workflow;
- hosted DTP becomes the accepted normal store for client-sensitive records.
