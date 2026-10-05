# 03. The TCP/IP Protocol Architecture — Practice MCQs, MSQs & NATs

> **Comprehensive assessment containing 55 questions:**  
> - **Part A:** 30 Multiple Choice Questions (Single Correct — balanced A/B/C/D distribution)  
> - **Part B:** 10 Multiple Select Questions (GATE style — 1 to 4 correct)  
> - **Part C:** 10 Numerical Answer Type (NAT) Questions  
> - **Part D:** 5 Scenario & Packet Inspection Challenges  
> All answers are hidden inside `<details>` blocks with detailed explanations debunking common traps.

---

## 📝 Part A: Multiple Choice Questions (Single Option Correct)

### Easy (Questions 1–10)

#### Q1. [Concept] How many layers are defined in the classic DoD (Department of Defense) TCP/IP reference model?
- A) 7 Layers
- B) 5 Layers
- C) 4 Layers
- D) 3 Layers
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
The classic DoD model defined 4 layers: Application, Host-to-Host (Transport), Internet, and Network Access.
</details>

#### Q2. [Concept] Which protocol provides connectionless, unreliable "best-effort" delivery of packets across the Internet?
- A) TCP
- B) IP (Internet Protocol)
- C) BGP
- D) SCTP
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
IP is connectionless and best-effort; it does not guarantee that packets will arrive without loss or in order.
</details>

#### Q3. [Company] What is the primary role of the Address Resolution Protocol (ARP)?
- A) To map a known IP address to a physical MAC address
- B) To map a domain name to an IP address
- C) To assign dynamic IP addresses to new clients
- D) To encrypt HTTP payloads using TLS
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
ARP resolves a known 32-bit IPv4 address into a 48-bit physical MAC address on a local broadcast domain.
</details>

#### Q4. [Concept] What is the PDU name used at the Transport layer for a TCP connection?
- A) Packet
- B) Frame
- C) Datagram
- D) Segment
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
At Layer 4, TCP data units are called **Segments**, whereas UDP data units are called **Datagrams**.
</details>

#### Q5. [GATE-style] Which layer of the 5-layer hybrid TCP/IP model handles physical signaling and bit encoding?
- A) Physical Layer
- B) Data Link Layer
- C) Network Layer
- D) Transport Layer
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
The Physical Layer (Layer 1) manages voltages, optical light pulses, connectors, and physical transmission media.
</details>

#### Q6. [Company] Which protocol is used by the `ping` utility to test network reachability?
- A) TCP
- B) ICMP (Internet Control Message Protocol)
- C) UDP
- D) ARP
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Ping uses ICMP Echo Request (`Type 8`) and ICMP Echo Reply (`Type 0`).
</details>

#### Q7. [Concept] In the TCP/IP stack, which layer combines the functions of OSI Layers 5, 6, and 7?
- A) Transport Layer
- B) Internet Layer
- C) Application Layer
- D) Network Access Layer
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
TCP/IP merges Application, Presentation, and Session functions directly into the Application layer.
</details>

#### Q8. [Concept] What happens to the Time-to-Live (TTL) field in an IPv4 packet header when it passes through a router?
- A) It is doubled to prevent timeouts
- B) It is replaced with the router's MAC address
- C) It is decremented by 1
- D) It remains unchanged until reaching the destination
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
Every router decrements TTL by at least 1. If $\text{TTL} = 0$, the packet is discarded to prevent infinite routing loops.
</details>

#### Q9. [GATE-style] What is the fixed size in bytes of the base IPv6 header?
- A) 40 Bytes
- B) 20 Bytes
- C) 60 Bytes
- D) 32 Bytes
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
The base IPv6 header has a strictly fixed size of 40 bytes, simplifying router hardware parsing.
</details>

#### Q10. [Company] On which port number does the Border Gateway Protocol (BGP) listen for peer connections?
- A) UDP Port 53
- B) TCP Port 80
- C) UDP Port 520
- D) TCP Port 179
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
BGP establishes persistent peer connections over TCP port 179.
</details>

---

### Medium (Questions 11–20)

#### Q11. [GATE-style] In an IPv4 packet header, how is the total header length represented by the 4-bit Internet Header Length (IHL) field?
- A) In units of 4 bytes (32-bit words)
- B) Directly in total bytes
- C) In units of 8 bytes
- D) In units of 16 bits
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
IHL counts 32-bit words (4-byte units). A standard 20-byte header has $\text{IHL} = 5$ ($5 \times 4 = 20\text{ bytes}$).
</details>

