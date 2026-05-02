# Agent Instructions

Read `CLAUDE.md`. It is the canonical instruction file for this repo.

## Practice OS Build Appendage

This appendage is additive guidance for the DTP / Practice OS product direction.
It does not remove the requirement to read `CLAUDE.md`.

## Project purpose

This repository is for building Practice OS, an internal operating system for a
solo AI/software implementation consulting practice.

Practice OS turns messy business context into working systems.

The core workflow is:

Raw input
-> clarifying questions
-> assumptions
-> context pack
-> workflow map
-> opportunity score
-> implementation spec
-> build tasks
-> exception register
-> runbook
-> value ledger
-> memory review
-> reprioritized backlog.

## Source of truth

Read these files before making product or implementation decisions:

1. `docs/source/practice_os_build_spec_v0_1.md`
2. `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md`
3. `database/schema/practice_os_schema_v0_1.sql`
4. Existing repo files, infrastructure, docs, migrations, and prior decisions

If there is a conflict, prioritize:

1. Current `AGENTS.md`
2. Existing working repo architecture
3. ADRs / decision records
4. `docs/source/practice_os_build_spec_v0_1.md`
5. `database/schema/practice_os_schema_v0_1.sql`
6. `docs/source/ai_implementation_layer_thesis_and_build_spec_v0_1.md`

Do not silently resolve meaningful conflicts. Add them to
`docs/integration/conflict_register.md`.

## Integration rule

New thesis/spec documents are additive source material. They should not
overwrite existing infrastructure decisions unless there is a clear reason.

Before implementing from new source material:

1. Inspect the existing repo.
2. Identify current architecture, schema, modules, conventions, and prior
   decisions.
3. Read the new source material.
4. Produce or update an Integration Map.
5. Identify reinforcements, conflicts, ambiguities, and gaps.
6. Preserve existing infrastructure unless a change is clearly justified.
7. Prefer additive changes first.
8. Implement only the next scoped slice.
9. Update decision logs, backlog, and reprioritization notes after
   implementation.

## Source preservation rule

Do not rewrite or dilute source thesis documents unless explicitly asked.

The source documents preserve strategic thinking and should retain their
nuance.

When converting source material into product requirements, summarize it in
integration docs, ADRs, implementation specs, or backlog items rather than
editing the source directly.

## Product philosophy

Do not build a flashy SaaS dashboard.

Build an operator console.

The system should be simple, fast, structured, and practical.

The product is not generic AI consulting software. It is an implementation
system for turning business context into working systems.

Preserve these strategic concepts:

- AI/software implementation layer
- businesses without a software team
- high-resolution input
- Input Studio
- clarifying questions that increase resolution without blocking
- assumptions
- context packs
- anti-slop review
- human-approved memory
- business-to-code translation
- workflow mapping
- opportunity scoring
- implementation specs
- exception/debug register
- value ledger
- runbooks
- repeatable iterative operating system
- user intent remains primary
- pushback is proportional and only blocking for real risk

## Memory rule

Do not build uncontrolled self-learning.

The system may capture raw input broadly, but durable memory must be explicitly
approved before becoming reusable playbook memory.

Use these memory levels:

1. Raw capture
2. Working memory
3. Decision memory
4. Pattern memory
5. Playbook memory

## Clarifying question behavior

Clarifying questions should increase resolution, not create friction.

Most questions are non-blocking. If the answer is missing, make a labeled
assumption and continue.

Blocking questions are only for:

- safety
- legal risk
- privacy risk
- security risk
- compliance risk
- money movement
- irreversible actions
- technical impossibility
- conflict-of-interest risk

Never ask more than three non-blocking questions before producing something
useful.

## User intent rule

The user's stated intent is primary.

The system may clarify, improve, suggest tradeoffs, and flag risk, but it
should not override the user's direction unless there is a real safety, legal,
privacy, security, compliance, money-movement, irreversible-action, technical,
or conflict-of-interest issue.

## Reprioritization rule

Everything important should be captured.

Priorities should be updated deliberately after meaningful events, not randomly.

Meaningful events include:

- new source document
- completed implementation slice
- major bug or exception
- client feedback
- new constraint
- strategy change
- architecture decision

After each meaningful change, update
`docs/integration/reprioritization_log.md`.

## MVP scope

Build the internal Practice OS first.

Do not build a client-facing portal yet.

Do not build autonomous agents yet.

Do not build unmanaged self-learning.

Do not overbuild analytics before the core workflow exists.

MVP modules:

1. Thought Inbox / Raw Input Capture
2. Input Studio
3. Clarifying Question Layer
4. Assumptions
5. Client Records
6. Workflow Maps
7. Opportunity Scoring
8. Implementation Specs
9. Build Tasks
10. Exception Register
11. Value Ledger
12. Decision Logs
13. Runbooks
14. Memory Review Queue
15. Template Library

## Implementation posture

Preserve existing infrastructure.

Do not delete, rename, or restructure existing architecture without explaining
why.

Prefer scoped, additive, reviewable changes.

Before coding, restate:

1. Scope
2. Non-goals
3. Files likely to change
4. Acceptance criteria

After coding, summarize:

1. What changed
2. What source ideas were preserved
3. What repo decisions were preserved
4. What remains open
5. What should happen next
