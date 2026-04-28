---
title: "V1 was a paper spec"
date: 2026-04-28
status: accepted
---

# Decision: V2 is the first real harness build

The original V2 build spec assumed an existing `diagnose-to-plan` V1 repo with a working `dtp draft` command and three authored skills: `voice`, `pricing`, and `sow`.

That repo does not exist on disk or in an authoritative remote. V1 was specified in conversation only. The implementation therefore starts fresh at `C:\Users\tonimontez\Projects\diagnose-to-plan`.

This changes the section 1 decision in the build spec:

- Do not extend a missing repo.
- Do not invent V1 history.
- Scaffold V2 as the first real implementation.
- Keep the CLI name `dtp`.
- Keep the Phase 1 acceptance target: a fixture diagnose note produces a markdown SOW with scope, deliverables, and pricing sections.

The three V1 skills are also paper-only. Phase 1 must create valid placeholder files at:

- `skills/voice/SKILL.md`
- `skills/pricing/SKILL.md`
- `skills/sow/SKILL.md`

Each placeholder must have valid frontmatter and the body `# TODO: Toni authors this skill`. The validator should see them as valid skills, but the implementation must not write the actual skill bodies for Toni.
