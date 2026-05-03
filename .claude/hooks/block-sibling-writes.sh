#!/usr/bin/env bash
set -euo pipefail

payload="${CLAUDE_TOOL_INPUT:-}"
if [ -z "$payload" ] && [ ! -t 0 ]; then
  payload="$(cat)"
fi

repo_root="$(git rev-parse --show-toplevel 2>/dev/null || pwd -P)"
export DTP_HOOK_PAYLOAD="$payload"

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

run_python - "$repo_root" <<'PY'
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

repo_root = Path(sys.argv[1]).resolve()
payload = os.environ.get("DTP_HOOK_PAYLOAD", "")

try:
    data = json.loads(payload) if payload else {}
except json.JSONDecodeError:
    data = {}


def walk(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key in {"file_path", "path", "notebook_path"} and isinstance(child, str):
                yield child
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


for raw_path in walk(data):
    candidate = Path(raw_path)
    target = (candidate if candidate.is_absolute() else repo_root / candidate).resolve()
    try:
        target.relative_to(repo_root)
    except ValueError:
        print(f"blocked write outside repo root: {target}", file=sys.stderr)
        raise SystemExit(2)
PY
