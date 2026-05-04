---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Business Admin Operating System

Status: source-of-truth workstream for Toni's Google Workspace, business
administration, legal/tax planning prompts, brand assets, and operating cadence.

Owner: `diagnose-to-plan`

Public surface: `consulting` may link to public-safe launcher/status entries
from `/admin`, but it must not render private records, legal/tax filings,
calendar details, raw email, client data, or payment/accounting records.

## Operating Intent

This lane turns Toni's own business overhead into a repeatable operating view:

- Google Workspace and meeting identity;
- Google Calendar / Meet booking policy;
- Apple Reminders daily task capture, with Google Tasks intentionally out of
  scope;
- LLC/EIN/banking/tax-readiness checklist;
- contracts, insurance, and professional-review prompts;
- brand and message asset inventory;
- reusable offer-catalog capture.

The goal is not to automate filings or legal/tax choices. The goal is to make
the overhead visible, sequenced, and reusable, then promote only safe, validated
patterns into client-facing offers.

## Calendar Policy

External meeting identity:

- `founder@tonimontez.co` is the business-facing email and calendar identity.
- Google Meet is the default conferencing option.
- Timezone is `America/Chicago`.
- Personal Gmail can block availability privately, but it should not be the
  external identity on client-facing invites once Workspace is fully connected.
- Codex must not create external events, appointment schedules, or calendar
  holds without explicit approval for the exact event details.

Live connector check on 2026-05-04:

| Check | Result | Status |
|---|---|---|
| Calendar connector profile | `founder@tonimontez.co` | verified for founder-facing reads and explicitly approved writes |
| Gmail connector profile | `founder@tonimontez.co` | verified |
| Domain MX | `smtp.google.com`, priority `1` | present |
| Root SPF TXT | `v=spf1 include:_spf.google.com ~all` observed | present |
| Google DKIM TXT | `google._domainkey.tonimontez.co` observed | present; Admin says authenticating |
| DMARC TXT | no `_dmarc.tonimontez.co` record observed | needs DNS |
| Custom service CNAMEs | `mail`, `calendar`, `meet` not observed | optional |

## Google Workspace Setup Checklist

| Item | Owner | Status | Next action | Evidence |
|---|---|---|---|---|
| Founder mailbox | Toni | tested | keep `founder@tonimontez.co` as the business-facing send/reply identity | Toni tested send/receive/reply behavior; Gmail connector returns founder address |
| MX routing | Toni | configured | leave as-is unless mail delivery fails | DNS shows `smtp.google.com` |
| SPF | Toni | configured | leave one root SPF record unless another sender is added later | DNS shows `v=spf1 include:_spf.google.com ~all` |
| DKIM follow-up reminder | Toni | waiting | recheck Google Admin DKIM status by 2026-05-06; do not generate a new record unless Google still cannot verify | DNS has `google._domainkey` TXT; Admin says authenticating |
| DMARC | Toni | open | add starter monitoring policy after DKIM is active: `v=DMARC1; p=none; pct=100` | no `_dmarc` TXT observed |
| Calendar connector | Toni | verified | use only for reads or explicitly approved event writes under the founder identity | Calendar connector returns founder address |
| Appointment schedules | Toni | tested | use the booking pages for qualified calls and keep questions/reminders aligned with the offer | Toni tested bookings and Meet links |
| Personal busy overlay | Toni | manual setup | share/read personal busy availability into Workspace calendar without exposing event details | Calendar settings |

## Appointment Schedule Blueprint

These schedules now belong in Google Calendar under the Workspace identity.
Toni tested bookings and Meet links manually; keep the blueprint here as the
operating standard for future edits:

| Schedule | Duration | Availability | Booking questions | Reminders | Gate |
|---|---:|---|---|---|---|
| Diagnostic Call | 30 minutes | weekday windows Toni approves | business context, broken workflow, what has been tried, what must stay private | 24h email, 1h popup | booking and Meet link tested |
| Client Working Session | 45 or 60 minutes | client cadence windows only | topic, artifact link, decision needed, blockers | 24h email, 2h popup | used only after qualified engagement |
| Handoff / Review | 30 minutes | delivery review windows | what needs review, owner decision, follow-up owner | 24h email, 1h popup | handoff artifact exists in DTP |

