# 01. Computer Networking Fundamentals — Solved Numericals

> **All numerical calculations in this file are mathematically verified against `tools/verify/verify_fundamentals.py`.**  
> Covers Transmission Delay, Propagation Delay, End-to-End Latency, Queuing, Bandwidth-Delay Product, Full Mesh Topologies, Switching Comparisons, and Goodput.

---

## 📐 Formula Sheet

| Metric / Parameter | Symbol | Formula | Standard Units | When to Use |
|---|:---:|---|:---:|---|
| **Transmission Delay** | $T_t$ | $$T_t = \frac{L}{R}$$ | Seconds ($\text{s}$) or $\text{ms}$ | Time to push $L$ bits onto a link of rate $R$ bps. Independent of distance. |
| **Propagation Delay** | $T_p$ | $$T_p = \frac{d}{v}$$ | Seconds ($\text{s}$) or $\text{ms}$ | Time for a bit to travel distance $d$ at speed $v$ ($2 \times 10^8\text{ m/s}$ in copper/fiber). Independent of bandwidth. |
| **Total Nodal Delay** | $D$ | $$D = T_t + T_p + T_q + T_{\text{proc}}$$ | Seconds / $\text{ms}$ | Total delay at a single link hop. |
| **Bandwidth-Delay Product** | $\text{BDP}$ | $$\text{BDP} = R \times \text{RTT}$$ (or $R \times T_p$) | Bits or Bytes | Volume of bits in flight filling the pipe. |
| **Full Mesh Duplex Links** | $N_{\text{links}}$ | $$N_{\text{links}} = \frac{n(n-1)}{2}$$ | Physical cables | Dedicated duplex links connecting $n$ nodes. |
| **Mesh Ports per Device** | $P$ | $$P = n - 1$$ | Hardware NIC ports | Ports required per device in full mesh. |
| **Store-and-Forward Pipelined Delay** | $T_{\text{total}}$ | $$T = (k + N - 1) \frac{L}{R} + N \cdot T_p$$ | Seconds | $k$ packets of size $L$ sent across $N$ identical hops of rate $R$. |
| **Circuit Switching Total Time** | $T_{\text{circ}}$ | $$T = T_{\text{setup}} + \frac{M}{R} + T_p$$ | Seconds | Entire message $M$ transmitted after circuit establishment. |
| **Throughput & Goodput** | $G$ | $$G = \text{Throughput} \times \frac{\text{Payload Bytes}}{\text{Total Packet Bytes}}$$ | bps / Mbps | Useful payload rate delivered to application. |

---

## 🟢 Level 1: Basic Fundamental Problems

### Problem 1.1: Transmission vs. Propagation Delay
**Question:** A host sends a 2 MB file over a 10 Mbps point-to-point link. The physical distance is 2,000 km, and the signal propagation speed in the cable is $2 \times 10^8\text{ m/s}$. Calculate (a) the transmission delay $T_t$, (b) the propagation delay $T_p$, and (c) the total link latency ignoring queuing and processing delays. (Assume $1\text{ MB} = 10^6\text{ bytes}$).

- **Given:**  
  - File size $L = 2\text{ MB} = 2 \times 10^6\text{ bytes} = 16 \times 10^6\text{ bits}$  
  - Bandwidth $R = 10\text{ Mbps} = 10 \times 10^6\text{ bps}$  
  - Distance $d = 2,000\text{ km} = 2 \times 10^6\text{ m}$  
  - Velocity $v = 2 \times 10^8\text{ m/s}$
- **Find:** $T_t$, $T_p$, and $T_{\text{total}}$
- **Formulas:**  
  $$T_t = \frac{L}{R}, \quad T_p = \frac{d}{v}, \quad T_{\text{total}} = T_t + T_p$$
