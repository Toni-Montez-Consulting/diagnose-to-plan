---
data_class: P1
confidential: false
permission_level: internal_only
review_status: draft
created: '2026-05-16T00:00:00Z'
fixture: true
---

# Omnexus Business Memory OS Diagnostic

Omnexus is Toni's known-business test case for the Business Memory OS
diagnostic. It uses only tracked repo and internal-safe facts from the
`fitness-app` / Omnexus docs.

This is internal diagnostic material. It is not public proof, a client claim,
an App Store readiness claim, or an instruction to connect private dashboards,
billing systems, support inboxes, App Store Connect, PostHog, Sentry, Stripe,
Supabase, or Apple data.

## Business Snapshot

- Business: Omnexus.
- Owner / operator: Toni, founder/operator.
- Industry: consumer fitness, AI coaching, workout tracking, learning, and
  mobile app subscription.
- Team size: founder-led product with AI/coding-agent support and external
  platform dependencies.
- Main customer type: people who want structured training, workout logging,
  AI coaching, learning, and progress support.
- Current systems: React/Vite/Capacitor app, Vercel functions, Supabase,
  Anthropic/OpenAI, PubMed, Stripe, Apple IAP, App Store Connect, PostHog,
  Sentry, GitHub Actions, repo docs, roadmap/backlog files, release receipts,
  and support/ops runbooks.
- Primary pain: product state, launch evidence, support readiness,
  subscription behavior, review status, and next operating actions are spread
  across docs, code, dashboards, App Store/manual evidence, and founder memory.
- Existing AI/tool usage: AI coach in product; AI/coding agents in delivery;
  no governed Business Memory OS layer for founder operations.

## Knowledge Map

| Knowledge area | Where it lives now | Trusted? | Owner | Freshness | Notes |
|---|---|---|---|---|---|
| Product scope / offers | `docs/HOW_OMNEXUS_WORKS.md`, product docs, app routes | yes | founder/product | changes often | Strong source trail, but future strategy can outrun docs. |
| Pricing / subscriptions | Subscription code, Stripe docs, Apple IAP docs, store receipts | partial | founder/platform | changes often | Web Stripe and iOS Apple IAP must stay distinct. |
| Customer onboarding | onboarding flow docs, app code, product user flows | yes | product | changes often | Guest, account, generated program, and upgrade paths need one readable state. |
| SOPs / process | launch docs, App Store repair docs, ops runbooks, CI docs | partial | founder/engineering | changes often | Good trail, but many docs are historical after approval. |
| Follow-up / support | support links, ops checks, issue/backlog docs, founder notes | partial | founder/support | changes often | Needs support triage and owner-action memory. |
| Vendor/admin | Vercel, Supabase, Stripe, Apple, AI providers, PostHog, Sentry docs | partial | founder | stable / changes often | Secrets and private dashboards stay outside tracked diagnostics. |
| Metrics/reporting | PostHog, Sentry, Vercel, Supabase, App Store Connect, roadmap docs | partial | founder/product | changes often | Use summaries and questions only; do not copy raw private records. |

## Recurring Question Inventory