Default controls:

- Google Meet video conferencing.
- Require email verification where available.
- Add a buffer before and after calls.
- Do not expose private personal calendar details to bookers.
- Keep scheduling copy short and operator-voiced.

## Apple Reminders Capture Lane

Decision: Apple Reminders is Toni's primary personal and daily task capture
surface. Google Tasks is intentionally out of scope and should not be proposed,
configured, or used as a replacement unless Toni explicitly reopens that
decision.

Operating role:

- Apple Reminders owns fast capture, phone/watch/Siri reminders, recurring
  personal tasks, and day-to-day action nudges.
- Google Tasks owns nothing in this operating system.
- Google Calendar owns external business meetings, Google Meet links, and
  booking availability.
- DTP owns source-of-truth planning, business-admin decisions, and reusable
  offer patterns.
- Notion may mirror sanitized reminder-derived status only after review.

Recommended pilot:

1. Use Apple Reminders as the daily action layer.
2. If/when a bridge is useful, use the existing `Consulting` Apple Reminders
   list as the first business-admin capture pilot.
3. Keep `Omnexus` and `Architected Strength` as separate product/personal-brand
   operating lists; do not merge them into the consulting capture pilot.
4. Keep personal/family/health reminders out of the sync lane.
5. Mirror only title, optional due date, list name, and a source marker.
6. Send mirrored items to a sanitized Notion/DTP inbox, not to public site
   markup and not directly into client records.
7. Review the capture lane daily or weekly before promoting items into roadmap,
   business-admin, client follow-up, or offer-catalog artifacts.

Automation options:

| Option | Fit | Notes | Current posture |
|---|---|---|---|
| Native Apple Reminders + Apple Calendar | best daily use | Apple now supports creating/viewing reminders in Calendar on Apple devices, which helps day planning without leaving the Apple ecosystem | use immediately |
| IFTTT iOS Reminders | useful pilot | Supports new/completed reminder triggers and add-reminder actions, but iOS background sync depends on the IFTTT app and can be unreliable if the app is not opened | pilot on one low-risk list only |
| iOS Shortcuts to webhook | best controlled bridge | Can be designed as a manual or scheduled export from a chosen list to Hub/Notion/DTP later; avoids broad third-party access but requires phone-side setup | plan next |
| Google Tasks | not aligned | Would create a second task surface and fight the way Toni already works on phone/watch/Siri | out of scope |
| Craft/Things/Todoist-style import | not preferred | Often turns Reminders into another task manager and may be one-way/import-oriented; not aligned with keeping Reminders as the daily system | avoid for now |
| macOS local script/EventKit | later option | More private and controllable if a Mac is always on; more maintenance and not mobile-first | later |

Hard gates:

- No full two-way sync until a one-list pilot proves reliable.
- No sync of all reminders.
- No raw personal reminders, health/family tasks, legal/tax details, or client
  private tasks into Notion.
- No auto-completion across systems until duplicate/completion behavior is
  tested.
- No automation tool gets broad access without a Tooling Steward review.

## Business Admin Items

Use `practice-os/templates/business-admin-item.md` for any item that belongs in
this lane. Use `practice-os/templates/apple-reminders-capture-pilot.md` before
connecting Apple Reminders to Notion, DTP, Hub, Google, IFTTT, Shortcuts, or any
other automation surface.

