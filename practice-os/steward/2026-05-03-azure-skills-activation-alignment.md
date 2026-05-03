---
data_class: P0
confidential: false
permission_level: internal_only
review_status: checked
---

# Azure Skills Activation Alignment - 2026-05-03

## Purpose

Align the first promoted Azure/Entra/Microsoft `tm-skills` incubator subset with
DTP activation routing before those skills are used for client or internal
infrastructure work.

## Decision

Keep the first Azure subset as a `tm-skills` incubator lane, not a Phase 1
practice-wide baseline. DTP remains the source of truth for COI, client facts,
proof, redaction, permission, and consulting gates.

## Activation Added

- Azure/Copilot/client prompts still start with DTP COI and data-boundary
  screening.
- Azure preparation routes to `azure-prepare`, with `azure-validate` as the
  next gate.
- Azure validation routes to `azure-validate` and must not become deployment
  without an accepted plan.
- Azure deployment routes to `azure-deploy` only after validation, owner
  approval, secrets handling, and rollback gates.
- Azure diagnostics, cost, RBAC, and resource lookup route to the matching
  incubator skills with a read-only default posture.
- Entra and Microsoft Foundry prompts route to `entra-app-registration`,
  `entra-agent-id`, and `microsoft-foundry` with tenant, identity, credential,
  eval, trace, and approval boundaries first.

## Boundary

- `dse-content` was intentionally not inspected, edited, staged, or touched in
  this slice.
- No additional Azure skill folders were promoted.
- No global install with `-Apply` was run.
- Claude Code and GitHub Copilot external smoke results remain manual until
  observed in those tools directly.

## Evidence

- DTP activation map updated:
  `practice-os/templates/activation-routing-map.md`
- `tm-skills` smoke/runbook hardening planned to cover Azure, Entra, and
  Foundry canary prompts.
- `tm-skills` doctor hardening planned to derive Phase 1/incubator coverage from
  `manifest.json` instead of duplicating promoted Azure skill names in the
  validator.

## Next Manual Gates

- Run the targeted Azure incubator smoke prompts in a safe internal context.
- Reload Claude Code and GitHub Copilot before marking external smoke passed.
- Record any trigger miss in `tm-skills/MISFIRES.md` and decide whether the fix
  belongs in a skill description, eval fixture, DTP routing map, or operating
  gate.
