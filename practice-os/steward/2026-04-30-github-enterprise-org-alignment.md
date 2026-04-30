---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Roadmap Steward Receipt: GitHub Enterprise Org Alignment

## Session

- Date: 2026-04-30
- Active story: GitHub Enterprise org alignment
- Steward mode: postflight
- Owner: Toni Montez

## Trigger

Toni upgraded GitHub to Enterprise and moved consulting/practice repositories under the `Toni-Montez-Consulting` organization. `dse-content` remains on the personal/Microsoft-linked account and must not be touched by this pass.

## Scope

Update current operational references so future agents, registry checks, and repo manifests use the correct organization boundary:

- Local non-DSE Git remotes point to `Toni-Montez-Consulting`.
- DTP roadmaps and manifests record the organization namespace.
- `hub-registry` targets use the organization namespace for non-DSE repos.
- Repo-local playbooks and current setup docs point to the organization URLs.
- `dse-content` stays excluded and COI-gated.

## Repos Touched

| Repo | Intended Change | Notes |
|---|---|---|
| `diagnose-to-plan` | Source-of-truth docs, manifests, steward receipt, decision record | DTP remains the roadmap/steward owner |
| `consulting` | Repo metadata and current admin link | Public site remains storefront/proof surface |
| `hub` | Repo metadata and current docs/deploy references | Runtime boundary unchanged |
| `hub-prompts` | Repo metadata and playbook references | Prompt content unchanged |
| `hub-registry` | Repo metadata, docs, validator docs, targets | Cross-repo CI access still deferred |
| `engineering-playbook` | Repo metadata and doctrine references | Does not become roadmap source of truth |
| `FamilyTrips` | Repo metadata and playbook references | Privacy-first boundary unchanged |
| `demario-pickleball-1` | Repo metadata and setup/playbook references | Local branch remains `master` |
| `fitness-app` / Omnexus | Repo metadata and current docs/scripts/test references | Verification cockpit remains reference pattern |
| `tm-skills` | Local remote alignment | No tracked content change required |
| `dse-content` | No touch | Remains personal/Microsoft-linked and dirty from unrelated work |

## Gates

- Run repo-local validation for repos with behavioral references or validators changed.
- Run DTP validation after roadmap/manifest/steward changes.
- Confirm `dse-content` local remote and working tree are unchanged by this pass.
- Commit and push touched non-DSE repos separately.
- Watch CI where workflows exist.

## Boundaries

- Do not move `dse-content`.
- Do not add cross-repo GitHub tokens or sibling checkout patterns.
- Do not treat organization ownership as proof permission.
- Do not publish consulting proof or weaken redaction, consent, reviewer, caveat, or COI gates.

## Next Action

Finish validation, commit/push each touched non-DSE repo, and update the DTP evidence index result from `pending` to `pass` or `blocked` based on the actual gates.
