from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

WATCHLIST = (
    "AI-powered",
    "AI-driven",
    "future-proof",
    "10x",
    "transform your",
    "cutting-edge",
    "unlock",
    "revolutionary",
    "game-changing",
    "seamless AI",
    "scale overnight",
    "leverage AI",
)

TEXT_EXTENSIONS = {
    ".astro",
    ".css",
    ".html",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".mdx",
    ".mjs",
    ".ts",
    ".tsx",
    ".txt",
    ".yml",
    ".yaml",
}

SKIP_DIRS = {
    ".astro",
    ".git",
    ".next",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "dist",
    "node_modules",
    "playwright-report",
    "test-results",
}


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    phrase: str
    text: str


def iter_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file():
            if path.suffix.lower() in TEXT_EXTENSIONS:
                files.append(path)
            continue
        if not path.exists():
            continue
        for child in path.rglob("*"):
            if any(part in SKIP_DIRS for part in child.parts):
                continue
            if child.is_file() and child.suffix.lower() in TEXT_EXTENSIONS:
                files.append(child)
    return sorted(set(files))


def scan_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    text = path.read_text(encoding="utf-8", errors="ignore")
    for index, line in enumerate(text.splitlines(), start=1):
        lower = line.lower()
        for phrase in WATCHLIST:
            if phrase.lower() in lower:
                findings.append(
                    Finding(
                        path=path,
                        line=index,
                        phrase=phrase,
                        text=line.strip(),
                    )
                )
    return findings


def scan(paths: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in iter_files(paths):
        findings.extend(scan_file(path))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Advisory scan for copy phrases that need authenticity review."
    )
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 when findings exist. Default is advisory exit 0.",
    )
    args = parser.parse_args()

    findings = scan(args.paths)
    if findings:
        print("copy authenticity scan: review recommended")
        for finding in findings:
            print(
                f"{finding.path.as_posix()}:{finding.line}: "
                f"{finding.phrase}: {finding.text}"
            )
    else:
        print("copy authenticity scan: no watchlist phrases found")
    return 1 if args.strict and findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