- **Step-by-Step Solution:**
  1. $T_t = \frac{16 \times 10^6\text{ bits}}{10 \times 10^6\text{ bps}} = 1.6000\text{ seconds} = 1,600\text{ ms}$.
  2. $T_p = \frac{2 \times 10^6\text{ m}}{2 \times 10^8\text{ m/s}} = 0.0100\text{ seconds} = 10\text{ ms}$.
  3. $T_{\text{total}} = 1.6000 + 0.0100 = 1.6100\text{ seconds} = 1,610\text{ ms}$.
- **Final Answer:** $T_t = 1.6\text{ s}$, $T_p = 10\text{ ms}$, Total Delay = $1,610\text{ ms}$.
- **⚠️ Common Trap:** Confusing bits with bytes! Always multiply byte sizes by 8 before dividing by bits-per-second bandwidth.

---

### Problem 1.2: VoIP Packet Transmission in High-Speed Networks
**Question:** A digitized voice packet of 64 bytes is sent over a 1 Gbps fiber optic link over a distance of 10 km ($v = 2 \times 10^8\text{ m/s}$). Calculate the transmission delay and propagation delay in microseconds ($\mu\text{s}$).

- **Given:**  
  - $L = 64\text{ bytes} = 64 \times 8 = 512\text{ bits}$  
  - $R = 1\text{ Gbps} = 10^9\text{ bps}$  
  - $d = 10\text{ km} = 10,000\text{ m}$  
  - $v = 2 \times 10^8\text{ m/s}$
- **Step-by-Step Solution:**
  1. $T_t = \frac{512}{10^9} = 5.12 \times 10^{-7}\text{ s} = 0.512\text{ }\mu\text{s}$.
  2. $T_p = \frac{10,000}{2 \times 10^8} = 5 \times 10^{-5}\text{ s} = 50.00\text{ }\mu\text{s}$.
- **Final Answer:** $T_t \approx 0.51\text{ }\mu\text{s}$, $T_p = 50.00\text{ }\mu\text{s}$.
- **Insight:** For small packets on high-speed links, propagation delay dominates transmission delay by nearly 100 to 1 ($50\text{ }\mu\text{s}$ vs $0.51\text{ }\mu\text{s}$).

---

### Problem 1.3: Full Mesh Topology Link & Port Calculation
**Question:** A company has 20 branch offices and wishes to build a fully meshed point-to-point network between all branches. Calculate:
1. The total number of dedicated duplex physical links required.
2. The number of ports required on each branch router.
3. The total number of ports across all 20 routers.

- **Given:** $n = 20$
- **Formulas:**  
  $$N_{\text{links}} = \frac{n(n-1)}{2}, \quad P = n - 1, \quad P_{\text{total}} = n(n-1)$$
- **Step-by-Step Solution:**
  1. $N_{\text{links}} = \frac{20 \times 19}{2} = 190\text{ links}$.
  2. $P = 20 - 1 = 19\text{ ports per router}$.
  3. $P_{\text{total}} = 20 \times 19 = 380\text{ total ports}$.
- **Final Answer:** 190 links, 19 ports per device, 380 total ports.

---

### Problem 1.4: Star vs. Mesh Cable Comparison
**Question:** Compare the number of physical cables needed to connect 10 computers using (a) a Star topology with a central switch, and (b) a Full Mesh topology.

- **Given:** $n = 10$
- **Step-by-Step Solution:**
  1. Star topology: Each host connects to the central switch with 1 cable. Total cables = $n = 10$.
  2. Full Mesh: Total cables = $\frac{10 \times 9}{2} = 45$.
- **Final Answer:** Star requires 10 cables; Full Mesh requires 45 cables (4.5× more cabling).

---

### Problem 1.5: Bandwidth-Delay Product (BDP) Calculation
**Question:** A cross-country link has a bandwidth of 100 Mbps and a Round-Trip Time (RTT) of 50 ms. Calculate the Bandwidth-Delay Product in (a) bits, and (b) bytes.

