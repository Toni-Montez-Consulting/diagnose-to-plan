---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Repo Manifest: tm-skills

## Identity

- Repo: `tm-skills`
- Local path: `tm-skills`
- Primary role: reusable SDLC skill library for coding agents across repos
- Owner lane: global agent skill behavior
- Public/private: private personal skills repo with public-safe patterns
- Deploy target: none; installed through personal tool discovery paths

## Boundaries

- Owns: Phase 1 SDLC skills, trigger evals, global instruction templates, doctor/freshness/install scripts, misfire notes
- Does not own: DTP practice methodology, COI policy, client records, public proof, Hub runtime state, repo-specific product roadmaps
- Sensitive data: global instruction files, skill trigger behavior, future misfire examples if they mention private work
- COI/privacy notes: Microsoft/client-adjacent prompts must route back to DTP COI before scoping or coding

## Gates

- Local gate: `.\scripts\doctor.ps1`, `.\scripts\freshness-check.ps1`, `.\scripts\install.ps1 -WhatIf`
- CI gate: tm-skills CI runs doctor, freshness, and install preview on Windows
- Release gate: `install.ps1 -Apply` requires explicit approval; `-Force` requires separate explicit approval
- Support gate: Codex, Claude Code, and GitHub Copilot discovery smoke prompts after reload
- Manual gate: external tool reloads and prompt smoke results must be recorded before treating discovery as fully complete

## Evidence

- Evidence path: `docs/INSTALL_SMOKE_2026-04-30.md`, GitHub Actions logs, `MISFIRES.md` for trigger misses
- Latest receipt: see `practice-os/efficiency/tm-skills-evidence-index.md`
- Proof eligibility: internal operating proof only; not a client-facing proof item by itself
- Redaction rule: do not put private client material, secrets, or day-job details into skills or trigger evals

## Automation

- Safe read commands: `rg`, `git status`, `git diff`, `.\scripts\doctor.ps1`, `.\scripts\freshness-check.ps1`, `.\scripts\install.ps1 -WhatIf`
- Safe write commands: skills/docs/evals/scripts after task approval
- Commands that need explicit approval: `.\scripts\install.ps1 -Apply`, any `-Force`, replacing global instruction files, project-pinned canaries
- Dependency maintenance: no package manager lane yet; keep scripts dependency-light
- Toolchain pinning: PowerShell scripts and markdown-only skill files for Phase 1

## Next Touch

- Lane: finish discovery smoke and trigger-quality learning loop
- Trigger: Claude Code and GitHub Copilot reloads become available or a real misfire is observed
- Blocker: this session cannot verify external Claude Code or GitHub Copilot discovery
- Next action: run README smoke prompts in Claude Code and GitHub Copilot, then record results or misfires
