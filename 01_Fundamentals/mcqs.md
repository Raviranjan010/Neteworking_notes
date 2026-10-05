# 01. Computer Networking Fundamentals — Practice MCQs, MSQs & NATs

> **Comprehensive assessment containing 55 questions:**  
> - **Part A:** 30 Multiple Choice Questions (Single Correct — balanced A/B/C/D distribution)  
> - **Part B:** 10 Multiple Select Questions (GATE style — 1 to 4 correct)  
> - **Part C:** 10 Numerical Answer Type (NAT) Questions  
> - **Part D:** 5 Scenario & Output Diagnosis Challenges  
> All answers are hidden inside `<details>` blocks with detailed explanations debunking common traps.

---

## 📝 Part A: Multiple Choice Questions (Single Option Correct)

### Easy (Questions 1–10)

#### Q1. [Concept] Which component of data communication represents the rules governing how devices exchange information?
- A) Transmission Medium
- B) Message Payload
- C) Protocol
- D) Network Interface Card
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
A protocol is a formalized set of rules governing syntax, semantics, and timing. The message is the information itself; the medium is the physical path; the NIC is the hardware adapter.
</details>

#### Q2. [Concept] What is the primary characteristic of a Simplex transmission mode?
- A) Data can flow in only one fixed direction at all times
- B) Data flows in both directions simultaneously
- C) Both stations can transmit, but only one at a time
- D) Data requires dedicated physical circuits before transmitting
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Simplex transmission is strictly unidirectional (e.g., traditional television broadcasting or keyboard inputs to a CPU).
</details>

#### Q3. [Company] In a Star topology network, what occurs if an individual workstation's cable is severed?
- A) The entire network immediately crashes due to signal reflections
- B) Only the disconnected workstation loses network access; all other nodes communicate normally
- C) The central switch enters an infinite broadcast storm
- D) The network converts dynamically to a bus topology
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Star topologies feature dedicated point-to-point links between each node and the central switch, providing fault isolation.
</details>

#### Q4. [Concept] Which organization is primarily responsible for publishing Internet Requests for Comments (RFCs)?
- A) IEEE
- B) ISO
- C) ITU-T
- D) IETF
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
The Internet Engineering Task Force (IETF) develops Internet standards and publishes them as RFCs.
</details>

#### Q5. [GATE-style] If the physical distance between sender and receiver is doubled while keeping link bandwidth constant, which delay component doubles?
- A) Propagation Delay ($T_p$)
- B) Transmission Delay ($T_t$)
- C) Queuing Delay ($T_q$)
- D) Processing Delay ($T_{\text{proc}}$)
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Propagation delay is $T_p = d / v$. Doubling distance $d$ doubles $T_p$. Transmission delay $T_t = L / R$ depends strictly on packet size and bandwidth, not distance.
</details>

#### Q6. [Concept] What is the geographic scope of a Metropolitan Area Network (MAN)?
- A) Within 10 meters around a single user
- B) Within a single office building
- C) Across an entire city or metropolitan municipality (5–50 km)
- D) Across multiple continents via undersea fiber cables
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
A MAN covers a city-wide geographic area (e.g., municipal fiber or city cable television networks).
</details>

#### Q7. [Company] Which of the following topologies requires 50-ohm terminating resistors at both physical ends of the cable?
- A) Ring Topology
- B) Bus Topology
- C) Mesh Topology
- D) Star Topology
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Bus topologies use electrical terminators at both ends of the shared coaxial backbone to absorb signals and prevent reflections.
</details>

#### Q8. [Concept] In a peer-to-peer (P2P) network, what role does each connected computer play?
- A) Only a client requesting files
- B) Only a dedicated server storing databases
- C) Both a client and a server simultaneously
- D) A passive repeater node without local storage
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
In P2P architectures, participating nodes (peers) act as both consumers of data and providers/seeders of data to others.
</details>

#### Q9. [GATE-style] How many duplex physical links are required to interconnect 6 nodes in a Full Mesh topology?
- A) 15
- B) 30
- C) 12
- D) 6
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Formula: $N_{\text{links}} = \frac{n(n-1)}{2} = \frac{6 \times 5}{2} = 15$ links.
</details>

#### Q10. [Concept] What is the term for the variation in packet transit delay across a network stream?
- A) Attenuation
- B) Jitter
- C) Distortion
- D) Crosstalk
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Jitter is the statistical variance in packet arrival delay, which impairs real-time streaming and voice calls.
</details>

