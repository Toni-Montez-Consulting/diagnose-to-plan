---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Research Arm V0 Receipt - 2026-05-09

## Trigger

Toni forwarded founder-email notes about:

- a small squad of practical agents;
- a Research Arm Agent;
- AI agent market/research tracking;
- human-led authority;
- consulting practice intelligence;
- relationship-led consulting growth;
- Opportunity OS as a future relationship/opportunity system.

## Decision

Start with Research Arm V0 before Opportunity OS.

Reason:

- It supports the already active agent/ops lane.
- It can improve consulting quality without requiring private relationship
  records.
- It creates a reusable intelligence loop that can later feed Opportunity OS,
  offer shaping, content seeds, client education, and implementation proposals.

## Boundary Decision

Accepted:

- DTP owns the Research Arm operating method and templates.
- Consulting can hold public-safe pointers and business-facing consumption
  rules.
- Notion can mirror sanitized status.
- Opportunity OS should come next, but with source-of-truth boundaries designed
  before any private relationship data is stored.

Rejected:

- Notion as source of truth.
- Consulting repo as the raw private relationship database.
- Always-on autonomous research that can change positioning, offers, pricing,
  docs, or repos without approval.

## Artifacts Added

- `docs/RESEARCH_ARM_V0.md`
- `practice-os/templates/research-arm-digest.md`
- `practice-os/research/digests/2026-05-09-ai-agent-operating-shift.md`

## First Pilot

First manual Research Arm digest created from the 2026-05-09 founder-email packet:

- Microsoft Work Trend Index signal;
- 2026 State of AI Agents report;
- Chris Hood AI governance article;
- Toni's "Squad ideas" note;
- Toni's "Ideas for clients" note.

## Opportunity OS Next

After the first Research Arm digest, create Opportunity OS V0 with:

- source-of-truth split;
- relationship/opportunity data model;
- Notion mirror fields;
- capacity and overcommitment gates;
- referral-map model;
- warm-lead follow-up workflow;
- scoring rules for fit, trust, timing, leverage, risk, and bandwidth.

## Validation

Pending after implementation:

- `dtp practice doctor`
- `git diff --check`
