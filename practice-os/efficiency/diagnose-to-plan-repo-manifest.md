---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Repo Manifest: diagnose-to-plan

## Identity

- Repo: `diagnose-to-plan`
- GitHub repo: `Toni-Montez-Consulting/diagnose-to-plan`
- Local path: `Projects/diagnose-to-plan`
- Primary role: private Practice OS, Client Operating Kits, redaction, COI, proof governance, and hosted-DTP private app foundation
- Owner lane: core infrastructure
- Public/private: private practice methodology with public-safe code/docs only
- Deploy target: none for current CLI; hosted DTP Phase 0.2 is a local/private app under `apps/private-dtp` with passed live smoke and live import/export round trip against the dedicated `DTP Private` Supabase project

## Boundaries

- Owns: DTP CLI, local Workbench, Practice OS, engagement-kit contracts, redaction/proof governance, hosted DTP schema/app-boundary planning, and the Phase 0.1 private app
- Does not own: consulting public site, Hub runtime records, client CRM/billing, project-specific app state
- Sensitive data: client kits, raw evidence, private proof assets, COI-sensitive notes
- COI/privacy notes: DSE/Microsoft-adjacent material requires COI-aware review before professional or public reuse

## Gates

- Local gate: `pytest`, `ruff check .`, `dtp skills --validate`, `dtp practice doctor`
- CI gate: DTP CI Python and Practice OS gates
- Release gate: targeted redaction checks for changed public-safe docs/templates
- Support gate: rerun hosted DTP live smoke and round trip after schema/Auth/RLS/import-export changes; public deployment waits on a separate accepted deployment decision
- Manual gate: public proof requires evidence, caveat, permission, redaction, and reviewer

## Evidence

- Evidence path: `artifacts/verification/dtp/` or GitHub Actions logs
- Latest receipt: see `practice-os/efficiency/diagnose-to-plan-evidence-index.md`
- Proof eligibility: DTP proof is internal until redacted and permissioned
- Redaction rule: raw private/client material stays out of public docs and repo history

## Automation

- Safe read commands: `rg`, `git status`, `git diff`, DTP validation commands
- Safe write commands: docs/templates/tests/code changes after task approval
- Commands that need explicit approval: global skill installs, hosted app deployment, private vault remote changes, production data writes
- Dependency maintenance: policy not enabled yet
- Toolchain pinning: future efficiency pass

## Next Touch

- Lane: Business Brain / Hosted DTP Phase 0.2 / Practice OS memory loop
- Trigger: next Cam, Greg, CCAAP reply, weekly Business Brain reset, hosted DTP deployment decision, or schema/Auth/RLS change
- Blocker: client-sensitive non-smoke records need lane-specific markdown fallback before Hosted DTP becomes normal workflow; public proof still needs permission/redaction/reviewer approval
- Next action: run reply intake on the next real client reply, repeat the Business Brain weekly reset, and use Hosted DTP only with markdown fallback plus review gates
