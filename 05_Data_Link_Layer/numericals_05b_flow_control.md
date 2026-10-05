# 05b. Flow Control & ARQ — Solved Numerical Problems

> **15 Rigorous, Step-by-Step Solved Numerical Problems across 3 Difficulty Levels (Basic, Standard, GATE-Hard) with complete dimensional analysis and verified calculations.**

---

## 📌 Standard Reference Formulas & Units

$$\text{Transmission Delay: } T_t = \frac{\text{Frame Size } L \text{ (bits)}}{\text{Bandwidth } B \text{ (bps)}} \quad [\text{seconds or ms}]$$
$$\text{Propagation Delay: } T_p = \frac{\text{Distance } d \text{ (m)}}{\text{Propagation Speed } v \text{ (m/s)}} \quad [\text{seconds or ms}]$$
$$\text{Ratio parameter: } a = \frac{T_p}{T_t}$$
$$\text{Stop-and-Wait Efficiency: } \eta_{\text{SW}} = \frac{T_t}{T_t + 2T_p + T_{\text{ack}} + T_{\text{proc}}} \approx \frac{1}{1 + 2a}$$
$$\text{Sliding Window Efficiency: } \eta_{\text{SWP}} = \min\left(1, \frac{N \cdot T_t}{T_t + 2T_p}\right) = \min\left(1, \frac{N}{1 + 2a}\right)$$
$$\text{Optimal Window for 100\% Utilization: } N_{\text{opt}} = \lceil 1 + 2a \rceil$$
$$\text{Bandwidth-Delay Product (BDP): } BDP = B \times 2T_p \text{ bits} = 2a \text{ frames}$$
$$\text{Sequence Numbers Bound: } W_s + W_r \le 2^k$$
$$\text{GBN: } W_s \le 2^k - 1, \; W_r = 1 \implies k \ge \lceil \log_2(W_s + 1) \rceil$$
$$\text{SR: } W_s \le 2^{k-1}, \; W_r \le 2^{k-1} \implies k \ge \lceil \log_2(2W_s) \rceil$$

---

## Level 1: Basic Concept Verification (Problems 1 to 5)

### Problem 1: Stop-and-Wait Terrestrial Link Efficiency
A 1000-km point-to-point link operates at a bandwidth of $1\text{ Mbps}$. Signal propagation speed is $2 \times 10^8\text{ m/s}$. The frame size is $1000\text{ bytes}$. Assuming acknowledgment transmission time and processing delays are negligible:
1. Calculate the transmission delay $T_t$ and propagation delay $T_p$.
2. Calculate parameter $a$.
3. Calculate the link efficiency $\eta$ and effective throughput.

#### Solution:
- **Given:**
  - $L = 1000\text{ Bytes} = 1000 \times 8 = 8000\text{ bits}$
  - $B = 1\text{ Mbps} = 10^6\text{ bps}$
  - $d = 1000\text{ km} = 10^6\text{ meters}$
  - $v = 2 \times 10^8\text{ m/s}$
- **Step 1: Delays:**
  $$T_t = \frac{8000\text{ bits}}{10^6\text{ bps}} = 8 \times 10^{-3}\text{ s} = 8.00\text{ ms}$$
  $$T_p = \frac{10^6\text{ m}}{2 \times 10^8\text{ m/s}} = 5 \times 10^{-3}\text{ s} = 5.00\text{ ms}$$
- **Step 2: Parameter $a$:**
  $$a = \frac{T_p}{T_t} = \frac{5.00\text{ ms}}{8.00\text{ ms}} = 0.625$$
- **Step 3: Efficiency and Throughput:**
  $$\eta = \frac{1}{1 + 2a} = \frac{1}{1 + 2(0.625)} = \frac{1}{1 + 1.25} = \frac{1}{2.25} \approx 0.4444 = 44.44\%$$
  $$\text{Throughput} = \eta \times B = 0.4444 \times 1000\text{ kbps} = 444.44\text{ kbps}$$

---

