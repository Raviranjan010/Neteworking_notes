# 📖 Computer Networking A–Z Glossary

> A quick-lookup dictionary for networking terminology, acronyms, protocols, and concepts.  
> Every definition is concise (1–2 lines) and links to the relevant module.

---

## Navigation
[A](#a) | [B](#b) | [C](#c) | [D](#d) | [E](#e) | [F](#f) | [G](#g) | [H](#h) | [I](#i) | [J](#j) | [K](#k) | [L](#l) | [M](#m) | [N](#n) | [O](#o) | [P](#p) | [Q](#q) | [R](#r) | [S](#s) | [T](#t) | [U](#u) | [V](#v) | [W](#w) | [X](#x) | [Y](#y) | [Z](#z)

---

### A
- **ACK (Acknowledgment):** A control message or flag sent by a receiver to confirm that a data block, frame, or segment has been received correctly. See [11_Transport_Layer](11_Transport_Layer/notes.md).
- **ACL (Access Control List):** A sequential set of permit or deny rules applied to router or switch interfaces to filter traffic based on IP, port, or protocol. See [13_Network_Security](13_Network_Security/).
- **Address Resolution Protocol (ARP):** A network-layer protocol used to dynamically map a known 32-bit IPv4 address to a 48-bit physical MAC address on a local link. See [09_Network_Layer_Protocols](09_Network_Layer_Protocols/).
- **AD (Administrative Distance):** A numerical value (0–255) assigned to routing information sources by routers to prioritize the trustworthiness of competing routes. See [10_Routing](10_Routing/notes.md).
- **ALOHA:** An early pioneering random medium-access protocol developed at the University of Hawaii; exists as Pure ALOHA (max 18.4% efficiency) and Slotted ALOHA (max 36.8% efficiency). See [05_Data_Link_Layer](05_Data_Link_Layer/).
- **Anycast:** A network addressing and routing technique where a single destination IP address is assigned to multiple physical endpoints, and packets are routed to the nearest topological node via BGP. See [07_IP_Addressing](07_IP_Addressing/notes.md).
- **APIPA (Automatic Private IP Addressing):** The link-local IPv4 range `169.254.0.0/16` automatically self-assigned by an OS when DHCP discovery fails. See [07_IP_Addressing](07_IP_Addressing/notes.md).
- **Application Layer:** Layer 7 of the OSI model and Layer 4/5 of TCP/IP, providing network services directly to end-user applications (HTTP, DNS, SMTP, SSH). See [12_Application_Layer](12_Application_Layer/notes.md).
- **ARQ (Automatic Repeat reQuest):** An error-control protocol mechanism in data link and transport layers that automatically requests retransmission of missing or corrupted frames (Stop-and-Wait, Go-Back-N, Selective Repeat). See [05_Data_Link_Layer](05_Data_Link_Layer/).
- **AS (Autonomous System):** A collection of connected IP routing prefixes under the control of a single administrative entity with a common routing policy. See [10_Routing](10_Routing/notes.md).
- **Attenuation:** The reduction in amplitude or energy of a physical signal as it propagates across a transmission medium over distance, measured in decibels (dB). See [04_Physical_Layer](04_Physical_Layer/).

---

### B
- **Bandwidth:** In analog communications, the width of the frequency band (in Hz); in digital communications, the maximum theoretical data transfer rate of a channel (in bits per second). See [01_Fundamentals](01_Fundamentals/notes.md).
- **Bandwidth-Delay Product (BDP):** The product of link bandwidth and round-trip time ($B \times \text{RTT}$), representing the maximum amount of data in transit across the link at any instant. See [01_Fundamentals](01_Fundamentals/notes.md).
- **Baud Rate:** The number of signal state transitions or symbol changes occurring per second in a communication channel; distinct from bit rate when a symbol conveys multiple bits. See [04_Physical_Layer](04_Physical_Layer/).
- **Bellman-Ford Algorithm:** A dynamic programming algorithm used in distance-vector routing protocols (like RIP) to compute shortest paths from a single source node to all other nodes. See [10_Routing](10_Routing/notes.md).
- **BGP (Border Gateway Protocol):** The standardized path-vector exterior gateway protocol (EGP) used to exchange routing and reachability information between autonomous systems across the global Internet. See [10_Routing](10_Routing/notes.md).
- **Bit Stuffing:** A framing technique in data link protocols (such as HDLC) where a sender inserts a '0' bit after five consecutive '1' bits to prevent user data from mimicking the delimiter flag pattern `01111110`. See [05_Data_Link_Layer](05_Data_Link_Layer/).
- **Bottleneck Link:** The link along an end-to-end network transmission path with the lowest transmission capacity, dictating the maximum possible throughput. See [01_Fundamentals](01_Fundamentals/notes.md).
- **BPDU (Bridge Protocol Data Unit):** A management frame exchanged between switches running Spanning Tree Protocol (STP) to elect a root bridge and calculate a loop-free topology. See [06_Network_Devices_and_LAN](06_Network_Devices_and_LAN/notes.md).
- **Broadcast Domain:** The logical network segment in which any computer connected to the network can directly transmit a broadcast frame to all other nodes without passing through a router. See [06_Network_Devices_and_LAN](06_Network_Devices_and_LAN/notes.md).
- **Byte Stuffing:** A data link framing method where a special escape byte (`ESC`) is inserted before any data byte that matches the frame delimiter flag. See [05_Data_Link_Layer](05_Data_Link_Layer/).

---

### C
- **CAN (Campus Area Network):** A network connecting multiple local area networks across a contiguous educational or corporate campus (1–5 km). See [01_Fundamentals](01_Fundamentals/notes.md).
- **CAM Table (Content Addressable Memory):** A high-speed hardware table in a network switch that maps MAC addresses to physical switch port numbers. See [06_Network_Devices_and_LAN](06_Network_Devices_and_LAN/notes.md).
- **CDN (Content Delivery Network):** A geographically distributed network of proxy cache servers that delivers web content and media quickly to users based on location. See [15_Modern_Networking](15_Modern_Networking/).
- **Checksum:** An error-detection value calculated by summing numerical chunks of a packet or header, used in IPv4, TCP, and UDP to detect bit inversions. See [05_Data_Link_Layer](05_Data_Link_Layer/) & [11_Transport_Layer](11_Transport_Layer/notes.md).
- **CIDR (Classless Inter-Domain Routing):** An IP addressing scheme replacing rigid class boundaries with variable-length prefix masks (e.g. `/24`) to slow IPv4 exhaustion. See [08_Subnetting_CIDR_VLSM](08_Subnetting_CIDR_VLSM/notes.md).
- **Circuit Switching:** A switching method that establishes a dedicated physical communication path between sender and receiver for the entire duration of a session (e.g. traditional telephone). See [01_Fundamentals](01_Fundamentals/notes.md).
- **Collision Domain:** A physical network segment where data packets can collide with one another if two or more devices transmit simultaneously (e.g. shared hub or single half-duplex wire). See [06_Network_Devices_and_LAN](06_Network_Devices_and_LAN/notes.md).
- **Congestion Window (`cwnd`):** A TCP state variable maintained by the sender that limits the number of unacknowledged bytes the sender may transmit to avoid overloading the network path. See [11_Transport_Layer](11_Transport_Layer/notes.md).
- **CRC (Cyclic Redundancy Check):** A powerful polynomial-based error-detecting code used widely in Ethernet and Wi-Fi frames to detect burst errors. See [05_Data_Link_Layer](05_Data_Link_Layer/).
- **CSMA/CD (Carrier Sense Multiple Access with Collision Detection):** A legacy half-duplex Ethernet MAC protocol where stations listen before transmitting and abort transmission upon detecting a collision. See [05_Data_Link_Layer](05_Data_Link_Layer/).
- **CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance):** A wireless MAC protocol (802.11) that avoids collisions using explicit inter-frame spacing, random backoff, and optional RTS/CTS exchanges. See [14_Wireless_and_Mobile](14_Wireless_and_Mobile/).

