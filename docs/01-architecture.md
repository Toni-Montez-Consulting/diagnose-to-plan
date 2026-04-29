# Architecture

`dtp` is a local CLI. The repo is the memory system.

The current architecture is markdown-first:

- `src/dtp/` contains the CLI and safety-checked command implementation.
- `skills/` contains the draft-time Skills loaded by `dtp draft`.
- `extracts/` contains raw repo fingerprints, pattern candidates, lessons, and synthesis docs.
- `practice-os/` contains reusable policies, templates, operator Skills, and reviewed Bottleneck Patterns.
- `engagements/` contains private client kit work and is gitignored by default.

Raw extraction stays in `extracts/`, reviewed reusable judgment moves to `practice-os/`, and client-private material stays in `engagements/`.
