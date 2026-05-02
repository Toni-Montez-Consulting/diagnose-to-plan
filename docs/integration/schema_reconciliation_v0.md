---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice OS Schema Reconciliation V0

Status: planning/control-plane artifact only. This is not a migration.

## Purpose

Map `database/schema/practice_os_schema_v0_1.sql` against
`docs/HOSTED_DTP_PHASE_0.md` so the source schema can sharpen DTP without
overwriting the accepted hosted-DTP boundary.

The source SQL is useful as module vocabulary and a starter data model. Hosted
DTP Phase 0 remains the implementation boundary because it already names the
private operator model, proof/redaction governance, import/export, evidence,
and security expectations.

## Source Tables To Phase 0 Contracts

| Source schema table | Closest Hosted DTP Phase 0 concept | Reconciliation note |
|---|---|---|
| `clients` | Engagement alias / client metadata | Phase 0 intentionally centers `Engagement`; future schema can keep `clients` if it improves normalization without adding CRM behavior. |
| `engagements` | `Engagement` | Needs Phase 0 fields for `kind`, `sensitivity`, `owner`, `source_repo`, and explicit stage values. |
| `raw_inputs` | Artifact / Thought Inbox | Needs data classification, source pointer, redaction status, and import/export handling before hosted storage. |
| `intent_briefs` | Artifact / Input Studio | Good module vocabulary. Needs ownership, sensitivity, and versioning rules. |
| `clarifying_questions` | Artifact / Input Studio | Good fit. Blocking reasons should align to safety, legal, privacy, security, compliance, money, irreversible action, technical impossibility, and COI. |
| `assumptions` | Artifact / decision support | Needs review status and promotion path into decision memory. |
| `workflows` | Artifact / Workflow Map | Useful product module. Needs engagement linkage and privacy boundary. |
| `opportunities` | Artifact / Opportunity Score | Useful product module. Needs score versioning and "advisory, not override" framing. |
| `implementation_specs` | Artifact / Work Item Spec | Useful product module. Needs artifact versioning and evidence/decision links. |
| `build_tasks` | Build task / artifact | Useful module, but should not become a full project-management replacement in Phase 0. |
| `exceptions` | Artifact / Exception Register | Useful module. Needs severity, evidence, and learning promotion review. |
| `value_metrics` | Proof candidate support / Value Ledger | Useful module. Public use still requires proof packet gates. |
| `memory_items` | Memory Review Queue | Must enforce human-approved durable memory; no unmanaged self-learning. |
| `decision_logs` | `Decision` | Strong fit. Needs status, related artifact/evidence links, and options/consequences. |
| `runbooks` | Artifact / runbook | Strong fit. Needs version and export support. |

## Phase 0 Concepts Missing Or Underdeveloped In The Source SQL

| Phase 0 need | Current source SQL coverage | Required reconciliation before migration |
|---|---|---|
| RLS and auth | absent | Add operator-only Supabase Auth and RLS policy design before any hosted implementation. |
| Artifact inventory | partial | Add artifact type, source kind, pointer, storage pointer, redaction, and proof eligibility. |
| Artifact versioning | absent | Add material revision history for proof and handoff traceability. |
| Evidence runs | absent | Add local, CI, release, support, proof, and manual evidence records. |
| Redaction review | absent | Add target type, reviewer, permission level, and approval states. |
| Proof candidates | partial through `value_metrics` | Add proof claim, baseline, after-state, caveat, evidence, permission, redaction, reviewer, and status. |
| Import/export | absent | Preserve local markdown kits as first-class fallback. |
| Storage pointers | absent | Store pointers and summaries before copying private material. |
| Data classification | absent | Add public/internal/private/client-confidential/COI-gated boundaries. |
| Permission review | partial | Add explicit permission levels for public proof and client-approved reuse. |

## Source Concepts Missing Or Underdeveloped In Hosted Phase 0

| Source concept | Current Hosted Phase 0 coverage | Additive recommendation |
|---|---|---|
| Thought Inbox / raw capture | artifact only | Add template-first support before schema work. |
| Input Studio / intent brief | artifact only | Preserve as a module vocabulary and future app surface. |
| Clarifying question layer | implicit | Add non-blocking/blocking question model to implementation design. |
| Assumptions | implicit decision support | Add assumption review status in a future merged schema design. |
| Workflow maps | artifact only | Keep as a Practice OS module before building dashboard views. |
| Opportunity scoring | artifact only | Keep advisory and human-overridable. |
| Exception register | artifact/evidence adjacent | Add as learning repair flow. |
| Value ledger | proof/evidence adjacent | Keep internal until proof gates are passed. |
| Memory review queue | future learning layer | Add only with human approval controls. |

## Recommended Next Schema Path

1. Preserve the source schema as vocabulary and starter structure.
2. Keep Hosted DTP Phase 0 as the governing security/privacy/proof boundary.
3. Use the new manual templates in real work before encoding them as database tables.
4. Create a merged schema design doc before any migration.
5. Add RLS, storage pointers, import/export, redaction, proof, evidence, permission, and classification in the merged design.
6. Only then write migrations.

## Explicit Non-Goals For This Slice

- No SQL migration.
- No Supabase project changes.
- No hosted DTP app shell.
- No client portal.
- No autonomous agents.
- No unmanaged self-learning.
- No QuickBooks, Notion, Gmail, or Hub sync tables.
- No public proof workflow beyond existing proof-governance docs.

## Open Questions

- Should `clients` remain separate from `engagements`, or should Phase 0 keep a simpler engagement-centered model until repeated work proves normalization is needed?
- Which source modules deserve first-class database tables versus artifact records with typed templates?
- Which evidence fields need exact parity with existing repo evidence indexes?
- What import/export format best preserves local private kits if hosted DTP becomes the daily app?
