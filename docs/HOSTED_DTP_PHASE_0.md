# Hosted DTP Phase 0

Status: accepted design boundary plus schema/app-shell scaffold, local Phase
0.1 private UI, passed live smoke against a dedicated Supabase environment, and
Phase 0.2 governance accepted for real operator, smoke fixture, backup/export,
and deployment posture.

Accepted: 2026-04-29 via `practice-os/steward/2026-04-29-hosted-dtp-phase-0-acceptance-review.md`.

Scaffold started: 2026-05-03 in `apps/private-dtp/`.

Phase 0.1 local private UI started: 2026-05-03 in `apps/private-dtp/`.

Live smoke harness added: 2026-05-03 at
`apps/private-dtp/scripts/smoke-live.mjs`.

Live import/export round-trip harness added: 2026-05-03 at
`apps/private-dtp/scripts/roundtrip-live.mjs`.

Live smoke passed: 2026-05-03 against the dedicated `DTP Private` Supabase
project.

Hosted DTP Phase 0 is the private foundation for engagement state, artifact governance, evidence, redaction, proof review, and decisions. It should not start as a dashboard. It should start as a private data model and app boundary that can later support useful views because the records already exist.

## Boundary

DTP owns practice methodology and private engagement governance:

- Client Operating Kits.
- Engagement stages and sensitivity.
- Artifact and evidence inventory.
- Redaction and permission reviews.
- Proof candidate review.
- Pattern promotion.
- Decisions and tradeoffs.
- Import/export with local markdown kits.

DTP does not own:

- Public marketing pages. Consulting owns those.
- Runtime intake, webhook, prompt-run, or support rows. Hub owns those.
- Client-facing portals by default.
- CRM, billing, e-signature, or account-management workflows.
- Omnexus, DeMario, FamilyTrips, DSE, or other project-specific source of truth.

## Phase 0 Product Shape

Phase 0 is private and single-operator first.

Required:

- Supabase Auth boundary for one private operator account.
- Postgres-backed records with RLS from the start.
- Storage pointers for artifacts instead of dumping private material into public docs.
- Import/export paths that preserve local markdown kits as fallback.
- Review queues for redaction and proof.
- Evidence records that can link to local/CI artifacts without copying raw logs by default.

Not required:

- Multi-user SaaS.
- Client portal.
- Deep Hub sync.
- MCP recall.
- Agent frontend.
- Analytics dashboard.
- Billing or CRM integration.

## Data Contracts

These are conceptual contracts for the first implementation pass. Field names can become exact database columns later, but the relationships should not change without a decision record.

### Engagement

Represents one client, internal, or project workstream.

Fields:

- `id`
- `title`
- `client_or_project_alias`
- `kind`: client | internal | product | proof_track | family_private
- `stage`: intake | diagnose | plan | build | handoff | support | proof_review | archived
- `sensitivity`: public | internal_only | private | client_confidential | coi_review
- `owner`
- `source_repo`
- `created_at`
- `updated_at`

Rules:

- An engagement can have many artifacts, evidence records, proof candidates, and decisions.
- Public-safe proof must reference an engagement only through reviewed aliases or public-safe project names.

### Artifact

Represents a source file, screenshot, note, report, runbook, proof asset, or imported markdown kit item.

Fields:

- `id`
- `engagement_id`
- `artifact_type`: note | kit_doc | screenshot | report | evidence | runbook | decision | asset | other
- `title`
- `source_kind`: local_markdown | repo_file | ci_artifact | upload | external_link | hub_reference
- `source_pointer`
- `storage_pointer`
- `redaction_status`: not_reviewed | needs_redaction | redacted | public_safe | restricted
- `proof_eligibility`: not_candidate | candidate | approved | rejected
- `created_at`
- `updated_at`

Rules:

- Store pointers and summaries first; do not copy raw private logs or client records unless there is a private-storage reason.
- Proof eligibility is not permission. Permission is tracked separately through reviews.

### Artifact Version

Represents a material revision to an artifact.

Fields:

- `id`
- `artifact_id`
- `version_label`
- `source_pointer`
- `storage_pointer`
- `summary`
- `created_at`

Rules:

- Preserve enough history to explain proof claims and handoff decisions.
- Do not use version history as a secret vault.

### Evidence Run

Represents a local, CI, release, support, or proof verification receipt.

Fields:

