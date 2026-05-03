# Working In This Repo

This repo is Toni's local consulting harness and the source of truth for the
Business Brain / Consulting OS.

## Operating Posture

- Treat DTP as the durable home for consulting practice memory, Practice OS
  assets, command contracts, business-domain operating rules, client kit
  methodology, proof/redaction gates, and roadmap execution.
- Keep the CLI local-first and file-first. Hosted DTP, Notion, Hub, and future
  consoles can render or mirror repo-authored artifacts, but they do not become
  source of truth unless a later decision explicitly changes that.
- Use `practice-os/` as the real repo convention for reusable policies,
  commands, skills, agents, templates, fixtures, comms, and steward receipts.
  Do not create a parallel `practice/` tree from older conceptual prompts.
- Keep client-sensitive work in ignored/private `engagements/` or a private
  vault. Promote only redacted, reviewed, reusable lessons into `practice-os/`.

## Business Brain Scope

- The Business Brain should understand more than software delivery: operations,
  managerial judgment, admin, accounting, finance, reporting, valuation,
  pricing, legal/compliance issue spotting, handoff, and support rhythms.
- Build the system through small, useful artifacts first: command contracts,
  fixtures, meeting prep, COI screens, proposals, operator handoffs, comms
  drafts, lessons, and eval candidates.
- Use human-in-the-loop self-improvement. Agents may propose skill, template, or
  command refactors against evidence and fixtures, but humans approve changes.

## Agent And Automation Boundaries

- Agents write repo artifacts. They do not auto-send client communications,
  auto-publish public proof, auto-merge skill refactors, or mutate production,
  billing, databases, or client data without explicit review.
- Controller, General Counsel, COO, and similar roles are draft-producing
  operating modes. They are not autonomous actors.
- Notion is a mirror and mobile inbox. QuickBooks, n8n, and other integrations
  stay stubbed or file-based until credentials, tools, and source-of-truth rules
  are confirmed.
- Do not add multi-tenant SaaS, public storefront pricing, courses/cohorts/info
  products, or self-rewriting skills unless a later accepted roadmap decision
  unlocks them.

## Editing Rules

- Do not write real bodies for root `skills/voice`, `skills/pricing`, or
  `skills/sow`; Toni owns those draft-time skills.
- Upgrade existing Practice OS skills before creating duplicates.
- Never write to sibling repos from this harness unless the user explicitly
  asks for a cross-repo implementation and the relevant repo boundary is clear.
