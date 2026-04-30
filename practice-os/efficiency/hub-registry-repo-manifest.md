---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Repo Manifest: hub-registry

## Identity

- Repo: `hub-registry`
- Local path: `hub-registry`
- Primary role: Hub automation target registry that maps repos, prompt ids, triggers, sensitivity, and dispatch settings
- Owner lane: prompt routing and automation-target governance
- Public/private: private/internal platform repo; registry changes can affect Hub automation behavior
- Deploy target: none; Hub consumes `targets.yml` during registry sync

## Boundaries

- Owns: `targets.yml`, registry schema validation, target/routing policy, sibling manifest validation, and local prompt-id cross-validation against `hub-prompts`
- Does not own: prompt body text, Hub runtime execution, DTP engagement kits, consulting proof, or production credential access
- Sensitive data: repo routing intent, prompt dispatch triggers, sensitivity labels, target metadata, and future automation policy
- COI/privacy notes: confidential repos and Microsoft/DSE-adjacent material must remain disabled/manual until explicit COI-aware approval exists

## Gates

- Local gate: `npm run validate`, `npm run validate:manifests`, `npm run validate:prompt-ids`, `npm test`
- CI gate: GitHub Actions `Validate registry` runs `npm run validate` only
- Release gate: local `npm test` before merging registry edits that add or change prompt ids or target routing
- Support gate: Hub registry sync and runtime dispatch checks remain Hub-owned
- Manual gate: private sibling-repo CI access, non-manual trigger activation, confidential target activation, and production dispatch changes require explicit approval

## Evidence

- Evidence path: local command output, GitHub Actions logs, and DTP evidence receipts
- Latest receipt: see `practice-os/efficiency/hub-registry-evidence-index.md`
- Proof eligibility: internal operating evidence only; not public proof by default
- Redaction rule: do not publish target routing, private repo intent, or disabled/confidential automation plans as public proof without review

## Automation

- Safe read commands: `rg`, `git status`, `git diff`, `npm run validate`, `npm run validate:manifests`, `npm run validate:prompt-ids`, `npm test`
- Safe write commands: registry docs, validation scripts, and target entries only when the registry lane is active
- Commands that need explicit approval: private sibling checkout tokens, CI access expansion, non-manual target activation, production dispatch changes, or confidential target enablement
- Dependency maintenance: keep lightweight; registry validation dependencies are repo-local
- Toolchain pinning: Node 22 through `package.json` engines and GitHub Actions setup-node

## Next Touch

- Lane: local-first prompt/registry validation and future CI-access decision
- Trigger: new Hub target, prompt id change, registry schema change, sibling manifest drift, or repeated local-only validation friction
- Blocker: private sibling-repo CI access is intentionally deferred; local `npm test` remains the full cross-repo validation gate
- Next action: keep repo-scoped CI thin and decide sibling CI access only if local-first validation becomes a real bottleneck