- `id`
- `engagement_id`
- `repo`
- `branch`
- `commit`
- `lane`: local | ci | release | support | proof | manual
- `result`: pass | fail | advisory_pass | manual_pending
- `commands`
- `hard_gate_status`
- `advisory_gate_status`
- `manual_gate_status`
- `artifact_path`
- `redaction_status`
- `reviewer`
- `created_at`

Rules:

- Hard failures stay visible even if advisory checks pass.
- Evidence can support proof, but raw logs are not public proof.

### Redaction Review

Represents the review state for an artifact or evidence record.

Fields:

- `id`
- `target_type`: artifact | evidence_run | proof_candidate
- `target_id`
- `reviewer`
- `status`: not_started | needs_changes | approved_internal | approved_public | rejected
- `permission_level`: internal_only | owner_approved | client_approved | public_safe | restricted
- `notes`
- `created_at`
- `updated_at`

Rules:

- Public proof needs both approved redaction and permission.
- DSE/Microsoft-adjacent material requires COI-aware review before professional reuse.

### Proof Candidate

Represents a possible public or internal proof claim.

Fields:

- `id`
- `engagement_id`
- `artifact_id`
- `public_claim`
- `baseline`
- `after_state`
- `metric`
- `caveat`
- `evidence_source`
- `permission_status`
- `redaction_status`
- `reviewer`
- `status`: proposed | needs_evidence | needs_permission | approved | rejected | parked
- `created_at`
- `updated_at`

Rules:

- A proof candidate is not publishable until evidence, caveat, permission, redaction, and reviewer are all present.
- Public claims should be receipt-style and specific.

### Decision

Represents a meaningful architecture, workflow, proof, automation, or scope decision.

Fields:

- `id`
- `engagement_id`
- `title`
- `status`: proposed | accepted | superseded | rejected
- `context`
- `options_considered`
- `chosen_path`
- `consequences`
- `related_artifact_id`
- `related_evidence_run_id`
- `created_at`
- `updated_at`

Rules:

- Decisions should explain why a path was chosen, not just what changed.
- Major boundary changes need a decision before implementation.

## Import / Export

Local markdown remains a first-class fallback.

Import should support:

- Engagement kit docs from `engagements/`.
- Practice OS templates.
- Verification evidence artifacts.
- Decision records.
- Redacted proof packets.

Export should support:

- Engagement summary markdown.
- Redaction queue markdown.
- Proof packet markdown.
- Evidence index markdown/JSON.
- Decision record markdown.

Rules:

- Import/export must preserve data classification and permission fields.
- Hosted DTP should never be the only copy of a private engagement unless backup and access rules are accepted.

## App Boundary

Phase 0 screens can be minimal:

- Engagement list.
- Engagement detail.
- Artifact inventory.
- Evidence list.
- Redaction queue.
- Proof queue.
- Decision list.

These screens should read from real records. Do not build charts, dashboards, or command-room widgets until the underlying records exist.

## Security And Privacy

- Use Supabase Auth and RLS from the first hosted implementation.
- Default all records to private/internal.
- Keep service-role access out of client code.
- Keep public proof export as a reviewed workflow, not a direct publish button.
- Keep Hub references pointer-based unless an accepted integration decision says otherwise.

## Implementation Gate

The schema, app-shell scaffold, Phase 0.2 local private UI/governance, live
smoke harness, and live round-trip harness now exist at `apps/private-dtp/`.

The first implementation slice is intentionally limited to schema, RLS, screen
contract, private Auth/RLS-backed record screens, and markdown import/export
fallback. It does not add dashboards, multi-user SaaS behavior, MCP recall,
deep Hub sync, QuickBooks writes, autonomous agents, or client portal features.

The smoke harness signs in two operator accounts, writes the core Phase 0
records, generates a markdown export, records an import/export receipt, checks
owner visibility across all inserted tables, and confirms the second operator
cannot read or attach rows to the primary operator's engagement.

The first live smoke created the dedicated `DTP Private` Supabase project,
created two smoke operator accounts, applied
`apps/private-dtp/supabase/migrations/0001_private_dtp_phase0.sql`, configured
local ignored env, and passed `npm run smoke:live`.

Phase 0.2 accepted that non-smoke private records use Toni's real operator
account, smoke accounts/records remain tagged regression fixtures unless they
become noisy, the app stays local/private with the dedicated live Supabase
project for now, and Hosted DTP is not the only copy of a private engagement
until markdown export fallback is verified for that lane. Existing Omnexus,
Consulting, FamilyTrips, and Mario Supabase projects are not the DTP brain
boundary and should not be reused.
