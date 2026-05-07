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
| Consulting squad pointer | consulting | Done | public repo points future proof/offer work back to DTP |
| Repo role split | DTP | Done | DTP, consulting, Hub, and `tm-skills` boundaries are explicit |
| Completed references | DTP | Done | DeMario/Mario and Omnexus are reference projects, not the next pilot |

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

## Acceptance

This wave is accepted when:

- Greg and CCAAP each have a completed Client OS packet and receipt;
- Cam is either confirmed into the same loop or explicitly still waiting;
- Knowledge Base V1 docs and templates exist;
- Hub and `tm-skills` have repo-local readiness notes without authority creep;
- consulting has a UX/design-system audit without premature proof publishing;
- the backlog reflects this order;
- validation gates pass or failures are recorded honestly.

