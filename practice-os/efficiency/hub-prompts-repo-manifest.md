---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Repo Manifest: hub-prompts

## Identity

- Repo: `hub-prompts`
- GitHub repo: `Toni-Montez-Consulting/hub-prompts`
- Local path: `hub-prompts`
- Primary role: Hub prompt catalog with versioned Markdown prompt definitions, prompt schemas, validation scripts, and future eval/golden-test fixtures
- Owner lane: prompt catalog and prompt-quality infrastructure
- Public/private: private/internal platform repo with no client-private prompt inputs committed by default
- Deploy target: none; Hub consumes this repo during prompt sync

## Boundaries

- Owns: prompt Markdown, prompt ids, prompt metadata, prompt schema expectations, Phase 0 consulting prompt checks, and future prompt eval fixtures
- Does not own: Hub runtime execution, Hub automation target routing, DTP practice roadmap, public proof, client engagement kits, or repo dispatch policy
- Sensitive data: prompt text, diagnostic framing, expected output schemas, prompt change history, and any future golden examples
- COI/privacy notes: prompts must stay general or redacted; do not commit customer data, private client facts, raw conversations, or Microsoft-adjacent confidential material

## Gates

- Local gate: `npm test`
- CI gate: GitHub Actions `Validate Prompts` runs `npm test` on push and pull request
- Release gate: prompt id, frontmatter, version, owner, expected output, golden-test, and change-log validation before prompt sync reliance
- Support gate: Hub prompt sync and runtime checks remain Hub-owned, not `hub-prompts`-owned
- Manual gate: new high-impact prompt behavior needs owner review, versioning judgment, and future eval/golden fixture review before runtime reliance

## Evidence

- Evidence path: local command output, GitHub Actions logs, and DTP evidence receipts
- Latest receipt: see `practice-os/efficiency/hub-prompts-evidence-index.md`
- Proof eligibility: internal operating evidence only; not public proof by default
- Redaction rule: never publish prompt fixtures, examples, or golden tests that include private client facts, private repo data, customer material, or unapproved business details

## Automation

- Safe read commands: `rg`, `git status`, `git diff`, `npm run validate`, `npm run validate:phase0`, `npm test`
- Safe write commands: prompt docs, schemas, validation scripts, and eval fixtures only when the prompt lane is active
- Commands that need explicit approval: changing production-critical prompt behavior, adding private examples, publishing prompt-derived proof, or wiring new runtime automation
- Dependency maintenance: keep lightweight; prompt validation dependencies are repo-local
- Toolchain pinning: Node 22 through `package.json` engines and GitHub Actions setup-node

## Next Touch

- Lane: prompt eval and quality fixtures
- Trigger: new prompt, prompt schema change, high-value prompt eval request, Hub prompt sync drift, or prompt id coordination with `hub-registry`
- Blocker: no blocker for catalog validation; runtime proof still depends on Hub-owned execution evidence
- Next action: add eval/golden fixtures only when real prompt misfires or high-value workflows justify them
