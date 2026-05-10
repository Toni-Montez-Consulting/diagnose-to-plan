---
data_class: P1
confidential: false
permission_level: internal_only
review_status: accepted
---

# Steward Receipt - Practice Operating Review Loop V0

Date: 2026-05-10

Status: accepted internal operating update

## Trigger

After the Practice Evolution, Memory Steward, Research Steward, Research Arm,
Knowledge Base Event Workflow, and Autonomy Readiness Ladder passes, Toni asked
for a thorough review of what had been done and to keep moving forward.

The review showed that the system had strong capture and routing surfaces, but
needed a deliberate operating cadence so lightweight captures do not remain
lightweight forever.

## Decision Captured

- Add a Practice Operating Review Loop V0.
- Default to a weekly operating review with a daily light check when actively
  working the practice.
- Use existing DTP commands and steward surfaces before deciding the next build.
- Produce a review receipt when priorities, promotion decisions, parked items,
  or autonomy candidates change.
- Keep client communication, public proof, Notion sync, tool installs,
  production writes, and autonomous workflows gated.

## Artifacts Added

- `docs/PRACTICE_OPERATING_REVIEW_LOOP_V0.md`
- `practice-os/templates/practice-operating-review.md`
- `decisions/0013-practice-operating-review-loop.md`

## Artifacts Updated

- `docs/DOCUMENTATION_MAP.md`
- `practice-os/templates/activation-routing-map.md`
- `docs/PRACTICE_INTELLIGENCE_CONTROL_PLANE.md`
- `docs/PRACTICE_OPERATING_SYSTEM_STRATEGIC_BACKLOG.md`
- `src/dtp/commands/practice.py`
- `tests/test_practice.py`

## Boundaries

- No runtime behavior was added.
- No consulting, Hub, Notion, Gmail, Calendar, client, public proof, or
  production system changed.
- This is an internal DTP operating cadence.

## Next Use

Run the loop when Toni asks:

- "where are we?";
- "review everything";
- "what is next?";
- "are we losing ideas?";
- "keep moving forward";
- "what should memory/research/autonomy do next?";
- or after a disconnect/timeout that risks context drift.
