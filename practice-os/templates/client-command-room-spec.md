---
data_class: P0
confidential: false
permission_level: internal_only
review_status: reviewed
---

# Client Command Room Spec

Use this only after `client-command-room-fit-assessment.md` chooses "Build a Client
Command Room." Keep the first version narrow, owner-safe, and tied to real workflow state.

## Project Boundary

- Client/project:
- Engagement:
- Owner/operator:
- Toni-side maintainer:
- Private route or surface:
- Auth boundary:
- Data classification:
- Source fit assessment:

## Operating Thesis

One sentence:

> This room helps the owner run _____ by keeping _____, _____, and _____ in one protected
> place.

## Surface 1: Owner Dashboard

Purpose: show live operating state the owner can act on.

| Panel | Source of truth | Owner action | Empty state | Risk |
|---|---|---|---|---|
| | | | | |

Rules:

- Use domain language, not generic dashboard language.
- Show only state the owner can understand or act on.
- Do not show private proof material or developer-only evidence here.

## Surface 2: Owner Tasks

Purpose: give the owner a short-term action list.

| Task category | Example tasks | Due/recurrence | Completion rule |
|---|---|---|---|
| | | | |

Expected controls:

- create/edit/complete/delete only if the owner owns the task;
- category, due date, recurrence, and notes when useful;
- clear confirmation for destructive actions;
- no assignment workflow unless there are multiple real operators.

## Surface 3: Business Roadmap

Purpose: show the plain-language checklist the client uses to finish launch or operations.

| Item | What to do | Done means | Owner / Toni | Status |
|---|---|---|---|---|
| | | | | |

Rules:

- Write for the owner, not a developer.
- Include hand-back points: when the owner should contact Toni.
- Avoid infra terms unless the owner needs to recognize an external dashboard.

## Surface 4: Developer / System Roadmap

Purpose: keep implementation state separate from owner operations.

| Item | System area | Gate | Evidence | Status |
|---|---|---|---|---|
| | | | | |

Rules:

- This is for Toni and future agents.
- Keep secrets, keys, and raw logs out.
- Link to redacted evidence or command output summaries, not private records.

## Surface 5: Handoff / Rules

Purpose: make daily, weekly, and exception workflows impossible to misread.

Daily workflow:

- [Daily owner action]

Weekly workflow:

- [Weekly owner action]

Exception workflow:

- [Exception path or escalation rule]

Do not touch:

- environment variables;
- database settings;
- OAuth/app-provider configuration;
- billing/payment processor configuration;
- code/deploy settings;
- private proof or redaction queues.

Domain rules:

| Rule | Why it exists | Owner action | Escalate when |
|---|---|---|---|
| | | | |

## Optional Surface 6: Support / Verification

Add this only when evidence is produced by real commands, integrations, or manual gate logs.
Until then, leave the surface as a placeholder in the spec, not a UI full of hand-maintained
status cards.

| Status | Evidence source | Last checked | Owner-safe wording | Internal notes |
|---|---|---|---|---|
| Deploy/build | | | | |
| Intake/form | | | | |
| Auth/access | | | | |
| Payment/booking/connector | | | | |
| Redaction/permission | | | | |

## Data Model Starter

Use the smallest table set that supports the actual workflow.

```text
operator_tasks
- id
- title
- notes
- category
- due_date
- recurrence
- completed_at
- created_at
- updated_at

roadmap_checks
- key
- label
- surface
- checked
- updated_at

operating_records
- id
- type
- status
- title
- owner
- due_at
- payload
- created_at
- updated_at
```

Add domain tables only after the workflow demands them.

Candidate domain tables:

- bookings;
- inquiries;
- donations;
- volunteers;
- approvals;
- releases;
- support requests;
- assets;
- content updates.

## Launch Acceptance

- [ ] Owner can see the key operating state.
- [ ] Owner can complete the expected weekly workflow.
- [ ] Business roadmap and developer roadmap are separated.
- [ ] Handoff/rules page matches the UI language.
- [ ] Risky admin surfaces are named in "do not touch."
- [ ] Support/verification is connected to real evidence or left as placeholder only.
- [ ] Redaction/permission status is clear before any screenshots or walkthroughs are reused.

## Proof Packet Hooks

- Baseline screenshot or description:
- After-state screenshot or walkthrough:
- Metric:
- Caveat:
- Evidence source:
- Permission level:
- Redaction reviewer:
- What stayed manual on purpose:
