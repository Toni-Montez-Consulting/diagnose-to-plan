---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
agent_role: software-architecture
---

# Software Architecture Source Policy Pilot - 2026-05-10

Status: internal Software Architecture pilot

Owner repo: `diagnose-to-plan`

## Purpose

This pilot tests how the Software Architecture Agent should use DTP, repo,
platform, and web evidence when shaping technical decisions for Toni's
workspace.

The strategic question:

> How should architecture guidance stay ambitious and useful without turning
> source research into accidental runtime authority?

## Source Packet

Internal sources:

- `practice-os/agents/software-architecture.md`
- `practice-os/templates/architecture-review-packet.md`
- `practice-os/templates/automation-authority-matrix.md`
- `docs/PRACTICE_ARCHITECTURE_REVIEW_PACKET_2026-05.md`
- `docs/PRACTICE_SYSTEM_ARCHITECTURE.md`
- `docs/PRACTICE_SYSTEM_FUTURE_STATE.md`
- `docs/AGENT_SOURCE_REGISTRY_AND_WEB_EVIDENCE_POLICY_V0.md`
- `practice-os/research/source-packs/agent-source-packs.v0.json`

External official sources reviewed as architecture context:

- Microsoft Azure Well-Architected Framework:
  `https://learn.microsoft.com/en-us/azure/well-architected/`
- AWS Well-Architected Framework:
  `https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html`
- Google Cloud Well-Architected Framework:
  `https://cloud.google.com/architecture/framework`
- Supabase Row Level Security docs:
  `https://supabase.com/docs/guides/database/postgres/row-level-security`
- Vercel production checklist:
  `https://vercel.com/docs/production-checklist`

Evidence boundary:

- Internal DTP and repo evidence decides ownership, gates, and current system
  truth.
- Official platform docs can clarify current platform behavior, architecture
  lenses, and verification expectations.
- External frameworks do not prove DTP should adopt a platform, add runtime,
  change schema, or expand autonomy.
- Broad web search can find source candidates and examples, but it cannot be
  used as architecture authority.

## Architecture Decision

The Software Architecture Agent should be boundary-first and implementation
ready.

Every architecture pass should produce a concrete decision surface:

- the system boundary being changed;
- the source of truth;
- the runtime authority being introduced or avoided;
- the interfaces, schemas, routes, jobs, repos, or tools affected;
- the failure modes and verification gates;
- the smallest useful implementation path;
- the approval required before implementation.

Architecture should not become abstract strategy. It should make the next code,
ops, product, or client decision safer and easier to execute.

## Source Posture

Default posture:

1. Start with repo state, DTP docs, local instructions, tests, manifests,
   existing contracts, and Toni's latest direction.
2. Use official docs for platform-specific behavior, limits, security posture,
   and current verification expectations.
3. Use cloud well-architected frameworks as review lenses, not as a mandate to
   make the system cloudier or more complex.
4. Use Supabase/Postgres, Vercel, Azure, AWS, Google Cloud, OpenAI, Stripe, or
   other vendor docs only when that platform is actually in scope.
5. Use broad search only to discover better sources, compare patterns, or find
   examples. Corroborate before turning it into a durable decision.
6. State evidence limits whenever a source could influence architecture.

## Operating Rules

### 1. Source Of Truth Before Shape

Before proposing architecture, identify which layer owns the truth.

Examples:

- DTP owns practice decisions, gates, records, and private operating memory.
- Consulting owns public storefront rendering and approved public copy.
- Hub owns runtime intake storage and runtime support.
- Project repos own their own product implementation.
- Notion is a mirror/cockpit unless a future decision changes that.

If source-of-truth ownership is unclear, the output should be a boundary memo,
not an implementation plan.

### 2. Runtime Authority Is A Gate

Any recommendation that introduces new runtime authority must stop at review.

Runtime authority includes:

- hosted services;
- write-enabled jobs;
- scheduled workflows;
- database migrations;
- webhooks;
- external API actions;
- production config;
- client-facing automation;
- autonomous agent behavior.

The architecture role can describe the path, required evidence, and rollback
conditions. It cannot approve the mutation by itself.

### 3. Official Docs For Current Platform Behavior

When a decision depends on a platform behavior, use official docs first.

Examples:

- Use Supabase docs for RLS, policies, auth, migrations, and service-role
  boundaries.
- Use Vercel docs for production checklist, deployment behavior, performance,
  security headers, observability, and rollback expectations.
- Use Azure, AWS, and Google Cloud architecture docs as cloud review lenses
  only when a cloud path is in scope.

### 4. Smallest Useful Architecture

Architecture should preserve ambition while avoiding premature complexity.

The default recommendation should answer:

- what is the smallest useful structure that keeps the future option open?
- what should remain manual, markdown, draft-only, or local for now?
- what would justify moving up the autonomy or runtime ladder later?

### 5. Handoff To Other Roles

Architecture should call in other roles when their boundary is reached:

- Software Engineering for implementation feasibility and code.
- DevOps / Infrastructure for deployment, observability, secrets, rollback, and
  runtime operations.
- Data Architecture for schema, RLS, retention, and privacy/data flow.
- QA / Audit for go/no-go evidence and regression risk.
- Product Strategy for whether the architecture supports the actual user or
  business outcome.
- Consulting Strategy for whether technical complexity is worth the business
  value.

## Default Outputs

Good Software Architecture outputs:

- architecture review packet;
- system boundary memo;
- ADR-style decision record;
- integration plan;
- runtime authority matrix update;
- data-flow note;
- implementation-ready architecture brief;
- risk and verification checklist.

Bad Software Architecture outputs:

- broad diagrams with no owner, gate, or next action;
- framework adoption without current need;
- cloud migration by vibes;
- schema or runtime changes presented as already approved;
- AI-agent autonomy language without an autonomy review;
- "best practice" claims without repo fit and evidence limits.

## Approval Gates

Require Toni approval before architecture becomes implementation when it touches:

- new runtime behavior;
- schema or migration changes;
- production data;
- secrets or credentials;
- OAuth/auth/payment/entitlement behavior;
- cross-repo orchestration;
- scheduled or autonomous workflow;
- public/client-facing architecture claims;
- live cloud, DNS, billing, deployment, or database changes.

## Source-Pack Implication

The role behavior is concrete enough for the source pack.

Recommended source-pack fields:

- internal role spec;
- architecture review packet;
- automation authority matrix;
- DTP architecture source docs;
- official platform docs as contextual sources;
- blocked broad-web and runtime-authority actions;
- default outputs;
- next review trigger.

## Next Review Trigger

Reopen this pilot when:

- a real architecture review changes a runtime boundary;
- hosted DTP moves from docs into implementation;
- Hub receives a schema/runtime change;
- source-pack schema validation is added;
- the Software Engineering, DevOps, Data Architecture, or QA role pilots
  depend on this architecture source posture.
