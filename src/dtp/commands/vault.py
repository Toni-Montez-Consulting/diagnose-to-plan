from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

from dtp.config import DtpConfig
from dtp.git_safety import resolve_inside_repo


class VaultError(ValueError):
    pass


@dataclass(frozen=True)
class VaultStatus:
    root: Path
    exists: bool
    git_initialized: bool
    branch: str
    head: str
    dirty: bool
    remote: str

    @property
    def ready(self) -> bool:
        return self.exists and self.git_initialized

    @property
    def has_remote(self) -> bool:
        return bool(self.remote)


@dataclass(frozen=True)
class VaultSnapshotResult:
    status: VaultStatus
    committed: bool
    pushed: bool
    message: str


def run_vault_status(config: DtpConfig) -> VaultStatus:
    root = resolve_inside_repo(config.engagements_dir, config.repo_root)
    if not root.exists():
        return VaultStatus(
            root=root,
            exists=False,
            git_initialized=False,
            branch="",
            head="",
            dirty=False,
            remote="",
        )
    if not (root / ".git").exists():
        return VaultStatus(
            root=root,
            exists=True,
            git_initialized=False,
            branch="",
            head="",
            dirty=False,
            remote="",
        )
    return VaultStatus(
        root=root,
        exists=True,
        git_initialized=True,
        branch=_git(root, "branch", "--show-current", allow_empty=True).strip(),
        head=_git(root, "rev-parse", "--short", "HEAD", allow_empty=True).strip(),
        dirty=bool(_git(root, "status", "--porcelain", allow_empty=True).strip()),
        remote=_git(root, "remote", "get-url", "origin", allow_empty=True).strip(),
    )


def run_vault_init(config: DtpConfig, *, remote: str | None = None) -> VaultStatus:
    root = resolve_inside_repo(config.engagements_dir, config.repo_root)
    root.mkdir(parents=True, exist_ok=True)
    if not (root / ".git").exists():
        _git(root, "init", "-b", "main")
    if remote:
        existing = _git(root, "remote", "get-url", "origin", allow_empty=True).strip()
        if existing and existing != remote:
            raise VaultError(f"vault already has a different origin: {existing}")
        if not existing:
            _git(root, "remote", "add", "origin", remote)
    return run_vault_status(config)


def run_vault_snapshot(
    config: DtpConfig,
    *,
    message: str,
    push: bool = False,
) -> VaultSnapshotResult:
    status = run_vault_status(config)
    if not status.git_initialized:
        raise VaultError("private vault is not initialized; run `dtp vault init` first")

    _git(status.root, "add", "-A")
    dirty = bool(_git(status.root, "status", "--porcelain", allow_empty=True).strip())
    committed = False
    pushed = False
    if dirty:
        _git(
            status.root,
            "-c",
            "user.name=DTP Vault",
            "-c",
            "user.email=dtp-vault@example.local",
            "commit",
            "-m",
            message,
        )
        committed = True

    latest = run_vault_status(config)
    if push:
        if not latest.remote:
            raise VaultError("cannot push vault snapshot without an origin remote")
        _git(latest.root, "push", "-u", "origin", latest.branch or "main")
        pushed = True
        latest = run_vault_status(config)

    return VaultSnapshotResult(
        status=latest,
        committed=committed,
        pushed=pushed,
        message=message,
    )


def render_vault_status(status: VaultStatus, repo_root: Path) -> str:
    relative = status.root.relative_to(repo_root).as_posix()
    if not status.exists:
        return f"private vault: missing\n  path: {relative}\n  next: dtp vault init\n"
    if not status.git_initialized:
        return f"private vault: local files only\n  path: {relative}\n  next: dtp vault init\n"
    lines = [
        "private vault: ready",
        f"  path: {relative}",
        f"  branch: {status.branch or 'unknown'}",
        f"  head: {status.head or 'no commits yet'}",
        f"  dirty: {'yes' if status.dirty else 'no'}",
        f"  remote: {status.remote or 'not set'}",
    ]
    return "\n".join(lines) + "\n"


def _git(root: Path, *args: str, allow_empty: bool = False) -> str:
    process = subprocess.run(
        ["git", *args],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if process.returncode != 0 and not allow_empty:
        message = process.stderr.strip() or process.stdout.strip() or "git command failed"
        raise VaultError(message)
    return process.stdout