---

### Medium (Questions 11–20)

#### Q11. [GATE-style] A packet of length $L = 1000\text{ bytes}$ is sent over a link of bandwidth $R = 10\text{ Mbps}$. What is the transmission delay?
- A) 8 ms
- B) 0.8 ms
- C) 0.1 ms
- D) 1 ms
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
$L = 1000 \times 8 = 8,000\text{ bits}$.  
$T_t = \frac{8,000\text{ bits}}{10 \times 10^6\text{ bps}} = 0.0008\text{ s} = 0.8\text{ ms}$.
</details>

#### Q12. [Company] Why is packet switching preferred over circuit switching for general Internet data traffic?
- A) Circuit switching has higher packet loss during periods of light traffic
- B) Data traffic is bursty, making dedicated circuits highly inefficient during idle periods
- C) Packet switching guarantees dedicated constant bandwidth for every flow
- D) Packet switching eliminates the need for routing tables in intermediate routers
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Internet traffic is bursty. Packet switching uses statistical multiplexing, allowing multiple users to share link capacity when others are idle.
</details>

#### Q13. [Concept] What is the relationship between wire Throughput and application Goodput?
- A) Goodput is strictly equal to bandwidth
- B) Goodput is always greater than Throughput
- C) Goodput is strictly less than or equal to Throughput because protocol headers and retransmissions are excluded
- D) Throughput measures analog frequency (Hz), while Goodput measures digital bits
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
Throughput measures all raw bits moving over the wire; Goodput measures only the useful application payload delivered.
</details>

#### Q14. [GATE-style] If the traffic intensity $I = \frac{a \cdot L}{R}$ at a router output port approaches 1, what happens to the average queuing delay?
- A) It drops to zero
- B) It approaches infinity
- C) It stabilizes at exactly $T_t / 2$
- D) It becomes independent of packet arrival rate
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Queuing theory dictates that as traffic intensity approaches 1, queue length and average waiting time explode asymptotically toward infinity.
</details>

#### Q15. [Concept] What role do Internet Exchange Points (IXPs) serve in global network routing?
- A) They are satellite base stations used to communicate with deep space probes
- B) They provide physical facilities where ISPs peer directly to exchange traffic without paying transit fees to Tier-1 backbones
- C) They assign MAC addresses to network hardware manufacturers
- D) They replace DNS root servers during emergency cyberattacks
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
IXPs allow networks (ISPs, CDNs, cloud giants) to interconnect directly using Ethernet fabrics, lowering latency and transit costs.
</details>

#### Q16. [Company] In a token-ring local area network, what prevents data packets from colliding?
- A) Dedicated full-mesh cabling between all nodes
- B) Carrier sense collision detection (CSMA/CD)
- C) Only the station holding the circulating token is permitted to transmit
- D) Frequency division multiplexing assigning unique frequencies to each PC
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
In token passing, possession of the token grants the sole right to transmit, mathematically preventing collisions.
</details>

#### Q17. [GATE-style] A 100-node network is designed as a Full Mesh. How many I/O ports are required on each router?
- A) 99
- B) 100
- C) 4,950
- D) 50
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Each node must maintain a dedicated point-to-point link to every other node: $P = n - 1 = 100 - 1 = 99\text{ ports}$.
</details>

#### Q18. [Concept] What is the Bandwidth-Delay Product (BDP) of a 1 Gbps link with an RTT of 40 ms?
- A) 40,000 bits
- B) 4,000,000 bits
- C) 40,000,000 bits
- D) 400,000 bits
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
$\text{BDP} = R \times \text{RTT} = (10^9\text{ bps}) \times (0.040\text{ s}) = 40,000,000\text{ bits} = 40\text{ Mbits} = 5\text{ MB}$.
</details>

#### Q19. [Company] What is the key functional difference between Datagram Packet Switching and Virtual Circuit Packet Switching?
- A) Datagram switching uses copper cables; virtual circuits use optical fiber
- B) In Datagram switching, each packet is routed independently; in Virtual Circuits, a fixed logical route is established before transmission
- C) Datagram switching requires connection setup; virtual circuits are completely connectionless
- D) Virtual circuits allow packets to arrive out of order, whereas datagrams strictly arrive in order
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Datagram switching is connectionless (packets take independent paths and may arrive out-of-order). Virtual circuits establish a path beforehand and preserve order.
</details>