### Problem 2: Stop-and-Wait on Fast Ethernet LAN
A host transmits 1500-byte Ethernet frames on a $100\text{ Mbps}$ local area network spanning a distance of $1\text{ km}$. Velocity of propagation in copper is $2 \times 10^8\text{ m/s}$. Find the transmission delay, propagation delay, and link utilization.

#### Solution:
- **Given:**
  - $L = 1500 \times 8 = 12000\text{ bits}$
  - $B = 100\text{ Mbps} = 10^8\text{ bps}$
  - $d = 1\text{ km} = 1000\text{ m}$
  - $v = 2 \times 10^8\text{ m/s}$
- **Calculations:**
  $$T_t = \frac{12000\text{ bits}}{10^8\text{ bps}} = 0.00012\text{ s} = 0.120\text{ ms} = 120\,\mu\text{s}$$
  $$T_p = \frac{1000\text{ m}}{2 \times 10^8\text{ m/s}} = 5 \times 10^{-6}\text{ s} = 0.005\text{ ms} = 5\,\mu\text{s}$$
  $$a = \frac{T_p}{T_t} = \frac{5\,\mu\text{s}}{120\,\mu\text{s}} = \frac{1}{24} \approx 0.04167$$
  $$\eta = \frac{1}{1 + 2a} = \frac{1}{1 + 2(1/24)} = \frac{1}{1 + 1/12} = \frac{12}{13} \approx 92.31\%$$
  $$\text{Throughput} = 0.9231 \times 100\text{ Mbps} = 92.31\text{ Mbps}$$

---

### Problem 3: Sequence Number Bit Requirements
Determine the minimum number of sequence number bits $k$ required in the frame header for:
1. Stop-and-Wait ARQ.
2. Go-Back-N ARQ with a sender window size of $W_s = 7$.
3. Selective Repeat ARQ with a sender window size of $W_s = 8$.

#### Solution:
- **Part 1: Stop-and-Wait ARQ:**
  $$W_s = 1, \; W_r = 1 \implies W_s + W_r = 2 \le 2^k \implies 2^k \ge 2 \implies k = 1\text{ bit}$$
- **Part 2: Go-Back-N with $W_s = 7$:**
  $$W_r = 1 \implies W_s + W_r = 7 + 1 = 8 \le 2^k \implies 2^k \ge 8 \implies k = 3\text{ bits}$$
  *(Check: Max $W_s = 2^3 - 1 = 7$. Perfectly fits $k = 3$ bits).*
- **Part 3: Selective Repeat with $W_s = 8$:**
  $$W_s = W_r = 8 \implies W_s + W_r = 8 + 8 = 16 \le 2^k \implies 2^k \ge 16 \implies k = 4\text{ bits}$$
  *(Check: Max $W_s = 2^{4-1} = 2^3 = 8$. Requires $k = 4$ bits).*

---

### Problem 4: Maximum Window Size for 4-Bit Sequence Numbers
A data link protocol allocates 4 bits for frame sequence numbers ($k = 4$).
1. What is the total number of distinct sequence numbers?
2. What is the maximum allowable sender window size in Go-Back-N?
3. What is the maximum allowable sender window size in Selective Repeat?

#### Solution:
- Total sequence numbers $M = 2^k = 2^4 = 16$ (numbered $0$ to $15$).
- **Go-Back-N:**
  $$W_s \le 2^k - 1 = 16 - 1 = 15, \quad W_r = 1$$
- **Selective Repeat:**
  $$W_s \le 2^{k-1} = 2^{4-1} = 2^3 = 8, \quad W_r \le 8$$

---

### Problem 5: Minimum Frame Size for 50% Efficiency
A network channel has a bandwidth of $10\text{ Mbps}$ and a one-way propagation delay of $10\text{ ms}$. If Stop-and-Wait ARQ is used, what is the minimum frame size required to achieve at least $50\%$ channel efficiency?

#### Solution:
- **Given:**
  - $\eta \ge 0.50$
  - $B = 10\text{ Mbps} = 10^7\text{ bps}$
  - $T_p = 10\text{ ms} = 0.01\text{ s}$
- **Formula:**
  $$\eta = \frac{T_t}{T_t + 2T_p} \ge 0.5 \implies T_t \ge 0.5(T_t + 2T_p) \implies 0.5 T_t \ge T_p \implies T_t \ge 2T_p$$
