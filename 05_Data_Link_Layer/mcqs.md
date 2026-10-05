# 05. Data Link Layer — Practice Question Bank

> **Comprehensive Practice Question Bank organized by sub-module sections.**
> - **Section 05a:** Framing, Bit/Byte Stuffing, Parity, Checksums, CRC, and Hamming Codes (55 Questions).
> - **Section 05b:** Flow Control, Stop-and-Wait, Go-Back-N, Selective Repeat, Sliding Window Math (55 Questions).
> - **Section 05c:** Medium Access Control & Ethernet 802.3 (55 Questions).

---

# Section 05a: Framing & Errors

## Part A: Single-Choice Questions (1 to 30)

### Easy (Questions 1 to 10)

#### Q1. [Concept] What is the primary operational scope of the Data Link Layer?
- A) Hop-to-hop frame delivery between two directly connected nodes
- B) End-to-end packet delivery between arbitrary Internet hosts
- C) Process-to-process multiplexing using port numbers
- D) Transmission of raw unformatted electrical voltages
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
The Data Link Layer is strictly responsible for node-to-node (hop-by-hop) frame transmission across a single physical link. See [notes.md#1-high-level-architectural-overview](notes.md#1-high-level-architectural-overview).
</details>

#### Q2. [Concept] Which sublayer of the IEEE 802 architecture interfaces directly with the Network Layer?
- A) Medium Access Control (MAC) sublayer
- B) Logical Link Control (LLC) sublayer
- C) Physical Medium Dependent (PMD) sublayer
- D) Physical Coding Sublayer (PCS)
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
LLC (IEEE 802.2) sits above the MAC sublayer and presents a uniform link interface to Network Layer protocols like IPv4 and IPv6.
</details>

#### Q3. [Concept] In HDLC bit stuffing, what is the exact delimiter flag byte sequence?
- A) `10101010`
- B) `11111111`
- C) `01111110`
- D) `00000000`
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
HDLC frames begin and end with the unique 8-bit flag sequence `01111110` (`0x7E`).
</details>

#### Q4. [Company] In HDLC bit stuffing, when does the transmitter automatically inject a '0' bit?
- A) After every five consecutive '0' bits
- B) After every byte of user payload
- C) After any occurrence of `0x7E`
- D) After every five consecutive '1' bits
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
Whenever five consecutive 1s appear in data, a 0 is stuffed to prevent user data from mimicking the 6-consecutive-ones flag pattern `01111110`.
</details>

#### Q5. [GATE-style] If the minimum Hamming distance $d_{\min}$ of a block code is 4, what is the maximum number of bit errors it can guarantee to detect?
- A) 3 bit errors
- B) 4 bit errors
- C) 2 bit errors
- D) 1 bit error
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Detection condition is $d_{\min} \ge d + 1 \implies d = d_{\min} - 1 = 4 - 1 = 3$. See [notes.md#4-hamming-distance-detection--correction-limits](notes.md#4-hamming-distance-detection--correction-limits).
</details>

#### Q6. [Concept] What is the major vulnerability of the Character Count framing method?
- A) It introduces up to 50% framing overhead
- B) A single bit error in a count byte desynchronizes all subsequent frames
- C) It requires complex polynomial hardware
- D) It cannot be implemented in software
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
If a count byte is corrupted, the receiver misinterprets frame boundaries, causing a catastrophic cascading framing error.
</details>

#### Q7. [Company] In byte stuffing, if the payload contains the escape byte `ESC` itself, what does the sender transmit?
- A) `FLAG` followed by `ESC`
- B) `FLAG` followed by `FLAG`
- C) `ESC` followed by `ESC`
- D) The byte is dropped
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
To transmit an escape byte as user data, the sender precedes it with an escape byte: `ESC ESC`.
</details>

#### Q8. [Concept] What type of error detection is provided by simple 1-D Even Parity?
- A) Detects all even numbers of bit errors
- B) Corrects single-bit errors
- C) Detects burst errors of length up to 8
- D) Detects all odd numbers of bit errors
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
Any odd number of inverted bits changes the overall parity, whereas any even number of inverted bits leaves parity unchanged and goes undetected.
</details>

#### Q9. [GATE-style] To correct up to $t = 2$ bit errors, what is the minimum Hamming distance $d_{\min}$ required?
- A) 5
- B) 4
- C) 3
- D) 2
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Correction condition is $d_{\min} \ge 2t + 1 \implies d_{\min} \ge 2(2) + 1 = 5$.
</details>

#### Q10. [Concept] Which arithmetic operation is equivalent to binary addition and subtraction in Modulo-2 arithmetic?
- A) Bitwise AND
- B) Bitwise XOR
- C) Bitwise OR
- D) Arithmetic subtraction with borrow
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Modulo-2 addition and subtraction are identical and equivalent to the exclusive-OR (XOR) operation without carries or borrows.
</details>

---

### Medium (Questions 11 to 20)

#### Q11. [GATE-style] A generator polynomial is given as $G(x) = x^4 + x + 1$. How many redundant bits (FCS) does it append to the data?
- A) 5 bits
- B) 16 bits
- C) 4 bits
- D) 3 bits
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
The degree of $G(x)$ is $r = 4$. A CRC generator of degree $r$ always generates an $r$-bit remainder (FCS) and appends $r$ zeros.
</details>

#### Q12. [Company] In a (7,4) Hamming code, which bit positions are assigned to parity bits?
- A) Positions 1, 3, 5
- B) Positions 3, 5, 6, 7
- C) Positions 5, 6, 7
- D) Positions 1, 2, 4
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
Parity bits occupy bit positions that are powers of 2: $2^0=1, 2^1=2, 2^2=4$. Positions 3, 5, 6, and 7 are reserved for data bits.
</details>

#### Q13. [GATE-style] How many parity bits $r$ are required to construct a single-error-correcting Hamming code for $m = 11$ data bits?
- A) 4 bits
- B) 3 bits
- C) 5 bits
- D) 6 bits
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
$2^r \ge m + r + 1$. For $r=4$: $2^4 = 16 \ge 11 + 4 + 1 = 16$ (Satisfied!).
</details>

#### Q14. [Concept] A CRC generator polynomial $G(x)$ will detect all odd numbers of bit errors if and only if:
- A) It has no zero coefficients
- B) It contains $(x + 1)$ as a factor
- C) Its degree is a power of 2
- D) It begins with $x^3$
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
A polynomial divisible by $(x + 1)$ evaluates to 0 at $x = 1$, which guarantees that any error polynomial with an odd number of terms cannot be evenly divided by $G(x)$.
</details>

#### Q15. [Company] What is the transmitted bitstream when the data `01111111` is processed using HDLC bit stuffing?
- A) `01111111`
- B) `01111101`
- C) `011111011`
- D) `011111110`
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
The sender counts five 1s (`011111`), inserts a `0`, and then transmits the remaining two 1s (`11`), resulting in `011111011`.
</details>

#### Q16. [GATE-style] For a CRC polynomial of degree $r = 16$, what is the guaranteed error-detection capability for burst errors of length $L \le 16$?
- A) 50%
- B) 99.9%
- C) 99.998%
- D) 100%
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
Any CRC polynomial of degree $r$ detects **100%** of all burst errors of length $L \le r$.
</details>

#### Q17. [Concept] What is the value obtained at a receiver when it sums all incoming 16-bit words including an uncorrupted Internet Checksum?
- A) `0xFFFF`
- B) `0x0000`
- C) `0xAAAA`
- D) `0x1000`
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Because the checksum is the one's complement of the data sum, adding the data sum to the checksum produces all binary 1s (`0xFFFF`).
</details>

#### Q18. [GATE-style] What is the binary representation of the generator polynomial $G(x) = x^5 + x^2 + 1$?
- A) `101001`
- B) `100101`
- C) `10101`
- D) `110011`
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
$G(x) = 1\cdot x^5 + 0\cdot x^4 + 0\cdot x^3 + 1\cdot x^2 + 0\cdot x^1 + 1\cdot x^0 \implies \mathbf{100101}$.
</details>

