from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path, PurePath

CODE_EXTENSIONS = {
    ".astro",
    ".css",
    ".html",
    ".js",
    ".jsx",
    ".json",
    ".md",
    ".mjs",
    ".py",
    ".sql",
    ".swift",
    ".ts",
    ".tsx",
    ".yaml",
    ".yml",
}


@dataclass(frozen=True)
class SignalHit:
    name: str
    evidence: str
    files: tuple[str, ...]


@dataclass(frozen=True)
class SignalDefinition:
    name: str
    evidence: str
    path_markers: tuple[str, ...] = ()
    file_globs: tuple[str, ...] = ()
    grep_terms: tuple[str, ...] = ()
    minimum_files: int = 1


SIGNALS: tuple[SignalDefinition, ...] = (
    SignalDefinition(
        name="web-routes",
        evidence="HTTP route directories",
        path_markers=("pages", "app", "routes", "src/pages", "src/app"),
    ),
    SignalDefinition(
        name="admin-surface",
        evidence="Admin, console, or dashboard surface",
        path_markers=(
            "admin",
            "src/admin",
            "app/admin",
            "pages/admin",
            "src/pages/admin",
            "apps/web/src/pages",
            "api/console",
        ),
        file_globs=(
            "**/admin.*",
            "**/admin/**/*",
            "**/Admin.*",
            "**/Console.*",
            "**/ConsoleRoadmap.*",
            "**/Dashboard.*",
            "**/console/**/*",
        ),
        grep_terms=("consoleDashboard", "/console", "admin_todos", "intake_submissions"),
    ),
    SignalDefinition(
        name="auth-system",
        evidence="Authentication files or helpers",
        path_markers=("auth", "src/auth", "lib/auth", "api/auth", "apps/server/src"),
        file_globs=("**/*auth*.ts", "**/*auth*.tsx", "**/*auth*.py", "**/*auth*.swift"),
        grep_terms=("requireAuth", "auth/v1", "login", "logout"),
    ),
    SignalDefinition(
        name="api-surface",
        evidence="API route directories",
        path_markers=("api", "src/api", "app/api", "routes/api", "pages/api", "src/pages/api"),
    ),
    SignalDefinition(
        name="db-migrations",
        evidence="Database migration history",
        path_markers=("migrations", "db/migrations", "supabase/migrations", "prisma/migrations"),
        file_globs=("**/migrations/**/*.sql",),
    ),
    SignalDefinition(
        name="component-library",
        evidence="Reusable UI component directories",
        path_markers=("components", "src/components", "apps/web/src/components"),
        minimum_files=5,
    ),
    SignalDefinition(
        name="design-tokens",
        evidence="Codified design tokens or Tailwind config",
        file_globs=("**/tailwind.config.*", "**/tokens.*", "**/*.tokens.*"),
        grep_terms=("--color-", "--bg-", "--ink-", "--accent-"),
    ),
    SignalDefinition(
        name="ios-app",
        evidence="Native iOS project files",
        file_globs=(
            "**/*.xcodeproj/**/*",
            "**/*.xcworkspace/**/*",
            "**/Package.swift",
            "**/Info.plist",
        ),
    ),
    SignalDefinition(
        name="agent-runtime",
        evidence="Agent runtime imports or model orchestration",
        grep_terms=(
            "claude-agent-sdk",
            "@anthropic-ai",
            "openai",
            "langchain",
            "ClaudeAgentOptions",
        ),
    ),
    SignalDefinition(
        name="prompt-registry",
        evidence="Prompt registry, parser, dispatcher, or prompt packs",
        path_markers=("prompts", "hub-prompts", "packages/prompts"),
        grep_terms=("promptId", "registry", "dispatcher", "frontmatter"),
    ),
    SignalDefinition(
        name="mcp-config",
        evidence="MCP configuration or tools",
        path_markers=(".mcp", "apps/mcp"),
        file_globs=("**/*mcp*.ts", "**/*mcp*.json", "**/*mcp*.md"),
        grep_terms=("mcpServers", "MCP", "modelcontextprotocol"),
    ),
    SignalDefinition(
        name="permission-tiers",
        evidence="Tiered permissions or access policy",
        grep_terms=("R0", "R1", "R2", "R3", "permission", "tier", "policy"),
    ),
    SignalDefinition(
        name="notification-system",
        evidence="Notification, email, or push code",
        file_globs=("**/*notification*", "**/*notif*", "**/*push*", "**/*email*"),
        grep_terms=("notify", "notification", "email", "ntfy"),
    ),
    SignalDefinition(
        name="cron-schedule",
        evidence="Scheduled jobs",
        file_globs=("**/*cron*", "**/*schedule*"),
        grep_terms=("cron", "node-cron", "schedule", "setInterval"),
    ),
)


def detect_signals(repo_root: Path, files: Iterable[Path]) -> tuple[SignalHit, ...]:
    relative_files = tuple(_relative(path, repo_root) for path in files)
    text_cache = _read_text_cache(repo_root, relative_files)
    hits: list[SignalHit] = []
    for definition in SIGNALS:
        matched = _matched_files(repo_root, relative_files, definition, text_cache)
        if len(matched) >= definition.minimum_files:
            hits.append(
                SignalHit(
                    name=definition.name,
                    evidence=definition.evidence,
                    files=tuple(sorted(matched)),
                )
            )
    return tuple(hits)


def signal_names() -> tuple[str, ...]:
    return tuple(signal.name for signal in SIGNALS)


def _matched_files(
    repo_root: Path,
    relative_files: tuple[str, ...],
    definition: SignalDefinition,
    text_cache: dict[str, str],
) -> set[str]:
    matched: set[str] = set()
    for marker in definition.path_markers:
        marker = marker.strip("/")
        marker_path = repo_root / Path(marker)
        if marker_path.is_dir():
            matched.update(_files_under(relative_files, marker))
        elif marker_path.is_file():
            matched.add(marker_path.relative_to(repo_root).as_posix())

    for pattern in definition.file_globs:
        matched.update(path for path in relative_files if PurePath(path).match(pattern))

    if definition.grep_terms:
        terms = tuple(term.lower() for term in definition.grep_terms)
        for relative in relative_files:
            path = repo_root / relative
            if not _is_reasonable_file(path):
                continue
            text = text_cache.get(relative, "")
            if any(term.lower() in text for term in terms):
                matched.add(relative)

    return {path for path in matched if _is_reasonable_file(repo_root / path)}


def _files_under(relative_files: tuple[str, ...], marker: str) -> set[str]:
    prefix = f"{marker}/"
    return {path for path in relative_files if path == marker or path.startswith(prefix)}


def _relative(path: Path, repo_root: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def _is_reasonable_file(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in CODE_EXTENSIONS


def _read_text_cache(repo_root: Path, relative_files: tuple[str, ...]) -> dict[str, str]:
    cache: dict[str, str] = {}
    for relative in relative_files:
        path = repo_root / relative
        if not _is_reasonable_file(path):
            continue
        try:
            cache[relative] = path.read_text(encoding="utf-8", errors="ignore").lower()
        except OSError:
            continue
    return cache