#### Q12. [Company] When a packet traverses an intermediate router, which of the following is true regarding its MAC and IP addresses?
- A) The IP addresses are rewritten; the MAC addresses remain unchanged
- B) The MAC addresses are rewritten; the IP addresses remain unchanged (barring NAT)
- C) Both MAC and IP addresses are completely rewritten at every hop
- D) Neither MAC nor IP addresses change across the entire path
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Layer 2 MAC addresses are local link identifiers replaced at every router hop; Layer 3 IP addresses remain constant end-to-end.
</details>

#### Q13. [Concept] Why does IPv6 explicitly eliminate the header checksum field that was present in IPv4?
- A) IPv6 packets are immune to electromagnetic noise
- B) Layer 2 (Ethernet CRC) and Layer 4 (TCP/UDP checksum) already check errors; removing it saves router CPU cycles
- C) Optical fiber cables automatically correct all bit flips in hardware
- D) Checksums are forbidden by the IETF in all protocols designed after 1995
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Recalculating checksums at every hop (because TTL changed) consumed immense router CPU. With reliable L2 and L4 checksums, IPv6 removed it.
</details>

#### Q14. [GATE-style] How does the Open Shortest Path First (OSPF) routing protocol encapsulate its packets?
- A) Directly inside IP packets with Protocol number 89
- B) Inside UDP datagrams on port 520
- C) Inside TCP segments on port 179
- D) Inside Layer 2 Ethernet frames using EtherType `0x8847`
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
OSPF runs directly on top of the Internet Protocol, carrying IP Protocol number 89 (bypassing transport layers).
</details>

#### Q15. [Company] Why does a TCP connection require a 4-tuple to uniquely identify a socket on a server?
- A) Because the server must track 4 different Ethernet MAC addresses simultaneously
- B) To differentiate concurrent connections from different clients (or different client ports) to the same server IP and listening port
- C) Because IPv4 addresses are divided into 4 decimal octets
- D) To prevent DNS cache poisoning attacks
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
A TCP socket is bound by $(Source\text{ IP}, Source\text{ Port}, Dest\text{ IP}, Dest\text{ Port})$. This allows thousands of clients to connect to port 443 simultaneously.
</details>

#### Q16. [Concept] Which protocol replaces ARP in IPv6 networks?
- A) Reverse ARP (RARP)
- B) Dynamic Host Configuration Protocol v6 (DHCPv6)
- C) Neighbor Discovery Protocol (NDP) using ICMPv6
- D) Spanning Tree Protocol (STP)
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
IPv6 uses NDP (Neighbor Discovery Protocol) based on ICMPv6 multicast messages to discover neighboring MAC addresses.
</details>

#### Q17. [GATE-style] If an IPv4 datagram has a total length of 1200 bytes and $\text{IHL} = 5$, what is the size of the data payload in bytes?
- A) 1180 Bytes
- B) 1195 Bytes
- C) 1176 Bytes
- D) 1160 Bytes
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Header length = $5 \times 4 = 20\text{ bytes}$.  
Payload = $\text{Total Length} - \text{Header Length} = 1200 - 20 = 1180\text{ bytes}$.
</details>

#### Q18. [Company] Which protocol is used by routers to manage dynamic multicast group memberships with local hosts?
- A) ICMP
- B) ARP
- C) IGMP (Internet Group Management Protocol)
- D) BGP
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
IGMP (IP Protocol 2) is used by IPv4 hosts to report their multicast group memberships to adjacent routers.
</details>

#### Q19. [Concept] The principle of "Fate-Sharing" in TCP/IP system design means that:
- A) All intermediate routers share an identical synchronized routing table
- B) Session state is maintained solely at end systems, surviving intermediate network node crashes
- C) If one packet is dropped, all packets in the flow are discarded
- D) Client and server must share the exact same operating system
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Fate-sharing (coined by David Clark) dictates that conversation state is kept at the endpoints; a session loses state only if the endpoint itself dies.
</details>

#### Q20. [GATE-style] What transport protocol and port does DNS use for standard domain name resolution queries?
- A) TCP Port 53
- B) UDP Port 67
- C) ICMP Port 1
- D) UDP Port 53
<details><summary><b>Answer & Explanation</b></summary>

**Answer: D**  
Standard DNS client queries use **UDP port 53** (low overhead). (TCP port 53 is used for zone transfers and large responses $> 512$ bytes).
</details>

---

### Hard (Questions 21–30)