#### Q19. [Company] In 2-Dimensional parity, what is the maximum number of arbitrary bit errors guaranteed to be detected?
- A) 1
- B) 2
- C) 3
- D) 4
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
2D parity detects any 1, 2, or 3 bit errors anywhere in the matrix. A 4-bit error arranged at the four corners of a rectangle can trick parity.
</details>

#### Q20. [Concept] Which network environment predominantly favors Forward Error Correction (FEC) over ARQ?
- A) Campus Local Area Networks (LAN)
- B) Low-latency datacenter InfiniBand
- C) Fiber-optic transcontinental backbones
- D) Deep-space satellite communication links
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
Satellite and deep-space channels have massive propagation delays ($T_p$); waiting for ARQ retransmissions is intolerable, necessitating local FEC repair.
</details>

---

### Hard (Questions 21 to 30)

#### Q21. [GATE-style] Data $100100$ is protected by generator polynomial $G(x) = x^3 + x^2 + 1$ ($1101$). What is the transmitted codeword?
- A) `100100001`
- B) `100100010`
- C) `100100101`
- D) `100100111`
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Appending 3 zeros gives `100100000`. Modulo-2 division by `1101` yields remainder `001`. Codeword is `100100001`. See [numericals.md#problem-21-crc-modulo-2-polynomial-long-division](numericals.md#problem-21-crc-modulo-2-polynomial-long-division).
</details>

#### Q22. [GATE-style] In an even parity Hamming(7,4) code with bit positions 1 to 7, the receiver receives the corrupted word `0110111`. If syndrome evaluation yields $S = 5$, what is the original data nibble ($d_3, d_5, d_6, d_7$)?
- A) `1111`
- B) `1011`
- C) `0110`
- D) `1101`
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Syndrome $S = 5$ means bit position 5 is inverted. Bit 5 was received as `1`, so its correct value is `0`. The corrected codeword is `0110011`. Extracting data bits at positions 3, 5, 6, 7 yields `1011`.
</details>

#### Q23. [Company] A byte-stuffing protocol uses `FLAG = 0x7E` and `ESC = 0x7D`. If a 4-byte payload consists entirely of `[0x7E, 0x7E, 0x7D, 0x7D]`, what is the total length of the transmitted frame including opening and closing flags?
- A) 8 bytes
- B) 9 bytes
- C) 10 bytes
- D) 6 bytes
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
Each of the 4 payload bytes requires an `ESC` prefix: $4 \times 2 = 8\text{ bytes}$. Adding opening and closing `FLAG` bytes yields $8 + 2 = 10\text{ bytes}$.
</details>

#### Q24. [GATE-style] What is the probability that a CRC-16 polynomial fails to detect an undetected burst error of length $L = 17$ bits?
- A) $1 / 65536$
- B) $1 / 16$
- C) $1 / 256$
- D) $1 / 32768$
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
For burst length $L = r + 1$, undetected probability is $(1/2)^{r-1} = (1/2)^{16-1} = (1/2)^{15} = 1 / 32768$.
</details>

#### Q25. [Concept] Why does Ethernet's 32-bit CRC (FCS) silently discard corrupted frames rather than requesting a link-layer retransmission?
- A) Ethernet is an unreliable, best-effort link layer designed for speed; reliability is delegated to TCP
- B) Ethernet hardware cannot detect whether a frame has errors
- C) Retransmissions are prohibited by IEEE 802.3 standards
- D) Switches store all packets permanently in non-volatile flash
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Ethernet provides connectionless, unacknowledged service. If a frame has CRC corruption, the NIC drops it immediately to avoid wasting CPU resources.
</details>

#### Q26. [GATE-style] How many bits are required in a Hamming code to send 64 data bits with single-error correction capability?
- A) 6 bits
- B) 7 bits
- C) 8 bits
- D) 9 bits
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
$2^r \ge 64 + r + 1$. For $r=6$: $64 \not\ge 71$. For $r=7$: $128 \ge 64 + 7 + 1 = 72$ (Satisfied!).
</details>

#### Q27. [Company] In a system calculating 16-bit Internet Checksum, what occurs if two separate 16-bit words swap positions during transit?
- A) The checksum detects the error immediately
- B) The connection is reset by the receiver
- C) The checksum fails to detect the reordering because addition is commutative
- D) An ICMP Parameter Problem message is generated
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
Checksum addition is mathematically commutative ($A + B = B + A$); reordered words produce an identical sum, highlighting a known limitation of checksums.
</details>

#### Q28. [GATE-style] A block code has valid codewords: `00000`, `01101`, `10110`, `11011`. What is the minimum Hamming distance $d_{\min}$ of this code?
- A) 1
- B) 2
- C) 4
- D) 3
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
Distances between pairs:  
$d(00000, 01101) = 3$  
$d(00000, 10110) = 3$  
$d(00000, 11011) = 3$  
$d(01101, 10110) = 4$  
$d(01101, 11011) = 3$  
$d(10110, 11011) = 3$.  
The minimum distance across all pairs is $\mathbf{3}$.
</details>

#### Q29. [Concept] What is SECDED in the context of computer memory and error correction?
- A) Single Error Correction, Double Error Detection using Hamming code plus an overall parity bit
- B) Synchronous Ethernet Collision Detection and Error Demarcation
- C) Serial Error Correction with Direct Encoding Devices
- D) Selective Error Checksum for Distributed Enterprise Datacenters
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
SECDED adds one additional parity bit covering the entire Hamming codeword, expanding $d_{\min}$ from 3 to 4, enabling single-error correction and double-error detection.
</details>

#### Q30. [Company] How is CRC implemented in high-speed network switches operating at 100 Gbps?
- A) In software running on the control-plane CPU
- B) Using lookup tables stored in system RAM
- C) Using parallel Linear Feedback Shift Register (LFSR) logic gates in ASIC hardware
- D) By transmitting packets to cloud servers for verification
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
Hardware XOR gates and shift register taps execute CRC verification in a single clock cycle at multi-gigabit line rates.
</details>

---

## Part B: Multiple Select Questions (31 to 40)

#### Q31. [Concept] Which of the following framing techniques rely on in-band control characters or flag sequences?
- [ ] A) Flag bytes with Byte Stuffing
- [ ] B) Physical Layer Coding Violations
- [ ] C) HDLC Bit Stuffing
- [ ] D) Character Count
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, C**  
Byte stuffing (`FLAG`/`ESC`) and bit stuffing (`01111110`) use in-band bit/byte patterns. Physical coding violations use invalid line signals (out-of-band). Character count uses an integer length.
</details>

#### Q32. [GATE-style] Which errors are guaranteed to be detected by a CRC polynomial that contains $(x + 1)$ as a factor and has non-zero $x^r$ and $x^0$ terms?
- [ ] A) All single-bit errors
- [ ] B) All odd numbers of bit errors
- [ ] C) All burst errors of length $L \le r$
- [ ] D) All quadruple-bit errors
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
Non-zero $x^0$ terms detect single errors; factor $(x+1)$ detects all odd errors; degree $r$ detects all burst errors $\le r$. Quadruple errors (even) are not guaranteed.
</details>

#### Q33. [Company] Which of the following statements regarding the Internet Checksum are true?
- [ ] A) It uses 16-bit one's complement arithmetic
- [ ] B) Any carry out of bit 15 must be wrapped and added to the LSB (end-around carry)
- [ ] C) It detects all byte permutations and reorderings
- [ ] D) The receiver verifies error-free transmission if the sum equals `0xFFFF`
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, D**  
A, B, and D are standard properties (RFC 1071). C is false because addition is commutative.
</details>

