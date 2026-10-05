# 🚀 Start Here: Your Computer Networking Journey

Welcome to the **Computer Networking Mastery** repository! Whether you are preparing for your university semester exam tomorrow, tackling the GATE CS/IT paper, walking into a high-stakes tech interview at Google or Amazon, or training for CCNA/DevOps roles, this guide will orient you in **5 minutes**.

---

## 🎨 Visual Colour System Used in This Repo

To make complex flows, headers, and topologies instantly recognizable across all Mermaid and SVG diagrams, we use a uniform color language:

- 🟦 **Blue (`#0284c7` / `#e0f2fe`)**: Sender / Client / Source host / Initiator
- 🟩 **Green (`#15803d` / `#dcfce7`)**: Receiver / Server / Destination host / Success state
- 🟥 **Red (`#e11d48` / `#ffe4e6`)**: Packet loss / Collision / Attack vector / Error state
- 🟨 **Amber (`#d97706` / `#fef3c7`)**: Header fields / Control flags / Intermediate routers / Warnings
- 🟪 **Purple (`#a21caf` / `#fae8ff`)**: Encapsulation layers / Protocol tags (e.g. 802.1Q)
- ⬜ **Slate / Neutral**: Transmission physical medium / Backbones

---

## 🎯 Step 1: Identify Your Track

Select your profile below to get your exact reading path and priority topics:

### 🟢 Track 1: Absolute Beginner / First-Time Learner
- **Your Goal:** Build rock-solid mental models of how the Internet works from the ground up without getting buried in raw jargon.
- **Your Path:**
  1. [01_Fundamentals](01_Fundamentals/notes.md) — What is a network, topologies, delays, packet vs circuit switching.
  2. [02_OSI_Model](02_OSI_Model/notes.md) & [03_TCP_IP_Model](03_TCP_IP_Model/notes.md) — How layers cooperate to deliver a packet.
  3. [04_Physical_Layer](04_Physical_Layer/) — Bits, signals, cables, and media.
  4. [05_Data_Link_Layer](05_Data_Link_Layer/) — Framing, error detection (CRC), and MAC addresses.
  5. [06_Network_Devices_and_LAN](06_Network_Devices_and_LAN/notes.md) — Hubs, switches, and collision/broadcast domains.
  6. [07_IP_Addressing](07_IP_Addressing/notes.md) & [08_Subnetting_CIDR_VLSM](08_Subnetting_CIDR_VLSM/notes.md) — IP scheme and subnetting.
  7. [09_Network_Layer_Protocols](09_Network_Layer_Protocols/) & [10_Routing](10_Routing/notes.md) — IPv4/v6, ARP, ICMP, and routing algorithms.
  8. [11_Transport_Layer](11_Transport_Layer/notes.md) — TCP 3-way handshake, reliability, and UDP.
  9. [12_Application_Layer](12_Application_Layer/notes.md) — DNS, HTTP/HTTPS, and DHCP.
