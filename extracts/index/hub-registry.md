# hub-registry index

- Repo slug: `hub-registry`
- Repo path: `C:\Users\tonimontez\hub-registry`
- Indexed at: `2026-04-29T14:05:35Z`
- Primary language: `Unknown`
- Files: `11`

## Signals

- `prompt-registry`: Prompt registry, parser, dispatcher, or prompt packs (9 files)
- `mcp-config`: MCP configuration or tools (2 files)
- `permission-tiers`: Tiered permissions or access policy (6 files)
- `cron-schedule`: Scheduled jobs (6 files)

## JSON

```json
{
  "repo_slug": "hub-registry",
  "repo_name": "hub-registry",
  "repo_path": "C:\\Users\\tonimontez\\hub-registry",
  "indexed_at": "2026-04-29T14:05:35Z",
  "git": {
    "first_commit_date": "2026-04-21",
    "last_commit_date": "2026-04-28",
    "total_commits": 15,
    "active_branches": [
      "main"
    ],
    "current_head": "4af0df1e",
    "uncommitted_changes": 0
  },
  "stack": {
    "primary_language": "Unknown",
    "frameworks": [],
    "package_managers": [
      "npm"
    ],
    "config_files": [
      "package.json"
    ]
  },
  "tree": {
    "depth_2_dirs": [
      ".github/",
      ".github/workflows/",
      ".repo.yml/",
      "README.md/",
      "SCHEMA.md/",
      "docs/",
      "docs/PLAYBOOK.md/",
      "docs/PORTFOLIO_REGISTRY_PHASE_0_1.md/",
      "package-lock.json/",
      "package.json/",
      "scripts/",
      "scripts/validate-manifests.mjs/",
      "scripts/validate-registry.mjs/",
      "targets.yml/"
    ],
    "notable_files": [
      "README.md",
      "docs/PLAYBOOK.md",
      "docs/PORTFOLIO_REGISTRY_PHASE_0_1.md"
    ]
  },
  "signals": [
    {
      "name": "prompt-registry",
      "evidence": "Prompt registry, parser, dispatcher, or prompt packs",
      "files": [
        ".github/workflows/validate.yml",
        ".repo.yml",
        "README.md",
        "docs/PORTFOLIO_REGISTRY_PHASE_0_1.md",
        "package-lock.json",
        "package.json",
        "scripts/validate-manifests.mjs",
        "scripts/validate-registry.mjs",
        "targets.yml"
      ]
    },
    {
      "name": "mcp-config",
      "evidence": "MCP configuration or tools",
      "files": [
        "README.md",
        "SCHEMA.md"
      ]
    },
    {
      "name": "permission-tiers",
      "evidence": "Tiered permissions or access policy",
      "files": [
        ".github/workflows/validate.yml",
        ".repo.yml",
        "docs/PORTFOLIO_REGISTRY_PHASE_0_1.md",
        "package-lock.json",
        "scripts/validate-manifests.mjs",
        "scripts/validate-registry.mjs"
      ]
    },
    {
      "name": "cron-schedule",
      "evidence": "Scheduled jobs",
      "files": [
        "README.md",
        "SCHEMA.md",
        "package-lock.json",
        "package.json",
        "scripts/validate-registry.mjs",
        "targets.yml"
      ]
    }
  ],
  "size": {
    "total_files": 11,
    "code_files": 11,
    "total_loc": 974
  }
}
```