- Substitute $T_t = \frac{L}{B}$:
  $$\frac{L}{B} \ge 2T_p \implies L \ge 2 \cdot T_p \cdot B$$
  $$L \ge 2 \times (0.01\text{ s}) \times (10^7\text{ bps}) = 200,000\text{ bits} = 25,000\text{ Bytes} = 25\text{ KB}$$

---

## Level 2: Standard University & Placement Problems (Problems 6 to 10)

### Problem 6: Geostationary Satellite Link with Stop-and-Wait
A geostationary satellite link connects two ground earth stations separated by $36,000\text{ km}$. The channel bandwidth is $1\text{ Mbps}$. Propagation speed in space is $3 \times 10^8\text{ m/s}$. The frame size is $1000\text{ bytes}$.
1. Find $T_t, T_p,$ and $a$.
2. Find Stop-and-Wait efficiency $\eta$ and throughput.
3. What is the optimal sliding window size $N$ needed to achieve $100\%$ efficiency?

#### Solution:
- **Given:**
  - $L = 1000 \times 8 = 8000\text{ bits}$
  - $B = 10^6\text{ bps}$
  - $d = 36,000\text{ km} = 36 \times 10^6\text{ m}$
  - $v = 3 \times 10^8\text{ m/s}$
- **Part 1: Delays:**
  $$T_t = \frac{8000\text{ bits}}{10^6\text{ bps}} = 8.00\text{ ms}$$
  $$T_p = \frac{36 \times 10^6\text{ m}}{3 \times 10^8\text{ m/s}} = 0.120\text{ s} = 120.00\text{ ms}$$
  $$a = \frac{T_p}{T_t} = \frac{120.00\text{ ms}}{8.00\text{ ms}} = 15.00$$
- **Part 2: Stop-and-Wait Performance:**
  $$\eta = \frac{1}{1 + 2a} = \frac{1}{1 + 2(15)} = \frac{1}{31} \approx 0.03226 = 3.226\%$$
  $$\text{Throughput} = \eta \times B = 0.03226 \times 1000\text{ kbps} = 32.26\text{ kbps}$$
- **Part 3: Optimal Sliding Window Size:**
  $$N_{\text{opt}} = \lceil 1 + 2a \rceil = 1 + 2(15) = 31\text{ frames}$$

---

### Problem 7: Sliding Window Performance on Satellite Link
Using the satellite link parameters from Problem 6 ($T_t = 8\text{ ms}, T_p = 120\text{ ms}, a = 15, B = 1\text{ Mbps}$):
1. Compute the efficiency and throughput if window size $N = 15$.
2. Compute the efficiency and throughput if window size $N = 31$.

#### Solution:
- **Part 1: When $N = 15$:**
  $$\eta = \min\left(1, \frac{N}{1 + 2a}\right) = \frac{15}{1 + 30} = \frac{15}{31} \approx 0.48387 = 48.39\%$$
  $$\text{Throughput} = 0.4839 \times 1000\text{ kbps} = 483.9\text{ kbps}$$
- **Part 2: When $N = 31$:**
  $$\eta = \min\left(1, \frac{31}{1 + 30}\right) = \frac{31}{31} = 1.00 = 100.0\%$$
  $$\text{Throughput} = 1.00 \times 1000\text{ kbps} = 1000.0\text{ kbps} = 1.00\text{ Mbps}$$

---

### Problem 8: Bandwidth-Delay Product (BDP) in Bits and Frames
A $100\text{ Mbps}$ cross-country optical fiber link has a one-way propagation delay of $T_p = 25\text{ ms}$. Frame size is $1250\text{ bytes}$.
1. Calculate the Bandwidth-Delay Product (BDP) in bits and bytes.
2. Express the BDP in terms of maximum frames in flight.
3. What is parameter $a$?

