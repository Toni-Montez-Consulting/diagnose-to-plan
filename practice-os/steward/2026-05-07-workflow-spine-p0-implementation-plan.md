---
data_class: P1
confidential: false
permission_level: internal_only
review_status: plan
created: 2026-05-07
owner: toni
plan_kind: workflow-spine-p0
source_audit: engagements/internal-steward/2026-05-07-practice-os-control-plane-deep-audit.md
---

# Workflow Spine P0 Implementation Plan - 2026-05-07

## Trigger

Toni accepted the control-plane audit direction and clarified the first
implementation scope:

- P0 only first; P1 comes later.
- The first case-file standard should include a template plus real Greg and
  Cam case files.
- The durable plan should live as a steward receipt and also update the roadmap
  so it drives future work.
- Stale docs should be labeled, not deleted or moved first.
- `tm-skills` readiness should be part of the first implementation pass.
- Greg and Cam should use the Workflow Spine after the readiness groundwork is
  in place.
- Toni later selected stable current-state filenames for the active spine:
  `active-workflow-spine.md`. Dated receipts must be easy to access and
  accurate from the spine file; if receipt discipline fails, switch to dated
  spine filenames.
- Stale-doc labels should touch DTP first; supporting repos come later.

This is a plan receipt only. It does not create the template, case files,
scoreboard, labels, archive moves, sends, public proof, or production changes.

## P0 Intent

Build the Workflow Spine as the central operating backbone for active work.

The Workflow Spine should make one thing obvious for Toni and future agents:

> What is the current state, what source owns it, what is allowed, what is
> blocked, what must be updated next, and what proof or approval gate controls
> movement?

This should reduce the current reliance on reconstructing state from many good
docs.

## Non-Goals For P0

- No hosted DTP changes.
- No vector/search implementation.
- No Notion, Hub, or Supabase source-of-truth migration.
- No public proof movement.
- No outbound client messages.
- No broad archive cleanup.
- No skill promotion or global install changes in `tm-skills`.
- No dashboard rewrite beyond planning the fields the dashboard should read
  later.
- No CCAAP, DeMario, Omnexus, Architected Strength, or consulting proof-lane
  expansion unless a direct dependency appears.

## Unified P0 Work Order

### 0. Roadmap and receipt wiring

Owner: DTP

Goal: make the plan durable and routeable.

Artifacts:

