#!/usr/bin/env python3
"""Scan a repository for common privacy leaks before publishing."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


EXCLUDED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    ".mypy_cache",
    ".pytest_cache",
}

TEXT_SUFFIXES = {
    ".cfg",
    ".css",
    ".csv",
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
    ".html",
    ".js",
    ".json",
    ".md",
    ".mjs",
    ".py",
    ".sh",
    ".toml",
    ".ts",
    ".txt",
    ".yaml",
    ".yml",
}


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    label: str
    snippet: str


PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "windows-home-path",
        re.compile(r"[A-Za-z]:\\Users\\[^\\\s`\"'>]+"),
    ),
    (
        "unix-home-path",
        re.compile(r"/(?:Users|home)/[^/\s`\"'>]+"),
    ),
    (
        "openai-or-service-key",
        re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    ),
    (
        "private-key-block",
        re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    ),
    (
        "secret-assignment",
        re.compile(
            r"(?i)\b(api[_-]?key|access[_-]?token|auth[_-]?token|password|secret|private[_-]?key)\b"
            r"\s*[:=]\s*['\"]?[^'\"\s`]{8,}"
        ),
    ),
    (
        "dotenv-secret-assignment",
        re.compile(
            r"(?im)^\s*[A-Z0-9_]*(KEY|TOKEN|PASSWORD|SECRET|PRIVATE)[A-Z0-9_]*"
            r"\s*=\s*(?!example\b|placeholder\b|redacted\b|changeme\b)[^\s#]+"
        ),
    ),
    (
        "raw-chat-transcript",
        re.compile(r"(?im)^\s*(user|assistant|system)\s*:\s+.{20,}"),
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan text files for likely secrets, personal paths, and raw transcript leaks."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Repository root to scan.",
    )
    parser.add_argument(
        "--term",
        action="append",
        default=[],
        help="Additional private project, client, or person term to flag. Repeat as needed.",
    )
    return parser.parse_args()


def is_text_file(path: Path) -> bool:
    if path.suffix.lower() in TEXT_SUFFIXES:
        return True
    if path.name in {"LICENSE", "README", "SECURITY"}:
        return True
    return False


def iter_files(root: Path):
    for path in root.rglob("*"):
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        if path.is_file() and is_text_file(path):
            yield path


def scan_file(path: Path, root: Path, private_terms: list[str]) -> list[Finding]:
    findings: list[Finding] = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="replace")

    term_patterns = [
        (f"private-term:{term}", re.compile(re.escape(term), re.IGNORECASE))
        for term in private_terms
        if term
    ]

    for line_number, line in enumerate(text.splitlines(), start=1):
        for label, pattern in (*PATTERNS, *term_patterns):
            if pattern.search(line):
                snippet = line.strip()
                if len(snippet) > 140:
                    snippet = snippet[:137] + "..."
                findings.append(Finding(path.relative_to(root), line_number, label, snippet))
    return findings


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if not root.exists():
        print(f"scan root does not exist: {root}", file=sys.stderr)
        return 2

    findings: list[Finding] = []
    for path in iter_files(root):
        findings.extend(scan_file(path, root, args.term))

    if findings:
        print("Privacy scan failed. Review these findings before publishing:\n")
        for finding in findings:
            print(
                f"{finding.path}:{finding.line}: {finding.label}: {finding.snippet}"
            )
        return 1

    print("Privacy scan passed. No configured leak patterns found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