#### Solution:
- **Part 1: BDP in bits:**
  $$\text{RTT} = 2 \times T_p = 2 \times 25\text{ ms} = 50\text{ ms} = 0.050\text{ s}$$
  $$\text{BDP (bits)} = B \times \text{RTT} = 100 \times 10^6\text{ bps} \times 0.050\text{ s} = 5,000,000\text{ bits} = 5\text{ Mbits}$$
  $$\text{BDP (bytes)} = \frac{5,000,000}{8} = 625,000\text{ Bytes} = 625\text{ KB}$$
- **Part 2: BDP in frames:**
  $$\text{Frame size in bits } L = 1250 \times 8 = 10,000\text{ bits}$$
  $$\text{BDP (frames)} = \frac{\text{BDP (bits)}}{L} = \frac{5,000,000\text{ bits}}{10,000\text{ bits}} = 500\text{ frames}$$
- **Part 3: Parameter $a$:**
  $$T_t = \frac{10,000\text{ bits}}{10^8\text{ bps}} = 0.0001\text{ s} = 0.1\text{ ms}$$
  $$a = \frac{T_p}{T_t} = \frac{25\text{ ms}}{0.1\text{ ms}} = 250 \implies 2a = 500\text{ frames}$$

---

### Problem 9: Stop-and-Wait with ACK Overhead and Processing Delay
A sender transmits 1000-byte data frames over a $1\text{ Mbps}$, $1000\text{ km}$ link ($v = 2 \times 10^8\text{ m/s}$). Unlike ideal textbook models:
- Acknowledgment frames are $100\text{ bytes}$ long.
- Receiver processing delay is $T_{\text{proc}} = 1.0\text{ ms}$.
Calculate the complete cycle time and the true channel efficiency.

#### Solution:
- **Given:**
  - $L = 1000 \times 8 = 8000\text{ bits} \implies T_t = \frac{8000}{10^6} = 8.00\text{ ms}$
  - $L_{\text{ack}} = 100 \times 8 = 800\text{ bits} \implies T_{\text{ack}} = \frac{800}{10^6} = 0.80\text{ ms}$
  - $d = 1000\text{ km} \implies T_p = \frac{10^6}{2 \times 10^8} = 5.00\text{ ms}$
  - $T_{\text{proc}} = 1.00\text{ ms}$
- **Total Cycle Time:**
  $$T_{\text{cycle}} = T_t + T_p + T_{\text{proc}} + T_{\text{ack}} + T_p$$
  $$T_{\text{cycle}} = 8.00 + 5.00 + 1.00 + 0.80 + 5.00 = 19.80\text{ ms}$$
- **Channel Efficiency:**
  $$\eta = \frac{T_t}{T_{\text{cycle}}} = \frac{8.00\text{ ms}}{19.80\text{ ms}} \approx 0.4040 = 40.40\%$$

---

### Problem 10: Retransmissions & Effective Throughput Under Frame Loss
Consider the link in Problem 9 where the ideal efficiency is $\eta_{\text{ideal}} = 40.40\%$. If the frame loss probability across the link is $P = 0.10$ ($10\%$ packet drop rate):
1. What is the average number of transmissions required to successfully deliver one frame?
2. What is the effective channel utilization and effective throughput?

#### Solution:
- **Part 1: Average Transmissions $\mathbb{E}[N_{tx}]$:**
  $$\mathbb{E}[N_{tx}] = \frac{1}{1 - P} = \frac{1}{1 - 0.10} = \frac{1}{0.90} \approx 1.111\text{ transmissions}$$
- **Part 2: Effective Efficiency:**
  $$\eta_{\text{eff}} = (1 - P) \times \eta_{\text{ideal}} = 0.90 \times 0.40404 \approx 0.3636 = 36.36\%$$
- **Effective Throughput:**
  $$\text{Effective Throughput} = \eta_{\text{eff}} \times B = 0.3636 \times 1000\text{ kbps} = 363.6\text{ kbps}$$

---

## Level 3: GATE CS/IT Examination Challenges (Problems 11 to 15)

