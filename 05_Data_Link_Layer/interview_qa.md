# 05. Data Link Layer (Part A) — Technical Interview Q&A

> **20 High-yield interview questions covering Framing, Error Detection, CRC, and Hamming Codes for Systems, Firmware, and Network Engineering roles.**

---

## 📑 Question Navigation
- [Foundations & Framing (Q1–Q7)](#foundations--framing)
- [Error Detection & CRC Mechanics (Q8–Q14)](#error-detection--crc-mechanics)
- [Hamming Codes & Production Diagnostics (Q15–Q20)](#hamming-codes--production-diagnostics)

---

## Foundations & Framing

### Q1. What is the fundamental difference between the Physical Layer and the Data Link Layer?
- **Level:** Basic
- **30-Second Summary:** The Physical Layer transmits raw, unformatted bits across a medium without awareness of content or boundaries. The Data Link Layer organizes raw bits into discrete **Frames**, adds hardware addressing (MAC), and detects errors. See [notes.md#1-high-level-architectural-overview](notes.md#1-high-level-architectural-overview).
- **Deep Answer:** The Physical Layer handles voltages, optical pulses, and line rates. The Data Link Layer provides framing, media access arbitration, and error control.
- **Interview Tip:** Always emphasize that frames have distinct headers, payloads, and trailers (FCS).

---

### Q2. Why did the IEEE 802 committee split Layer 2 into LLC and MAC sublayers?
- **Level:** Medium
- **30-Second Summary:** To decouple physical transmission hardware from network protocol software. The MAC sublayer manages media-specific details (CSMA/CD on Ethernet vs. CSMA/CA on Wi-Fi), while the Logical Link Control (LLC — 802.2) sublayer presents a uniform interface to Layer 3.
- **Deep Answer:** Without this split, every change in physical transmission hardware would require modifying Network Layer IP drivers. See [diagrams.md#1-ieee-802-sublayer-architecture-llc-vs-mac](diagrams.md#1-ieee-802-sublayer-architecture-llc-vs-mac).

---

### Q3. Why is character count considered an obsolete framing method?
- **Level:** Basic
- **30-Second Summary:** It lacks framing error resilience. A single-bit corruption in any frame's length count causes the receiver to lose frame synchronization indefinitely.
- **Deep Answer:** Delimiter flags (bit/byte stuffing) allow receivers to resynchronize at the very next flag byte, whereas character count cannot recover until transmission stops. See [notes.md#21-character-count](notes.md#21-character-count).

---

### Q4. How does HDLC bit stuffing work, and why is it called "transparent"?
- **Level:** Medium
- **30-Second Summary:** The transmitter automatically injects a `0` bit after any sequence of five consecutive `1`s. This guarantees that user data never mimics the 6-consecutive-ones frame delimiter `01111110`. It is "transparent" because the receiver strips the stuffed zeros, completely hiding the mechanism from upper layers.
- **Deep Answer:** See worked execution in [notes.md#23-bit-stuffing-bit-oriented-framing--hdlc-standard](notes.md#23-bit-stuffing-bit-oriented-framing--hdlc-standard).
- **Common Trap:** Stuffed bits are NOT parity bits; they carry zero information and exist solely for boundary delineation.

---

### Q5. What is the difference between bit stuffing and byte stuffing?
- **Level:** Basic
- **30-Second Summary:** Byte stuffing operates on character boundaries by inserting escape bytes (`ESC`) before literal `FLAG` or `ESC` payload bytes (used in PPP/BISYNC). Bit stuffing operates at the raw bit level by inserting a `0` after five consecutive `1`s (used in HDLC).
- **Deep Answer:** Byte stuffing introduces variable overhead up to 100% on binary data; bit stuffing introduces average overhead of only ~1.5% to 3%.

---

### Q6. How does physical layer coding violation achieve framing without data stuffing overhead?
- **Level:** Hard
- **30-Second Summary:** Certain line coding schemes (like Manchester or 4B/5B) contain invalid physical signal combinations that never represent legitimate data symbols. Transmitting these invalid states signals frame boundaries out-of-band with zero payload stuffing overhead.
- **Deep Answer:** For example, Manchester encoding requires a voltage transition in the middle of every bit cell; maintaining a high or low level throughout the bit cell violates the code and signals a delimiter.

---

### Q7. What is the MTU of standard Ethernet, and what dictates its lower and upper bounds?
- **Level:** Medium
- **30-Second Summary:** Maximum Transmission Unit is **1500 bytes**. The lower bound (minimum frame size 64 bytes, payload 46 bytes) is dictated by half-duplex CSMA/CD collision detection ($T_t \ge 2T_p$). The upper bound (1500 bytes) was chosen in 1980 to limit receiver buffer memory consumption and prevent channel monopolization.

---

## Error Detection & CRC Mechanics

### Q8. What is the fundamental difference between Error Detection and Forward Error Correction (FEC)?
- **Level:** Basic
- **30-Second Summary:** **Exam Answer First:** Error detection detects corrupted frames and relies on ARQ retransmissions to achieve reliability. FEC adds mathematical redundancy allowing the receiver to locate and repair errors locally. **Real-World Note Second:** FEC is used in deep-space/satellite links and 100G/400G optical PHYs, while standard Ethernet uses CRC detection and silent drops.

---

### Q9. What is Minimum Hamming Distance ($d_{\min}$), and what does it tell you about code capabilities?
- **Level:** Medium
- **30-Second Summary:** $d_{\min}$ is the smallest number of bit flips that transforms one valid codeword into another valid codeword.
  - To detect $d$ errors: $d_{\min} \ge d + 1$.
  - To correct $t$ errors: $d_{\min} \ge 2t + 1$.
  - See mathematical explanation in [notes.md#4-hamming-distance-detection--correction-limits](notes.md#4-hamming-distance-detection--correction-limits).

---

### Q10. Why is simple 1-D parity completely incapable of correcting errors?
- **Level:** Basic
- **30-Second Summary:** Simple parity appends 1 bit, giving $d_{\min} = 2$. By the correction formula $t = \lfloor \frac{d_{\min}-1}{2} \rfloor = \lfloor \frac{1}{2} \rfloor = 0$. While it can detect that an odd number of errors occurred, it provides zero spatial coordinate information on *which* bit flipped.

---

### Q11. How does 2-D parity locate and correct a single-bit error?
- **Level:** Medium
- **30-Second Summary:** Data is formatted as a rectangular matrix with row and column parities. A single bit flip invalidates exactly one row parity check and exactly one column parity check. The intersection point of the invalid row and column identifies the corrupted bit. See [diagrams.md#5-2-dimensional-parity-grid-error-detection--correction](diagrams.md#5-2-dimensional-parity-grid-error-detection--correction).

---

### Q12. How does the Internet Checksum (RFC 1071) differ mathematically from CRC?
- **Level:** Hard
- **30-Second Summary:** The Internet Checksum uses 16-bit one's complement addition with end-around carries (simple to compute in CPU software, but blind to byte reordering). CRC uses Galois Field polynomial division over $GF(2)$ using bitwise XOR (computationally heavier, but detects all burst errors $\le r$).
- **Deep Answer:** Checksums were chosen for IP/TCP because 1980s CPUs could compute them in software loops; CRC is implemented in hardware ASICs at Layer 2.

---

### Q13. Why must a CRC generator polynomial have a non-zero $x^0$ term?
- **Level:** Hard
- **30-Second Summary:** If the $x^0$ term is zero, $G(x)$ contains a factor of $x$, meaning all codewords end in zero and division shifts bits without checking the LSB. A non-zero $x^0$ term guarantees that $G(x)$ does not divide $x^k$, ensuring all single-bit errors $E(x) = x^k$ are 100% detected.

---

### Q14. What are the burst error detection guarantees of an $r$-degree CRC polynomial?
- **Level:** Medium
- **30-Second Summary:**
  - Burst length $L \le r$: **100% detected**.
  - Burst length $L = r + 1$: detected with probability $1 - (1/2)^{r-1}$ (e.g. 99.997% for CRC-16).
  - Burst length $L > r + 1$: detected with probability $1 - (1/2)^r$.

---

## Hamming Codes & Production Diagnostics

### Q15. How do you determine the required number of parity bits in a Hamming code?
- **Level:** Medium
- **30-Second Summary:** Using the Hamming inequality: $2^r \ge m + r + 1$, where $m$ is data bits and $r$ is parity bits. $r$ bits must represent $(m + r)$ error positions plus the $1$ "no error" condition. For $m = 4 \implies r = 3$ (Hamming(7,4)). For $m = 8 \implies r = 4$.

---

### Q16. In Hamming code, why are parity bits placed at positions that are powers of 2?
- **Level:** Medium
- **30-Second Summary:** Placing parity bits at indices $1, 2, 4, 8, \dots$ ($2^k$) ensures that each parity bit has a single $1$ in its binary representation. This creates an orthogonal basis where evaluating parity equations produces a binary syndrome whose integer value points directly to the erroneous bit index.

---

### Q17. What is SECDED, and why is it standard in server ECC RAM?
- **Level:** Hard
- **30-Second Summary:** Single Error Correction, Double Error Detection. It augments a Hamming code with an overall parity bit covering the entire codeword, increasing $d_{\min}$ from 3 to 4.
  - If syndrome is non-zero and overall parity is odd: **Single error corrected**.
  - If syndrome is non-zero and overall parity is even: **Double error detected (system alerts/halts without silent corruption)**.

---

### Q18. In Wireshark, why is the Ethernet Frame Check Sequence (FCS) usually missing or zeroed out?
- **Level:** Practical / SRE
- **30-Second Summary:** Modern Network Interface Cards (NICs) perform CRC checking in hardware ASIC. The NIC verifies the FCS, strips the 4-byte trailer, and hands only the verified packet to the operating system driver. Packets captured by libpcap/Npcap lack the FCS or show dummy `0x00000000`.

---

### Q19. How do you troubleshoot escalating `FCS/CRC Errors` on a Cisco or Linux switch port?
- **Level:** Practical / Network Engineering
- **30-Second Summary:** FCS errors indicate layer-1 physical transmission corruption:
  1. Inspect physical cable: replace patch cord; inspect fiber for dust or micro-bends.
  2. Check for duplex mismatch (one end configured as Half, other as Full).
  3. Check for high EMI (cable running parallel to high-voltage conduits or fluorescent ballasts).
  4. Swap SFP transceiver optics or switch port.
  - See diagnostic workflow in [diagrams.md#12-link-layer-diagnostic-workflow-for-crc-errors](diagrams.md#12-link-layer-diagnostic-workflow-for-crc-errors).

---

### Q20. If Ethernet only detects errors and drops frames, how does an application receive reliable data?
- **Level:** Foundational
- **30-Second Summary:** The Data Link Layer delegates end-to-end reliability to the Transport Layer (**TCP**). When Ethernet drops a corrupted frame, the receiving TCP stack never sends an acknowledgment (ACK). The sending TCP stack's Retransmission Timeout (RTO) expires, and TCP retransmits the missing segment end-to-end.

---

## Flow Control & ARQ Protocols (05b)

### Q21. What is the fundamental difference between Flow Control and Congestion Control?
- **Level:** Foundational / Systems
- **30-Second Summary:** Flow control is **point-to-point / end-to-end**: it prevents a fast transmitter from overwhelming the **receiver's local memory buffer**. Congestion control is **network-wide**: it prevents multiple transmitters from injecting more traffic than **intermediate routers, switches, and transit links** can physically carry.
- **Deep Answer:** Flow control is governed by explicit receiver buffer advertisements (e.g., TCP Receive Window `rcv_wnd` or 802.3x Pause frames). Congestion control is inferred from packet loss, latency growth, or explicit network signaling (TCP `cwnd`, ECN). See [notes_05b_flow_control.md#12-flow-control-vs-congestion-control](notes_05b_flow_control.md#12-flow-control-vs-congestion-control).

---

### Q22. Why is Stop-and-Wait ARQ catastrophically inefficient on high Bandwidth-Delay Product (BDP) links?
- **Level:** Medium
- **30-Second Summary:** In Stop-and-Wait, the sender transmits one frame and then idles for an entire Round-Trip Time ($2T_p$) waiting for confirmation. On high-delay links (such as satellite or transoceanic fiber), propagation delay dwarfs transmission delay ($a = T_p / T_t \gg 1$), resulting in efficiency $\eta = \frac{1}{1 + 2a} \to 0$. The transmission pipe remains $>95\%$ empty.
- **Deep Answer:** See numerical verification on satellite links in [numericals_05b_flow_control.md#problem-6-geostationary-satellite-link-with-stop-and-wait](numericals_05b_flow_control.md#problem-6-geostationary-satellite-link-with-stop-and-wait).

---

### Q23. How does Go-Back-N handle out-of-order frames, and why does this cause poor throughput on noisy links?
- **Level:** Hard
- **30-Second Summary:** Go-Back-N maintains a receiver window of strictly $W_r = 1$. If Frame $i$ is corrupted or lost, all subsequent undamaged frames ($i+1, i+2, \dots$) arriving at the receiver are discarded immediately. When the sender's timer for Frame $i$ expires, the sender must retransmit the entire pending window of $N$ frames, causing a retransmission storm.
- **Deep Answer:** Under error probability $P$, average transmissions per frame is $\frac{1 + (N-1)P}{1-P}$. Even low error rates drastically degrade GBN efficiency. See [notes_05b_flow_control.md#72-go-back-n-arq-under-loss](notes_05b_flow_control.md#72-go-back-n-arq-under-loss).

---

### Q24. How does Selective Repeat ARQ resolve the GBN retransmission storm, and what is the engineering trade-off?
- **Level:** Hard
- **30-Second Summary:** Selective Repeat expands the receiver window to $W_r = 2^{k-1}$. When an out-of-order frame arrives, it is accepted and stored in the receiver's buffer. The sender retransmits **only the specific missing frame**. Once it arrives, the receiver releases the buffered frames in order.
- **Trade-off:** High memory usage (must allocate buffer slots for all $W_r$ frames), individual timers per frame at sender, and complex sequence sorting logic in firmware/software. See [diagrams_05b_flow_control.md#9-selective-repeat-sr-arq-single-frame-recovery-via-out-of-order-buffering](diagrams_05b_flow_control.md#9-selective-repeat-sr-arq-single-frame-recovery-via-out-of-order-buffering).

---

### Q25. Why must the sender window in Go-Back-N be $W_s \le 2^k - 1$ instead of $2^k$?
- **Level:** High-Yield GATE / Deep Technical
- **30-Second Summary:** If $W_s = 2^k$, the sequence number of the first frame of the next generation becomes identical to the first frame of the current generation. If all ACKs for a full window are lost in transit, the sender retransmits Frame 0. The receiver, having already advanced to expect Frame 0 of the next cycle, cannot distinguish the old duplicate from new data, causing silent undetected data duplication.
- **Deep Answer:** By capping $W_s \le 2^k - 1$, the expected frame sequence number is never identical to any unacknowledged frame in flight. See [notes_05b_flow_control.md#62-the-overlapping-window-proof-for-go-back-n](notes_05b_flow_control.md#62-the-overlapping-window-proof-for-go-back-n).

---

### Q26. Why must Selective Repeat allocate window size $W_s \le 2^{k-1}$?
- **Level:** High-Yield GATE / Deep Technical
- **30-Second Summary:** In Selective Repeat, both sender and receiver maintain active windows. If $W_s > 2^{k-1}$ (for example, $W_s = W_r = 3$ with $k=2$), if all ACKs are lost, the receiver window slides forward to overlap with sequence numbers from the previous cycle. A retransmitted frame from the old cycle will fall inside the receiver's new window and be mistakenly accepted as fresh data.
- **Rule:** The sum of sender and receiver windows must never exceed the sequence space: $W_s + W_r \le 2^k$. When $W_s = W_r$, $W_s \le 2^{k-1}$. See [notes_05b_flow_control.md#63-the-overlapping-window-proof-for-selective-repeat](notes_05b_flow_control.md#63-the-overlapping-window-proof-for-selective-repeat).

---

### Q27. What is Piggybacking, and what prevents a transmitter from stalling if no reverse traffic exists?
- **Level:** Medium
- **30-Second Summary:** Piggybacking embeds acknowledgment numbers into the headers of reverse-direction data packets, halving standalone ACK framing overhead. To prevent transmission stalls when the reverse node has no data to send, a **delayed ACK timer** runs (typically 50–200 ms). When the timer expires, an independent standalone ACK is dispatched immediately.
- **Deep Answer:** See [diagrams_05b_flow_control.md#12-piggybacking-bidirectional-data-flow-timeline](diagrams_05b_flow_control.md#12-piggybacking-bidirectional-data-flow-timeline).

---

### Q28. How is optimal sliding window size derived from the Bandwidth-Delay Product (BDP)?
- **Level:** Medium / Core Networking
- **30-Second Summary:** To achieve 100% channel utilization without pausing, the sender must transmit enough bits during one Round-Trip Time to completely fill the transmission medium pipe. Thus:
  $$\text{Optimal Window Bits} = \text{BDP} = \text{Bandwidth} \times \text{RTT}$$
  Dividing by frame length $L$, the window in frames is $N_{\text{opt}} = 1 + 2a$ where $a = T_p / T_t$.

---

### Q29. Why does modern wired Ethernet (802.3) drop corrupt frames silently rather than providing Layer 2 ARQ?
- **Level:** Real-World Architecture
- **30-Second Summary:** Fiber and twisted-pair copper have Bit Error Rates (BER) below $10^{-12}$. Over 99.9999% of frames arrive intact. Maintaining state tables, sequence buffers, and retransmission timers at 100 Gbps in switch hardware would massively increase silicon cost and latency. Dropping corrupt frames in hardware ASIC and delegating rare retransmissions to end-to-end Layer 4 TCP is far more efficient.

---

### Q30. How does TCP Window Scaling (RFC 1323) overcome the classic 16-bit sliding window limitation?
- **Level:** Production Systems / Performance Engineering
- **30-Second Summary:** The standard TCP header allocates 16 bits for the Receive Window field, capping the maximum window at $2^{16} - 1 = 65,535\text{ bytes}$ (64 KB). On high-speed, long-fat networks (LFNs, e.g., 10 Gbps with 50 ms RTT, where $\text{BDP} \approx 62.5\text{ MB}$), throughput would be bottlenecked at $\approx 10\text{ Mbps}$. RFC 1323 introduces a Window Scale option during the SYN handshake that left-shifts the 16-bit window value up to 14 bits, enabling window sizes up to $1\text{ GB}$.

---

## ⬅️ Navigation
- **Module Index:** [INDEX.md](../INDEX.md)
- **Deep-Dive Notes:** [notes.md](notes.md) | [notes_05b_flow_control.md](notes_05b_flow_control.md)
- **Solved Numericals:** [numericals.md](numericals.md) | [numericals_05b_flow_control.md](numericals_05b_flow_control.md)
- **Visual Diagrams:** [diagrams.md](diagrams.md) | [diagrams_05b_flow_control.md](diagrams_05b_flow_control.md)
- **Practice Questions:** [mcqs.md](mcqs.md)
- **One-Page Cheatsheet:** [cheatsheet.md](cheatsheet.md)
- **Next Sub-step:** [05c MAC Protocols & Ethernet 802.3](../05_Data_Link_Layer/)

