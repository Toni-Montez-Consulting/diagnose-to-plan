---
name: redact
description: Reviews artifacts before external sharing or promotion into practice assets, checking identity, financial, credential, and claim/evidence risk.
risk_class: R2
version: 0.1.0
---

# Purpose

Prevent client-private or compliance-sensitive material from leaking into public proof or reusable practice assets.

# Checks

- identities removed or approved
- screenshots redacted
- financial specifics removed or approved
- credentials absent
- Microsoft-sensitive context absent
- claim has evidence, baseline, after-state, caveat, permission level, redaction status, and reviewer

# Output Format

Pass/fail list with required fixes.

# Human Approval Trigger

External publication, named case study use, or any case-study claim.
