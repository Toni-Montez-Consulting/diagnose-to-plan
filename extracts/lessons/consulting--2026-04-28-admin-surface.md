---
repo: consulting
pattern: admin-surface
type: lesson
created: '2026-04-28T23:59:07Z'
source: C:\Users\tonimontez\consulting\docs\BUILD_SPEC_EXTRACT_REVIEW.md
promoted: false
private_review_required: true
---

# consulting admin-surface

## Lesson

The first admin pattern should be a public-safe command room on the consulting site paired with a private Hub console. The public route can show routing status, triage stages, work orders, health links, and runbook boundaries, but the operational records stay in Hub.

This is the right first reusable pattern because it is small enough to ship, visible enough to reuse, and strict enough to protect private client context. It gives future scopes a concrete shape: public proof and operator clarity outside, protected record management inside.

## Reusable Pattern Impact

Future admin-dashboard scopes should start by asking which layer they need:

- public-safe command room for links, status, runbook, and launch tasks
- protected console for intake rows, client notes, workflow state, and owner decisions
- extraction pattern for reusable dashboard anatomy and citations

`dtp recall admin --type pattern` should surface both halves: the consulting `/admin` command room and the Hub console implementation.

## Do Not Reuse Blindly

Do not copy private data shape, prospect records, service-role behavior, workflow tables, or client-specific triage language into a public page. Reuse the boundary and operating anatomy, then adapt the record schema, auth level, copy, and privacy rules per client.

## Source

# Build Spec Extract Review

Source reviewed: `C:\Users\tonimontez\Downloads\build-spec-extract.md`

## Strategic Read

This is a strong spec because it protects the thing that matters: Toni's practice memory should become a structured asset without becoming a fragile platform. The best choices are the hard Phase 1 gate, markdown-first storage, grep-first recall, human-authored lessons, constrained LLM reads, and the insistence that scaffold waits until real engagements prove a pattern.

The potency gap is usability. The spec explains how to build the extraction system, but it can do more to make Toni and future agents reach for it naturally.

## Additions That Would Make It More Potent

### 1. Add A "Daily Use" Section

Add a short section after the module overview called "How Toni actually uses this." Include five concrete command flows:

- "I just shipped client work. What should I capture?"
- "I am drafting a proposal. What patterns should I reuse?"
- "I need an admin dashboard for a new client. What did I already build?"
- "I solved an App Store or auth failure. How do I preserve the lesson?"
- "I want to start a new project from a proven pattern. What can be scaffolded?"

This turns the spec from architecture into operator muscle memory.

### 2. Add Pattern Quality Rubrics

Before Module 2, add a rubric for what counts as a useful pattern:

- has evidence in real files
- names the reusable shape
- names what must vary per client
- names the private or risky parts
- explains why it mattered operationally
- includes a "do not reuse blindly" note

This will prevent pattern docs from becoming generic summaries.

### 3. Add An Admin-Surface Pattern As A First-Class Candidate

The spec already includes an `admin-surface` signal, but it should explicitly name the reusable pattern Toni keeps reaching for:

> Public proof surface outside, protected operating room inside, handoff record when work ships.

Canonical candidates now include the consulting `/admin` command room, Hub console, and future client admin dashboards.

### 4. Add Recall Examples To Every Module

Each module should include one example of the question it should eventually answer. Example:

```bash
dtp recall admin --type pattern
dtp recall "intake handoff" --repo consulting
dtp recall "App Store expired subscription" --type lesson
```

These examples make acceptance criteria feel usable instead of only testable.

### 5. Add A "Pattern Promotion" Workflow

Add a small lifecycle:

1. Signal found by `dtp index`.
2. Pattern drafted by `dtp detect`.
3. Toni marks it `promoted: true` only if it was useful in real work.
4. Synthesizer uses promoted patterns first.
5. Scaffold can only read promoted synthesis docs.

That creates a quality gate between "the agent noticed this" and "this is part of the practice."

### 6. Add Cost And Confidence Review Output

For LLM phases, make each run end with a tiny ledger:

- files read
- files truncated
- estimated cost
- patterns created
- low-confidence outputs
- recommended human review order

This helps Toni skim the result and decide whether to trust it.

### 7. Add A "No Private Leakage" Checklist

Because this system reads across repos, add a checklist before any pattern or synthesis doc is committed:

- no secrets
- no credentials
- no private client names unless already public
- no raw intake content
- no App Store reviewer credentials
- no service-role values
- no proprietary source data

This belongs near sections 6, 7, and 11.

### 8. Add SOW Injection Examples

Section 11 is important. Make it sharper with examples of how synthesis docs change a proposal:

- before: "Build an admin portal."
- after: "Install the admin-portal pattern proven in the consulting/Hub stack: intake queue, triage state, artifact inventory, decision log, handoff room."

That makes the business value obvious.

### 9. Add A `dtp extract status` Or `dtp recall --review`

The command surface could use one operator dashboard command:

```bash
dtp extract status
```

It should print counts and stale areas:

- indexed repos
- detected patterns
- lessons captured this month
- synthesis docs
- low-confidence patterns needing review
- candidate patterns for promotion

This is not a web UI. It is a CLI dashboard that makes the system visible.

### 10. Turn Open Questions Into Decision Records

The open questions are good, but agents need execution rails. Add a rule:

> Before Phase 1.5 begins, unanswered open questions become ADR stubs under `decisions/`.

That prevents "open question drift" from reappearing every time the spec is reopened.

## One Strong Product Move

Make admin dashboards the first practice pattern this system proves.

The consulting site now has a public-safe `/admin` command room. Hub is the private runtime. That pair is exactly the kind of cross-repo pattern this extract system should capture:

- `consulting`: public site, intake field shape, command room, launch checklist
- `hub`: private runtime, protected console, Supabase-backed records
- future clients: same shape, different domain language and workflow states

That gives `dtp` a concrete first win: when Toni scopes the next owner-led business system, the proposal can say the admin-room pattern is already proven in Toni's own operating stack.
