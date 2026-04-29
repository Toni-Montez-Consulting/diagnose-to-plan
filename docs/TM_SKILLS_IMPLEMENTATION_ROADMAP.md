# tm-skills Implementation Roadmap

This is the implementation handoff for `tm-skills`, Toni's cross-tool SDLC skills library.

Use this doc when starting the build from a fresh chat. The original build spec was reviewed on 2026-04-29 and accepted as a high-leverage addition. This doc turns that spec into a practical build path that fits the current DTP, consulting, Hub, Omnexus, Brother, Cam, and Greg roadmap.

## Purpose

`tm-skills` is a version-controlled personal skills repo for reusable software-development behavior across coding agents.

It should make future agent sessions better at:

- reviewing code without generic review theater;
- building frontend surfaces with craft and domain fit;
- drawing backend boundaries before adding persistence or services;
- choosing test coverage proportional to risk;
- finishing work with validation, repo hygiene, and handoff quality.

It is not a consulting CRM, client vault, DTP replacement, or public product.

## Relationship To Existing Repos

| Layer | Owns | Does Not Own |
|---|---|---|
| `diagnose-to-plan` | Practice OS, consulting methodology, Client Operating Kits, redaction, COI, case-study promotion, hosted DTP roadmap | Generic coding-agent SDLC behavior |
| `tm-skills` | Cross-repo SDLC skills, global coding-agent instructions, trigger evals, local install/doctor scripts | Client records, consulting pricing, SOWs, proof packets |
| `consulting` | Public storefront, public proof, `/start`, noindex `/admin` command room | Private skill library, private engagement kits |
| `hub` | Intake/runtime records, private console, Supabase/Vercel runtime | DTP cockpit, skills library |
| Project repos | Actual app/site delivery and proof evidence | Practice-wide roadmap |

The clean boundary is:

- DTP teaches the practice what to do with clients.
- `tm-skills` teaches coding agents how to build software with Toni's standards.
- Project repos consume both when relevant.

## Current Local State

Verified on 2026-04-29:

- `C:\Users\tonimontez\.codex\skills` exists.
- `C:\Users\tonimontez\.agents\skills` does not exist yet.
- `C:\Users\tonimontez\.claude\skills` does not exist yet.
- `C:\Users\tonimontez\.copilot\skills` does not exist yet.
- `C:\Users\tonimontez\.codex\AGENTS.md` exists.
- `C:\Users\tonimontez\.claude\CLAUDE.md` does not exist yet.
- `C:\Users\tonimontez\.copilot\copilot-instructions.md` does not exist yet.

Implementation rule: do not delete, move, or overwrite existing global instructions or skill folders. The installer must detect them and either preserve, merge, or require an explicit `--force`.

## Official Discovery Model To Use

Re-check these docs during implementation because tool behavior can change:

- Codex Agent Skills: `https://developers.openai.com/codex/skills`
- Codex AGENTS.md guidance: `https://developers.openai.com/codex/guides/agents-md`
- Claude Code skills: `https://code.claude.com/docs/en/skills`
- Claude Code memory: `https://code.claude.com/docs/en/memory`
- GitHub Copilot agent skills: `https://docs.github.com/en/copilot/concepts/agents/about-agent-skills`
- GitHub Copilot add skills: `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills`
- GitHub Copilot custom instructions: `https://docs.github.com/copilot/how-tos/custom-instructions`

Current target paths:

- Codex user skills: `$HOME/.agents/skills`
- Codex repo skills: `<repo>/.agents/skills`
- Codex global guidance: `$HOME/.codex/AGENTS.md`
- Claude user skills: `$HOME/.claude/skills`
- Claude repo skills: `<repo>/.claude/skills`
- Claude global guidance: `$HOME/.claude/CLAUDE.md`
- Copilot personal skills: `$HOME/.copilot/skills` or `$HOME/.agents/skills`
- Copilot project skills: `<repo>/.github/skills`, `<repo>/.claude/skills`, or `<repo>/.agents/skills`
- Copilot repo instructions: `<repo>/.github/copilot-instructions.md`

Codex and Copilot support `$HOME/.agents/skills`, so Phase 1 should make that the shared personal skills path. Keep existing `C:\Users\tonimontez\.codex\skills` as legacy/local context and have the doctor report it.

## Recommended Repo Home

Use a separate repo:

```text
C:\Users\tonimontez\tm-skills
```

If Toni explicitly wants a `dev` folder, `C:\Users\tonimontez\dev\tm-skills` is also acceptable. Pick one path once, then make every symlink and script use that path consistently.

## Repo Layout

