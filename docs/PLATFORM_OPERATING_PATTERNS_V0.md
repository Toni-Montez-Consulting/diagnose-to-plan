---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Platform Operating Patterns V0

Status: DTP-owned planning and template layer.

Use this document when Toni wants to borrow what feels strong about platforms
like Vercel and Supabase without turning the consulting practice into a tool
reseller, stack monoculture, or generic SaaS clone.

## Purpose

Vercel and Supabase work because they make serious engineering behavior feel
lighter:

- every change can have a preview;
- environments have clear meaning;
- infrastructure choices are visible in the product workflow;
- database changes can be versioned, reset, and reviewed;
- data access is a boundary, not an afterthought;
- the dashboard shows useful state without forcing the operator into raw logs;
- starter templates reduce blank-page friction while preserving code ownership.

The Consulting Workspace OS should extract those operating moves into DTP
patterns that help Toni build and hand off better work across consulting,
Hub, Omnexus, FamilyTrips, CCAAP, DeMario, and future client projects.

This is not a directive to use Vercel or Supabase everywhere. It is a way to
capture the platform behaviors worth reusing.

## Boundary

This slice is docs and protocol only.

- No public consulting copy changes.
- No Greg soft-launch proof movement before the next meeting.
- No Hub runtime, Supabase, Vercel, production, DNS, or client system mutation.
- No `tm-skills` mutation.
- No app-code change.
- No new hosted DTP behavior.
- No new dashboard until manual receipts prove the useful fields.

## Platform Moves To Extract

| Move | Plain-language translation | DTP artifact |
|---|---|---|
| Preview every change | Before a change is called ready, show what changed in a disposable, reviewable state | Preview Receipt |
| Separate local, preview, and production | Do not let environment state blur into mystery | Environment Ledger |
| Make storage and access explicit | Data source, owner, policy, and exposed surface are part of the build, not background details | Data Boundary Ledger |
| Give operators a useful dashboard | Show the next decision, not every internal table | Client Handoff Console Spec |
| Start from templates, not blank pages | Reuse proven scaffolds while keeping the result specific to the business | Pattern and Template Library |
| Treat launch as a measured event | Capture activation, feedback, caveats, and next action before promoting proof | Launch Momentum Receipt |

## Core Patterns

### Preview-To-Production Ladder

Every meaningful site, app, workflow, or proof surface should name the claim
level:

| Level | Meaning | Typical proof |
|---|---|---|
| Local | Works on the developer machine with local or mocked data | local build/test output, screenshots, local smoke |
| Preview | Works in a shareable non-production environment | preview URL, route checks, preview env confirmation |
| Production | Works on the live domain or shipped app | live route/API smoke, deployment evidence, rollback notes |
| Operator-ready | A real owner can use it without Toni driving every click | runbook, handoff console, UAT receipt |
| Public-proof-ready | Evidence can be used externally | permission, redaction, public claim review, caveats |

Do not collapse these into one vague "done."

### Environment Ledger

Every repo with live behavior should have a small environment ledger when the
lane is active. The ledger should answer:

- What are the environments called?
- Which domain or URL belongs to each?
- Which environment variables exist by name?
- Which values are secret and must never be printed?
- Which environment was verified last?
- What command or manual step proves it?
- What deployment or rollback path exists?

The ledger is not a secret store. It records names, scopes, owners, and proof
paths, not secret values.

### Data Boundary Ledger

Any Supabase, Postgres, storage, auth, or private data lane needs a boundary
ledger before handoff or public proof.

It should answer:

- What data exists?
- Where is the source of truth?
- Who owns the account, billing, and credentials?
- Which tables, buckets, APIs, or files are exposed?
- What RLS, auth, route, or role boundary protects the data?
- Which service-role or admin operations exist, and who may run them?
- What can be safely shown in a public/client/admin surface?
- What must stay private or redacted?

### Client Handoff Console

Many clients do not need a full portal. They need a task-based command room
that shows:

