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

## ⬅️ Navigation
- **Module Overview:** [README.md](README.md)
- **Deep-Dive Notes:** [notes.md](notes.md)
- **Solved Numericals:** [numericals.md](numericals.md)
- **Visual Diagrams:** [diagrams.md](diagrams.md)
- **Practice Questions:** [mcqs.md](mcqs.md)
- **One-Page Cheatsheet:** [cheatsheet.md](cheatsheet.md)
- **Next Sub-step:** [05b Flow Control & ARQ](../05_Data_Link_Layer/)
