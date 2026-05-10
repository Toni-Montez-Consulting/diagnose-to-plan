---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Agent Source Registry And Web Evidence Policy V0

Status: internal evidence policy and first source registry for specialized
agent roles

Owner repo: `diagnose-to-plan`

## Purpose

Toni wants every agent, steward, and function in the practice system to be able
to use web search when it helps the work. That is the right direction. Each
domain has credible outside sources, and the system should use them instead of
pretending the repo already knows everything.

This policy makes that useful without letting search results become accidental
authority.

Core rule:

> Search can inform every agent. Search cannot authorize action by itself.

## Scope

This V0 policy covers:

- specialized agent roles in `practice-os/agents/`;
- squad lenses in `docs/AGENT_SQUADS_KNOWLEDGE_BASE_V0.md`;
- Research Arm source freshness work;
- Memory Steward, Research Steward, and future status stewards;
- consulting, product, engineering, design, operations, finance, legal,
  compliance, and communications reasoning;
- future machine-readable source packs.

It does not create:

- autonomous web crawlers;
- scheduled source monitors;
- public claims;
- legal, tax, accounting, medical, compliance, or financial advice;
- client communications;
- Notion sync;
- live repo, cloud, billing, DNS, database, calendar, or email actions.

## Web Evidence Defaults

All agent roles may use web search when the work would benefit from current or
domain-specific evidence.

Default posture:

1. Start with DTP source-of-truth docs, repo state, approved client records, and
   Toni's latest instruction.
2. Use official or primary sources first when factual accuracy matters.
3. Use broad web search for discovery, framing, market sense, examples,
   language, or source finding.
4. Treat broad search results as low-confidence until corroborated by primary,
   official, standards, or directly observed sources.
5. Attach source date, source type, evidence limit, and review state when a
   source affects a durable artifact.
6. Use `dtp research source-freshness` when a source check, search query, or
   public URL should create a reviewable queue item.
7. Promote evidence through the right human-gated artifact before changing
   public copy, client communication, pricing, legal posture, technical
   architecture, runtime behavior, or repo-owned knowledge bases.

## Evidence Tiers

| Tier | Source type | Default use | Confidence posture |
|---|---|---|---|
| 0 | Toni-provided source material, repo evidence, approved client/operator notes, meeting transcripts, internal receipts | intent, real operating need, accepted decisions, field signal | high for internal direction; public use still gated |
| 1 | Official product docs, release notes, changelogs, API references, vendor announcements, regulator pages, direct dataset or source documents | current facts, implementation details, platform behavior | medium to high after review |
| 2 | Standards, security bodies, governance bodies, peer-reviewed research, professional bodies, recognized benchmarks | governance, risk, accessibility, security, quality, explainability | medium to high after applicability review |
| 3 | Reputable analyst reports, industry reports, business essays, newsletters, podcasts, books, expert social posts with cited sources | trend sensing, framing, buyer language, hypotheses, examples | low to medium until corroborated |
| 4 | Loose social posts, screenshots, forums, unsourced commentary, anonymous claims, generic search summaries | inspiration and source discovery only | low; do not use for claims or decisions |

## Promotion Path

Use this path when web evidence or domain research matters beyond a single chat
answer:

1. Route the prompt through `practice-os/templates/activation-routing-map.md`.
2. Select the relevant agent role or squad lens.
3. Check DTP docs and repo-local sources first.
4. Search the web using the role's source posture.
5. Capture reusable or currentness-sensitive findings with
   `dtp research source-freshness`.
6. State the evidence limit.
7. Ask Toni for review when the finding would change durable memory,
   messaging, public proof, client communication, pricing, architecture,
   runtime behavior, legal/compliance posture, finance/tax posture, or
   autonomous authority.
8. Promote the finding to the right artifact:
   - research decision record;
   - research pattern candidate;
   - knowledge-base event record;
   - idea-evolution record;
   - memory-promotion record;
   - steward receipt;
   - ADR;
   - client deliverable draft;
   - implementation plan or review.

## Agent Source Registry

The table below is the first role-level source registry. Current first-wave
roles and broader future roster entries are included so future agents can see
the ambition without treating every role as autonomous or live.

