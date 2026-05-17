---
data_class: P1
confidential: false
permission_level: internal_only
review_status: draft
---

# Business Operating System Coverage Map

Status: internal manual coverage layer for auditing Toni's practice and client
businesses across the full operating surface.

Owner: `diagnose-to-plan`

Public rule: this map is not public offer copy, a SaaS plan, an automation
platform, a generic AI pitch, or approval to touch live systems. It is a
diagnostic lens for deciding which operating domain needs the next useful
artifact.

## Purpose

The current Practice OS is strong at the consulting spine: intake, diagnosis,
planning, build, proof, handoff, client cadence, steward review, Business
Memory, Campaign Ops, and admin setup.

This map adds the broader business-operations lens. It asks: if a real
business is messy, which operating domain is actually failing, what evidence
should Toni request, what is safe to do first, and what should stay gated?

Use this before claiming that a client, project, or Toni's own practice has a
complete operating system.

## Operating Rules

- Start manual. Create a coverage audit before proposing software, dashboards,
  connectors, public copy, or automation.
- Use source artifacts instead of guesses: emails, meeting notes, invoices,
  CRM exports, dashboards, SOPs, reports, calendars, support logs, and repo
  docs only when access is approved.
- Separate the business problem from the tool request.
- When AI, agents, automation, model orchestration, or governance are part of
  the business problem, complete
  `practice-os/templates/ai-operating-loop-readiness-review.md` before
  proposing runtime, connectors, public copy, compliance language, or autonomy.
- Keep private facts in ignored `engagements/` or private vaults. Track only
  sanitized operating meaning in DTP.
- Do not mutate client systems, financial systems, calendars, ad accounts,
  billing, legal records, production databases, Hub runtime, Notion, or
  QuickBooks from this map.
- Route public proof, public copy, client communications, connector setup, and
  live actions through their existing gates.

## Manual Audit Flow

1. Pick the business or client lane.
2. Complete `practice-os/templates/business-operating-system-domain-audit.md`.
3. Score each domain as `covered`, `partial`, `gap`, `blocked`, or `not
   relevant`.
4. Rank the top three opportunities by pain, repetition, source trust, safety,
   business value, and implementation clarity.
5. Recommend one safe first workflow or artifact.
6. Update the owning roadmap, private kit, steward receipt, or offer catalog
   only after the review creates a concrete next action.

## Domain Taxonomy

