# 🤝 Repository Handoff & Project Memory

### 1. Current Position
- **Current Position:** Ready for Phase 2 — Module 04 (Physical Layer).
- **Branch:** `main` | **Target Coverage:** 20 Modules.

### 2. Done Modules & Commit Hashes
- **Phase 0 (Scaffolding & Architecture Audit):** `c57e5f1`
- **Module 01 (Fundamentals):** `1d4e82c` (Notes, 10 Diagrams, Numericals, 55 MCQs, Interview QA, Cheatsheet)
- **Module 02 (OSI Model):** `a74c409` (Notes, 10 Diagrams, 55 MCQs, Interview QA, Cheatsheet)
- **Module 03 (TCP/IP Model):** `a73c3b3` (Notes, 10 Diagrams, 55 MCQs, Interview QA, Cheatsheet)
- **Pre-Phase 2 Tooling & Setup:** `757c63e` (Templates, lint, links, balance, index, glossary, new_module)

### 3. Conventions & Efficiency Rules (Strict)
- **Chat Scope:** 1 chat = 1 module (or sub-step 05a/05b/05c, 11a/11b, 12a/12b, 13a/13b). At start, read ONLY `HANDOFF.md` + current module's part of `MASTER_PROMPT.md`.
- **Authoring Order:** (a) `verify_<mod>.py` & run -> (b) `notes.md` -> (c) `numericals.md` -> (d) `diagrams.md` -> (e) `mcqs.md` -> (f) `interview_qa.md` -> (g) `cheatsheet.md` -> (h) `README.md`.
- **Content Rules:** Explain concepts ONCE in notes; link back from MCQs/interview. Size targets: notes 500–800 lines, 10–15 diagrams, 55 MCQs (30 MCQ + 10 MSQ + 10 NAT + 5 Scenario), 20–30 interview Qs, 1-page cheatsheet.
- **Tooling:** Run `lint.py`, `check_links.py`, `check_mcq_balance.py`, `update_index.py`, and `glossary_add.py`. Never edit INDEX/PROGRESS manually.
- **Incremental Commits:** Commit after each file group; update HANDOFF.md at end and STOP for user.

### 4. Decisions ("Exam Answer First, Real-World Note Second")
- When textbooks/GATE differ from technical precision, MCQs/cheatsheets use the EXAM answer, with a concise real-world note:
  - **ARP / RARP:** Network Layer (L3) *(in practice sits between L2 and L3)*.
  - **ICMP / IGMP:** Network Layer (L3) *(encapsulated in IP Protocol 1 / 2)*.
  - **OSPF:** Network Layer (L3) *(encapsulated in IP Protocol 89)*.
  - **BGP:** Application Layer (L7) *(runs over TCP 179; functionally path-vector routing)*.
  - **RIP:** Application Layer (L7) *(runs over UDP 520; functionally distance-vector routing)*.
  - **DHCP / DNS:** Application Layer (L7) *(UDP 67/68, UDP/TCP 53)*.
  - **Hardware:** Router = L3 device, Switch = L2 device, Hub = L1 device.

### 5. Facts Needing Human Review
- None blocking. All formulas in 01 verified with Python. Modules 01–03 patched.

### 6. Next 3 Actions
1. Author **04_Physical_Layer** (Signals, Nyquist/Shannon capacities, transmission media, line coding, PCM, numericals, 55 MCQs).
2. Author **05_Data_Link_Layer** (Framing, CRC, Stop-and-Wait/GBN/SR ARQ, CSMA/CD, Ethernet, numericals, 55 MCQs).
3. Validate Phase 2 with automated quality gate tooling (`lint.py`, `check_links.py`, `check_mcq_balance.py`).