- **Given:** $R = 100\text{ Mbps} = 10^8\text{ bps}$, $\text{RTT} = 50\text{ ms} = 0.050\text{ s}$.
- **Formula:** $\text{BDP} = R \times \text{RTT}$
- **Step-by-Step Solution:**
  1. $\text{BDP (bits)} = 10^8\text{ bps} \times 0.050\text{ s} = 5,000,000\text{ bits}$.
  2. $\text{BDP (bytes)} = \frac{5,000,000}{8} = 625,000\text{ bytes} \approx 610.35\text{ KiB}$.
- **Final Answer:** 5,000,000 bits (625,000 bytes).

---

### Problem 1.6: Throughput vs. Goodput with Header Overhead
**Question:** A web server streams data over a 100 Mbps Ethernet link. Each packet on the wire is 1518 bytes long, containing 18 bytes of Ethernet framing, 20 bytes of IPv4 header, 20 bytes of TCP header, and 1460 bytes of user data payload. If the link runs at 100% throughput, what is the maximum achievable goodput?

- **Given:** $R = 100\text{ Mbps}$, Total Packet = 1518 bytes, Data Payload = 1460 bytes.
- **Formula:** $\text{Goodput} = R \times \frac{\text{Payload}}{\text{Total}}$
- **Step-by-Step Solution:**
  1. Protocol efficiency ratio = $\frac{1460}{1518} \approx 0.96179$ (96.18%).
  2. $\text{Goodput} = 100\text{ Mbps} \times 0.96179 = 96.18\text{ Mbps}$.
- **Final Answer:** Goodput = 96.18 Mbps.

---

### Problem 1.7: Satellite Channel Propagation Delay
**Question:** A Geostationary Earth Orbit (GEO) communications satellite orbits at an altitude of 36,000 km above the earth. Calculate the one-way propagation delay from a ground station to the satellite. ($v = 3 \times 10^8\text{ m/s}$ in space).

- **Given:** $d = 36,000\text{ km} = 3.6 \times 10^7\text{ m}$, $v = 3 \times 10^8\text{ m/s}$.
- **Step-by-Step Solution:**
  $$T_p = \frac{3.6 \times 10^7}{3 \times 10^8} = 0.12\text{ s} = 120\text{ ms}$$
- **Final Answer:** 120 ms (Note: RTT is ground-satellite-ground round trip $\approx 4 \times 120 = 480\text{ ms}$).

---

### Problem 1.8: Distance Where $T_t = T_p$
**Question:** A sender transmits 1000-byte packets onto a 100 Mbps link. At what physical distance will the propagation delay equal the transmission delay? ($v = 2 \times 10^8\text{ m/s}$).

- **Given:** $L = 1000 \times 8 = 8000\text{ bits}$, $R = 10^8\text{ bps}$, $v = 2 \times 10^8\text{ m/s}$.
- **Equating Delays:**  
  $$T_t = \frac{8000}{10^8} = 8 \times 10^{-5}\text{ s} = 80\text{ }\mu\text{s}$$  
  $$T_p = \frac{d}{v} = 8 \times 10^{-5} \implies d = (8 \times 10^{-5}) \times (2 \times 10^8) = 16,000\text{ meters} = 16\text{ km}$$
- **Final Answer:** 16 km.

---

### Problem 1.9: Link Utilization in Stop-and-Wait
**Question:** In a point-to-point link where $T_t = 1\text{ ms}$ and $T_p = 49.5\text{ ms}$, the sender transmits 1 packet and must wait for an acknowledgment before sending the next. Acknowledgment transmission time is negligible. What is the link utilization $\eta$?

- **Formula:** $\eta = \frac{T_t}{T_t + 2T_p} = \frac{1}{1 + 2a}$, where $a = \frac{T_p}{T_t}$.
- **Step-by-Step Solution:**
  1. $a = \frac{49.5}{1} = 49.5$.
  2. $\text{Cycle Time} = T_t + 2T_p = 1 + 2(49.5) = 100\text{ ms}$.
  3. $\eta = \frac{1\text{ ms}}{100\text{ ms}} = 0.01 = 1.0\%$.
- **Final Answer:** 1.0% (The link is 99% idle!).

---

