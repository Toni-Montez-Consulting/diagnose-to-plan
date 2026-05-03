---
data_class: P0
confidential: false
permission_level: internal_only
review_status: checked
---

# Hosted DTP Live Smoke Harness

## Trigger

Toni parked Stripe for now and asked to run the operating loop for real. The
active implementation lane became Hosted DTP Phase 0.1 live smoke while
Cameron, Greg, and CCAAP remain in waiting state until real replies arrive.

## Client Reply Check

- Gmail targeted scan found no new Cameron packet, Greg reply, or CCAAP owner
  reply beyond the already-recorded Cameron 2026-05-02 response.
- No email was sent, drafted, marked, or promoted from private state.
- Client lanes stay waiting; the next real reply should run through the client
  reply intake loop before build work, repo access, calendar movement, Notion
  mirroring, or public proof.

## Supabase Discovery

- Before live setup, `apps/private-dtp/.env` was not present.
- Supabase CLI is not installed locally in this shell.
- Supabase MCP is available, but discovered live projects are Omnexus Mobile,
  Consulting, familytrips, and Mario Pickleball.
- No dedicated DTP / Hosted DTP Supabase project was found before this pass.

## Decision

Do not reuse existing Omnexus, Consulting, FamilyTrips, or Mario Supabase
projects for the DTP operating brain. Hosted DTP needs its own project boundary
before live private records are written.

The first implementation pass added a repeatable live smoke harness instead of
applying migrations to the wrong environment. This follow-up pass created the
dedicated environment and ran that harness.

## Implemented

- Added `npm run smoke:live` in `apps/private-dtp/package.json`.
- Added private smoke env placeholders to `apps/private-dtp/.env.example`.
- Added `apps/private-dtp/scripts/smoke-live.mjs`.
- Updated Hosted DTP docs, evidence index, repo manifest, roadmap backlog, and
  this Business Brain packet to make the gate explicit.
- Hardened the Phase 0 migration so authenticated access is explicitly granted
  and anon table access is explicitly revoked for all `private_dtp_*` tables.

## Live Execution

- Created dedicated Supabase project: `DTP Private`.
- Project ref: `mrludoqxipapdmzxhrtf`.
- Region: `us-east-1`.
- Applied `apps/private-dtp/supabase/migrations/0001_private_dtp_phase0.sql`.
- Configured ignored local env at `apps/private-dtp/.env`.
- Created two smoke operator accounts.
- Confirmed Auth accounts for smoke use.
- Ran `npm run smoke:live`.
- Result: pass.
- Latest smoke engagement id: `05ab37c8-4674-44f1-8394-f6be147f187b`.
- Metadata verification showed all `private_dtp_*` tables have RLS enabled,
  authenticated select/insert privileges, no anon select privilege, and
  policies that explicitly require `auth.uid() is not null`.

## Smoke Coverage

The harness uses only browser-safe Supabase client credentials and two normal
operator accounts. It does not use a service-role key.

When configured, it:

- Signs in the primary operator and a second operator.
- Inserts one smoke record into engagements, artifacts, artifact versions,
  evidence runs, redaction reviews, proof candidates, decisions, steward items,
  research items, and import/export receipts.
- Generates a markdown engagement-summary export in memory.
- Verifies the primary operator can read every inserted row.
- Verifies the second operator cannot read any inserted row.
- Verifies the second operator cannot attach an artifact to the primary
  operator's engagement.

## Completed Gate

Completed on 2026-05-03:

1. Created a dedicated DTP Supabase project.
2. Created two operator test accounts.
3. Applied `apps/private-dtp/supabase/migrations/0001_private_dtp_phase0.sql`.
4. Configured `apps/private-dtp/.env` with public Supabase URL/publishable key
   plus the two test account credentials.
5. Ran `npm run smoke:live` from `apps/private-dtp`.

## Next Gate

- Decide the real operator account policy.
- Decide backup/export rules before storing non-smoke private engagement
  records.
- Decide deployment posture for the private app.
- Decide whether smoke accounts and records stay as regression fixtures or are
  rotated/deleted after each smoke run.

## No-Touch Boundaries

- No Omnexus, Consulting, FamilyTrips, or Mario Supabase project was reused.
- No service-role key was requested or used.
- No emails were sent.
- Stripe remains parked.
- FAOS, QuickBooks, public proof, client portals, and autonomous agents remain
  parked.
