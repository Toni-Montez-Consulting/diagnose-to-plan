# Build Spec: `dtp` — Personal AI Consulting Harness (V2)

**Operator:** Toni Montez
**Purpose:** Single-user CLI harness that lives next to `tonimontez.co`, `demariomontezpb.com`, Omnexus, and future client repos in one VS Code workspace. The repo IS the practice's memory: every meaningful conversation produces a durable artifact.
**Audience for this document:** A coding agent (Codex, Claude Code, or Cursor) executing sequentially. Toni will read it too.
**Status:** Historical V2 harness implementation spec. It is preserved for context, but the V2 foundation was promoted to `main` through PR #1 on 2026-05-03. The current production roadmap lives in `docs/PRACTICE_PRODUCTION_ROADMAP.md`. If this spec's local-only or no-cloud assumptions conflict with the hosted private DTP direction, follow the production roadmap.

---

## 0. Reading order for the implementing agent

Read sections 1, 12, and 13 first. That tells you what to do, in what order, and what NOT to do. Then read everything else top to bottom. Do not skip section 5 (multi-repo guardrails) — that's the section most likely to cause a real incident if implemented sloppily.

When in doubt, prefer the boring choice. This is a personal tool for a 3–5 client practice, not a platform.

---

## 1. Decision: extend `diagnose-to-plan` or start fresh

**Recommendation: extend `diagnose-to-plan`. Rename nothing on disk; the CLI binary stays `dtp`.**

The decision rule, stated so the agent can re-derive it if context drifts: extend when (a) the existing repo already contains durable artifacts (skills, prompts, voice samples, prior drafts), (b) the new scope is additive rather than architecturally incompatible, and (c) git history has value as practice memory. All three hold here.

V1 was Python + `claude-agent-sdk` + `typer` with three skills (`voice`, `pricing`, `sow`) and one command (`draft`). V2 keeps that stack, keeps those three skills verbatim, and adds eight commands plus four skills plus multi-repo awareness. Nothing in V1 needs to be torn out. The SOW skill, voice samples, and pricing logic are the most expensive artifacts in the repo and they carry over unchanged.

Starting fresh would force re-importing those files anyway, lose the git trail of voice iteration, and create a naming problem (the user has typed `dtp draft` enough times that re-training muscle memory is a tax). The only argument for fresh would be if the V1 directory layout fundamentally fought the new scope. It doesn't — V1 already has `skills/`, `prompts/`, `inputs/`, `outputs/`. We're adding siblings to those, not restructuring them.

**Action for the agent:** `git checkout -b v2/harness` on the existing `diagnose-to-plan` repo. All Phase 1 work lands on that branch. Do not delete or move anything in V1 until Phase 2 acceptance passes.

If you discover during Phase 1 that the V1 code is in worse shape than this spec assumes — e.g., the skills don't actually load, the typer entrypoint is broken — stop, file a one-paragraph note in `decisions/0001-v1-state.md`, and ask. Do not silently rewrite V1.

---

## 2. Stack recommendation

**Python 3.12 + `claude-agent-sdk` (Python) + `typer` + `rich`. Same as V1.**

The 2026 landscape, briefly: Anthropic ships `claude-agent-sdk` in both Python and TypeScript at near parity. The Python package added a top-level `skills` parameter to `ClaudeAgentOptions` that takes `"all"`, a list of skill names, or `[]`. It has built-in `Read`, `Write`, `Edit`, `Bash`, `Glob`, `Grep`, `WebSearch`, `WebFetch`, hooks, subagents, and MCP support. LangChain Deep Agents and OpenAI's Agents SDK are real options but neither buys this project anything. LangGraph's reducer/checkpoint sophistication is overkill for a single-user CLI. OpenAI Agents SDK would mean rebuilding the skills mechanism from scratch and giving up the file-first ergonomics that Claude Code and the Agent SDK share.

TypeScript would be a defensible choice if the harness needed to ship in the browser or share types with the Astro site. It doesn't. Python keeps the harness in the same language as the user's day job (Microsoft DS work) and the V1 code, and `typer` is the cleanest CLI ergonomics story in either ecosystem.

**Models:**
- **Default: `claude-sonnet-4-6` ($3/$15 per MTok, 1M context).** Sonnet 4.6 lands within ~1 point of Opus 4.6 on SWE-bench and matches it on computer-use benchmarks at one-fifth the cost. For drafting, critique, brainstorm, and review it is the right tool.
- **Escalate to `claude-opus-4-6` ($5/$25 per MTok, 1M context)** only inside `dtp coi` (high-stakes reasoning where missing a Microsoft-customer overlap is a career risk) and inside `dtp draft --deep` when the user explicitly opts into a deeper SOW pass.
- **`claude-haiku-4-5` ($1/$5 per MTok)** for `dtp note` classification and `dtp review` summarization. These are short, cheap, structured tasks.

Hard-code the model strings in `src/dtp/models.py` as constants. Do not let the agent pick its own model at runtime.

