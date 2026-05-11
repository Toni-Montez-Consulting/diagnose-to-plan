---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice Operating Review Loop V0

Status: internal operating cadence for turning Practice OS signals into
decisions, next actions, and receipts.

Owner repo: `diagnose-to-plan`

## Purpose

The Practice OS now captures ideas, meta-patterns, research signals, memory
promotion candidates, agent-role gaps, KB events, status surfaces, and autonomy
candidates. The next risk is not lack of capture. The next risk is capture
without return.

This loop exists so useful signals get reviewed, promoted, parked, rejected, or
turned into work at a predictable cadence.

Core rule:

> Capture broadly, then review deliberately on a rhythm.

## Default Cadence

Use two levels:

| Cadence | When | Target Duration | Purpose |
|---|---|---:|---|
| Daily light check | when Toni is actively working the practice that day | 5-10 minutes | see `now`, `next`, obvious blockers, and fresh signals |
| Weekly operating review | once per week or before a major practice push | 30-45 minutes | decide what gets promoted, parked, built, or scheduled |

Do not let the daily check become a second planning job. It should answer:

1. What is active?
2. What changed?
3. What needs a decision?
4. What is the next best build/review action?

## Standard Inputs

Run or inspect these in order:

```powershell
.\.venv\Scripts\dtp.exe kaizen status --limit 10
.\.venv\Scripts\dtp.exe evolution status
.\.venv\Scripts\dtp.exe memory steward --limit 10
.\.venv\Scripts\dtp.exe research steward --limit 10
.\.venv\Scripts\dtp.exe practice doctor
git status --short --branch
```

Add `dtp workspace dashboard` or `dtp workspace report` when the review spans
multiple repos or client lanes.

## Review Order

1. Confirm repo state and validation health.
2. Check Kaizen `now`, `next`, `waiting`, `blocked`, and `parked`.
3. Check Practice Evolution records that need review.
4. Check Memory Steward recommendations.
5. Check Research Steward recommendations.
6. Check Business Pattern Steward routes when firm, industry, innovation,
   infrastructure, or market observations were captured.
7. Check Knowledge Base Event Workflow triggers.
8. Check Autonomy Readiness candidates.
9. Decide one to three next actions.
10. Leave a review receipt when decisions or priorities changed.

## Decision Types

Every reviewed item should land in one of these states:

| Decision | Meaning | Typical Artifact |
|---|---|---|
| keep visible | useful but not ready for action | dashboard/status note |
| promote | move to decision, pattern, playbook, or source-of-truth memory | idea-evolution record, memory-promotion record |
| build | turn into scoped implementation | work item spec, PR, template, doc |
| pilot | test in one real lane before generalizing | pilot receipt |
| park | preserve without current action | Kaizen parked row, evolution parked state |
| reject | explicitly do not pursue | decision record or Kaizen discarded row |
| supersede | replace older idea/rule with newer operating rule | updated source doc and receipt |

## First Review Bias

For now, bias reviews toward internal OS quality before returning to client
lanes unless a client date is imminent.

Priority order:

1. operating patterns that prevent lost ideas;
2. memory/research/status surfaces that reduce Toni's manual load;
3. autonomy-readiness candidates that are internal and low-risk;
4. consulting-site/business-positioning artifacts after internal language is
   reviewed;
5. client-lane work when a meeting, reply, or deadline is inside the active
   window.

## Boundaries

This review loop does not authorize:

- sending emails;
- changing calendar events;
- syncing Notion;
- changing public consulting copy;
- publishing proof;
- installing tools/connectors;
- running autonomous workflows;
- touching production systems;
- creating or modifying raw private client records outside the approved vault.

The loop can recommend those actions. Toni approval and the owning gate still
decide whether they happen.

## Output

Use `practice-os/templates/practice-operating-review.md`.

The output should be short enough to read quickly and durable enough that a
future agent can resume without asking Toni to replay the conversation.

Minimum output:

- date and reviewer;
- sources checked;
- current state;
- decisions made;
- next one to three actions;
- parked items;
- approval gates;
- validation result;
- next review trigger.

## Acceptance Criteria

This loop is working if:

- Toni can ask "where are we?" and get a current answer from DTP state;
- captured ideas do not disappear after one chat;
- steward recommendations turn into decisions, not noise;
- useful patterns are promoted only after review;
- parked ideas remain visible without hijacking the day;
- autonomy candidates move through readiness gates instead of becoming vague
  ambitions;
- the next best action is obvious after the review.
