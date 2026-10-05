#!/usr/bin/env python3
"""
tools/update_index.py - Automatically regenerate INDEX.md and PROGRESS.md status table.

Inspects the 20-module repository tree and updates:
1. The status matrix table in PROGRESS.md.
2. The topic listings and module file links in INDEX.md.

Usage:
  python tools/update_index.py
"""

import sys
import os
import re
from pathlib import Path

# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

MODULE_METADATA = [
    ("01", "01_Fundamentals", "Fundamentals", "Network models, components, topologies, transmission delays, and switching techniques.", True),
    ("02", "02_OSI_Model", "OSI Model", "The 7-layer theoretical reference framework and end-to-end data encapsulation.", False),
    ("03", "03_TCP_IP_Model", "TCP/IP Model", "The practical 4-layer / 5-layer hybrid architecture running the global Internet.", False),
    ("04", "04_Physical_Layer", "Physical Layer", "Analog vs digital signals, transmission media, Nyquist/Shannon capacities, and line coding.", True),
    ("05", "05_Data_Link_Layer", "Data Link Layer", "Node-to-node framing, error detection (CRC), flow control (ARQ), CSMA/CD, and Ethernet.", True),
    ("06", "06_Network_Devices_and_LAN", "Network Devices & LAN", "Hubs, switches, routers, collision/broadcast domains, VLANs, and trunking.", True),
    ("07", "07_IP_Addressing", "IP Addressing", "IPv4 classful/classless addressing, special IP blocks, private ranges, and IPv6 structure.", True),
    ("08", "08_Subnetting_CIDR_VLSM", "Subnetting, CIDR & VLSM", "Subnet masks, CIDR prefix notation, VLSM design, host ranges, and network/broadcast calculations.", True),
    ("09", "09_Network_Layer_Protocols", "Network Layer Protocols", "IPv4/IPv6 packet formats, ARP, ICMP, DHCP, NAT/PAT, and fragmentation mechanics.", True),
    ("10", "10_Routing", "Routing", "Static vs dynamic routing, Distance Vector (RIP), Link State (OSPF), Path Vector (BGP).", True),
    ("11", "11_Transport_Layer", "Transport Layer", "TCP 3-way handshake, flow control, Reno/Tahoe congestion control, UDP, and QUIC.", True),
    ("12", "12_Application_Layer", "Application Layer", "DNS, HTTP/1.1 to HTTP/3, SMTP, FTP, SSH, socket programming in Python.", True),
    ("13", "13_Network_Security", "Network Security", "Symmetric/asymmetric crypto, TLS 1.3 handshake, firewalls, IPSec, and DDoS mitigation.", True),
    ("14", "14_Wireless_and_Mobile", "Wireless & Mobile", "802.11 Wi-Fi standards (Wi-Fi 6/7), CSMA/CA, cellular (4G LTE/5G), and roaming.", True),
    ("15", "15_Modern_Networking", "Modern Networking", "Software-Defined Networking (SDN), Cloud VPC architecture, Overlay networks, and CDNs.", False),
    ("16", "16_Troubleshooting_and_Tools", "Troubleshooting & Tools", "Wireshark packet analysis, tcpdump, traceroute/ping internals, and real-world failure cases.", False),
    ("17", "17_Interview_Prep", "Interview Prep", "Top 100 core networking questions, 60 protocol difference tables, and systems design screens.", False),
    ("18", "18_GATE_and_Competitive_Zone", "GATE & Competitive", "GATE syllabus mapping, master formula sheet, and 100+ topic-wise PYQs.", False),
    ("19", "19_Hands_On_Labs", "Hands-On Labs", "Cisco Packet Tracer configs, Wireshark packet captures, and socket programming labs.", False),
    ("20", "20_Cheatsheets", "Cheatsheets", "10 high-yield printable cheat sheets covering protocols, port numbers, formulas, and CLI.", False),
]

