# ANTIGRAVITY MASTER PROMPT: Computer Networking Mastery

> **How to use this file**
> 1. Open the repo (`Neteworking_notes-main`) as the workspace in Antigravity.
> 2. Save this whole file in the repo root as `MASTER_PROMPT.md` (or put Parts 1, 3, 4, 7, 8 in your workspace rules file if Antigravity supports one).
> 3. Paste the **KICK-OFF MESSAGE** (below) into the agent.
> 4. Then run the work **one phase at a time** (Part 9). Do not ask for everything in one run; the output is too large and quality drops.
> 5. After every phase, read `PROGRESS.md`, spot-check 2 files, then say "Continue to the next phase".

---

## KICK-OFF MESSAGE (paste this first)

~~~text
You are a senior network engineer, GATE CS/IT mentor and technical writer.
Read MASTER_PROMPT.md fully before doing anything. It is your specification.
Your job: transform this repository into the most complete, accurate, visual and
easy-to-navigate Computer Networking learning repo for beginners, college exams,
GATE, campus placements, company interviews and CCNA-level knowledge.

Rules of engagement:
- Work phase by phase exactly as in Part 9. Start with Phase 0.
- Never leave placeholders, "TODO", "to be continued" or "similar to above".
- Preserve the good existing content and style. Improve and extend, don't blindly rewrite.
- Use `git mv` when renaming/moving so history is kept. Fix every internal link after a move.
- After each phase: update PROGRESS.md, run the quality gates in Part 8, commit with a clear message.
- If a phase is too large for one response, finish it in several steps and tell me which files are done.
Begin with Phase 0 now.
~~~

---

# PART 1: MISSION, AUDIENCE, PRINCIPLES

## 1.1 Mission
Build a repo where **a person who knows nothing about networking can start at file 1, follow the links in order, and finish able to answer any networking question** asked in:
- **College semester exams** (CN / Data Communication)
- **GATE CS/IT** (numericals, MCQ, MSQ, NAT) and **UGC NET, ISRO, DRDO, PSU CS papers**
- **Campus placements** (TCS, Infosys, Wipro, Accenture, Capgemini, Cognizant and similar: aptitude-level CN MCQs and HR/technical rounds)
- **Product-company interviews** (Amazon, Google, Microsoft and similar: "what happens when you type a URL", TCP internals, DNS, load balancing, system-design networking)
- **Networking/cloud/DevOps/SRE roles** (CCNA/Network+ level, troubleshooting, security basics)
- **Quizzes, viva, hackathon and tech events**

## 1.2 Audience
Absolute beginner → advanced. Language must be **simple English**, short sentences, no unexplained jargon. Every new term is explained the first time it appears, and also added to `GLOSSARY.md`.

## 1.3 Non-negotiable principles
1. **Complete.** Every topic in Part 6's checklists is covered. Nothing is "left for the reader".
2. **Correct.** Every fact, number, formula and port is verified (Part 8). When unsure, say so and cite the RFC/IEEE standard instead of guessing.
3. **Easy.** Explain *why* before *what* before *how*. Use an analogy, then the real thing.
4. **Visual.** Every concept that has a flow, structure, state or comparison gets a diagram or table (Part 7).
5. **Connected.** Every topic page links to prerequisites, next topic and related topics ("Where this fits" map).
6. **Exam-ready.** Every topic has solved numericals, MCQ/MSQ/NAT, interview Q&A and a one-page cheatsheet.
7. **Not boring.** Use short real-life stories, "Why does this exist?" boxes, "Common trap" boxes, "Remember this" mnemonics, and small "Try it yourself" tasks.
8. **Navigable.** One root README, one index, consistent filenames, prev/next links on every page.

## 1.4 Writing style rules
- Start every section with a one-line **plain definition**, then an analogy, then details.
- Max ~5 lines per paragraph. Prefer tables, numbered steps and diagrams over long text.
- Use these callout styles consistently (GitHub-flavoured):
  - `> **💡 Why this exists:** ...`
  - `> **⚠️ Common trap:** ...`
  - `> **🧠 Remember:** ...` (mnemonic)
  - `> **🎯 Exam/Interview tip:** ...`
  - `> **🛠️ Try it yourself:** ...`
  - `> **📌 GATE:** ...` (only where GATE tests it)
- Every notes file ends with: **Summary (5-10 bullets) → Quick Revision Checklist → "Next:" link**.
- No emojis in headings except the single callout icons above. No filler motivational text.

---

# PART 2: AUDIT OF THE CURRENT REPO (what is wrong today)

Fix all of these in Phase 0/1.

| # | Problem found | Fix |
|---|---|---|
| 1 | Root `README.md` is only 4 lines; real README is inside `Computer-Networking-Mastery/` | Rewrite root README as the landing page (Part 5, file R1) |
| 2 | Repo/folder name typo: `Neteworking_notes` | Rename remote repo to `Computer-Networking-Mastery` (tell the user to do on GitHub); fix all text references |
| 3 | README lists topics 10-14 and 5 cheatsheets that **do not exist** (also says "Section 12 is crucial", "Master section 14") | Create them (Part 6) or remove claims until built |
| 4 | `CONTENT_STATUS.md` is stale (says 4 topics done, "12/51 files") but 9 topics exist | Delete it, replace with auto-maintained `PROGRESS.md` |
| 5 | `09_Network_Devices/` has **no `diagrams.md`** | Create it |
| 6 | `07_Transport_Layer/mcqs.md` title says "Troubleshooting & Scenario-Based"; several other MCQ titles are inconsistent | Standardise titles |
| 7 | Stray Chinese text in `03_TCP_IP_Model/notes.md`: heading "快递 System (Courier)" | Replace with "Courier System" |
| 8 | **MCQ answer bias**: answer B is correct in 14-24 of 30 questions per file (e.g. Network Devices: B=24, A=2, C=4, D=0) | Re-balance so A/B/C/D are each ~25% per file; shuffle options |
| 9 | **No images/Mermaid at all**; only ASCII art (210 code blocks) | Add Mermaid + SVG assets (Part 7); keep ASCII only for tiny headers/bit layouts |
| 10 | No Data Link layer, no Physical layer, no Network Security, no Wireless, no Troubleshooting, no Interview, no GATE content | Create (Part 6) |
| 11 | Only 3 practice problems in Subnetting; Transport has almost no numericals; **zero numericals for delay, sliding window, CSMA/CD, CRC, Dijkstra/DV, cwnd** | Create `numericals.md` per topic (Part 4) |
| 12 | MCQs are single-answer only. GATE also has **MSQ** and **NAT** | Add them (Part 4, mcqs template) |
| 13 | TCP congestion control section says loss → "cut in half, return to slow start or fast recovery" (blurs Tahoe/Reno) | Rewrite precisely (Part 5, file 07) |
| 14 | Application layer covers only DNS, HTTP/HTTPS, Email, DHCP | Extend (Part 5, file 08) |
| 15 | `OSI`/`TCP-IP` call "Gateway" a Layer 7 device without explaining the term is overloaded | Clarify (Part 5, files 02/09) |
| 16 | README "Interview weight" table is a guess (e.g. "Security 10%") with no source | Replace with a **GATE-syllabus-based** weightage map (honestly labelled "approximate") |
| 17 | No glossary, no index, no prev/next navigation, no license, no contributing guide, no learning paths | Create (Part 3) |

---

# PART 3: TARGET REPOSITORY ARCHITECTURE

Renumber so the order follows how the subject is actually learned (bottom of the stack to top), and so the previously missing layers fit naturally. Use `git mv` for existing folders.