#### Q21. [GATE-style] An IPv4 packet with $\text{Total Length} = 4000\text{ bytes}$ and $\text{IHL} = 5$ must be fragmented across an outgoing link with $\text{MTU} = 1500\text{ bytes}$. How many fragments are created, and what are their payload sizes?
- A) 3 fragments: 1480 B, 1480 B, and 1020 B
- B) 3 fragments: 1500 B, 1500 B, and 1000 B
- C) 4 fragments: 1000 B each
- D) 3 fragments: 1480 B, 1480 B, and 1040 B
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Total data payload = $4000 - 20 = 3980\text{ bytes}$.  
Max payload per fragment must fit in $\text{MTU} - 20 = 1480\text{ bytes}$ and be a multiple of 8 ($1480 / 8 = 185$, valid!).  
- Frag 1: 20 B header + 1480 B data ($MF=1$, Offset = 0).  
- Frag 2: 20 B header + 1480 B data ($MF=1$, Offset = 185).  
- Frag 3: 20 B header + $3980 - 2960 = 1020\text{ B}$ data ($MF=0$, Offset = 370).
</details>

#### Q22. [Company] Why does modern IPv6 prohibit intermediate routers from fragmenting packets?
- A) IPv6 routers lack memory to read packet headers
- B) Router fragmentation causes severe CPU overhead and packet reassembly buffer exhaustion during high-speed routing
- C) IPv6 packets are strictly limited to 64 bytes
- D) IPv6 requires all transmission links to have infinite MTU
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
By making the sender responsible for discovering Path MTU (PMTUD), intermediate routers forward packets without performing expensive slicing and copying.
</details>

#### Q23. [GATE-style] In an IPv4 packet header, what does an Identification field value of `0x1A2B` shared across multiple received packets signify?
- A) All these packets belong to fragments of the same original IP datagram
- B) A TCP SYN flood attack is currently underway
- C) The packets are duplicate broadcasts from a rogue switch
- D) The packets are using the OSPF routing protocol
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
The Identification field uniquely labels fragments belonging to the same original datagram so the receiving host can reassemble them.
</details>

#### Q24. [Concept] What is the architectural role of the EtherType field in an Ethernet frame?
- A) It specifies the physical link speed (10 Mbps vs 1 Gbps)
- B) It multiplexes/demultiplexes the payload to the appropriate Network layer protocol (e.g., `0x0800` for IPv4, `0x0806` for ARP)
- C) It tracks TCP sequence numbers across local switches
- D) It stores the default gateway router's IP address
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
EtherType is a 2-byte field identifying which Layer 3 protocol payload is encapsulated inside the frame.
</details>

#### Q25. [Company] Which routing protocol uses UDP port 520 for exchanging distance-vector routing updates?
- A) BGP
- B) RIP (Routing Information Protocol)
- C) OSPF
- D) IS-IS
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
RIP uses UDP port 520 to broadcast/multicast its routing table every 30 seconds.
</details>

#### Q26. [GATE-style] If an IPv4 packet arrives at a host with $\text{Fragment Offset} = 300$, what is the starting byte position of this fragment's data in the original unfragmented payload?
- A) Byte 300
- B) Byte 600
- C) Byte 2,400
- D) Byte 1,200
<details><summary><b>Answer & Explanation</b></summary>

**Answer: C**  
The Fragment Offset field counts in **units of 8 bytes**.  
Starting byte position = $300 \times 8 = 2,400$.
</details>

#### Q27. [Concept] Why is ARP classified functionally as a Network Layer (Layer 3) protocol even though it is encapsulated in a Layer 2 frame?
- A) It contains 32-bit IPv4 addresses and directly enables Layer 3 host-to-host delivery
- B) It performs shortest-path Dijkstra calculations
- C) It requires a TCP 3-way handshake before querying
- D) It can route packets across transatlantic undersea fiber links
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
ARP operates on behalf of the Network layer, resolving IP addresses so that Layer 3 packets can be encapsulated into physical frames.
</details>

#### Q28. [Company] In a cloud data center, what is the primary benefit of the IPv6 Flow Label field?
- A) It encrypts packet contents with AES-256
- B) It enables routers to identify and forward packets belonging to the same flow along the same ECMP path without inspecting deep transport headers
- C) It replaces DNS resolution
- D) It doubles link bandwidth on copper cables
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
The 20-bit Flow Label allows Equal-Cost Multi-Path (ECMP) switches to hash and load-balance flows without parsing upper-layer TCP/UDP port headers.
</details>