CORE_FILES = ["README.md", "notes.md", "diagrams.md", "numericals.md", "mcqs.md", "interview_qa.md", "cheatsheet.md"]


def determine_file_status(folder_path: Path, filename: str, is_active_mod: bool, numericals_needed: bool) -> str:
    target = folder_path / filename
    if filename == "numericals.md" and not numericals_needed:
        return "➖"

    if not target.exists():
        return "📋"

    # File exists: check if active module or legacy
    if is_active_mod:
        return "✅"
    else:
        # Legacy file from original repo
        return "🚧"


def generate_status_matrix(root: Path) -> str:
    lines = [
        "| # | Module Name | `README.md` | `notes.md` | `diagrams.md` | `numericals.md` | `mcqs.md` | `interview_qa.md` | `cheatsheet.md` |",
        "|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|",
    ]

    for num, folder, title, desc, num_needed in MODULE_METADATA:
        folder_path = root / folder
        is_active = (folder_path / "README.md").exists()

        if int(num) >= 17:
            # Custom specialized modules
            readme_st = "✅" if (folder_path / "README.md").exists() else "📋"
            if num == "17":
                lines.append(f"| **{num}** | {title} | {readme_st} | *(custom)* | *(custom)* | ➖ | *(custom)* | *(custom)* | *(custom)* |")
            elif num == "18":
                lines.append(f"| **{num}** | {title} | {readme_st} | *(custom)* | *(custom)* | *(custom)* | *(custom)* | *(custom)* | *(custom)* |")
            elif num == "19":
                lines.append(f"| **{num}** | {title} | {readme_st} | *(custom)* | *(custom)* | ➖ | ➖ | ➖ | ➖ |")
            elif num == "20":
                lines.append(f"| **{num}** | {title} | {readme_st} | *(custom)* | *(custom)* | *(custom)* | ➖ | ➖ | *(custom)* |")
            continue

        statuses = []
        for cf in CORE_FILES:
            st = determine_file_status(folder_path, cf, is_active, num_needed)
            statuses.append(st)

        row = f"| **{num}** | {title} | " + " | ".join(statuses) + " |"
        lines.append(row)

    return "\n".join(lines)


def update_progress_md(root: Path, new_matrix: str):
    progress_file = root / "PROGRESS.md"
    if not progress_file.exists():
        return

    content = progress_file.read_text(encoding="utf-8")
    table_pattern = re.compile(
        r'\| # \| Module Name \| `README\.md`.*?\n\|:---:\|.*?\n(?:\|.*?\|\n)+',
        re.MULTILINE
    )

    if table_pattern.search(content):
        updated = table_pattern.sub(new_matrix + "\n", content)
        progress_file.write_text(updated, encoding="utf-8")
        print("Updated status matrix in PROGRESS.md")
    else:
        print("Warning: Could not locate status matrix table pattern in PROGRESS.md")


