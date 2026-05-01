---
data_class: P0
confidential: false
permission_level: internal_only
review_status: draft
---

# Repo Manifest: architected-strength

## Identity

- Repo: `architected-strength`
- GitHub repo: `Toni-Montez-Consulting/architected-strength`
- Local path: `architected-strength`
- Primary role: Toni's personal brand OS, content hub, networking engine, public proof lab, and personality-forward systems-thinking site
- Owner lane: personal brand OS and first assistant-pattern candidate
- Public/private: private source repo for a future public personal-brand site
- Deploy target: Azure-first static web/infra lane, with repo-local workflows controlling validation and deploy artifacts

## Boundaries

- Owns: public personal-brand site, Interactive OS theme, content/field-note/build/training publishing, source registry, claim ledger, agent policies, Notion-doc manifest, and repo-local validation gates
- Does not own: Toni Consulting service intake, DTP practice-wide roadmap, Hub runtime records, CCAAP launch records, Microsoft confidential material, client records, or private outreach data
- Sensitive data: private notes, employer/client confidential details, unsupported work claims, raw agent traces, Notion tokens/page IDs, private networking notes, and unpublished personal logs
- COI/privacy notes: Microsoft/work references must stay personal, public-safe, and non-confidential; the repo must not imply official Microsoft endorsement

## Gates

- Local gate: `pnpm run ci`
- CI gate: GitHub Actions Validate, Run Evals, and Deploy Web workflows on `main`
- Release gate: manual public-claim review against source registry and claim ledger; manual route/content review before public launch
- Support gate: keep roadmap, AGENTS.md, README, Notion docs manifest, and assistant lane aligned with the repo's personal-brand role
- Manual gate: publishing, outreach, proof claims, Notion writes, Azure production deployment, and assistant launch remain human-approved

## Evidence

- Evidence path: GitHub Actions logs, local `pnpm run ci`, `docs/roadmap/`, `docs/adr/`, agent policies, content/data validators, and DTP steward receipts
- Latest receipt: see `practice-os/efficiency/architected-strength-evidence-index.md`
- Proof eligibility: public-safe personal proof only; no private employer/client details or unsupported claims
- Redaction rule: do not publish raw traces, private notes, private networking records, private Hub/DTP material, or confidential Microsoft/client content

## Automation

- Safe read commands: `rg`, `git status`, `git diff`, `pnpm run doctor`, `pnpm run matrix`, `pnpm run verify:local`, `pnpm run ci`
- Safe write commands: repo docs, content, data contracts, site components, and validation scripts when the Architected Strength lane is active
- Commands that need explicit approval: Azure deployment, Notion write sync, public proof publication, outreach generation at send time, assistant runtime launch, and any secret/environment changes
- Dependency maintenance: keep private-source baseline stable; run full `pnpm run ci` before merge or release
- Toolchain pinning: pnpm/Astro/TypeScript/Bicep versions stay repo-local

## Next Touch

- Lane: cross-site assistant pattern and personal-brand publishing
- Trigger: assistant architecture acceptance, content publishing cadence, Notion docs sync, or public launch/deploy decision
- Blocker: assistant implementation needs an accepted site manifest, approved source corpus, refusal policy, analytics/logging plan, and human handoff path
- Next action: use `docs/CROSS_SITE_ASSISTANT_ARCHITECTURE_BRIEF.md` to scope the first public assistant pattern after CCAAP owner-input closure is moving