#### Q34. [GATE-style] Which of the following statements about Hamming codes are correct?
- [ ] A) Parity bits are placed in positions that are powers of 2
- [ ] B) A Hamming code with $d_{\min} = 3$ can correct single-bit errors
- [ ] C) The syndrome value directly gives the index of the corrupted bit
- [ ] D) Hamming codes can correct arbitrary burst errors of length 16 without interleaving
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
A, B, and C are fundamental Hamming code mechanisms. D is false; standard Hamming codes only correct isolated single-bit errors.
</details>

#### Q35. [Concept] What advantages does 2-D Parity have over simple 1-D Parity?
- [ ] A) It can detect 2-bit errors
- [ ] B) It can locate and correct a single-bit error
- [ ] C) It has zero bit overhead
- [ ] D) It detects all burst errors of length less than or equal to column size
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, D**  
2D parity detects up to 3 errors, locates 1-bit errors, and handles burst errors up to column width. C is false because row and column parity bits add overhead.
</details>

#### Q36. [Company] Which of the following are valid reasons why Ethernet frame formats mandate a minimum payload size of 46 bytes (minimum frame size 64 bytes)?
- [ ] A) To ensure collision detection (CSMA/CD) works reliably over the maximum physical cable length
- [ ] B) To prevent transmission delay from being smaller than round-trip propagation time ($T_t \ge 2T_p$)
- [ ] C) To ensure CRC-32 polynomials have enough bits to divide
- [ ] D) To maintain physical line synchronization
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B**  
Under half-duplex CSMA/CD, the sender must continue transmitting long enough to detect a collision from the furthest cable end ($T_t \ge 2T_p$).
</details>

#### Q37. [GATE-style] In an HDLC bit-stuffed stream, what does the sequence `01111110` represent to the receiver?
- [ ] A) A stuffed user data sequence
- [ ] B) Frame boundary delimiter (FLAG)
- [ ] C) Idle link fill
- [ ] D) Hardware clock reset
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B, C**  
In HDLC, `01111110` acts as the start/end frame delimiter and is also transmitted continuously as idle line fill between frames.
</details>

#### Q38. [Concept] Which factors determine whether a network designer chooses FEC over ARQ?
- [ ] A) Round-trip propagation latency ($T_p$)
- [ ] B) Availability of a full-duplex reverse feedback channel
- [ ] C) Channel bit error rate
- [ ] D) Host operating system filesystem type
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
High latency (satellite) and simplex channels (broadcast) favor FEC. Low latency with feedback favors ARQ. Filesystem type is irrelevant.
</details>

#### Q39. [Company] What happens when an Ethernet switch port detects a frame with an invalid FCS (CRC) checksum?
- [ ] A) The switch drops the frame immediately
- [ ] B) The switch increments its port `FCS-Errors` counter
- [ ] C) The switch sends an ICMP error packet to the sender
- [ ] D) The switch broadcasts an ARP request
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B**  
Switches drop CRC-corrupted frames silently and increment error counters for diagnostic monitoring. L2 switches never generate L3 ICMP packets.
</details>

#### Q40. [GATE-style] Which of the following generator polynomials can detect all single-bit errors in a transmitted message?
- [ ] A) $G(x) = x^3 + x^2 + 1$
- [ ] B) $G(x) = x^4 + x + 1$
- [ ] C) $G(x) = x^2$
- [ ] D) $G(x) = x^16 + x^12 + x^5 + 1$
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, D**  
To detect single-bit errors, $G(x)$ must have at least two terms with non-zero $x^r$ and $x^0$. $G(x) = x^2$ has $x^0 = 0$ and fails.
</details>

---

## Part C: Numerical Answer Type (NAT) (41 to 50)

#### Q41. [GATE-style] In an HDLC frame, the transmitter transmits user data containing exactly 35 consecutive 1s. How many zero bits are stuffed into this sequence?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 7**  
A 0 is stuffed after every five 1s: $\lfloor 35 / 5 \rfloor = 7\text{ zero bits}$.
</details>

#### Q42. [GATE-style] A block code has a minimum Hamming distance $d_{\min} = 7$. What is the maximum number of bit errors it can guarantee to correct?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 3**  
$d_{\min} \ge 2t + 1 \implies 2t \le 7 - 1 = 6 \implies t = 3$.
</details>

#### Q43. [GATE-style] What is the minimum number of parity bits required in a Hamming code to protect a payload of $m = 8$ data bits against single-bit errors?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 4**  
$2^r \ge 8 + r + 1$. For $r=4$: $16 \ge 13$.
</details>

#### Q44. [GATE-style] The generator polynomial for CRC-8 is $G(x) = x^8 + x^2 + x + 1$. How many bits long is the Frame Check Sequence (FCS)?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 8**  
The degree of $G(x)$ is $r = 8$, so the FCS remainder is exactly 8 bits.
</details>

#### Q45. [GATE-style] A 16-bit Internet Checksum calculation produces a preliminary sum of `0x2453A` before folding carry bits. What is the value of the 16-bit sum after adding the carry bit? Express answer as hexadecimal without `0x` prefix (in uppercase).
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 453C**  
Carry is `0x2`. Adding carry to LSB: `0x453A + 0x2 = 0x453C`.
</details>

#### Q46. [GATE-style] What is the Hamming distance between the two codewords `1011010` and `1101100`?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 4**  
Bitwise XOR: `1011010` $\oplus$ `1101100` = `0110110`, which contains four 1s.
</details>

#### Q47. [GATE-style] In an even-parity Hamming(7,4) code, if data bits are $d_3=1, d_5=0, d_6=1, d_7=1$, what is the value of parity bit $p_2$?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 1**  
$p_2 = d_3 \oplus d_6 \oplus d_7 = 1 \oplus 1 \oplus 1 = 1$.
</details>

#### Q48. [GATE-style] What is the code rate (efficiency percentage) of a Hamming(7,4) code? Round to 1 decimal place.
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 57.1**  
$\text{Rate} = \frac{m}{n} = \frac{4}{7} \approx 57.14\%$.
</details>

#### Q49. [GATE-style] An engineer transmits 100 bytes of payload using byte stuffing. In the worst case where every payload byte is `FLAG`, how many total bytes are transmitted (including 2 framing flags)?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 202**  
Each `FLAG` byte becomes `ESC FLAG` (2 bytes): $100 \times 2 = 200\text{ bytes}$. Adding opening and closing flags: $200 + 2 = 202\text{ bytes}$.
</details>

#### Q50. [GATE-style] To simultaneously correct up to 1 bit error and detect up to 2 bit errors, what is the required minimum Hamming distance $d_{\min}$?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 4**  
Formula: $d_{\min} \ge t + d + 1 = 1 + 2 + 1 = 4$.
</details>

---

## Part D: Scenario-Based & Troubleshooting Case Studies (51 to 55)

#### Q51. [Scenario] A network administrator observes that a 1 Gbps fiber uplink between two switches is incrementing thousands of `FCS / CRC Errors` every minute. However, ping packets across the link report 0% packet loss. What is the most plausible explanation?
- A) The switches are using different framing flag delimiters
- B) Only large 1500-byte data frames encounter bit flips and are dropped by the switch; small 64-byte ICMP ping packets have a statistically higher chance of surviving corruption
- C) CRC checks only apply to UDP traffic, not ICMP
- D) The ping command automatically corrects corrupted CRC frames
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
On an optical link with marginal optical power (dirty fiber connector), bit error rate may be $\sim 10^{-6}$. A 1500-byte frame (12,000 bits) has a high probability of bit corruption and gets dropped, while a 64-byte ping packet (512 bits) frequently slips through uncorrupted.
</details>