**No new heavy dependencies.** `typer`, `rich`, `pydantic`, `python-frontmatter`, `gitpython`, `claude-agent-sdk`. That's it. If you reach for `langchain`, `langgraph`, `crewai`, `chromadb`, `qdrant`, or anything with "vector" in the name during Phase 1–4, stop — that's an out-of-scope signal (see section 13).

---

## 3. Directory structure

```
diagnose-to-plan/
├── README.md                  # one-screen orientation, links to docs/
├── CLAUDE.md                  # advisory rules for any agent working in this repo
├── AGENTS.md                  # symlink to CLAUDE.md (cross-tool compatibility)
├── pyproject.toml
├── .env.example
├── .gitignore
├── .claude/
│   ├── settings.json          # hooks: branch guard, sibling-write guard, secret scan
│   └── hooks/
│       ├── block-sibling-writes.sh
│       ├── block-protected-branch.sh
│       └── scan-client-confidential.sh
├── docs/
│   ├── 01-architecture.md
│   ├── 02-commands.md
│   ├── 03-skills.md
│   └── 04-multi-repo.md
├── src/dtp/
│   ├── __init__.py
│   ├── __main__.py            # `python -m dtp`
│   ├── cli.py                 # typer app, command registration only
│   ├── models.py              # model name constants, token budgets
│   ├── config.py              # pydantic Settings, .env loader
│   ├── workspace.py           # sibling-repo discovery, read-only access
│   ├── git_safety.py          # commit/branch guards, repo-boundary checks
│   ├── capture.py             # file-naming, frontmatter, journal templates
│   ├── agent.py               # ClaudeAgentOptions builder, single shared loop
│   ├── skills_loader.py       # discover + validate SKILL.md frontmatter
│   └── commands/
│       ├── draft.py
│       ├── note.py
│       ├── client.py
│       ├── review.py
│       ├── critique.py
│       ├── brainstorm.py
│       ├── eval_cmd.py        # `eval` is a keyword
│       ├── coi.py
│       ├── skills_cmd.py
│       ├── story.py
│       └── mentor.py
├── skills/                    # loaded by claude-agent-sdk
│   ├── voice/SKILL.md         # carried over from V1
│   ├── pricing/SKILL.md       # carried over from V1
│   ├── sow/SKILL.md           # carried over from V1
│   ├── positioning/SKILL.md
│   ├── offerings/SKILL.md
│   ├── content/SKILL.md
│   └── compliance-coi/SKILL.md
├── prompts/                   # raw text prompts loaded by commands
│   ├── draft.system.md
│   ├── critique.system.md
│   ├── brainstorm.system.md
│   ├── review.weekly.md
│   └── coi.screen.md
├── journal/
│   ├── README.md              # "one line per idea, timestamped, never edit"
│   └── 2026/
│       └── 04/
│           └── 2026-04-28.md
├── clients/
│   ├── README.md              # max 3-5 active clients, capacity rule explained
│   ├── _template/             # scaffold for `dtp client new`
│   │   ├── README.md
│   │   ├── diagnose.md
│   │   ├── sow.md
│   │   ├── decisions/
│   │   ├── deliverables/
│   │   └── meta.yaml
│   └── ACTIVE.md              # human-edited list of active engagements
├── decisions/                 # ADR-lite, numbered
│   ├── 0001-stack.md
│   ├── 0002-multi-repo-access.md
│   └── 0003-model-defaults.md
├── omnexus/
│   └── stories/               # war-story log, one file per incident/insight
├── mentor-log/                # learning capture from senior practitioner shadowing
│   └── README.md
├── inputs/                    # paste raw diagnose notes, transcripts, etc. (gitignored except README)
│   └── README.md
├── outputs/                   # generated drafts before they move to clients/<name>/
│   └── README.md
├── evals/
│   ├── README.md
│   ├── voice/                 # 20 should-trigger / should-not-trigger pairs per skill
│   ├── coi/
│   ├── sow/
│   └── runner.py
└── tests/
    ├── unit/
    ├── integration/
    └── fixtures/
```

`inputs/` and `outputs/` exist in gitignore except for their READMEs. They're scratch surfaces. Anything worth keeping moves to `clients/<name>/` or `journal/`.

`clients/` is committed but each client folder has a `meta.yaml` flag `confidential: true` that triggers the pre-commit scan (section 9). Client *names* are fine in git; client *identifying detail* (full company names, contracts, financials) goes in files flagged confidential and gets scrubbed before push if `meta.yaml` says so. Decide per client during onboarding.

---

## 4. CLI command surface

Single binary: `dtp`. Installed via `pip install -e .` in dev. Every command exits 0 on success, 1 on user error (bad flags, missing file), 2 on safety abort (sibling-write blocked, COI flagged), 3 on agent/API failure.

Every command that mutates state writes a line to `.dtp/audit.log` with timestamp, command, args, exit code. That log is gitignored — it's local-only telemetry, not practice memory.

### `dtp draft` — proposal mode (the V1 command)

```
dtp draft INPUT_PATH [--client NAME] [--deep] [--skip-coi] [--out PATH]
```

Reads a Diagnose note from `INPUT_PATH` (default: most recent `inputs/diagnose-*.md`). Loads `voice`, `pricing`, `sow` skills. Produces a draft SOW in `outputs/<timestamp>-<slug>.md` unless `--out` or `--client` is given (in which case it lands in `clients/<name>/sow.md`).

