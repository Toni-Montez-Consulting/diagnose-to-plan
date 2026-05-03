# Private DTP Phase 0.1

Status: local private UI implementation plus schema/app-shell scaffold and
passed live smoke against the dedicated `DTP Private` Supabase project.

This app is the private hosted surface for the DTP operating brain. It is
single-operator first and preserves local markdown/private-kit fallback.

## Owns

- Engagement records.
- Artifact inventory and artifact versions.
- Evidence runs.
- Redaction reviews.
- Proof candidates.
- Decisions.
- Steward items.
- Research items.
- Import/export receipts.

## Does Not Own

- Consulting public proof pages.
- Hub intake/runtime/prompt-run rows.
- Client-facing portals.
- CRM, billing, e-signature, or account-management workflows.
- Autonomous agents, auto-send, or direct public publishing.

## Phase 0 Files

- `supabase/migrations/0001_private_dtp_phase0.sql`: Supabase schema, RLS, and
  operator-owned records.
- `src/screens.json`: minimal app-shell route contract for the first private UI.
- `src/import-export-contract.json`: markdown/private-kit round-trip contract.
- `src/App.tsx`: private Auth/RLS-backed record surface for the core queues.
- `src/importExport.ts`: markdown import/export helpers for local fallback.
- `src/schema.ts`: screen/table/field contract used by the UI.
- `scripts/smoke-live.mjs`: Auth/RLS live smoke for the core Phase 0 tables.
- `.env.example`: required Supabase public client environment keys.

## Local Commands

```powershell
npm install
npm test
npm run build
npm run smoke:live
npm run dev
```

Required environment:

- `VITE_SUPABASE_URL`
- `VITE_SUPABASE_ANON_KEY`
- `PRIVATE_DTP_OPERATOR_EMAIL`
- `PRIVATE_DTP_OPERATOR_PASSWORD`
- `PRIVATE_DTP_SECOND_OPERATOR_EMAIL`
- `PRIVATE_DTP_SECOND_OPERATOR_PASSWORD`

The app uses the browser Supabase client only. Service-role keys do not belong
in this app.

`npm run smoke:live` signs in two private operator accounts, writes one smoke
record across each core Phase 0 table, generates an engagement-summary markdown
export in memory, records an import/export receipt, verifies the primary
operator can read the rows, verifies the second operator cannot read them, and
verifies the second operator cannot attach a row to the primary operator's
engagement. It does not use service-role credentials.

## Implementation Boundary

The Phase 0.1 app reads and writes the core records through Supabase Auth and
RLS when pointed at a Supabase project with the Phase 0 migration applied. It
does not add dashboards, analytics, client portals, deep Hub sync, MCP recall,
QuickBooks writes, or public proof publishing.

Local markdown remains a first-class fallback. Hosted DTP is not the only copy
of private engagement state until backup, export, and access rules are accepted.

## Next Gate

The first live smoke passed against the dedicated `DTP Private` Supabase project
on 2026-05-03. Local `.env` is configured on this machine and remains ignored
by git.

Do not reuse existing Omnexus, Consulting, FamilyTrips, or Mario Supabase
projects for the DTP brain. The next gate is deciding the real operator account,
backup/export rules, and deployment posture before storing non-smoke engagement
records.
