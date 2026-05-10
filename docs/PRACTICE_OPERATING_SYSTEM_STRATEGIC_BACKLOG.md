---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice Operating System Strategic Backlog

Status: implementation backlog for the next Practice OS wave.

Owner repo: `diagnose-to-plan`

Primary decision: prove the operating system in real client/operator work before
building more architecture, hosted workflow, vector memory, or agent
orchestration.

## Operating Thesis

The Practice OS should make Toni's consulting practice easier to run, easier to
trust, and easier for agents to help with. The near-term system is not a public
product, CRM, autonomous agent manager, or generic knowledge base. It is a
source-indexed operating loop with receipts.

This does not flatten the long-term ambition. Toni wants a larger squad system
and eventually autonomous agents where they are genuinely useful. The near-term
answer is to prove the operating loop first, then move repeated workflows up
`docs/AUTONOMY_READINESS_LADDER_V0.md` when the source scope, evals, audit
logs, rollback, privacy boundary, and approval gates are ready.

The first wave is draft-only automation:

- agents prepare briefs, packets, audits, source indexes, PR notes, and next
  action drafts;
- humans approve client communication, public proof, publishing, scheduling,
  production writes, and repo mutation;
- DTP remains the source of truth;
- Notion, Gmail, Calendar, Hub, and project repos remain input or execution
  surfaces.

## P0 Foundation

| Work | Owner | Status | Done gate |
|---|---|---|---|
| Agent Squads + Knowledge Base V0 | DTP | Done | source map, templates, approval gates, and receipt pattern merged |
| Agent Source Registry + Web Evidence Policy V0 | DTP | Done | all current and future roles can use web search under source tiers, role source posture, and promotion gates |
| Consulting squad pointer | consulting | Done | public repo points future proof/offer work back to DTP |
| Repo role split | DTP | Done | DTP, consulting, Hub, and `tm-skills` boundaries are explicit |
| Autonomy Readiness Ladder V0 | DTP | Done | autonomy levels, candidate workflows, readiness gates, template, and receipt pattern exist |
| Practice Operating Review Loop V0 | DTP | Done | daily-light and weekly-review cadence exists for turning captured signals into decisions |
| Completed references | DTP | Done | DeMario/Mario and Omnexus are reference projects, not the next pilot |

## P0 Workflow Spine Implementation

The next P0 fix is the Workflow Spine: one canonical, markdown-first operating
state object for active client/operator work.

Source receipt:

- `practice-os/steward/2026-05-07-workflow-spine-p0-implementation-plan.md`

Order:

1. Define the minimal doc lifecycle vocabulary needed for stale/current labels.
2. Add a DTP-linked `tm-skills` readiness scorecard without promoting candidate
   skills or changing global install state.
3. Create `practice-os/templates/workflow-spine.md`.
4. Create a Greg Workflow Spine record for launch-readiness discovery.
5. Create a Cam Workflow Spine record for waiting-on-packet/build readiness.
6. Label only obvious stale docs; do not move, delete, or broadly archive docs
   in P0.

Done gate:

- future agents can open one Workflow Spine record for Greg or Cam and know the
  current state, canonical source files, allowed actions, blocked actions,
  proof posture, open gates, and next artifact to update.

P1 remains parked until this P0 spine exists: dashboard parsing, completeness
scores, full archive index, persistent mirrors, hosted workflow updates, vector
retrieval, and broader lane expansion.

Use `docs/PRACTICE_OPERATING_REVIEW_LOOP_V0.md` after each substantial internal
OS pass so the Workflow Spine, Kaizen, Evolution, Memory Steward, Research
Steward, KB-event, and Autonomy surfaces produce decisions instead of passive
status.

Current internal-OS next action from the first operating review:

- `practice-os/steward/2026-05-10-autonomy-readiness-review-internal-candidates.md`
  approves Research source freshness as the first autonomy candidate to move
  forward, but only as a dry-run design.
- `docs/RESEARCH_SOURCE_FRESHNESS_DRY_RUN_V0.md` now defines the source subset,
  output schema, dry-run queue path, validation command, blocked-source
  behavior, and human review states.
- `dtp research source-freshness` is now the local dry-run command. It accepts
  source snapshots/operator notes, URLs, optional public fetches, and search
  packets/results, then emits schema-validated queue items under ignored
  `outputs/research-source-freshness/`.
- `docs/AGENT_SOURCE_REGISTRY_AND_WEB_EVIDENCE_POLICY_V0.md` now defines the
  role-level evidence policy for all current and future agent functions. It
  allows broad web search while keeping official/primary sources first and
  requiring human-gated promotion before public, client, legal, finance,
  runtime, or repo-authority changes.
