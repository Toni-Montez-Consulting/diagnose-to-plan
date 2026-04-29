# Client Command Room Pattern

This pattern captures the reusable concepts from the `demario-pickleball-1` admin portal and turns them into a future engagement pattern for Toni's practice.

The goal is not to clone the pickleball admin UI into every project. The goal is to reuse the operating shape: a small protected room where the owner can run the thing after the build ships.

## Source Pattern

The current reference implementation is `demario-pickleball-1`:

- `/admin`: protected owner dashboard.
- `/admin/tasks`: short-term operating tasks.
- `/admin/roadmap`: owner-facing business roadmap.
- `/admin/site-roadmap`: developer-facing implementation roadmap.
- Admin auth is protected by allowed admin emails plus MFA.
- The dashboard is domain-specific: bookings, inquiries, payment status, availability, manual blocks, recurring blocks, and calendar diagnostics.
- The handoff docs translate technical setup into owner language: daily review, weekly review, cancellation rules, payment matching, venue routing, and "do not touch" areas.

The most important idea is the split between owner operations and developer operations. Mario sees the business checklist and tasks he can act on. Tonio sees the implementation roadmap and technical gates.

## Reusable Shape

A Client Command Room should usually have five surfaces:

1. **Dashboard**
   - The client's live operating state.
   - Examples: bookings, intake, inquiries, orders, requests, approvals, open issues, upcoming commitments.
   - The data should match the business workflow, not generic SaaS dashboard tropes.

2. **Tasks**
   - Short-term actions the owner can finish this week or next.
   - Supports categories, due dates, recurrence, notes, complete/delete/edit.
   - This is not a full project-management system.

3. **Business Roadmap**
   - Plain-language owner checklist.
   - Each item says what to do, what done looks like, and when to hand something back.
   - Written for the client, not for a developer.

4. **Developer / System Roadmap**
   - Implementation tracker for Toni.
   - Shows shipped items, remaining technical gates, and deferred work.
   - Keeps owner-facing operations separate from code/infra decisions.

5. **Handoff / Rules**
   - Daily, weekly, and exception workflows.
   - "Do not touch" list for risky surfaces: environment variables, database settings, secrets, OAuth apps, code, payment processor config.
   - Domain rules that prevent future confusion, such as venue-routing rules, cancellation rules, payment matching, permission proof, or redaction rules.

## Why It Works

The pattern gives the client a way to operate the system without learning the stack.

It also gives Toni a stronger delivery artifact:

- The client receives more than a site or app.
- The handoff becomes visible in the product.
- The roadmap prevents support drift.
- The owner has one place to see what matters.
- Future improvements have a home before they become random text threads.
- Case-study proof becomes easier because the command room shows before/after operating state.

## What To Reuse From Pickleball

Reuse these ideas:

- Protected owner route with real auth when private records exist.
- Simple top navigation: Dashboard, Tasks, Business, Developer.
- Domain-first dashboard panels.
- Filterable operational tables.
- Status badges for state that matters.
- Deliberate destructive actions with confirmations.
- Plain-language empty states.
- Owner-safe task list with recurrence.
- Checkable roadmap items persisted to a tiny table.
- Separate owner roadmap and developer roadmap.
- Diagnostics cards for connected systems.
- Handoff docs that match the UI.
- "Do not touch" sections for risky admin surfaces.

Do not automatically reuse:

- The exact data model.
- The exact navigation labels.
- The exact visual system.
- The exact booking/availability workflow.
- A full admin app for a client that only needs a static handoff checklist.

## Fit In Toni's Practice

### For Toni

The current consulting `/admin` is a noindex public-safe command room. It is useful as a launcher/status surface, but it is not the final private practice cockpit.

The future hosted private DTP app can borrow this pattern:

- Dashboard: active engagements, missing kit artifacts, proof queue, redaction queue, open COI items.
- Tasks: near-term practice actions, client follow-ups, proof capture, launch checks.
- Business: practice roadmap and offer/proof gates.
- Developer: hosted DTP build, Hub integration, `tm-skills`, tooling, deploy gates.
- Handoff/Rules: Microsoft kill switch, COI, redaction, public/private boundary, client consent.

### For Clients

Use the command room when the engagement creates an ongoing operating workflow:

- A local business needs booking, intake, payment tracking, scheduling, or follow-up.
- A nonprofit needs donation/contact intake, content responsibilities, volunteer/task flow, or grant/reporting reminders.
- A builder/founder needs launch checklist, support queue, user feedback triage, or release readiness.
- A client has repeated decisions that currently live in scattered texts, spreadsheets, email, or memory.

Skip the command room when the client only needs:

- A simple marketing site.
- A static handoff document.
- A one-time audit with no ongoing operating workflow.
- A workflow already well handled by Notion, Airtable, Google Sheets, or an existing CRM.

## Data Model Starter

Keep the first version small.

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

Only add domain tables when the workflow demands them: bookings, inquiries, volunteers, donations, approvals, assets, releases, support requests, content updates, or inventory.

## Build Order

1. Capture the workflow in the Client Operating Kit.
2. Decide whether the client needs a command room or just a handoff checklist.
3. Define the owner-facing operating states.
4. Define the developer/system roadmap separately.
5. Create the smallest protected surface that lets the owner run the workflow.
6. Add handoff docs that use the same language as the UI.
7. Add proof capture: screenshots, walkthrough, metric baseline, and caveats.
8. After delivery, promote reusable pieces into DTP patterns only after redaction review.

## Candidate Pilots

- **Brother / DeMario pickleball:** reference implementation for local business operations, booking, tasks, owner roadmap, developer roadmap, and handoff.
- **Mom nonprofit:** likely candidate if the rebuild includes recurring volunteer, donation, content, reporting, or intake responsibilities.
- **Greg app/site:** candidate once scope clarifies; use DTP to decide whether it needs a command room or just a launch checklist.
- **Cam application:** likely a builder launch surface first; command room only if the app needs post-launch operations.
- **Toni consulting / hosted DTP:** private practice command room for engagement state, redaction queue, proof queue, and internal tasks.

## Anti-Patterns

- Building a generic CRM.
- Showing vanity metrics the owner cannot act on.
- Mixing public proof pages with private records.
- Making the client manage developer tasks.
- Making Toni manage the client's routine tasks forever.
- Adding a database because the UI looks better with live state.
- Turning every small website into a portal.

## Case Study Angle

The proof format should show:

- before: owner was managing work through texts, memory, manual follow-up, or scattered spreadsheets;
- after: owner has one protected room with the key actions and rules;
- evidence: dashboard screenshot, task list, roadmap progress, handoff checklist, and a short walkthrough;
- metric: fewer missed follow-ups, faster booking/inquiry handling, clearer owner handoff, or reduced admin time;
- caveat: what stayed manual on purpose.

This is the kind of proof local operators understand quickly. It reads as receipts, not a glossy case-study essay.
