---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Repo Manifest: dse-content

## Identity

- Repo: `dse-content`
- GitHub repo: personal/Microsoft-linked namespace; verify live before reuse
- Local path: `dse-content`
- Primary role: internal Azure Apps/AI content, readiness workflows, and Microsoft-adjacent delivery surfaces
- Owner lane: DSE/internal professional proof candidate
- Public/private: COI-gated internal/professional lane
- Deploy target: verify in repo before any touch pass

## Boundaries

- Owns: DSE content workflows, readiness-center surfaces, internal/professional artifacts, repo-local validation
- Does not own: consulting public proof, DTP practice roadmap, Hub runtime, client engagement kits, public claims
- Sensitive data: Microsoft-adjacent work context, internal names, customer/prospect references, unreleased strategy, DSE-specific proof
- COI/privacy notes: any reuse outside the repo requires COI, permission, redaction, and reviewer gates before publishing or sales use

## Gates

- Local gate: verify in `dse-content` before touching; do not infer from DTP
- CI gate: verify GitHub Actions or deployment status live before claiming current health
- Release gate: repo-specific and Microsoft-adjacent; not owned by DTP
- Support gate: manual until repo lane is reopened
- Manual gate: COI review, permission review, and redaction review before proof or public positioning

## Evidence

- Evidence path: `practice-os/efficiency/dse-content-evidence-index.md`
- Latest receipt: placeholder coverage row only; live verification required before implementation or proof
- Proof eligibility: internal/professional only until COI and permission gates pass
- Redaction rule: do not copy raw DSE/Microsoft/customer material into DTP public docs or consulting proof

## Automation

- Safe read commands: `git status --short --branch`, repo README/docs inspection, repo-local test/build commands after checking package scripts
- Safe write commands: none from DTP by default
- Commands that need explicit approval: production deploys, public proof edits, Microsoft/customer-adjacent reuse, repo migration, external publication
- Dependency maintenance: repo-owned; DTP only records evidence if a touch lane is active
- Toolchain pinning: repo-owned

## Next Touch

- Lane: COI-aware proof/readiness pass
- Trigger: Toni explicitly reopens DSE lane or needs an internal/professional proof packet
- Blocker: COI, permission, and redaction review are required before reuse
- Next action: run a repo-local status/validation sweep and create a DTP proof review only when the lane is active
