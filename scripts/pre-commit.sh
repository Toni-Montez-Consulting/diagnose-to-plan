#!/usr/bin/env bash
set -euo pipefail

branch="$(git branch --show-current 2>/dev/null || true)"
if [[ "$branch" == "main" || "$branch" == "master" ]]; then
  echo "blocked git commit on protected branch: $branch" >&2
  exit 2
fi

blocked=0
staged_files="$(git diff --cached --name-only --diff-filter=ACM)"

if [ -n "$staged_files" ]; then
  while IFS= read -r file; do
    [ -z "$file" ] && continue
    content="$(git show ":$file" 2>/dev/null || true)"
    if printf '%s\n' "$content" | sed -n '1,40p' | grep -Eiq '^confidential:[[:space:]]*true[[:space:]]*$'; then
      echo "blocked confidential staged artifact: $file" >&2
      blocked=1
    fi
  done <<< "$staged_files"
fi

if command -v gitleaks >/dev/null 2>&1; then
  gitleaks protect --staged --redact
elif [ -n "$staged_files" ]; then
  patterns_file=".dtp/scrub-patterns.txt"
  while IFS= read -r pattern || [ -n "$pattern" ]; do
    [[ -z "$pattern" || "$pattern" == \#* ]] && continue
    while IFS= read -r file; do
      [ -z "$file" ] && continue
      [ "$file" = ".dtp/scrub-patterns.txt" ] && continue
      [ "$file" = ".gitleaks.toml" ] && continue
      if git show ":$file" 2>/dev/null | grep -Eq "$pattern"; then
        echo "blocked potential secret in staged file: $file" >&2
        blocked=1
      fi
    done <<< "$staged_files"
  done < "$patterns_file"
fi

exit "$blocked"
