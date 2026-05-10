---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Autonomy Readiness Ladder V0

Status: internal autonomy gate and sequencing model

Owner repo: `diagnose-to-plan`

## Thesis

Toni wants a larger squad ecosystem and eventually autonomous agents. The
practice should preserve that ambition while proving the rails that make
autonomy useful, explainable, reversible, and safe.

Core rule:

> Autonomy is earned by evidence, not granted by excitement.

The ladder exists so future agents, squads, workflows, hosted DTP, and FAOS can
advance deliberately instead of staying manual forever or jumping straight into
untrusted action.

## What This Solves

Without a ladder, the practice tends to swing between two bad states:

- everything stays lightweight and manual forever;
- a promising idea jumps too quickly into autonomous behavior.

The useful middle is staged autonomy:

1. prove the workflow manually;
2. make the source, decision, and output visible;
3. add read-only recommendation;
4. add draft-only production;
5. add supervised execution;
6. add bounded autonomy only where the workflow has gates, logs, evals, and
   rollback.

## Autonomy Levels

| Level | Name | Agent Can | Agent Cannot | Typical Candidates |
|---|---|---|---|---|
| A0 | Manual only | follow instructions in chat and use templates after explicit prompt | initiate work, schedule, write, send, sync, merge, or mutate state by itself | legal/compliance claims, public proof, payments, production data, client commitments |
| A1 | Read-only recommendation | inspect approved sources, summarize, classify, recommend, flag drift | write source-of-truth state, send messages, create public claims, install tools, mutate repos | Research Steward, Memory Steward, status dashboards, repo-health reviews |
| A2 | Draft-only operator | create drafts, packets, decision records, specs, source indexes, PR descriptions, and email drafts | send, publish, merge, deploy, sync Notion, change live data, or present drafts as approved | External Communications, proposal drafts, client packets, research digests |
| A3 | Supervised local execution | edit scoped files, run tests, regenerate local dashboards, prepare PRs after an accepted task | act outside the approved repo/scope, touch live systems, expose private data, or bypass validation | DTP docs/templates, consulting site copy after copy gate, repo-local tests |
| A4 | Bounded scheduled workflow | run on an event or cadence, write only to approved internal queues/drafts, produce audit logs | touch public/client/live surfaces, make irreversible changes, or run without failure review | source freshness sweeps, stale-doc detection, KB freshness checks, validation sweep drafts |
| A5 | Bounded live action | perform approved low-risk external writes with scoped credentials, logs, rollback, and human override | act on money, legal, production config, client commitments, public claims, or private data outside scope | sanitized Notion mirror update, GitHub issue/PR creation, low-risk status sync |
| A6 | High-trust autonomous action | execute high-value workflows with mature evals, monitoring, escalation, kill switch, and rollback | operate without owner, budget, trace, policy, or incident path | future only; no current DTP workflow qualifies |

The current practice default is A0 to A2. A3 is allowed when Toni explicitly
asks for implementation in a scoped repo. A4 and higher require a readiness
review.

## First Autonomy Candidates

The safest early candidates are internal, read-only, and evidence-producing.

| Candidate | Starting Level | Next Possible Level | Why First | Hard Stop |
|---|---|---|---|---|
| Research source freshness | A1 | A4 | sources are public/internal, output can be a queue or digest draft | no public claims or tool installs |
| Memory review queue | A1 | A2 | can recommend promotion/parking without changing memory authority | no autonomous playbook promotion |
| Practice/status dashboards | A1 | A3/A4 | status visibility prevents drift and does not need client action | no Notion/live sync without gate |
| Knowledge-base drift review | A1 | A4 | flags stale docs and missing routing before they hurt execution | no source rewrite without review |
| External communications drafts | A2 | A3 for local draft files only | high leverage, but sending must stay human-approved | no auto-send |
| Repo-local validation sweeps | A1 | A3/A4 | repeatable commands can produce evidence | no deploy, secret, database, or cloud mutation |
| Notion mirror draft updates | A2 | A5 later | useful cockpit support after DTP update | Notion cannot become source of truth |

## Readiness Gates

Every move up the ladder needs a written readiness review.

Use `practice-os/templates/autonomy-readiness-review.md`.

Minimum gates:

- named owner and owning repo/lane;
- source scope and blocked sources;
- data classification and privacy boundary;
- allowed reads;
- allowed writes;
- allowed trigger: manual, event-based, scheduled, or continuous;
- expected output and destination;
- evidence and eval fixtures;
- audit log or receipt path;
- rollback or undo path;
- human override or kill switch;
- cost/budget boundary when external services are involved;
- failure modes and escalation path;
- approval gate before the next autonomy level.