`--deep` switches the model to Opus 4.6 for the SOW pass and increases the thinking budget.

`--skip-coi` is allowed but logs a warning and writes a `coi-skipped` marker into the output frontmatter. It exists for when Toni already ran `dtp coi` separately and doesn't want to double-bill.

By default, `dtp draft` invokes the COI screen as a precondition. If COI returns "flag," draft halts with exit 2 and writes the flag reason to `outputs/<timestamp>-coi-flag.md`.

Examples:
```bash
dtp draft inputs/diagnose-acme.md --client acme
dtp draft inputs/diagnose-acme.md --deep
dtp draft inputs/diagnose-acme.md --skip-coi --out /tmp/throwaway.md
```

### `dtp note` — journal capture

```
dtp note "TEXT"  [--tag TAG ...]
```

Appends a single line to `journal/YYYY/MM/YYYY-MM-DD.md`, timestamped to the second. Creates the file if missing. No agent call by default — this is fast, local, no network. Pass `--classify` to spend a Haiku call categorizing the note.

```bash
dtp note "Pricing anchor: $1500 retainer keeps churn-prone clients out"
dtp note "Idea: positioning page should lead with COI cleanly handled" --tag positioning
```

Exits 0 even if the daily file already has 200 lines. Journal is append-only forever.

### `dtp client` — CRM-lite

```
dtp client new NAME
dtp client list
dtp client status NAME
dtp client archive NAME
```

`new` scaffolds `clients/<name>/` from `clients/_template/` and refuses if `clients/ACTIVE.md` already lists 5 active clients. The cap is enforced. Refusal exits 1 with a message: "active client cap reached; archive one before adding."

`list` reads `ACTIVE.md` and prints the table. `status` summarizes the named client folder (uses Haiku). `archive` moves the folder to `clients/_archive/<name>/` and updates `ACTIVE.md`.

### `dtp review` — Friday/Sunday summaries

```
dtp review [--since DATE] [--mode friday|sunday]
```

`friday` mode: scans the week's journal entries, decision files, story log, and mentor-log; produces `reviews/YYYY-MM-DD-friday.md` with three sections: shipped, learned, next. Uses Sonnet 4.6.

`sunday` mode: longer, more reflective. Same inputs but adds the previous Friday review and surfaces unfinished threads. Writes `reviews/YYYY-MM-DD-sunday.md`.

Both modes are read-only against everything except `reviews/`.

### `dtp critique` — voice/positioning check

```
dtp critique PATH [--skill voice|positioning|both] [--inplace]
```

Reads the file, loads the named skills, returns critique to stdout. With `--inplace`, appends a `## Critique` section to the file rather than printing. Refuses to run on files outside the harness repo (see section 5).

### `dtp brainstorm` — content/positioning ideation

```
dtp brainstorm "TOPIC" [--skill positioning|content|offerings] [--n 5]
```

Streams `--n` distinct angles to stdout and writes a copy to `journal/brainstorms/YYYY-MM-DD-<slug>.md`. Brainstorms are journal artifacts, not outputs — they belong with the idea capture path.

### `dtp eval` — run evals

```
dtp eval [--skill SKILL] [--all]
```

Runs the JSON eval pairs in `evals/<skill>/` against the loaded skill. Reports trigger accuracy (should-trigger hit rate, should-not-trigger false positive rate). Exits 0 if accuracy ≥ 0.85 across all targeted skills, 1 otherwise. See section 11 for thresholds per skill.

### `dtp coi` — COI screen

```
dtp coi INPUT_PATH [--client NAME]
```

Loads `compliance-coi` skill. Reads the diagnose note (or any text file). Runs against Opus 4.6 with extended thinking. Output is a structured verdict:

```yaml
verdict: clear | flag | block
reason: <one sentence>
overlap_indicators: [<list>]
recommended_action: proceed | clarify_with_client | decline
```

Writes to `clients/<name>/coi-<timestamp>.md` if `--client` is set, otherwise `outputs/`. `verdict: block` exits 2.

### `dtp skills` — list loaded skills

```
dtp skills [--validate]
```

Lists every `skills/*/SKILL.md` with name, description first line, body line count, and frontmatter validation status. With `--validate`, fails (exit 1) if any skill violates the frontmatter constraints in section 4 of this spec.

### `dtp story` — Omnexus war-story capture

```
dtp story "TITLE" [--from PATH]
```

Creates `omnexus/stories/YYYY-MM-DD-<slug>.md` with a template (situation / decision / outcome / lesson). If `--from` is a file (e.g., a chat transcript), the agent extracts and structures. Otherwise opens `$EDITOR`.

### `dtp mentor` — mentor-log entry

```
dtp mentor "WHAT" [--mentor NAME] [--from PATH]
```

Creates `mentor-log/YYYY-MM-DD-<slug>.md`. Same shape as `dtp story` but framed for learning-from-shadowing rather than war-story. Distinct command because the audience and use are different — mentor entries feed the review summary differently.

---

## 5. Skills architecture