```text
tm-skills/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── decisions/
│   ├── 0001-separate-from-dtp.md
│   └── 0002-global-vs-project-pinned-install.md
├── instructions/
│   └── global/
│       ├── AGENTS.md
│       ├── CLAUDE.md
│       └── copilot-instructions.md
├── skills/
│   ├── review-checklist/
│   │   ├── SKILL.md
│   │   └── evals/
│   │       ├── trigger.json
│   │       └── output.md
│   ├── frontend-craft/
│   ├── backend-design/
│   ├── testing-ladder/
│   └── delivery-baseline/
├── scripts/
│   ├── doctor.ps1
│   ├── install.ps1
│   └── freshness-check.ps1
├── manifest.json
└── MISFIRES.md
```

Prefer PowerShell scripts for this Windows machine. If Bash scripts are added later, they should be secondary wrappers, not the only path.

## Phase 1 Skills

### review-checklist

Use for code review, PR review, self-review, regression checks, and "review this" requests.

Default behavior:

- lead with findings;
- order by severity;
- reference file and line when possible;
- separate bugs, risk, missing tests, and open questions;
- do not pad with generic compliments.

Expected output:

- findings first;
- open questions;
- test gaps or residual risk;
- concise summary only after issues.

### frontend-craft

Use for UI polish, responsive layout, visual QA, interaction quality, and domain-fit design.

Default behavior:

- inspect the existing design system before inventing a new look;
- keep operational tools dense, calm, and usable;
- use real assets or meaningful generated assets when a website needs visual proof;
- verify desktop and mobile behavior when changing visible UI.

Expected output:

- implemented UI or a specific craft plan;
- design constraints followed;
- viewport/browser checks when practical.

### backend-design

Use before adding APIs, persistence, auth, queues, storage, background jobs, or service boundaries.

Default behavior:

- understand the existing data model and runtime first;
- choose the smallest durable boundary that supports the workflow;
- keep secrets out of code and logs;
- avoid building a platform when a local module or table is enough.

Expected output:

- proposed boundary;
- data contract;
- failure modes;
- migration or rollout notes.

### testing-ladder

Use when adding or changing tests, choosing verification depth, fixing flaky coverage, or preparing release confidence.

Default behavior:

- match test depth to risk;
- prefer deterministic tests before broad E2E;
- name manual gates when automation cannot cover them;
- keep Windows/local constraints visible.

Expected output:

- test choices and rationale;
- commands to run;
- what remains manual.

### delivery-baseline

Use for commits, branches, CI, deploys, release gates, repo hygiene, and handoff.

Default behavior:

- verify before calling work done;
- do not revert unrelated changes;
- keep dirty-worktree state explicit;
- produce a clear handoff with commands run and remaining gates.

Expected output:

- validation summary;
- files changed;
- commit/push/deploy state;
- next manual gates.

## Always-On Instruction Floor

Always-on rules belong in global instruction files, not in Phase 1 skills.

Minimum floor:

- Work with Toni as a creative technical partner.
- Read the actual repo before making architectural claims.
- Prefer implementation when the request is concrete.
- Never commit secrets.
- Never revert unrelated user changes.
- If work is consulting-adjacent, client-adjacent, Microsoft-adjacent, or involves Azure, Copilot, M365, Purview, or a Microsoft customer, pause and run the DTP COI screen before scoping or coding.

Do not create a Phase 1 `compliance-coi` skill. DTP remains the full COI system.

## Install Modes

### Mode A: Global-Only First

Start here.

Target links:

```text
$HOME/.agents/skills -> <tm-skills>/skills
$HOME/.claude/skills -> <tm-skills>/skills
$HOME/.copilot/skills -> <tm-skills>/skills
```

Global instruction files:

```text
$HOME/.codex/AGENTS.md
$HOME/.claude/CLAUDE.md
$HOME/.copilot/copilot-instructions.md
```

Do not replace existing files by default. `install.ps1` should print a diff/merge note and stop unless `--force` is provided.

### Mode B: Project-Pinned Canary

Use only after global discovery works.

Pick one repo as the canary and add a small checked-in pointer:

```text
<repo>/.tm-skills/
<repo>/.agents/skills
<repo>/.claude/skills
<repo>/.github/skills
```

Do not casually run duplicate global and project-pinned skills with the same names. Codex can show duplicates instead of merging them, so the doctor must report duplicate skill names.

## Trigger Evals

Each skill gets:

```text
skills/<skill>/evals/trigger.json
skills/<skill>/evals/output.md
```

`trigger.json` should include prompts that should trigger the skill and prompts that should not. `output.md` should describe the expected behavior, not a brittle exact transcript.

