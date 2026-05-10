---
data_class: P1
confidential: false
permission_level: internal_only
review_status: template
template_name: autonomy-readiness-review
---

# Autonomy Readiness Review - <Workflow>

Date:

Reviewer:

Workflow:

Owning repo/lane:

Current autonomy level: A0 | A1 | A2 | A3 | A4 | A5 | A6

Requested next level: A1 | A2 | A3 | A4 | A5 | A6

Decision: approve next level | pilot next level | keep current level | park | reject

## Why This Workflow Wants More Autonomy

What repeated pain, delay, drift, or opportunity makes autonomy worth
considering?

## Current Manual Evidence

- Existing docs/templates/receipts:
- Number of successful manual runs:
- Known failures or misses:
- User value observed:

## Source Scope

- Allowed sources:
- Blocked sources:
- Source freshness risk:
- Private/client-sensitive data involved: yes | no

## Allowed Actions

- Allowed reads:
- Allowed writes:
- Allowed tools/connectors:
- Allowed triggers: manual | event-based | scheduled | continuous
- Output destination:

## Explicitly Blocked Actions

List sends, publishes, syncs, deploys, migrations, credential changes, public
claims, client actions, financial actions, or private-data actions this workflow
cannot perform.

## Data And Privacy Boundary

- Data class:
- Redaction needed:
- Retention rule:
- Logging/trace rule:
- Notion mirror allowed: yes | no

## Validation And Evals

- Dry-run mode:
- Test fixtures:
- Expected output checks:
- Regression checks:
- False-positive/false-negative risks:

## Audit, Rollback, And Override

- Audit log or receipt path:
- Rollback/undo path:
- Human override:
- Kill switch:
- Failure escalation:

## Cost And Runtime Boundary

- Runtime limit:
- Budget/cost limit:
- Rate limit:
- External service dependency:

## Promotion Decision

Why the workflow should move up, stay put, or be parked.

## Next Artifact

The next concrete artifact: role spec, source list, event workflow, eval
fixture, CLI command, dashboard, queue, PR, or FAOS story.

## Review Trigger

What future event should reopen this readiness review?