#### Q52. [Scenario] A developer implementing an HDLC framing parser finds that the receiver frequently drops frames with "Premature End of Frame" errors. Wireshark analysis shows the sender transmits raw binary video data without bit stuffing. Why does this cause framing errors?
- A) Video data cannot be transmitted over serial lines
- B) Compressed video bitstreams frequently contain the pattern `01111110` by chance, which the receiver misinterprets as an end-of-frame FLAG
- C) HDLC only supports ASCII text
- D) Video data requires 2-D parity instead of CRC
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Without bit stuffing, random payload data that happens to match `01111110` will prematurely terminate the frame at the receiver, truncating payload.
</details>

#### Q53. [Scenario] A storage area network uses ECC memory with SECDED (Hamming code with overall parity). During an alpha radiation event, two memory bits flip in the same 64-bit word. What action does the memory controller take?
- A) It detects the double-bit error, declares an uncorrectable error, and triggers a system crash/alert rather than silently corrupting data
- B) It erroneously corrects a third bit
- C) It silently ignores the error
- D) It re-reads the word from the L1 cache
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
SECDED ($d_{\min} = 4$) can detect double-bit errors because the syndrome is non-zero while overall parity remains even. It alerts the system to avoid silent data corruption.
</details>

#### Q54. [Scenario] An engineer captures an Ethernet frame where the FCS field shows `0x00000000` inside Wireshark on the receiving server. Is this frame corrupted?
- A) Yes, `0x00000000` is an illegal FCS value
- B) No, standard Ethernet NICs perform hardware CRC offloading; the NIC validates the FCS in silicon, strips it, and the OS driver fills the Wireshark capture buffer with zeros
- C) Yes, the frame was corrupted by an intermediate router
- D) No, Ethernet has deprecated CRC in favor of TCP checksums
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Modern NICs verify and strip the 4-byte FCS in hardware ASIC. By the time packet capture drivers (libpcap/Npcap) inspect the frame, the FCS is absent or zeroed out.
</details>

#### Q55. [Scenario] During a lab experiment, two identical 16-bit words in a packet are swapped in position during transmission over an experimental link. The Internet Checksum at the receiver verifies the packet as valid. What does this demonstrate?
- A) The link layer corrected the order in hardware
- B) One's complement addition is commutative ($W_1 + W_2 = W_2 + W_1$), making checksums blind to byte reordering errors
- C) Checksums use polynomial division
- D) UDP automatically re-sequences words before checksum validation
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Because addition is commutative, swapping two words produces the exact same sum, demonstrating why link layers rely on CRC rather than simple checksums.
</details>

---

# Section 05b: Flow Control & ARQ

## Part A: Single-Choice Questions (1 to 30)

### Easy (Questions 1 to 10)

#### Q1. [Concept] What is the primary operational objective of Flow Control at the Data Link Layer?
- A) Preventing a fast transmitter from overflowing a slow receiver's local buffer
- B) Preventing physical cable signals from attenuating over distance
- C) Detecting and re-ordering packets that travel over multiple router hops
- D) Dynamically assigning IP addresses to newly attached local hosts
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Flow control specifically matches the sending rate to the receiving host's buffer capacity to prevent packet dropping due to receiver buffer overflow. See [notes_05b_flow_control.md#1-why-flow-control-exists](notes_05b_flow_control.md#1-why-flow-control-exists).
</details>

#### Q2. [Concept] In Stop-and-Wait ARQ, what action occurs when an acknowledgment (ACK) frame is lost in transit?
- A) The receiver sends a Negative Acknowledgment (NAK) requesting the frame again
- B) The sender's retransmission timer expires, the sender retransmits the frame, and the receiver discards the duplicate and re-sends the ACK
- C) The sender assumes the frame was safely delivered and advances to the next frame
- D) The entire physical link is reset by the Layer 2 hardware controller
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
When an ACK is lost, the sender times out and retransmits the data frame. The receiver uses the 1-bit sequence number to detect the duplicate, discards the payload, and retransmits the ACK. See [notes_05b_flow_control.md#23-the-three-failure-scenarios](notes_05b_flow_control.md#23-the-three-failure-scenarios).
</details>

#### Q3. [Formula] If $T_p$ is propagation delay and $T_t$ is transmission delay, what is the link efficiency $\eta$ of Stop-and-Wait ARQ under error-free conditions (neglecting processing and ACK transmission delays)?
- A) $\frac{T_p}{T_t}$
- B) $\frac{1}{1 + a}$
- C) $\frac{1}{1 + 2a}$ where $a = \frac{T_p}{T_t}$
- D) $\frac{2a}{1 + 2a}$
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
Cycle time is $T_t + 2T_p$. Efficiency $\eta = \frac{T_t}{T_t + 2T_p} = \frac{1}{1 + 2(T_p/T_t)} = \frac{1}{1 + 2a}$. See [notes_05b_flow_control.md#24-mathematical-analysis-of-stop-and-wait](notes_05b_flow_control.md#24-mathematical-analysis-of-stop-and-wait).
</details>

#### Q4. [GATE-style] In Go-Back-N ARQ, if a 3-bit sequence number field is used in the frame header, what is the maximum permissible sender window size $W_s$?
- A) 8
- B) 4
- C) 3
- D) 7
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
For $k$ sequence number bits, the sequence space is $2^k = 2^3 = 8$. To prevent overlapping window ambiguity, Go-Back-N requires $W_s \le 2^k - 1 = 8 - 1 = 7$. See [notes_05b_flow_control.md#41-architecture-and-operational-rules](notes_05b_flow_control.md#41-architecture-and-operational-rules).
</details>

#### Q5. [Concept] What type of acknowledgments are utilized in standard Go-Back-N ARQ?
- A) Cumulative acknowledgments where $ACK(n)$ confirms receipt of all frames prior to $n$
- B) Selective acknowledgments specifying each individual frame received
- C) Negative acknowledgments only; successful transmissions receive no confirmation
- D) Dual-tone multi-frequency signaling pulses
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Go-Back-N relies on cumulative acknowledgments. An arriving $ACK(n)$ implicitly confirms that all frames preceding $n$ have been accepted by the receiver. See [notes_05b_flow_control.md#41-architecture-and-operational-rules](notes_05b_flow_control.md#41-architecture-and-operational-rules).
</details>

#### Q6. [Architecture] What is the receiver window size $W_r$ in Go-Back-N ARQ?
- A) Equal to the sender window size $W_s$
- B) Strictly 1
- C) $2^{k-1}$
- D) Unlimited
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Go-Back-N uses a receiver window of size 1 ($W_r = 1$). It only accepts the next expected in-order frame and discards all out-of-order frames. See [notes_05b_flow_control.md#41-architecture-and-operational-rules](notes_05b_flow_control.md#41-architecture-and-operational-rules).
</details>

#### Q7. [Formula] In a sliding window protocol with sender window size $N$ and parameter $a = T_p / T_t$, what is the minimum window size $N$ required to achieve 100% channel utilization?
- A) $N = a$
- B) $N = 2a$
- C) $N \ge 1 + 2a$
- D) $N = 1 + a$
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
Link efficiency is $\eta = \min(1, \frac{N}{1 + 2a})$. To achieve $\eta = 1$ (100%), we must have $\frac{N}{1 + 2a} \ge 1 \implies N \ge 1 + 2a$. See [notes_05b_flow_control.md#32-sliding-window-efficiency-formula](notes_05b_flow_control.md#32-sliding-window-efficiency-formula).
</details>

#### Q8. [GATE-style] In Selective Repeat ARQ with a 4-bit sequence number field, what is the maximum allowable sender and receiver window size ($W_s = W_r$)?
- A) 16
- B) 15
- C) 7
- D) 8
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
In Selective Repeat, $W_s + W_r \le 2^k$. When $W_s = W_r$, $2 W_s \le 2^k \implies W_s \le 2^{k-1} = 2^{4-1} = 2^3 = 8$. See [notes_05b_flow_control.md#51-architecture-and-operational-rules](notes_05b_flow_control.md#51-architecture-and-operational-rules).
</details>

#### Q9. [Concept] Why does Selective Repeat ARQ strictly mandate that $W_s \le 2^{k-1}$?
- A) To prevent overlap between the current receive window and a retransmitted frame from the previous cycle
- B) Because hardware shift registers cannot count higher than half of their bit capacity
- C) To allow half the sequence numbers to be reserved for control packets
- D) To force the transmitter to pause halfway through the sequence
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
If $W_s > 2^{k-1}$, an old retransmitted frame can fall into the receiver's advanced receive window, causing the receiver to accept a duplicate frame as new data. See [notes_05b_flow_control.md#63-the-overlapping-window-proof-for-selective-repeat](notes_05b_flow_control.md#63-the-overlapping-window-proof-for-selective-repeat).
</details>

