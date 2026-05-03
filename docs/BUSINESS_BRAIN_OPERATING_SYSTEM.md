---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Business Brain / Consulting OS

This document normalizes the Business Brain work into DTP's real repo
structure. It captures the rebuilt source docs, Claude planning context, and
the decisions needed for future agents to continue without recreating this chat.

## Purpose

The Business Brain is a repo-centered operating system for Toni's solo
consulting practice. It should help the practice understand and operate across
business domains: operations, admin, finance, accounting, reporting, metrics,
pricing, valuation, legal/compliance issue spotting, managerial judgment,
client handoff, and support rhythms.

It is also the reusable pattern for client operating systems. The system Toni
builds for himself should improve the systems he installs for operators, and
lessons from those installs should flow back only after review and redaction.

## Source Packet

The current source packet is:

- `ETHOS_REBUILT.md`: voice, worldview, proof-point posture, audience guidance,
  public/private destination gates, anti-generic-AI-copy rules, and comms
  artifact shapes.
- `BUILD_SPEC_REBUILT.md`: system behavior, command contracts, Business Brain
  primitives, initial agent roles, eval/refactor rules, Notion mirror rules, and
  build sequence.
- `prep_2026-05-01_REBUILT.md`: live work order and first regression seeds for
  Greg, Cameron, and Mom/Mario.
- `REVIEW_MEMO.md`: migration checklist for path drift, Notion source-of-truth
  ambiguity, operator-handoff duplication, public/private proof gates, and
  command contract completeness.
- Claude planning context from 2026-05-01: the broader ambition to make the
  workspace understand business practice as deeply as software delivery, with
  self-improving human-gated skills, agents, runbooks, and comms.

If original versions exist elsewhere, use the rebuilt versions as the current
working packet unless live repo state proves a conflict with accepted decisions.

## Source Of Truth Order

1. Live DTP repo state and accepted implementation patterns.
2. Toni's latest direct instruction.
3. Current DTP compliance/source-of-truth files.
4. Canonical operating methodology and roadmap docs.
5. `ETHOS_REBUILT.md`.
6. `BUILD_SPEC_REBUILT.md`.
7. `prep_2026-05-01_REBUILT.md`.
8. `REVIEW_MEMO.md` as integration QA.

Stop and ask before changing compliance, public copy, contract terms, client
data handling, or directory duplication. Resolve naming/path drift from the repo
when safe.

## Repo Mapping Decisions

- DTP is the Business Brain home.
- `practice-os/` is the durable reusable asset root. Do not create a parallel
  `practice/` root from Claude's conceptual examples.
- Existing Practice OS skills are upgraded in place: `diagnose`, `coi-screen`,
  `proposal-draft`, and `handoff-runbook`.
- Command contracts live in `practice-os/commands/`.
- First fixtures live in `practice-os/fixtures/business-brain/`.
- Agent role specs live in `practice-os/agents/`.
- Reusable comms drafts live in `practice-os/comms/`.
- Live/private engagement records stay in ignored `engagements/` or a private
  vault.

## Operating Thesis

The operator is the unit. The goal is not to sell AI or build a platform. The
goal is to help real operators decide what is worth doing, build or install the
right system in the right order, and leave with a handoff they can operate.

The Business Brain should improve through:

- real client and prospect artifacts;
- lessons captured after meetings, builds, handoffs, and close rituals;
- fixtures and evals derived from actual misses;
- agent-proposed refactors that humans approve;
- public proof only after permission, redaction, evidence, caveat, and review.

The Business Brain should not depend on chat memory alone. Use
`docs/PRACTICE_MEMORY_CONTROL_PLANE.md` and
`practice-os/templates/memory-control-checkpoint.md` when a new idea,
connector, client status sweep, or infrastructure decision needs to become
durable operating state.

## Initial Proof Threads

- Greg / TheGrantApp.io tests founder/product feedback, case-study engagement
  shape, marketing/onboarding/match-explanation UX, and the boundary that Toni
  should not own the matching algorithm.
- Cameron / M&A platform tests Builder-path boundaries, equity decline,
  diligence, and COI discipline before any contracting.
- Mom/Mario tests the operator-handoff pattern for a non-technical admin running
  a real small-business admin system.

The Mom nonprofit / CCAAP stream remains separate and should not be folded into
this slice except through existing roadmap boundaries.

## Communication Rules

Human-facing artifacts must classify destination first:

- private conversation;
- internal/private network;
- client-facing draft;
- public internet.

Private drafts can mention Mario, Mom, Greg, Cameron, and Omnexus when useful,
but public use remains gated. Avoid implying employer endorsement. AI adoption
statistics from planning context are research candidates, not public claims.

## Forbidden Until Unlocked

- Multi-tenant SaaS.
- Agent auto-merge or self-rewriting skills.
- Auto-send client or prospect communication.
- Auto-published public proof.
- Public storefront services/pricing changes.
- Courses, cohorts, accelerators, or info products.
- Notion as source of truth.
- QuickBooks/n8n/business integrations as live dependencies before credentials,
  tools, and source-of-truth rules are confirmed.
- QuickBooks write behavior, tax/accounting advice, or live financial imports
  before a read-only connector gate is accepted.

## First Slice

The first implementation slice is:

1. Commit this source map, agent guidance, and kickoff receipts.
2. Add command contracts for `/diagnose-prospect`, `/coi-screen`,
   `/draft-proposal`, and comms generation.
3. Upgrade the existing Practice OS skills.
4. Add Controller, General Counsel, and COO as draft-producing role specs.
5. Create fixtures for Greg, Cameron, and Mom/Mario.
6. Produce a private-first comms kit.
7. Update roadmap/backlog/documentation map.
8. Run DTP validation and record any gaps.