~~~text
Computer-Networking-Mastery/
├── README.md                      ← landing page (what, who, how, roadmap, progress)
├── START_HERE.md                  ← 5-minute guide: pick your path (beginner / GATE / interview / CCNA)
├── INDEX.md                       ← master table of contents with every file linked
├── GLOSSARY.md                    ← A-Z of every term (1-2 lines each + link to topic)
├── PROGRESS.md                    ← checklist table of all modules/files, auto-updated by agent
├── STUDY_PLANS.md                 ← 7-day crash, 30-day, 60-day, GATE 90-day, interview 14-day
├── LICENSE  CONTRIBUTING.md  CODE_OF_CONDUCT.md
├── .github/
│   ├── workflows/links.yml        ← markdown link checker
│   └── ISSUE_TEMPLATE/ (typo.md, wrong-answer.md, topic-request.md)
├── assets/
│   ├── images/<topic>/*.svg|png   ← exported diagrams, packet headers, screenshots
│   └── source/*.drawio|*.excalidraw
│
├── 01_Fundamentals/               (existing 01, EXTENDED)
├── 02_OSI_Model/                  (existing 02, extended)
├── 03_TCP_IP_Model/               (existing 03, extended)
├── 04_Physical_Layer/             (NEW)
├── 05_Data_Link_Layer/            (NEW, biggest GATE area)
├── 06_Network_Devices_and_LAN/    (existing 09, MOVED + extended: STP, VLAN, etc.)
├── 07_IP_Addressing/              (existing 04, extended)
├── 08_Subnetting_CIDR_VLSM/       (existing 05, extended)
├── 09_Network_Layer_Protocols/    (NEW: IPv4 header, fragmentation, ARP, ICMP, NAT, IPv6 deep, multicast)
├── 10_Routing/                    (existing 06, extended)
├── 11_Transport_Layer/            (existing 07, extended)
├── 12_Application_Layer/          (existing 08, extended)
├── 13_Network_Security/           (NEW)
├── 14_Wireless_and_Mobile/        (NEW)
├── 15_Modern_Networking/          (NEW: SDN, MPLS, QoS, CDN, cloud/VPC, data center, IoT)
├── 16_Troubleshooting_and_Tools/  (NEW)
├── 17_Interview_Prep/             (NEW)
├── 18_GATE_and_Competitive_Zone/  (NEW)
├── 19_Hands_On_Labs/              (NEW)
└── 20_Cheatsheets/                (NEW)
~~~

**Each topic folder (01-16) contains exactly these files** (so navigation is identical everywhere):

~~~text
README.md        ← topic landing page: goals, prerequisites, time needed, "where this fits" map, file list, prev/next
notes.md         ← the full explanation
diagrams.md      ← Mermaid + SVG visual guide
numericals.md    ← solved calculation problems (ONLY for formula/calculation topics; see Part 4.4)
mcqs.md          ← 50+ questions: MCQ + MSQ + NAT, with answers & explanations
interview_qa.md  ← 20-40 real questions with model answers (30-sec / 2-min versions)
cheatsheet.md    ← one-page revision sheet for that topic
~~~

Folders 17-20 have their own structure (Part 6).

---

# PART 4: STANDARD TEMPLATES

## 4.1 `README.md` (topic landing page)

~~~markdown
# <NN>. <Topic Name>

> One-sentence promise: "After this module you can ...".

| ⏱ Time | 🎯 Level | 📌 GATE weight | 💼 Interview weight |
|---|---|---|---|
| 3-4 h | Beginner→Intermediate | Medium | High |

## Where this fits
(Mermaid flowchart showing the previous topic → THIS topic → next topic, with related topics dotted)

## Prerequisites
- [Topic X](../0X_.../README.md)

## What you will learn (checklist)
- [ ] ...

## Files in this module
| File | What it gives you | Time |
|---|---|---|
| [notes.md](notes.md) | ... | ... |
...

## ⬅️ Previous: [..] | ➡️ Next: [..]
~~~

## 4.2 `notes.md`

Section order (keep your existing good sections, add the missing ones):

~~~text
1. Why this topic exists (problem it solves, with a real-life story)
2. Real-world analogy
3. Core concepts, in simple steps  (each concept: Definition → Analogy → How it works → Diagram link → Example)
4. Deep dive (header formats, algorithms, state machines, formulas)
5. Worked examples (small)
6. Real-world scenarios (home, office, ISP, cloud)
7. Comparison tables (X vs Y)
8. Common mistakes / traps
9. Memory tricks (mnemonics)
10. Exam & interview insights (what is asked, how to answer)
11. Summary (5-10 bullets)
12. Quick revision checklist
13. Next topic link
~~~

## 4.3 `diagrams.md`
- Each diagram: **title → 1-line "what to notice" → diagram → "How to read it" bullets**.
- Use **Mermaid** (`sequenceDiagram`, `flowchart`, `stateDiagram-v2`, `graph`) for flows/handshakes/state machines/topologies, and **SVG/PNG in `assets/images/<topic>/`** for packet headers, device photos, Wireshark screenshots.
- Keep ASCII only for small bit-layouts.
- Minimum diagrams per topic: 8 (15 for big topics such as Transport, Routing, Data Link).

## 4.4 `numericals.md` (needed for: 01 Fundamentals, 04, 05, 06, 07 IP, 08, 09, 10, 11, 12 partly)

~~~text
## Formula sheet (all formulas of this topic, with units & when to use)
## Solved problems, in 3 levels
  Level 1: Basic (10)    Level 2: Exam-standard (10)    Level 3: GATE-hard (10)
Each problem:
  Question → Given → Find → Formula used → Step-by-step solution → Final answer → "Trap" note
## Practice problems (10, answers at the bottom, hidden in <details>)
~~~
Every numeric answer **must be verified with a small Python script** (Part 8.2) before being written.

## 4.5 `mcqs.md`

~~~text
Part A: MCQ (single correct)        - 30 questions (10 easy / 10 medium / 10 hard)
Part B: MSQ (multiple correct)      - 10 questions (GATE style: may have 1-4 correct)
Part C: NAT (numerical answer)      - 10 questions (answer is a number)
Part D: Scenario / output-based      - 5 questions (given ping/traceroute/Wireshark/command output)
Answer key table at the end + score interpretation.
~~~
Rules:
- **Balance answers**: across Part A, A/B/C/D must each be correct 6-9 times. Randomise option order.
- Plausible distractors that match *common misconceptions* (and the explanation says which misconception).
- Each question has: tag `[Company]`, `[GATE-style]` or `[Concept]`, difficulty, answer, 2-4 line explanation.
- Wrap answers in `<details><summary>Answer</summary> ... </details>` so beginners can't see them by accident.
- Add the **GATE previous-year question list** to `18_GATE_and_Competitive_Zone/` (not here) and link it.

## 4.6 `interview_qa.md`
Each question: **Level (Basic/Medium/Hard) → Question → 30-second answer → Full answer (with diagram/example) → Likely follow-ups → Common wrong answers**.
Group as: Definitions, Differences (X vs Y), How does it work, Scenario/troubleshooting, Design, Trick questions.

## 4.7 `cheatsheet.md`
One screen/page: key tables, formulas, ports, header sizes, mnemonics, top-10 interview Q one-liners. Printable.

---

# PART 5: FILE-BY-FILE INSTRUCTIONS FOR EXISTING FILES

For each file: **KEEP** = preserve, **ADD** = new content, **FIX** = correct, **REMOVE** = delete.

## Root
**R1 `README.md` (4 lines)** → REWRITE completely: title, badges (license, stars, "PRs welcome"), what/who/why, 6-line "how to learn from this repo", mermaid learning-roadmap, table of all modules with status + GATE/Interview weight + estimated hours, paths (Beginner / GATE / Interview / CCNA) linking to `START_HERE.md`, how to contribute, license.

**R2 `Computer-Networking-Mastery/README.md` (374 lines)** → Move the good parts (roadmap, study method, interview strategy, key skills, tools, tips) into `START_HERE.md`, `STUDY_PLANS.md`, `17_Interview_Prep/`. REMOVE the false repository-structure tree and the invented "interview weight" percentages. Delete this file after moving (root README replaces it).

**R3 `CONTENT_STATUS.md`** → REMOVE. Replace by `PROGRESS.md` (table: module × files × status ✅/🚧/❌, plus "last verified" date).

## 01_Fundamentals
**notes.md (457 lines)**
- KEEP: postal analogy, nodes/links, 5 components, types, topologies, transmission modes, client-server vs P2P.
- ADD: history & evolution (ARPANET → Internet), Internet structure (access network, ISP tiers 1/2/3, IXP, backbone), network standards bodies (IEEE, IETF/RFC, ISO, ITU, W3C, ICANN/IANA), PAN/LAN/CAN/MAN/WAN/SAN, protocol definition (syntax, semantics, timing), **switching techniques** (circuit, packet, message; datagram vs virtual circuit; comparison table), **delay components** (transmission, propagation, queuing, processing; formulas, end-to-end delay over n links), **bandwidth-delay product**, throughput vs goodput vs bandwidth, bottleneck link, packet loss, jitter, topology numericals (links in full mesh n(n-1)/2, cables/ports needed per topology, failure behaviour).
- FIX: define "bandwidth" both as Hz (analog) and bits/s (digital); never use them interchangeably without saying so.
**diagrams.md** → ADD Mermaid for Internet structure, circuit vs packet switching, delay timeline, all topologies (star/bus/ring/mesh/tree/hybrid) with failure scenarios.
**mcqs.md** → rebuild per Part 4.5 (add MSQ/NAT, delay numericals).
**NEW:** `README.md`, `numericals.md` (delay, BDP, throughput, mesh links, packet vs circuit switching time), `interview_qa.md`, `cheatsheet.md`.

## 02_OSI_Model
**notes.md (536)**
- KEEP: 7 layers, encapsulation/decapsulation, memory tricks, example of loading a web page.
- ADD: for every layer a fixed card: *Job, PDU, Addressing, Protocols, Devices, Example, "what breaks if it fails"*; **header + trailer sizes** shown during encapsulation (e.g. Ethernet 14+4, IPv4 20, TCP 20); services vs protocols vs interfaces; connection-oriented vs connectionless at each layer; OSI vs TCP/IP table; why OSI lost to TCP/IP (history); "layer-by-layer troubleshooting" mini-section pointing to module 16.
- FIX: the word **Gateway** at L7/L5/L6 → explain it is an overloaded term (default gateway = router; protocol gateway = application proxy). **TLS** placement: say clearly it does not map cleanly (often shown at L6, actually between L4 and L7 in TCP/IP). **Firewall** at L3/L4/L7 depends on type.
**diagrams.md** → convert flow diagrams to Mermaid sequence/flowchart; ADD encapsulation animation-style step diagram (data → segment → packet → frame → bits) with real header boxes.
**mcqs.md** → rebuild per Part 4.5.
**NEW:** `README.md`, `interview_qa.md` (OSI classics: "which layer is X", "ping works but browser doesn't"), `cheatsheet.md`.

## 03_TCP_IP_Model
**notes.md (390)**
- KEEP: 4-layer model, mapping, protocol suite, loading-a-website example.
- FIX: remove stray Chinese "快递" in heading; keep "Courier System".
- ADD: the **5-layer hybrid model** (physical, link, network, transport, application) used by most textbooks and GATE; PDU names per layer; protocol-to-layer matrix (ARP, DHCP, DNS, ICMP, IGMP, OSPF, BGP, RIP… and **which layer each really belongs to** with the usual exam answer vs the technically precise answer); end-to-end packet journey with the **actual header fields** at each hop (src/dst MAC changes, IP stays, ports stay), TCP/IP history & RFCs, IPv4 vs IPv6 stack differences.
**diagrams.md** → ADD Mermaid "packet journey across 3 routers showing MAC/IP changes at every hop"; Wireshark-style layered capture screenshot (create an annotated SVG).
**mcqs.md** → rebuild per Part 4.5.
**NEW:** `README.md`, `interview_qa.md`, `cheatsheet.md`.

## 04_Physical_Layer  (NEW)
Full spec in Part 6.1.

## 05_Data_Link_Layer  (NEW)
Full spec in Part 6.2.

## 06_Network_Devices_and_LAN  (move of existing `09_Network_Devices`)
**notes.md (582)**
- KEEP: hub/switch/router comparison, VLAN, inter-VLAN routing, enterprise design, bridge, WAP, firewall, load balancer, complete packet flow.
- ADD: **repeater, NIC, modem, gateway, L3 switch, multilayer switch, IDS/IPS, proxy, WLC**; **collision domain vs broadcast domain** (rules + counting numericals for hubs/switches/routers/VLANs); **switch internals** (MAC learning, flooding, forwarding, filtering, aging, CAM table; store-and-forward vs cut-through vs fragment-free); **STP** (why loops are deadly, broadcast storm, root-bridge election with bridge ID, root/designated/blocked ports, port states, timers, BPDU; worked election example; RSTP overview); **VLAN depth** (access vs trunk, 802.1Q tag fields, native VLAN, VTP overview, router-on-a-stick, L3 switch SVI); **EtherChannel/LACP**; **port security**; **HSRP/VRRP**; **DMZ**; star/hierarchical 3-tier design (access/distribution/core) and spine-leaf.
- FIX: "Gateway = L7" (see 02). Say clearly which device works at which layer *depending on type*.
**diagrams.md** → **MISSING, CREATE** (Mermaid: MAC learning sequence; STP election; VLAN trunk; 3-tier and spine-leaf; collision/broadcast domain colour-coded diagram).
**mcqs.md** → rebuild; fix the heavy B-bias (B=24/30).
**NEW:** `README.md`, `numericals.md` (domain counting, STP root election, VLAN counts), `interview_qa.md`, `cheatsheet.md`.

## 07_IP_Addressing  (existing `04_IP_Addressing`)
**notes.md (394)**
- KEEP: structure, classes, private/public, loopback, APIPA, subnet mask basics, IPv6 basics, mnemonics.
- ADD: first-octet **binary patterns** for classes (0, 10, 110, 1110, 1111); netid/hostid bits, **number of networks and hosts per class** (with the "reserved 0 and 127" nuance), default masks; **all special addresses table** (0.0.0.0, 255.255.255.255 limited broadcast, directed broadcast, 127/8, 169.254/16, 100.64/10 CGNAT, 192.0.2/24 TEST-NET, multicast 224/4 & well-known 224.0.0.x); unicast/broadcast/multicast/anycast; static vs dynamic; public/private + NAT forward link to module 09; IPv4 exhaustion & the RIR (IANA/RIRs); **IPv6**: 128-bit, notation compression rules (with 10 practice conversions), address types (global unicast, link-local fe80::/10, ULA fc00::/7, multicast ff00::/8, anycast, loopback ::1), **EUI-64**, SLAAC, no broadcast in IPv6, IPv6 header (move deep dive to module 09 but give the 1-page intro here).
- FIX: ensure Class A range "1-126" is footnoted ("0 and 127 reserved").
**diagrams.md** → Mermaid for class bit boundaries, address-type decision tree, IPv6 compression steps, EUI-64 construction.
**mcqs.md** → rebuild (class identification, hosts-per-class, special addresses, IPv6 compression NATs).
**NEW:** `README.md`, `numericals.md`, `interview_qa.md`, `cheatsheet.md`.

## 08_Subnetting_CIDR_VLSM  (existing `05_Subnetting`)
**notes.md (586)**
- KEEP: SUBNET method, 256-trick, borrowing bits, VLSM example, scenarios, power-of-2 table.
- ADD: classful vs classless; **CIDR** & route aggregation/**supernetting** (rules for summarisation: contiguous, power-of-2 sized, aligned), **wildcard masks** (ACL/OSPF), same-subnet test, "which subnet does this IP belong to", first/last/usable/broadcast shortcuts, `/31` (RFC 3021) and `/32` special cases, **subnet-zero and all-ones subnet** (old vs modern rule; say which GATE uses), VLSM allocation order and **wasted-address analysis**, **longest-prefix-match** intro (link to routing), subnetting with IPv6 (/64 rule).
- FIX: the "practice problems" count: only 3 exist → **write 45** (15 per level), all verified by a Python script using the `ipaddress` module; include GATE-style: "number of subnets/hosts", "minimum mask for N hosts", "router has these routes, which interface?", "aggregate these 4 blocks".
**diagrams.md** → Mermaid/SVG: bit-borrowing visual, address-space "pie" splitting, VLSM allocation blocks, supernet merge tree.
**mcqs.md** → rebuild with 10 NAT (computations).
**NEW:** `README.md`, `numericals.md`, `interview_qa.md`, `cheatsheet.md` (the **fast subnetting card**).

## 09_Network_Layer_Protocols  (NEW)
Full spec in Part 6.3.

## 10_Routing  (existing `06_Routing`)
**notes.md (714)**
- KEEP: router/routing-table basics, static vs dynamic, protocol classification, scenarios, AD table, mnemonics.
- ADD: forwarding vs routing (data plane vs control plane); **longest prefix match** worked examples; **Distance Vector** with a full **Bellman-Ford iteration table** on a 5-node graph, **count-to-infinity**, split horizon, poison reverse, triggered updates, **RIP** (hop count, 15 max, 30 s updates, timers, RIPv1/v2); **Link State** with **Dijkstra step table** on a 6-node graph, LSA flooding, LSDB, SPF; **OSPF** (areas, area 0, ABR/ASBR, router types, DR/BDR election, hello/dead timers, cost = reference bandwidth / interface bandwidth, LSA types overview, neighbour states); **EIGRP** overview (DUAL, feasible successor, composite metric); **BGP** (AS, ASN, eBGP vs iBGP, path vector, key attributes AS-PATH/LOCAL_PREF/MED/NEXT_HOP, best-path steps in order, why BGP is the "glue of the Internet", BGP hijack/leak example); intra-AS vs inter-AS; hierarchical routing; default route, floating static route, route redistribution (brief); multicast routing (IGMP, PIM overview) and broadcast routing (flooding, RPF); routing loops & TTL; hot-potato vs cold-potato; Router architecture (input port, switching fabric, output port, queuing, HOL blocking).
- FIX: AD table is fine; add full AD list incl. Connected 0, EIGRP-external 170, iBGP 200.
**diagrams.md** → Mermaid for DV tables evolving, Dijkstra tree building, OSPF areas, BGP AS graph, packet forwarding with LPM decision, count-to-infinity timeline.
**mcqs.md** → rebuild; add 10 NAT (shortest-path cost, number of iterations, hop counts).
**NEW:** `README.md`, `numericals.md` (Dijkstra, DV, LPM, OSPF cost, aggregation), `interview_qa.md`, `cheatsheet.md`.

## 11_Transport_Layer  (existing `07_Transport_Layer`)
**notes.md (631)**
- KEEP: ports, sockets, mux/demux, 3-way/4-way handshake, TCP segment, flow control basics, UDP, TCP vs UDP, port table, scenarios.
- FIX **TCP congestion control** (current text is imprecise): write properly:
  - `cwnd`, `ssthresh`, `rwnd`, **effective window = min(cwnd, rwnd)**.
  - **Slow start** (cwnd doubles per RTT) → **congestion avoidance** (+1 MSS per RTT).
  - **Timeout**: `ssthresh = cwnd/2`, `cwnd = 1 MSS` (all variants).
  - **3 duplicate ACKs**: *Tahoe* → same as timeout; *Reno* → fast retransmit + fast recovery (`ssthresh = cwnd/2`, `cwnd = ssthresh + 3`, then linear); NewReno/SACK mention; CUBIC and BBR overview.
  - Include a **cwnd-vs-RTT round table** and graph for Tahoe vs Reno from the same loss events.
- ADD: **TCP state machine** (all 11 states incl. TIME_WAIT, 2MSL, CLOSE_WAIT, half-close); **TCP header every field** (flags: SYN ACK FIN RST PSH URG, header length 20-60 B, window scaling, options: MSS, SACK, timestamps); sequence/ack number numericals (ISN, ack = next expected byte); **retransmission timer** (EstimatedRTT, DevRTT, RTO formulas), **Karn's algorithm**, **delayed ACK**, **Nagle's algorithm**, **silly window syndrome**, zero-window probe/persist timer, **sequence-number wrap-around**; connection setup attacks (SYN flood, SYN cookies); half-open; TCP keep-alive; **UDP**: header (8 B), checksum with pseudo-header worked example, use cases (DNS, DHCP, VoIP, gaming, QUIC); **QUIC** & why HTTP/3 uses it; SCTP/DCCP brief; **throughput formulas** (window/RTT, max throughput of TCP link, link utilisation); **connection-oriented vs connectionless** definition cleanly; NAT & ports (PAT) link; port scanning at concept level.
- Link to 05_Data_Link_Layer for sliding-window protocols (GBN/SR) so they are not duplicated: here say how TCP differs (byte-oriented, cumulative ACK, SACK).
**diagrams.md** → Mermaid sequence for handshake/teardown with real seq/ack numbers; state diagram; cwnd graphs; Nagle/delayed-ACK timeline; sliding window picture.
**mcqs.md** → rebuild; add NAT: throughput, cwnd after N RTTs, RTO.
**NEW:** `README.md`, `numericals.md`, `interview_qa.md` ("TCP vs UDP", "why 3-way not 2-way", "what is TIME_WAIT", "what if ACK is lost"), `cheatsheet.md`.

## 12_Application_Layer  (existing `08_Application_Layer`)
**notes.md (747)**
- KEEP: DNS, HTTP/HTTPS, SMTP/POP3/IMAP, DHCP, scenarios (URL load, email not received, slow site).
- ADD: **client-server vs P2P architectures**; **socket programming** (Python TCP and UDP client/server, 20-30 lines each, runnable); **HTTP deep dive** (versions 1.0/1.1/2/3, persistent connections, pipelining, head-of-line blocking, multiplexing, methods & idempotency, **all status-code classes with the 15 most-asked codes**, headers, cookies, sessions, caching (Cache-Control, ETag, conditional GET), CORS in 5 lines, REST basics, WebSocket, long-polling vs SSE); **DNS deep dive** (hierarchy: root/TLD/authoritative, iterative vs recursive, caching & TTL, all record types A AAAA CNAME MX NS TXT PTR SOA SRV, DNS over UDP/TCP 53, DNSSEC, DoH/DoT, DNS load balancing, DNS poisoning at concept level, worked resolution with the number of queries); **DHCP DORA + relay agent + lease renewal (T1/T2) + ports 67/68**; **FTP** (control 21 & data 20, active vs passive), **TFTP**, **Telnet vs SSH (22)**, **SNMP** (manager/agent/MIB, v1/v2c/v3, traps), **NTP**, **SMTP commands + MIME**, **POP3 vs IMAP table**, **proxy/reverse proxy/forward proxy**, **CDN** (how it works, anycast + DNS), **VoIP/SIP/RTP/RTCP**, **video streaming (DASH/HLS)**, **BitTorrent** overview, **LDAP/SMB/NFS** (one paragraph each), **TLS handshake** (TLS 1.2 vs 1.3 with a sequence diagram; link to module 13).
- FIX: make sure DNS is described as using **UDP and TCP**; HTTP/3 = **QUIC over UDP**; HTTPS = HTTP over TLS (not "HTTP over SSL").
**diagrams.md** → keep DNS/HTTP/TLS/Email/DHCP diagrams, convert to Mermaid sequence diagrams; ADD FTP active/passive, HTTP/1.1 vs /2 vs /3 timeline comparison, CDN request flow, proxy vs reverse proxy.
**mcqs.md** → rebuild; add scenario questions with `curl -v`, `dig`, `nslookup` output.
**NEW:** `README.md`, `numericals.md` (HTTP response-time with RTTs: non-persistent vs persistent vs pipelined; DNS query time; email size/encoding), `interview_qa.md` (incl. **"What happens when you type a URL"** full 10-12 step answer, which is also linked from 17_Interview_Prep), `cheatsheet.md` (ports + status codes + DNS records).

## 13_Network_Security through 20_Cheatsheets
Create per Part 6.

---

# PART 6: NEW MODULES: COMPLETE TOPIC CHECKLISTS

Each bullet below must appear in the module's `notes.md` (with a diagram where visual) and be tested in `mcqs.md`.

## 6.1 04_Physical_Layer
- Data vs signal, analog vs digital, periodic signals, amplitude/frequency/phase, wavelength, bandwidth (Hz), spectrum
- **Transmission impairments**: attenuation, distortion, noise; dB, SNR, SNR in dB
- **Data rate limits**: **Nyquist** (2·B·log2 L) and **Shannon** (B·log2(1+SNR)): with 10 numericals each and "which one to apply" rule
- Digital transmission: **line coding** (NRZ-L, NRZ-I, RZ, Manchester, Differential Manchester, AMI, B8ZS, HDB3, 4B/5B), baud rate vs bit rate, clock recovery, synchronisation
- Analog modulation: ASK, FSK, PSK, QAM, constellation diagrams; bits per symbol
- **Multiplexing**: FDM, TDM (synchronous, statistical), WDM/DWDM, CDMA (with the walsh-code worked example)
- **Switching** (cross-link from 01) and **transmission media**: twisted pair (UTP/STP, Cat5e/6/6a, straight vs crossover, T568A/B), coaxial, **fibre** (single vs multi-mode, total internal reflection), wireless media (radio, microwave, infrared, satellite: LEO/MEO/GEO), propagation modes
- Connectors (RJ45, SFP, LC/SC), cable length limits, speeds (Ethernet standards table 10BASE-T → 100G)
- Digital subscriber and access tech: dial-up, DSL, cable, FTTH, Metro-E; modem vs router
- Numericals: SNR/dB, Nyquist/Shannon capacities, channel capacity needed, TDM frame size/slot count, CDMA decode, line-code waveforms (draw as SVG)

## 6.2 05_Data_Link_Layer  (highest GATE value: be exhaustive)
- Role: node-to-node delivery, sublayers LLC/MAC, services (framing, addressing, error/flow control, access control)
- **Framing**: character count, flag bytes with **byte stuffing**, flags with **bit stuffing** (worked examples), physical-layer coding violations
- **Error detection & correction**: error types (single-bit/burst), **parity (1-D, 2-D)**, **checksum** (Internet checksum worked example), **CRC** (polynomial division worked, generator polynomials, which errors detected), **Hamming code** (r bits, positions, error location worked), Hamming distance (detect d errors needs distance d+1; correct needs 2d+1), FEC vs ARQ
- **Flow control & ARQ**: **Stop-and-Wait**, **Go-Back-N**, **Selective Repeat**: diagrams, window sizes, sequence-number bits (SW 1 bit; GBN 2^k−1 window; SR 2^(k−1) window), **efficiency/utilisation formulas** (η = 1/(1+2a) for SW; N/(1+2a) for sliding window, a = Tp/Tt), throughput, retransmission counts, **piggybacking**, **optimal window size**, delay-bandwidth product
- **Medium access control**: Random access (**Pure/Slotted ALOHA** with 18.4% & 36.8% max efficiency, **CSMA** 1-persistent/non-persistent/p-persistent, **CSMA/CD** with **min frame size = 2·Tp·B**, binary exponential backoff, jam signal, **CSMA/CA** with ACK/RTS-CTS), Controlled access (polling, token passing, **token ring**, reservation), Channelisation (FDMA/TDMA/CDMA)
- **Ethernet (IEEE 802.3)**: frame format field-by-field (preamble 7, SFD 1, dst 6, src 6, type/length 2, payload 46-1500, FCS 4; min 64 B / max 1518 B, MTU 1500), **MAC address** (48 bits, OUI, unicast/multicast/broadcast ff:ff:ff:ff:ff:ff), Ethernet evolution (10/100/1000/10G), full vs half duplex, auto-negotiation, jumbo frames, 802.1Q VLAN tag, 802.1ad Q-in-Q, **PPP**, HDLC, Frame Relay/ATM (brief, history)
- **ARP's place** (full detail in module 09), **switching at L2** (cross-link to 06)
- Numericals: min frame length for CSMA/CD at given length/speed, efficiency of SW/GBN/SR, CRC remainder, Hamming codeword, bit-stuffed output, ALOHA throughput, window size for 100% utilisation, number of retransmissions on error

## 6.3 09_Network_Layer_Protocols
- Network layer services; **datagram vs virtual circuit** networks; forwarding vs routing; store-and-forward; where the network layer fits (links to 10)
- **IPv4 header, every field**: version, IHL, DSCP/ECN, total length, identification, flags (DF, MF), fragment offset (in 8-byte units), TTL, protocol numbers (1 ICMP, 6 TCP, 17 UDP, 89 OSPF), header checksum (worked), options; header min 20 / max 60 B
- **Fragmentation & reassembly**: MTU, DF flag, offset calculation, worked multi-hop examples, path MTU discovery, why fragmentation is avoided; numericals ×10
- **ARP** (request broadcast / reply unicast, ARP cache, gratuitous ARP, Proxy ARP, **RARP**, ARP spoofing link), **ICMP** (types/codes: echo, dest-unreachable codes, time-exceeded, redirect; how **ping** and **traceroute** work using TTL), **IGMP** & multicast (class D, multicast MAC mapping, group membership)
- **DHCP** at network-layer view (link to 12) and **APIPA**
- **NAT / PAT**: static, dynamic, PAT (port translation table worked), NAT types, why NAT broke end-to-end, NAT traversal (STUN/TURN/hole punching brief), CGNAT, **NAT is not a firewall**
- **IPv6 deep dive**: header (fixed 40 B, fields: version, traffic class, flow label, payload length, next header, hop limit), extension headers, **no fragmentation by routers**, ICMPv6 & **NDP** (NS/NA/RS/RA, replaces ARP), SLAAC vs DHCPv6, **transition mechanisms** (dual stack, tunnelling 6in4, 6to4, Teredo, NAT64/DNS64) with diagrams, IPv4 vs IPv6 table (≥12 rows)
- Mobile IP (brief), IP security link to 13, **QoS fields** link to 15
- Numericals: fragmentation, header-length/total-length, checksum, NAT table entries, ICMP traceroute hop counts

## 6.4 13_Network_Security
- CIA triad, threats vs vulnerabilities vs attacks, attacker types, security goals (authentication, authorisation, integrity, non-repudiation)
- **Attacks (concept + defence, never exploit code)**: sniffing, spoofing (IP/ARP/DNS/MAC), MITM, replay, DoS/DDoS (SYN flood, UDP/ICMP flood, amplification), phishing, port scanning, session hijacking, VLAN hopping, rogue DHCP, brute force, ransomware path, SQL-injection/XSS at network-appsec intro level
- **Cryptography**: symmetric (DES/3DES/**AES**, block vs stream, modes ECB/CBC/GCM), asymmetric (**RSA** worked small example, **Diffie-Hellman** worked numeric example, ECC overview), hash (MD5/SHA-1/SHA-2/SHA-3, collisions), **MAC/HMAC**, **digital signatures**, **PKI, X.509 certificates, CA chain of trust**, key exchange, perfect forward secrecy, password hashing/salting
- **Protocols**: **TLS/SSL handshake** (1.2 vs 1.3, certificates, cipher suites), **HTTPS**, **SSH**, **IPsec** (AH vs ESP, transport vs tunnel mode, IKE/SA), **VPN** (site-to-site, remote access, SSL VPN, WireGuard/OpenVPN overview, split tunnelling), **Kerberos**, **802.1X/RADIUS/TACACS+**, **PGP/S-MIME**, **DNSSEC**, **SPF/DKIM/DMARC**
- **Defences**: firewalls (packet filter, stateful, application/proxy, NGFW, WAF), **ACLs** (standard/extended; worked rules; wildcard masks), IDS vs IPS (signature/anomaly), DMZ, honeypots, network segmentation/zero-trust, port security, DHCP snooping, dynamic ARP inspection, rate limiting, patching, logging/SIEM
- Numericals: RSA/DH small-number, key counts (n(n−1)/2 symmetric keys), brute-force time
- ⚠ Keep it defensive/educational; no working attack tooling.

## 6.5 14_Wireless_and_Mobile
- Wireless basics: spectrum, 2.4/5/6 GHz, channels & overlap (1/6/11), interference, attenuation, hidden & exposed terminal problem
- **Wi-Fi 802.11**: a/b/g/n/ac/ax(Wi-Fi 6/6E)/be(7) table (band, max rate, MIMO, OFDMA), BSS/ESS/IBSS/SSID/BSSID, AP modes, **association process** (probe, auth, assoc), **CSMA/CA + RTS/CTS + NAV**, frame types (mgmt/control/data), roaming, mesh, controller-based
- **Wi-Fi security**: WEP (broken, why), WPA, WPA2 (AES-CCMP, 4-way handshake), **WPA3 (SAE)**, WPS risks, enterprise (802.1X), rogue AP/evil twin
- Bluetooth/BLE, Zigbee, NFC, RFID, LoRa (comparison table: range/rate/power)
- **Cellular**: cell concept, frequency reuse, handoff, **1G→5G** table, 4G LTE architecture (UE, eNodeB, EPC), **5G** (eMBB/URLLC/mMTC, slicing, mmWave), GSM/CDMA basics, satellite (LEO/Starlink)
- Mobile IP, WLAN planning basics (site survey, coverage, capacity)
- Numericals: path loss/dB, frequency reuse pattern (cluster size N, capacity), channel capacity with Shannon for Wi-Fi

## 6.6 15_Modern_Networking
- **QoS**: traffic classes, DSCP, queuing (FIFO/priority/WFQ), **traffic shaping vs policing**, **leaky bucket & token bucket** (with numericals), IntServ/DiffServ, jitter/latency requirements for VoIP/video
- **MPLS** (labels, LSR/LER, LSP, VPN use), **SD-WAN**, **SDN** (control/data plane separation, OpenFlow, controller), **NFV**
- **Load balancing** (L4 vs L7, algorithms round-robin/least-conn/IP-hash, health checks, sticky sessions, HAProxy/Nginx/AWS ELB), **reverse proxy**, **API gateway**, **CDN** (deeper), **anycast**, **BGP in the cloud**
- **Cloud networking**: VPC/VNet, subnets (public/private), route tables, **Internet gateway, NAT gateway**, security groups vs NACLs, peering, transit gateway, VPN/Direct Connect, DNS (Route 53-style), load balancers; **Docker/Kubernetes networking** (bridge, overlay, CNI, services, ingress)
- **Data centre networks**: 3-tier vs **spine-leaf**, east-west traffic, VXLAN
- **IoT networking**: MQTT, CoAP, 6LoWPAN, edge computing; **Network programmability** (REST APIs, NETCONF/YANG, Ansible/Python/Netmiko basics); **Observability** (SNMP, NetFlow, syslog, packet capture, Prometheus)
- **Emerging**: HTTP/3-QUIC, IPv6 adoption, Wi-Fi 7, 5G/6G, zero trust, SASE

## 6.7 16_Troubleshooting_and_Tools
- **Troubleshooting methodologies**: OSI top-down / bottom-up / divide-and-conquer, "Is it DNS?" decision tree, a **master flowchart** (Mermaid)
- **Commands with real annotated outputs (Windows + Linux + macOS)**: `ping`, `tracert/traceroute/mtr`, `ipconfig/ifconfig/ip a/ip r`, `arp -a`, `nslookup/dig` (read every field), `netstat/ss`, `curl -v`, `telnet/nc` port tests, `nmap` (ethical usage, basics), `tcpdump`, `route`, `hostname`, `whois`, `pathping`, `iperf` for throughput, `openssl s_client`
- **Wireshark**: capture/display filters (20 most useful), following a TCP stream, reading handshake, DNS, HTTP, TLS; 5 sample `.pcap` exercises (describe what to find; provide a script that generates simple pcaps with `scapy` *or* link to free public pcap sources)
- **Cisco/CLI basics**: user/privileged/config modes, `show ip route`, `show ip interface brief`, `show vlan brief`, `show running-config`, basic interface/VLAN/static-route/OSPF/DHCP/NAT config, `write memory`
- **50 troubleshooting scenarios** in a table: Symptom → Likely layer → What to check → Command → Fix (e.g., "can ping IP not name", "intermittent slow", "169.254 address", "duplicate IP", "DHCP not working", "VLAN can't reach gateway", "MTU/black-hole", "asymmetric routing", "TLS cert error", "port blocked by firewall")
- `numericals.md` not needed; `mcqs.md` must have 15 output-reading questions

## 6.8 17_Interview_Prep
Structure:
~~~text
README.md                 ← how to use, 14-day interview plan
top_100_questions.md      ← grouped by topic, tiered Basic/Medium/Hard, with model answers
scenario_questions.md     ← 40 scenario/troubleshooting/design questions with step-by-step answers
what_happens_when_url.md  ← the ULTIMATE answer: 12+ steps, one Mermaid diagram, 30-s/2-min/10-min versions
tricky_questions.md       ← 30 trick questions & the classic wrong answers
company_wise_themes.md    ← typical themes: service companies (aptitude+basic CN), product companies (TCP, DNS, LB, system-design), networking/cloud roles (routing, OSPF/BGP, VLAN, troubleshooting). State clearly these are *themes*, not guarantees
hr_and_resume_tips.md     ← how to present networking projects/labs on a resume
mock_interviews.md        ← 10 mock Q-sets (20 questions each) with scoring rubric
difference_between.md     ← 60 "X vs Y" comparison tables (TCP/UDP, Hub/Switch/Router, IPv4/IPv6, HTTP/HTTPS, HTTP1/2/3, SMTP/IMAP/POP3, ARP/RARP, TCP/IP vs OSI, Switch vs L3 switch, NAT vs PAT, Static vs Dynamic routing, DV vs LS, OSPF vs BGP, Symmetric vs Asymmetric, Firewall vs IDS vs IPS, VPN vs Proxy, Unicast/Broadcast/Multicast/Anycast, Forward vs Reverse proxy, Cookies vs Sessions, Stateful vs Stateless, Public vs Private IP, MAC vs IP, Bit rate vs Baud, Bandwidth vs Throughput vs Latency, Collision vs Broadcast domain, Router vs Gateway ...)
rapid_fire_500.md         ← 500 one-line Q&A for last-day revision
~~~
Answer format for every question: **Short answer → Explanation → Example → Follow-up**.

## 6.9 18_GATE_and_Competitive_Zone
~~~text
README.md                   ← GATE CN syllabus mapped to repo files, weightage (approx., labelled as such), strategy, how many marks, time per question
syllabus_map.md             ← table: GATE topic → repo module/file → status
formula_sheet.md            ← ALL formulas on 2 pages (delay, BDP, Nyquist, Shannon, SW/GBN/SR efficiency, CSMA/CD frame size, ALOHA, subnets/hosts, fragmentation, TCP throughput, cwnd, RTO, CRC/Hamming, token bucket)
pyq_by_topic.md             ← GATE previous-year questions grouped by topic with year, solution and the concept tag.
                              RULE: do NOT invent questions or years. Write only questions you can reproduce accurately;
                              otherwise write "GATE-style" original problems of the same pattern and label them as such.
gate_style_practice/        ← 12 topic-wise tests of 20 questions each (MCQ+MSQ+NAT) + 4 full-length mock tests of 30 questions (1 & 2 marks), with solutions
ugc_net_isro_psu.md         ← typical CN topics in UGC NET, ISRO, DRDO, PSU papers: pattern + 100 practice Qs
ccna_network_plus_map.md    ← map of CCNA 200-301 and CompTIA Network+ objectives to repo files (+ gaps to study elsewhere)
quick_revision_7_days.md    ← GATE last-week plan
common_mistakes_in_gate.md  ← 30 classic traps (units: ms vs s, bytes vs bits, 2^n−2, ceiling vs floor, header included or not)
~~~

## 6.10 19_Hands_On_Labs
- `README.md` (setup: Packet Tracer, GNS3/EVE-NG, Wireshark, VirtualBox, Python)
- **Packet Tracer labs (≥15)** each with: objective, topology (Mermaid), IP plan table, step-by-step commands, verification, "what you learned", challenge task, solution. Include `.pkt` files **only if you can generate them; otherwise provide complete CLI configs** (no fake binaries). Labs: first LAN, switch basics, VLANs + trunk, inter-VLAN routing (router-on-a-stick and L3 switch), static routing, default routing, RIP, OSPF single-area, OSPF multi-area, DHCP server/relay, NAT/PAT, ACLs, STP, EtherChannel, HSRP, port security, IPv6 basics, DNS/HTTP server, site-to-site VPN overview
- **Wireshark labs (≥8)**: ARP, ICMP/ping/traceroute, DNS, TCP 3-way handshake & teardown, HTTP vs HTTPS, DHCP DORA, TLS handshake, UDP vs TCP
- **Python/Code labs** (runnable, commented, tested): TCP echo server/client, UDP chat, multi-client threaded server, simple HTTP server, port scanner (only against localhost/own lab; add ethical note), subnet calculator using `ipaddress`, ping with `socket`/`scapy` (lab-only), packet sniffer with `scapy` (lab-only), simple DNS lookup, **CRC/Hamming/bit-stuffing simulators**, **Dijkstra/Bellman-Ford simulators**, **sliding window protocol simulator**
- `projects.md`: 10 resume-worthy projects (chat app, mini-Wireshark, subnet calculator web app, network monitor dashboard, load balancer in Python/Node, DNS resolver, file transfer over TCP, VPN toy example (educational), IoT MQTT dashboard) with feature lists and difficulty

## 6.11 20_Cheatsheets
~~~text
protocols_and_ports.md       ← 100 protocols: layer, port, transport, purpose, one-line "remember"
osi_tcpip_quick.md           ← model mapping, PDUs, devices, protocols
subnetting_cheatsheet.md     ← CIDR table /0-/32, mask, wildcard, hosts, block size, class defaults, fast method
commands_cheatsheet.md       ← Windows/Linux/macOS/Cisco side by side
formulas.md                  ← copy of 18/formula_sheet.md
headers_cheatsheet.md        ← Ethernet, IPv4, IPv6, TCP, UDP, ICMP, ARP header layouts (as SVG/Mermaid packet diagrams)
http_status_and_methods.md   ← status codes, methods, headers
differences_one_page.md      ← top 25 differences
security_cheatsheet.md       ← attacks → defences, crypto algorithm table, TLS/IPsec summary
last_day_revision.md         ← 2-hour speed revision: the 100 things you must remember
~~~

## 6.12 Root-level support files
- `GLOSSARY.md`: **≥ 400 terms**, alphabetical, each: term → definition (≤ 2 lines) → layer/module link. Include abbreviations expansion.
- `INDEX.md`: every file in the repo linked in order.
- `STUDY_PLANS.md`: 7-day crash, 14-day interview, 30-day, 60-day, 90-day GATE; each day lists exact files and time; include a checkbox table.
- `START_HERE.md`: "I'm a ... (beginner / college student / GATE aspirant / interview in a week / CCNA)" → exact path with links.
- `PROGRESS.md`, `CONTRIBUTING.md` (how to add a topic using the templates), `LICENSE` (suggest MIT or CC BY-SA 4.0 and ask the owner), `.github/ISSUE_TEMPLATE/*`, link-check workflow.

---

# PART 7: VISUAL STANDARDS

1. **Mermaid first.** GitHub renders it. Preferred types:
   - Handshakes/protocol exchanges → `sequenceDiagram`
   - Decisions/troubleshooting → `flowchart TD`
   - State machines (TCP, STP port states, DHCP client) → `stateDiagram-v2`
   - Topologies/hierarchies → `graph LR` / `flowchart`
   - Timelines → `timeline`, comparisons → tables
2. **SVG assets** in `assets/images/<topic>/` for: packet/frame header layouts (bit-accurate widths), Wireshark-style annotated captures, device icons, signal waveforms (line coding), constellation diagrams, cwnd graphs, Dijkstra step pictures. Generate with Python (matplotlib → SVG) or hand-written SVG. Use descriptive file names (`tcp-header.svg`) and **alt text**.
3. **Never hotlink random web images** (licences, link-rot). Use only self-made or clearly public-domain/CC0 images, and record the source in `assets/ATTRIBUTION.md`.
4. **Colour language** (document it in `START_HERE.md`): 🟦 sender/client, 🟩 receiver/server, 🟥 error/attack, 🟨 important field, ⬜ neutral.
5. **Every diagram** must be understandable without the text: labelled arrows, numbered steps.
6. Test every Mermaid block renders (no syntax errors). Keep nodes ≤ 15 per diagram; split large ones.
7. **Tables everywhere** for comparisons, header fields (name, bits, purpose), port lists, command → meaning.

---

# PART 8: ACCURACY & QUALITY GATES

## 8.1 Fact traps: get these exactly right
- IPv4 Class A first octet 1-126 (0 and 127 reserved); usable hosts = 2^h − 2 (except /31, /32 special); Class B 128-191, C 192-223, D 224-239, E 240-255.
- Private ranges: 10/8, 172.16/12 (172.16-172.31), 192.168/16. APIPA 169.254/16. CGNAT 100.64/10.
- Header sizes: Ethernet header 14 B + FCS 4 B (frame 64-1518 B; payload 46-1500); IPv4 20-60 B; IPv6 40 B; TCP 20-60 B; UDP 8 B; ICMP 8 B (header).
- Ports: HTTP 80, HTTPS 443, FTP 20/21, SSH 22, Telnet 23, SMTP 25 (587 submission, 465 SMTPS), DNS 53 (UDP & TCP), DHCP 67/68, TFTP 69, POP3 110 (995), IMAP 143 (993), NTP 123, SNMP 161/162, LDAP 389, SMB 445, RDP 3389, BGP 179 (TCP), RIP 520 (UDP).
- Protocol numbers: ICMP 1, IGMP 2, TCP 6, UDP 17, GRE 47, ESP 50, AH 51, OSPF 89.
- **TCP**: 3-way handshake SYN → SYN-ACK → ACK; ACK number = next byte expected; SYN and FIN consume 1 sequence number; TIME_WAIT = 2·MSL; Tahoe vs Reno behaviours as in Part 5; TCP is byte-oriented, UDP message-oriented.
- **Sliding window**: GBN receiver window 1, sender N ≤ 2^k − 1; SR both windows N ≤ 2^(k−1); utilisation formulas use a = Tp/Tt; units (bits vs bytes, ms vs s) are always shown.
- **CSMA/CD**: Tt ≥ 2·Tp; min frame = 2·Tp·B; Ethernet 10 Mbps min 64 B (512 bits).
- **ALOHA**: Pure 18.4% (1/2e), Slotted 36.8% (1/e).
- **Nyquist** noiseless: C = 2B·log2(L); **Shannon** noisy: C = B·log2(1 + SNR) (SNR as ratio, not dB).
- **Hub** = 1 collision domain, 1 broadcast domain; **Switch** = a collision domain per port, 1 broadcast domain (per VLAN); **Router** = separates broadcast domains.
- OSPF cost = reference bandwidth / interface bandwidth (default ref 100 Mbps in Cisco IOS; mention it must be tuned); AD: Connected 0, Static 1, eBGP 20, EIGRP 90, OSPF 110, RIP 120, iBGP 200.
- DNS uses UDP & TCP; HTTP/3 uses QUIC (UDP); HTTPS = HTTP over TLS; TLS 1.3 handshake = 1-RTT; NAT is **not** a security feature; WEP broken; MD5/SHA-1 broken for collisions.
- ARP: request is broadcast, reply is unicast; MAC changes every hop, IP (src/dst) doesn't (except NAT).
- Don't say "router operates only at Layer 3" without noting L1/L2 on its interfaces; don't say "switch never looks at IP" without mentioning L3 switches.
- When the textbook answer differs from the technically precise answer, **give both** and label: "Exam answer" / "Real world".

## 8.2 Verification procedure (mandatory)
1. Every numerical in `numericals.md`, `mcqs.md` and `notes.md` is **computed by a Python script** stored in `tools/verify/` (e.g., `verify_subnetting.py`, `verify_datalink.py`, `verify_transport.py`) using `ipaddress`, `math`, etc. The script prints expected answers; compare with the written ones.
2. Run a Markdown link checker; zero broken internal links.
3. Validate every Mermaid block (e.g., with `@mermaid-js/mermaid-cli` or a CI step).
4. Spell-check and make sure headings are consistent.
5. Search the whole repo for: `TODO`, `TBD`, `coming soon`, `similar to above`, `etc.` used to dodge explanation, non-English stray characters, and fix.
6. Re-balance and verify answer-key distribution per MCQ file.
7. Ensure each question has exactly one explanation, and the explanation **proves** the answer (not just restates it).

## 8.3 Per-file quality checklist (the agent ticks this in `PROGRESS.md`)
- [ ] Beginner can follow without outside help
- [ ] Every term defined at first use, and added to glossary
- [ ] Every flow/structure has a diagram; every comparison has a table
- [ ] Numerical examples exist and are verified
- [ ] Exam tip + interview tip + common trap present
- [ ] Prev/next/related links work
- [ ] Summary + revision checklist at the end
- [ ] No placeholder or unfinished text

---

# PART 9: EXECUTION PLAN (run one phase at a time)

After **every** phase: update `PROGRESS.md`, run Part 8 checks for the files touched, commit (`git commit -m "phase X: ..."`), then print a short report (files created/changed, issues found, what's next).

**Phase 0: Audit & scaffold (no content writing yet)**
- Read every existing file; confirm Part 2 findings; list anything else wrong.
- Create the target folder tree (Part 3) with `git mv` for existing folders (04→07, 05→08, 06→10, 07→11, 08→12, 09→06) and fix all links.
- Create `PROGRESS.md`, `START_HERE.md` skeleton, `GLOSSARY.md` skeleton, templates in `.github/` and `CONTRIBUTING.md`.
- Rewrite root `README.md`; delete `CONTENT_STATUS.md` and the old inner README (after moving its content).

**Phase 1: Repair existing modules (01, 02, 03)**
Apply Part 5 to 01-03, add their README/numericals/interview_qa/cheatsheet, convert diagrams to Mermaid, rebuild MCQs.

**Phase 2: Physical + Data Link (04, 05)**: write fully (Part 6.1, 6.2). Build `tools/verify` scripts. This is the largest GATE area. Split into sub-steps (04; 05a framing+error control; 05b flow control/ARQ; 05c MAC+Ethernet).

**Phase 3: Devices/LAN + IP + Subnetting (06, 07, 08)**: Part 5 + extra content; write 45 subnetting problems.

**Phase 4: Network layer protocols + Routing (09, 10)**.

**Phase 5: Transport (11)** including precise congestion control, state machine, RTO, numericals.

**Phase 6: Application layer (12)** including "type a URL" answer and socket programming code (test it runs).

**Phase 7: Security + Wireless (13, 14)**.

**Phase 8: Modern networking + Troubleshooting (15, 16)**.

**Phase 9: Interview + GATE zones (17, 18)**: no fabricated PYQs (Part 6.9 rule).

**Phase 10: Labs + Cheatsheets (19, 20)**: test all code; provide full CLI configs.

**Phase 11: Final integration & polish**
- Complete `GLOSSARY.md` (≥ 400 terms), `INDEX.md`, `STUDY_PLANS.md`, `START_HERE.md`.
- Add "Related topics" links across modules (e.g., ARP ↔ switching ↔ NAT ↔ DHCP).
- Run all gates in Part 8; fix everything; final `PROGRESS.md` shows 100%.
- Produce `RELEASE_NOTES.md` summarising the repo and **list of anything the owner must do manually** (rename GitHub repo, choose licence, enable GitHub Pages / link-check Action, add real screenshots if desired).

---

# PART 10: DEFINITION OF DONE

The repo is complete only when:
1. All 20 folders exist with the required files; no empty or stub files.
2. Every topic in Part 6 checklists is explained, diagrammed, and tested.
3. ≥ 16 topic modules × (50+ questions) ≈ **800+ MCQ/MSQ/NAT** with balanced answer keys, plus 500 rapid-fire, 100 interview Qs, 40 scenarios, 4 GATE-style full mocks.
4. Every numeric answer is script-verified; `tools/verify/` is committed.
5. A newcomer can start at `START_HERE.md`, follow prev/next links through all modules without hitting a dead end or an undefined term.
6. A reader can answer, with a diagram, any of: *"What happens when you type a URL?"*, *"TCP vs UDP"*, *"How does DNS work?"*, *"Subnet this network"*, *"Explain OSPF vs BGP"*, *"How does HTTPS work?"*, *"Design a network for a 3-floor office"*, *"Troubleshoot: can't reach the internet"*, *"Explain Go-Back-N with efficiency"*, *"Why does CSMA/CD need a minimum frame size?"*.
7. All internal links work, all Mermaid renders, no TODOs, no stray non-English characters, consistent style.

---

# PART 11: HOW THE AGENT SHOULD HANDLE UNCERTAINTY

- If a fact is uncertain: write it conservatively, add `> ⚠️ Verify:` note with the RFC/standard name, and list it in `PROGRESS.md → "Needs human review"`.
- If something would require copyrighted material (textbook diagrams, copyrighted PYQ papers, vendor docs): **don't copy**; create original explanations/diagrams and link to the official source.
- If you cannot generate a real binary file (e.g., `.pkt`, screenshots): provide the complete text instructions/configs and note it. Never fake it.
- Prefer clarity over cleverness, and consistency over variety.

**END OF MASTER PROMPT**
