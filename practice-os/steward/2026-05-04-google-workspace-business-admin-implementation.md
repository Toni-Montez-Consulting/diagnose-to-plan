---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Google Workspace And Business Admin Implementation - 2026-05-04

## Trigger

Toni asked to implement the Google Workspace + Business Admin Operating Plan:
make the founder Workspace address the business-facing identity, use Google
Meet and Calendar, create a planning view for LLC/admin overhead, and capture
the reusable offering pattern from his own business buildout.

## Scope

- DTP is the source-of-truth layer.
- Notion is the clean cockpit/mirror.
- Consulting `/admin` is a launcher/status surface only.
- No filings, calendar writes, appointment-schedule creation, email sends, or
  legal/tax decisions were performed.

## Live Checks

| Check | Result |
|---|---|
| Google Calendar connector profile | founder Workspace address verified |
| Gmail connector profile | founder Workspace address verified |
| `tonimontez.co` MX | `smtp.google.com`, priority `1` |
| `tonimontez.co` root TXT | Google site verification and `v=spf1 include:_spf.google.com ~all` observed after Toni added SPF |
| `google._domainkey.tonimontez.co` TXT | DKIM record observed; Google Admin says authenticating |
| `_dmarc.tonimontez.co` TXT | not observed |
| `mail/calendar/meet.tonimontez.co` CNAMEs | not observed; optional service URLs |

## Artifacts Added

- `docs/BUSINESS_ADMIN_OPERATING_SYSTEM.md`
- `docs/INTERNAL_OFFER_REPERTOIRE_CATALOG.md`
- `practice-os/templates/business-admin-item.md`
- `practice-os/templates/offer-catalog-item.md`
- `practice-os/templates/calendar-policy.md`
- `practice-os/templates/apple-reminders-capture-pilot.md`

## Routing / Launcher Updates

- `docs/BUSINESS_BRAIN_OPERATING_SYSTEM.md`
- `docs/PRACTICE_MACHINE_OPERATING_MAP.md`
- `docs/OFFER_LED_PRACTICE_PACKAGING.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/PRACTICE_PRODUCTION_ROADMAP.md`
- `docs/ROADMAP_EXECUTION_BACKLOG.md`
- `docs/integration/reprioritization_log.md`
- `practice-os/templates/activation-routing-map.md`
- `practice-os/templates/connector-map.md`
- `C:\Users\tonimontez\consulting\src\pages\admin.astro`
- `C:\Users\tonimontez\consulting\README.md`
- `C:\Users\tonimontez\consulting\.env.example`

## Decisions

- Founder Workspace identity is the target for all external-facing calendar and
  meeting workflows.
- Personal Gmail remains a private availability source only.
- Google appointment schedules were created/tested manually and remain
  maintained through the Calendar UI.
- LLC/EIN/banking/tax work is a planning view with attorney/CPA gates, not
  Codex-executed filing behavior.
- Brand kit, mission/vision messaging, admin cockpit, Google setup, and client
  workflow systems belong in a private offer repertoire first.
- Apple Reminders stays Toni's daily task-capture/action surface. Google Tasks
  is intentionally out of scope. If a bridge is useful later, the first safe
  automation shape is a one-list business capture pilot into DTP/Notion, not an
  all-reminders sync.

## Notion Mirror

Mirror only sanitized rows:

- Business Admin:
  `https://www.notion.so/35672f18e4cc8150910cc68447fd0ba7`
- Google Workspace:
  `https://www.notion.so/35672f18e4cc817993c1d08e6977014e`
- LLC Readiness:
  `https://www.notion.so/35672f18e4cc8142a8cfde375f49be40`
- Offer Catalog:
  `https://www.notion.so/35672f18e4cc8136bcc5f732f403a70f`
- Apple Reminders Capture:
  `https://www.notion.so/35672f18e4cc81a9b99ec6fcd7216f7a`

The DTP artifact is authoritative. Notion rows are daily operating visibility,
not source-of-truth records.

## Next Actions

| Owner | Action | Gate |
|---|---|---|
| Toni | Keep Google Calendar/Meet connector on the founder Workspace account | connector profile returns founder address |
| Toni | Recheck DKIM in Google Admin by 2026-05-06; do not generate a new record unless Google still cannot verify | Admin console says enabled/verified |
| Toni | Add starter DMARC after DKIM is active: `v=DMARC1; p=none; pct=100` | `_dmarc` TXT exists |
| Toni | Maintain tested appointment schedules in Google Calendar UI | booking creates Meet event and mailbox flow is tested |
| Toni | Keep Apple Reminders as the task system; do not route daily work to Google Tasks | `Consulting` is the first bridge list only if a bridge becomes useful; `Omnexus` and `Architected Strength` stay separate; no all-reminders sync |
| Toni | Choose LLC professional-review path | attorney/CPA questions answered before filing |
| Codex | Keep DTP docs and Notion mirror in sync after Toni completes manual gates | DTP updated first |

## Safety Notes

Do not put raw email, calendar details, legal/tax documents, banking data,
personal reminders, client private records, unapproved screenshots, or
unsupported proof claims in Notion or the consulting site.
