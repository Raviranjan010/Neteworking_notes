#!/usr/bin/env python3
"""
tools/check_links.py - Comprehensive Markdown Link and Anchor Checker.

Verifies:
1. All relative file links point to existing files or directories.
2. All anchor links (#anchor or file.md#anchor) match valid heading slugs or HTML id/name anchors.
3. Flags broken links with file, line number, and link target.

Exit codes:
  0 = All links and anchors valid
  1 = Broken links or anchors found
"""

import sys
import os
import re
import urllib.parse
from pathlib import Path

# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

EXCLUDE_DIRS = {".git", ".github", ".gemini", "node_modules", "venv", "__pycache__", "_templates"}
EXCLUDE_FILES = {"MASTER_PROMPT.md"}

# Match Markdown links [text](url) and image links ![alt](url)
LINK_REGEX = re.compile(r'!?\[([^\]]*)\]\(([^)]+)\)')

# External schemes to ignore
EXTERNAL_SCHEMES = ("http://", "https://", "mailto:", "ftp://", "tel:", "data:", "javascript:")


def extract_anchors(file_path: Path) -> set:
    """Extract all valid anchor identifiers from a markdown file."""
    anchors = set()
    counts = {}

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return anchors

    for line in content.splitlines():
        line_stripped = line.strip()

        # Markdown headings
        if line_stripped.startswith("#"):
            raw = re.sub(r'^#+\s*', '', line_stripped)
            raw = re.sub(r'<[^>]+>', '', raw)
            raw = re.sub(r'[*_`~]', '', raw).lower().strip()

            # Version A: Punctuation stripped, each space -> hyphen (preserves double hyphens from stripped '&')
            s_raw = re.sub(r'[^\w\s-]', '', raw)
            uncollapsed = re.sub(r'\s', '-', s_raw).strip('-')
            # Version B: Fully collapsed hyphens
            collapsed = re.sub(r'[-\s]+', '-', s_raw).strip('-')

            for slug in {collapsed, uncollapsed}:
                if slug:
                    if slug in counts:
                        counts[slug] += 1
                        anchors.add(f"{slug}-{counts[slug]}")
                    else:
                        counts[slug] = 0
                        anchors.add(slug)

        # HTML id / name attributes
        for match in re.finditer(r'<[a-zA-Z0-9]+[^>]+(?:id|name)=["\']([^"\']+)["\']', line):
            anchors.add(match.group(1).lower())

    return anchors


def check_links_in_file(file_path: Path, root: Path, anchor_cache: dict) -> list:
    rel_path = file_path.relative_to(root).as_posix()
    errors = []

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"{rel_path}: Could not read file: {e}"]

    # Cache anchors for this file if not already done
    if file_path not in anchor_cache:
        anchor_cache[file_path] = extract_anchors(file_path)

    lines = content.splitlines()
    in_code_block = False

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("````"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        for match in LINK_REGEX.finditer(line):
            link_target = match.group(2).strip()

            # Ignore external links
            if any(link_target.startswith(scheme) for scheme in EXTERNAL_SCHEMES):
                continue

            # Strip title attribute if present: [text](path "title")
            if " " in link_target and not link_target.startswith("#"):
                parts = link_target.split(None, 1)
                link_target = parts[0]

            # Unquote URL encoding
            clean_target = urllib.parse.unquote(link_target)

            # Split path and fragment/anchor
            if "#" in clean_target:
                target_path_str, fragment = clean_target.split("#", 1)
                fragment = fragment.lower().strip()
            else:
                target_path_str, fragment = clean_target, None

            # 1. Same-file anchor link: [text](#anchor)
            if not target_path_str:
                if fragment and fragment not in anchor_cache[file_path]:
                    # Also try collapsed version if fragment had multiple hyphens
                    collapsed_frag = re.sub(r'-+', '-', fragment)
                    if collapsed_frag not in anchor_cache[file_path]:
                        errors.append(
                            f"{rel_path}:{idx}: Broken local anchor '#{fragment}' (no matching heading in this file)"
                        )
                continue

            # 2. Relative file or directory path
            target_path = (file_path.parent / target_path_str).resolve()

            if not target_path.exists():
                errors.append(
                    f"{rel_path}:{idx}: Broken link to target '{clean_target}' (file does not exist: {target_path_str})"
                )
                continue

            # If target is directory, verify it's a valid dir
            if target_path.is_dir():
                if fragment:
                    errors.append(
                        f"{rel_path}:{idx}: Anchor '#{fragment}' specified on directory target '{target_path_str}'"
                    )
                continue

            # Target is a file: if fragment is present, check anchor in target file
            if fragment and target_path.suffix.lower() == ".md":
                if target_path not in anchor_cache:
                    anchor_cache[target_path] = extract_anchors(target_path)
                if fragment not in anchor_cache[target_path]:
                    collapsed_frag = re.sub(r'-+', '-', fragment)
                    if collapsed_frag not in anchor_cache[target_path]:
                        errors.append(
                            f"{rel_path}:{idx}: Broken anchor '#{fragment}' in target file '{target_path_str}'"
                        )

    return errors


def main():
    root = Path(__file__).resolve().parent.parent
    all_errors = []
    anchor_cache = {}
    checked_count = 0

    for md_file in sorted(root.rglob("*.md")):
        if md_file.name in EXCLUDE_FILES:
            continue
        rel = md_file.relative_to(root)
        if any(part in EXCLUDE_DIRS for part in rel.parts):
            continue
        checked_count += 1
        errors = check_links_in_file(md_file, root, anchor_cache)
        if errors:
            all_errors.extend(errors)

    print(f"Checked links across {checked_count} markdown files in {root}")
    if all_errors:
        print(f"\n❌ Found {len(all_errors)} broken link/anchor issue(s):")
        for err in all_errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("✅ All relative links and anchors are valid!")
        sys.exit(0)


if __name__ == "__main__":
    main()