#### Q20. [GATE-style] In an end-to-end path with links having capacities of 10 Mbps, 100 Mbps, 2 Mbps, and 50 Mbps, what is the theoretical maximum bottleneck throughput?
- A) 100 Mbps
- B) 40.5 Mbps
- C) 162 Mbps
- D) 2 Mbps
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
End-to-end throughput is bounded by the bottleneck link: $\min(10, 100, 2, 50) = 2\text{ Mbps}$.
</details>

---

### Hard (Questions 21–30)

#### Q21. [GATE-style] A message of size $M = 10^6\text{ bits}$ is transmitted across 3 identical links ($N=3$) of rate $R = 1\text{ Mbps}$. If the message is segmented into 1,000 packets of 1,000 bits each (ignore headers and propagation delay), what is the total packet switching delay?
- A) 1.002 s
- B) 3.000 s
- C) 0.500 s
- D) 2.004 s
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Formula: $T = (k + N - 1) \frac{L}{R}$.  
$T_t$ per packet = $\frac{1000}{10^6} = 0.001\text{ s}$.  
$T = (1000 + 3 - 1) \times 0.001 = 1002 \times 0.001 = 1.002\text{ s}$.  
(Compare to message switching which takes $3 \times 1\text{ s} = 3.000\text{ s}$).
</details>

#### Q22. [GATE-style] A link has distance $d = 1000\text{ km}$ and propagation velocity $v = 2 \times 10^8\text{ m/s}$. For what packet size will the transmission delay equal the propagation delay if the link bandwidth is 100 Mbps?
- A) 5,000 bytes
- B) 125,000 bytes
- C) 62,500 bytes
- D) 50,000 bytes
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
$T_p = \frac{10^6\text{ m}}{2 \times 10^8\text{ m/s}} = 0.005\text{ s} = 5\text{ ms}$.  
We want $T_t = \frac{L}{R} = 0.005\text{ s} \implies L = 0.005 \times 10^8 = 500,000\text{ bits}$.  
In bytes: $\frac{500,000}{8} = 62,500\text{ bytes}$.
</details>

#### Q23. [Company] Why is statistical multiplexing more efficient than Frequency Division Multiplexing (FDM) for packet networks?
- A) FDM dedicates a fixed frequency band to each user regardless of activity, leaving idle bands wasted
- B) Statistical multiplexing requires complex optical modulation hardware at every endpoint
- C) FDM introduces high packet reordering overhead in the operating system kernel
- D) Statistical multiplexing completely eliminates the need for queuing memory in routers
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
FDM statically allocates spectrum. If a user is not actively typing or downloading, their allocated slice sits idle. Statistical multiplexing dynamically allocates bandwidth on demand.
</details>

#### Q24. [GATE-style] In Store-and-Forward packet switching, what does the switch do before transmitting a packet onto the outgoing link?
- A) Transmits the first bit immediately upon reading the destination address
- B) Waits until all bits of the packet arrive, verifies the checksum, then begins transmission
- C) Establishes an end-to-end circuit reservation to the final destination host
- D) Compresses the payload using Huffman coding to double link throughput
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Store-and-forward means the entire packet must be received into buffer memory and checked for transmission errors before the first bit is forwarded onto the next hop.
</details>

#### Q25. [Concept] A company operates 10 regional data centers. Switching from a Full Mesh to a Hub-and-Spoke (Star) topology reduces the number of dedicated links from:
- A) 90 to 10
- B) 45 to 9
- C) 45 to 10
- D) 100 to 10
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
In a full mesh of 10 nodes, links = $\frac{10 \times 9}{2} = 45$. In a hub-and-spoke where 1 node is chosen as the central hub and the other 9 connect to it, links = 9. (If a dedicated external switch is added as a star center, links = 10). Both reduce cables dramatically.
</details>

