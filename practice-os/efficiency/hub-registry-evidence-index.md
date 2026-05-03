---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Evidence Index: hub-registry

## Repo

- Name: `hub-registry`
- Branch: `main`
- Last updated: 2026-04-30
- Reviewer: accepted by steward review on 2026-04-30

## Latest Verification

| Lane | Date | Result | Commit | Artifact |
|---|---|---|---|---|
| local | 2026-04-30 | pass | `3dcc759` | `npm run validate`: 9 targets, 11 prompt-trigger pairs, 1 cron schedule |
| local manifests | 2026-04-30 | pass | `3dcc759` | `npm run validate:manifests`: 8 manifests valid; `fitness-app` deferred by design |
| local prompt ids | 2026-04-30 | pass | `3dcc759` | `npm run validate:prompt-ids`: 3 referenced prompt ids exist in sibling `hub-prompts` |
| local full gate | 2026-04-30 | pass | `3dcc759` | `npm test`: registry shape, sibling manifests, and prompt ids passed |
| CI | 2026-04-30 | pass | `3dcc759` | GitHub Actions `Validate registry` run 25144066822; repo-scoped CI runs `npm run validate` only |

## Proof Candidates

| Claim | Evidence | Permission | Redaction | Reviewer |
|---|---|---|---|---|
| Hub registry references are locally cross-validated against prompt ids | `npm run validate:prompt-ids` and `npm test` output | internal_only | no public proof | steward reviewed |

## Open Gaps

- Repo-scoped CI does not run sibling manifest or prompt-id checks because private sibling checkout/access is intentionally deferred.
- Non-manual trigger activation remains gated by registry policy and explicit approval.
- Hub runtime dispatch and sync proof remain Hub-owned.

## Notes

This index records the local-first cross-repo validation contract. It does not authorize private CI tokens, target activation, prompt content changes, or Hub runtime changes.