Skills are folders under `skills/` with one required file: `SKILL.md`. The frontmatter spec, derived from the Anthropic skills standard:

```markdown
---
name: voice                          # required, ≤64 chars, [a-z0-9-] only
description: Use this skill whenever the user is drafting, editing, or
  critiquing client-facing prose — proposals, emails, SOWs, positioning copy,
  LinkedIn posts, anything in Toni's operator voice. Enforces directness, no
  hedging, no buzzwords (leverage, synergy, AI-powered, 10x), prose over
  bullets, lead with the recommendation. Pushy: invoke this even if the user
  doesn't say "voice" explicitly.
allowed-tools: Read, Glob, Grep        # optional, narrows tool surface
---

# Voice

[body, <500 lines, structured as: when to use / rules / examples / anti-examples]
```

Required: `name`, `description`. The description is the trigger. Make it pushy — Anthropic's own guidance says skills under-trigger by default and the description should explicitly say "use this skill whenever…". Cap description at 1024 chars. Cap body at 500 lines; if a skill needs more, split into `references/` files referenced by path from the body.

Three loading levels:
1. **Metadata (always loaded):** ~100 tokens of name + description per skill into the system prompt.
2. **Body (loaded on trigger):** SKILL.md is read into context when the description matches the user request.
3. **References/scripts (loaded by demand):** files in `skills/<name>/references/` are read only when the body references them.

Implementation: `ClaudeAgentOptions(skills="all", setting_sources=["project"], cwd=str(repo_root))`. The SDK handles discovery. Don't reimplement skill loading.

### Skills to ship

| name | when it fires | notes |
|---|---|---|
| `voice` | drafting/editing client-facing prose | carry over from V1, do not modify in Phase 1 |
| `pricing` | computing retainer ranges, hourly equivalents, deliverable scoping | carry over from V1 |
| `sow` | producing SOW structure | carry over from V1 |
| `positioning` | positioning statements, offer pages, niche framing | new |
| `offerings` | productized offer scoping, packaging fixed/variable scope | new |
| `content` | LinkedIn / X / blog drafts, hooks, story structure | new |
| `compliance-coi` | screening for Microsoft-customer overlap and confidential-info bleed | new, escalates to Opus |

`compliance-coi` is the load-bearing skill for keeping Toni's FTE status safe. Its description should be the most pushy of the bunch and its body should explicitly enumerate: any Microsoft cloud customer named in public case studies; any account Toni has personally touched in his MSFT role (read from a local-only `~/.dtp/msft-touched.yaml` that is NOT in the repo); any prospect whose stack centers on Azure AI, Fabric, Power Platform consulting; any prospect requesting work that overlaps with services Microsoft sells directly.

Validate every SKILL.md on `dtp skills --validate`. The validator checks: frontmatter present, `name` and `description` non-empty, name regex, description ≤1024 chars, body ≤500 lines. Anything else is a warning, not a failure.

---

## 6. Multi-repo access architecture

This is the section to read carefully. The failure modes Toni named — stale data, accidental writes, client-confidential bleed, commits to wrong repo — are real and have caused incidents in other practitioners' setups.

**Recommendation: explicit allow-list of sibling read paths in `.dtp/workspace.yaml`, never write outside `repo_root`, two layers of defense (Python-level guard + Claude Code hook).**

### Discovery

`src/dtp/workspace.py` walks up from `repo_root` until it finds a directory containing more than one git repo as a child (the workspace root) or hits `$HOME`. Each discovered repo is registered if and only if it appears in `.dtp/workspace.yaml`:

```yaml
# .dtp/workspace.yaml — checked into git
workspace_root: ${WORKSPACE_ROOT:-../}
siblings:
  - path: tonimontez.co
    access: read
    purpose: site copy reference, voice samples
  - path: demariomontezpb.com
    access: read
    purpose: brother's site, structural reference only
  - path: omnexus-ios
    access: read
    purpose: war-story source material
client_repos:
  pattern: clients/*-repo/      # if a client gives source access, it lives here
  access: read
```

Anything not listed is invisible. Discovery is explicit — the harness does not auto-scan and auto-include.

### Read access pattern

When a command needs sibling content, it builds a `ClaudeAgentOptions` with `cwd=repo_root` and an explicit `add_dirs` list pulling from `workspace.yaml`. The SDK's filesystem tools honor `add_dirs` as additional roots. We layer an `allowed-tools` constraint that disables `Write` and `Edit` on those paths via a permission callback:

```python
async def repo_boundary_check(tool_name, tool_input, ctx):
    path = tool_input.get("path") or tool_input.get("file_path") or ""
    abs_path = Path(path).resolve()
    if tool_name in ("Write", "Edit", "MultiEdit"):
        if not is_inside(abs_path, repo_root):
            return PermissionResult(behavior="deny",
                reason=f"Write blocked: {abs_path} is outside {repo_root}")
    return PermissionResult(behavior="allow")
```

This goes on every command's options as `can_use_tool=repo_boundary_check`.

### Stale data

