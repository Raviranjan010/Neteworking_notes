# 📅 Computer Networking Study Plans

Choose the study plan that matches your current goal, available hours, and deadline. Every plan includes daily checklists, exact file links, and time budgets.

---

## Quick Navigation
- [⚡ 7-Day Exam Cram Plan](#7-day-exam-cram-plan) (College Semester / Viva)
- [💼 14-Day Interview Sprint](#14-day-interview-sprint) (SWE / SRE / DevOps / Cloud)
- [🌱 30-Day Foundation Plan](#30-day-foundation-plan) (Beginners / Campus Placements)
- [🌐 60-Day Complete Engineer Plan](#60-day-complete-engineer-plan) (CCNA / Deep Systems Mastery)
- [🏆 90-Day GATE CS/IT Mastery Plan](#90-day-gate-csit-mastery-plan) (GATE / ISRO / DRDO / PSUs)

---

## ⚡ 7-Day Exam Cram Plan

> **Target:** College semester exams, viva voce, or urgent refresh.  
> **Commitment:** 4–5 hours/day.

| Day | Focus Topic | Files to Study | Daily Goal & Deliverable |
|:---:|---|---|---|
| **Day 1** | Network Basics & Topologies | [01_Fundamentals/notes.md](01_Fundamentals/notes.md)<br/>[01_Fundamentals/diagrams.md](01_Fundamentals/diagrams.md) | Grasp transmission delays ($T_t, T_p$), switching types, and star/mesh topologies. |
| **Day 2** | Layered Architectures | [02_OSI_Model/notes.md](02_OSI_Model/notes.md)<br/>[03_TCP_IP_Model/notes.md](03_TCP_IP_Model/notes.md) | Draw the 7 OSI layers and 5-layer hybrid model. Master encapsulation headers. |
| **Day 3** | Data Link Protocols & MAC | [05_Data_Link_Layer/](05_Data_Link_Layer/)<br/>[06_Network_Devices_and_LAN/notes.md](06_Network_Devices_and_LAN/notes.md) | Solve Stop-and-Wait/GBN efficiency, CRC division, and switch vs hub differences. |
| **Day 4** | IP Addressing & Subnetting | [07_IP_Addressing/notes.md](07_IP_Addressing/notes.md)<br/>[08_Subnetting_CIDR_VLSM/notes.md](08_Subnetting_CIDR_VLSM/notes.md) | Calculate valid host ranges, subnet masks, and network/broadcast IDs for CIDR prefixes. |
| **Day 5** | Network Layer & Routing | [09_Network_Layer_Protocols/](09_Network_Layer_Protocols/)<br/>[10_Routing/notes.md](10_Routing/notes.md) | Master IPv4 header fields, ARP flow, Dijkstra SPF step table, and Bellman-Ford. |
| **Day 6** | Transport Layer Protocols | [11_Transport_Layer/notes.md](11_Transport_Layer/notes.md)<br/>[11_Transport_Layer/diagrams.md](11_Transport_Layer/diagrams.md) | TCP 3-way handshake, 4-way teardown, congestion control (Tahoe vs Reno), TCP vs UDP. |
| **Day 7** | Application Layer & Speed Revision | [12_Application_Layer/notes.md](12_Application_Layer/notes.md)<br/>[20_Cheatsheets/](20_Cheatsheets/) | DNS resolution steps, HTTP/1.1 vs HTTP/2, DHCP DORA, and review top 100 revision points. |

---

## 💼 14-Day Interview Sprint

> **Target:** Software engineering, SRE, systems infrastructure, and cloud interviews.  
> **Commitment:** 2–3 hours/day.

- [ ] **Day 1:** OSI vs TCP/IP Models & Packet Encapsulation ([02_OSI_Model/notes.md](02_OSI_Model/notes.md), [03_TCP_IP_Model/notes.md](03_TCP_IP_Model/notes.md))
- [ ] **Day 2:** The Ultimate Interview Question: *"What happens when you type a URL into a browser?"* ([17_Interview_Prep/](17_Interview_Prep/))
- [ ] **Day 3:** IP Addressing, Private IPs (RFC 1918), and Subnetting Math ([07_IP_Addressing/notes.md](07_IP_Addressing/notes.md), [08_Subnetting_CIDR_VLSM/notes.md](08_Subnetting_CIDR_VLSM/notes.md))
- [ ] **Day 4:** Network Layer Protocols: ARP, ICMP, and NAT/PAT ([09_Network_Layer_Protocols/](09_Network_Layer_Protocols/))
- [ ] **Day 5:** TCP Deep Dive: 3-Way Handshake, Sequence/Ack numbers, and Teardown ([11_Transport_Layer/notes.md](11_Transport_Layer/notes.md))
- [ ] **Day 6:** TCP Reliability: Congestion Control (Slow Start, Tahoe vs Reno), Flow Control, and TIME_WAIT ([11_Transport_Layer/notes.md](11_Transport_Layer/notes.md))
- [ ] **Day 7:** TCP vs UDP & Modern Transports: QUIC and HTTP/3 ([11_Transport_Layer/notes.md](11_Transport_Layer/notes.md), [12_Application_Layer/notes.md](12_Application_Layer/notes.md))
- [ ] **Day 8:** DNS Architecture: Hierarchy, Record types (A, AAAA, CNAME, MX), TTL, and Caching ([12_Application_Layer/notes.md](12_Application_Layer/notes.md))
- [ ] **Day 9:** HTTP Evolution: HTTP/1.0, 1.1 (Keep-Alive, Pipelining), HTTP/2 (Multiplexing), HTTP/3 ([12_Application_Layer/notes.md](12_Application_Layer/notes.md))
- [ ] **Day 10:** TLS 1.2 vs 1.3 Handshake & HTTPS Security ([13_Network_Security/](13_Network_Security/))
- [ ] **Day 11:** Load Balancing (L4 vs L7), Reverse Proxies, and CDNs ([15_Modern_Networking/](15_Modern_Networking/))
- [ ] **Day 12:** Cloud Networking: VPCs, Subnets, Gateways, and Security Groups ([15_Modern_Networking/](15_Modern_Networking/))
- [ ] **Day 13:** Troubleshooting Methodologies & Command Outputs (`ping`, `traceroute`, `curl`, `netstat`) ([16_Troubleshooting_and_Tools/](16_Troubleshooting_and_Tools/))
- [ ] **Day 14:** Review 60 Differences & 500 Rapid-Fire Q&A ([17_Interview_Prep/](17_Interview_Prep/))

---

## 🌱 30-Day Foundation Plan

> **Target:** Complete beginners, campus placements (TCS, Infosys, Wipro, Accenture, Cognizant), and core CS building.  
> **Commitment:** 1.5–2 hours/day.

```
Week 1: Fundamentals & Layered Models
├── Day 1-2:   01_Fundamentals (Basics, Topologies, Delays)
├── Day 3-4:   02_OSI_Model (7 Layers & Encapsulation)
├── Day 5-6:   03_TCP_IP_Model (5-Layer Hybrid & Protocol Mapping)
└── Day 7:     Weekly Revision & 01-03 MCQs

Week 2: Physical & Data Link Layers
├── Day 8-9:   04_Physical_Layer (Signals, Nyquist/Shannon, Media)
├── Day 10-12: 05_Data_Link_Layer (Framing, CRC, ARQ, CSMA/CD)
├── Day 13:    06_Network_Devices_and_LAN (Hubs, Switches, VLANs)
└── Day 14:    Weekly Revision & 04-06 MCQs

Week 3: Addressing, Subnetting & Routing
├── Day 15-16: 07_IP_Addressing (IPv4 Classes & IPv6 Basics)
├── Day 17-18: 08_Subnetting_CIDR_VLSM (Subnet Calculations)
├── Day 19-20: 09_Network_Layer_Protocols (IPv4 Header, ARP, ICMP, NAT)
├── Day 21:    10_Routing (Dijkstra SPF & Distance Vector)
└── Day 22:    Weekly Revision & 07-10 MCQs

Week 4: Transport, Application & Security
├── Day 23-24: 11_Transport_Layer (TCP Handshake, Congestion, UDP)
├── Day 25-26: 12_Application_Layer (DNS, HTTP/HTTPS, DHCP)
├── Day 27:    13_Network_Security (Basics of Crypto & Firewalls)
├── Day 28:    16_Troubleshooting_and_Tools (Ping, Traceroute, Wireshark)
└── Day 29-30: Comprehensive Mock Test & Cheatsheet Review
```

---

## 🌐 60-Day Complete Engineer Plan

> **Target:** Aspiring network engineers, CCNA 200-301 candidates, and systems engineers.  
> **Commitment:** 2 hours/day including hands-on CLI practice.

- **Days 1–8:** Networking Fundamentals, Signals, Physical Media, and Cabling standards (Modules 01 & 04).
- **Days 9–18:** Data Link Layer, Ethernet 802.3, Switching Internals, STP/RSTP, and VLAN Trunking 802.1Q (Modules 05 & 06 + Packet Tracer Labs 1–4).
- **Days 19–28:** IPv4/IPv6 Addressing, Subnetting mastery, VLSM design, and Supernetting (Modules 07 & 08 + 45 Numericals).
- **Days 29–38:** Network Layer Protocols, IPv4/v6 Headers, ARP, ICMP, DHCP Relay, and NAT/PAT (Module 09 + Packet Tracer Labs 5–7).
- **Days 39–48:** Routing protocols: Static Routes, OSPF Single/Multi-Area, and BGP peering (Module 10 + Packet Tracer Labs 8–10).
- **Days 49–54:** Transport & Application Protocols, TCP internals, Wireshark packet capture analysis (Modules 11 & 12 + Wireshark Labs 1–6).
- **Days 55–58:** Network Security: Standard/Extended ACLs, Port Security, Firewalls, and VPNs (Module 13 + Packet Tracer Labs 11–13).
- **Days 59–60:** Complete troubleshooting walkthroughs and Capstone network design project (Modules 16 & 19).

---

## 🏆 90-Day GATE CS/IT Mastery Plan

> **Target:** Top percentile in GATE CS/IT, UGC NET, ISRO, and DRDO.  
> **Commitment:** 2–3 hours/day with heavy emphasis on numericals and previous-year questions (PYQs).

| Phase | Days | Modules Covered | High-Yield GATE Focus Areas |
|---|:---:|---|---|
| **Phase 1: Foundations & Media** | Days 1–15 | 01, 04 | Transmission delay ($L/R$), Propagation delay ($d/v$), Total end-to-end latency over $n$ links, Nyquist formula ($2B \log_2 L$), Shannon noisy capacity ($B \log_2(1 + \text{SNR})$). |
| **Phase 2: Data Link & MAC** | Days 16–35 | 05, 06 | Bit/Byte stuffing, CRC generator division, 2D parity, Hamming distance/codes, Stop-and-Wait ($\eta = \frac{1}{1+2a}$), Go-Back-N, Selective Repeat window sizing ($2^{k-1}$), Pure ALOHA (18.4%), Slotted ALOHA (36.8%), CSMA/CD minimum frame size ($2 \cdot T_p \cdot B$). |
| **Phase 3: Addressing & Subnetting** | Days 36–50 | 07, 08 | CIDR address allocation, valid subnets, subnet zero, host requirement sizing, supernetting aggregation, longest prefix match table lookups. |
| **Phase 4: Network Layer & Routing** | Days 51–65 | 09, 10 | IPv4 Header: IHL, Total Length, Fragmentation offset in 8-byte units, Flags (DF/MF), Checksum computation, Distance Vector iterations and count-to-infinity, Dijkstra SPF step tables. |
| **Phase 5: Transport & Congestion** | Days 66–78 | 11 | Sequence and Ack number tracking, Window wrap-around time, TCP Tahoe vs Reno congestion window growth rounds, RTO timer estimation using EWMA, Maximum TCP throughput. |
| **Phase 6: Application & Security** | Days 79–85 | 12, 13 | HTTP non-persistent vs persistent RTT delays, DNS iterative vs recursive query counting, RSA encryption/decryption numericals, Diffie-Hellman key exchange. |
| **Phase 7: PYQs & Full Mocks** | Days 86–90 | 18, 20 | Solve topic-wise PYQs from 2000–2026, attempt 4 full-length 30-question mock tests, review master formula sheet in [18_GATE_and_Competitive_Zone/formula_sheet.md](18_GATE_and_Competitive_Zone/formula_sheet.md). |
