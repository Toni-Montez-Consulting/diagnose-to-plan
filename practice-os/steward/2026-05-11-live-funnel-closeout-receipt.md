---
created: '2026-05-11T13:18:57Z'
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Live Funnel Closeout Receipt

## Receipt Metadata

- Date: 2026-05-11
- Operator: Codex for Toni
- Public surface: `https://tonimontez.co/start`
- Runtime owner: Hub on `https://onhand.dev`
- Consulting branch: `codex/live-funnel-polish-20260511`
- Hub commit after dependency triage: `d8478c6`
- Environment: production public intake to production Hub runtime
- Test record label: `DTP live intake smoke 20260511T131132Z`

## Scope

This pass closed the live buyer-path loop and kept adjacent runtime
maintenance separate:

- reconcile booking-link docs;
- run one approved production browser smoke;
- record sanitized Hub verification;
- retire unused consulting components;
- triage green Hub dependency PRs without touching failing PRs.

Out of scope: public proof, screenshots, private Hub row dumps, client
communication, new assistant runtime, new backend architecture, or direct
production row deletion.

## Preflight

- [x] Public `/start` rendered the form.
- [x] Normal `/start#contact` had no visible `Book a Diagnostic Call` link.
- [x] Test record used synthetic, clearly disposable content.
- [x] No real client/private data was submitted.
- [x] Hub protected dashboard was used only for summarized field verification.

Note: Vercel env export blanks protected secret values. The protected Hub
dashboard verification used the local Hub operator token from the ignored Hub
`.env` file without printing the token.

## Submission

- Submitted at: 2026-05-11T13:11:32Z
- Browser or command used: Playwright browser against production page
- Public route: `https://tonimontez.co/start#contact`
- Endpoint path: production Hub intake action from the rendered form
- Response status: browser success state reached
- User-visible result: URL changed to
  `https://tonimontez.co/start?intake=sent#contact`
- Post-submit CTA: `https://calendar.app.google/b8tqDrveqe2FQGnMA`

## Hub Verification

Do not paste the full private row.

- Verified at: 2026-05-11T13:18:57Z
- Verified by: Hub protected dashboard API with operator token
- Row/table pointer: `supabase.intake_submissions`, row id suffix `165e0a8e`
- Expected field summary: synthetic smoke-test name, redacted synthetic test
  email marker, source `tonimontez.co`, triage version `practice-start-v1`
- Storage result: row found with status `new`
- Any unexpected field: none observed from summarized fields
- Screenshot or log path, if redacted: none captured

## Cleanup

- [x] Test row is clearly labeled as disposable test data.
- Cleanup action: no current Hub console/API intake archive or delete route
  exists. Hub supports archive/delete for todos and outreach, not intake
  submissions.
- Cleanup verified at: 2026-05-11T13:18:57Z
- Residual record, if any: one synthetic test row remains in
  `supabase.intake_submissions` with the smoke-test label.

## Consulting Cleanup

- Updated consulting docs that still treated `PUBLIC_DIAGNOSTIC_CALL_URL` as
  pending.
- Added a small submit-state note and `aria-busy` form state to
  `ContactIntake.astro`.
- Retired unused components after `npm run knip:advisory` identified them:
  `BusinessSpine`, `MediaGallery`, `OperatingInstall`,
  `OperatorConsolePreview`, `PerformanceChart`, `PersonalDossier`,
  `ProductPreview`, `ProofShelf`, and `SystemOverlay`.

## Hub Dependency Triage

Merged after green remote CI/security checks:

- Hub PR #74: `3e3447c`
- Hub PR #75: `dc114d3`
- Hub PR #76: `d8478c6`

Left parked:

- Hub PR #77: `@hono/zod-openapi` 1.4.0; build-test jobs fail.
- Hub PR #78: Tailwind 4.3.0; typecheck and build-test jobs fail.

Decision: do not merge #77 or #78 without a targeted Hub-local fix pass.

## Result

- Status: `passed_with_notes`
- What this proves: the live public path can submit a synthetic intake, the
  post-submit Diagnostic Call CTA renders the approved booking URL, and Hub can
  see the private intake row.
- What this does not prove: public proof, real prospect conversion quality,
  private row screenshot safety, intake cleanup automation, or the next real
  prospect follow-up template.
- Follow-up: run the next real prospect, Cam/Greg/CCAAP reply, or weekly
  Business Brain reset through the DTP templates; add Hub intake cleanup only
  if repeated test/ops friction makes it worth a runtime change.

## Proof Boundary

- This receipt supports private operational confidence.
- This receipt does not authorize public screenshots, private row excerpts, Hub
  console captures, or proof claims without the proof promotion runbook.
