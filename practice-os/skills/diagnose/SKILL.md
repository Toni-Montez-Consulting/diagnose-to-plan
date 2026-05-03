---
name: diagnose
description: Turns rough owner, prospect, or business context into a concise Diagnose memo or meeting brief with current read, bottleneck, non-AI fix, gaps, questions, data sensitivity, COI/proof gates, and next action.
risk_class: R1
version: 0.2.0
---

# Purpose

Convert messy business context into a grounded Diagnose memo or
`/diagnose-prospect` meeting brief.

Use this for operator-path prospects, Builder-path exceptions, owner calls,
client operating kits, and live proof threads where Toni needs a clear read
before deciding what to build or propose.

# Inputs Required

- owner/prospect notes or transcript
- current workflow or product state
- what breaks or what is unclear
- systems touched
- destination: meeting prep, diagnose memo, proposal input, or handoff input
- known COI/proof/permission constraints

# Data Allowed

Use only provided context, public facts supplied by the operator, and facts
verified during the run.

# Data Prohibited

Do not invent customer details, financials, Microsoft relationship facts, hidden
constraints, pricing, proof rights, or case-study approval.

# Steps

1. Identify the actual bottleneck.
2. Name the non-AI fix first.
3. Separate what works from what is missing.
4. Record data sensitivity, COI risk, and proof/permission gates.
5. Write questions that would change the recommended path.
6. Name the next useful artifact.
7. Capture skill/template candidates without promoting them automatically.

# Output Format

For internal diagnose work, use `practice-os/templates/diagnose-memo.md`.

For prospect prep, follow
`practice-os/commands/diagnose-prospect.md` and include:

- What this is.
- Current read.
- What works.
- Highest-leverage gaps.
- Recommended conversation sequence.
- Questions to ask.
- Risks / gates.
- Proposed next action.
- Follow-up artifact to draft.
- Skill/template capture candidates.

# Human Approval Trigger

Escalate if the scope touches Microsoft purchasing, regulated data,
legal/financial account detail, unclear consent, public proof, case-study rights,
or Builder-path equity/ownership.

# Fixtures

- Greg / TheGrantApp.io: marketing, onboarding, and match-explanation UX.
- Cameron / M&A platform: Builder-path boundary and COI gate.