| Domain | Owner pain | Common signals | Source artifacts to request | Diagnostic questions | Safe first deliverables | Gates and no-touch boundaries | Likely offer route |
|---|---|---|---|---|---|---|---|
| Marketing / demand / Campaign Ops | The business needs attention, but channels, message, tracking, and follow-up are scattered. | Leads arrive from ads, referrals, social, groups, SEO, events, or word of mouth with unclear source quality. | Landing pages, ad notes, creative examples, channel reports, intake forms, analytics summaries, follow-up records. | Which channels produce qualified conversations? What message is repeated? Where does a lead go next? What should be learned weekly? | Campaign readiness packet, landing-page/offer review, tracking and follow-up checklist, weekly learning memo. | No ad account access, budget movement, campaign publishing, pixel changes, or ROAS promises without explicit approval. | Campaign Ops, Diagnostic Intake System, Business Systems Blueprint. |
| Sales / pipeline / CRM | Opportunities live in memory, inboxes, DMs, spreadsheets, or one person's head. | Follow-ups are missed, deal stages are unclear, proposals drift, and close/lost learning is not captured. | CRM export, spreadsheet, inbox labels, proposal list, call notes, intake submissions, referral notes. | What is an opportunity? What stage is it in? Who owns the next action? Why do deals close or stall? | Pipeline map, lead-stage definitions, next-action queue, proposal tracker, close/lost review. | No automatic outreach, calendar booking, pricing promise, contract change, or client message without review. | Client Follow-up / Cadence Queue, Diagnostic Intake System, Blueprint. |
| Offer / pricing / proposals | The business cannot explain, price, or scope work cleanly. | Custom quotes repeat, buyers ask the same questions, scope creep appears, value is hard to defend. | Offer docs, pricing notes, proposals, SOWs, service menus, sales objections, proof packets. | What is being sold? Who is it for? What is included/excluded? What evidence supports the price? | Offer map, proposal outline, SOW bridge, pricing decision ledger, proof-to-offer matrix. | No public pricing, contract terms, guarantees, or legal language without owner/professional review. | Mission / Vision / Message Sprint, Business Systems Blueprint, Custom Implementation SOW. |
| Delivery / fulfillment / workflow | Work gets done, but the path depends on memory and heroics. | Rework, status confusion, unclear owner tasks, inconsistent QA, or repeated handoff questions. | Current workflow, project plans, checklists, tickets, shared docs, handoff notes, delivery metrics. | What happens from sale to done? Where does work wait? What decisions repeat? What quality gate matters? | Workflow map, build task list, handoff checklist, exception register, delivery runbook. | No production mutation, system migration, or client-facing change without project-specific approval and verification. | Build The System, Launch / Proof Hardening Sprint, Client Command Room. |
| Customer success / support / retention | Customers need help after delivery, but support, adoption, and renewal signals are thin. | Repeated support questions, unclear severity, weak onboarding, churn risk, no health view. | Support inbox, FAQ, onboarding notes, issue tracker, renewal notes, usage summaries, feedback. | What do customers ask after purchase? What makes them successful? What needs owner judgment? | Support triage map, FAQ/source map, onboarding checklist, customer health memo, retention opportunity list. | No account changes, refunds, billing action, medical/legal/financial advice, or customer replies without review. | Business Memory OS, Client Operating Kit, Improve The System. |
| Finance / accounting / cashflow | Money state is hard to see or owner-dependent. | Invoices, expenses, taxes, subscriptions, AR/AP, margins, and cash timing live across tools. | P&L summary, invoice aging, expense categories, subscription list, tax calendar, payment processor summaries. | What is owed, due, recurring, profitable, or risky? Which reports are trusted? Who reviews them? | Manual finance source map, weekly close checklist, subscription/vendor register, redacted management memo. | No QuickBooks OAuth, live imports, bank access, payments, tax filings, or financial advice; use manual exports or mark unavailable. | Business Admin Cockpit, Controller close loop later. |
| Legal / risk / compliance / procurement | Obligations exist but are scattered or outside Toni's authority. | Missing contracts, unclear approvals, insurance questions, compliance promises, vendor terms. | SOWs, contract templates, policy docs, insurance notes, vendor agreements, COI screens, approval records. | What must be reviewed by a professional? What cannot be promised? What approvals are missing? | Issue-spotting checklist, COI screen, contract question list, procurement approval path. | No legal advice, signature, filing, insurance purchase, regulated assurance, or contract-term change without professional/owner review. | COI screen, Business Admin OS, proposal/SOW bridge. |
| People / vendors / delegation / access | Work depends on one owner or unclear helpers. | Contractors wait for direction, access persists too long, roles overlap, onboarding is verbal. | Role list, access list, contractor agreements, SOPs, task boards, delegation notes, QA assignments. | Who owns the work? Who can approve? Who has access? What should be delegated or removed? | Role/responsibility map, access review checklist, vendor approval queue, delegation playbook. | No account grants, access removals, hiring decisions, compensation changes, or vendor commitments without approval. | Admin Command Room, Client Command Room, Business Admin Cockpit. |
| Knowledge / SOP / training / Business Memory | The business answers recurring questions from memory. | Same questions repeat, documents are stale, onboarding is slow, decisions are hard to find. | SOPs, Drive folders, email templates, recordings, training notes, internal FAQs, product docs. | What questions repeat? Where is the answer trusted? What can be searched, drafted, workflowed, or human-only? | Business Memory diagnostic, source map, 25 recurring questions, SOP cleanup list, training handoff. | No uncontrolled self-learning, private retrieval, public assistant, or autonomous action; human approves durable memory. | Business Memory OS, Handoff / Review, Knowledge Layer Audit. |
| Tools / data / KPI / reporting | Tools exist, but management cannot see what matters. | Dashboards are stale, metrics conflict, reports do not drive decisions, tool ownership is unclear. | Tool inventory, KPI reports, dashboards, analytics summaries, data definitions, manual spreadsheets. | What decision does each metric support? Which source wins? What cadence reviews it? | KPI source map, weekly operating memo, dashboard critique, reporting cadence, tool owner list, AI operating loop readiness review. | No new connector, dashboard, tracking script, data warehouse, AI runtime, model orchestration, or analytics claim without source, privacy, and human-review gates. | Business Admin Cockpit, Improve The System, Practice Intelligence lens. |
| Launch / change management | A system exists, but people are not ready to operate it. | Launch stalls, owner inputs are missing, training is informal, rollback/support path is unclear. | Launch checklist, UAT notes, release notes, owner action list, training docs, support plan. | Who must do what before launch? What breaks trust? What should be tested, taught, or rolled back? | Launch gate matrix, UAT receipt, owner action packet, training/handoff plan, rollback checklist. | No production launch, DNS, App Store, public proof, or customer-facing change without explicit gate approval. | Launch / Proof Hardening Sprint, UAT Kit, Platform Operating Patterns. |
| Domain-specific operations | The business has industry-specific rules that generic templates miss. | Scheduling, inventory, donations, field service, fitness programming, nonprofit operations, marketplace workflow, valuation, or regulated steps shape the work. | Industry workflows, domain rules, service calendars, inventory sheets, donation/member flows, product-specific docs, compliance notes. | What makes this business different? What cannot be generalized? What domain rule changes the system design? | Domain operating brief, specialized workflow map, domain-source list, safe first artifact. | No regulated, clinical, financial, legal, marketplace, payment, or operational action without domain owner review. | Business Systems Blueprint, Client Operating Kit, Custom Implementation. |

