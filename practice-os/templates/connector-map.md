---
data_class: P0
confidential: false
permission_level: internal_only
review_status: reviewed
---

# Connector Map

| System | Permission | Data touched | Account owner | Fallback | Disable path |
|---|---|---|---|---|---|
| Notion | OAuth available; cockpit/mirror only | sanitized roadmap, client snapshot, proof status, idea inbox, meeting/action summaries | Toni | DTP markdown docs and private kits | revoke Notion integration/OAuth; stop Notion mirror updates |
| Gmail | Authenticated connector available when Toni explicitly asks | email headers/body snippets needed for reply intake and draft/send actions | Toni | manual copy into DTP reply-intake template | revoke Gmail connector; use manual email workflow |
| Google Calendar | Authenticated connector available for internal holds and confirmed client meetings | meeting titles/times/attendees; no raw client records | Toni | manual calendar entry plus DTP cadence note | revoke Calendar connector; delete or cancel generated holds |
| GitHub | Authenticated connector/CLI available for repo work when repo lane is selected | repo metadata, issues, PRs, commits; no secrets | Toni / repo org | local git and GitHub web UI | revoke GitHub app access; use local git only |
| QuickBooks Online | Not connected; future read-only financial input only after approval | financial/accounting summaries; invoices/payments/expenses only if explicitly approved | Toni | user-provided QuickBooks exports or financials unavailable | revoke Intuit app/OAuth tokens; remove connector secrets outside git |