#### Q10. [Concept] What occurs in Selective Repeat ARQ when an out-of-order frame arrives that falls within the receiver's window?
- A) It is dropped immediately and a NAK is generated
- B) It is accepted, stored in the receiver's buffer, and acknowledged, but held until preceding missing frames arrive
- C) It is forwarded immediately to the Network Layer out of order
- D) The receiver crashes due to lack of sequential index pointers
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Unlike GBN, Selective Repeat buffers out-of-order frames that fall within its window and delivers them sequentially to the network layer once the missing gap is filled. See [notes_05b_flow_control.md#51-architecture-and-operational-rules](notes_05b_flow_control.md#51-architecture-and-operational-rules).
</details>

### Medium (Questions 11 to 20)

#### Q11. [Protocol] Which protocol feature combines an outgoing data payload with an acknowledgment for incoming traffic?
- A) Bit stuffing
- B) Cyclic Redundancy Check
- C) Piggybacking
- D) Pipelining
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
Piggybacking embeds an acknowledgment field inside the header of a reverse-direction data frame, eliminating the overhead of standalone ACK packets. See [notes_05b_flow_control.md#8-piggybacking](notes_05b_flow_control.md#8-piggybacking).
</details>

#### Q12. [Calculations] A physical link has transmission delay $T_t = 2.0\text{ ms}$ and one-way propagation delay $T_p = 18.0\text{ ms}$. What is the value of parameter $a$?
- A) 4.5
- B) 0.11
- C) 18.0
- D) 9.0
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
$a = \frac{T_p}{T_t} = \frac{18.0\text{ ms}}{2.0\text{ ms}} = 9.0$. See [numericals_05b_flow_control.md#problem-1-stop-and-wait-terrestrial-link-efficiency](numericals_05b_flow_control.md#problem-1-stop-and-wait-terrestrial-link-efficiency).
</details>

#### Q13. [GATE-style] On a satellite channel with $a = 15$, what is the link efficiency of Stop-and-Wait ARQ?
- A) $\approx 3.23\%$
- B) $\approx 6.25\%$
- C) $\approx 50.0\%$
- D) $\approx 15.0\%$
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
$\eta = \frac{1}{1 + 2a} = \frac{1}{1 + 2(15)} = \frac{1}{31} \approx 0.03226 = 3.23\%$. Stop-and-Wait is disastrously inefficient on high-latency links. See [notes_05b_flow_control.md#24-mathematical-analysis-of-stop-and-wait](notes_05b_flow_control.md#24-mathematical-analysis-of-stop-and-wait).
</details>

#### Q14. [Calculations] A 100 Mbps link has a round-trip time $RTT = 20\text{ ms}$. What is the Bandwidth-Delay Product (BDP) in bits?
- A) $200,000\text{ bits}$
- B) $2,000,000\text{ bits}$ (2 Mbits)
- C) $20,000,000\text{ bits}$
- D) $5,000,000\text{ bits}$
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
$\text{BDP} = B \times \text{RTT} = (100 \times 10^6\text{ bps}) \times (0.020\text{ s}) = 2 \times 10^6\text{ bits} = 2\text{ Mbits}$. See [notes_05b_flow_control.md#31-pipelining-and-the-bandwidth-delay-product-bdp](notes_05b_flow_control.md#31-pipelining-and-the-bandwidth-delay-product-bdp).
</details>

#### Q15. [Concept] If Frame 2 is lost during a Go-Back-N transmission with sender window size $N = 5$ (where frames 2, 3, 4, 5, 6 were sent), which frames will the sender retransmit upon timeout?
- A) Only Frame 2
- B) Frame 2 and Frame 3 only
- C) Frames 2, 3, 4, 5, and 6
- D) None; the receiver will request them via selective repeat
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
In GBN, the receiver discards all subsequent frames after a missing frame ($Wr=1$). When the sender timer expires for Frame 2, the sender must "go back" and retransmit Frame 2 and all subsequent frames in the window. See [notes_05b_flow_control.md#41-architecture-and-operational-rules](notes_05b_flow_control.md#41-architecture-and-operational-rules).
</details>

#### Q16. [GATE-style] If the frame error rate across a link is $P = 0.1$, what is the expected average number of transmissions required to successfully transfer one frame in Stop-and-Wait ARQ?
- A) 1.00
- B) 0.90
- C) 2.00
- D) $\approx 1.11$
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
The number of transmissions follows a geometric distribution with mean $\mathbb{E}[N_{tx}] = \frac{1}{1 - P} = \frac{1}{1 - 0.1} = \frac{1}{0.9} \approx 1.111$. See [notes_05b_flow_control.md#71-stop-and-wait-arq-under-loss](notes_05b_flow_control.md#71-stop-and-wait-arq-under-loss).
</details>

#### Q17. [Concept] Why do modern wired Ethernet networks (IEEE 802.3) omit sliding-window ARQ at Layer 2?
- A) Wired fiber and copper links have extremely low physical error rates ($< 10^{-12}$), making hop-by-hop ARQ overhead unnecessary compared to end-to-end TCP
- B) Ethernet hardware cannot support timers
- C) Sliding window algorithms are proprietary to IBM
- D) Ethernet frames do not contain preamble bits
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Because wired links are exceptionally reliable, wired Ethernet drops invalid FCS frames silently without Layer 2 ARQ retransmissions, leaving reliability to Layer 4 TCP. See [notes_05b_flow_control.md#10-exam-traps-vs-real-world-engineering](notes_05b_flow_control.md#10-exam-traps-vs-real-world-engineering).
</details>

#### Q18. [Calculations] For a link with parameter $a = 5.0$ and sender window size $N = 4$, what is the ideal sliding window link efficiency?
- A) $100\%$
- B) $\approx 36.36\%$
- C) $\approx 80.0\%$
- D) $\approx 9.09\%$
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
$\eta = \min(1, \frac{N}{1 + 2a}) = \frac{4}{1 + 2(5)} = \frac{4}{11} \approx 0.3636 = 36.36\%$. See [numericals_05b_flow_control.md#problem-7-sliding-window-performance-on-satellite-link](numericals_05b_flow_control.md#problem-7-sliding-window-performance-on-satellite-link).
</details>

#### Q19. [GATE-style] A sliding window protocol uses an $m$-bit sequence number. If the receiver window is configured to $W_r = 3$, what is the absolute maximum allowable sender window $W_s$?
- A) $2^m$
- B) $2^m - 1$
- C) $2^m - 3$
- D) $2^{m-1}$
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
The fundamental anti-overlap inequality is $W_s + W_r \le 2^m$. Given $W_r = 3$, we have $W_s \le 2^m - 3$. See [numericals_05b_flow_control.md#problem-14-overlapping-window-boundary-with-asymmetric-windows](numericals_05b_flow_control.md#problem-14-overlapping-window-boundary-with-asymmetric-windows).
</details>

#### Q20. [Concept] What is the operational purpose of a delayed ACK timer in a piggybacking protocol?
- A) To delay the sender from transmitting new data frames
- B) To throttle the transmission line clock frequency
- C) To discard noisy frames automatically
- D) To wait briefly for outbound data before falling back to transmitting an independent standalone ACK
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
If no reverse data is immediately ready, a delayed ACK timer waits a brief window (e.g., 50–200 ms). If outbound data appears, the ACK is piggybacked; if the timer expires, a standalone ACK is dispatched to prevent sender timeout. See [notes_05b_flow_control.md#8-piggybacking](notes_05b_flow_control.md#8-piggybacking).
</details>

### Hard / GATE-Level (Questions 21 to 30)

#### Q21. [Formula] In Go-Back-N ARQ with window size $N$ and frame error probability $P$, what is the formula for the average number of transmissions required per frame?
- A) $\frac{1 + (N - 1)P}{1 - P}$
- B) $\frac{1}{1 - P}$
- C) $1 + N \cdot P$
- D) $\frac{N(1 - P)}{1 + P}$
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
In GBN, each error forces the retransmission of $N$ frames. The expected number of transmissions is $1 + N \frac{P}{1 - P} = \frac{1 + (N - 1)P}{1 - P}$. See [notes_05b_flow_control.md#72-go-back-n-arq-under-loss](notes_05b_flow_control.md#72-go-back-n-arq-under-loss).
</details>

#### Q22. [GATE-style] What is the minimum number of sequence number bits $k$ required for a Go-Back-N protocol configured with a sender window of $W_s = 15$?
- A) 3 bits
- B) 4 bits
- C) 5 bits
- D) 16 bits
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
For GBN, $W_s \le 2^k - 1 \implies 15 \le 2^k - 1 \implies 2^k \ge 16 \implies k \ge 4\text{ bits}$. See [numericals_05b_flow_control.md#problem-3-sequence-number-bit-requirements](numericals_05b_flow_control.md#problem-3-sequence-number-bit-requirements).
</details>

#### Q23. [Concept] In Selective Repeat ARQ, how many timers does the sender maintain?
- A) Only one timer for the entire session
- B) Exactly two timers: one for data and one for ACKs
- C) One independent timer for each active, unacknowledged frame in the window
- D) None; timers are maintained exclusively at the receiver
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
Because each frame can be individually acknowledged or lost, the sender in Selective Repeat tracks an independent retransmission timer for every frame in flight. See [notes_05b_flow_control.md#51-architecture-and-operational-rules](notes_05b_flow_control.md#51-architecture-and-operational-rules).
</details>

#### Q24. [Calculations] A channel has bandwidth $B = 10\text{ Mbps}$, frame size $L = 1000\text{ bytes}$, and one-way propagation delay $T_p = 4.0\text{ ms}$. What is the optimal sliding window size $N$ needed to achieve 100% throughput?
- A) 5 frames
- B) 9 frames
- C) 10 frames
- D) 11 frames
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
$T_t = \frac{1000 \times 8}{10^7} = 0.8\text{ ms}$. $a = \frac{T_p}{T_t} = \frac{4.0}{0.8} = 5.0$. Optimal window $N = \lceil 1 + 2a \rceil = 1 + 2(5) = 11\text{ frames}$. See [notes_05b_flow_control.md#32-sliding-window-efficiency-formula](notes_05b_flow_control.md#32-sliding-window-efficiency-formula).
</details>

#### Q25. [Concept] In Stop-and-Wait ARQ, what happens if the sender's timeout duration is configured to be less than the round-trip propagation time ($2T_p$)?
- A) Spurious premature timeouts occur, flooding the link with redundant duplicate transmissions
- B) Link throughput increases towards 100%
- C) The receiver's buffer is prevented from overflowing
- D) The CRC polynomial is invalidated
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
If the timer expires before the legitimate ACK has physical time to return, the sender prematurely retransmits, wasting bandwidth on unnecessary duplicate frames. See [diagrams_05b_flow_control.md#4-stop-and-wait-arq-delayed-ack--premature-timeout](diagrams_05b_flow_control.md#4-stop-and-wait-arq-delayed-ack--premature-timeout).
</details>

#### Q26. [Calculations] What is the minimum number of sequence number bits $k$ needed for Selective Repeat with a sender window size of $W_s = 16$?
- A) 4 bits
- B) 5 bits
- C) 6 bits
- D) 32 bits
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
For SR, $W_s \le 2^{k-1} \implies 16 \le 2^{k-1} \implies 2^{k-1} \ge 16 = 2^4 \implies k - 1 \ge 4 \implies k \ge 5\text{ bits}$. (Or $W_s + W_r \le 2^k \implies 16 + 16 = 32 \le 2^k \implies k = 5$). See [numericals_05b_flow_control.md#problem-3-sequence-number-bit-requirements](numericals_05b_flow_control.md#problem-3-sequence-number-bit-requirements).
</details>

#### Q27. [Concept] Which specific problem does the sliding window protocol's sender window bound solve?
- A) Transmission channel cross-talk
- B) Electromagnetic interference in copper cables
- C) Transmitter buffer exhaustion and unconstrained frame emission that would overwhelm receiver memory
- D) Cryptographic certificate expiration
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
The sender window bounds the maximum number of unacknowledged frames in flight, bounding both sender buffer allocation and preventing receiver buffer overrun. See [notes_05b_flow_control.md#11-the-core-dilemma](notes_05b_flow_control.md#11-the-core-dilemma).
</details>

#### Q28. [GATE-style] In Go-Back-N with $k = 3$, the sender transmits frames 0, 1, 2, 3, 4, 5, 6. If Frame 3 is lost in transit, what acknowledgment does the receiver repeatedly send when frames 4, 5, and 6 arrive?
- A) $ACK(4), ACK(5), ACK(6)$
- B) $NAK(3)$
- C) None (silent drop)
- D) $ACK(3)$ (acknowledging all frames up to 2 and requesting frame 3)
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
Because $W_r = 1$, the receiver drops frames 4, 5, and 6, and repeats the acknowledgment for the last successfully received in-order frame, which is $ACK(3)$ (meaning "I am still waiting for Frame 3"). See [diagrams_05b_flow_control.md#6-go-back-n-gbn-arq-lost-frame--cascading-discard](diagrams_05b_flow_control.md#6-go-back-n-gbn-arq-lost-frame--cascading-discard).
</details>

#### Q29. [Calculations] A communication link with $T_t = 1.0\text{ ms}$ and $T_p = 2.0\text{ ms}$ utilizes Stop-and-Wait ARQ. What is the link efficiency?
- A) $20\%$
- B) $25\%$
- C) $50\%$
- D) $33.3\%$
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
$a = \frac{T_p}{T_t} = \frac{2.0}{1.0} = 2.0$. Efficiency $\eta = \frac{1}{1 + 2a} = \frac{1}{1 + 2(2)} = \frac{1}{5} = 0.20 = 20\%$. See [numericals_05b_flow_control.md#problem-1-stop-and-wait-terrestrial-link-efficiency](numericals_05b_flow_control.md#problem-1-stop-and-wait-terrestrial-link-efficiency).
</details>

#### Q30. [Concept] What is the primary operational trade-off of Selective Repeat ARQ compared to Go-Back-N ARQ?
- A) Selective Repeat has lower throughput on noisy channels
- B) Selective Repeat uses smaller sequence numbers
- C) Selective Repeat achieves higher link efficiency on lossy channels at the cost of receiver buffer memory and sorting logic complexity
- D) Selective Repeat eliminates the need for frame CRC check sequences
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
Selective Repeat avoids cascading retransmissions on error-prone channels by only retransmitting lost frames, but requires substantial receiver-side buffering, individual timers, and logic to reassemble out-of-order frames. See [notes_05b_flow_control.md#9-comprehensive-protocol-comparison-matrix](notes_05b_flow_control.md#9-comprehensive-protocol-comparison-matrix).
</details>

---

## Part B: Multiple Select Questions (MSQs) (31 to 40)

#### Q31. [MSQ] Which of the following statements about Stop-and-Wait ARQ are TRUE?
- A) Alternating 1-bit sequence numbers (0 and 1) are sufficient to prevent duplicate acceptance
- B) Channel efficiency increases as propagation delay increases
- C) Channel efficiency is given by $\frac{1}{1 + 2a}$ where $a = T_p / T_t$
- D) The receiver buffer only needs capacity to hold 1 frame
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, C, D**  
- A is TRUE: 1 bit (0 and 1) avoids duplication across lost frame/ACK cycles.
- B is FALSE: As $T_p$ increases, $a$ increases, causing efficiency $\eta = \frac{1}{1+2a}$ to *decrease*.
- C is TRUE: Standard efficiency formula.
- D is TRUE: Receiver window $W_r = 1$.
</details>