def generate_index_content(root: Path) -> str:
    lines = [
        "# 📑 Master Table of Contents (INDEX)",
        "",
        "A comprehensive directory of every topic, module, guide, cheatsheet, and lab in the **Computer Networking Mastery** repository.",
        "",
        "---",
        "",
        "## 🏛️ Root Guides & Standards",
        "- [README.md](README.md) — Landing page, mission, curriculum roadmap, and track overview.",
        "- [START_HERE.md](START_HERE.md) — 5-minute onboarding guide, learning tracks, and diagram color scheme.",
        "- [STUDY_PLANS.md](STUDY_PLANS.md) — 7-day, 14-day, 30-day, 60-day, and 90-day GATE study plans.",
        "- [HANDOFF.md](HANDOFF.md) — Project memory, completed module commit log, and quality decisions.",
        "- [PROGRESS.md](PROGRESS.md) — Live progress dashboard, file matrix, and quality gate tracker.",
        "- [GLOSSARY.md](GLOSSARY.md) — A–Z glossary of networking terminology and acronyms.",
        "- [CONTRIBUTING.md](CONTRIBUTING.md) — Guidelines for contributing content, diagrams, or fixes.",
        "- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — Community standards and contributor code of conduct.",
        "- [LICENSE](LICENSE) — MIT License.",
        "",
        "---",
        "",
        "## 📚 Core Modules (01–16)",
        "",
    ]

    for num, folder, title, desc, num_needed in MODULE_METADATA[:16]:
        folder_path = root / folder
        is_active = (folder_path / "README.md").exists()

        if is_active:
            lines.append(f"### [{num}. {title}]({folder}/README.md)")
            lines.append(f"*{desc}*")
            for cf in CORE_FILES:
                fp = folder_path / cf
                if fp.exists():
                    label = {
                        "README.md": "Module overview & learning roadmap",
                        "notes.md": "Comprehensive deep-dive notes, formulas, and theory",
                        "diagrams.md": "Mermaid architectural, timing, and sequence diagrams",
                        "numericals.md": "Solved calculations across 3 levels (verified with Python)",
                        "mcqs.md": "55 practice questions (MCQ, MSQ, NAT, Scenarios)",
                        "interview_qa.md": "Technical interview questions with model answers",
                        "cheatsheet.md": "One-page quick revision sheet",
                    }.get(cf, cf)
                    lines.append(f"- [{folder}/{cf}]({folder}/{cf}) — {label}")
            lines.append("")
        else:
            lines.append(f"### [{num}. {title}]({folder}/) *(Planned)*")
            lines.append(f"*{desc}*")
            existing = [f.name for f in sorted(folder_path.glob("*.md")) if f.is_file()]
            if existing:
                for ef in existing:
                    lines.append(f"- [{folder}/{ef}]({folder}/{ef}) *(Legacy content; scheduled for overhaul)*")
            else:
                lines.append(f"- `{folder}/notes.md` *(Authoring scheduled in roadmap)*")
                lines.append(f"- `{folder}/diagrams.md` *(Authoring scheduled in roadmap)*")
                lines.append(f"- `{folder}/mcqs.md` *(Authoring scheduled in roadmap)*")
            lines.append("")

    lines.extend([
        "---",
        "",
        "## 🎯 Specialized & Practice Zones (17–20)",
        "",
        "### [17. Interview Prep](17_Interview_Prep/)",
        "*Top 100 core networking questions, 60 protocol difference tables, and systems design screens.*",
        "- `17_Interview_Prep/` — Systems design, behavioral, and troubleshooting screens.",
        "",
        "### [18. GATE and Competitive Zone](18_GATE_and_Competitive_Zone/)",
        "*GATE syllabus mapping, master formula sheet, and 100+ topic-wise PYQs with verified step-by-step solutions.*",
        "- `18_GATE_and_Competitive_Zone/` — Exam-oriented practice and PYQ repository.",
        "",
        "### [19. Hands-On Labs](19_Hands_On_Labs/)",
        "*Practical packet analysis and simulation labs across Wireshark, Cisco Packet Tracer, and Python sockets.*",
        "- `19_Hands_On_Labs/` — Wireshark traces, Packet Tracer .pkt files, and socket scripts.",
        "",
        "### [20. Cheatsheets](20_Cheatsheets/)",
        "*High-yield, printable, standalone one-page reference sheets for rapid revision.*",
        "- `20_Cheatsheets/` — Comprehensive topic cheat sheets and reference cards.",
        "",
    ])

    return "\n".join(lines)


def main():
    root = Path(__file__).resolve().parent.parent

    # 1. Update PROGRESS.md
    new_matrix = generate_status_matrix(root)
    update_progress_md(root, new_matrix)

    # 2. Update INDEX.md
    new_index = generate_index_content(root)
    (root / "INDEX.md").write_text(new_index, encoding="utf-8")
    print("Regenerated INDEX.md")

    print("Index and Progress update complete!")


if __name__ == "__main__":
    main()