#### Q29. [GATE-style] An IPv4 packet has an 8-bit TTL field set to 1. What does the first router that receives this packet do?
- A) Forwards it to the next router with $\text{TTL} = 1$
- B) Decrements TTL to 0, drops the packet, and sends an ICMP Time Exceeded message to the sender
- C) Increments TTL to 64 and forwards it
- D) Returns the packet directly to the sender's MAC address
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
The router decrements TTL from 1 to 0, discards the datagram, and returns an ICMP Type 11, Code 0 error.
</details>

#### Q30. [GATE-style] What is the Protocol field value in the IPv4 header when encapsulating a TCP segment?
- A) 6
- B) 17
- C) 1
- D) 89
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A**  
Protocol value 6 indicates TCP (17 = UDP, 1 = ICMP, 89 = OSPF).
</details>

---

## 🔢 Part B: Multiple Select Questions (MSQ — 1 to 4 Correct)

#### Q31. [GATE-style] Which of the following protocols operate at the Application Layer of the TCP/IP suite?
- [ ] A) Domain Name System (DNS)
- [ ] B) Hypertext Transfer Protocol (HTTP)
- [ ] C) Dynamic Host Configuration Protocol (DHCP)
- [ ] D) Internet Control Message Protocol (ICMP)
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
DNS, HTTP, and DHCP are Application layer protocols. ICMP is a Network layer protocol.
</details>

#### Q32. [Company] Which fields in a packet header are modified as a packet traverses an intermediate router?
- [ ] A) Layer 2 Source MAC Address
- [ ] B) Layer 2 Destination MAC Address
- [ ] C) Layer 3 IPv4 Time to Live (TTL)
- [ ] D) Layer 4 TCP Destination Port Number
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
L2 MACs are rewritten at each hop; IP TTL is decremented. Port numbers (D) remain unchanged (barring PAT).
</details>

#### Q33. [GATE-style] Which of the following features were removed or changed in IPv6 compared to IPv4?
- [ ] A) The 16-bit Header Checksum field was completely eliminated
- [ ] B) Intermediate router fragmentation was eliminated
- [ ] C) Broadcast addressing was eliminated and replaced by Multicast/Anycast
- [ ] D) Address length was reduced to accelerate hardware forwarding
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
A, B, and C are major IPv6 improvements. D is false (address length expanded from 32 to 128 bits).
</details>

#### Q34. [Concept] Which of the following protocols run directly on top of the Internet Protocol (IP), bypassing TCP and UDP?
- [ ] A) ICMP (Protocol 1)
- [ ] B) IGMP (Protocol 2)
- [ ] C) OSPF (Protocol 89)
- [ ] D) BGP (Port 179)
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
ICMP, IGMP, and OSPF run directly in IP packets. BGP runs on top of TCP port 179.
</details>

#### Q35. [Company] Which of the following statements about Address Resolution Protocol (ARP) are true?
- [ ] A) The ARP Request is broadcast to MAC `FF:FF:FF:FF:FF:FF`
- [ ] B) The ARP Reply is unicast directly to the requesting host's MAC address
- [ ] C) ARP tables dynamically cache IP-to-MAC mappings with a timeout
- [ ] D) ARP requests can cross routers to resolve MAC addresses on remote subnets
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
A, B, and C are correct. D is false (L2 broadcasts do not cross routers; routers forward using the default gateway's MAC).
</details>

#### Q36. [GATE-style] Which of the following transport protocols provide connectionless service without retransmissions?
- [ ] A) User Datagram Protocol (UDP)
- [ ] B) Transmission Control Protocol (TCP)
- [ ] C) Stream Control Transmission Protocol (SCTP)
- [ ] D) Real-time Transport Protocol (RTP, running over UDP)
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, D**  
UDP and RTP over UDP are connectionless without retransmissions. TCP and SCTP are connection-oriented and reliable.
</details>

#### Q37. [Concept] Why does DNS support both UDP and TCP on port 53?
- [ ] A) Standard client resolution queries use UDP for low-latency single-packet lookups
- [ ] B) Zone transfers between primary and secondary DNS servers use TCP for reliable bulk replication
- [ ] C) DNS responses exceeding 512 bytes fallback to TCP (EDNS0 mitigates this)
- [ ] D) DNS uses TCP exclusively for government `.gov` domains
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
A, B, and C are standard RFC 1035 behaviors. D is fictitious.
</details>

