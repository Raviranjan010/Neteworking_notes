# 05. Data Link Layer (Part A) — Solved Numerical Problems

> **Rigorous step-by-step mathematical calculations for framing, bit stuffing, CRC, Checksums, and Hamming codes, verified programmatically with Python.**

---

## 📐 Master Formula Index

| Concept / Formula | Mathematical Equation | Variables & Definitions | When to Use |
|---|---|---|---|
| **Hamming Inequality** | $$2^r \ge m + r + 1$$ | $m$: data bits, $r$: redundant parity bits | Calculating minimum parity bits for single-bit error correction |
| **Error Detection Distance** | $$d_{\min} \ge d + 1$$ | $d$: number of simultaneous bit errors to detect | Designing block codes with guaranteed error detection |
| **Error Correction Distance** | $$d_{\min} \ge 2t + 1$$ | $t$: number of simultaneous bit errors to correct | Designing forward error correction (FEC) codes |
| **CRC FCS Length** | $$L_{\text{FCS}} = \deg(G(x)) = r$$ | $r$: degree of generator polynomial | Determining number of zero bits to append before division |
| **CRC Burst Error Guarantee**| $$L_{\text{burst}} \le r \implies 100\%$$ | $L_{\text{burst}}$: span between first and last error bits | Evaluating hardware CRC reliability against impulse noise |

---

## Level 1: Core Fundamentals

### Problem 1.1: HDLC Bit Stuffing
**Question:**  
A transmitter using HDLC framing must transmit the following 27-bit payload:  
`011111101111100111111111110`  
Determine the stuffed bitstream, the total number of stuffed zero bits, and the overhead percentage.

<details><summary><b>Step-by-Step Solution</b></summary>

**Given:**
- Raw data stream: `011111101111100111111111110` (27 bits)
- HDLC stuffing rule: Insert a `'0'` immediately after five consecutive `'1'`s.

**Step-by-Step Execution:**
1. Bits 1–6: `011111` $\rightarrow$ Five 1s reached! Insert `0`: `011111`**0**`10...`
2. Bits 7–12: Next sequence has `11111` $\rightarrow$ Five 1s reached! Insert `0`: `...11111`**0**`00...`
3. Bits 13–18: Next sequence has `11111` $\rightarrow$ Five 1s reached! Insert `0`: `...11111`**0**`...`
4. Bits 19–24: Next five bits are `11111` $\rightarrow$ Insert `0`: `...11111`**0**`10`

**Resulting Stuffed Stream:**  
`011111`**0**`1011111`**0**`0011111`**0**`11111`**0**`10`

**Calculations:**
- Stuffed zero count = $4\text{ bits}$
- Total transmitted bits = $27 + 4 = 31\text{ bits}$
- Overhead = $\frac{4}{27} \times 100\% = \mathbf{14.81\%}$

**Final Answer:**  
$$\text{Stuffed stream: }\mathbf{0111110101111100011111011111010} \quad (4\text{ stuffed zeros, } 31\text{ bits total})$$
</details>

---

### Problem 1.2: Minimum Hamming Distance for Error Detection
**Question:**  
A communication engineer must design a linear block code that guarantees the detection of any 2-bit error occurring on a noisy channel. What is the minimum Hamming distance required between any pair of valid codewords?

<details><summary><b>Step-by-Step Solution</b></summary>

**Given:**
- Number of detectable errors $d = 2$

**Formula:**
$$d_{\min} \ge d + 1$$

**Calculation:**
$$d_{\min} \ge 2 + 1 = 3$$

**Trap Note:**  
If the question asked to *correct* 2-bit errors, the formula would be $d_{\min} \ge 2(2) + 1 = 5$. For *detection*, $d_{\min} = 3$ is sufficient.

**Final Answer:**  
$$d_{\min} = \mathbf{3}$$
</details>

---

### Problem 1.3: Number of Redundant Bits in Hamming Code
**Question:**  
Find the minimum number of parity bits $r$ required to construct a single-error-correcting Hamming code for:
1. $m = 4$ data bits
2. $m = 8$ data bits
3. $m = 16$ data bits

<details><summary><b>Step-by-Step Solution</b></summary>

**Formula:**
$$2^r \ge m + r + 1$$

**Evaluation:**
1. For $m = 4$:
   - Try $r = 2$: $2^2 = 4 \not\ge 4 + 2 + 1 = 7$ (False)
   - Try $r = 3$: $2^3 = 8 \ge 4 + 3 + 1 = 8$ (**True** $\implies r = 3$)
2. For $m = 8$:
   - Try $r = 3$: $2^3 = 8 \not\ge 8 + 3 + 1 = 12$ (False)
   - Try $r = 4$: $2^4 = 16 \ge 8 + 4 + 1 = 13$ (**True** $\implies r = 4$)
