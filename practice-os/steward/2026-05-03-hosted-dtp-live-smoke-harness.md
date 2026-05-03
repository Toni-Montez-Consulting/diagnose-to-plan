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

- `apps/private-dtp/.env` is not present.
- Supabase CLI is not installed locally in this shell.
- Supabase MCP is available, but discovered live projects are Omnexus Mobile,
  Consulting, familytrips, and Mario Pickleball.
- No dedicated DTP / Hosted DTP Supabase project was found.

## Decision

Do not reuse existing Omnexus, Consulting, FamilyTrips, or Mario Supabase
projects for the DTP operating brain. Hosted DTP needs its own project boundary
before live private records are written.

Because the dedicated project and operator accounts do not exist yet, the
implementation pass added a repeatable live smoke harness instead of applying
migrations to the wrong environment.

## Implemented

- Added `npm run smoke:live` in `apps/private-dtp/package.json`.
- Added private smoke env placeholders to `apps/private-dtp/.env.example`.
- Added `apps/private-dtp/scripts/smoke-live.mjs`.
- Updated Hosted DTP docs, evidence index, repo manifest, roadmap backlog, and
  this Business Brain packet to make the gate explicit.

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

## Manual Gate

To complete the live smoke:

1. Create or select a dedicated DTP Supabase project.
2. Create two operator test accounts.
3. Apply `apps/private-dtp/supabase/migrations/0001_private_dtp_phase0.sql`.
4. Configure `apps/private-dtp/.env` with public Supabase URL/anon key plus the
   two test account credentials.
5. Run `npm run smoke:live` from `apps/private-dtp`.

## No-Touch Boundaries

- No Supabase project was created.
- No migration was applied to an existing live project.
- No service-role key was requested or used.
- No emails were sent.
- Stripe remains parked.
- FAOS, QuickBooks, public proof, client portals, and autonomous agents remain
  parked.