#### Q26. [Company] In modern fiber networks, why does increasing bandwidth from 1 Gbps to 10 Gbps have negligible effect on the round-trip latency of an HTTP handshake between New York and London?
- A) The transatlantic fiber is already saturated with queuing delays
- B) HTTP packets are too large to fit in 10 Gbps frames
- C) The transatlantic latency is overwhelmingly dominated by the speed-of-light propagation delay in optical fiber
- D) Tier-1 ISPs throttle all international traffic to 100 ms
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
Over 6,000 km, propagation delay $T_p \approx 30\text{ ms}$ (RTT $\approx 60\text{ ms}$). Small 64-byte TCP handshake packets have $T_t = 0.5\text{ }\mu\text{s}$ at 1 Gbps and $0.05\text{ }\mu\text{s}$ at 10 Gbps. A fraction of a microsecond is unnoticeable against 60,000 $\mu\text{s}$ of physical light propagation.
</details>

#### Q27. [GATE-style] In an optimal packet size calculation for minimizing total store-and-forward delay with fixed header overhead $h$, optimal payload size $p$ is proportional to:
- A) $\sqrt{M \cdot h}$
- B) $\frac{M \cdot h}{N - 1}$
- C) $M^2 \cdot h$
- D) $\frac{1}{\sqrt{M \cdot h}}$
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
From calculus derivation: $p_{\text{opt}} = \sqrt{\frac{M \cdot h}{N - 1}}$, which is proportional to $\sqrt{M \cdot h}$.
</details>

#### Q28. [Concept] Which organization administers the allocation of globally unique Autonomous System Numbers (ASNs) and IP address space?
- A) IEEE Standards Association
- B) ISO
- C) IETF
- D) IANA / ICANN
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
The Internet Assigned Numbers Authority (IANA), operated by ICANN, coordinates global IP address pools and ASNs.
</details>

#### Q29. [Company] Which of the following is considered an in-band control characteristic of packet switching?
- A) Separate physical telephone copper circuits manage signaling
- B) Control information (headers) and payload data travel within the exact same packet on the same physical link
- C) Operators manually switch patch cables during network outages
- D) Bandwidth is negotiated using DTMF dual-tone frequencies
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
In packet switching, control headers (IP, TCP) are embedded directly at the front of each data packet on the same communication channel.
</details>

#### Q30. [GATE-style] If a transmission link has a processing delay of 10 $\mu\text{s}$, a transmission delay of 1 ms, a propagation delay of 2 ms, and a queuing delay of 5 ms, what percentage of total delay is spent in the buffer queue?
- A) 62.4%
- B) 12.5%
- C) 25.0%
- D) 50.0%
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Total delay = $10\text{ }\mu\text{s} + 1\text{ ms} + 2\text{ ms} + 5\text{ ms} = 0.010 + 1 + 2 + 5 = 8.010\text{ ms}$.  
Queuing percentage = $\frac{5}{8.010} \times 100 \approx 62.42\%$.
</details>

---

## 🔢 Part B: Multiple Select Questions (MSQ — 1 to 4 Correct)

#### Q31. [GATE-style] Which of the following factors directly affect the Propagation Delay ($T_p$) of a network link?
- [ ] A) Physical distance between sender and receiver ($d$)
- [ ] B) Physical propagation speed of light/signals in the medium ($v$)
- [ ] C) Bandwidth capacity of the network interface ($R$)
- [ ] D) Packet size in bits ($L$)
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B**  
$T_p = d / v$. Distance and velocity are the only two factors. Bandwidth and packet size affect Transmission Delay ($T_t = L / R$).
</details>

#### Q32. [GATE-style] Which of the following are advantages of a Star topology over a Bus topology?
- [ ] A) Fault isolation: one severed cable does not disconnect other hosts
- [ ] B) Easier troubleshooting and port status monitoring via the central switch
- [ ] C) Complete elimination of all single points of failure in the network
- [ ] D) No signal reflection issues requiring terminating resistors
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, D**  
Star topologies offer fault isolation, switch monitoring, and no terminator requirements. However, option C is false because the central switch itself remains a single point of failure.
</details>

#### Q33. [Company] In which of the following scenarios does Circuit Switching provide an advantage over Packet Switching?
- [ ] A) Continuous, constant-bitrate audio/video streaming requiring guaranteed bandwidth
- [ ] B) Highly bursty web browsing traffic with long periods of silence
- [ ] C) Real-time mission-critical applications where unpredictable queuing jitter is unacceptable
- [ ] D) Large-scale networks with millions of intermittent, short-lived API requests
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, C**  
Circuit switching provides dedicated capacity and zero queuing delay/jitter. For bursty or short-lived traffic (B and D), packet switching is vastly superior.
</details>

