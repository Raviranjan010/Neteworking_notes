#!/usr/bin/env python3
"""
tools/check_mcq_balance.py - Multiple Choice Question (MCQ) Answer Key Balance Checker.

Scans mcqs.md files (Part A: Single Choice Questions), extracts the correct answers,
and verifies that each option (A, B, C, D) falls strictly within 20% to 30% of the total
single-choice questions (e.g. 6 to 9 questions per letter for a 30-question Part A).

Usage:
  python tools/check_mcq_balance.py                  # Scans all active mcqs.md files
  python tools/check_mcq_balance.py path/to/mcqs.md  # Checks specific mcqs.md file

Exit codes:
  0 = All checked files satisfy the 20% - 30% balance rule
  1 = One or more letters in a checked file fall outside 20% - 30%
"""

import sys
import os
import re
from pathlib import Path

# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

EXCLUDE_DIRS = {".git", ".github", ".gemini", "node_modules", "venv", "__pycache__", "_templates"}


def check_mcq_balance(file_path: Path, root: Path) -> tuple[bool, str]:
    rel_path = file_path.relative_to(root).as_posix()
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return False, f"❌ {rel_path}: Could not read file: {e}"

    # Locate Part A header and Part B header
    m_a = re.search(r'^##\s+.*?Part A.*$', content, re.MULTILINE)
    if not m_a:
        return True, f"ℹ️  {rel_path}: No 'Part A' heading found (skipped)"

    m_b = re.search(r'^##\s+.*?Part B.*$', content, re.MULTILINE)
    if m_b:
        part_a_text = content[m_a.end():m_b.start()]
    else:
        part_a_text = content[m_a.end():]

    # Find answer declarations: **Answer: X** or **Answer:** X
    answers = re.findall(r'\*\*Answer:\s*\*?\s*([A-D])\b', part_a_text)
    total = len(answers)

    if total == 0:
        return False, f"❌ {rel_path}: No single-choice answers found in Part A"

    counts = {opt: answers.count(opt) for opt in "ABCD"}
    percentages = {opt: (counts[opt] / total) * 100 for opt in "ABCD"}

    # Evaluate balance rule: strictly 20.0% to 30.0%
    is_balanced = True
    report_lines = [
        f"\n📄 {rel_path} (Part A Total: {total} questions)"
    ]

    for opt in "ABCD":
        cnt = counts[opt]
        pct = percentages[opt]
        if pct < 20.0 or pct > 30.0:
            is_balanced = False
            status = f"❌ FAIL (Outside 20%-30% range: {pct:.1f}%)"
        else:
            status = f"✅ PASS ({pct:.1f}%)"
        report_lines.append(f"   Option {opt}: {cnt:2d} / {total} ({pct:5.1f}%)  -> {status}")

    return is_balanced, "\n".join(report_lines)


def main():
    root = Path(__file__).resolve().parent.parent

    # Determine files to check
    if len(sys.argv) > 1:
        targets = [Path(arg).resolve() for arg in sys.argv[1:]]
    else:
        # Default: scan active module mcqs.md files (folders with README.md)
        targets = []
        for p in sorted(root.rglob("mcqs.md")):
            rel = p.relative_to(root)
            if any(part in EXCLUDE_DIRS for part in rel.parts):
                continue
            if (p.parent / "README.md").exists():
                targets.append(p)

    if not targets:
        print("No mcqs.md files found to check.")
        sys.exit(0)

    overall_success = True
    print(f"Checking MCQ Part A answer balance across {len(targets)} file(s)...")

    for target in targets:
        success, report = check_mcq_balance(target, root)
        print(report)
        if not success:
            overall_success = False

    if overall_success:
        print("\n🎉 All checked MCQ files passed the 20%–30% answer balance test!")
        sys.exit(0)
    else:
        print("\n⚠️ One or more MCQ files failed the 20%–30% answer balance test.")
        sys.exit(1)


if __name__ == "__main__":
    main()