- `practice-os/steward/2026-05-10-agent-source-policy-first-pilot.md` records
  the first source-policy pilot. It tested OpenAI Agents SDK docs as an
  AI/platform source and Microsoft 2026 Work Trend Index as a consulting /
  business source, then promoted reviewed source-freshness records into a
  decision record and pattern candidate.
- `practice-os/steward/2026-05-10-external-communications-source-policy-pilot.md`
  records the second role pilot. It converted reviewed source evidence into
  draft-only prospect, executive, and client-education language with explicit
  send/public-proof gates.
- The next action is to run one more role pilot, ideally Consulting Strategy,
  then decide whether to add structured source configs, deduplication, source
  snapshots, richer search parsing, or the first machine-readable agent
  source-pack file. Do not implement a scheduled workflow until dry-run queues
  prove useful and a new autonomy-readiness review is accepted.

## P1 Client OS Pilot Wave

Order:

1. Greg / TheGrantApp.io on 2026-05-08.
2. CCAAP prototype review on 2026-05-12.
3. Cam after the active recurring sync and item-packet state are confirmed.

Each pilot must produce:

- Client OS packet;
- source index;
- meeting intent;
- permission/privacy notes;
- post-meeting receipt;
- open-loop list;
- next-action packet;
- squad handoff receipt when a squad is used.

Public DTP docs may carry only sanitized lane/status/gate facts. Private working
truth belongs in the nested `engagements` vault or future hosted private DTP.

## P1 Knowledge Base V1

Knowledge Base V1 is still markdown-first. It upgrades V0 from a source-index
habit into a repeatable corpus shape:

- every record names owner, source, data class, review state, freshness, and
  blocked sources;
- every client/operator loop leaves a receipt;
- every useful pattern has a promotion path from raw capture to playbook memory;
- validation detects missing sources, stale pointers, unclosed gates, and
  receipts without owners.

Hosted DTP remains the scale target, but the schema should follow repeated
markdown examples rather than imagined platform needs.

## P2 Runtime And Skill Layers

Hub supports runtime, intake, private console evidence, prompts, webhooks,
health, and future memory retrieval. It does not own client truth, public proof,
DTP roadmap state, CRM, billing, or the practice cockpit.

`tm-skills` supports reusable SDLC behavior. It does not own client records,
proof packets, public offers, COI, redaction, or Practice OS roadmap ownership.

Near-term work:

- Hub: clarify runtime readiness, route classification, v0.4 hardening, and
  live-intake evidence without expanding authority.
- `tm-skills`: run doctor/freshness/install preview, classify untracked skill
  candidates, and keep external smoke manual until reloads are observed.

## P2 Consulting Design And Architecture Cleanup

Consulting gets an audit now, not public proof changes.

Audit dimensions:

- CTA clarity;
- navigation and first-visit comprehension;
- originality and visual polish;
- mobile/desktop layout quality;
- case-study/proof presentation;
- component inventory and design-system health;
- route/data-flow architecture clarity.

Public proof and case-study content still waits for DTP evidence, permission,
redaction, reviewer, and caveat gates.

## P3 Vector Brain Path

Vector memory can help once the markdown corpus is disciplined. Useful first
jobs:

- meeting prep from source-indexed records;
- "what have we solved like this before";
- proof-gap search;
- drift detection;
- cross-repo architecture lookup;
- source packs for future agent sessions.

Sequence:

1. Markdown corpus with stable metadata.
2. Sanitized local retrieval prototype.
3. Hosted/RLS-backed retrieval.
4. Agent-integrated retrieval only after privacy, citation, and refusal tests.

## P3 FAOS Readiness

FAOS stays readiness/review work until at least two Client OS pilot loops are
complete. The next FAOS move is a separate command/version/readiness pass, not a
new repo or service.

Any FAOS workflow that would become scheduled, write-enabled, live, or
externally mutating must pass the Autonomy Readiness Ladder first. The first
likely candidates are read-only Research/Memory/Status workflows, then
draft-only communications and local validation sweeps, not client-facing,
payment, legal, public-proof, or production actions.

## Acceptance

This wave is accepted when:

- Workflow Spine P0 exists with lifecycle vocabulary, `tm-skills` readiness
  scorecard, template, Greg record, Cam record, and obvious stale labels;
- Greg and CCAAP each have a completed Client OS packet and receipt;
- Cam is either confirmed into the same loop or explicitly still waiting;
- Knowledge Base V1 docs and templates exist;
- autonomy candidates are classified through the Autonomy Readiness Ladder
  before any autonomous runtime or write-enabled workflow is proposed;
- the Practice Operating Review Loop is used to decide what gets promoted,
  parked, built, piloted, rejected, or superseded after major internal OS work;
- Hub and `tm-skills` have repo-local readiness notes without authority creep;
- consulting has a UX/design-system audit without premature proof publishing;
- the backlog reflects this order;
- validation gates pass or failures are recorded honestly.