If any gate is missing, keep the workflow at the lower level.

## Level-Specific Standards

### A1 Read-Only Recommendation

Required:

- approved source list;
- no credentialed write access;
- clear recommendation format;
- evidence limit;
- next human decision.

Good fit:

- research steward;
- memory steward;
- proof queue review;
- stale routing review;
- status dashboards.

### A2 Draft-Only Operator

Required:

- draft destination;
- review owner;
- label that the output is unapproved;
- redaction/privacy check when client context is used;
- no send/publish/deploy/sync action.

Good fit:

- Gmail draft creation after Toni asks;
- proposal or packet drafts;
- decision records;
- source indexes;
- PR descriptions.

### A3 Supervised Local Execution

Required:

- scoped task;
- owning repo;
- allowed file set or module boundary;
- validation commands;
- no live external mutation;
- commit/PR only when requested or accepted.

Good fit:

- DTP docs/templates;
- consulting site implementation after copy/design gate;
- Hub code after runtime/migration gate;
- generated dashboards.

### A4 Bounded Scheduled Workflow

Required:

- event/cadence trigger;
- dry-run mode;
- audit log;
- output queue;
- duplicate/drift handling;
- max runtime and failure policy;
- human review before applying changes.

Good fit:

- weekly source freshness report;
- stale-doc drift detector;
- workspace status digest;
- dependency/update recommendation draft.

### A5 Bounded Live Action

Required:

- least-privilege credentials;
- scoped external surface;
- idempotent write behavior;
- rollback path;
- audit log;
- explicit owner approval for the class of action;
- monitoring/failure alert.

Good fit later:

- sanitized Notion mirror update after DTP source update;
- GitHub issue/PR creation from accepted DTP records;
- low-risk dashboard publication.

### A6 High-Trust Autonomous Action

No current practice workflow qualifies.

This level requires:

- repeated successful lower-level runs;
- evals and trace review;
- incident/rollback process;
- kill switch;
- budget limits;
- owner acceptance;
- legal/privacy/security review when relevant.

## Blocked Until Explicit Approval

These stay manual or human-approved even if adjacent workflows become
autonomous:

- sending client/prospect emails;
- calendar invites or meeting changes;
- public proof, case studies, testimonials, or outcome claims;
- pricing, contract, legal, tax, insurance, or compliance language;
- payment, billing, banking, subscription, or invoice actions;
- production deploys, DNS, cloud config, database migrations, secrets, OAuth,
  or credential changes;
- anything using Microsoft confidential, customer-sensitive, or day-job
  context;
- raw private client relationship records;
- public site copy derived from private or unreviewed sources.

## Relationship To Existing Systems

| System | Relationship |
|---|---|
| Agent Squads + Knowledge Base V0 | defines roles, squads, source scope, value justification, approvals, and handoffs |
| Knowledge Base Event Workflows V0 | captures events that may justify moving a workflow up the ladder |
| Practice Evolution System V0 | matures collaboration patterns and agent behaviors into reviewed memory |
| Research Arm V0 | first candidate for A1 and later A4 source freshness workflows |
| Memory Control Plane | first candidate for A1/A2 memory review workflows |
| Practice Intelligence Control Plane | input router that decides which gate applies before action |
| FAOS Orchestration Roadmap | future technical substrate after readiness gates prove the need |
| Hub | possible runtime support later, not the source of autonomy authority |
| Notion | mirror/cockpit candidate for A5 only after DTP remains source of truth |

## How To Use This

When Toni asks for autonomous agents, a larger squad, an agent manager, an
automated steward, a recurring workflow, or a knowledge-base maintainer:

1. Identify the candidate workflow.
2. Assign the current autonomy level.
3. Name the desired next level.
4. Fill `practice-os/templates/autonomy-readiness-review.md`.
5. Decide whether the next step is a role spec, event workflow, eval fixture,
   source list, dashboard, queue, PR, or parked FAOS story.
6. Leave a steward receipt.

## Acceptance Criteria

This ladder is working if:

- Toni's ambition for autonomous agents is preserved, not dampened;
- future agents can tell why a workflow is manual, draft-only, supervised, or
  autonomous;
- the first autonomy candidates are obvious;
- risky actions stay gated;
- repeated manual work becomes a candidate for higher autonomy instead of being
  forgotten;
- FAOS has a clearer path from idea to safe implementation.

