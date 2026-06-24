#!/usr/bin/env python3
"""Self-contained public-release verification for this case-study repo.

Stdlib only. No third-party dependencies. Run before publishing changes:

    python3 scripts/verify_public.py

Checks performed:
  1. Internal markdown-link resolution.
     Every relative `[text](target)` link target must resolve to an existing
     file in the repo. (Inline-code prose citations such as `README.md:5` are
     evidence footnotes, not links, and are intentionally not checked.)
  2. Forbidden-pattern scan.
     Tracked text files must not contain secrets, credentials, API keys, or
     `.env` contents per SECURITY.md.

Exits 0 if all checks pass, 1 otherwise. This replaces the previously
documented `repo_preflight.py`, which was not present in this repo.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Files/dirs ignored when collecting text to scan.
IGNORE_DIRS = {".git", "__pycache__", ".pytest_cache", ".cache", "node_modules",
               "venv", ".venv", "build", "dist"}
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".txt", ".cfg", ".toml", ".json"}

# Markdown link: [text](target)
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

# Forbidden patterns: secrets, keys, credentials, env contents.
FORBIDDEN = [
    (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS access key id"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key block"),
    (re.compile(r"sk-[A-Za-z0-9]{20,}"), "API secret key (sk- prefix)"),
    (re.compile(r"ghp_[A-Za-z0-9]{30,}"), "GitHub personal access token"),
    (re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"), "Slack token"),
    (re.compile(r"(?i)\b(?:api[_-]?key|secret|password|passwd)\b\s*[:=]\s*['\"][^'\"]+['\"]"),
     "inline credential assignment"),
]


def is_ignored(path: Path) -> bool:
    return any(part in IGNORE_DIRS for part in path.relative_to(REPO_ROOT).parts)


def text_files() -> list[Path]:
    out = []
    for p in REPO_ROOT.rglob("*"):
        if p.is_file() and p.suffix in TEXT_SUFFIXES and not is_ignored(p):
            out.append(p)
    return sorted(out)


def check_links(failures: list[str]) -> None:
    for md in [p for p in text_files() if p.suffix == ".md"]:
        text = md.read_text(encoding="utf-8", errors="replace")
        targets = set(MD_LINK_RE.findall(text))
        for target in targets:
            # Skip external links and pure anchors.
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            ref = target.split("#", 1)[0].strip()
            if not ref:
                continue
            resolved = (md.parent / ref).resolve()
            if not resolved.exists():
                rel = md.relative_to(REPO_ROOT)
                failures.append(f"broken reference in {rel}: '{target}' -> {ref}")


def check_forbidden(failures: list[str]) -> None:
    self_path = Path(__file__).resolve()
    for f in text_files():
        if f.resolve() == self_path:
            continue  # this script defines the patterns; skip self
        text = f.read_text(encoding="utf-8", errors="replace")
        for pattern, label in FORBIDDEN:
            if pattern.search(text):
                rel = f.relative_to(REPO_ROOT)
                failures.append(f"forbidden pattern ({label}) in {rel}")


def main() -> int:
    failures: list[str] = []
    print(f"verify_public: scanning {REPO_ROOT}")

    check_links(failures)
    check_forbidden(failures)

    n_files = len(text_files())
    if failures:
        print(f"\nFAIL: {len(failures)} issue(s) across {n_files} text file(s):")
        for msg in failures:
            print(f"  - {msg}")
        return 1

    print(f"\nPASS: {n_files} text file(s) checked; "
          "all internal references resolve and no forbidden patterns found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