### Problem 1.10: Number of Subnet Links in Tree Topology
**Question:** An enterprise network connects 1 root core switch to 4 distribution switches, and each distribution switch connects to 8 access switches. Each access switch connects to 24 workstations. How many total physical point-to-point links exist in this network?

- **Step-by-Step Solution:**
  1. Core to Distribution links: $1 \times 4 = 4$.
  2. Distribution to Access links: $4 \times 8 = 32$.
  3. Access to Workstation links: $(4 \times 8) \times 24 = 32 \times 24 = 768$.
  4. Total links = $4 + 32 + 768 = 804\text{ links}$.
- **Final Answer:** 804 links.

---

## 🟡 Level 2: Exam-Standard Problems

### Problem 2.1: Store-and-Forward Packet Switching Delay Across 3 Links
**Question:** A source host transmits a file of 1 MB ($10^6$ bytes) to a destination host across 3 links (connected by 2 intermediate store-and-forward routers). Each link has a transmission capacity of 10 Mbps. Assume propagation, queuing, and processing delays are negligible.
1. Calculate the total transmission time if the file is sent as one large message (**Message Switching**).
2. Calculate the total transmission time if the file is segmented into 1,000 packets of 1,000 bytes each (**Packet Switching**).
3. Determine the speedup ratio achieved by packet switching.

- **Given:**  
  - File $M = 10^6\text{ bytes} = 8 \times 10^6\text{ bits}$  
  - Links $N = 3$ links (2 routers)  
  - Rate $R = 10\text{ Mbps} = 10^7\text{ bps}$  
  - Packet size $L = 1000\text{ bytes} = 8000\text{ bits}$, $k = 1000\text{ packets}$
- **Formulas:**  
  - Message Switching: $T_{\text{msg}} = N \times \frac{M}{R}$  
  - Packet Switching: $T_{\text{pkt}} = (k + N - 1) \times \frac{L}{R}$
- **Step-by-Step Solution:**
  1. Transmission delay for whole file per link: $\frac{8 \times 10^6}{10^7} = 0.8\text{ s}$.  
     Message switching delay = $3 \times 0.8\text{ s} = 2.4000\text{ seconds}$.
  2. Transmission delay for one 1000-byte packet: $\frac{8000}{10^7} = 0.0008\text{ s}$.  
     $T_{\text{pkt}} = (1000 + 3 - 1) \times 0.0008 = 1002 \times 0.0008 = 0.8016\text{ seconds}$.
  3. Speedup ratio = $\frac{2.4000}{0.8016} \approx 2.99\times$.
- **Final Answer:** Message Switching = 2.40 s; Packet Switching = 0.8016 s; Speedup = $2.99\times$.

---

### Problem 2.2: Circuit Switching vs. Packet Switching With Header Overhead
**Question:** A 5 MB file is sent over 4 links (3 intermediate switches) at 50 Mbps.
- **Circuit Switching:** Connection setup time is 200 ms; total propagation delay across all 4 links combined is 20 ms.
- **Packet Switching:** Packets are 1500 bytes long, including 40 bytes of headers (payload = 1460 bytes). Propagation delay is 5 ms per link. Queuing and processing delays are zero.
Which method delivers the file faster?

- **Step-by-Step Solution:**
  1. **Circuit Switching:**  
     $$T_t = \frac{5 \times 10^6 \times 8}{50 \times 10^6} = \frac{40 \times 10^6}{50 \times 10^6} = 0.8000\text{ s}$$  
     $$T_{\text{circ}} = T_{\text{setup}} + T_t + T_p = 0.200 + 0.800 + 0.020 = 1.0200\text{ s}$$
  2. **Packet Switching:**  
     Number of packets $k = \lceil\frac{5,000,000}{1460}\rceil = 3425\text{ packets}$.  
     Total packet size on wire = $1500\text{ bytes} = 12,000\text{ bits}$.  
     $T_t$ per packet = $\frac{12,000}{50 \times 10^6} = 0.00024\text{ s}$.  
     Formula: $T_{\text{pkt}} = (k + N - 1) T_t + N \times T_p$  
     $$T_{\text{pkt}} = (3425 + 4 - 1) \times 0.00024 + 4 \times 0.005$$  
     $$T_{\text{pkt}} = 3428 \times 0.00024 + 0.020 = 0.82272 + 0.020 = 0.8427\text{ s}$$
