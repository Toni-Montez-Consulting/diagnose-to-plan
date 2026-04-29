---
name: coi-screen
description: Screens prospects and scopes for Microsoft conflict risk using public/prospect-disclosed facts and written escalation rules.
risk_class: R2
version: 0.1.0
---

# Purpose

Protect the day job before proposal or serious scoping.

# Inputs Required

Prospect legal name, website, industry, location, tools, platforms, customer categories if voluntarily disclosed, and whether Microsoft products or purchasing are central.

# Decision Rules

- Pass if no obvious overlap exists.
- Flag if Microsoft products, purchasing, Azure, Copilot, M365, Purview, GitHub Enterprise, or day-job overlap are meaningful.
- Block if the work requires influence, confidential knowledge, Microsoft customer overlap, or competition with Microsoft business interests.

# Data Prohibited

Do not use or store internal Microsoft customer lists, partner information, roadmap, code, policies, or deal context.

# Output Format

Verdict: pass, flag, or block. Include short rationale and next action.