---

### D
- **Data Link Layer:** Layer 2 of the OSI reference model responsible for node-to-node frame delivery, physical MAC addressing, flow control, and error detection. See [05_Data_Link_Layer](05_Data_Link_Layer/).
- **Datagram:** A self-contained, independent packet carrying sufficient routing information to be forwarded from source to destination without reliance on earlier exchanges or pre-established state. See [09_Network_Layer_Protocols](09_Network_Layer_Protocols/).
- **Default Gateway:** A router interface IP configured on a local host to which all traffic destined outside the local subnet is forwarded. See [06_Network_Devices_and_LAN](06_Network_Devices_and_LAN/notes.md).
- **DHCP (Dynamic Host Configuration Protocol):** An application-layer client-server protocol (ports 67/68) that automatically assigns IP addresses, subnet masks, default gateways, and DNS servers to client devices. See [12_Application_Layer](12_Application_Layer/notes.md).
- **Dijkstra's Algorithm:** A greedy shortest-path algorithm used in link-state routing protocols like OSPF to compute the shortest path tree from a single node to all network destinations. See [10_Routing](10_Routing/notes.md).
- **DNS (Domain Name System):** The hierarchical, distributed naming database that translates human-readable hostnames (e.g. `google.com`) into numerical IP addresses (port 53). See [12_Application_Layer](12_Application_Layer/notes.md).
- **DORA:** The four-step message handshake in DHCP: Discover (broadcast), Offer (unicast/broadcast), Request (broadcast), Acknowledgment (unicast/broadcast). See [12_Application_Layer](12_Application_Layer/notes.md).

