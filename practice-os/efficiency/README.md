---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Workspace Efficiency Pilots

This folder holds optional pilot artifacts for the Workspace Efficiency Layer. These files are not runtime configuration and do not change repo behavior.

Rules:

- Start with DTP, then expand only to touched/core lanes.
- Current core manifests: DTP, consulting, Hub, `hub-prompts`, `hub-registry`, and `tm-skills`.
- Current adjacent manifests: `demario-pickleball-1`, `FamilyTrips`, `engineering-playbook`, and `fitness-app` / Omnexus.
- Use pilots to prove the shape before applying it to more adjacent projects.
- Keep repo-local gates authoritative.
- Do not centralize secrets, private client data, or production write credentials here.
- Use `dtp workspace report` for read-only coverage/evidence/blocker checks; do not implement live git/CI reads or a Workspace Command Center runner until the V0 report proves useful.
- Treat evidence indexes as receipts from the last review pass, not as a replacement for fresh local validation.