- **Final Answer:** Packet Switching is faster (0.8427 s vs. 1.0200 s).

---

### Problem 2.3: End-to-End Delay with Queue and Processing Buffers
**Question:** A packet of size 1250 bytes (10,000 bits) travels from Host A to Host B across 2 intermediate routers (3 links). Each link is 10 Mbps and 100 km long ($v = 2 \times 10^8\text{ m/s}$).
- Each router has a processing delay of 20 $\mu\text{s}$.
- When the packet reaches Router 1, there are 2 packets waiting ahead in the output queue.
- When it reaches Router 2, there is 1 packet waiting ahead in the output queue.
Calculate the total end-to-end delay in milliseconds.

- **Given:**  
  - $L = 10,000\text{ bits}$, $R = 10\text{ Mbps} = 10^7\text{ bps}$  
  - $T_t = \frac{10,000}{10^7} = 1.000\text{ ms}$ per link  
  - $T_p = \frac{100,000}{2 \times 10^8} = 0.500\text{ ms}$ per link  
  - $T_{\text{proc}} = 20\text{ }\mu\text{s} = 0.020\text{ ms}$ per router (2 routers = $0.040\text{ ms}$)
- **Queuing Delays:**  
  - At Router 1: Waits for 2 packets ahead to transmit = $2 \times 1.000\text{ ms} = 2.000\text{ ms}$.  
  - At Router 2: Waits for 1 packet ahead to transmit = $1 \times 1.000\text{ ms} = 1.000\text{ ms}$.  
  - Total Queuing Delay $T_q = 2.000 + 1.000 = 3.000\text{ ms}$.
- **Summing All Components:**  
  - Total $T_t$ (3 links) = $3 \times 1.000 = 3.000\text{ ms}$  
  - Total $T_p$ (3 links) = $3 \times 0.500 = 1.500\text{ ms}$  
  - Total $T_{\text{proc}}$ = $0.040\text{ ms}$  
  - Total $T_q$ = $3.000\text{ ms}$  
  - $T_{\text{total}} = 3.000 + 1.500 + 0.040 + 3.000 = 7.540\text{ ms}$.
- **Final Answer:** 7.540 ms.

---

## 🔴 Level 3: GATE-Hard Problems

### Problem 3.1: Optimal Packet Size for Minimum End-to-End Delay (GATE Classic)
**Question:** A message of size $M$ bits is to be transmitted across $N$ identical store-and-forward links, each of bandwidth $R$ bps. Each packet carries a fixed header of $h$ bits. If the user data payload in each packet is $p$ bits (so total packet length is $p + h$), find the value of $p$ that minimizes total transmission delay, and calculate the optimal payload size for $M = 100,000\text{ bits}$, $N = 5\text{ links}$, and $h = 160\text{ bits}$.

- **Step-by-Step Derivation:**
  1. Number of packets $k = \frac{M}{p}$.
  2. Packet size $L = p + h$.
  3. Total transmission time:  
     $$T(p) = (k + N - 1) \frac{p + h}{R} = \left(\frac{M}{p} + N - 1\right) \frac{p + h}{R}$$
  4. Expanding numerator:  
     $$f(p) = M + \frac{M \cdot h}{p} + (N - 1)p + (N - 1)h$$
  5. Take derivative with respect to $p$ and set to 0:  
     $$\frac{df}{dp} = -\frac{M \cdot h}{p^2} + (N - 1) = 0 \implies p^2 = \frac{M \cdot h}{N - 1}$$  
     $$p_{\text{opt}} = \sqrt{\frac{M \cdot h}{N - 1}}$$
  6. Substitute values:  
     $$p_{\text{opt}} = \sqrt{\frac{100,000 \times 160}{5 - 1}} = \sqrt{\frac{16,000,000}{4}} = \sqrt{4,000,000} = 2,000\text{ bits}$$
