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

## Postflight Results

- Non-DSE local `origin` remotes now point at `Toni-Montez-Consulting`; `dse-content` remains on the personal/Microsoft-linked remote.
- DTP, consulting, Hub prompts, Hub registry, FamilyTrips, DeMario, engineering-playbook, and tm-skills org-alignment changes were pushed.
- Hub protected-branch work landed through PR #60 after replacing the org-blocked Gitleaks Action with a pinned Gitleaks CLI scan.
- Omnexus protected-branch work is ready in PR #559 with green checks, but merge is blocked by the required-review policy.
- The old Omnexus PR #558 was closed because its `chore/*` branch name intentionally failed the main-branch gate.
- GitHub org ownership changes made hosted action licensing a real infrastructure concern: repo secret scans should prefer pinned local CLI/script gates unless a paid action license is intentionally configured.
- Hub current-tree secret scanning passes. Full-history scanning surfaced an old redacted historical finding, so any future "scan all history" policy should be handled as a separate baseline/rotation/history-cleanup story rather than mixed into org URL hygiene.

## 2026-04-30 Closeout Follow-Up

- Omnexus PR #559 was rechecked and remains blocked by required review; this gate was not bypassed.
- Hub local `main` is aligned to `origin/main`; stale local branch `chore/org-repo-references` was deleted after content-equivalence review against the squash-merged PR #60.
- Hub PR #59 was updated from `main` so the org-safe secret scan workflow can rerun on the dependency branch.
- Hub dependency triage is now tracked in `practice-os/steward/2026-04-30-org-migration-closeout-and-hub-dependency-triage.md`.

## Next Action

Merge Omnexus PR #559 after human review, then prune or resync local protected-repo PR branches. Keep `dse-content` excluded unless explicitly selected with a COI-aware scope.