---

### E
- **Encapsulation:** The process where a protocol layer wraps data received from the layer above with its own control header (and optional trailer) before passing it down the stack. See [02_OSI_Model](02_OSI_Model/notes.md).
- **Ethernet:** The dominant IEEE 802.3 wired local area network (LAN) standard defining frame formats, MAC addressing, and physical signaling specifications. See [05_Data_Link_Layer](05_Data_Link_Layer/).
- **EUI-64:** An IEEE standard method for automatically generating a 64-bit IPv6 interface identifier from a device's 48-bit MAC address by inserting `FF:FE` in the middle and flipping the universal/local bit. See [07_IP_Addressing](07_IP_Addressing/notes.md).

---

### F
- **Flow Control:** A mechanism preventing a fast sender from overwhelming a slow receiver with data faster than the receiver can buffer and process it. See [05_Data_Link_Layer](05_Data_Link_Layer/) & [11_Transport_Layer](11_Transport_Layer/notes.md).
- **Forwarding:** The data-plane process of moving an incoming packet from a router's input port to the appropriate output port based on its destination IP address and routing table lookup. See [10_Routing](10_Routing/notes.md).
- **Fragmentation:** The division of an IP datagram into smaller pieces by a router or sending host when the packet size exceeds the outgoing link's Maximum Transmission Unit (MTU). See [09_Network_Layer_Protocols](09_Network_Layer_Protocols/).
- **FTP (File Transfer Protocol):** An application-layer protocol using dual TCP connections (port 21 for commands, port 20 for data) to transfer files between client and server. See [12_Application_Layer](12_Application_Layer/notes.md).

---

### G
- **Gateway:** A network node that connects two different network architectures or protocols, acting as a translator; commonly used to denote the default router on a local subnet. See [06_Network_Devices_and_LAN](06_Network_Devices_and_LAN/notes.md).
- **Go-Back-N (GBN):** A sliding window ARQ protocol where the sender can transmit up to $N$ unacknowledged frames, but the receiver accepts only consecutive frames and discards out-of-order frames, forcing retransmission of all unacknowledged frames on loss. See [05_Data_Link_Layer](05_Data_Link_Layer/).
- **Goodput:** The application-level throughput, measured as the number of useful data bits delivered to the application per second (excluding protocol headers and retransmitted packets). See [01_Fundamentals](01_Fundamentals/notes.md).

---

### H
- **Hamming Distance:** The number of bit positions at which two equal-length binary codewords differ; minimum distance $d_{\min} \ge 2t+1$ is required to correct $t$ bit errors. See [05_Data_Link_Layer](05_Data_Link_Layer/).
- **HTTP (Hypertext Transfer Protocol):** The foundational application-layer protocol for the World Wide Web running over TCP port 80 (stateless, request-response). See [12_Application_Layer](12_Application_Layer/notes.md).
- **HTTPS:** HTTP secured inside a Transport Layer Security (TLS) cryptographic tunnel over TCP port 443. See [12_Application_Layer](12_Application_Layer/notes.md) & [13_Network_Security](13_Network_Security/).
- **Hub:** A physical-layer (L1) multiport repeater that blindly broadcasts incoming electrical signals out to all other connected ports, creating a single shared collision domain. See [06_Network_Devices_and_LAN](06_Network_Devices_and_LAN/notes.md).

---

