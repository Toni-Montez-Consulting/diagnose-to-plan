---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Status Surface Before Scale Promotion - 2026-05-10

## Trigger

Research Steward surfaced the draft pattern candidate
`practice-os/research/pattern-candidates/2026-05-10-status-visibility-prevents-lightweight-capture-drift.md`.

Toni approved promoting it as an internal operating rule with these constraints:

- use a more operational, less phrase-y name;
- start in DTP/Practice OS, then expand after more refinement;
- keep it eventually explainable to clients at a high level without exposing
  internal mechanics or "secret sauce."

## Decision

Promote the candidate to:

`practice-os/patterns/status-surface-before-scale.md`

Pattern name:

**Status Surface Before Scale**

## Why This Pattern Matters

This pattern names the operating risk Toni has been calling out:

lightweight capture is useful, but it becomes frustrating if the system never
returns to build on it, review it, promote it, or park it intentionally.

The fix is not "build a giant system immediately." The fix is to make state,
next action, boundary, and review trigger visible before scaling.

## Current Scope

Active now:

- DTP;
- Practice OS;
- Practice Evolution;
- Research Arm;
- Memory Steward;
- Research Steward.

Candidate later:

- Opportunity OS;
- client-operating-kit receipts;
- workspace dashboard / cockpit views;
- consulting offer explanations;
- client-facing systems where owners need clear follow-through.

## Public / Client Boundary

Allowed internally:

- use the pattern to decide when a workflow needs a status surface;
- use it to prevent ideas and research signals from becoming stale invisible
  drafts;
- use it as a review lens before scaling dashboards, Notion mirrors, hosted
  systems, or automation.

Not allowed without review:

- public site copy;
- client proof claims;
- private client examples;
- productivity or revenue claims;
- exposing DTP internals or agent prompts.

## Client-Explainable Seed

Future high-level explanation:

> Before we add more tools, dashboards, or automation, we need a simple way to
> see what exists, what state it is in, what needs a decision, and what happens
> next. That visibility is what keeps good ideas and follow-ups from getting
> lost.

This is a seed only. It is not approved public copy.

## Verification

Run after promotion:

```powershell
.\.venv\Scripts\dtp.exe research steward --limit 8
.\.venv\Scripts\python.exe -m pytest tests\test_research.py tests\test_cli.py
.\.venv\Scripts\python.exe -m ruff check src tests
.\.venv\Scripts\dtp.exe practice doctor
git diff --check
```