| Lane | Owner | Status | Deadline | Next action | Blocker | Professional needed |
|---|---|---|---|---|---|---|
| Google Workspace | Toni | active | 2026-05-08 | add starter DMARC after DKIM Admin verification is settled | `_dmarc` not observed | no |
| Calendar / Meet | Toni | tested | 2026-05-08 | use tested booking pages for qualified calls; keep Meet, buffers, reminders, and questions aligned | booking links must stay maintained | no |
| Apple Reminders capture | Toni | active | 2026-05-10 | keep Apple Reminders as the action layer; use `Consulting` first only if a bridge is later useful | Google Tasks is out of scope | no |
| LLC readiness | Toni | planning | before first formal contract under entity | choose name, registered agent, mailing address, organizer, tax/pro review path | legal/tax choice | yes |
| EIN / banking | Toni | gated | after LLC filing | apply for EIN only after entity formation if using LLC | state filing not complete | yes |
| Contracts / SOW | Toni + attorney | planning | before paid client expansion | collect template needs and attorney-review questions | attorney review | yes |
| Insurance | Toni | planning | before higher-risk client work | price E&O/professional liability options | coverage choice | yes |
| Brand assets | Toni | active | 2026-05-06 | preserve official logo kit path and usage guide | none | no |
| Operating cadence | Toni | active | weekly | review Business Brain packet and admin blockers | starter DMARC still manual | no |

## LLC Readiness Prompt

This is a planning checklist, not legal or tax advice.

Texas working assumptions:

- Texas LLC formation uses Secretary of State Form 205 / SOSDirect-style filing.
- Formation fee is treated as a planning cost to verify before filing.
- A Texas registered agent and registered office are required.
- EIN should be requested after the entity is formed if the LLC path is chosen.
- Texas franchise/public information reporting remains an annual compliance
  item even when no tax is due.

Questions to settle with professional review:

- Entity name and availability.
- Registered agent choice and address privacy.
- Member-managed vs manager-managed.
- Operating agreement needs.
- Tax election posture.
- Contract signature block and invoice/payment name.
- Insurance needs by offer type.

## Brand And Messaging Source

Current official logo kit:

`C:\Users\tonimontez\Pictures\Toni-Montez-Official-Logo-Kit\2026-05-04`

Current brand language:

- Primary slogan: `Get the Work Out of Your Head.`
- Supporting descriptor: `Custom Apps / Workflow Systems / Practical AI Tools`
- Full explanation: `I help owner-led businesses turn scattered processes,
  manual work, and owner-only knowledge into custom apps, workflow systems, and
  practical AI tools that make the business easier to run.`

Durable routing:

- Use the logo kit as internal asset proof and brand-system source material.
- Consulting public site promoted the current slogan, descriptor, header
  wordmark, footer mark, favicon, and Open Graph image from this kit on
  2026-05-04.
- Architected Strength and other sibling sites are not automatically updated
  from this lane; each brand surface needs its own reopened scope and public
  boundary check.
- Do not publish new proof claims just because the brand kit exists.
- If this becomes a client offer, route it through
  `docs/INTERNAL_OFFER_REPERTOIRE_CATALOG.md` first.

## Notion Mirror Contract

DTP owns the source record. Notion may mirror only clean operational status:

- lane;
- current focus;
- status;
- next action;
- blocker/waiting-on;
- DTP source path;
- last mirrored date;
- proof status.

Do not mirror:

- private email content;
- raw meeting transcripts;
- legal/tax private documents;
- payment records;
- credential records;
- unapproved proof claims;
- client private data.

## Source References

- Google Workspace MX: https://support.google.com/a/answer/7174013
- Google Workspace SPF: https://support.google.com/a/answer/33786
- Google Workspace DKIM: https://support.google.com/a/answer/174124
- Google Workspace DMARC: https://support.google.com/a/answer/2466563
- Google Calendar appointment schedules:
  https://support.google.com/calendar/answer/10729749
- Apple Reminders:
  https://support.apple.com/en-us/102484
- Apple Reminders in Calendar:
  https://support.apple.com/en-gb/guide/iphone/iph14f1d32a5/ios
- Apple Shortcuts:
  https://support.apple.com/guide/shortcuts/welcome/ios
- IFTTT iOS Reminders:
  https://ifttt.com/ios_reminders
- IFTTT iOS background syncing:
  https://help.ifttt.com/hc/en-us/articles/115010193327-About-iOS-background-syncing
- Texas LLC Form 205:
  https://www.sos.state.tx.us/corp/instructions/205.shtml
- Texas franchise tax forms:
  https://comptroller.texas.gov/taxes/franchise/forms/2026-franchise.php
- IRS EIN:
  https://www.irs.gov/businesses/small-businesses-self-employed/get-an-employer-identification-number