#### Q34. [GATE-style] Which of the following components comprise total nodal packet latency in store-and-forward networks?
- [ ] A) Transmission delay ($L/R$)
- [ ] B) Propagation delay ($d/v$)
- [ ] C) Queuing delay ($T_q$)
- [ ] D) Nodal processing delay ($T_{\text{proc}}$)
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C, D**  
All four components sum to the total nodal delay: $D = T_t + T_p + T_q + T_{\text{proc}}$.
</details>

#### Q35. [Concept] Which of the following statements regarding the Bandwidth-Delay Product (BDP) are true?
- [ ] A) BDP represents the maximum number of bits that can be present on the link at any instant
- [ ] B) BDP is calculated as the product of link bandwidth and round-trip time ($R \times \text{RTT}$)
- [ ] C) A network with high bandwidth and high delay is referred to as a "Long Fat Network" (LFN)
- [ ] D) Increasing the physical length of the wire decreases BDP
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
A, B, and C are true. D is false because increasing physical distance increases propagation delay, which increases BDP.
</details>

#### Q36. [Company] Which of the following communication systems operate in Half-Duplex mode?
- [ ] A) Traditional push-to-talk Walkie-Talkies
- [ ] B) Legacy 10BASE2 coaxial Ethernet with CSMA/CD
- [ ] C) Full-duplex Gigabit switched Ethernet with Cat6 cabling
- [ ] D) Standard 802.11 Wi-Fi shared radio channels
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, D**  
Walkie-talkies, shared coaxial Ethernet, and 802.11 Wi-Fi all share a single frequency or wire and alternate transmissions. Modern switched Ethernet (C) is full duplex.
</details>

#### Q37. [GATE-style] Which of the following statements about Full Mesh topologies are correct?
- [ ] A) A full mesh of $n$ nodes requires $\frac{n(n-1)}{2}$ duplex links
- [ ] B) Every node requires $n-1$ physical I/O ports
- [ ] C) The failure of any single link disconnects the entire network
- [ ] D) Full mesh topologies scale efficiently to tens of thousands of corporate desktop computers
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B**  
A and B are standard formulas. C is false (mesh offers redundant alternate paths). D is false ($O(n^2)$ link explosion makes mesh impossible for desktop LANs).
</details>

#### Q38. [Concept] What causes packet loss at intermediate routers?
- [ ] A) Output buffer memory queues filling to capacity during congestion
- [ ] B) Electromagnetic noise or bit errors causing checksum verification failure
- [ ] C) Packets looping endlessly due to routing errors until their TTL expires
- [ ] D) Propagation velocity dropping below the speed of light in optical fiber
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
Buffer overflow (A), bit corruption (B), and TTL expiration (C) all cause packet drops. Propagation speed (D) is constant in a medium.
</details>

#### Q39. [Company] Which of the following characterize the Client-Server model?
- [ ] A) Centralized control and access management
- [ ] B) Servers typically have static, well-known IP addresses
- [ ] C) If the central server crashes, clients cannot access the service unless redundancy exists
- [ ] D) Clients communicate directly with one another without contacting the server
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
A, B, and C describe client-server. D describes P2P systems.
</details>

#### Q40. [GATE-style] In Datagram Packet Switching, which of the following are true?
- [ ] A) Each packet contains full source and destination IP addresses in its header
- [ ] B) Consecutive packets of the same file may follow completely different paths across intermediate routers
- [ ] C) Packets are guaranteed to arrive in the exact order they were sent
- [ ] D) Intermediate routers make independent forwarding decisions per packet based on their routing table
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, D**  
Datagram routing is connectionless and independent. Out-of-order arrival is possible, making C false.
</details>

---

## 🔢 Part C: Numerical Answer Type (NAT)

#### Q41. [GATE-style] A 100 KB file ($1\text{ KB} = 1000\text{ bytes}$) is sent over a 1 Mbps point-to-point link. The transmission delay in milliseconds is ________.
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 800**  
$L = 100 \times 1000 \times 8 = 800,000\text{ bits}$.  
$R = 1,000,000\text{ bps}$.  
$T_t = \frac{800,000}{1,000,000} = 0.8\text{ s} = 800\text{ ms}$.
</details>

