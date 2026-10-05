#!/usr/bin/env python3
"""
tools/new_module.py - Scaffold a new networking module with the 7 standard files.

Creates:
  1. README.md
  2. notes.md
  3. diagrams.md
  4. numericals.md
  5. mcqs.md
  6. interview_qa.md
  7. cheatsheet.md

Templates are sourced from `_templates/` and populated with metadata.

Usage:
  python tools/new_module.py <folder_name> "<Module Title>" [--force]

Example:
  python tools/new_module.py 04_Physical_Layer "Physical Layer"
"""

import sys
import os
import re
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

MODULE_REGISTRY = [
    ("01", "01_Fundamentals", "Fundamentals"),
    ("02", "02_OSI_Model", "OSI Model"),
    ("03", "03_TCP_IP_Model", "TCP/IP Model"),
    ("04", "04_Physical_Layer", "Physical Layer"),
    ("05", "05_Data_Link_Layer", "Data Link Layer"),
    ("06", "06_Network_Devices_and_LAN", "Network Devices & LAN"),
    ("07", "07_IP_Addressing", "IP Addressing"),
    ("08", "08_Subnetting_CIDR_VLSM", "Subnetting, CIDR & VLSM"),
    ("09", "09_Network_Layer_Protocols", "Network Layer Protocols"),
    ("10", "10_Routing", "Routing"),
    ("11", "11_Transport_Layer", "Transport Layer"),
    ("12", "12_Application_Layer", "Application Layer"),
    ("13", "13_Network_Security", "Network Security"),
    ("14", "14_Wireless_and_Mobile", "Wireless & Mobile"),
    ("15", "15_Modern_Networking", "Modern Networking"),
    ("16", "16_Troubleshooting_and_Tools", "Troubleshooting & Tools"),
    ("17", "17_Interview_Prep", "Interview Prep"),
    ("18", "18_GATE_and_Competitive_Zone", "GATE & Competitive Zone"),
    ("19", "19_Hands_On_Labs", "Hands-On Labs"),
    ("20", "20_Cheatsheets", "Cheatsheets"),
]

TEMPLATE_FILES = [
    "README.md",
    "notes.md",
    "diagrams.md",
    "numericals.md",
    "mcqs.md",
    "interview_qa.md",
    "cheatsheet.md",
]


def get_prev_next(num_str: str) -> tuple[str, str, str, str]:
    num = int(num_str)
    prev_info = ("00_Index", "INDEX.md")
    next_info = ("INDEX", "INDEX.md")

    for i, (n, folder, title) in enumerate(MODULE_REGISTRY):
        if n == num_str:
            if i > 0:
                prev_n, prev_folder, prev_title = MODULE_REGISTRY[i - 1]
                prev_info = (prev_folder, prev_folder)
            if i < len(MODULE_REGISTRY) - 1:
                next_n, next_folder, next_title = MODULE_REGISTRY[i + 1]
                next_info = (next_folder, next_folder)
            break

    return prev_info[0], prev_info[1], next_info[0], next_info[1]


def scaffold_module(folder_name: str, title: str, force: bool = False):
    root = Path(__file__).resolve().parent.parent
    target_dir = root / folder_name
    template_dir = root / "_templates"

    if not template_dir.exists():
        print(f"Error: Template directory not found at {template_dir}")
        sys.exit(1)

    # Extract module number from folder name
    m = re.match(r'^(\d{2})', folder_name)
    mod_num = m.group(1) if m else "XX"
    shortname = re.sub(r'^\d{2}_', '', folder_name).lower()

    prev_name, prev_folder, next_name, next_folder = get_prev_next(mod_num)

    target_dir.mkdir(parents=True, exist_ok=True)

    variables = {
        "{{MODULE_NUM}}": mod_num,
        "{{MODULE_TITLE}}": title,
        "{{MODULE_FOLDER}}": folder_name,
        "{{MODULE_SHORTNAME}}": shortname,
        "{{MODULE_SUBTITLE}}": f"Comprehensive master guide to {title.lower()} principles, architecture, and protocols.",
        "{{TIME_BUDGET}}": "4–5 Hours",
        "{{TARGET_LEVEL}}": "Beginner → Advanced",
        "{{GATE_WEIGHT}}": "High (3–6 Marks in GATE CS/IT)",
        "{{INTERVIEW_WEIGHT}}": "High (Essential Core Networking Concepts)",
        "{{PREREQUISITES}}": f"Completion of [{prev_name}](../{prev_folder}/README.md) recommended.",
        "{{CORE_CONCEPTS_CHECKLIST}}": f"Fundamental mechanisms and physical/logical models of {title.lower()}.",
        "{{ARCHITECTURE_CHECKLIST}}": "Key protocols, framing structures, and end-to-end traversal.",
        "{{FORMULAS_CHECKLIST}}": "Standard calculations, conversions, and performance equations.",
        "{{EXAM_CHECKLIST}}": "Common trick questions, university traps, and interview edge cases.",
        "{{PREV_MODULE_NAME}}": prev_name,
        "{{PREV_MODULE_FOLDER}}": prev_folder,
        "{{NEXT_MODULE_NAME}}": next_name,
        "{{NEXT_MODULE_FOLDER}}": next_folder,
    }

    created_files = []
    skipped_files = []

    for tf in TEMPLATE_FILES:
        tpl_path = template_dir / tf
        dst_path = target_dir / tf

        if dst_path.exists() and not force:
            skipped_files.append(tf)
            continue

        if not tpl_path.exists():
            print(f"Warning: Template {tf} missing from _templates/")
            continue

        raw_text = tpl_path.read_text(encoding="utf-8")
        for key, val in variables.items():
            raw_text = raw_text.replace(key, val)

        dst_path.write_text(raw_text, encoding="utf-8")
        created_files.append(tf)

    print(f"\n📁 Scaffolding Module: {folder_name} ('{title}')")
    if created_files:
        print(f"   ✅ Created {len(created_files)} file(s): {', '.join(created_files)}")
    if skipped_files:
        print(f"   ⚠️  Skipped {len(skipped_files)} existing file(s) (use --force to overwrite): {', '.join(skipped_files)}")

    print(f"\n🎉 Module {folder_name} is ready for authoring!")


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new networking module.")
    parser.add_argument("folder", help="Folder name (e.g. 04_Physical_Layer)")
    parser.add_argument("title", help="Module Title (e.g. 'Physical Layer')")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files if present")

    args = parser.parse_args()
    scaffold_module(args.folder, args.title, force=args.force)


if __name__ == "__main__":
    main()
