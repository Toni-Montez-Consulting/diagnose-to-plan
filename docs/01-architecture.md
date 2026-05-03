# Architecture

`dtp` is the Practice OS for the consulting practice. Today it is a local CLI plus a local browser Workbench. The production direction is a private hosted DTP app backed by Supabase Auth/RLS/storage, with the local CLI, Workbench, markdown artifacts, and private vault preserved as fallback and import/export surfaces.

The current architecture is markdown-first:

- `src/dtp/` contains the CLI and safety-checked command implementation.
- `dtp web` serves a local-only Workbench from the same command layer; it does not introduce a separate app database.
- `skills/` contains the draft-time Skills loaded by `dtp draft`.
- `extracts/` contains raw repo fingerprints, pattern candidates, lessons, and synthesis docs.
- `practice-os/` contains reusable policies, templates, operator Skills, and reviewed Bottleneck Patterns.
- `engagements/` contains private client kit work and is gitignored by default.
- `dtp vault` can initialize `engagements/` as a separate private git repo so client artifacts can be snapshotted and pushed without entering the public/code repo history.

Raw extraction stays in `extracts/`, reviewed reusable judgment moves to `practice-os/`, and client-private material stays in `engagements/`.

## Production Direction

The hosted DTP app should be private and single-user first. It should persist engagements, artifacts, artifact versions, metrics, redaction reviews, pattern candidates, and decisions. It should not replace the consulting site or Hub:

- Consulting remains the public storefront, `/start` path, public proof layer, and noindex command room.
- Hub remains runtime support for intake, private console rows, Supabase-backed operational records, webhooks, captures, runs, and prompts.
- DTP owns Client Operating Kits, redaction/COI gates, pattern promotion, and the canonical practice roadmap.

The Phase 0 schema/app boundary lives in `docs/HOSTED_DTP_PHASE_0.md`. That doc is the starting point for any future hosted schema, migration, or app-shell implementation.

See `docs/PRACTICE_PRODUCTION_ROADMAP.md` and `docs/DOCUMENTATION_MAP.md`.