#### Q42. [GATE-style] A signal propagates along a 400 km optical fiber with velocity $v = 2 \times 10^8\text{ m/s}$. The propagation delay in milliseconds is ________.
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 2**  
$d = 400,000\text{ m}$.  
$T_p = \frac{400,000}{2 \times 10^8} = 0.002\text{ s} = 2\text{ ms}$.
</details>

#### Q43. [GATE-style] In a full mesh network connecting 16 routers, the total number of duplex physical links is ________.
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 120**  
$N_{\text{links}} = \frac{16 \times 15}{2} = 120$.
</details>

#### Q44. [GATE-style] A communication pipe has a bandwidth of 10 Mbps and a one-way propagation delay of 25 ms. The Bandwidth-Delay Product of this channel in bits is ________.
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 250000**  
$\text{BDP} = 10 \times 10^6\text{ bps} \times 0.025\text{ s} = 250,000\text{ bits}$.
</details>

#### Q45. [GATE-style] A message is broken into 100 packets. The packets are transmitted across 4 store-and-forward links. The transmission delay for each packet on each link is 1 ms. Ignoring propagation and queuing delays, the total time to deliver all packets to the destination is ________ ms.
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 103**  
Formula: $T = (k + N - 1) T_t = (100 + 4 - 1) \times 1\text{ ms} = 103\text{ ms}$.
</details>

#### Q46. [GATE-style] A link has a transmission capacity of 100 Mbps. A packet of 1250 bytes is transmitted. The transmission delay in microseconds ($\mu\text{s}$) is ________.
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 100**  
$L = 1250 \times 8 = 10,000\text{ bits}$.  
$T_t = \frac{10,000}{10^8} = 10^{-4}\text{ s} = 100\text{ }\mu\text{s}$.
</details>

#### Q47. [GATE-style] For a link with propagation velocity $v = 2 \times 10^8\text{ m/s}$ and bandwidth $R = 10\text{ Mbps}$, the physical length of the link in kilometers such that $T_p = 5\text{ ms}$ is ________ km.
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 1000**  
$d = T_p \times v = 0.005\text{ s} \times (2 \times 10^8\text{ m/s}) = 1,000,000\text{ m} = 1,000\text{ km}$.
</details>

#### Q48. [GATE-style] In an office of 12 computers, replacing a Bus topology with a Full Mesh topology increases the number of required physical cables from 1 to ________.
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 66**  
Full mesh links for 12 nodes: $\frac{12 \times 11}{2} = 66$.
</details>

#### Q49. [GATE-style] A packet stream delivers 960 bytes of user data payload inside 1000-byte packets over an 80 Mbps link. The resulting goodput in Mbps is ________.
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 76.8**  
$\text{Goodput} = 80\text{ Mbps} \times \frac{960}{1000} = 76.8\text{ Mbps}$.
</details>

#### Q50. [GATE-style] A 1 MB ($10^6$ bytes) file is transmitted using circuit switching. Circuit setup takes 150 ms, teardown takes 50 ms, link rate is 20 Mbps, and total propagation delay is 10 ms. The total elapsed time in milliseconds is ________ ms.
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 610**  
$T_t = \frac{10^6 \times 8}{20 \times 10^6} = 0.4\text{ s} = 400\text{ ms}$.  
$T_{\text{total}} = T_{\text{setup}} + T_t + T_p + T_{\text{teardown}} = 150 + 400 + 10 + 50 = 610\text{ ms}$.
</details>

---

## 🛠️ Part D: Scenario & Output-Based Questions

#### Q51. [Scenario] A network administrator pings a server 100 meters away across an office LAN and observes an RTT of 0.2 ms. Later, the admin pings a server located 8,000 km away across an ocean and observes an RTT of 82 ms. What explains this 410-fold increase in latency?
- A) The transatlantic router is dropping 90% of packets due to CRC checksum mismatches
- B) Physical propagation delay ($T_p = d/v$) through 8,000 km of optical fiber dictates a minimum round-trip physical light travel time of ~80 ms
- C) The local LAN uses circuit switching while the transatlantic link uses message switching
- D) DNS servers must be queried on every single ICMP ping echo packet
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
In fiber optic glass, light travels at $\approx 200,000\text{ km/s}$. Over an 8,000 km path, one-way propagation is $\frac{8,000}{200,000} = 0.040\text{ s} = 40\text{ ms}$, creating a physical round trip of $\approx 80\text{ ms}$. No amount of bandwidth upgrade can bypass this speed-of-light limit.
</details>

