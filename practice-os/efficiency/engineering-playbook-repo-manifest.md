---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Repo Manifest: Engineering Playbook

## Identity

- Repo: `engineering-playbook`
- GitHub repo: `Toni-Montez-Consulting/engineering-playbook`
- Local path: `engineering-playbook`
- Primary role: cross-project engineering doctrine, repo schemas, templates, historical decisions, secret-management references, and operating playbook material
- Owner lane: adjacent reference/doctrine maintenance
- Public/private: private/internal reference repo
- Deploy target: none

## Boundaries

- Owns: general engineering doctrine, portfolio manifest schemas, artifact metadata schemas, sanitization policy, secret-management process, reusable templates, and historical operating decisions
- Does not own: active practice-production roadmap sequencing, private DTP engagement kits, hosted DTP implementation, Hub runtime records, public consulting proof pages, prompt catalogues, or project-specific app work
- Sensitive data: secret names and classifications may be tracked; secret values, client records, private engagement facts, Microsoft/customer data, and production credentials must not be committed
- COI/privacy notes: keep Microsoft-adjacent and client-specific material out unless it is public-safe, permissioned, and redacted

## Gates

- Local gate: PowerShell parse check for changed scripts, `.\scripts\portfolio-ops-check.ps1 -StatusOnly`, and `git diff --check`
- CI gate: none today; engineering-playbook remains local-evidence only unless a future workflow is intentionally added
- Release gate: no production release; push only after docs/scripts pass local checks
- Support gate: `README.md`, `.repo.yml`, `PORTFOLIO_DELIVERY_PROTOCOL.md`, `SECRET_MANAGEMENT.md`, `SANITIZATION_POLICY.md`, and `decisions/2026-04-29-practice-roadmap-source-of-truth.md`
- Manual gate: do not promote doctrine into active DTP roadmap ownership; DTP remains the current practice source of truth

## Evidence

- Evidence path: local PowerShell/check output, git status, and DTP evidence receipts
- Latest receipt: see `practice-os/efficiency/engineering-playbook-evidence-index.md`
- Proof eligibility: internal reference only; not a public proof source by default
- Redaction rule: never publish secret names in a way that implies values, client-private facts, Microsoft/customer material, or unreviewed internal process screenshots

## Automation

- Safe read commands: `rg`, `git status`, `git diff`, `Get-Content`, and `Select-String`
- Safe write commands: docs, templates, value-free schemas, and value-free scripts only when the engineering-playbook lane is active
- Commands that need explicit approval: adding CI workflows, changing secret vault bootstrap behavior, altering repo ownership policies, or publishing any playbook content outside the private repo
- Dependency maintenance: not applicable unless scripts gain external package dependencies
- Toolchain pinning: PowerShell and GitHub CLI assumptions live in scripts and README notes; keep them value-free and optional where possible

## Next Touch

- Lane: doctrine/reference maintenance
- Trigger: DTP changes a reusable cross-repo principle, a portfolio schema changes, secret-management process changes, or a repo policy in `scripts/consulting-ops-check.ps1` drifts from actual workspace gates
- Blocker: this repo must not become the active roadmap owner
- Next action: revisit only when a general doctrine or portfolio policy change needs durable reference material