- **Recommended Schedule:** [30-Day Foundation Plan](STUDY_PLANS.md#30-day-foundation-plan) (1.5–2 hours/day).

---

### 🎓 Track 2: College Semester Exams (B.Tech / BCA / MCA / BSc)
- **Your Goal:** Score top grades in written descriptive papers, solve typical numericals, and clear the university viva.
- **Priority Areas:**
  - Layer comparisons: OSI vs TCP/IP (Module 02 & 03).
  - Data Link calculations: Stop-and-Wait, Go-Back-N, Selective Repeat efficiency, and CRC ([05_Data_Link_Layer](05_Data_Link_Layer/)).
  - CSMA/CD minimum frame size formulas ([05_Data_Link_Layer](05_Data_Link_Layer/)).
  - Subnetting: Find network ID, broadcast ID, and valid host range (Module 08).
  - Distance Vector (Bellman-Ford) and Link State (Dijkstra) step-by-step tables (Module 10).
  - TCP congestion control phases and header layout (Module 11).
  - DNS resolution and HTTP persistent vs non-persistent timing (Module 12).
- **Recommended Schedule:** [7-Day Exam Cram](STUDY_PLANS.md#7-day-exam-cram-plan) or [30-Day Plan](STUDY_PLANS.md#30-day-foundation-plan).

---

### 🏆 Track 3: GATE CS/IT & PSU Aspirants (ISRO, DRDO, NIELIT, UGC NET)
- **Your Goal:** Score 100% on the 6–10 marks of Computer Networks. Master numerical questions (NAT), multiple select questions (MSQ), and tricky edge cases.
- **Non-Negotiable Topics:**
  - Delays & Bandwidth-Delay Product (Module 01).
  - Shannon & Nyquist channel capacity ([04_Physical_Layer](04_Physical_Layer/)).
  - Framing (Bit/Byte stuffing), CRC generator math, Hamming distance ([05_Data_Link_Layer](05_Data_Link_Layer/)).
  - Flow Control: Efficiency formulas $\eta = \frac{N}{1 + 2a}$, sequence numbers, window sizing ([05_Data_Link_Layer](05_Data_Link_Layer/)).
  - Medium Access: Pure/Slotted ALOHA throughput, CSMA/CD $T_t \ge 2T_p$, Exponential Backoff ([05_Data_Link_Layer](05_Data_Link_Layer/)).
  - Subnetting, Supernetting, and Longest Prefix Match (Module 08 & 10).
  - IPv4 Header: Fragmentation offsets, DF/MF flags, Total Length vs Header Length ([09_Network_Layer_Protocols](09_Network_Layer_Protocols/)).
  - Routing: Count-to-infinity, Split Horizon, Distance Vector iterations, Dijkstra SPF (Module 10).
  - TCP Congestion Control: Tahoe vs Reno `cwnd` growth, `ssthresh`, timeout vs 3-dup ACKs, RTO calculation (Module 11).
  - Check the dedicated syllabus mapping & PYQs in [18_GATE_and_Competitive_Zone/](18_GATE_and_Competitive_Zone/).
- **Recommended Schedule:** [90-Day GATE Plan](STUDY_PLANS.md#90-day-gate-csit-mastery-plan).

---

### 💼 Track 4: Product Company Software Engineering & SRE Interviews
- **Your Goal:** Crack networking & systems questions at Amazon, Google, Microsoft, Meta, Uber, and top startups.
- **Top Questions You Must Master:**
  - *"What happens when you type a URL into a browser and press Enter?"* (Detailed 12-step breakdown in [17_Interview_Prep](17_Interview_Prep/)).
  - TCP vs UDP: when to use which, head-of-line blocking, connection establishment, and TIME_WAIT state (Module 11).
  - DNS: hierarchical resolution, record types (A, CNAME, MX, TXT), TTL, and DNS caching (Module 12).
  - HTTP evolution: HTTP/1.1 vs HTTP/2 vs HTTP/3 (QUIC) (Module 12).
  - Load balancing: L4 vs L7, reverse proxy vs forward proxy, sticky sessions ([15_Modern_Networking](15_Modern_Networking/)).
  - Network troubleshooting: latency spikes, packet loss, MTU issues, and Wireshark inspection ([16_Troubleshooting_and_Tools](16_Troubleshooting_and_Tools/)).
  - Review [17_Interview_Prep/](17_Interview_Prep/) and [20_Cheatsheets/](20_Cheatsheets/).
- **Recommended Schedule:** [14-Day Interview Sprint](STUDY_PLANS.md#14-day-interview-sprint).

---

### 🌐 Track 5: Network Engineer / CCNA / DevOps / Sysadmin
- **Your Goal:** Practical command-line expertise, enterprise LAN design, IP planning, and troubleshooting.
- **Key Modules:**
  - Switching & LAN: VLANs, 802.1Q trunking, STP/RSTP, EtherChannel (Module 06).
  - Subnetting & VLSM: Fast CIDR math, host sizing, route summarization (Module 08).
  - Network Protocols: ARP, ICMP, DHCP Relay, NAT/PAT ([09_Network_Layer_Protocols](09_Network_Layer_Protocols/)).
  - Enterprise Routing: OSPF single/multi-area, BGP basics (Module 10).
  - Network Security: ACLs, Firewalls, IPsec VPNs, 802.1X ([13_Network_Security](13_Network_Security/)).
  - CLI & Tools: Cisco IOS commands, Wireshark, ping, traceroute, netstat ([16_Troubleshooting_and_Tools](16_Troubleshooting_and_Tools/)).
  - Hands-On Practice: Complete all 15 CLI labs in [19_Hands_On_Labs/](19_Hands_On_Labs/).
- **Recommended Schedule:** [60-Day Complete Engineer Plan](STUDY_PLANS.md#60-day-complete-engineer-plan).

---

## 📖 The 4-Step Study Method for Every Topic

To ensure maximum retention, use this 4-step workflow for every numbered module:

```
┌─────────────────────────────────────────────────────────────┐
│  Step 1: Read notes.md (45–60 min)                          │
│  - Understand "Why This Exists" real-world story            │
│  - Grasp definitions and everyday analogies                 │
│  - Study protocol formats, algorithms, and RFC details      │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 2: Study diagrams.md (20–30 min)                      │
│  - Inspect Mermaid sequences, flowcharts, and state machines│
│  - Trace packet hops and header changes                     │
│  - Recreate the core diagram on paper from memory           │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 3: Solve numericals.md & mcqs.md (45–60 min)          │
│  - Solve Level 1 (Basic), Level 2 (Exam), Level 3 (GATE)     │
│  - Attempt MCQs, MSQs, and NATs with answers hidden         │
│  - Read explanations for EVERY question, especially wrongs  │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 4: Review cheatsheet.md & interview_qa.md (15–20 min) │
│  - Revisit key tables, port numbers, and header bit sizes   │
│  - Practice 30-second rapid-fire answers aloud              │
│  - Check off items in the Quick Revision Checklist          │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Recommended Practice Tools

To bridge theory and practice, install and practice with these free industry tools:

| Tool | Purpose | Download / Platform |
|---|---|---|
| **Cisco Packet Tracer** | Visual LAN/WAN topology building and Cisco CLI simulation | [NetAcad](https://www.netacad.com/courses/packet-tracer) (Free with account) |
| **Wireshark** | Real-time packet capture, header dissection, and protocol analysis | [wireshark.org](https://www.wireshark.org/) (Free & Open Source) |
| **Python 3** | Network socket programming, subnetting math (`ipaddress`), and protocol scripting | [python.org](https://www.python.org/) |
| **GNS3 / EVE-NG** | Advanced multi-vendor network emulation (optional for CCNA/CCNP) | [gns3.com](https://www.gns3.com/) |

---

## 🔑 Key Habits for Success

1. **Focus on *Why* before *How*:** Protocols exist to solve specific physics, hardware, or coordination problems (e.g., CRC exists because physical channels have thermal noise; CSMA/CD exists because shared wires collide).
2. **Never memorize blindly:** When learning a header, understand *why* each field is required (e.g., TTL prevents infinite routing loops).
3. **Write calculations on paper:** Subnetting, Hamming codes, and sliding-window arithmetic become second nature only when computed by hand.
4. **Teach or explain aloud:** If you can explain the difference between a switch and a router to a friend or a rubber duck in 60 seconds, you own the concept.

Ready? Choose your first module in [INDEX.md](INDEX.md) or start directly at [01_Fundamentals/notes.md](01_Fundamentals/notes.md)!
