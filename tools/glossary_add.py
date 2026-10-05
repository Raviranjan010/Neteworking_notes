#!/usr/bin/env python3
"""
tools/glossary_add.py - Append new terminology to GLOSSARY.md in alphabetical order.

Accepts input via:
  1. Positional arguments:
     python tools/glossary_add.py "Term" "Definition text." "Module_Folder"
  2. Delimited pipe string:
     python tools/glossary_add.py "Term|Definition text.|Module_Folder"
  3. Interactive or pipe via stdin:
     echo "Term|Definition|Module" | python tools/glossary_add.py

Usage example:
  python tools/glossary_add.py "Jumbo Frame" "An Ethernet frame with a payload greater than 1500 bytes (up to 9000 bytes)." "05_Data_Link_Layer"
"""

import sys
import os
import re
from pathlib import Path

# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def parse_term_entry(line: str) -> tuple[str, str, str]:
    parts = [p.strip() for p in line.split("|")]
    if len(parts) >= 3:
        return parts[0], parts[1], parts[2]
    raise ValueError(f"Entry must be formatted as 'term|definition|module', got: '{line}'")


def format_entry(term: str, definition: str, module: str) -> str:
    # Ensure definition ends with period
    if not definition.endswith("."):
        definition += "."

    # Check if module is already a markdown link
    if module.startswith("[") and "](" in module:
        see_link = module
    else:
        # Clean module folder path
        clean_mod = module.strip("/\\")
        link_target = f"{clean_mod}/notes.md" if (Path(__file__).resolve().parent.parent / clean_mod / "notes.md").exists() else f"{clean_mod}/"
        see_link = f"[{clean_mod}]({link_target})"

    return f"- **{term}:** {definition} See {see_link}."


def add_term_to_glossary(glossary_path: Path, term: str, definition: str, module: str) -> bool:
    content = glossary_path.read_text(encoding="utf-8")
    first_letter = term.strip()[0].upper()
    if not first_letter.isalpha():
        first_letter = "A"

    new_line = format_entry(term, definition, module)

    section_header = f"### {first_letter}"
    if section_header not in content:
        print(f"Error: Section header '{section_header}' not found in {glossary_path.name}")
        return False

    # Find where the section starts
    sec_idx = content.find(section_header)
    # Find next section or divider
    next_div = content.find("\n---\n", sec_idx)
    if next_div == -1:
        next_div = len(content)

    section_content = content[sec_idx:next_div]
    lines = section_content.splitlines()

    header_line = lines[0]
    entries = [l for l in lines[1:] if l.strip().startswith("- **")]

    # Check if term already exists
    term_pattern = re.compile(rf'-\s*\*\*{re.escape(term)}[\s*:(]', re.IGNORECASE)
    for existing in entries:
        if term_pattern.search(existing):
            print(f"Term '{term}' already exists in {glossary_path.name}: {existing}")
            return False

    # Add new entry and sort alphabetically by term name
    entries.append(new_line)

    def extract_term_key(entry_line: str) -> str:
        m = re.search(r'\*\*(.*?)\*\*', entry_line)
        return m.group(1).lower() if m else entry_line.lower()

    entries.sort(key=extract_term_key)

    new_section = header_line + "\n" + "\n".join(entries) + "\n"
    updated_content = content[:sec_idx] + new_section + content[next_div:]

    glossary_path.write_text(updated_content, encoding="utf-8")
    print(f"Added term '{term}' to {glossary_path.name} under section [{first_letter}]")
    return True


def main():
    root = Path(__file__).resolve().parent.parent
    glossary_path = root / "GLOSSARY.md"

    if not glossary_path.exists():
        print(f"Error: {glossary_path} not found.")
        sys.exit(1)

    entries_to_add = []

    if len(sys.argv) == 4:
        # python tools/glossary_add.py "Term" "Definition" "Module"
        entries_to_add.append((sys.argv[1], sys.argv[2], sys.argv[3]))
    elif len(sys.argv) == 2:
        # python tools/glossary_add.py "Term|Definition|Module"
        entries_to_add.append(parse_term_entry(sys.argv[1]))
    elif not sys.stdin.isatty():
        # Piped stdin
        for line in sys.stdin:
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                entries_to_add.append(parse_term_entry(stripped))
    else:
        print("Usage:")
        print('  python tools/glossary_add.py "Term" "Definition" "Module"')
        print('  python tools/glossary_add.py "Term|Definition|Module"')
        sys.exit(1)

    success_count = 0
    for term, definition, module in entries_to_add:
        if add_term_to_glossary(glossary_path, term, definition, module):
            success_count += 1

    print(f"Successfully processed {success_count} glossary entry(ies).")


if __name__ == "__main__":
    main()