| Role or function | Primary sources | Web source posture | Default outputs | Blocked without approval |
|---|---|---|---|---|
| Research Steward / Research Arm | DTP research docs, source list, freshness queues, saved reports, approved internal notes | official docs and standards first; broad search allowed for discovery and trend sensing | digest, decision record, pattern candidate, source-freshness item | public claims, client comms, tool installs, repo changes, scheduled crawling |
| Memory Steward | DTP Kaizen, Practice Evolution, steward receipts, promoted memory records, docs map | web only for memory-method, retrieval, and tooling patterns; not for Toni-specific facts | promotion recommendation, parking recommendation, memory source index | autonomous self-learning, Notion source-of-truth shift, public or client action |
| Consulting Strategy Agent | DTP offer/proof docs, pricing posture, buyer notes, approved field evidence | consulting packaging, SMB/startup research, pricing benchmarks, market reports as context; corroborate before claims | offer framing, scope shape, value case, bad-fit boundaries | unsupported ROI, public offer changes, pricing commitments, proof claims |
| External Communications Agent | client thread, approved context, DTP proof gates, authentic voice policy, send-ready drafts | web only for factual references, audience context, or external claim verification | email summary, draft, executive update, follow-up receipt | sending, unsupported claims, legal/finance advice, private data exposure |
| Product Strategy Agent | user feedback, transcripts, analytics if approved, roadmap, product docs | product docs, market pages, competitor pages, JTBD/product references, app-store patterns | product memo, MVP scope, adoption loop, feedback synthesis | invented demand, market proof, conversion claims, roadmap commitments |
| UX / Design Agent | repo UI, screenshots, design system, visual QA, user task flow | WCAG/W3C, platform guidelines, Nielsen Norman Group, Baymard, design-system docs | page spine, UI critique, craft brief, accessibility notes | new public visual direction without brief, private-proof exposure |
| Web Experience Agent | consulting source, sitemap/routes, analytics or Search Console if approved, screenshots | Astro/Vercel docs, accessibility sources, SEO docs, web UX references, conversion examples | page architecture, route QA, public-site improvement plan | public claims, proof movement, tracking changes, deploy decisions |
| Software Architecture Agent | repo source, ADRs, data flows, manifests, runtime docs | official framework docs, cloud docs, API specs, Postgres/Supabase/Vercel/Azure/AWS/GCP docs | ADR, architecture review, integration plan, tradeoff memo | new runtime authority, schema changes, cross-repo orchestration |
| Software Engineering Agent | repo source, tests, CI, lockfiles, local AGENTS.md, issue context | official library docs, changelogs, security advisories, examples from source repos | code change, test plan, implementation handoff | production writes, deploys, commits/pushes unless requested, broad repo churn |
| DevOps / Infrastructure Agent | CI/CD, deployment docs, env inventories, logs if approved, rollback plans | official cloud docs, provider changelogs, status pages, OWASP, NIST, CIS, Terraform docs | readiness review, runbook, rollback plan, cost/risk note | deploys, DNS, billing, secrets, OAuth, DB migrations, live config |
| QA / Audit Agent | tests, CI logs, screenshots, acceptance criteria, repo manifests | testing framework docs, security advisories, WCAG, OWASP, platform guidance | go/no-go review, regression list, acceptance evidence | calling work done without evidence, public release approval by itself |
| COO Agent | operating receipts, meeting prep, engagement runbooks, project status, owner inputs | operations sources, project-management references, vendor docs for tools being used | cadence, runbook, status dashboard, handoff plan | changing source of truth, client comms, calendar changes without approval |
| Controller Agent | approved financial exports, Stripe/payment records, pipeline records, budgets, close notes | IRS/state official pages, accounting standards, Stripe docs, SBA and industry benchmarks | finance summary, pipeline arithmetic, close checklist | tax/legal/accounting advice, filings, bank/payment actions |
| Business Admin Agent | Google Workspace, Calendar, LLC/admin docs, Apple Reminders capture, internal offer catalog | Google/Apple/IRS/state official docs, vendor docs, admin best-practice references | admin checklist, policy draft, operating note | filings, calendar writes, account changes, public offers |
| General Counsel / Legal Review Agent | contracts, permission records, COI notes, privacy/proof gates, policy docs | official statutes/regulators/courts where relevant; law firm memos as context; Harvey MCP can be future tool source | issue-spotting memo, review questions, escalation gate | legal advice, contract approval, filings, unreviewed client-facing legal language |
| Compliance / AI Governance Agent | DTP AI/privacy policies, proof gates, architecture notes, data classification | NIST AI RMF, OWASP GenAI, FTC/regulator guidance, ISO or sector standards where applicable | governance review, risk note, guardrail checklist | certification claims, legal/compliance conclusions, public trust claims |
| Data Architecture Agent | schemas, data dictionaries, Supabase/Postgres docs, RLS policies, flow diagrams | official database docs, data-governance sources, privacy and security guidance | data-flow review, schema memo, migration risk note | migrations, production data access, data-retention policy changes |
| PR / Brand Narrative Agent | messaging KB, proof queue, authentic voice policy, approved claims library | brand strategy examples, press pages, communications references, source-backed market context | narrative options, public-safe angle, proof-language draft | publishing, unsupported proof, over-polished generic AI claims |
| Internal Review Agent | DTP docs, checklists, acceptance criteria, prior receipts | web only when the review needs external standards or current tool facts | critique, gap review, escalation note | final approval for gated public/client/legal/runtime actions |
| Legal Review Agent | same as General Counsel, with legal-domain focus | official legal sources first; secondary commentary only as context; Harvey MCP later | legal-risk review questions, counsel escalation memo | legal advice or final legal approval |
| Finance and Operations Squad | Controller, COO, Business Admin sources | official finance/admin/vendor sources first; broad search for benchmark context | operating packet, close inputs, admin backlog | filings, tax advice, bank actions, commitments |
| Research and Intelligence Squad | Research Arm, source list, source freshness, external reports | official and primary sources first; broad search allowed for discovery | digest, pattern candidates, decision records | autonomous crawler, public claims, tool adoption without review |
| Memory and Knowledge Stewardship Squad | DTP docs, evolution, Kaizen, receipts, docs map | web for retrieval/memory system patterns only | KB event, memory promotion, status review | self-modifying memory, silent KB rewrites |
| External Communications Squad | External Communications, Consulting Strategy, Legal/Compliance gates | web for claim verification and audience context | sendable draft, summary, comms review | send action, unsupported claims, private leakage |

