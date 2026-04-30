---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Evidence Index: tm-skills

## Repo

- Name: `tm-skills`
- Branch: `main`
- Last updated: 2026-04-30
- Reviewer: Roadmap Steward expansion pass

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| local | 2026-04-30 | pass | `3e08ae0` | `doctor.ps1`, `freshness-check.ps1`, `install.ps1 -WhatIf` |
| CI | 2026-04-30 | pass | `3e08ae0` | tm-skills CI run `25143380786` |
| release | 2026-04-30 | partial | `3e08ae0` | `install.ps1 -Apply` previously succeeded without `-Force`; Codex discovery verified |
| support | 2026-04-30 | partial | `3e08ae0` | Codex discovered all five skills; Claude Code and GitHub Copilot remain manual |
| proof | 2026-04-30 | internal_only | current branch | operating proof only, not a client case study |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| Phase 1 global SDLC skills are visible in Codex | `tm-skills/docs/INSTALL_SMOKE_2026-04-30.md`, DTP roadmap update | internal_only | public-safe | reviewed for operating use |
| Claude Code and GitHub Copilot discovery are ready for manual smoke | installed links and install preview | internal_only | public-safe | pending |

## Open Gaps

- Claude Code and GitHub Copilot reload/smoke tests remain manual.
- Project-pinned canary is deferred until global discovery is stable.
- Real trigger misses should become `MISFIRES.md` notes or trigger eval updates.

## Notes

DTP owns cross-system routing. `tm-skills` owns the actual SDLC skill files, trigger descriptions, evals, install scripts, and misfire records.