### Problem 11: GBN vs Selective Repeat Under Channel Error (GATE CS)
A link has bandwidth $B = 10\text{ Mbps}$, distance $d = 2000\text{ km}$, and propagation speed $v = 2 \times 10^8\text{ m/s}$. Frame size is $1000\text{ bytes}$. The sender uses a sliding window size of $N = 8$. The frame error rate is $P = 0.05$.
Compare the effective utilization and average transmission count per frame for:
1. Go-Back-N (GBN) ARQ.
2. Selective Repeat (SR) ARQ.

#### Solution:
- **Step 1: Delays & Ideal Utilization:**
  $$T_t = \frac{8000\text{ bits}}{10^7\text{ bps}} = 0.80\text{ ms}, \quad T_p = \frac{2 \times 10^6\text{ m}}{2 \times 10^8\text{ m/s}} = 10.0\text{ ms}$$
  $$a = \frac{T_p}{T_t} = \frac{10.0}{0.80} = 12.50$$
  $$\eta_{\text{ideal}} = \frac{N}{1 + 2a} = \frac{8}{1 + 2(12.5)} = \frac{8}{26} \approx 0.30769 = 30.77\%$$
- **Step 2: Go-Back-N ARQ under Loss:**
  $$\mathbb{E}[N_{tx, \text{GBN}}] = \frac{1 + (N - 1)P}{1 - P} = \frac{1 + (8 - 1)(0.05)}{1 - 0.05} = \frac{1 + 0.35}{0.95} = \frac{1.35}{0.95} \approx 1.421$$
  $$\eta_{\text{eff, GBN}} = \frac{1 - P}{1 + (N - 1)P} \cdot \eta_{\text{ideal}} = \frac{0.95}{1.35} \times 0.30769 \approx 0.2165 = 21.65\%$$
- **Step 3: Selective Repeat ARQ under Loss:**
  $$\mathbb{E}[N_{tx, \text{SR}}] = \frac{1}{1 - P} = \frac{1}{0.95} \approx 1.053$$
  $$\eta_{\text{eff, SR}} = (1 - P) \cdot \eta_{\text{ideal}} = 0.95 \times 0.30769 \approx 0.2923 = 29.23\%$$
- **Summary:** Selective Repeat achieves $29.23\%$ efficiency vs GBN's $21.65\%$, saving significant channel capacity.

---

### Problem 12: Reverse Window Sizing for Target Utilization (GATE CS)
A satellite link has bandwidth $B = 100\text{ Mbps}$ and one-way propagation delay $T_p = 2.0\text{ ms}$. Frame size is $1000\text{ bytes}$. The system requires an overall channel efficiency of at least $80\%$.
1. What is the minimum required sender window size $N$?
2. What is the minimum number of sequence number bits $k$ required if Go-Back-N is used?
3. What is the minimum number of sequence number bits $k$ required if Selective Repeat is used?

#### Solution:
- **Delays:**
  $$T_t = \frac{8000\text{ bits}}{10^8\text{ bps}} = 0.08\text{ ms} = 80\,\mu\text{s}$$
  $$a = \frac{T_p}{T_t} = \frac{2.0\text{ ms}}{0.08\text{ ms}} = 25.0$$
- **Window Size for $\eta \ge 0.80$:**
  $$\eta = \frac{N}{1 + 2a} \ge 0.80 \implies N \ge 0.80(1 + 2 \times 25) = 0.80(51) = 40.8$$
  Since $N$ must be an integer:
  $$N = \lceil 40.8 \rceil = 41\text{ frames}$$
- **Sequence Bits for GBN ($W_s = 41, W_r = 1$):**
  $$2^k \ge W_s + 1 = 41 + 1 = 42 \implies k = \lceil \log_2(42) \rceil = 6\text{ bits} \quad (2^6 = 64 \ge 42)$$
- **Sequence Bits for SR ($W_s = 41, W_r = 41$):**
  $$2^k \ge 2 \times W_s = 2 \times 41 = 82 \implies k = \lceil \log_2(82) \rceil = 7\text{ bits} \quad (2^7 = 128 \ge 82)$$

---

### Problem 13: Optimal Frame Size Derivation for Stop-and-Wait
In a noisy channel with bit error rate (BER) $p$, the probability that an $L$-bit frame arrives uncorrupted is $(1 - p)^L \approx 1 - Lp$ (for small $p$).
Derive the expression for the optimal frame length $L^*$ that maximizes the effective throughput in Stop-and-Wait ARQ.

