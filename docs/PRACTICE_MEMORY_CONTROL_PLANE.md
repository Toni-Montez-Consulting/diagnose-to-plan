---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Practice Memory Control Plane

Status: Priority 1 operating layer before larger infrastructure.

Owner repo: `diagnose-to-plan`

## Honest Capacity Assessment

Codex can help Toni handle the current project load if important state is
captured into durable artifacts as work happens.

Codex should not be trusted as the only memory for the practice. Chat context
can compact, live tool state can drift, inboxes can change, repo branches can
move, and client work can become too sensitive to reconstruct from memory.

The practical answer is a memory control plane:

1. DTP is the source of truth.
2. Notion is the phone cockpit and idea inbox.
3. Gmail, Calendar, QuickBooks, GitHub, and project repos are inputs or
   execution surfaces, not the practice memory by themselves.
4. Every meaningful idea, reply, meeting note, blocker, decision, proof gate,
   or next action becomes a DTP artifact first.
5. Notion mirrors only the sanitized fields Toni needs to see quickly.

## Current Pressure

The active load includes:

- Cam / SMB marketplace prototype: waiting on requested item packet and using
  Cameron's personal email for future communication.
- Greg / TheGrantApp.io: waiting on discovery availability and case-study
  permission boundaries.
- CCAAP: waiting on Dad/Leah clarification before site changes or launch work.
- Consulting site: first public assistant pilot candidate, still pre-code.
- Notion cockpit: active and useful, but not authoritative.
- Business Brain: useful enough to keep, but still early and manual.
- QuickBooks: possible future financial source, not connected yet.

## Memory Objects

Use these objects instead of relying on chat memory.

| Object | Source | DTP destination | Notion mirror |
|---|---|---|---|
| Client reply | Gmail, text, call follow-up | `engagements/<client>/<engagement>/reply-intake-*.md` | sanitized status only |
| Meeting notes | AI summary, owner call, discovery session | private kit meeting notes plus extraction files | sanitized meeting status/action summary |
| New idea | chat, phone thought, meeting tangent | `practice-os/templates/contextual-idea-intake.md` output or backlog story | Idea Inbox row |
| Decision | architecture, client boundary, proof posture, tool choice | decision record or steward receipt | decision summary only |
| Waiting state | client input, COI, proof, repo gate, owner approval | `owner-action-items.md`, `plan.md`, backlog | waiting_on / blocked_by |
| Proof candidate | project result, screenshot, outcome, client quote | proof packet and redaction queue | proof gate status only |
| Connector | Notion, Gmail, Calendar, QuickBooks, GitHub | `practice-os/templates/connector-map.md` plus runbook | capability/status summary only |
| Session receipt | major implementation/review sprint | `practice-os/steward/*.md` | latest status / next action |

## Priority 1 Loop

### Start Of Work Block

1. Run `dtp workspace report` when the question spans more than one repo or
   active client.
2. Check DTP client kit status for Cam, Greg, and CCAAP when client work is in
   scope.
3. Check Gmail only for the relevant threads before changing waiting states.
4. Check Notion Command Center for cockpit visibility, not source-of-truth
   decisions.
5. Check `git status --short --branch` in any repo that may be edited.

### During Work

1. If Toni gives a new idea, classify it before building it.
2. If the idea is actionable now, create or update the owning DTP artifact.
3. If the idea is useful but not active, put it in the backlog or idea intake.
4. If the idea touches sensitive data, proof, client communication, payments,
   finance, legal, COI, or public claims, record the gate before execution.
5. If work changes external status, update DTP first and Notion second.

### End Of Work Block

1. Update the relevant DTP source files.
2. Update sanitized Notion cockpit fields only when status changed.
3. Leave a steward receipt for major sprints.
4. Run the repo gates appropriate to the changed files.
5. Commit tracked DTP docs/templates when they are meant to be durable public
   practice infrastructure.
6. Leave private engagement files ignored unless they belong in a separate
   private durability path.

## Weekly Business Brain Reset

Use the Monday reset to answer:

1. What changed in Gmail, Calendar, Notion, and active repos?
2. Which client is waiting on Toni?
3. Which client is Toni waiting on?
4. Which proof claims are blocked?
5. Which ideas are still only in Notion or chat and need DTP triage?
6. Which repo has dirty/uncommitted work?
7. What are the next three actions for the week?
8. What should stay parked?

## Notion Premium Boundary

Notion Premium/Plus may make the cockpit more useful through better views,
search, collaboration, page history, or AI features depending on the exact plan
enabled in the workspace.

The upgrade does not change the source-of-truth rule:

- Notion may capture ideas quickly.
- Notion may mirror active status.
- Notion may help with phone review.
- Notion should not become the private engagement archive, proof vault, repo
  validation source, or place where raw transcripts, secrets, payment records,
  client data, or unsupported claims live.

Any premium-only feature should be verified in the live workspace before DTP
depends on it.

## QuickBooks Boundary

QuickBooks can become a read-only financial input later, but it should not be
hooked into the operating system casually.

Official Intuit docs indicate QuickBooks Online integrations use the
QuickBooks Online Accounting API, OAuth 2.0, scopes such as
`com.intuit.quickbooks.accounting`, and company identifiers called `realmID` or
company ID. Webhooks are also OAuth-gated.

Reference docs:

- https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api
- https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0
- https://developer.intuit.com/app/developer/qbo/docs/learn/scopes
- https://developer.intuit.com/app/developer/qbo/docs/develop/webhooks

Use this ladder:

### V0: Manual Export

- Toni exports the specific QuickBooks report needed.
- DTP stores only a redacted summary or a private file outside tracked git.
- The Controller role marks financials unavailable if no export is provided.
- No OAuth app, token storage, webhook, or API polling exists.

### V1: Read-Only Connector Readiness

- Confirm QuickBooks Online vs QuickBooks Desktop.
- Confirm account owner and company realm.
- Create or select an Intuit developer app.
- Request only the minimum read scope needed.
- Store client secret, refresh token, realm ID, and app credentials outside git.
- Define which reports/entities are allowed: for example invoices, payments,
  expenses, P&L summary, and pipeline-adjacent revenue summaries.
- Define which data is blocked: payroll, tax filings, bank balances, personal
  account data, SSNs, raw customer payment details, and anything not needed for
  the operating summary.

### V2: DTP/Hosted DTP Read-Only Import

- Pull only approved summary fields.
- Write an import receipt.
- Keep raw financial data out of public docs and Notion.
- Never create invoices, update books, send payment reminders, or mutate
  QuickBooks from DTP without a separate write-scope decision.

## Hard Rules

- Do not keep decisions only in chat.
- Do not let Notion become the source of truth.
- Do not let QuickBooks become a live dependency before connector rules,
  credentials, source-of-truth order, and read/write boundaries are accepted.
- Do not mirror private contact details, raw emails, transcripts, terms,
  payment/member records, or proof claims to Notion.
- Do not build more automation to compensate for missing intake discipline.

## Next Implementation Slice

1. Use the memory checkpoint template for the next broad infrastructure or
   client-status session.
2. Add QuickBooks to the connector map as `not_connected`.
3. Keep Notion cockpit as the daily visible layer.
4. After two weekly reset cycles, decide whether the pain is still capture
   discipline or whether hosted DTP/import automation is justified.
