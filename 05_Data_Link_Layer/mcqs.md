# 05. Data Link Layer (Part A) — Practice Question Bank

> **55 Rigorous Practice Questions covering Framing, Bit/Byte Stuffing, Parity, Checksums, CRC, and Hamming Codes.**  
> - **Part A:** 30 Single-Choice MCQs (Strictly balanced answer distribution: ~25% per option)  
> - **Part B:** 10 Multiple Select Questions (MSQs)  
> - **Part C:** 10 Numerical Answer Type (NAT) Questions  
> - **Part D:** 5 Real-World Scenario & Troubleshooting Challenges  

---

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

## ⬅️ Navigation
- **Module Overview:** [README.md](README.md)
- **Deep-Dive Notes:** [notes.md](notes.md)
- **Solved Numericals:** [numericals.md](numericals.md)
- **Visual Diagrams:** [diagrams.md](diagrams.md)
- **Interview Q&A:** [interview_qa.md](interview_qa.md)
- **One-Page Cheatsheet:** [cheatsheet.md](cheatsheet.md)
- **Next Sub-step:** [05b Flow Control & ARQ](../05_Data_Link_Layer/)