## Source-Pack Rules

Machine-readable source packs encode this policy after real role workflows prove
the shape.

Current V0 location:

```text
practice-os/research/source-packs/agent-source-packs.v0.json
```

The source-pack file should not add new authority. It should encode this policy
for tools, dashboards, stewards, and future automation.

Validation is documented in `docs/AGENT_SOURCE_PACK_SCHEMA_V0.md` and enforced
by:

```powershell
.\.venv\Scripts\dtp.exe practice source-packs validate
```

`dtp practice doctor` also runs the same source-pack contract check.

V0 includes the roles proven by source-policy pilots:

- Research Steward / Research Arm;
- External Communications;
- Consulting Strategy;
- Software Architecture;
- Software Engineering;
- QA / Audit;
- DevOps / Infrastructure.

Minimum fields:

- `role_id`
- `role_name`
- `source_pack_version`
- `primary_sources`
- `allowed_web_sources`
- `search_posture`
- `evidence_tiers`
- `blocked_sources`
- `default_outputs`
- `promotion_required_for`
- `last_reviewed_at`

## Search Query Rules

Use search to find better sources, not just louder opinions.

Preferred query patterns:

- `site:<official-domain> <topic>`
- `<vendor/product> official docs <feature>`
- `<standard body> <topic> guidance`
- `<tool> changelog <feature>`
- `<domain> benchmark report <year> source`
- `<risk topic> OWASP NIST guidance`

When a role needs current evidence, prefer a source-freshness run:

```powershell
.\.venv\Scripts\dtp.exe research source-freshness `
  --source-id agent-source-check `
  --source-name "Agent source registry check" `
  --query "official AI agent governance guidance NIST OWASP"
```

If a public URL should be inspected:

```powershell
.\.venv\Scripts\dtp.exe research source-freshness `
  --source-id agent-source-check `
  --source-name "Agent source registry check" `
  --url "https://example.com/source" `
  --fetch-url