| # | Question | Asked by | Answer lives where? | Owner | Changes how often? | Safe for AI? | After-answer action | Classification |
|---|---|---|---|---|---|---|---|---|
| 1 | What is the current shipped product scope? | founder / engineer | `docs/HOW_OMNEXUS_WORKS.md`, V1 scope, app routes | product | often | yes | Summarize current scope with source links | search |
| 2 | Which launch or App Store tracker rows are historical versus current blockers? | founder / engineer | approval closeout, submission tracker, execution backlog | founder | often | maybe | Flag stale blockers and current gates for review | draft |
| 3 | What should be checked before calling the iOS release ready? | founder | submission checklist, live-proof checklist, App Store evidence | founder | often | maybe | Draft release-proof checklist for human review | draft |
| 4 | Which subscription path applies on iOS versus web? | founder / engineer | IAP decision docs, subscription code, billing docs | engineering | stable / changes often | yes | Return source-backed distinction and caveats | search |
| 5 | Is this subscription or entitlement issue Stripe, Apple IAP, or app state? | founder / support | billing state machine, code, support facts, dashboards | founder / support | daily | maybe | Triage path; do not mutate billing | workflow |
| 6 | Which user trust surfaces must stay easy to find? | founder / reviewer | account deletion, export, privacy, support, metadata docs | product | stable | yes | Add to review checklist | workflow |
| 7 | What should a support reply say for a failed payment or restore issue? | founder / support | support policy, subscription docs, private account facts | support | often | maybe | Draft response after human verifies account state | draft |
| 8 | Which AI coach limits or model routes are active? | founder / engineer | AI route policy, entitlements, API docs, code | engineering | often | yes | Summarize routing and quota state | search |
| 9 | What are the highest-risk product areas before release work? | founder / engineer | AGENTS, invariants, roadmap, launch docs | founder / engineering | stable | yes | Produce risk checklist | draft |
| 10 | Which docs should a future agent read before touching billing? | engineer / agent | AGENTS, billing docs, roadmap, code ownership | engineering | stable | yes | Return source list and no-touch warnings | search |
| 11 | What changed in the last release or PR? | founder / engineer | git history, PR notes, release notes | engineering | daily | yes | Generate release summary draft | draft |
| 12 | Which production checks should run after a launch? | founder | ops runbooks, SLO docs, live-proof docs | founder / ops | stable | yes | Create manual check queue | workflow |
| 13 | What metrics indicate early user trust is healthy? | founder | PostHog, Sentry, support notes, ops docs | founder / product | weekly | maybe | Draft weekly owner memo after dashboard review | draft |
| 14 | Which roadmap lane should a new idea enter? | founder | execution backlog, future roadmap, strategy docs | founder | often | yes | Route to backlog lane or park | workflow |
| 15 | Is a reported issue launch-critical or normal backlog? | founder / support | issue details, SLO docs, roadmap priority rules | founder | daily | maybe | Draft severity and next action | draft |
| 16 | What should not be built yet? | founder / agent | roadmap, strategy, proof gates, parked ideas | founder | often | yes | Return blocked/parked rationale | search |
| 17 | Which App Store proof can be described publicly? | founder | proof packets, approval closeout, permission gates | founder | often | maybe | Route to proof/redaction review | workflow |
| 18 | Which private evidence must stay out of tracked docs? | founder / agent | approval closeout, no-secrets policy, proof templates | founder | stable | yes | Block copying private evidence | workflow |
| 19 | What is the next best retention improvement? | founder / product | execution backlog, product audits, analytics summaries | product | weekly | maybe | Draft story options for review | draft |
| 20 | Which user journey should be smoked after a release? | founder / engineer | user flows, release checklist, live proof docs | engineering | stable | yes | Produce smoke checklist | workflow |
| 21 | Does this feature need native/App Store review attention? | engineer / agent | native docs, App Store repair docs, submission rules | engineering | often | yes | Add submission-lint or manual gate | workflow |
| 22 | Which docs are current versus archival? | founder / agent | doc headers, closeout notes, roadmap status | founder | often | yes | Mark source confidence in answer | search |
| 23 | Should AI answer a health, injury, or medical-adjacent question? | user / founder | product safety docs, AI prompts, disclaimers | product | stable | no | Human/safety policy review only | human |
| 24 | Can an agent change billing, App Store, user, or production state? | agent / founder | repo instructions, approval gates, platform policy | founder | stable | no | Require explicit human approval | human |
| 25 | What should go in the weekly founder operating memo? | founder | roadmap, release state, support status, metrics summaries | founder | weekly | maybe | Draft memo from approved summaries | draft |

## Classification Summary

| Classification | Count | What it means |
|---|---:|---|
| Search only | 7 | The answer can be grounded in tracked docs or code pointers. |
| Draft only | 8 | AI can propose language or a read, but Toni reviews before acting. |
| Workflow | 8 | The value is routing, checklists, support queues, or proof gates. |
| Do not automate | 2 | Health/medical-adjacent guidance and production/billing/App Store authority stay human. |

## Opportunity Score

| Candidate | Repetition | Pain | Source trust | AI safety | Business value | Score | Notes |
|---|---|---|---|---|---|---:|---|
| Release and support memory cockpit | high | high | medium | medium | high | 23 | Best first internal assistant because it reduces founder memory load without taking live action. |
| Billing and App Store state explainer | high | high | medium | medium | high | 22 | Strong value if it stays read-only and separates Stripe, Apple IAP, App Store, and app-state facts. |
| Weekly founder operating memo | high | medium | medium | high | high | 20 | Useful once source summaries are approved and dashboards remain external/private. |

## Recommendation

- Best first assistant/workflow: release and support memory cockpit.
- Why this one: Omnexus has enough product, launch, App Store, billing,
  release, support, and roadmap evidence that founder memory becomes a real
  bottleneck, but the safest first layer is read-only synthesis and checklist
  routing.
- What to clean up first: current-versus-historical launch docs, subscription
  source map, live-proof checklist, support escalation paths, and weekly owner
  memo format.
- What not to connect yet: App Store Connect writes, Stripe or Apple billing
  actions, private user records, private support messages, raw analytics,
  Sentry event payloads, Supabase service-role operations, or automatic public
  proof publishing.
- Human-review point: Toni approves release readiness, billing support
  decisions, public claims, support replies, and production/App Store actions.
- Handoff/runbook needed: source map, stale-doc rules, current-state summary,
  release/support checklist, billing/App Store escalation path, and weekly memo
  cadence.
- Suggested path:
  - [ ] no build yet
  - [x] Knowledge Layer Audit
  - [x] Business Memory Assistant
  - [ ] Business Memory OS
  - [ ] park

## What This Proves

The diagnostic produces a clearer first workflow than a generic "AI search"
pitch: read-only release/support memory for a founder-operated app.

For Omnexus, the Business Memory OS lens is useful because it turns scattered
docs, launch receipts, subscription rules, proof gates, and roadmap state into
ranked operating questions. It does not justify a public offer, product
platform, or connected assistant yet.

The next useful test is not more software. It is review: decide whether this
Omnexus fixture and the Northline fixture are specific enough to become a
repeatable diagnostic review pattern.