Sibling reads are real-time (filesystem, not cached). Stale-data risk comes from the agent assuming a file's content is current when the user has uncommitted changes elsewhere. Mitigation: at the start of any command that reads sibling repos, log the sibling repo's `git rev-parse HEAD` and the count of uncommitted changes (`git status --porcelain | wc -l`) into the command's audit line. If uncommitted-count > 0, print a warning to stderr: "sibling X has uncommitted changes; output may not match HEAD."

### Layer 2: Claude Code hook

`.claude/settings.json` adds a `PreToolUse` hook on `Write|Edit|MultiEdit` that runs `.claude/hooks/block-sibling-writes.sh`. The hook reads `$CLAUDE_TOOL_INPUT`, extracts the path, runs the same `is_inside(repo_root)` check in shell, and exits non-zero if the path is outside. This catches the case where the harness is being driven by Claude Code interactively, not via the `dtp` CLI.

### Commit boundary

The harness never runs `git commit` in a sibling repo. `src/dtp/git_safety.py` wraps every git operation and asserts `cwd == repo_root`. Branch operations: same. The only git surface area inside the harness is committing harness artifacts. If Toni wants a commit in `tonimontez.co`, he runs git himself.

### Failure modes, explicitly addressed

| failure | guard |
|---|---|
| stale data in sibling | git status check at command start, stderr warning |
| accidental write to sibling | python permission callback + Claude Code hook (two layers) |
| client-confidential leak in commit | pre-commit hook scans staged files for `confidential: true` frontmatter and string patterns from `.dtp/scrub-patterns.txt` |
| commit to wrong repo | `git_safety.py` asserts `cwd == repo_root`; `block-protected-branch.sh` blocks commits to `main` outside a feature branch |
| API key in committed file | pre-commit hook runs `gitleaks` if installed, else regex scan for `sk-ant-`, `AKIA`, common secret patterns |

---

## 7. Agent loop architecture

**Single-agent, single-process, one shared loop. No multi-agent orchestration.**

`src/dtp/agent.py` exposes one function:

```python
async def run(
    *,
    command: str,
    user_prompt: str,
    skills: list[str] | str = "all",
    model: str = SONNET_4_6,
    extended_thinking: bool = False,
    add_dirs: list[Path] | None = None,
    out_path: Path | None = None,
) -> RunResult:
    ...
```

It builds `ClaudeAgentOptions`, calls `query()` from `claude-agent-sdk`, streams messages through a `rich`-based renderer, persists the final result to `out_path` if given, and returns the structured result.

**Skill loading per command:**

| command | skills loaded | model | thinking |
|---|---|---|---|
| `draft` | voice, pricing, sow + compliance-coi (precondition) | Sonnet | off, on for `--deep` |
| `note` | none (no agent) or content (with `--classify`) | Haiku | off |
| `review` | voice + content | Sonnet | off |
| `critique` | voice, positioning (configurable) | Sonnet | off |
| `brainstorm` | positioning, offerings, content | Sonnet | off |
| `coi` | compliance-coi | Opus | on, budget=20k tokens |
| `story` | voice (light) | Sonnet | off |
| `mentor` | voice (light) | Sonnet | off |

Don't pass `skills="all"` to every command. Loading the metadata for unused skills is cheap (~100 tokens each) but loading the body via under-triggered descriptions is a real failure mode. Be explicit about which skills each command needs.

**Context window management:** Sonnet 4.6 has 1M context at standard pricing, so for this scale of personal tooling, do not implement a custom compaction layer. If a command would push >200K tokens (e.g., `dtp review --since 2026-01-01` after a year of journals), use Sonnet's beta context compaction flag rather than rolling your own. If even that overflows, bucket by month and summarize iteratively — but defer that until Phase 5 or later. It will not happen in V1.

**Tool selection:** rely on the SDK's built-ins (`Read`, `Glob`, `Grep`, `WebSearch`, `WebFetch`). Do not register custom MCP tools for V1. `Write` and `Edit` are gated by the permission callback in section 6.

---

## 8. MCP integration

**Recommendation: do not expose any MCP servers from this harness in V1. Optionally consume one read-only filesystem MCP server for siblings if the in-process `add_dirs` pattern proves limiting. Defer the decision to Phase 4.**

The reasoning: MCP solves the n×m integration problem across many clients and many servers. A single-user CLI does not have that problem. The Agent SDK already has filesystem access via `Read`/`Glob`/`Grep`/`Bash`, and the harness already constrains those via the permission callback. Adding an MCP layer on top adds another consent boundary, another process, another security surface. There's a real industry trend (visible in 2026 commentary) of MCP being over-applied — "why run a filesystem MCP server when your agent already has filesystem access?"

The exception: if you want a hard, OS-level read-only mount for sibling repos (so even a misbehaving agent literally cannot write to them), the `modelcontextprotocol/server-filesystem` package supports `--readonly` per-directory. That's worth considering in Phase 4 if any incident reveals the Python permission callback was bypassed. Until then, two layers of Python + hook is sufficient.

The harness will not expose its own MCP server. There is no second client.

---

## 9. Capture-pattern enforcement

The capture pattern — every meaningful conversation produces a durable artifact — is enforced by three mechanisms.