3. For $m = 16$:
   - Try $r = 4$: $2^4 = 16 \not\ge 16 + 4 + 1 = 21$ (False)
   - Try $r = 5$: $2^5 = 32 \ge 16 + 5 + 1 = 22$ (**True** $\implies r = 5$)

**Final Answer:**  
- $m = 4 \implies r = \mathbf{3}\text{ bits}$ (Codeword = 7 bits)
- $m = 8 \implies r = \mathbf{4}\text{ bits}$ (Codeword = 12 bits)
- $m = 16 \implies r = \mathbf{5}\text{ bits}$ (Codeword = 21 bits)
</details>

---

## Level 2: Standard Exam & University Problems

### Problem 2.1: CRC Modulo-2 Polynomial Long Division
**Question:**  
Calculate the transmitted Cyclic Redundancy Check (CRC) codeword for data bit sequence $D = \mathbf{100100}$ using the generator polynomial $G(x) = x^3 + x^2 + 1$.

<details><summary><b>Step-by-Step Solution</b></summary>

**Given:**
- Data $D = 100100$ ($k = 6$ bits)
- Generator $G(x) = x^3 + x^2 + 0x + 1 \implies G = \mathbf{1101}$ ($r = 3$ bits)

**Step 1: Augment Data**  
Append $r = 3$ zeros to the data:
$$\text{Augmented Data} = 100100000$$

**Step 2: Modulo-2 Binary Division (XOR Division)**  
```
          111101
1101 | 100100000
       1101
       ----
        1000
        1101
        ----
         1010
         1101
         ----
          1110
          1101
          ----
           0110
           0000
           ----
            1100
            1101
            ----
            0001  <-- Remainder (FCS = 001)
```

**Step 3: Construct Codeword**  
$$\text{Codeword} = \text{Data} \mid \text{Remainder} = 100100 \mid 001 = \mathbf{100100001}$$

**Final Answer:**  
$$\text{FCS Remainder} = \mathbf{001}, \quad \text{Transmitted Codeword} = \mathbf{100100001}$$
</details>

---

### Problem 2.2: Internet 16-Bit Checksum Calculation
**Question:**  
Compute the 16-bit Internet Checksum (RFC 1071) for two consecutive 16-bit hexadecimal words:  
$W_1 = \mathbf{0x4500}, \quad W_2 = \mathbf{0x003C}$.  
Demonstrate receiver verification.

<details><summary><b>Step-by-Step Solution</b></summary>

**Given:**
- Word 1: `0x4500` ($0100\text{ }0101\text{ }0000\text{ }0000_2$)
- Word 2: `0x003C` ($0000\text{ }0000\text{ }0011\text{ }1100_2$)

**Sender Calculation:**
1. Sum the 16-bit words:
   $$0x4500 + 0x003C = \mathbf{0x453C}$$
   *(No carry out of bit 15 occurred).*
2. Take the 1's complement (bitwise NOT):
   $$\sim(0x453C) = \mathbf{0xBAC3}$$

**Receiver Verification:**
Add $W_1 + W_2 + \text{Checksum}$:
$$0x4500 + 0x003C + 0xBAC3 = 0x453C + 0xBAC3 = \mathbf{0xFFFF}$$
Taking 1's complement of `0xFFFF` yields `0x0000`, confirming no errors.

**Final Answer:**  
$$\text{Checksum} = \mathbf{0xBAC3} \quad (\text{Receiver sum} = \mathbf{0xFFFF})$$
</details>

---

### Problem 2.3: Byte Stuffing Overhead
**Question:**  
An application layer delivers a 5-byte payload:  
`['A', 'FLAG', 'B', 'ESC', 'C']`  
Compute the resulting frame after byte stuffing (where each frame begins and ends with `FLAG`, and literal occurrences of `FLAG` or `ESC` in the payload are escaped with `ESC`).

<details><summary><b>Step-by-Step Solution</b></summary>

**Given:**
- Payload: `A`, `FLAG`, `B`, `ESC`, `C` (5 bytes)
- Framing markers: Leading `FLAG`, Trailing `FLAG`

**Step-by-Step Stuffing:**
1. Open frame: `FLAG`
2. Byte 1 (`A`): Unchanged $\rightarrow$ `A`
3. Byte 2 (`FLAG`): Matches delimiter $\rightarrow$ Insert `ESC` before it $\rightarrow$ `ESC`, `FLAG`
4. Byte 3 (`B`): Unchanged $\rightarrow$ `B`
5. Byte 4 (`ESC`): Matches escape $\rightarrow$ Insert `ESC` before it $\rightarrow$ `ESC`, `ESC`
6. Byte 5 (`C`): Unchanged $\rightarrow$ `C`
7. Close frame: `FLAG`

**Stuffed Frame:**  
`[FLAG, A, ESC, FLAG, B, ESC, ESC, C, FLAG]`