#### Solution:
- Effective throughput:
  $$S(L) = \frac{L(1 - Lp)}{T_t + 2T_p} = \frac{L(1 - Lp)}{\frac{L}{B} + 2T_p}$$
- To find the maximum, take derivative with respect to $L$ and set $\frac{dS}{dL} = 0$:
  Let $f(L) = L - pL^2$, $g(L) = \frac{L}{B} + 2T_p$.
  $$\frac{dS}{dL} = \frac{(1 - 2pL)(\frac{L}{B} + 2T_p) - (L - pL^2)(\frac{1}{B})}{(\frac{L}{B} + 2T_p)^2} = 0$$
  $$(1 - 2pL)\left(\frac{L}{B} + 2T_p\right) - \frac{L}{B} + \frac{pL^2}{B} = 0$$
  $$\frac{L}{B} + 2T_p - \frac{2pL^2}{B} - 4pL T_p - \frac{L}{B} + \frac{pL^2}{B} = 0$$
  $$2T_p - \frac{pL^2}{B} - 4pL T_p = 0$$
- For typical physical links where frame transmission is much shorter than RTT ($\frac{pL^2}{B} \gg 4pL T_p$ when transmission rate is high):
  $$\frac{p L^2}{B} \approx 2T_p \implies L^{*2} \approx \frac{2 \cdot B \cdot T_p}{p} \implies L^* \approx \sqrt{\frac{2 \cdot B \cdot T_p}{p}}$$

---

### Problem 14: Overlapping Window Boundary with Asymmetric Windows
A data link protocol runs over a link where sequence numbers are represented by $m = 4$ bits. The receiver has a fixed buffer allocating a receiver window size of $W_r = 5$.
What is the absolute maximum sender window size $W_s$ that can be configured without risking duplicate frame delivery?

#### Solution:
- The fundamental anti-ambiguity condition across all sliding window protocols is:
  $$W_s + W_r \le 2^m$$
- Given $m = 4 \implies 2^m = 2^4 = 16$.
- Given $W_r = 5$:
  $$W_s + 5 \le 16 \implies W_s \le 16 - 5 = 11$$
- Therefore, the maximum allowable sender window size is $W_s = 11$.

---

### Problem 15: Bidirectional Piggybacking Savings Calculation
Two routers A and B exchange bidirectional data at $10\text{ Mbps}$ with $T_p = 5\text{ ms}$. Each data packet has $L = 1000\text{ bytes}$.
- Case 1: Standalone ACKs of size $64\text{ bytes}$ are transmitted.
- Case 2: Full Piggybacking is utilized (ACK is inserted into header with $0\text{ byte}$ overhead).
Compare the total bandwidth consumed by ACKs across a 10,000-frame transfer session.

#### Solution:
- **Case 1 (Standalone ACKs):**
  - Number of ACK packets $= 10,000$
  - Size of each ACK $= 64\text{ Bytes} = 512\text{ bits}$
  - Total overhead bits $= 10,000 \times 512 = 5,120,000\text{ bits} = 5.12\text{ Mbits} = 640\text{ KB}$
  - Time spent transmitting ACKs $= \frac{5.12\times 10^6\text{ bits}}{10^7\text{ bps}} = 0.512\text{ seconds}$
- **Case 2 (Piggybacking):**
  - Standalone ACK frames $= 0$
  - Total extra bits transmitted for ACKs $= 0\text{ bits}$
  - Channel capacity saved $= 5.12\text{ Mbits}$
- **Conclusion:** Piggybacking saves $100\%$ of standalone ACK framing overhead in continuous bidirectional communication.

---

## ⬅️ Navigation
- **Module Index:** [INDEX.md](../INDEX.md)
- **Conceptual Notes:** [notes_05b_flow_control.md](notes_05b_flow_control.md)
- **Visual Diagrams:** [diagrams_05b_flow_control.md](diagrams_05b_flow_control.md)
- **Practice MCQs:** [mcqs.md](mcqs.md)