**File-naming convention:** every artifact-producing command writes to a path of the form `<area>/YYYY-MM-DD-<slug>.md` (or `<area>/YYYY/MM/YYYY-MM-DD.md` for the journal). The slug is generated from the command and a short hash of the input or first 4 words of the prompt. This means artifacts are sortable by area, then date, then specificity.

**Frontmatter on every generated file:**
```yaml
---
created: 2026-04-28T14:32:11-07:00
command: dtp draft
inputs: [inputs/diagnose-acme.md]
skills_loaded: [voice, pricing, sow, compliance-coi]
model: claude-sonnet-4-6
coi_verdict: clear
client: acme
confidential: false
---
```

`src/dtp/capture.py` writes this header on every generated file. The review command parses these headers to surface what was produced, when, and against what inputs.

**Pre-commit hook (`.git/hooks/pre-commit`, installed by `make install-hooks`):**
1. For every staged `.md` file under `clients/`, parse frontmatter. If `confidential: true`, abort the commit and print: "confidential client file staged: <path> — either flip the flag or unstage." This is intentional friction.
2. Run a regex pass for known leak patterns (full client legal names from `.dtp/scrub-patterns.txt`, API keys, MSFT internal codenames if listed locally). Abort on hit.
3. Run `dtp skills --validate` if any `skills/` file is staged.

The hook is bash, not Python, to keep startup time near zero. Toni will type `git commit` 50 times a week; the hook needs to be fast.

**Journal templates:** `dtp note` is intentionally ungated — no review, no validation. The friction-free path is the only path that gets used. The journal is the funnel; the review surfaces what's worth keeping.

**Review surfacing:** `dtp review` reads journal, decisions, stories, mentor-log, and the week's `outputs/` and `clients/*/` deltas (via git log on the harness repo). It does not edit those files. It produces a new artifact that summarizes them. That artifact is itself captured.

---

## 10. Git workflow

**Branches:** `main` is protected. All work happens on feature branches named `phase-N/<slug>` for build-sequence work, `feat/<slug>` for additive features after V1 ships, `fix/<slug>` for bugs. The branch-guard hook in `.claude/hooks/block-protected-branch.sh` blocks any `git commit` issued by an agent while `HEAD` is `main` or `master`.

**Commit messages:** Conventional Commits format. Imperative mood. No AI attribution lines. Explicitly: do not append `Co-authored-by: Claude <claude@anthropic.com>` or `🤖 Generated with Claude Code` or `Generated-by:` trailers. The commit message is Toni's voice; the agent is a tool.

```
feat(coi): add Opus-backed COI screen with structured verdict

- escalates to claude-opus-4-6 with 20k thinking budget
- writes verdict frontmatter to outputs/
- exits 2 on `block`, blocking dependent draft commands
```

**Per-step commits:** every phase in section 12 ends with a working commit. Within a phase, commit after each command's happy path passes its acceptance test. Don't squash before merge — the granular history is part of the practice memory.

**The harness never auto-commits to a sibling repo.** Section 6 enforces this. The harness does auto-stage and commit *its own* artifacts only when explicitly invoked with `dtp <cmd> --commit` (a flag that does not exist in V1; defer to Phase 5 if Toni wants it).

---

## 11. Environment and secrets

`.env` (gitignored) holds:

```bash
ANTHROPIC_API_KEY=sk-ant-...
DTP_HOME=/Users/toni/code/diagnose-to-plan
DTP_WORKSPACE_ROOT=/Users/toni/code
DTP_DEFAULT_MODEL=claude-sonnet-4-6
DTP_DEEP_MODEL=claude-opus-4-6
DTP_FAST_MODEL=claude-haiku-4-5
DTP_LOG_LEVEL=info
DTP_MSFT_TOUCHED_FILE=~/.dtp/msft-touched.yaml
```

`.env.example` ships in git with the keys and empty values.

`~/.dtp/msft-touched.yaml` is local-only, never in the repo. It holds the list of accounts/customers Toni has touched in his Microsoft role. The COI skill reads it. If it's missing, COI runs with a stderr warning and the verdict frontmatter sets `msft_touched_list: missing`.

Pydantic Settings (`config.py`) loads `.env`, validates types, and exposes a `Settings` singleton. No `os.getenv` calls anywhere else in the codebase.

---

## 12. Acceptance criteria

Per command. Each is testable. Each must pass before the phase that introduces it is considered done.

**`dtp draft`:**
- given a fixture diagnose note, produces a non-empty markdown SOW with the three V1 sections (scope, deliverables, pricing).
- frontmatter includes `coi_verdict`, `model`, `skills_loaded`.
- `--skip-coi` produces output with `coi_verdict: skipped`.
- when COI returns `block`, command exits 2 and writes a flag file, no SOW produced.

**`dtp note`:**
- runs in <200ms with no agent flags.
- creates `journal/YYYY/MM/YYYY-MM-DD.md` if missing.
- appends `HH:MM:SS — TEXT` line.
- with `--tag X`, appends `[X]` token to the line.

**`dtp client new`:**
- creates folder from template.
- refuses (exit 1) when 5 active clients are listed in `ACTIVE.md`.
- updates `ACTIVE.md`.