- this steward receipt;
- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md` roadmap update;
- `docs/ROADMAP_EXECUTION_BACKLOG.md` active story update.

Done gate:

- the roadmap names Workflow Spine P0 as the active operating-system fix;
- the backlog names the first implementation stories, owner repos, gates, and
  next actions;
- validation passes.

### 1. Minimal lifecycle vocabulary

Owner: DTP

Goal: label obvious stale/current docs without inventing a heavy archive
system.

P0 labels:

- `current`: use as active operating guidance.
- `active`: live work in progress.
- `needs_stale_review`: likely stale or conflicting; do not use as current
  guidance without review.
- `historical_reference`: useful evidence, not current guidance.
- `superseded`: replaced by a newer artifact.

P0 fields:

- `lifecycle_status`
- `last_verified`
- `superseded_by`
- `recheck_trigger`
- `owner`

Done gate:

- a short lifecycle note or template snippet exists;
- only obvious stale docs identified by the audit receive labels;
- no broad move/delete/archive pass happens yet.

Implementation note:

- This is the small vocabulary needed before labels land. The fuller archive
  model can be P1.

### 2. tm-skills readiness scorecard

Owner: DTP plus `tm-skills`

Goal: make `tm-skills` safe to treat as part of the squad workflow without
letting it override DTP gates.

Artifacts:

- DTP scorecard or readiness record for `tm-skills`;
- optional `tm-skills` repo-local pointer update if needed;
- no candidate skill promotion unless separately approved.

Scorecard fields:

- skill name;
- phase: `phase-1`, `incubator`, `parked`, `candidate`, `high-risk`;
- manifest status;
- eval status;
- external smoke status;
- DTP activation-map alignment;
- last reviewed;
- allowed use;
- blocked use;
- next gate.

Known P0 inputs:

- Phase 1 skills are installed and useful.
- Azure/Foundry skills are incubator.
- Candidate folders exist for `docx`, `pptx`, `xlsx`, `excalidraw`,
  `expense-report`, `loop`, and `web-artifacts-builder`.
- `tm-skills` doctor passes but warns about the unexpected candidate folders.
- Freshness check passes.
- Install preview confirms global links are already in place.

Done gate:

- Toni and future agents can tell which skills are safe to use now, which are
  incubator, which are parked, and which are high-risk;
- DTP gates still own client facts, COI, proof, public claims, and live writes.

### 3. Workflow Spine standard

Owner: DTP

Goal: define the canonical state object for active client/operator work.

Artifact:

- `practice-os/templates/workflow-spine.md`

Required frontmatter:

```yaml
case_file_id:
workflow_run_id:
client_or_lane:
workflow_kind:
phase:
status:
data_class:
confidential:
permission_level:
source_index:
proof_gate:
last_verified:
owner:
next_action:
```

Required sections:

- Current state
- Source files
- Allowed actions
- Blocked actions
- Open gates
- Next artifact to update
- Proof/public-use posture
- Dashboard mirror fields
- Handoff/closeout condition

Done gate:

- the template is short enough for agents to use;
- the template is structured enough for future dashboard parsing;
- it points to existing Client OS templates instead of replacing them.

### 4. Greg Workflow Spine record

Owner: DTP private engagement kit

Goal: make Greg the discovery and launch-readiness example.

Artifact:

- `engagements/greg-thegrantapp/case-study-sprint/active-workflow-spine.md`

Initial state:

- workflow kind: launch-readiness discovery;
- phase: meeting prep / pre-call;
- status: active or waiting on meeting;
- proof: blocked until Greg gives written approval, reviewer, and asset/claim
  boundaries;
- allowed: review prep, update internal notes, record post-call receipt;
- blocked: public screenshots, public claims, repo/product takeover,
  outbound messages without approval.

Done gate:

- a future agent can open one Greg spine file and know what to read, what is
  stale/provisional, what to ask in the meeting, what to update after, and what
  remains blocked.

### 5. Cam Workflow Spine record

Owner: DTP private engagement kit

Goal: make Cam the future front-to-back build example without prematurely
advancing blocked work.

Artifact:

- `engagements/cameron-mckesson/smb-ma-platform/active-workflow-spine.md`

Initial state:

- workflow kind: front-to-back build readiness;
- phase: waiting on item packet;
- status: waiting;
- proof: blocked until explicit approval and review;
- allowed: intake/classification prep, safe mock-data planning, source-index
  updates after packet arrives;
- blocked: repo creation, production build, live data handling, public proof,
  comp/IP assumptions, COI-sensitive work without review.

Done gate:

- a future agent can open one Cam spine file and know that the correct current
  action is waiting/classifying, not building.

### 6. Obvious stale-doc labels

Owner: DTP first; supporting repos later

Goal: reduce drift without starting a cleanup spree.

P0 target:

- label only DTP docs that the audit clearly identified as risky to treat as
  current guidance. Supporting repo candidates should be named for later rather
  than edited in P0.

Candidate examples:

- older Omnexus roadmap/planning state that conflicts with newer App Store
  closeout evidence;
- DTP architecture/control-plane docs that are reference-heavy but not the
  current active operating entrypoint;
- any roadmap overlay superseded by this Workflow Spine P0 plan.

Done gate:

- labels are visible;
- superseded/current pointers exist where needed;
- no deletion or move happens in P0.

## P0 Acceptance

P0 is done when:

- the steward receipt and roadmap/backlog entries exist;
- lifecycle labels are minimally defined;
- obvious stale docs are labeled without deletion;
- a `tm-skills` readiness scorecard exists;
- the Workflow Spine template exists;
- Greg has a Workflow Spine record;
- Cam has a Workflow Spine record;
- DTP validation passes;
- any cross-repo edits are separately verified in their repo;
- public proof, client sends, production writes, and skill promotion remain
  blocked unless separately approved.

## P1 Parking Lot

These are intentionally not P0:

- dashboard parser/resolver for Workflow Spine records;
- generated completeness scores;
- full archive index;
- Notion/Hub/Supabase mirror schema;
- hosted DTP app updates;
- vector retrieval;
- skill promotion beyond scorecard classification;
- CCAAP/DeMario/Omnexus/Architected Strength expansion into the spine.

## Decisions Before Starting P0

- Use stable current-state filenames: `active-workflow-spine.md`.
- Keep dated receipts and history in a receipt register inside each spine.
- If the receipt register is not maintained accurately, switch that workflow
  back to dated spine filenames.
- Label DTP docs first. Supporting repos are a later pass.

## Recommended Next Step

Implement P0 in this order:

1. lifecycle vocabulary snippet;
2. `tm-skills` readiness scorecard;
3. Workflow Spine template;
4. Greg Workflow Spine record;
5. Cam Workflow Spine record;
6. obvious stale-doc labels;
7. DTP validation;
8. roadmap/dashboard source notes if needed.