### I
- **IXP (Internet Exchange Point):** A physical switching facility where multiple ISPs, CDNs, and cloud networks interconnect directly to exchange traffic without paying transit fees. See [01_Fundamentals](01_Fundamentals/notes.md).
- **ICMP (Internet Control Message Protocol):** A supporting network-layer protocol (IP protocol 1) used by network devices and utilities like `ping` and `traceroute` to diagnose errors and report delivery problems. See [09_Network_Layer_Protocols](09_Network_Layer_Protocols/).
- **IPv4:** The 32-bit connectionless Internet Protocol providing approximately 4.29 billion unique global addresses formatted as four decimal octets. See [07_IP_Addressing](07_IP_Addressing/notes.md).
- **IPv6:** The 128-bit next-generation Internet Protocol providing $2^{128}$ unique addresses formatted as eight hexadecimal quartets. See [07_IP_Addressing](07_IP_Addressing/notes.md).

---

### J
- **Jitter:** The statistical variation in packet transit delay across a network; highly disruptive to real-time interactive traffic like VoIP and video streaming. See [01_Fundamentals](01_Fundamentals/notes.md).

---

### L
- **Link State Routing:** A dynamic routing algorithm category (e.g. OSPF, IS-IS) where every router floods link-state advertisements (LSAs) so all routers construct an identical topology map before running Dijkstra's algorithm. See [10_Routing](10_Routing/notes.md).
- **Longest Prefix Match (LPM):** The forwarding algorithm used by IP routers to select the routing table entry with the most specific (longest) subnet mask matching a packet's destination IP. See [10_Routing](10_Routing/notes.md).

---

### M
- **MAC Address (Media Access Control):** A globally unique 48-bit physical hardware identifier burned into a Network Interface Card (NIC) at Layer 2. See [05_Data_Link_Layer](05_Data_Link_Layer/).
- **Maximum Transmission Unit (MTU):** The largest packet or frame size (in bytes) that can be sent over a physical network medium without requiring fragmentation (typically 1500 bytes for Ethernet). See [09_Network_Layer_Protocols](09_Network_Layer_Protocols/).
- **MSS (Maximum Segment Size):** The largest amount of data (in bytes) that a host can receive in a single unfragmented TCP segment (typically MTU minus 40 bytes = 1460 bytes for IPv4). See [11_Transport_Layer](11_Transport_Layer/notes.md).

---

### N
- **NAT (Network Address Translation):** A technique enabling an entire private network (RFC 1918) to share one or a small pool of public IP addresses by rewriting packet headers at the border router. See [09_Network_Layer_Protocols](09_Network_Layer_Protocols/).
- **Nyquist Rate:** The theoretical maximum data rate of a noiseless channel with bandwidth $B$ Hz and $L$ discrete signal levels: $C = 2B \log_2(L)$ bps. See [04_Physical_Layer](04_Physical_Layer/).

---

### O
- **OSI Model (Open Systems Interconnection):** A conceptual 7-layer reference framework developed by ISO to standardize telecommunication functions: Physical, Data Link, Network, Transport, Session, Presentation, Application. See [02_OSI_Model](02_OSI_Model/notes.md).
- **OSPF (Open Shortest Path First):** An open-standard link-state interior gateway routing protocol (IP protocol 89) using Dijkstra's algorithm, areas, and bandwidth-based costs. See [10_Routing](10_Routing/notes.md).

---

### P
- **PAT (Port Address Translation):** A dynamic form of NAT (also known as NAT Overload) where thousands of internal private host connections are multiplexed onto a single public IP using distinct source port numbers. See [09_Network_Layer_Protocols](09_Network_Layer_Protocols/).
- **PDU (Protocol Data Unit):** The specific unit of data processed and exchanged at a given layer: Bits (L1), Frame (L2), Packet (L3), Segment (L4), Message/Data (L5–L7). See [02_OSI_Model](02_OSI_Model/notes.md).
- **Propagation Delay ($T_p$):** The time required for a physical bit signal to travel through the transmission medium from source to destination ($T_p = \frac{\text{Distance}}{\text{Propagation Speed}}$). See [01_Fundamentals](01_Fundamentals/notes.md).

---

### R
- **RTO (Retransmission Timeout):** The dynamic timer maintained by a TCP sender; if an ACK is not received before RTO expires, the unacknowledged segment is considered lost and retransmitted. See [11_Transport_Layer](11_Transport_Layer/notes.md).
- **RTT (Round Trip Time):** The total time taken for a data packet to travel from sender to receiver plus the time taken for the receiver's acknowledgment to travel back. See [01_Fundamentals](01_Fundamentals/notes.md).