- **Final Answer:** $p_{\text{opt}} = \sqrt{\frac{M \cdot h}{N - 1}} = 2,000\text{ bits}$ (250 bytes).

---

### Problem 3.2: Concurrent User Capacity in Circuit vs. Packet Switching (GATE Standard)
**Question:** Users share a 10 Mbps link. Each user requires 1 Mbps when transmitting, but an active user transmits only 10% of the time.
1. How many users can be supported under Circuit Switching?
2. If 35 users are supported under Packet Switching, what is the probability that more than 10 users transmit simultaneously? (Write the binomial formulation).

- **Step-by-Step Solution:**
  1. **Circuit Switching:** Since each user needs 1 Mbps dedicated bandwidth, the link capacity is strictly:  
     $$\text{Users} = \frac{10\text{ Mbps}}{1\text{ Mbps}} = 10\text{ users}$$
  2. **Packet Switching:**  
     With 35 users, each transmitting with independent probability $p = 0.1$, the number of active users $X \sim \text{Binomial}(n=35, p=0.1)$.  
     The link becomes congested when $X > 10$:  
     $$P(X > 10) = \sum_{k=11}^{35} \binom{35}{k} (0.1)^k (0.9)^{35-k} \approx 0.00042\text{ (0.04\%)}$$
- **Final Answer:** Circuit Switching supports 10 users; Packet Switching supports 35 users with only a 0.04% congestion probability (statistical multiplexing yields 3.5× capacity!).

---

## 📝 Practice Problems

<details>
<summary><b>Practice 1: Full Mesh Link Scalability</b> (Click to reveal answer)</summary>

**Question:** An engineer adds 5 new routers to an existing full mesh network of 10 routers. How many *new* physical cables must be installed to maintain full mesh connectivity?  
**Solution:**  
- Links in 10-node mesh: $\frac{10 \times 9}{2} = 45$.  
- Links in 15-node mesh: $\frac{15 \times 14}{2} = 105$.  
- New links required = $105 - 45 = 60\text{ cables}$.  
**Answer:** 60 cables.
</details>

<details>
<summary><b>Practice 2: Transmission Delay for 1500-byte MTU</b> (Click to reveal answer)</summary>

**Question:** Calculate the transmission delay of an Ethernet MTU frame (1500 bytes) on:
(a) A 10 Mbps link, (b) A 100 Mbps Fast Ethernet link, and (c) A 10 Gbps 10GBASE-T link.  
**Solution:**  
- Bits = $1500 \times 8 = 12,000\text{ bits}$.  
- (a) $T_t = \frac{12,000}{10^7} = 1.2\text{ ms}$.  
- (b) $T_t = \frac{12,000}{10^8} = 0.12\text{ ms} = 120\text{ }\mu\text{s}$.  
- (c) $T_t = \frac{12,000}{10^{10}} = 1.2\text{ }\mu\text{s}$.  
**Answer:** (a) 1.2 ms, (b) 120 $\mu\text{s}$, (c) 1.2 $\mu\text{s}$.
</details>

<details>
<summary><b>Practice 3: Propagation Delay Across Fiber vs. Copper</b> (Click to reveal answer)</summary>

**Question:** Does a light pulse in an optical fiber travel faster than an electrical wave in twisted-pair copper cable?  
**Solution:**  
In both media, signal velocity is dictated by the relative dielectric constant / refractive index of the insulating material ($v = c / n$).  
For both standard copper cable and silica glass fiber, $n \approx 1.46 - 1.5$, giving $v \approx 2 \times 10^8\text{ m/s}$ (about two-thirds the speed of light in vacuum). The propagation speed is essentially identical. Fiber provides orders-of-magnitude higher *bandwidth* ($R$), not higher propagation speed ($v$).  
**Answer:** No; both propagate at approximately $2 \times 10^8\text{ m/s}$.
</details>
