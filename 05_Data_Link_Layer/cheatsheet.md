# 05. Data Link Layer — Master Revision Cheatsheet

> **High-yield one-page revision sheet for university exams, GATE CS/IT, and technical interview screens.**

---

## ⚡ 1. Framing & Error Control at a Glance (05a)

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

## 🔄 2. Flow Control & ARQ Protocols at a Glance (05b)

| Metric / Property | Stop-and-Wait ARQ | Go-Back-N (GBN) ARQ | Selective Repeat (SR) ARQ |
|---|---|---|---|
| **Sender Window ($W_s$)** | $1$ | $\le 2^k - 1$ | $\le 2^{k-1}$ |
| **Receiver Window ($W_r$)** | $1$ | $1$ | $\le 2^{k-1}$ (normally $W_s$) |
| **Min Sequence Bits ($k$)** | $1$ bit (0 and 1) | $\lceil \log_2(W_s + 1) \rceil$ | $\lceil \log_2(2 W_s) \rceil$ |
| **Window Sum Rule** | $W_s + W_r = 2 \le 2^1$ | $W_s + W_r = 2^k$ | $W_s + W_r = 2^k$ |
| **Out-of-Order Frames** | Discarded | Discarded immediately | Accepted and buffered |
| **Receiver Buffer Size** | $1$ frame | $1$ frame | $W_r$ frames ($2^{k-1}$) |
| **ACK Type** | Alternating ($ACK_0, ACK_1$) | Cumulative ($ACK_n$) | Individual / Selective ($SACK$) |
| **Retransmit on Timeout**| Single frame | Entire pending window ($N$ frames) | Only the single lost frame |
| **Timer Allocation** | $1$ timer | $1$ timer (for oldest un-ACKed frame) | $N$ timers (one per frame) |
| **Ideal Efficiency ($\eta$)** | $\frac{1}{1 + 2a}$ | $\min\left(1, \frac{N}{1 + 2a}\right)$ | $\min\left(1, \frac{N}{1 + 2a}\right)$ |
| **Effective Util Under Loss $P$** | $\frac{1 - P}{1 + 2a}$ | $\frac{1 - P}{1 + (N-1)P} \cdot \frac{N}{1 + 2a}$ | $(1 - P) \cdot \min\left(1, \frac{N}{1 + 2a}\right)$ |

---

## 📐 3. Essential Formulas & Decision Rules

| Concept / Metric | Mathematical Formula | Variables & Units | Golden Rule |
|---|---|---|---|
| **Ratio parameter $a$** | $$a = \frac{T_p}{T_t} = \frac{d/v}{L/B}$$ | $T_p, T_t$ in seconds or ms | When $a \gg 1$, Stop-and-Wait efficiency collapses |
| **Bandwidth-Delay Product** | $$\text{BDP} = B \times 2T_p \text{ bits} = 2a \text{ frames}$$ | $B$ in bps, $T_p$ in s, $L$ in bits | Window size must equal BDP to fill the pipe |
| **Optimal Window Size** | $$N_{\text{opt}} = \lceil 1 + 2a \rceil$$ | Frames | Minimum window size for $100\%$ channel utilization |
| **Average Transmissions** | $$\mathbb{E}[N_{tx}] = \frac{1}{1 - P}$$ | $P$: frame loss probability | Applies to Stop-and-Wait and Selective Repeat |
| **Hamming Inequality** | $$2^r \ge m + r + 1$$ | $m$: data bits, $r$: parity bits | $m=4 \implies r=3$; $m=8 \implies r=4$; $m=16 \implies r=5$ |
| **Detection Distance** | $$d_{\min} \ge d + 1$$ | $d$: errors to detect | To detect 2-bit error $\implies d_{\min} \ge 3$ |
| **Correction Distance** | $$d_{\min} \ge 2t + 1$$ | $t$: errors to correct | To correct 1-bit error $\implies d_{\min} \ge 3$; 2-bit $\implies d_{\min} \ge 5$ |
| **Simultaneous Bound** | $$d_{\min} \ge t + d + 1$$ | $t$: corrected, $d$: detected ($d > t$) | To correct 1 and detect 2 $\implies d_{\min} \ge 4$ (SECDED) |
| **CRC FCS Bits** | $$r = \deg(G(x))$$ | Degree of highest power of $x$ | Append $r$ zeros, NOT $(r+1)$ zeros |

