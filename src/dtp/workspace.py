from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, ConfigDict


class WorkspaceRepo(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str
    path: Path
    access: str = "read"


class Workspace(BaseModel):
    model_config = ConfigDict(frozen=True)

    repos: tuple[WorkspaceRepo, ...] = ()


def load_workspace(path: Path) -> Workspace:
    """Load the small workspace file without taking a hard dependency on YAML."""

    if not path.exists():
        return Workspace()

    repos: list[WorkspaceRepo] = []
    current: dict[str, str] | None = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line == "repos:":
            continue
        if line.startswith("- "):
            if current:
                repos.append(_repo_from_mapping(current, path.parent.parent))
            current = _parse_inline_mapping(line[2:])
            continue
        if current is not None and ":" in line:
            key, value = line.split(":", 1)
            current[key.strip()] = value.strip()

    if current:
        repos.append(_repo_from_mapping(current, path.parent.parent))

    return Workspace(repos=tuple(repos))


def _parse_inline_mapping(text: str) -> dict[str, str]:
    if ":" not in text:
        return {}
    key, value = text.split(":", 1)
    return {key.strip(): value.strip()}


def _repo_from_mapping(mapping: dict[str, str], repo_root: Path) -> WorkspaceRepo:
    name = mapping.get("name")
    raw_path = mapping.get("path")
    if not name or not raw_path:
        raise ValueError("workspace repo entries require name and path")

    repo_path = Path(raw_path)
    if not repo_path.is_absolute():
        repo_path = (repo_root / repo_path).resolve()

    return WorkspaceRepo(name=name, path=repo_path, access=mapping.get("access", "read"))
