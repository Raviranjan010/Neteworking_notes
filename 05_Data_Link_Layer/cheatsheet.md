# 05. Data Link Layer (Part A) — One-Page Cheatsheet

> **High-yield revision sheet for university exams, GATE, and technical interview screens.**

---

## ⚡ Framing & Error Control at a Glance

| Technique | Primary Mechanism | Guaranteed Capability | Standard Protocol | Key Nuance |
|---|---|---|---|---|
| **HDLC Bit Stuffing** | Insert `0` after five consecutive `1`s | Delineates frames with `01111110` | HDLC, PPP | Receiver strips `0`; overhead ~1.5% |
| **Byte Stuffing** | Prepend `ESC` (`0x7D`) to `FLAG`/`ESC` | Character-oriented framing | BISYNC, PPP | Worst-case overhead = 100% |
| **1-D Parity** | Single bit ensures even/odd ones | Detects odd errors ($d_{\min}=2$) | ASCII, UART | Zero error correction ($t=0$) |
| **2-D Parity** | Row parity + Column LRC | Detects $\le 3$ errors; corrects 1 bit | Magnetic tapes | Intersection gives $(row, col)$ flip |
| **Internet Checksum** | 16-bit 1's complement sum + NOT | Detects transport bit inversions | IPv4, TCP, UDP | End-around carry; blind to reordering |
| **CRC (FCS)** | Modulo-2 polynomial division | 100% burst errors $\le r$ | Ethernet, Wi-Fi | Hardware LFSR; $r$ zeros appended |
| **Hamming Code** | $2^r \ge m + r + 1$; parity at $2^k$ | Single-bit error correction ($t=1$) | ECC Memory, Satellite | Syndrome integer points to error bit |

---

## 📐 Essential Formulas & Decision Rules

| Concept / Metric | Mathematical Formula | Variables & Units | Golden Rule |
|---|---|---|---|
| **Hamming Inequality** | $$2^r \ge m + r + 1$$ | $m$: data bits, $r$: parity bits | $m=4 \implies r=3$; $m=8 \implies r=4$; $m=16 \implies r=5$ |
| **Detection Distance** | $$d_{\min} \ge d + 1$$ | $d$: errors to detect | To detect 2-bit error $\implies d_{\min} \ge 3$ |
| **Correction Distance** | $$d_{\min} \ge 2t + 1$$ | $t$: errors to correct | To correct 1-bit error $\implies d_{\min} \ge 3$; 2-bit $\implies d_{\min} \ge 5$ |
| **Simultaneous Bound** | $$d_{\min} \ge t + d + 1$$ | $t$: corrected, $d$: detected ($d > t$) | To correct 1 and detect 2 $\implies d_{\min} \ge 4$ (SECDED) |
| **CRC FCS Bits** | $$r = \deg(G(x))$$ | Degree of highest power of $x$ | Append $r$ zeros, NOT $(r+1)$ zeros |
| **CRC Burst Detection**| $$P = 1 - (1/2)^{r-1}$$ | Burst length $L = r + 1$ | $L \le r$ is 100% detected; $L=r+1 \implies 99.997\%$ for CRC-16 |

---

## 🛠️ CLI Diagnostics & Command Cheat Sheet

| Command | Environment | Purpose / What to Look For |
|---|---|---|
| `show interface <id>` | Cisco IOS | Inspect `input errors`, `CRC`, `frame` counters (nonzero indicates bad cable/duplex) |
| `ip -s link show <dev>` | Linux | Inspect `RX errors` and `dropped` packet counters |
| `ethtool -S <dev>` | Linux | Displays detailed hardware ASIC counters: `rx_crc_errors`, `rx_fcs_errors` |
| `tshark -r trace.pcap -Y "eth.fcs_bad == 1"` | CLI Wireshark | Filters packets with invalid FCS trailers |

---

## ⚠️ Top 5 Exam & Interview Traps

1. **"Generator Polynomial Degree vs. Bits":** Polynomial $G(x) = x^4 + x + 1$ has **$r = 4$ degree**, requires **$r = 4$ appended zeros**, but has **$r + 1 = 5$ binary bits** (`10011`). Never append 5 zeros!
2. **"Detection vs. Correction Distance":** To *detect* $k$ errors requires $d_{\min} = k + 1$. To *correct* $k$ errors requires $d_{\min} = 2k + 1$. Confusing detection with correction loses marks.
3. **"Exam Answer First, Real-World Note Second" (Ethernet Reliability):**
   - **Exam Answer:** Data Link Layer provides error detection and framing.
   - **Real-World Note:** Ethernet silently **drops** CRC-corrupted frames without generating retransmissions or ICMP error messages. Reliability is delegated to TCP.
4. **"HDLC Bit Stuffing Trigger":** Stuffed zeros are added after **five** consecutive 1s in data, NOT six. If six 1s were allowed to pass, the receiver would misinterpret user data as a `FLAG`.
5. **"Checksum Commutativity":** Checksum addition is commutative. If words $A$ and $B$ swap positions, the sum is unchanged and the corruption goes undetected.

---

## ⬅️ Navigation
- **Module Overview:** [README.md](README.md)
- **Deep-Dive Notes:** [notes.md](notes.md)
- **Solved Numericals:** [numericals.md](numericals.md)
- **Visual Diagrams:** [diagrams.md](diagrams.md)
- **Practice Questions:** [mcqs.md](mcqs.md)
- **Interview Q&A:** [interview_qa.md](interview_qa.md)
- **Next Sub-step:** [05b Flow Control & ARQ](../05_Data_Link_Layer/)