---

### S
- **SAN (Storage Area Network):** A dedicated, specialized high-speed network providing block-level access to consolidated shared storage arrays (Fibre Channel, iSCSI). See [01_Fundamentals](01_Fundamentals/notes.md).
- **Statistical Multiplexing:** A dynamic channel-sharing method where transmission capacity is allocated on demand to actively transmitting packets, maximizing link utilization for bursty traffic. See [01_Fundamentals](01_Fundamentals/notes.md).
- **Store-and-Forward:** A switching technique where a packet must be completely received and verified for bit errors before being forwarded onto the next link. See [01_Fundamentals](01_Fundamentals/notes.md).
- **Selective Repeat (SR):** An advanced sliding-window ARQ protocol where both sender and receiver maintain equal window sizes ($\le 2^{k-1}$); the receiver buffers out-of-order frames, and only lost frames are retransmitted. See [05_Data_Link_Layer](05_Data_Link_Layer/).
- **Shannon Capacity:** The theoretical upper bound on the data rate of a noisy channel with bandwidth $B$ Hz and signal-to-noise ratio SNR: $C = B \log_2(1 + \text{SNR})$ bps. See [04_Physical_Layer](04_Physical_Layer/).
- **Stop-and-Wait ARQ:** The simplest flow-control protocol where a sender transmits exactly one frame and waits for an acknowledgment before sending the next. See [05_Data_Link_Layer](05_Data_Link_Layer/).
- **STP (Spanning Tree Protocol):** An IEEE 802.1D network protocol running on switches that prevents bridge loops and broadcast storms by selectively blocking redundant physical links. See [06_Network_Devices_and_LAN](06_Network_Devices_and_LAN/notes.md).
- **Switch:** A Layer 2 internetworking device that inspects frame MAC addresses to intelligently forward frames only to the designated destination port using hardware CAM tables. See [06_Network_Devices_and_LAN](06_Network_Devices_and_LAN/notes.md).

---

### T
- **Tier-1 ISP:** A global telecommunications backbone provider that owns transcontinental infrastructure and peers with other Tier-1 providers settlement-free. See [01_Fundamentals](01_Fundamentals/notes.md).
- **TCP (Transmission Control Protocol):** A connection-oriented, reliable, byte-stream transport-layer protocol providing ordered delivery, flow control, and congestion control over IP. See [11_Transport_Layer](11_Transport_Layer/notes.md).
- **Throughput:** The actual rate at which data is successfully delivered over a communication channel per unit of time (measured in bits/sec). See [01_Fundamentals](01_Fundamentals/notes.md).
- **Transmission Delay ($T_t$):** The time required to push all bits of a packet onto the physical transmission medium ($T_t = \frac{\text{Packet Size (bits)}}{\text{Bandwidth (bps)}}$). See [01_Fundamentals](01_Fundamentals/notes.md).
- **TTL (Time to Live):** An 8-bit field in the IPv4 header (Hop Limit in IPv6) decremented by 1 at every router hop to prevent packets from looping infinitely. See [09_Network_Layer_Protocols](09_Network_Layer_Protocols/).

---

### U
- **UDP (User Datagram Protocol):** A lightweight, connectionless, message-oriented transport protocol (port protocol 17) offering fast, unacknowledged transmission without flow control or congestion management. See [11_Transport_Layer](11_Transport_Layer/notes.md).

---

### V
- **VLAN (Virtual Local Area Network):** A custom logical network configured on switches that partitions physical ports into isolated broadcast domains regardless of physical location. See [06_Network_Devices_and_LAN](06_Network_Devices_and_LAN/notes.md).
- **VLSM (Variable Length Subnet Masking):** A subnetting strategy allowing subnets of different sizes to be allocated within the same IP address block to prevent address waste. See [08_Subnetting_CIDR_VLSM](08_Subnetting_CIDR_VLSM/notes.md).

---

### W
- **Wireshark:** A widely used open-source packet analyzer tool for network troubleshooting, analysis, software and protocol development, and education. See [16_Troubleshooting_and_Tools](16_Troubleshooting_and_Tools/).

*(Target: 400+ entries across all phases; updated incrementally with every module.)*
