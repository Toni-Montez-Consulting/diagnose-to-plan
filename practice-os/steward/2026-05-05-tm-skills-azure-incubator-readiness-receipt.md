# Engineering Readiness Receipt - tm-skills Azure/Foundry Incubator - 2026-05-05

Purpose: record whether the current tm-skills Azure/Foundry incubator state can be trusted, promoted, parked, or treated as not ready.

## Repo State

- Repo: `tm-skills`
- Branch: `main...origin/main`
- Commit SHA: `afa7897`
- Worktree state: dirty unresolved
- Dependency/install state: existing PowerShell scripts used; no install or dependency change run
- Run at: 2026-05-05
- Operator: Toni with Codex

## Scope

Inventory and gate the current Azure/Foundry incubator state:

- Modified promoted/incubator Azure, Entra, and Microsoft Foundry skill files.
- Deleted eval artifacts referenced by `manifest.json`.
- Untracked Azure and app/AKS/App Insights skill folders.
- Installer/freshness behavior for existing global discovery links.

No skill files were edited in this checkpoint. No global install was applied.

## Environment

- OS: Windows / PowerShell
- Runtime/tool versions: PowerShell scripts in `tm-skills/scripts`
- Important env/config notes: global skill links already point at `C:\Users\tonimontez\tm-skills\skills`

## Commands Run

| Command | Required? | Result | Notes or artifact |
|---|---|---|---|
| `.\scripts\doctor.ps1` | yes | fail | Hard failures: manifest references missing eval files; several SKILL.md files have unexpected frontmatter keys; unexpected untracked skill directories are present. |
| `.\scripts\freshness-check.ps1` | yes | pass | Phase 1 and current Azure/Foundry manifest entries are fresh through their due dates. |
| `.\scripts\install.ps1 -WhatIf` | yes | pass_with_skips | Skill links already point to tm-skills; existing global instruction files were skipped by design. |
| `git status --short --branch` | yes | fail_for_stability | Worktree remains dirty with modified/deleted tracked skill/eval files and untracked Azure skill folders. |

## Change Classification

| Change set | Classification | Reason |
|---|---|---|
| Existing modified Azure/Entra/Foundry SKILL.md files | parked | Doctor rejects unexpected frontmatter keys; do not promote until normalized. |
| Deleted eval trigger/output files | not accepted | Manifest still references these files; either restore evals or update manifest in a focused tm-skills pass. |
| Untracked Azure/app/AKS/App Insights skill folders | incubator only | Doctor treats them as unexpected; do not promote until manifest, eval, freshness, and smoke expectations are defined. |
| Global skill links | accepted | Installer preview reports `.agents`, `.claude`, and `.copilot` skill links already point to tm-skills. |
| External Claude Code / GitHub Copilot discovery | parked | Manual external reload/smoke was not run in this pass. |

## Security And Dependency Notes

- Secret scan: not run.
- Dependency/audit status: not applicable for this script-only checkpoint.
- Data/privacy notes: no project/client data was added or promoted.

## Manual QA

- Scenario: external Claude Code and GitHub Copilot discovery smoke.
- Result: skipped.
- Evidence location: `docs/EXTERNAL_TOOL_SMOKE_RUNBOOK.md` remains the manual runbook.

## Known Issues

| Issue | Severity | Owner decision |
|---|---|---|
| Doctor hard-fails on missing eval artifacts referenced by `manifest.json`. | High | fix in focused tm-skills pass |
| Doctor hard-fails on unexpected frontmatter keys in Azure/Foundry SKILL.md files. | High | fix in focused tm-skills pass |
| Doctor warns on unexpected untracked Azure skill directories. | Medium | park as incubator only |
| Worktree remains dirty and unresolved. | High | not ready |

## Decision

Checkpoint decision: not ready

## Next Action

- Next action: run a dedicated tm-skills fix pass that either restores eval files or updates manifest references, normalizes frontmatter, and decides whether untracked Azure folders are deleted, incubated with manifest coverage, or promoted with evals.
- Owner: Toni with Codex
- Target timing: after DTP and consulting checkpoints are committed or intentionally parked.

## Public Proof Notes

Do not use this receipt as public proof by itself. Public proof still needs source evidence, permission, redaction, reviewer approval, and caveat.
