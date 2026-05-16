---
data_class: P1
confidential: false
permission_level: internal_only
review_status: draft
created: '2026-05-15T00:00:00Z'
---

# Practice Investment Roadmap 2026

This is a private infrastructure plan for Toni's consulting practice.

It is not a spending commitment. It exists so future revenue can be invested
deliberately instead of turning into random tools, subscriptions, or hardware.

The rule:

> Do not spend money to feel like the practice is real. Spend money only where
> it makes the practice more capable.

## Investment Thesis

The practice should stay small, serious, and high-quality.

The right operating cockpit should help Toni:

- understand the business;
- decide what is worth doing;
- build the right thing;
- explain it clearly;
- hand it off cleanly;
- stay close if support makes sense;
- keep clean boundaries between employment, product work, and consulting.

Do not buy enterprise tooling for a practice that is intentionally lean.

## Buy Now

Only buy or maintain these if they directly reduce friction, protect the
practice, or are already part of delivery.

| Category | Investment | Why | Notes |
|---|---|---|---|
| Security | Password manager and hardware security keys | Client data, repo access, and business accounts need clean boundaries | Highest trust-per-dollar item |
| Separation | Separate business accounts and folders | Prevents employer/client/personal crossover | More important than fancy tooling |
| Backup | External/cloud backup for practice artifacts | Protects source material, docs, repos, and client work | Keep simple and auditable |
| Templates | Proposal, SOW, COI, intake, roadmap, runbook, and handoff templates | Compounds every engagement | Mostly time investment, not cash |
| AI/dev tools | Current tools that are actively used | Helps ship work now | Keep only tools that show daily/weekly utility |
| Domain/site/runtime basics | Existing public site, Vercel/Supabase/Hub basics | Keeps front door and demos professional | Avoid expanding until workflow proves need |
| Documentation cockpit | DTP/Practice OS surfaces | Makes the practice more repeatable | Continue improving in small increments |

## Buy Soon If Revenue Or Friction Justifies It

These are worthwhile after they solve a repeated pain or the practice earns the
right to carry them.

| Category | Investment | Trigger | Why |
|---|---|---|---|
| Main machine | Mac with at least 64GB RAM and 2TB storage | Current machine materially slows client delivery, agent workflows, local dev, or video/research multitasking | Good purchase when it removes real work friction, not as a confidence prop |
| Monitor/dock setup | Larger display, dock, webcam, mic, lighting | Client calls, screen sharing, design review, and agent orchestration feel cramped or unprofessional | Improves delivery polish and endurance |
| Recorded handoff | Screen recording/walkthrough tooling | Repeat clients need explanations, runbooks, and transfer | Directly improves handoff quality |
| Design/diagram tools | Figma/Canva/diagramming stack | Visual explanation becomes a recurring differentiator | Useful for Blueprint, architecture, and client education |
| Observability | Sentry/PostHog/logging baseline for client demos | Demos or live client systems need support confidence | Do not add to static/mock work by default |
| Secure file exchange | Client-safe upload/storage path | Clients need to share private files | Needs data policy before broad use |

## Wait

These may become valuable, but only after repeated work proves the need.

| Category | Investment | Wait for | Reason |
|---|---|---|---|
| Client portal | Dedicated client command room or portal | Multiple clients need recurring visibility and self-serve status | Do not turn every engagement into a portal |
| Reusable cloud template | Standard Vercel/Supabase/Azure deployment baseline | Three or more similar builds repeat | Build after pattern is real |
| Automation server | Dedicated scheduled automation/runtime host | Repeated cron/workflow support work | Hub/runtime layer may already cover enough |
| CRM | Simple CRM beyond current notes/intake | More active prospects than Toni can track manually | Avoid admin drag too early |
| Accounting/invoicing upgrades | Paid bookkeeping stack | Revenue and tax complexity justify it | Keep clean but lightweight first |
| Insurance/legal templates | Professional review or policy | Paid client work creates exposure | Important later, not a reason to stall learning |
| Hosted DTP/private platform | Web app around Practice OS | Manual artifacts become too slow or too valuable to leave local-only | Do not build because it is interesting |

## Avoid For Now

Avoid these unless a specific, paying client or repeated pattern changes the
math.

| Investment | Why to avoid |
|---|---|
| Universal Glean alternative | Too product-heavy, too security-heavy, and not the consulting lane |
| Multi-tenant SaaS for Business Memory OS | Premature before diagnostic demand is proven |
| Enterprise project-management stack | Adds overhead and cosplay before client volume requires it |
| Random automation subscriptions | They create maintenance without improving delivery judgment |
| Expensive cloud architecture for demos | Static/local/private prototypes are enough until a client needs live runtime |
| Overbuilt internal dashboards | DTP docs and simple command rooms are enough until repeated pain appears |
| Tools bought for legitimacy | The practice becomes real by delivering useful work, not by buying more software |

## Business Memory OS Investment Implication

Business Memory OS should begin as an internal consulting lens and diagnostic,
not a product platform.

Near-term investment should be mostly artifact work:

- diagnostic worksheet;
- 25-question inventory;
- source-of-truth map;
- AI safety/action classification;
- first workflow recommendation;
- runbook and handoff format.

Only after several diagnostics show repeated demand should Toni consider:

- reusable assistant scaffold;
- secure source ingestion pattern;
- client dashboard;
- hosted Business Memory workspace;
- paid monthly support package.

## Claude Agent SDK Credit

Toni received an Anthropic notice that Max 5x subscribers can claim a monthly
`$100` credit for Claude Agent SDK and `claude -p` programmatic usage starting
June 15.

Decision:

- Treat this as helpful experimentation budget.
- Do not treat it as practice infrastructure.
- Use it for bounded agent/CLI experiments, not client-critical systems, until
  the terms, claim flow, usage limits, and billing behavior are confirmed.

Good uses:

- prototype agent workflows;
- test command-line coding/research routines;
- compare `claude -p` against existing Codex/Claude workflows;
- evaluate where programmatic agent usage actually improves delivery.

Bad uses:

- assuming free credit will cover client production usage;
- adding a dependency to client delivery before billing controls are clear;
- buying more tooling because the credit exists.

## Decision Ladder

Before buying anything, ask:

1. Does this remove a real bottleneck in current delivery?
2. Does this make client work safer, clearer, faster, or easier to hand off?
3. Does this create a reusable asset?
4. Would I still buy it if no one saw it?
5. Can the practice support the recurring cost?
6. Is there a cheaper/manual version that proves the need first?

If the answer is mostly no, wait.

## Next Actions

1. Review the first Business Memory OS diagnostic fixture:
   `practice-os/fixtures/consulting-intelligence/northline-business-memory-os-diagnostic.md`.
2. Run a second diagnostic against Omnexus or another known business after the
   shape is clean.
3. Track actual friction for 30 days before buying hardware.
4. Keep cloud investments tied to real client/demo needs.
5. Revisit this roadmap after the next paid engagement or after the first full
   Business Memory diagnostic test.