**`dtp review --mode friday`:**
- reads at least journal/, decisions/, omnexus/stories/, mentor-log/.
- output has three sections: shipped, learned, next.
- runs in <30s on a week of typical journal volume (≤200 entries).

**`dtp critique`:**
- refuses files outside `repo_root` with exit 2.
- with `--inplace`, appends `## Critique` section without modifying existing content.

**`dtp brainstorm`:**
- produces `--n` distinct angles (default 5).
- writes a copy to `journal/brainstorms/`.

**`dtp eval`:**
- runs all `evals/<skill>/*.json` pairs.
- per-skill threshold: trigger accuracy ≥ 0.85 (correct should-trigger) AND false-positive rate ≤ 0.15.
- exits 1 if any targeted skill misses threshold.
- writes `evals/results/YYYY-MM-DD-results.md`.

**`dtp coi`:**
- emits structured verdict (`clear` / `flag` / `block`) in YAML frontmatter.
- `block` exits 2.
- runs against Opus 4.6.
- when `~/.dtp/msft-touched.yaml` is missing, sets `msft_touched_list: missing` and warns.

**`dtp skills --validate`:**
- exits 0 when all SKILL.md files have valid frontmatter.
- exits 1 with a per-file diagnostic when any fails.

**`dtp story` / `dtp mentor`:**
- create file with the right template.
- frontmatter includes `command`, `created`.

**Multi-repo guards (cross-cutting):**
- writing to a sibling repo path raises a Python exception AND the Claude Code hook blocks the underlying tool call. Test by attempting `dtp critique ../tonimontez.co/index.md --inplace` — must exit 2.
- committing while `cwd != repo_root` raises in `git_safety.py`.
- committing to `main` is blocked by the hook.
- staging a file with `confidential: true` frontmatter blocks the commit.

---

## 13. Build sequence

Five phases. Each ends with a green test run and a working commit on `phase-N/...` merged into `v2/harness`. Do not start phase N+1 until phase N's acceptance criteria pass.

### Phase 1 — Foundation + V1 parity (2 working sessions)

1. Branch `phase-1/foundation` off current main.
2. Create directory structure from section 3 (empty READMEs in each).
3. Set up `pyproject.toml` with dependencies from section 2.
4. Port V1's `voice`, `pricing`, `sow` skills into `skills/` if not already there.
5. Implement `src/dtp/config.py`, `models.py`, `workspace.py` (stub: just reads `workspace.yaml`), `git_safety.py`.
6. Implement `src/dtp/agent.py` with the single `run()` function.
7. Implement `dtp draft` with V1 parity (no COI yet).
8. Implement `dtp skills` and `dtp skills --validate`.
9. Tests: unit on config + workspace + git_safety; integration on `dtp draft` against a fixture.
10. Commit, merge to `v2/harness`.

**Phase 1 ships when:** `dtp draft inputs/fixture-diagnose.md` produces a valid SOW with the three V1 skills loaded.

### Phase 2 — Capture path + safety layer (2 sessions)

1. Branch `phase-2/capture-and-safety`.
2. Implement `dtp note`, `dtp story`, `dtp mentor`.
3. Implement `src/dtp/capture.py` with the frontmatter helper.
4. Wire Capture into `dtp draft` so its outputs carry frontmatter.
5. Build the Claude Code hooks (`block-sibling-writes.sh`, `block-protected-branch.sh`, `scan-client-confidential.sh`).
6. Build the pre-commit hook bash script and `make install-hooks`.
7. Implement the `repo_boundary_check` permission callback and wire to all commands.
8. Tests: every guard from section 12's "Multi-repo guards" entry.
9. Commit, merge.

**Phase 2 ships when:** an attempted write to `../tonimontez.co/` is blocked by both layers and an attempted commit on main is blocked.

### Phase 3 — COI + client management (1.5 sessions)

1. Branch `phase-3/coi-and-clients`.
2. Author `skills/compliance-coi/SKILL.md`. Use the pushy description pattern. Reference `~/.dtp/msft-touched.yaml`.
3. Implement `dtp coi`. Wire Opus 4.6 + extended thinking.
4. Wire COI as a precondition into `dtp draft`. Honor `--skip-coi`.
5. Implement `dtp client new|list|status|archive`. Enforce the 5-cap.
6. Tests: COI returns structured verdict on three fixture cases (clear / flag / block); client cap refuses correctly.
7. Commit, merge.

**Phase 3 ships when:** `dtp coi` runs against three fixtures and produces correct verdicts, `dtp draft` halts on `block`, and `dtp client new` enforces capacity.

### Phase 4 — Review + critique + brainstorm + new skills (2 sessions)

1. Branch `phase-4/loops`.
2. Author `skills/positioning`, `skills/offerings`, `skills/content`.
3. Implement `dtp critique`, `dtp brainstorm`, `dtp review --mode friday`, `dtp review --mode sunday`.
4. Decide whether to add the read-only filesystem MCP server (section 8). Default: no. Document the decision in `decisions/0004-mcp.md` either way.
5. Tests per acceptance.
6. Commit, merge.

