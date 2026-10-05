# Computer Networking Mastery

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GATE Weight](https://img.shields.io/badge/GATE%20CS%2FIT-6--10%20Marks-orange.svg)](18_GATE_and_Competitive_Zone/README.md)
[![Status](https://img.shields.io/badge/Status-Active%20Revamp-blueviolet.svg)](PROGRESS.md)

> **The ultimate, visual, zero-to-advanced Computer Networking repository.**  
> Designed for complete beginners, college university exams, GATE CS/IT, campus placements, product engineering interviews (Amazon, Google, Microsoft), and CCNA/Network+ industry certifications.

---

## 🎯 What, Who, and Why

- **What:** A self-contained, crystal-clear, visual, and mathematically rigorous curriculum covering computer networking from physical bits up to distributed web applications and modern cloud architectures.
- **Who:** Absolute beginners with zero prior networking background, college engineering students, GATE/PSU aspirants preparing for numericals & MSQs, software engineers preparing for systems/infrastructure interviews, and network engineers aiming for CCNA/Network+.
- **Why:** Most networking tutorials are either dry RFC dumps, vague high-level slide decks, or scattered across disjointed sites. This repo explains **why** a technology exists before **what** it is and **how** it works, backed by **Mermaid diagrams, verified formulas, Python simulation scripts, real packet headers, and exam-proven questions**.

---

## 🧭 How to Learn From This Repository

1. **Pick your target path** in [START_HERE.md](START_HERE.md) based on your deadline and learning goal.
2. **Follow topics in numbered sequence** (bottom of the protocol stack to top) for the deepest intuition.
3. **Read `notes.md`** first — every concept starts with a simple real-world analogy and step-by-step breakdown.
4. **Inspect `diagrams.md`** — study the Mermaid sequence, flowcharts, and packet structures.
5. **Solve `numericals.md`** — master calculation problems with step-by-step verified solutions.
6. **Self-test with `mcqs.md`** — 50+ balanced questions per topic (MCQ, MSQ, NAT, output scenarios) with hidden answers and misconceptions debunked.

---

## 🗺️ Visual Learning Roadmap

```mermaid
flowchart TD
    subgraph S1["Level 1: Foundations & Physical Layer"]
        M01["01 Fundamentals<br/>(Topologies, Delays, Switching)"] --> M02["02 OSI Model<br/>(7 Layers, Encapsulation)"]
        M02 --> M03["03 TCP/IP Model<br/>(5-Layer Hybrid, Packet Hop)"]
        M03 --> M04["04 Physical Layer<br/>(Signals, Nyquist/Shannon, Media)"]
    end

    subgraph S2["Level 2: Link Layer & Local Area Networks"]
        M04 --> M05["05 Data Link Layer<br/>(Framing, CRC, ARQ, CSMA/CD, Ethernet)"]
        M05 --> M06["06 Network Devices & LAN<br/>(Switches, STP, VLANs, Broadcast Domains)"]
    end

    subgraph S3["Level 3: Internet Layer & Routing"]
        M06 --> M07["07 IP Addressing<br/>(IPv4 Classes, Special IPs, IPv6 Basics)"]
        M07 --> M08["08 Subnetting, CIDR & VLSM<br/>(Calculations, Aggregation, Wildcards)"]
        M08 --> M09["09 Network Layer Protocols<br/>(IPv4/IPv6 Headers, ARP, ICMP, NAT, Fragmentation)"]
        M09 --> M10["10 Routing<br/>(Dijkstra, Bellman-Ford, OSPF, BGP, RIP)"]
    end

    subgraph S4["Level 4: End-to-End Transport & Applications"]
        M10 --> M11["11 Transport Layer<br/>(TCP Handshake, Reno/Tahoe, RTO, UDP, QUIC)"]
        M11 --> M12["12 Application Layer<br/>(DNS, HTTP/1-3, Sockets, DHCP, TLS Handshake)"]
    end

    subgraph S5["Level 5: Advanced, Security & Cloud"]
        M12 --> M13["13 Network Security<br/>(Crypto, Firewalls, TLS, IPSec, Attacks & Defences)"]
        M12 --> M14["14 Wireless & Mobile<br/>(Wi-Fi 6/7, CSMA/CA, 4G/5G, Cellular)"]
        M13 --> M15["15 Modern Networking<br/>(SDN, Cloud VPC, CDN, Spine-Leaf, K8s CNI)"]
        M14 --> M15
    end

    subgraph S6["Level 6: Applied Mastery & Exam Prep"]
        M15 --> M16["16 Troubleshooting & Tools<br/>(Wireshark, tcpdump, ping, Cisco CLI, 50 Scenarios)"]
        M16 --> M17["17 Interview Prep<br/>(URL Deep Dive, Top 100 Q&A, 60 Differences)"]
        M16 --> M18["18 GATE & Competitive Zone<br/>(Syllabus Map, Formulas, PYQs, Mocks)"]
        M16 --> M19["19 Hands-On Labs<br/>(15 Packet Tracer + 8 Wireshark + Python Code)"]
        M17 --> M20["20 Cheatsheets<br/>(Ports, Protocols, Subnets, Fast Formulas)"]
        M18 --> M20
        M19 --> M20
    end

    classDef l1 fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    classDef l2 fill:#e0e7ff,stroke:#4338ca,stroke-width:2px;
    classDef l3 fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    classDef l4 fill:#dcfce7,stroke:#15803d,stroke-width:2px;
    classDef l5 fill:#fae8ff,stroke:#a21caf,stroke-width:2px;
    classDef l6 fill:#ffe4e6,stroke:#e11d48,stroke-width:2px;

    class M01,M02,M03,M04 l1;
    class M05,M06 l2;
    class M07,M08,M09,M10 l3;
    class M11,M12 l4;
    class M13,M14,M15 l5;
    class M16,M17,M18,M19,M20 l6;
```

---

## 📚 Curriculum & Module Overview

| # | Module Name | Core Highlights | Est. Time | GATE Weight | Interview Weight | Status |
|---|---|---|:---:|:---:|:---:|:---:|
| **01** | [01_Fundamentals](01_Fundamentals/notes.md) | Topologies, Delays (Tt, Tp, Tq, Tproc), Switching, BDP | 3–4 hrs | Medium | High | 🚧 Rebuilding |
| **02** | [02_OSI_Model](02_OSI_Model/notes.md) | 7 Layers, Encapsulation, Headers/Trailers, Troubleshooting | 3–4 hrs | Low–Med | Very High | 🚧 Rebuilding |
| **03** | [03_TCP_IP_Model](03_TCP_IP_Model/notes.md) | 5-Layer Hybrid Model, Packet Hop Journey, Protocol Matrix | 3–4 hrs | Medium | High | 🚧 Rebuilding |
| **04** | [04_Physical_Layer](04_Physical_Layer/) | Nyquist, Shannon Capacity, Line Coding, Media, Modulation | 4–5 hrs | Medium | Medium | 📋 Planned (Phase 2) |
| **05** | [05_Data_Link_Layer](05_Data_Link_Layer/) | CRC, Hamming, Stop-and-Wait, GBN, SR, CSMA/CD, Ethernet | 8–10 hrs | **Highest** | High | 📋 Planned (Phase 2) |
| **06** | [06_Network_Devices_and_LAN](06_Network_Devices_and_LAN/notes.md) | Hubs vs Switches, STP Elections, VLANs, 802.1Q, Domains | 5–6 hrs | Medium | High | 🚧 Rebuilding |
| **07** | [07_IP_Addressing](07_IP_Addressing/notes.md) | IPv4 Classes, Special Blocks, IPv6 Addressing, EUI-64 | 4–5 hrs | Medium | Very High | 🚧 Rebuilding |
| **08** | [08_Subnetting_CIDR_VLSM](08_Subnetting_CIDR_VLSM/notes.md) | Fast Subnetting, VLSM, CIDR Aggregation, 45 Numericals | 6–8 hrs | High | **Highest** | 🚧 Rebuilding |
| **09** | [09_Network_Layer_Protocols](09_Network_Layer_Protocols/) | IPv4 Header, Fragmentation, ARP, ICMP, NAT/PAT, IPv6 Header | 6–7 hrs | High | High | 📋 Planned (Phase 4) |
| **10** | [10_Routing](10_Routing/notes.md) | Dijkstra SPF, Bellman-Ford, OSPF, BGP, RIP, LPM | 7–8 hrs | High | High | 🚧 Rebuilding |
| **11** | [11_Transport_Layer](11_Transport_Layer/notes.md) | TCP Handshake/Teardown, Tahoe vs Reno, States, RTO, UDP | 8–10 hrs | **Highest** | **Highest** | 🚧 Rebuilding |
| **12** | [12_Application_Layer](12_Application_Layer/notes.md) | DNS, HTTP/1.1/2/3, Socket Code, DHCP DORA, TLS 1.3 | 6–8 hrs | High | **Highest** | 🚧 Rebuilding |
| **13** | [13_Network_Security](13_Network_Security/) | Cryptography (RSA/DH/AES), Firewalls, ACLs, TLS, IPsec | 6–8 hrs | Medium | High | 📋 Planned (Phase 7) |
| **14** | [14_Wireless_and_Mobile](14_Wireless_and_Mobile/) | 802.11 Wi-Fi, CSMA/CA, WPA3, 4G LTE/5G Slicing | 4–5 hrs | Low–Med | Medium | 📋 Planned (Phase 7) |
| **15** | [15_Modern_Networking](15_Modern_Networking/) | SDN, Cloud VPC, Load Balancers, CDN, Spine-Leaf, K8s CNI | 5–6 hrs | Low | Very High | 📋 Planned (Phase 8) |
| **16** | [16_Troubleshooting_and_Tools](16_Troubleshooting_and_Tools/) | Wireshark, tcpdump, ping, traceroute, Cisco CLI, 50 Scenarios | 5–6 hrs | Low | Very High | 📋 Planned (Phase 8) |
| **17** | [17_Interview_Prep](17_Interview_Prep/) | "What happens when you type a URL", Top 100 Q&A, 60 Diffs | 6–8 hrs | N/A | **Highest** | 📋 Planned (Phase 9) |
| **18** | [18_GATE_and_Competitive_Zone](18_GATE_and_Competitive_Zone/) | Syllabus Map, Master Formula Sheet, PYQ Solutions, Mocks | 10–12 hrs | **Benchmark** | Medium | 📋 Planned (Phase 9) |
| **19** | [19_Hands_On_Labs](19_Hands_On_Labs/) | 15 Packet Tracer CLI Labs, 8 Wireshark Labs, Python Code | 10–15 hrs | Medium | Very High | 📋 Planned (Phase 10) |
| **20** | [20_Cheatsheets](20_Cheatsheets/) | 100 Protocols/Ports, One-Page Revision Sheets, Formulas | 2–3 hrs | High | High | 📋 Planned (Phase 10) |

*Status key: ✅ Verified Complete | 🚧 Rebuilding / Expanding | 📋 Planned in Phase Roadmap*

---

## 🎯 Choose Your Track

| Track | Who It Is For | Recommended Path | Plan |
|---|---|---|---|
| **🟢 Absolute Beginner** | Starting from zero, wanting clear intuition | Modules 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 11 → 12 | [30-Day Plan](STUDY_PLANS.md#30-day-foundation-plan) |
| **🎓 College Exams** | University syllabus (B.Tech / BCA / MCA / BSc CS) | All modules 01 to 12 + 13 & 16 + Cheatsheets | [7-Day Crash](STUDY_PLANS.md#7-day-exam-cram-plan) |
| **🏆 GATE CS/IT** | Numerical mastery, MSQ precision, high marks | Focus: 01, 04, 05, 07, 08, 09, 10, 11 + Module 18 | [90-Day GATE Plan](STUDY_PLANS.md#90-day-gate-csit-mastery-plan) |
| **💼 Software Engineering Interviews** | Amazon, Google, Microsoft, SRE, DevOps | Focus: 02, 07, 08, 11, 12, 15, 16 + Module 17 | [14-Day Interview Plan](STUDY_PLANS.md#14-day-interview-sprint) |
| **🌐 Network Engineer / CCNA** | Enterprise LAN/WAN, Cisco CLI, operations | Focus: 04, 05, 06, 07, 08, 09, 10, 16 + Module 19 | [60-Day Deep Dive](STUDY_PLANS.md#60-day-complete-engineer-plan) |

👉 **Read the complete onboarding guide in [START_HERE.md](START_HERE.md)**.

---

## 📂 Standard File Architecture Per Topic

Every core topic folder (`01` through `16`) strictly follows this structure:

```text
<Topic_Folder>/
├── README.md        ← Module overview, time budget, prerequisites, "Where this fits" map, next links
├── notes.md         ← Full conceptual deep-dive (analogy → plain English → math/headers → real world)
├── diagrams.md      ← Mermaid sequence/flowcharts + SVG packet layouts (minimum 8-15 visual diagrams)
├── numericals.md    ← Solved calculations in 3 levels (Basic, Exam, GATE-hard) verified with Python
├── mcqs.md          ← 50+ questions (30 MCQs, 10 MSQs, 10 NAT, 5 Output scenarios) with balanced options
├── interview_qa.md  ← Top questions with 30-second summary and detailed 2-minute answers
└── cheatsheet.md    ← One-page quick revision sheet
```

---

## 🛠️ Verification & Quality Assurance

All numerical calculations, CIDR masks, throughput formulas, and checksums in this repository are verified using reproducible Python scripts in `tools/verify/`. No hand-waving or unverified numbers.

---

## 🤝 Contributing

We welcome corrections, new diagrams, verified numerical solutions, and lab scenarios. Please review [CONTRIBUTING.md](CONTRIBUTING.md) and our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