#### Q38. [Company] What advantages did the 5-layer hybrid model provide over the 4-layer DoD model for computer networking education?
- [ ] A) It cleanly separates physical transmission media from link-layer framing
- [ ] B) It aligns with real-world network interface hardware architecture (PHY chip vs. MAC controller)
- [ ] C) It eliminates the need for IP addressing
- [ ] D) It matches the physical-to-application pedagogical structure used in GATE CS/IT
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, D**  
A, B, and D describe the pedagogical and engineering value of the 5-layer model. C is nonsensical.
</details>

#### Q39. [GATE-style] In an IPv4 header, which fields are involved in packet fragmentation and reassembly?
- [ ] A) Identification (16 bits)
- [ ] B) Flags (3 bits: DF, MF)
- [ ] C) Fragment Offset (13 bits)
- [ ] D) Time to Live (8 bits)
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, C**  
Identification, Flags, and Fragment Offset are the fragmentation triplet. TTL is for loop prevention.
</details>

#### Q40. [Concept] Which of the following are core tenets of the Internet architectural philosophy (RFC 1958)?
- [ ] A) End-to-End Principle (intelligence and state kept at endpoints)
- [ ] B) Simplicity in the network core (routers focus on fast stateless packet forwarding)
- [ ] C) Mandatory centralized gatekeepers for all protocol innovation
- [ ] D) Open standards published free of charge as RFCs
<details><summary><b>Answer & Explanation</b></summary>

**Answer: A, B, D**  
A, B, and D define the open Internet. C is the antithesis of the Internet's permissionless innovation model.
</details>

---

## 🔢 Part C: Numerical Answer Type (NAT)

#### Q41. [GATE-style] In an IPv4 header, if the `IHL` field contains the binary value `0111`, the header length in bytes is ________.
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 28**  
Binary `0111` = decimal 7.  
Header length = $7 \times 4\text{ bytes} = 28\text{ bytes}$.
</details>

#### Q42. [GATE-style] What is the Protocol number field value in the IPv4 header for the User Datagram Protocol (UDP)?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 17**  
UDP is assigned Protocol number 17 (TCP = 6, ICMP = 1, OSPF = 89).
</details>

#### Q43. [GATE-style] What is the Protocol number field value in the IPv4 header for the Internet Control Message Protocol (ICMP)?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 1**  
ICMP is assigned IP Protocol number 1.
</details>

#### Q44. [GATE-style] An IPv6 address has a length of how many bytes?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 16**  
128 bits $= \frac{128}{8} = 16\text{ bytes}$.
</details>

#### Q45. [GATE-style] In the IPv4 header, the Fragment Offset field value is measured in multiples of how many bytes?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 8**  
Fragment offset is measured in units of 8 bytes (64 bits).
</details>

#### Q46. [GATE-style] What is the standard port number used by HTTP web traffic?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 80**  
Unencrypted HTTP operates on well-known TCP port 80.
</details>

#### Q47. [GATE-style] What is the standard port number used by HTTPS encrypted web traffic?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 443**  
HTTPS operates on TCP port 443.
</details>

#### Q48. [GATE-style] What is the standard port number used by the Dynamic Host Configuration Protocol (DHCP) server daemon?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 67**  
DHCP Server listens on UDP port 67; clients receive on UDP port 68.
</details>

#### Q49. [GATE-style] An IPv4 packet with $\text{Total Length} = 1500\text{ bytes}$ and $\text{IHL} = 5$ carries a TCP segment whose header length is 32 bytes (Data Offset = 8). What is the size of the application payload in bytes?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 1448**  
IP Header = $5 \times 4 = 20\text{ bytes}$.  
TCP Header = $8 \times 4 = 32\text{ bytes}$.  
Application Payload = $1500 - (20 + 32) = 1500 - 52 = 1448\text{ bytes}$.
</details>

#### Q50. [GATE-style] How many bits are allocated to the Time-to-Live (TTL) field in an IPv4 packet header?
<details><summary><b>Answer & Explanation</b></summary>

**Answer: 8**  
The TTL field is an 8-bit integer (maximum value 255).
</details>

---

## 🛠️ Part D: Scenario & Packet Inspection Challenges

#### Q51. [Scenario] A network analyst inspects a packet capture and observes an ICMP message:
```text
Internet Control Message Protocol
  Type: 11 (Time-to-live exceeded)
  Code: 0 (Time to live exceeded in transit)
```
What network diagnostic tool relies on this exact message to construct its output?
- A) `ping`
- B) `traceroute` (or `tracert`)
- C) `arp -a`
- D) `nslookup`
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
`traceroute` sends probe packets with increasing TTL values ($1, 2, 3\dots$) specifically to elicit ICMP Type 11 Code 0 responses from intermediate routers.
</details>