`MISFIRES.md` records real misses:

```markdown
## YYYY-MM-DD

- Prompt:
- Expected skill:
- Actual behavior:
- Fix:
```

This makes the skills iterate on real usage instead of becoming frozen commandments.

## Manifest And Freshness

`manifest.json` should track each skill:

- name;
- version;
- last reviewed date;
- review cadence days;
- source files;
- eval files;
- owner;
- status.

`freshness-check.ps1` should report stale skills without editing them automatically.

## Doctor Requirements

`scripts/doctor.ps1` should check:

- every Phase 1 skill has `SKILL.md`;
- every `SKILL.md` has `name` and `description`;
- descriptions include clear trigger words;
- skill body is concise enough for progressive disclosure;
- eval files exist;
- `manifest.json` references real files;
- `MISFIRES.md` exists;
- Windows symlink targets resolve;
- existing global instruction files are not overwritten;
- existing legacy/current skill dirs are reported, especially `C:\Users\tonimontez\.codex\skills`;
- duplicate skill names are reported across global and project paths;
- no Phase 1 `compliance-coi` skill exists.

## Build Sequence

1. Create the separate `tm-skills` repo.
2. Add `README.md`, root `AGENTS.md`, root `CLAUDE.md`, and the two decision records.
3. Add `instructions/global/AGENTS.md`, `CLAUDE.md`, and `copilot-instructions.md`.
4. Create the five Phase 1 skill folders.
5. Author concise `SKILL.md` files with strong descriptions and practical workflows.
6. Port any existing mature PR review prompt into `review-checklist` if present.
7. Add trigger evals and expected-output notes.
8. Add `MISFIRES.md`.
9. Add `manifest.json`.
10. Add `doctor.ps1`, `install.ps1`, and `freshness-check.ps1`.
11. Run the doctor before installing anything globally.
12. Install global symlinks only when the doctor confirms the target state.
13. Restart or reload each tool as needed.
14. Run discovery smoke tests in Codex, Claude Code, and GitHub Copilot.
15. Add one project-pinned canary only after global discovery works.
16. Commit and push the repo.
17. Update this roadmap with what actually shipped.

## Smoke Tests

Run equivalent prompts in Codex, Claude Code, and GitHub Copilot.

Discovery:

```text
What skills do you have available for software development?
```

Review:

```text
Please review this diff for regressions, missing tests, and release risk.
```

Frontend:

```text
Polish this dashboard UI so it feels like a serious operator tool on desktop and mobile.
```

Backend:

```text
Before coding, design the smallest backend boundary for saving engagement artifacts with auth and audit history.
```

Testing:

```text
Choose the right test ladder for this feature and tell me what commands to run.
```

Delivery:

```text
Validate this branch, summarize repo state, and prepare it for commit and push.
```

Compliance floor:

```text
This is for a consulting client that uses Azure and Copilot. Start building the automation.
```

Expected behavior: the agent should pause and route to the DTP COI screen before scoping or coding.

## Acceptance Criteria

- `tm-skills` exists as a separate repo.
- The five Phase 1 skills exist and are discoverable.
- No Phase 1 `compliance-coi` skill exists.
- Always-on global instructions include the Microsoft/COI floor and point to DTP.
- Doctor passes before global install.
- Installer does not overwrite existing files without explicit force.
- `MISFIRES.md`, `manifest.json`, and eval files exist.
- Smoke tests pass in Codex first, then Claude Code and GitHub Copilot.
- DTP roadmap includes `tm-skills` as a sibling SDLC layer.

## Deferred

- Multi-user skill product.
- Public skill marketplace.
- Self-rewriting skills.
- Skill telemetry beyond local evals and `MISFIRES.md`.
- DTP `skills-keeper` automation before there is real misfire/update history.
- Stack overlays before the five base skills prove useful.

## Implementation Prompt For A Future Chat

Paste this into a fresh chat from the DTP repo:

```text
Please implement the tm-skills roadmap. Start by reading diagnose-to-plan/docs/PRACTICE_PRODUCTION_ROADMAP.md, diagnose-to-plan/docs/DOCUMENTATION_MAP.md, and diagnose-to-plan/docs/TM_SKILLS_IMPLEMENTATION_ROADMAP.md. Then create the separate tm-skills repo, scaffold the five Phase 1 skills, add evals, MISFIRES.md, manifest.json, PowerShell doctor/install/freshness scripts, and run the doctor before any global install. Do not overwrite existing global instruction files or legacy skill folders. Keep DTP as the consulting Practice OS and tm-skills as the cross-repo SDLC skills layer. After implementation, summarize validation, repo state, and any manual install steps that remain.
```
