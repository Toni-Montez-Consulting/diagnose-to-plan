---
created: 2026-04-30
command: manual
type: decision
status: accepted
---

# 0006 - GitHub enterprise organization boundary

## Decision

Use `Toni-Montez-Consulting` as the canonical GitHub organization for the consulting/practice portfolio repositories:

- `consulting`
- `diagnose-to-plan`
- `hub`
- `engineering-playbook`
- `hub-prompts`
- `hub-registry`
- `Omnexus`
- `FamilyTrips`
- `demario-pickleball`
- `tm-skills`

Keep `dse-content` outside this organization in the personal/Microsoft-linked namespace because it is Microsoft-adjacent and remains COI-gated.

## Rationale

Organization ownership gives the consulting practice a cleaner business boundary, centralized policy/billing surface, and clearer separation between public/professional consulting work and Microsoft-adjacent DSE work.

## Consequences

- Local `origin` remotes for consulting/practice repos should point to `https://github.com/Toni-Montez-Consulting/<repo>.git`.
- DTP manifests and roadmaps should use `Toni-Montez-Consulting` for consulting/practice GitHub references.
- `hub-registry` targets should use the organization namespace for non-DSE repos.
- `dse-content` remains explicitly excluded from this ownership move until Toni selects it with COI-aware scope.

## Guardrails

- Do not move `dse-content` into the consulting organization by default.
- Do not treat GitHub organization ownership as proof-publication approval.
- Do not weaken redaction, consent, proof, or COI gates because a repo moved under the consulting organization.
