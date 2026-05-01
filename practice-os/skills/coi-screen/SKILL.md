---
name: coi-screen
description: Screens prospects, scopes, proof claims, and Builder-path opportunities for conflict/compliance risk using only public or prospect-disclosed facts and written escalation rules.
risk_class: R2
version: 0.2.0
---

# Purpose

Protect the day job and the practice before proposal, serious scoping,
contracting, public proof, or active-client creation.

# Inputs Required

- prospect legal name
- website or public context if provided
- industry and location
- tools, platforms, and customer categories if voluntarily disclosed
- whether Microsoft products, purchasing, Azure, Copilot, M365, Purview, GitHub
  Enterprise, or vendor selection are central
- proposed engagement shape
- public proof or naming expectations if any

# Decision Rules

- `pass`: no obvious overlap exists.
- `pass_with_conditions`: low-risk work can proceed only within named limits.
- `pending_human_review`: material facts are missing or employer/customer
  adjacency needs review.
- `refer_out`: work is better handled by another provider.
- `block`: work requires influence, confidential knowledge, Microsoft customer
  overlap, competition with Microsoft business interests, or unresolved risk.

# Data Prohibited

Do not use or store internal Microsoft customer lists, partner information,
roadmaps, code, policies, deal context, account context, or confidential employer
information.

# Output Format

Follow `practice-os/commands/coi-screen.md`:

- Prospect.
- Date.
- Source facts.
- Known unknowns.
- Risk checks.
- Decision.
- Contracting gate.
- Follow-up questions.

# Contracting Gate

If the screen is missing or unresolved, active-client creation, `/install-os`,
signed scope, paid work, equity agreements, and public proof should refuse.

# Fixture

- Cameron / Deloitte M&A side-project scenario:
  `practice-os/fixtures/business-brain/cameron-mckesson-coi-screen.md`