#### Q32. [MSQ] Which conditions will cause link utilization in a sliding window protocol to decrease?
- A) Increasing the transmission rate (bandwidth) while keeping frame size and distance constant
- B) Increasing the physical distance between sender and receiver
- C) Decreasing the sender window size $N$
- D) Increasing the frame size while keeping bandwidth constant
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
- A decreases $T_t$, increasing $a$, which lowers $\eta$ if $N$ is fixed.
- B increases $T_p$, increasing $a$, lowering $\eta$.
- C directly reduces $\eta = \min(1, \frac{N}{1+2a})$.
- D increases $T_t$, decreasing $a$, which *increases* efficiency.
</details>

#### Q33. [MSQ] Which properties are characteristic of Go-Back-N ARQ?
- A) Receiver window size $W_r = 1$
- B) Out-of-order undamaged frames arriving at the receiver are discarded
- C) Cumulative acknowledgments are supported
- D) Sender retransmits only the single corrupted frame upon timeout
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
- D is FALSE: GBN retransmits the *entire* pending window of $N$ frames, not just the single lost frame.
</details>

#### Q34. [MSQ] Which properties are characteristic of Selective Repeat ARQ?
- A) Receiver buffer capacity must be at least $W_r$ frames
- B) Out-of-order frames arriving within the receiver window are buffered
- C) For $k$-bit sequence numbers, $W_s \le 2^{k-1}$
- D) The sender retransmits all frames starting from the oldest unacknowledged frame on any timeout
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
- D describes Go-Back-N. In Selective Repeat, only the specific frame whose timer expired is retransmitted.
</details>

