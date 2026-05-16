---
created: '2026-05-15T00:00:00Z'
data_class: P1
confidential: false
permission_level: internal_only
review_status: draft
source: Toni pasted self-sent email because Gmail connector auth was blocked
---

# Business Memory OS And Practice Cockpit Capture

This is an internal strategy capture from Toni's self-sent memo on Glean,
business memory, and long-term consulting-practice infrastructure.

It is not public copy, a buying plan, final pricing, or an instruction to build
a Glean competitor.

## Source Summary

Toni had a lunch conversation about Glean that clarified a broader business
software pattern: companies increasingly need an internal intelligence layer
that helps people find, understand, and eventually act on company knowledge
across tools, documents, conversations, workflows, and permissions.

The useful takeaway for Toni's practice is not to copy Glean. The useful
takeaway is to translate the pattern down to small businesses: help owners
clean up business knowledge, decide what should be searchable or automated,
build one useful assistant/workflow around the highest-value pain point, and
hand it off clearly.

The same memo also raised a second question: if Toni eventually had money to
invest in the practice, what would actually make the practice more capable
instead of merely making it feel more real?

## Strategic Read

This is a strong lane if it stays inside the consulting model.

The shape fits Toni's existing builder-led practice because it is not "AI tool
installation." It is diagnosis, source-of-truth cleanup, practical workflow
design, implementation, runbook, and handoff.

The risk is overbuilding. The move becomes distracting if it turns into:

- a universal enterprise search product;
- a multi-tenant SaaS platform;
- a generic chatbot offer;
- a vague "AI transformation" pitch;
- a buying spree for tools before client revenue justifies them.

The disciplined version is:

> Use Glean as proof of the pattern. Do not copy the company. Mirror the shape
> at small-business scale. Sell judgment, cleanup, sequencing, assistant,
> workflow, and handoff.

## Working Positioning

Keep public language plain:

> Most small businesses do not need another AI tool. They need their business
> knowledge cleaned up, connected to the right places, and turned into
> something the owner and team can actually use.

Possible internal/public offer names:

- Business Memory OS.
- Business Knowledge Layer.
- Internal Search & Assistant Audit.
- Owner's Command Center.
- Business Memory Assistant.

Current strongest name: **Business Memory OS**.

## Offer Ladder Hypothesis

### Knowledge Layer Audit

Potential price: `$500-$1,500`.

Use when an owner feels like everything is everywhere.

Outputs:

- knowledge map;
- source-of-truth findings;
- trusted vs stale source classification;
- recurring questions from customers, employees, vendors, and owner;
- safe/not-safe for AI answer classification;
- first three assistant/workflow opportunities.

### Business Memory Assistant

Potential price: `$1,500-$4,000` plus `$150-$500/month`.

Use for one assistant around one business function.

Examples:

- owner FAQ assistant;
- client onboarding assistant;
- sales follow-up assistant;
- SOP assistant;
- donor operations assistant for nonprofits;
- service business intake assistant;
- proposal or estimate assistant.

### Business Memory OS

Potential price: `$5,000-$15,000` plus `$750-$2,500/month`.

Use for a fuller operating-system engagement:

- source cleanup;
- connected tools;
- assistant;
- automations;
- weekly owner summary;
- runbook;
- handoff;
- monthly support.

## Diagnostic Experiment

Run this against one known business, Omnexus, or a fictional local service
business:

> List the 25 questions this business owner, employee, customer, or vendor
> might ask every month. For each question, identify where the answer currently
> lives, who owns it, how often it changes, whether it is safe for AI to answer,
> and what action should happen after the answer is found.

Classify each question as:

1. Search only: find the answer.
2. Draft only: help write the response.
3. Workflow: take the next step.
4. Do not automate: human judgment required.

This diagnostic can become the first artifact before any software build.

## Practice Cockpit Question

The memo also asks what the right operating cockpit looks like for a serious,
small, high-quality solo AI consulting practice.

This should be treated as a phased infrastructure roadmap, not a gadget list.

### Phase 1: Clean And Safe Essentials

Invest only where it reduces friction, improves boundaries, or protects work:

- separate business email and accounts where appropriate;
- password manager and hardware security keys;
- clean client folder/repo/data boundaries;
- backups;
- no employer/client confidential crossover;
- baseline proposal/SOW/intake templates;
- reusable client context, decision log, runbook, and handoff templates.

### Phase 2: Delivery Speed And Quality

Invest when it improves actual delivery:

- better main machine if local development and agent workflows are materially
  constrained;
- AI/dev subscriptions that are actively used in client delivery;
- testing, docs, diagramming, and design tools;
- recorded walkthrough and handoff tooling;
- reusable build spec, audit, roadmap, and runbook formats.

### Phase 3: Cloud And Client Infrastructure

Invest when there is a repeating delivery pattern:

- reusable staging/production deployment template;
- client demo environments;
- logging/observability baseline;
- secure file storage;
- Supabase/Vercel/Azure templates;
- client-specific sandboxes;
- backup and recovery pattern;
- lightweight internal command room.

### Phase 4: Optional Upgrades After Revenue

Delay until revenue proves need:

- expensive hardware beyond the main bottleneck;
- enterprise project-management tooling;
- broad multi-tenant SaaS infrastructure;
- custom platform work before the offer has repeatable demand;
- tools bought mainly to make the practice feel more legitimate.

## Claude Credit Note

Toni also pasted an Anthropic notice saying Max 5x subscribers can claim a
monthly `$100` credit for Claude Agent SDK and `claude -p` programmatic usage
starting June 15.

Treat this as a possible tooling budget input, not a planning dependency, until
the claim flow and terms are available.

## Near-Term Recommendation

Do not buy the full cockpit yet.

Near term, turn the memo into:

1. a Business Memory OS diagnostic worksheet;
2. a one-page internal offer hypothesis;
3. a phased practice investment roadmap;
4. one test run against a real or fictional small business.

Current first test fixture:

- `practice-os/fixtures/consulting-intelligence/northline-business-memory-os-diagnostic.md`

The buying principle:

> Do not spend money to feel like the practice is real. Spend money only where
> it makes the practice more capable.

## Open Questions For Toni

1. Decision: Business Memory OS should stay as an internal lens now, with the
   option to become a named offer later after diagnostics prove demand.
2. Recommendation: run the first diagnostic on a fictional/local service
   business, then a second pass on Omnexus or another known business. The first
   fictional pass now uses Northline Performance Studio.
3. Decision: create a hard buy-now / wait / avoid investment roadmap for the
   practice cockpit.

## Next Artifact Candidates

- `business-memory-os-diagnostic.md`
- `business-memory-os-offer-hypothesis.md`
- `docs/PRACTICE_INVESTMENT_ROADMAP_2026.md`
- `practice-cockpit-baseline.md`
