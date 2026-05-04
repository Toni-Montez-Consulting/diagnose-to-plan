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
| Google Workspace / Google Admin | Workspace exists; admin console remains manual | domain email, DNS/authentication status, users/groups/settings, Meet/Calendar defaults | Toni / founder Workspace account | Google Admin web UI plus DTP business-admin checklist | revoke/limit admin OAuth apps; change Workspace admin access outside git |
| Google Calendar | Authenticated connector target is founder Workspace account; current connector must be rechecked before use | meeting titles/times/attendees; no raw client records | Toni | manual calendar entry plus DTP cadence note | revoke Calendar connector; delete or cancel generated holds |
| Apple Reminders | Not connected; future one-list capture pilot only | selected business reminder titles/due dates/list/source marker; no all-reminders sync | Toni | manual review in Apple Reminders plus DTP weekly packet | revoke IFTTT/Shortcuts/Reminders permission; delete pilot applet/shortcut |
| IFTTT / Shortcuts bridge | Candidate bridge for Apple Reminders after tooling review and `apple-reminders-capture-pilot` checklist | sanitized reminder events from one list only | Toni | manual copy into DTP/Notion | disable applet/shortcut/webhook; revoke app permissions on iPhone |
| GitHub | Authenticated connector/CLI available for repo work when repo lane is selected | repo metadata, issues, PRs, commits; no secrets | Toni / repo org | local git and GitHub web UI | revoke GitHub app access; use local git only |
| Browser / Playwright | Available for visual QA and local browser checks | rendered pages, screenshots, local app state; no private records unless explicitly approved | Toni / repo owner | repo-local build plus manual browser check | close browser session; remove generated artifacts if private |
| Canva / Figma | Candidate for proof/design assets | public-safe visual assets only after permission | Toni | static markdown briefs or repo-local assets | revoke design tool access; keep proof in DTP templates |
| Vercel / Supabase | Available by owning repo lane only | deployment/runtime metadata, logs, database schema or records depending on repo | repo owner | repo-local env/dashboard/manual checks | revoke project integration; rotate affected secrets outside git |
| QuickBooks Online | Not connected; future read-only financial input only after approval | financial/accounting summaries; invoices/payments/expenses only if explicitly approved | Toni | user-provided QuickBooks exports or financials unavailable | revoke Intuit app/OAuth tokens; remove connector secrets outside git |
| Assistant runtime | Not selected; future consulting public assistant candidate | approved public source corpus only for V0 | future runtime owner | human intake route and static site navigation | disable endpoint/widget; remove runtime secrets outside git |
