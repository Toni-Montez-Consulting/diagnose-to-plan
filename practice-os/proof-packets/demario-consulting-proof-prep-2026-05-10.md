---
data_class: P0
confidential: false
permission_level: internal_only
review_status: review_ready
---

# DeMario Consulting Proof Prep Brief - 2026-05-10

Status: approved for a narrow consulting-site proof-card upgrade after public
claim review.

Owner: `diagnose-to-plan`

Target public surface: `consulting` homepage proof card for DeMario.

This brief prepares the next public-safe proof move. It does not approve a full
case study, private screenshots, testimonials, metrics, admin views, booking
rows, payment proof, or stronger business-impact claims.

## Recommended First Move

Use DeMario to strengthen the existing proof-type card only.

Do not create a full public case study yet. The current evidence is strong
enough to show practical local-business implementation, but a richer case study
would need a separate asset inventory, screenshot review, testimonial/review
source check, and owner-approved wording.

## Public-Safe Claim Shape

Allowed claim pattern:

> DeMario shows local-business implementation: a public coaching site with
> lesson paths, venue routing, booking flow, payment guidance, admin handoff,
> owner tasks, and launch operations around the real way the business runs.

Safe emphasis:

- local-business implementation;
- booking and venue-routing clarity;
- payment guidance and court-confirmation handoff;
- owner-operable admin workflow;
- launch readiness and handoff;
- site plus operating surface, not just a brochure.

## Stronger Homepage Card Candidate

Use this as the first candidate if `consulting` upgrades the proof card:

> DeMario shows the local-operator side of the work: a coaching site that
> helps students understand lessons, venue paths, booking, payment guidance,
> and court-confirmation expectations, with an owner admin workflow for
> bookings, inquiries, availability, tasks, and launch follow-through.

Shorter option:

> DeMario shows local-business implementation: lessons, venue routing, booking,
> payment guidance, owner admin workflow, and launch handoff for a real DFW
> coaching business.

## Evidence Used

- DTP proof packet:
  `practice-os/proof-packets/demario-launch-feedback-social-packet-2026-05-05.md`
- DTP evidence index:
  `practice-os/efficiency/demario-pickleball-1-evidence-index.md`
- DeMario repo-local docs:
  - `demario-pickleball-1/docs/APP_OVERVIEW.md`
  - `demario-pickleball-1/docs/DEVELOPER_PLAN.md`
  - `demario-pickleball-1/docs/RELEASE_CHECKLIST.md`
  - `demario-pickleball-1/docs/ADMIN_HANDOFF.md`
  - `demario-pickleball-1/docs/MARIO_ACTION_PLAN.md`
  - `demario-pickleball-1/docs/VENUE_RULES.md`
  - `demario-pickleball-1/docs/LAUNCH_OUTSTANDING.md`
- Live route spot-check on 2026-05-10:
  - `https://demariomontezpb.com/` returned 200
  - `/pay` returned 200
  - `/privacy` returned 200
  - `/terms` returned 200
  - `/admin/login` returned 200
- Repo state observed on 2026-05-10:
  - `demario-pickleball-1` clean on `master...origin/master`
  - HEAD `e92b1c0`

## Baseline

The local-business need was not only a polished web page. The business needed a
student-facing booking path, venue/platform routing, payment guidance, exact
court-confirmation expectations, owner admin workflow, launch handoff docs, and
plain-language owner tasks.

## After-State

The site and repo-local docs now support:

- public lesson and coaching presentation;
- venue-specific booking behavior instead of one generic booking path;
- direct site booking for public outdoor courts;
- platform-required routing for Dallas Indoor, The Grove, Life Time,
  TeachMe.To, and Samuel-Grand / Impact;
- payment guidance and booking-ID memo expectations;
- admin handoff for bookings, inquiries, availability, tasks, roadmap items,
  cancellation, and payment status;
- release and broader-promotion checklists that separate code readiness from
  manual business gates.

## Measurement Caveat

Do not claim business impact yet.

Allowed:

- launch/readiness;
- workflow clarity;
- owner-operable system;
- practical implementation;
- public route availability from spot-checks.

Not allowed without separate proof:

- bookings increased;
- revenue grew;
- conversion improved;
- student count changed;
- review count is verified;
- customer satisfaction improved;
- admin time was reduced by a measured amount.

## Permission And Redaction

Current permission:

- Toni already posted public-safe DeMario launch copy from Toni-owned LinkedIn
  and Instagram channels, with public post URLs recorded in the source proof
  packet.
- This brief prepares a consulting-site proof-card upgrade. It does not expand
  permission to private assets.

Public-safe today:

- text summary of the public site and workflow categories;
- public route names;
- public-page screenshots after a fresh screenshot review;
- the public domain `https://demariomontezpb.com`.

Still gated:

- private admin screenshots;
- booking rows;
- student names, emails, phone numbers, notes, or photos;
- payment records, QR/payment screenshots, payment memos, or financial data;
- Supabase, Vercel, Resend, Google Calendar, Sentry, or environment screens;
- testimonial or review claims until source and permission are confirmed;
- metrics or business-impact claims.

## Blocked Wording

Do not say:

- "automated Mario's business";
- "fully automated booking and payments";
- "proven revenue growth";
- "increased bookings";
- "students love the site";
- "AI built the site";
- "a complete CRM";
- "hands-free operations";
- "public proof of Toni's whole consulting OS";
- "case study" unless a separate case-study packet is approved.

## Consulting Copy Recommendation

For the next `consulting` pass, upgrade only the DeMario proof card.

Recommended target:

- `consulting/src/pages/index.astro`, DeMario proof record.

Recommended scope:

- replace the current DeMario copy with one stronger paragraph using the
  stronger homepage card candidate above;
- keep the card proof-type based;
- do not add metrics, testimonial language, screenshots, or a case-study link
  yet;
- keep the homepage proof-boundary note visible.

## Next Proof Work

If Toni wants a richer DeMario mini case study later:

1. create a screenshot asset inventory;
2. review every screenshot for private data;
3. confirm review/testimonial sources and permissions;
4. run a public claim review for exact wording;
5. run copy authenticity review;
6. only then add a dedicated case-study page or richer proof module.

## Review Decision

Claim review passed in
`practice-os/proof-packets/demario-homepage-card-public-claim-review-2026-05-10.md`.
Copy authenticity review passed in
`practice-os/proof-packets/demario-homepage-card-copy-authenticity-audit-2026-05-10.md`.

The approved public move is the homepage proof-card upgrade only. A full case
study should wait.