## Current DTP Coverage Read

| Coverage area | Current state | Notes |
|---|---|---|
| Intake, diagnosis, proof, handoff, steward review | covered | Practice OS, Business Brain, proof/redaction, UAT, and steward receipts are strong. |
| Marketing / Campaign Ops | partial | Campaign Ops research exists, but needs a client-specific readiness packet before offer movement. |
| Sales / CRM | partial | Follow-up and intake patterns exist; full pipeline and close/lost operating cadence are not yet normalized. |
| Finance / accounting / cashflow | gap / blocked | Business Admin planning exists; QuickBooks and live financials remain intentionally blocked. |
| Customer success / support | partial | Omnexus and launch support patterns exist, but reusable post-launch support/retention cadence is thin. |
| Legal / risk / procurement | partial | COI and issue-spotting exist; procurement and contract ops are not a reusable lane yet. |
| People / vendor / capacity | gap | Access, delegation, vendor, and capacity reviews are not yet first-class templates. |
| KPI / reporting cadence | partial | Proof and verification exist; management reporting cadence is underbuilt. |
| AI governance / operating loops | review | MDASH-inspired pattern candidate and AI Operating Loop Readiness Review template exist; they need application to Greg, Cam, or DTP delivery before any public offer or runtime movement. |
| Training / adoption | partial | Handoff/runbooks exist; adoption and training plans need a stronger standard. |
| Domain-specific ops | gap | Active pilots contain domain knowledge, but there is no reusable domain-ops audit map yet. |

## First Use Recommendation

Use this map on one active or known lane before expanding it:

1. Greg, for sales funnel, Campaign Ops, app launch readiness, and support
   conversion.
2. Cam, for marketplace/M&A domain-specific operations, data, and workflow
   scope.
3. CCAAP, for nonprofit launch, donations/membership/contact routing, and
   owner handoff.
4. Omnexus, for product support, billing explanation, launch memory, and
   founder operating cadence.

Do not create software, hosted DTP behavior, Notion sync, Hub runtime, or public
offer copy until at least one manual audit proves the map changes the next
artifact.
