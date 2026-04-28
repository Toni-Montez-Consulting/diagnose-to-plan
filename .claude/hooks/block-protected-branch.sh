#!/usr/bin/env bash
set -euo pipefail

payload="${CLAUDE_TOOL_INPUT:-}"
if [ -z "$payload" ] && [ ! -t 0 ]; then
  payload="$(cat)"
fi

run_python() {
  if [ -n "${DTP_PYTHON:-}" ]; then
    "$DTP_PYTHON" "$@"
  elif command -v python >/dev/null 2>&1; then
    python "$@"
  elif command -v python3 >/dev/null 2>&1; then
    python3 "$@"
  elif command -v py >/dev/null 2>&1; then
    py -3 "$@"
  else
    echo "python not found for DTP hook" >&2
    exit 127
  fi
}

command="$(DTP_HOOK_PAYLOAD="$payload" run_python - <<'PY'
from __future__ import annotations

import json
import os

payload = os.environ.get("DTP_HOOK_PAYLOAD", "")
try:
    data = json.loads(payload) if payload else {}
except json.JSONDecodeError:
    data = {}

if isinstance(data, dict):
    value = data.get("command") or data.get("tool_input", {}).get("command", "")
    print(value if isinstance(value, str) else "")
PY
)"

if [[ "$command" != *"git commit"* ]]; then
  exit 0
fi

branch="$(git branch --show-current 2>/dev/null || true)"
if [[ "$branch" == "main" || "$branch" == "master" ]]; then
  echo "blocked git commit on protected branch: $branch" >&2
  exit 2
fi