- current status;
- next action;
- owner responsibilities;
- links to the live thing;
- common failure modes;
- support path;
- runbook pointers;
- last verified date;
- what not to touch without help.

The console should feel like a calm operating surface, not a database screen.

### Pattern And Template Library

The practice should accumulate templates the way platforms offer starters:
not as generic final products, but as strong starting shapes.

Reusable templates should be:

- specific enough to reduce blank-page work;
- small enough to adapt;
- tied to evidence;
- gated by Integrity Layer checks;
- promoted only after repeated useful use.

### Launch Momentum Receipt

When a soft launch, first-user pass, ad push, community post, waitlist, or
pilot produces real signal, capture it as private evidence first.

The receipt should separate:

- what happened;
- what changed in user behavior;
- what metrics are visible;
- what feedback or bugs surfaced;
- what can be said internally;
- what cannot yet be said publicly;
- what should happen before the next decision.

Greg's current soft-launch screenshots are intentionally deferred until the
next meeting. The pattern exists now; the client-specific receipt waits.

## How This Fits The Workspace OS

| Existing module | New platform-inspired layer |
|---|---|
| Requirements Gatherer | asks for environment, data, handoff, preview, and launch-proof constraints earlier |
| Integrity Layer | keeps platform polish from hiding weak proof, weak handoff, or overbuilt architecture |
| UAT Kit | records claim level, environment, data boundary, handoff, and proof caveats |
| Pattern loop | turns repeated platform moves into reviewed pattern candidates |
| Tooling Steward | decides when Vercel, Supabase, or another tool is appropriate for a lane |
| Public proof gate | prevents internal metrics, screenshots, or customer data from leaking into copy |

## V0 Artifacts

Templates:

- `practice-os/templates/platform-preview-receipt.md`
- `practice-os/templates/environment-ledger.md`
- `practice-os/templates/data-boundary-ledger.md`
- `practice-os/templates/client-handoff-console-spec.md`
- `practice-os/templates/launch-momentum-receipt.md`

Draft pattern candidates:

- `practice-os/research/pattern-candidates/2026-05-14-preview-to-production-ladder.md`
- `practice-os/research/pattern-candidates/2026-05-14-environment-ledger-as-delivery-control.md`
- `practice-os/research/pattern-candidates/2026-05-14-data-boundary-ledger.md`
- `practice-os/research/pattern-candidates/2026-05-14-client-handoff-console.md`
- `practice-os/research/pattern-candidates/2026-05-14-launch-momentum-receipt.md`

Steward receipt:

- `practice-os/steward/2026-05-14-platform-operating-patterns-v0.md`

## Operating Rules

- Start manual and docs-first.
- Use the templates only when a lane is active.
- Do not bulk-add ledgers to inactive repos.
- Do not copy private screenshots or raw client data into tracked docs.
- Do not promote a pattern to `practice-os/patterns/` until reviewed.
- Do not promote public proof until permission, redaction, evidence, reviewer,
  and caveat gates pass.
- Do not let a platform's dashboard shape become the client's workflow by
  default. Translate it into the client's task language.

## First Test Lanes

Use this order:

1. Greg meeting follow-up, after tomorrow's meeting, if Toni chooses to capture
   the soft-launch signal.
2. Hub dependency/runtime cleanup, when Hub PRs are reopened, using the
   Environment Ledger and Preview Receipt.
3. Omnexus release proof, only after live-state verification, using Preview
   Receipt and Data Boundary Ledger.
4. CCAAP launch readiness, after owner inputs, using Client Handoff Console and
   Launch Momentum Receipt only if launch signal exists.
5. Future consulting public proof, only after proof gates.

## Acceptance Criteria

V0 is useful if a future agent can answer:

- What platform behavior are we copying?
- What are we deliberately not copying?
- Which template should be used?
- Which repo owns the runtime truth?
- Which environment or data boundary is being claimed?
- What evidence proves the claim?
- What remains private, manual, or unproven?
- What next decision is safe?