**Phase 4 ships when:** all five new commands pass acceptance and the four new skills validate.

### Phase 5 — Evals + polish (1 session)

1. Branch `phase-5/evals`.
2. Author 20 trigger pairs per skill in `evals/<skill>/`.
3. Implement `evals/runner.py` and `dtp eval`.
4. Run baseline; tune skill descriptions where false-positive or false-negative rates fail threshold.
5. Document results in `decisions/0005-eval-baseline.md`.
6. Update `README.md` and `docs/` with the final command surface.
7. Commit, merge `v2/harness` to `main` with a single squash-on-merge for cleanliness across the v2 boundary (do NOT squash within phases).

**Phase 5 ships when:** `dtp eval --all` exits 0.

After Phase 5, V2 is done. Stop. Don't keep adding.

---

## 14. Out of scope (explicit non-goals)

The following will not be built in this spec. If the implementing agent feels the urge to add any of them, that's the signal to stop and re-read this list.

- **Vector database, embeddings, RAG, semantic search.** The journal is small; grep is enough. The skills mechanism handles knowledge layering. Adding vectors adds operational surface area for zero benefit at this scale.
- **Multi-agent orchestration.** No Agent Squad, CrewAI, LangGraph, AutoGen, Strands subagent fanout. One agent loop, one process. The Agent SDK supports subagents; do not use them in V1.
- **Web UI.** The CLI is the UI. VS Code is the editor. There is no dashboard.
- **Auto-publishing.** Nothing posts to LinkedIn, X, Threads, or anywhere else. Brainstorm and content skills produce drafts; Toni publishes by hand.
- **Notion sync, Google Docs sync, Drive sync.** The repo is the source of truth.
- **Fine-tuning, custom model training, model hosting.** Use Anthropic's API. Do not build a model layer.
- **Cloud deployment.** This is a local CLI. No Docker (except optionally for the filesystem MCP server in Phase 4 if that path is taken). No Lambda. No Render. No Railway.
- **Billing, invoicing, contract execution, e-signature integration.** SOW drafts go to clients out-of-band. The harness does not touch money or signatures.
- **CRM beyond the file-based pattern.** No HubSpot, Pipedrive, Folk, Attio integration. `clients/` is the CRM.
- **Telemetry to anywhere off-machine.** `audit.log` is local-only. Nothing phones home.
- **An MCP server exposed by the harness.** Section 8 covers this.
- **Background daemons, file watchers, schedulers.** All commands are explicit and synchronous. If Toni wants a Friday review every Friday, he runs `dtp review --mode friday` on Friday. Cron is fine; building it into `dtp` is not.

If any of these become genuinely needed later, they get their own spec, their own branch, and a fresh decision document. They do not creep into V1.

---

## Appendix A — Research notes informing this spec (April 2026 state)

**Agent SDK landscape.** Anthropic's `claude-agent-sdk` ships in Python and TypeScript at near parity. Recent Python releases added a top-level `skills` parameter, SessionStore adapters at parity with TS, and OpenTelemetry support. LangChain Deep Agents and OpenAI Agents SDK are real alternatives but solve problems (multi-tenant deployment, sandbox-as-tool, parallel reducer state) that a single-user personal CLI does not have. Claude Agent SDK keeps the agent inside its execution sandbox, which is the right model when "the sandbox" is the user's own dev box.

**Skills.** The Agent Skills standard (now hosted at agentskills.io, governed openly with broad client adoption beyond Anthropic) requires `name` (≤64 chars, lowercase + hyphens) and `description` (≤1024 chars, no XML). Three loading levels: metadata always in context (~100 tokens), instructions on trigger (<5K tokens recommended), references/scripts on demand. Anthropic's own guidance is that skills *under-trigger* — be deliberately pushy in the description. Body capped at 500 lines for performance; split larger skills via reference files.

**Models.** Sonnet 4.6 (released Feb 17, 2026) lands within ~1 point of Opus 4.6 on SWE-bench Verified at 1/5 the cost ($3/$15 vs $5/$25 per MTok). Both ship with 1M context at standard pricing. Opus 4.6's clear lead is on PhD-level reasoning (GPQA Diamond: 91.3% vs 74.1%). For this harness, that gap matters only inside `dtp coi` — getting a Microsoft-customer-overlap call wrong is the only place where reasoning depth has career-level downside.

**MCP.** As of April 2026, MCP is the de facto AI tool-integration standard with broad client support and a large server ecosystem, but there is also active commentary that it is over-applied for cases the host already handles natively. For a single-user CLI with the Agent SDK's built-in filesystem tools, MCP adds surface area without adding capability. The exception is hard read-only enforcement on sibling repos via the official filesystem server — worth keeping as a Phase 4 option, not a default.

**Multi-repo guardrails.** The pattern that holds up in 2026 practitioner write-ups: explicit allow-listed read paths, explicit write paths, blocked paths, and two enforcement layers (in-process permission callback + Claude Code PreToolUse hook). Branch protection via hook (`branch-guard` pattern) is standard. Pre-commit secret scanning is standard. Using both belt and suspenders is the operator-grade default — relying only on the agent's politeness has a published incident record.