---

## 🛠️ 4. CLI Diagnostics & Command Cheat Sheet

| Command | Environment | Purpose / What to Look For |
|---|---|---|
| `show interface <id>` | Cisco IOS | Inspect `input errors`, `CRC`, `frame` counters (nonzero indicates bad cable/duplex) |
| `ip -s link show <dev>` | Linux | Inspect `RX errors` and `dropped` packet counters |
| `ethtool -S <dev>` | Linux | Displays detailed hardware ASIC counters: `rx_crc_errors`, `rx_fcs_errors` |
| `tshark -r trace.pcap -Y "eth.fcs_bad == 1"` | CLI Wireshark | Filters packets with invalid FCS trailers |
| `ethtool -a <dev>` | Linux | Displays Layer 2 pause frame (flow control) auto-negotiation status |

---

## ⚠️ 5. Top 7 Exam & Interview Traps

1. **"GBN Sequence Number Bits":** If sender window is $N = 7$, students answer $\log_2(7) = 3$ bits (correct, $2^3 - 1 = 7$). But if $N = 8$, students often answer $\log_2(8) = 3$ bits! **Wrong!** $2^3 - 1 = 7 < 8$, so $N=8$ requires **$k = 4$ bits** ($\lceil \log_2(8 + 1) \rceil = 4$).
2. **"Selective Repeat Window Limit":** In SR, $W_s \le 2^{k-1}$. For $k = 4$, max window is $2^3 = 8$, NOT 15. Window sum $W_s + W_r \le 2^k$ is absolute.
3. **"Overlapping Window Failure Mode":** Violating $W_s + W_r \le 2^k$ does NOT cause CRC errors; it causes the receiver to accept old retransmitted duplicate frames as brand-new data!
4. **"Detection vs. Correction Distance":** To *detect* $k$ errors requires $d_{\min} = k + 1$. To *correct* $k$ errors requires $d_{\min} = 2k + 1$.
5. **"Exam Answer First, Real-World Note Second" (Ethernet Reliability):**
   - **Exam Answer:** Data Link Layer provides framing, error detection, and sliding window flow control.
   - **Real-World Note:** Wired Ethernet silently **drops** CRC-corrupted frames without Layer 2 ARQ retransmissions. End-to-end reliability is handled by TCP at Layer 4.
6. **"Generator Polynomial Degree vs. Bits":** Polynomial $G(x) = x^4 + x + 1$ has **$r = 4$ degree**, requires **$r = 4$ appended zeros**, but has **$r + 1 = 5$ binary bits** (`10011`). Never append 5 zeros!
7. **"Stop-and-Wait ACK Loss":** When an ACK is lost, the sender retransmits the data frame. The receiver **must discard the duplicate payload** before re-sending the ACK to prevent application duplicate delivery.

---

## ⬅️ Navigation
- **Module Index:** [INDEX.md](../INDEX.md)
- **Deep-Dive Notes:** [notes.md](notes.md) | [notes_05b_flow_control.md](notes_05b_flow_control.md)
- **Solved Numericals:** [numericals.md](numericals.md) | [numericals_05b_flow_control.md](numericals_05b_flow_control.md)
- **Visual Diagrams:** [diagrams.md](diagrams.md) | [diagrams_05b_flow_control.md](diagrams_05b_flow_control.md)
- **Practice Question Bank:** [mcqs.md](mcqs.md)
- **Interview Q&A:** [interview_qa.md](interview_qa.md)
- **Next Sub-step:** [05c MAC Protocols & Ethernet 802.3](../05_Data_Link_Layer/)