#### Q52. [Scenario] During a live video call, audio sounds choppy and robotic, yet a file download occurring in the background runs at full 50 Mbps speed. Which network impairment is affecting the audio?
- A) High Jitter (latency variance) causing buffer starvation in the voice decoder
- B) Fiber optic cable attenuation reducing audio frequencies
- C) The LAN switch converting to half-duplex mode
- D) The client-server model failing to resolve DNS records
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
File downloads use TCP and rely on raw throughput; arrival timing variance does not hurt downloads. Real-time audio (VoIP) requires deterministic packet inter-arrival times; high jitter causes the jitter buffer to underflow, resulting in clipped or robotic speech.
</details>

#### Q53. [Scenario] An engineer notices that adding 20 new workstations to an old coaxial 10BASE2 bus network causes the overall network throughput to collapse almost to zero. What physical phenomenon is occurring?
- A) Token exhaustion
- B) Packet reassembly timeout in the router CPU
- C) Excessive CSMA/CD collisions on the shared electrical bus causing exponential backoffs
- D) Bandwidth-Delay Product exceeding the TCP window limit
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
A coaxial bus is a single shared collision domain. As host count rises, the probability of two devices sensing an idle channel and transmitting simultaneously explodes. Frequent collisions trigger jam signals and exponential backoffs, collapsing throughput.
</details>

#### Q54. [Scenario] A company replaces an unmanaged hub with an Ethernet switch. What immediate architectural change happens to the local collision domains?
- A) The entire building merges into a single collision domain
- B) Each individual switch port becomes its own isolated collision domain
- C) The broadcast domain is divided into 24 separate subnets
- D) The network converts from star topology to full mesh
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Hubs repeat signals to all ports (1 shared collision domain). Switches inspect MAC addresses and buffer frames, isolating each port into its own collision domain and enabling collision-free full-duplex operation.
</details>

#### Q55. [Scenario] The output of an interface status command shows:
```text
GigabitEthernet0/1 is up, line protocol is up
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec
  Encapsulation ARPA, loopback not set
  Full-duplex, 1000Mb/s, link type is force-up, media type is 1000BaseTX
```
What is confirmed about this link?
- A) It is running in half-duplex mode with CSMA/CD enabled
- B) It can transmit and receive simultaneously at 1 Gbps without collisions
- C) Its propagation delay is fixed at 1500 milliseconds
- D) The physical cable length is exactly 10 kilometers
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
The output clearly states `Full-duplex, 1000Mb/s` (Gigabit Ethernet). In full duplex, separate transmit and receive wire pairs eliminate collisions entirely.
</details>

---

## 📊 Part A Answer Key & Statistics

| Q# | Answer | Q# | Answer | Q# | Answer |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | C | **11** | B | **21** | A |
| **2** | A | **12** | B | **22** | C |
| **3** | B | **13** | C | **23** | A |
| **4** | D | **14** | B | **24** | B |
| **5** | A | **15** | B | **25** | B |
| **6** | C | **16** | C | **26** | C |
| **7** | B | **17** | A | **27** | A |
| **8** | C | **18** | C | **28** | D |
| **9** | A | **19** | B | **29** | B |
| **10** | B | **20** | D | **30** | A |

### Answer Key Distribution (Part A)
- **Option A:** 8 / 30 (26.7%)
- **Option B:** 8 / 30 (26.7%)
- **Option C:** 7 / 30 (23.3%)
- **Option D:** 7 / 30 (23.3%)
*Perfect balance (~25% each), eliminating test-taking guessing bias!*

---

## 🏆 Score Interpretation

| Score | Rating | Action Plan |
|---|---|---|
| **50–55** | 🌟 Expert / GATE Ranker | Outstanding fundamentals. Proceed to [02_OSI_Model](../02_OSI_Model/notes.md). |
| **42–49** | 🚀 Solid Foundation | Good conceptual grasp. Review BDP and store-and-forward pipelining formulas. |
| **32–41** | 📈 Intermediate | Review delay components ($T_t$ vs. $T_p$) in [notes.md](notes.md) and retry NAT questions. |
| **< 32** | 🔄 Novice | Re-read [notes.md](notes.md), study the visual timelines in [diagrams.md](diagrams.md), and solve Level 1 numericals. |