#### Q35. [MSQ] Which of the following expressions accurately represent the Bandwidth-Delay Product (BDP)?
- A) $\text{BDP} = B \times \text{RTT}$ in bits
- B) $\text{BDP} = 2a$ in units of frames
- C) $\text{BDP} = \frac{T_p}{T_t}$ in bits
- D) $\text{BDP} = B \times 2T_p$ in bits
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, D**  
BDP represents the capacity of the link pipe: $B \times \text{RTT} = B \times 2T_p$ bits, which equals $\frac{2T_p}{T_t} = 2a$ frames.
</details>

#### Q36. [MSQ] If the sliding window constraint $W_s + W_r \le 2^k$ is violated, which failure modes can occur?
- A) Undetected acceptance of duplicate data frames
- B) Inability of the receiver to distinguish between a retransmitted frame and a new frame from the next generation
- C) Frame Check Sequence calculation failure
- D) Silent data corruption delivered to the higher network layer
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, D**  
Violating $W_s + W_r \le 2^k$ causes window overlap ambiguity. CRC/FCS is unrelated to sliding window state (C is false).
</details>

#### Q37. [MSQ] Which statements regarding cumulative acknowledgments are TRUE?
- A) A single lost ACK does not necessarily trigger a retransmission if a later ACK arrives in time
- B) An ACK containing sequence number $n$ confirms that all frames up to $n-1$ have been received
- C) Cumulative ACKs require individual timers for every frame in flight
- D) Go-Back-N commonly uses cumulative ACKs
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, D**  
- C is FALSE: Cumulative ACKs allow the sender to maintain just a single timer for the oldest unacknowledged frame.
</details>

#### Q38. [MSQ] In a bidirectional piggybacking protocol, which mechanisms prevent protocol deadlocks?
- A) A delayed ACK timer that forces dispatch of a standalone ACK if no return data is generated
- B) Independent transmission line grounding
- C) Retransmission timers running on unacknowledged transmitted data
- D) Hardware CRC registers
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, C**  
Delayed ACK timers ensure ACKs are not held indefinitely if reverse data is absent, and sender retransmission timers guarantee recovery if an embedded ACK is lost.
</details>

#### Q39. [MSQ] When deciding between Go-Back-N and Selective Repeat for an embedded system, which factors favor Go-Back-N?
- A) Severe receiver memory limitations (e.g., microcontrollers with tiny RAM)
- B) Highly reliable physical links with negligible packet error rates
- C) Noisy satellite links with high error probability and high latency
- D) Simplicity of receiver firmware logic (no sorting or buffer tracking required)
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, D**  
On noisy links with high latency (C), Go-Back-N suffers disastrous throughput collapse; Selective Repeat is strongly preferred there.
</details>

#### Q40. [MSQ] In modern computer networking architectures, which layers or protocols actively employ sliding-window flow control?
- A) Layer 4 TCP (Transmission Control Protocol)
- B) Layer 2 HDLC (High-Level Data Link Control)
- C) Layer 2 Ethernet full-duplex pause frames (IEEE 802.3x)
- D) Layer 3 IPv4
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
TCP uses sliding-window flow control (`rcv_wnd`), HDLC supports sliding-window ARQ, and IEEE 802.3x provides link-layer flow control via Pause frames. IPv4 is a connectionless datagram protocol without flow control.
</details>

---

## Part C: Numerical Answer Type (NAT) Questions (41 to 50)

#### Q41. [NAT] A point-to-point link has bandwidth $B = 2\text{ Mbps}$, distance $d = 2000\text{ km}$, propagation speed $v = 2 \times 10^8\text{ m/s}$, and frame size $L = 1000\text{ bytes}$. Calculate the parameter $a = T_p / T_t$. *(Give your answer to 2 decimal places).*
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 2.50**  
- $T_t = \frac{1000 \times 8}{2 \times 10^6} = 0.004\text{ s} = 4.0\text{ ms}$
- $T_p = \frac{2 \times 10^6\text{ m}}{2 \times 10^8\text{ m/s}} = 0.010\text{ s} = 10.0\text{ ms}$
- $a = \frac{10.0}{4.0} = 2.50$
</details>

#### Q42. [NAT] A satellite link with parameter $a = 15$ operates using Stop-and-Wait ARQ. Calculate the percentage channel efficiency $\eta$. *(Give your answer rounded to 2 decimal places, e.g., 3.23).*
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 3.23**  
$\eta = \frac{1}{1 + 2(15)} = \frac{1}{31} \approx 0.03226 = 3.23\%$.
</details>

#### Q43. [NAT] A sliding window protocol uses a 5-bit sequence number field. What is the maximum allowable sender window size $W_s$ in Go-Back-N ARQ?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 31**  
$W_s \le 2^k - 1 = 2^5 - 1 = 32 - 1 = 31$.
</details>

#### Q44. [NAT] A sliding window protocol uses a 5-bit sequence number field. What is the maximum allowable sender window size $W_s$ in Selective Repeat ARQ when $W_s = W_r$?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 16**  
$W_s \le 2^{k-1} = 2^{5-1} = 2^4 = 16$.
</details>

#### Q45. [NAT] A 100 Mbps fiber link has a one-way propagation delay $T_p = 10\text{ ms}$. If frames are $1250\text{ bytes}$ in length, calculate the Bandwidth-Delay Product (BDP) expressed as the number of frames.
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 200**  
- $\text{BDP (bits)} = B \times 2T_p = 10^8 \times 0.020 = 2,000,000\text{ bits}$
- Frame size in bits $L = 1250 \times 8 = 10,000\text{ bits}$
- $\text{BDP (frames)} = \frac{2,000,000}{10,000} = 200\text{ frames}$
</details>

