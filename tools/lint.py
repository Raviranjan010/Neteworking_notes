#!/usr/bin/env python3
"""
tools/lint.py - Quality Gate Linter for Markdown Documentation.

Scans all .md files for:
1. Placeholder text: TODO, TBD, "coming soon", "similar to above".
2. Non-ASCII CJK (Chinese, Japanese, Korean) characters.
3. Unbalanced code fences (``` and ````).
4. Bad Mermaid block starts (malformed fences or missing diagram types).
5. Missing 'Next:' or 'Next Module:' links in active module notes.md files.

Exit codes:
  0 = All checks passed
  1 = Lint errors found
"""

import sys
import os
import re
from pathlib import Path

# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Paths to ignore from linting
EXCLUDE_DIRS = {".git", ".github", ".gemini", "node_modules", "venv", "__pycache__", "_templates"}

# Meta documentation files where placeholder and audit rules are documented
META_FILES = {"CONTRIBUTING.md", "PROGRESS.md", "MASTER_PROMPT.md", "HANDOFF.md"}

# Valid Mermaid diagram declarations (first non-empty, non-comment line inside ```mermaid)
VALID_MERMAID_TYPES = (
    "graph", "flowchart", "sequencediagram", "statediagram", "statediagram-v2",
    "erdiagram", "classdiagram", "pie", "gantt", "gitgraph", "mindmap",
    "quadrantchart", "timeline", "c4context", "xychart-beta", "block-beta", "packet-beta"
)

# CJK Unicode pattern
CJK_REGEX = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf\u3040-\u30ff\uac00-\ud7af]')

# Placeholder patterns
PLACEHOLDER_REGEX = re.compile(r'\b(TODO|TBD)\b|coming soon|similar to above', re.IGNORECASE)


def is_excluded(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return any(part in EXCLUDE_DIRS for part in rel.parts)


def check_file(path: Path, root: Path) -> list:
    rel_path = path.relative_to(root).as_posix()
    errors = []

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        return [f"{rel_path}: Encoding error - failed to read as UTF-8: {e}"]

    lines = content.splitlines()
    in_code_block = False
    current_fence = None
    in_mermaid = False
    mermaid_first_line = None
    mermaid_start_line = None

    fence_3_count = 0
    fence_4_count = 0

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()

        # 1. Check placeholders (skip meta documentation files)
        if path.name not in META_FILES:
            match = PLACEHOLDER_REGEX.search(line)
            if match:
                errors.append(f"{rel_path}:{idx}: Found placeholder '{match.group(0)}': {line.strip()[:80]}")

            # 2. Check CJK characters
            cjk_match = CJK_REGEX.search(line)
            if cjk_match:
                errors.append(f"{rel_path}:{idx}: Found stray CJK character '{cjk_match.group(0)}': {line.strip()[:80]}")

        # Track code fences
        if stripped.startswith("````"):
            fence_4_count += 1
            if current_fence == "````":
                current_fence = None
                in_code_block = False
            elif current_fence is None:
                current_fence = "````"
                in_code_block = True
        elif stripped.startswith("```"):
            fence_3_count += 1
            if current_fence == "```":
                current_fence = None
                in_code_block = False
                if in_mermaid:
                    in_mermaid = False
                    if mermaid_first_line is None:
                        errors.append(f"{rel_path}:{mermaid_start_line}: Empty Mermaid block")
                    else:
                        first_word = mermaid_first_line.split()[0].lower() if mermaid_first_line.split() else ""
                        if not any(first_word.startswith(t) for t in VALID_MERMAID_TYPES):
                            errors.append(
                                f"{rel_path}:{mermaid_start_line}: Bad Mermaid diagram declaration '{mermaid_first_line}'"
                            )
            elif current_fence is None:
                current_fence = "```"
                in_code_block = True
                # Check for bad mermaid start
                if stripped.startswith("```mermaid"):
                    in_mermaid = True
                    mermaid_start_line = idx
                    mermaid_first_line = None
                    # Flag inline mermaid declarations like ```mermaid graph TD
                    remainder = stripped[len("```mermaid"):].strip()
                    if remainder:
                        errors.append(
                            f"{rel_path}:{idx}: Mermaid header should not contain inline diagram type '{remainder}' (place on newline)"
                        )

        elif in_mermaid:
            if mermaid_first_line is None and stripped and not stripped.startswith("%%"):
                mermaid_first_line = stripped

    # 3. Check balanced code fences
    if fence_3_count % 2 != 0:
        errors.append(f"{rel_path}: Unbalanced 3-backtick code fences (count = {fence_3_count})")
    if fence_4_count % 2 != 0:
        errors.append(f"{rel_path}: Unbalanced 4-backtick code fences (count = {fence_4_count})")

    # 4. Check for Next: link in active module notes.md files (modules containing README.md)
    parts = path.parts
    if path.name == "notes.md" and any(re.match(r'^\d{2}_', p) for p in parts):
        has_readme = (path.parent / "README.md").exists()
        if has_readme:
            has_next = bool(re.search(r'\bNext\b[^:\n]*:\s*\[', content, re.IGNORECASE))
            if not has_next and "20_" not in rel_path:
                errors.append(f"{rel_path}: Missing 'Next:' or 'Next Module:' navigation link at end of file")

    return errors


def main():
    root = Path(__file__).resolve().parent.parent
    all_errors = []
    checked_count = 0

    for md_file in sorted(root.rglob("*.md")):
        if is_excluded(md_file, root):
            continue
        checked_count += 1
        errors = check_file(md_file, root)
        if errors:
            all_errors.extend(errors)

    print(f"Linted {checked_count} markdown files in {root}")
    if all_errors:
        print(f"\n❌ Found {len(all_errors)} lint issue(s):")
        for err in all_errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("✅ All markdown files passed linting with zero issues!")
        sys.exit(0)


if __name__ == "__main__":
    main()
