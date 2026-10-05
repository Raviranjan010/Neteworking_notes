# 🤝 Contributing to Computer Networking Mastery

Thank you for your interest in making this repository the most complete, accurate, and visual networking learning resource in the world!

---

## 🎯 How You Can Contribute

1. **Fix typos or grammar:** Small corrections improve clarity for thousands of students.
2. **Report wrong numerical answers or MCQs:** Use our [Wrong Answer Issue Template](.github/ISSUE_TEMPLATE/wrong-answer.md).
3. **Contribute diagrams:** Mermaid sequence diagrams, flowcharts, or original SVGs for packet layouts.
4. **Submit hands-on labs:** Verified Cisco Packet Tracer CLI configs, Wireshark filter walkthroughs, or Python networking scripts.
5. **Suggest interview or exam questions:** Provide authentic questions from recent university papers, GATE exams, or tech interviews.

---

## 📐 Topic Module File Standard

Every numbered module folder (`01` through `16`) must strictly contain the following files:

```text
├── README.md        ← Module landing page (Time, Level, GATE/Interview weight, "Where this fits" map)
├── notes.md         ← Conceptual guide (Problem/Story → Analogy → Mechanics → Headers → Traps → Checklist)
├── diagrams.md      ← Mermaid sequence/flowcharts + SVG packet layouts (≥ 8-15 diagrams)
├── numericals.md    ← Solved calculations in 3 levels (Basic, Exam, GATE) verified with Python scripts
├── mcqs.md          ← 50+ balanced questions (MCQ, MSQ, NAT, Output) with hidden answers & explanations
├── interview_qa.md  ← Top 20-40 interview questions with 30-sec summary and detailed 2-min answer
└── cheatsheet.md    ← One-page printable revision summary
```

---

## 🛡️ Non-Negotiable Quality Gates

Before submitting a Pull Request, verify:
- [ ] **No placeholders:** Never leave `TODO`, `TBD`, `coming soon`, or `similar to above`.
- [ ] **Verified calculations:** Every numerical in `notes.md`, `numericals.md`, or `mcqs.md` must be computed with a Python script placed in `tools/verify/`.
- [ ] **Balanced MCQs:** In Part A (single-choice), options A, B, C, D must each be the correct answer 6–9 times (~25% each).
- [ ] **Mermaid syntax:** Test that all Mermaid diagrams render cleanly without syntax errors.
- [ ] **Color rules:** Use the standard diagram color palette (🟦 sender/client, 🟩 receiver/server, 🟥 error/loss, 🟨 header/intermediate).
- [ ] **No broken links:** Ensure all relative Markdown links resolve correctly.

---

## 🚀 Pull Request Process

1. Fork the repository and create your feature branch:
   ```bash
   git checkout -b feature/topic-upgrade
   ```
2. Make your edits following the style standards.
3. Run internal verification scripts.
4. Commit with a clear message:
   ```bash
   git commit -m "docs(05_datalink): add solved CRC numericals and python verifier"
   ```
5. Push to your branch and open a Pull Request.
