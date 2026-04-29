# Architecture

`dtp` is a local CLI plus a local browser workbench. The repo and private vault are the memory system.

The current architecture is markdown-first:

- `src/dtp/` contains the CLI and safety-checked command implementation.
- `dtp web` serves a local-only Workbench from the same command layer; it does not introduce a separate app database.
- `skills/` contains the draft-time Skills loaded by `dtp draft`.
- `extracts/` contains raw repo fingerprints, pattern candidates, lessons, and synthesis docs.
- `practice-os/` contains reusable policies, templates, operator Skills, and reviewed Bottleneck Patterns.
- `engagements/` contains private client kit work and is gitignored by default.
- `dtp vault` can initialize `engagements/` as a separate private git repo so client artifacts can be snapshotted and pushed without entering the public/code repo history.

Raw extraction stays in `extracts/`, reviewed reusable judgment moves to `practice-os/`, and client-private material stays in `engagements/`.