#### Q46. [NAT] In a sliding window system, $T_t = 1.0\text{ ms}$ and $T_p = 12.0\text{ ms}$. What is the minimum sender window size $N$ needed to achieve $100\%$ channel utilization?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 25**  
$a = \frac{12.0}{1.0} = 12.0$. Optimal window $N = \lceil 1 + 2a \rceil = 1 + 2(12) = 25$.
</details>

#### Q47. [NAT] In Stop-and-Wait ARQ, transmission delay is $T_t = 4.0\text{ ms}$ and one-way propagation delay is $T_p = 6.0\text{ ms}$. If the link bandwidth is $10\text{ Mbps}$, what is the effective throughput in Mbps?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 2.5**  
- Total cycle time $= T_t + 2T_p = 4.0 + 2(6.0) = 16.0\text{ ms}$
- Efficiency $\eta = \frac{4.0}{16.0} = 0.25 = 25\%$
- Throughput $= 0.25 \times 10\text{ Mbps} = 2.5\text{ Mbps}$
</details>

#### Q48. [NAT] An engineer wants to design a Go-Back-N link with a sender window size of $W_s = 63$. What is the minimum number of sequence number bits $k$ that must be allocated in the header?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 6**  
$2^k \ge W_s + 1 = 63 + 1 = 64 \implies k = \log_2(64) = 6\text{ bits}$.
</details>

#### Q49. [NAT] In Selective Repeat ARQ, the independent frame error rate is $P = 0.20$. What is the average number of transmissions required to successfully transfer one frame?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 1.25**  
$\mathbb{E}[N_{tx}] = \frac{1}{1 - P} = \frac{1}{1 - 0.20} = \frac{1}{0.80} = 1.25$.
</details>

#### Q50. [NAT] A link has transmission delay $T_t = 0.5\text{ ms}$ and one-way propagation delay $T_p = 4.75\text{ ms}$. If the sender window size is $N = 5$, what is the percentage link efficiency $\eta$?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 25.0**  
- $a = \frac{4.75}{0.5} = 9.5$
- $\eta = \frac{N}{1 + 2a} = \frac{5}{1 + 2(9.5)} = \frac{5}{1 + 19} = \frac{5}{20} = 0.25 = 25.0\%$
</details>

---

## Part D: Real-World Scenario & Troubleshooting Challenges (51 to 55)

#### Q51. [Scenario] A network administrator deploys a 100 Mbps point-to-point satellite connection with an RTT of 500 ms. File transfers over TCP only reach ~1.0 Mbps. Packet captures show TCP window sizes are capped at 64 KB because TCP Window Scaling (RFC 1323) is disabled on the legacy client. How does this bottleneck relate to sliding window mechanics?
- A) The link speed is throttled by satellite solar flare activity
- B) The Bandwidth-Delay Product is $100\text{ Mbps} \times 0.5\text{ s} = 50\text{ Mbits} = 6.25\text{ MB}$. A 64 KB window can only achieve throughput of $\frac{64\text{ KB}}{0.5\text{ s}} \approx 1.05\text{ Mbps}$
- C) Stop-and-Wait is being enforced by the Layer 2 satellite modem
- D) The client is experiencing CRC checksum collisions
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
To fill a link pipe, the sliding window must equal or exceed the BDP. Without window scaling, TCP's window is capped at $65,535\text{ bytes}$, which caps maximum throughput to $\frac{64\text{ KB}}{0.5\text{ s}} \approx 1.024\text{ Mbps}$ regardless of link bandwidth.
</details>

#### Q52. [Scenario] An embedded sensor transmits readings to a base station using Stop-and-Wait ARQ over an industrial 868 MHz wireless link. The base station periodically receives duplicate sensor readings. Investigation reveals that the base station's CPU load spikes during database writes, causing it to take 120 ms to process and return ACKs, while the sensor's retransmission timeout is fixed at 100 ms. What is the corrective action?
- A) Invert the polynomial generator at the sensor
- B) Increase the sensor's retransmission timer to exceed $T_t + 2T_p + T_{\text{proc, max}}$ (e.g., 200 ms)
- C) Reduce the sensor's frame size by half
- D) Switch the sensor to pure simplex mode
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Setting timeout < RTT + processing delay causes spurious premature timeouts. The sender retransmits before the valid ACK arrives, causing the receiver to receive duplicates. Increasing timeout resolves the issue.
</details>

#### Q53. [Scenario] An automated factory floor uses Go-Back-N ARQ across an RS-485 serial bus ($N = 8$). Whenever an electric motor starts up, electromagnetic interference causes a brief 2% packet error rate. During these periods, bus throughput drops by almost 30%. Why would converting to Selective Repeat ARQ stabilize throughput?
- A) Selective Repeat uses smaller CRC fields
- B) In Go-Back-N, every single dropped frame triggers retransmission of all 8 frames in the window; Selective Repeat retransmits only the single corrupted frame, eliminating the $N$-frame retransmission storm
- C) Selective Repeat eliminates propagation delay across copper cables
- D) Selective Repeat suppresses electrical interference at the PHY layer
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
In GBN, each error forces retransmitting $N$ frames ($\mathbb{E}[N_{tx}] = \frac{1 + (N-1)P}{1-P}$), causing severe channel starvation. Selective Repeat retransmits only the failed frame ($\mathbb{E}[N_{tx}] = \frac{1}{1-P}$), maintaining high efficiency.
</details>

#### Q54. [Scenario] Two routers A and B run a proprietary protocol that uses bidirectional piggybacking. Router A is transmitting a continuous high-volume file transfer to Router B, while Router B has no user data to return to Router A. Router A's transfer rate suddenly drops to near zero and retransmits frequently. What bug exists in Router B's implementation?
- A) Router B lacks a delayed ACK fallback timer, so it holds acknowledgments indefinitely waiting for outbound data that never arrives
- B) Router B's receive buffer has negative capacity
- C) Router A is sending too many bits per second for copper wire
- D) Router B has inverted the sequence numbers
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Piggybacking systems must implement a delayed ACK timer (typically 50–200 ms). If no outbound data arrives before timer expiry, a standalone ACK must be sent; otherwise, sender timers expire and transmission stalls completely.
</details>

#### Q55. [Scenario] A developer implements a custom sliding window data link protocol with a 4-bit sequence number ($k = 4 \implies M = 16$). Seeking maximum performance, the developer configures $W_s = 10$ and $W_r = 10$. On a lossless testbed, tests pass with 100% throughput. But when deployed across a WAN link with random packet loss, the destination file becomes silently corrupted with duplicate blocks. What caused this defect?
- A) 4-bit sequence numbers are not supported by operating system sockets
- B) $W_s + W_r = 10 + 10 = 20 > 2^4 = 16$, violating the anti-overlap condition and causing retransmitted frames to fall inside the receiver's advanced window
- C) The WAN router corrupted the TCP checksum
- D) Stop-and-Wait was improperly initialized
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
The fundamental condition for correct sliding window operation is $W_s + W_r \le 2^k$. With $k=4$, $2^k=16$. Having $W_s + W_r = 20 > 16$ creates window overlap: when all ACKs are lost, retransmitted frames from the old generation fall within the advanced receive window and are accepted as new data.
</details>

---

## ⬅️ Navigation
- **Module Index:** [INDEX.md](../INDEX.md)
- **Previous Sub-step:** [05a: Framing & Error Control](notes.md)
- **Current Sub-step:** [05b: Flow Control & ARQ Notes](notes_05b_flow_control.md) | [Numericals](numericals_05b_flow_control.md) | [Diagrams](diagrams_05b_flow_control.md)
- **Next Sub-step:** [05c: MAC Protocols & Ethernet 802.3](../05_Data_Link_Layer/)

