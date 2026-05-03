from __future__ import annotations

from pathlib import Path
from typing import Any


def split_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text

    end = text.find("\n---", 4)
    if end == -1:
        return {}, text

    raw_metadata = text[4:end]
    body = text[end + 4 :].strip()
    metadata: dict[str, Any] = {}
    for line in raw_metadata.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = _parse_scalar(value.strip())
    return metadata, body


def _parse_scalar(value: str) -> Any:
    cleaned = value.strip().strip('"').strip("'")
    lowered = cleaned.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered in {"null", "none"}:
        return None
    return cleaned
