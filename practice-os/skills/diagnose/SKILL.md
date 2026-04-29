---
name: diagnose
description: Turns rough owner context into a concise Diagnose memo with bottleneck, non-AI fix, data sensitivity, and success criteria.
risk_class: R1
version: 0.1.0
---

# Purpose

Convert messy business context into a grounded Diagnose memo.

# Inputs Required

- owner notes or transcript
- current workflow
- what breaks
- systems touched

# Data Allowed

Use only provided context and public facts supplied by the operator.

# Data Prohibited

Do not invent customer details, financials, Microsoft relationship facts, or hidden constraints.

# Steps

1. Identify the actual bottleneck.
2. Name the non-AI fix first.
3. Record data sensitivity and COI risk.
4. Write success criteria the owner can recognize.

# Output Format

Use `practice-os/templates/diagnose-memo.md`.

# Human Approval Trigger

Escalate if the scope touches Microsoft purchasing, regulated data, legal/financial account detail, or unclear consent.
