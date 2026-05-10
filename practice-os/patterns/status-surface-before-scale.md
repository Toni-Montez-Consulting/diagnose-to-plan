---
data_class: P1
confidential: false
permission_level: internal_only
review_status: reviewed
---

# Pattern: Status Surface Before Scale

## Signal

Ideas, research signals, client follow-ups, agent behaviors, or operating
improvements get captured once but do not reliably become reviewed decisions,
usable artifacts, or intentionally parked work.

The operator starts feeling the system is "lightweight" in the bad way: fast to
capture, but too easy to lose.

## Real Constraint

Capture is not the same as operating memory.

A system can have plenty of notes, templates, dashboards, records, and agent
outputs and still fail if no one can quickly answer:

- What exists?
- What state is it in?
- What is waiting?
- What needs review?
- What was intentionally parked?
- What would make this worth building more ambitiously?
- What is the next artifact or stop condition?

## Non-AI Fix First

Create a small visible status surface before expanding the system.

The surface does not need to be fancy. It needs to show:

- item name;
- current state;
- owner or review lens;
- source path;
- next action;
- boundary or approval gate;
- review trigger;
- close, park, supersede, or promotion condition.

## Intervention

Use a status surface before scaling the workflow into a larger dashboard,
Notion cockpit, hosted app, agent role, automation, public copy, or client
system.

Good first surfaces:

- a markdown ledger;
- a generated static dashboard;
- a CLI status view;
- a steward receipt;
- a reviewed task ledger;
- a small owner-facing checklist;
- a sanitized Notion mirror only after source-of-truth rules are clear.

## Where This Applies First

Use this pattern inside DTP and Practice OS before broad rollout:

- Practice Evolution records;
- Research Arm digests and pattern candidates;
- Opportunity OS records;
- Memory Steward reviews;
- Research Steward reviews;
- client-operating-kit receipts;
- workspace task ledgers;
- future agent/squad role pilots.

Expand to other repos only after the DTP pattern proves useful in one more real
review cycle.

## Client-Explainable Version

High-level client-safe framing:

> Before we add more tools, dashboards, or automation, we need a simple way to
> see what exists, what state it is in, what needs a decision, and what happens
> next. That visibility is what keeps good ideas and follow-ups from getting
> lost.

Do not expose internal DTP mechanics, private client examples, agent prompts,
or proof metrics unless they pass the normal proof and redaction gates.

## Eval

Primary:

- A future session can identify the current queue, next action, and boundary
  without rereading chat.

Secondary:

- fewer stale drafts;
- fewer rediscovered ideas with no source path;
- clearer promotion/parking decisions;
- less pressure to build a larger system before the workflow earns it.

## When Not To Use This

Do not build a status surface when:

- there is only a one-off task with no reuse value;
- the item is not worth tracking after the current session;
- the surface would expose private/client-sensitive material in the wrong repo;
- a checklist or direct action would resolve the issue faster.

## Current Evidence

- Toni repeatedly asked that valuable ideas and meta-patterns not disappear
  after a lightweight capture.
- Practice Evolution gained a generated dashboard so captured records can be
  inspected by state.
- Memory Steward and Research Steward became read-only recommendation surfaces
  before any autonomous memory or research behavior.
- The first Research Steward pass became clearer after accepted digests stopped
  appearing in the active attention queue.

## Source Candidate

Promoted from:

`practice-os/research/pattern-candidates/2026-05-10-status-visibility-prevents-lightweight-capture-drift.md`