```

## Blocked Sources

Do not use these as raw evidence unless Toni explicitly opens the source and
the owning gate permits it:

- secrets or credentials;
- private client financial data;
- raw Gmail or calendar content outside the current approved task;
- Microsoft confidential or day-job material;
- private relationship notes;
- unredacted logs;
- private paid databases;
- screenshots without provenance;
- AI-generated summaries with no source trail;
- social posts used as proof rather than inspiration.

## Role Review Prompts

Each role should ask these questions before using web evidence in a durable
artifact:

1. What claim or decision is this source being used to support?
2. Is the source primary, official, standards-based, reputable secondary, or
   loose discovery?
3. What does this source not prove?
4. Does this source need a freshness check?
5. Does this belong in a decision record, pattern candidate, KB event, memory
   promotion record, ADR, or client draft?
6. What approval gate is required before action?

## Acceptance Scenarios

This policy is useful if future agents can:

- use web search without pretending every search result is reliable;
- select credible domain sources for each role;
- explain evidence quality in plain language;
- capture reusable source checks instead of losing them in chat;
- keep broad web search available while protecting public proof, client comms,
  legal, finance, privacy, security, repo, and runtime gates;
- add future source packs without changing the source-of-truth boundary.

## First Pilot

The first pilot is recorded in:

```text
practice-os/steward/2026-05-10-agent-source-policy-first-pilot.md
```

It tested:

- OpenAI Agents SDK docs as a Tier 1 AI/platform source;
- Microsoft 2026 Work Trend Index as a Tier 3 consulting/business source.

The pilot confirmed the source registry can produce reviewed source-freshness
items, a research decision record, and a research pattern candidate without
changing public copy, client communication, tooling, runtime behavior, or
autonomy level.

The pilot also surfaced and fixed a local dry-run run-id collision risk when
two source-freshness checks are run in parallel.

## Second Pilot

The second pilot is recorded in:

```text
practice-os/steward/2026-05-10-external-communications-source-policy-pilot.md
```

It tested whether the External Communications Agent could translate reviewed
source evidence into clear, client-safe language without sending a message,
changing public copy, or implying unsupported proof.

The pilot produced:

- a reusable internal communications artifact;
- prospect, executive, and client-education draft blocks;
- a send checklist for source-backed AI implementation language;
- messaging knowledge base updates that remain internal-only.

## Third Pilot

The third pilot is recorded in:

```text
practice-os/steward/2026-05-10-consulting-strategy-source-policy-pilot.md
```

It tested whether Consulting Strategy could turn source-backed AI/workflow
language into offer logic, buyer-fit criteria, Blueprint routing, and public
copy boundaries.

The strategy decision:

- do not lead publicly with AI as a standalone category;
- keep the front door broad around unclear ideas, broken workflows, and tech
  bottlenecks;
- route unclear AI/workflow opportunities to Business Systems Blueprint;
- allow Fast Track only for contained low-risk AI/workflow implementation;
- preserve public-copy and proof gates.

## Fourth Pilot

The fourth pilot is recorded in:

```text
practice-os/steward/2026-05-10-software-architecture-source-policy-pilot.md
```

It tested Software Architecture as the boundary and runtime-authority decision
layer.

The architecture decision:

- start with DTP, repo state, contracts, tests, and Toni's latest direction;
- use official platform docs for current technical behavior;
- treat cloud well-architected frameworks as review lenses, not mandates;
- use broad web search for source discovery only;
- require approval before schema, runtime, cloud, cross-repo, or autonomy
  changes.

## Fifth Pilot

The fifth pilot is recorded in:

```text
practice-os/steward/2026-05-10-software-engineering-source-policy-pilot.md
```

It tested Software Engineering as the repo-grounded implementation layer.

The engineering decision:

- code can move when Toni approved implementation, the owning repo is clear,
  and the change stays inside scope;
- repo instructions, nearby patterns, package scripts, tests, CI, and recent
  commits are the first implementation sources;
- official docs clarify current tool behavior;
- architecture handoff is required before source-of-truth, schema, runtime,
  autonomy, or cross-repo changes;
- green local checks are implementation evidence, not live production proof.

## Sixth Pilot

The sixth pilot is recorded in:

```text
practice-os/steward/2026-05-10-qa-audit-source-policy-pilot.md
```

It tested QA / Audit as the evidence-to-claim layer.

The QA decision:

- start with the exact claim being made;
- match tests, CI, logs, screenshots, route checks, and receipts to that claim;
- separate verified passes, confirmed failures, manual gates, missing evidence,
  residual risk, and queued follow-up;
- use official testing, browser, CI, security, accessibility, and platform docs
  when the claim depends on current tool or standard behavior;
- do not approve production release, public proof, client communication,
  legal/compliance posture, runtime behavior, or autonomy level changes.

## Seventh Pilot

The seventh pilot is recorded in:

```text
practice-os/steward/2026-05-10-devops-infrastructure-source-policy-pilot.md
```

It tested DevOps / Infrastructure as the runtime-evidence and mutation-gate
layer.

The DevOps decision:

- start with repo-local CI/CD, deployment, environment, monitoring, rollback,
  and handoff evidence;
- separate local, CI, preview, staging, production, and marketplace proof;
- use Architecture, Engineering, and QA evidence as handoff inputs;
- use official platform, cloud, database, hosting, CI, identity, security, and
  operational-excellence docs when current behavior matters;
- include rollback, observability, cost, quota, maintenance, and secret
  inventory in readiness reviews;
- do not deploy, mutate live infrastructure, update secrets, change DNS,
  change billing, run production migrations, or approve production readiness
  without explicit approval.

## Open Follow-Up

Next iteration:

1. Decide whether a dashboard should show source-pack freshness by role.
2. If continuing role pilots, choose Product Strategy, UX / Design, Web
   Experience, General Counsel, Compliance, Data Architecture, Controller, or
   another repeated-gap role.