**Final Answer:**  
$$\text{Stuffed Frame Length} = \mathbf{9\text{ Bytes}} \quad (\text{Added } 2\text{ escape bytes } + 2\text{ delimiter bytes})$$
</details>

---

## Level 3: Advanced GATE & Competitive Challenges

### Problem 3.1: GATE CRC Polynomial Division
**Question:**  
A bitstream `1101011011` is transmitted using the standard generator polynomial $G(x) = x^4 + x + 1$.  
Find the resulting Frame Check Sequence (FCS) remainder and the complete transmitted codeword.

<details><summary><b>Step-by-Step Solution</b></summary>

**Given:**
- Data $D = 1101011011$ (10 bits)
- $G(x) = x^4 + 0x^3 + 0x^2 + x^1 + 1 \implies G = \mathbf{10011}$ ($r = 4$ bits)

**Step 1: Augment Data**  
Append $r = 4$ zeros:
$$\text{Augmented Data} = 11010110110000$$

**Step 2: Modulo-2 Division**  
```
            1100001010
10011 | 11010110110000
        10011
        -----
         10011
         10011
         -----
          000010110
              10011
              -----
               010100
                10011
                -----
                001110  <-- Remainder (4 bits = 1110)
```

**Step 3: Assemble Codeword**  
Codeword = $\text{Data} \mid \text{Remainder} = \mathbf{11010110111110}$

**Final Answer:**  
$$\text{FCS Remainder} = \mathbf{1110}, \quad \text{Codeword} = \mathbf{11010110111110}$$
</details>

---

### Problem 3.2: Hamming(7,4) Single-Bit Error Syndrome Correction
**Question:**  
Using even parity Hamming(7,4) code with bit positions 1 to 7:
1. Encode data bits $D = \mathbf{1011}$ (where $d_3=1, d_5=0, d_6=1, d_7=1$).
2. Suppose transmission noise corrupts bit position 5 ($d_5$). Show how the receiver calculates the syndrome vector to detect and correct the erroneous bit.

<details><summary><b>Step-by-Step Solution</b></summary>

**Part 1: Sender Encoding**  
Codeword positions: $[p_1, p_2, d_3, p_4, d_5, d_6, d_7]$
- $p_1$ checks positions $\{1, 3, 5, 7\} \implies p_1 = d_3 \oplus d_5 \oplus d_7 = 1 \oplus 0 \oplus 1 = \mathbf{0}$
- $p_2$ checks positions $\{2, 3, 6, 7\} \implies p_2 = d_3 \oplus d_6 \oplus d_7 = 1 \oplus 1 \oplus 1 = \mathbf{1}$
- $p_4$ checks positions $\{4, 5, 6, 7\} \implies p_4 = d_5 \oplus d_6 \oplus d_7 = 0 \oplus 1 \oplus 1 = \mathbf{0}$

$$\text{Codeword} = [p_1=0, p_2=1, d_3=1, p_4=0, d_5=0, d_6=1, d_7=1] = \mathbf{0110011}$$

**Part 2: Noise Injection at Position 5**  
Bit 5 flips from $0 \rightarrow 1$:
$$\text{Received Codeword } R = \mathbf{0110111}$$

**Part 3: Syndrome Calculation at Receiver**  
- $s_1 = r_1 \oplus r_3 \oplus r_5 \oplus r_7 = 0 \oplus 1 \oplus 1 \oplus 1 = \mathbf{1}$
- $s_2 = r_2 \oplus r_3 \oplus r_6 \oplus r_7 = 1 \oplus 1 \oplus 1 \oplus 1 = \mathbf{0}$
- $s_4 = r_4 \oplus r_5 \oplus r_6 \oplus r_7 = 0 \oplus 1 \oplus 1 \oplus 1 = \mathbf{1}$

$$\text{Syndrome } S = (s_4 s_2 s_1)_2 = (101)_2 = \mathbf{5}$$

**Correction:**  
Syndrome equals $5$, directly pointing to bit position 5. Invert bit 5:
$$0110\mathbf{1}11 \longrightarrow \mathbf{0110011} \quad (\text{Corrected back to original!})$$

**Final Answer:**  
$$\text{Codeword: }\mathbf{0110011}, \quad \text{Syndrome: }\mathbf{5} \implies \text{Bit 5 corrected}$$
</details>

---

## 🐍 Python Verification Script

All calculations above are verified by the companion verification script:

```bash
python tools/verify/verify_datalink.py
```

---

## ⬅️ Navigation
- **Module Overview:** [README.md](README.md)
- **Deep-Dive Notes:** [notes.md](notes.md)
- **Visual Diagrams:** [diagrams.md](diagrams.md)
- **Practice Questions:** [mcqs.md](mcqs.md)
- **Interview Q&A:** [interview_qa.md](interview_qa.md)
- **Cheatsheet:** [cheatsheet.md](cheatsheet.md)
- **Next Sub-step:** [05b Flow Control & ARQ](../05_Data_Link_Layer/)
