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
- Current core manifests: DTP, consulting, Hub, and `tm-skills`.
- Current adjacent manifests: `demario-pickleball-1`, `FamilyTrips`, `engineering-playbook`, and `fitness-app` / Omnexus.
- Use pilots to prove the shape before applying it to more adjacent projects.
- Keep repo-local gates authoritative.
- Do not centralize secrets, private client data, or production write credentials here.
- Do not implement a Workspace Command Center runner until repo manifests and evidence indexes prove useful; the V0 spec is docs-only.
- Treat evidence indexes as receipts from the last review pass, not as a replacement for fresh local validation.
