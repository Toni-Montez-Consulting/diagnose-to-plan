---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Recovery Closeout Prompt Specs

Status: reusable DTP prompt/spec pack.

Purpose: preserve the recovered prompt patterns from the 2026-05-05 chat
recovery work without turning raw chat transcripts into source-of-truth docs.

Use these specs when Toni asks for broad roadmap synthesis, prompt recovery,
buildspec review, repo audit, handoff, or public assistant QA planning.

## Shared Rules

- Ground in current repo files and git state before summarizing.
- Treat Codex, Copilot, Claude, or memory summaries as leads, not proof.
- Count only files, diffs, commits, tests, scripts, docs, routes, or concrete
  repo state as implementation evidence.
- Keep DTP, consulting, Hub, `tm-skills`, DSE, and sibling repos in their own
  ownership lanes.
- Summarize sensitive/private material; do not paste raw transcripts, secrets,
  client records, account data, personal trip details, or Microsoft-confidential
  material.
- End each recovered idea as one of: canonical doc, backlog item, reusable
  prompt/spec, future-phase parking, archive/discard, or Toni decision.

## Roadmap Synthesis Prompt

Use when Toni asks what else belongs on the roadmap based on prior conversations
or workspace history.

Required output:

- Current source docs checked.
- Existing active backlog items that should not be duplicated.
- New or materially evolved candidates only.
- Owning repo/lane for each candidate.
- Proof, privacy, COI, validation, or no-touch gate.
- Recommendation: now, next, later, hold, or discard.

Do not invent goals from agent suggestions. Preserve ambition, but require
evidence before promotion.

## Prompt-To-Implementation Audit Prompt

Use when Toni is worried that a chat idea was never implemented or promoted.

Required output:

- Chat/session access findings.
- Prompt-like artifacts found.
- Recovered prompts/plans/responses.
- Prompt-to-implementation comparison.
- Dirty repo explanation.
- Lost/floating ideas.
- Items to promote, backlog, save as prompts/specs, park, or archive.

Required status discipline:

- Do not count an assistant response as implementation.
- Do not count an uncommitted diff as stable.
- Do not treat documented ideas as implemented.
- Name when chat history is inaccessible or practically unreadable.

## Buildspec Review Prompt

Use when Toni drops a buildspec, extracted spec, rough plan, or chat-generated
implementation idea and asks how to make it more potent.

Required output:

- What the spec is trying to make true.
- Missing audience, owner, source, validation, data, proof, and handoff
  boundaries.
- The smallest execution-ready version.
- The ambitious version, if useful.
- What should become a doc, prompt, script, test, template, backlog item, or
  future-phase parking item.

Do not start implementation until the target repo and validation gate are clear.

## Repo Audit / Review Prompt

Use when Toni asks for a codebase audit, cleanup pass, launch-readiness review,
or reliability review.

Required output:

- Actual current repo state, not memory.
- Findings ordered by severity.
- Missing tests, validation, docs, or ownership boundaries.
- P0/P1 actions separated from later polish.
- Concrete validation gates before stable.

If the task spans repos, keep each repo's findings and commits separate.

## Handoff Prompt

Use when work is ending, moving to another chat, or needs a clean checkpoint.

Required output:

- Repo, branch, commit status, and dirty state.
- Changed files by purpose.
- Validation commands run and results.
- What is stable, what is uncommitted, what is parked, and what needs Toni.
- Exact next action and owning repo.

Do not say "done" if validation, commit, push, or manual owner gates remain.

## Public Assistant QA Prompt

Use before any public assistant widget, endpoint, private retrieval, vector
index, admin helper, or assistant runtime.

Required output:

- Approved public source corpus.
- Blocked private sources.
- Refusal fixtures and unsafe-answer examples.
- Human handoff route.
- Logging/analytics privacy boundary.
- No-widget QA gate and route smoke gate.

Runtime implementation stays blocked until the consulting-specific QA checklist
and source/refusal fixtures pass.