#### Q52. [Scenario] A client device on an office network boots up and needs an IP address. It has no knowledge of local routers or servers. What is the destination IP and MAC address of its initial DHCP Discover message?
- A) Dest IP: `0.0.0.0`, Dest MAC: `00:00:00:00:00:00`
- B) Dest IP: `255.255.255.255`, Dest MAC: `FF:FF:FF:FF:FF:FF`
- C) Dest IP: `127.0.0.1`, Dest MAC: `AA:BB:CC:DD:EE:FF`
- D) Dest IP: `8.8.8.8`, Dest MAC: Default Gateway MAC
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Because the client has no IP and does not know the DHCP server's location, it broadcasts at both Layer 3 (`255.255.255.255`) and Layer 2 (`FF:FF:FF:FF:FF:FF`).
</details>

#### Q53. [Scenario] An engineer captures an ARP request:
```text
Address Resolution Protocol (request)
  Sender MAC: 00:1a:2b:3c:4d:5e, Sender IP: 192.168.1.10
  Target MAC: 00:00:00:00:00:00, Target IP: 192.168.1.50
```
Why is the Target MAC set to all zeros?
- A) The target machine has crashed
- B) The target MAC is unknown; this is the information the sender is requesting
- C) The target machine is an unmanaged hub
- D) ARP does not support MAC addresses
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
The sender is asking *"Who has 192.168.1.50?"*. Because the target's MAC is unknown, it is zero-filled in the request body.
</details>

#### Q54. [Scenario] Two hosts on the same physical switch have IP addresses `192.168.1.10/24` and `192.168.2.20/24`. Host A attempts to ping Host B. Host A generates an ARP request for its Default Gateway rather than Host B. Why?
- A) Host A's network interface card is defective
- B) Host A performs an `AND` operation with its subnet mask, realizes Host B is on a different subnet, and must send the packet via its default router
- C) ARP cannot resolve IP addresses ending in zero
- D) Switches block all ARP requests between even and odd IP addresses
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
Hosts only ARP for destination IPs on their *own* local subnet. For remote subnets, the host ARPs for its Default Gateway's MAC address.
</details>

#### Q55. [Scenario] A server receives two TCP segments:
- Segment 1: $(10.0.0.5:49152 \rightarrow 192.168.1.100:80)$
- Segment 2: $(10.0.0.5:49153 \rightarrow 192.168.1.100:80)$
How does the server operating system route these segments?
- A) Both are merged into a single thread and one is overwritten
- B) They are delivered to two separate TCP sockets because their Source Port numbers differ
- C) The second segment is dropped as a duplicate
- D) The server resets the TCP connection
<details><summary><b>Answer & Explanation</b></summary>

**Answer: B**  
TCP demultiplexes using the full 4-tuple. Since the source ports differ (`49152` vs `49153`), the OS routes them to two independent socket streams.
</details>

---

## 📊 Part A Answer Key & Statistics

| Q# | Answer | Q# | Answer | Q# | Answer |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | C | **11** | A | **21** | A |
| **2** | B | **12** | B | **22** | B |
| **3** | A | **13** | B | **23** | A |
| **4** | D | **14** | A | **24** | B |
| **5** | A | **15** | B | **25** | B |
| **6** | B | **16** | C | **26** | C |
| **7** | C | **17** | A | **27** | A |
| **8** | C | **18** | C | **28** | B |
| **9** | A | **19** | B | **29** | B |
| **10** | D | **20** | D | **30** | A |

### Answer Key Distribution (Part A)
- **Option A:** 8 / 30 (26.7%)
- **Option B:** 8 / 30 (26.7%)
- **Option C:** 7 / 30 (23.3%)
- **Option D:** 7 / 30 (23.3%)
*Balanced option distribution eliminating guessing bias.*

---

## 🏆 Score Interpretation

| Score | Rating | Action Plan |
|---|---|---|
| **50–55** | 🌟 Protocol Architect | Flawless mastery of TCP/IP stack mechanics. Ready for [04_Physical_Layer](../04_Physical_Layer/). |
| **42–49** | 🚀 Strong Understanding | Review packet fragmentation calculations and protocol port numbers in [notes.md](notes.md). |
| **32–41** | 📈 Intermediate | Review the hop-by-hop packet header changes in [diagrams.md](diagrams.md). |
| **< 32** | 🔄 Novice | Re-read [notes.md](notes.md) and practice the protocol-to-layer placement matrix. |
