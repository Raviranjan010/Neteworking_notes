# 🤝 Repository Handoff & Project Memory

### 1. Current Position
- **Current Position:** Pre-Phase 2 Setup (Tooling, Templates, Decisions Patch).
- **Target Next Step:** Phase 2 — Module 04 (Physical Layer).
- **Branch:** `main` | **Target Coverage:** 20 Modules.

### 2. Done Modules & Commit Hashes
- **Phase 0 (Scaffolding & Architecture Audit):** `c57e5f1`
- **Module 01 (Fundamentals):** `1d4e82c` (Notes, 10 Diagrams, Solved Numericals, 55 MCQs, Interview QA, Cheatsheet)
- **Module 02 (OSI Model):** `a74c409` (Notes, 10 Diagrams, 55 MCQs, Interview QA, Cheatsheet)
- **Module 03 (TCP/IP Model):** `a73c3b3` (Notes, 10 Diagrams, 55 MCQs, Interview QA, Cheatsheet)

### 3. Conventions
- **7-File Module Structure:** `README.md`, `notes.md`, `diagrams.md`, `numericals.md`, `mcqs.md`, `interview_qa.md`, `cheatsheet.md` (built from `_templates/`).
- **55-Question Practice Set:** 30 MCQ (Part A) + 10 MSQ (Part B) + 10 NAT (Part C) + 5 Scenario (Part D).
- **MCQ Standards:** Answers hidden in `<details><summary><b>Answer & Explanation</b></summary>`. Part A balanced with 20%–30% distribution for each of A, B, C, D (6–9 per letter).
- **Style:** GitHub callouts (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`). Mermaid diagrams first for complex flows before tables. Every note ends with a `Next:` link.

### 4. Decisions ("Exam Answer First, Real-World Note Second")
- When textbooks/exams (Forouzan, Kurose, GATE) differ from implementation reality, MCQs and cheatsheets use the EXAM answer, with a concise real-world note:
  - **ARP / RARP:** Network Layer (L3) *(in practice sits between L2 and L3 / encapsulated in L2 frame)*.
  - **ICMP / IGMP:** Network Layer (L3) *(encapsulated in IP Protocol 1 / 2)*.
  - **OSPF:** Network Layer (L3) *(encapsulated in IP Protocol 89)*.
  - **BGP:** Application Layer (L7) *(runs over TCP 179; functionally path-vector routing)*.
  - **RIP:** Application Layer (L7) *(runs over UDP 520; functionally distance-vector routing)*.
  - **DHCP / DNS:** Application Layer (L7) *(runs over UDP 67/68, UDP/TCP 53)*.
  - **Hardware:** Router = L3 device, Switch = L2 device, Hub = L1 device.
- Applied across modules 01, 02, 03 and all future modules.

### 5. Facts Needing Human Review
- None blocking. All formulas in 01 mathematically verified. Modules 01–03 patched to conform to exam-first classification.

### 6. Next 3 Actions
1. Author **04_Physical_Layer** (Signals, Nyquist/Shannon capacities, transmission media, line coding, PCM, numericals, 55 MCQs).
2. Author **05_Data_Link_Layer** (Framing, CRC, Stop-and-Wait/GBN/SR ARQ, CSMA/CD, Ethernet, numericals, 55 MCQs).
3. Run verification tooling (`lint.py`, `check_links.py`, `check_mcq_balance.py`, `update_index.py`).
