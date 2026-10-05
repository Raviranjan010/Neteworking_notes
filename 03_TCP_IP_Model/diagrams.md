# 03. The TCP/IP Protocol Architecture — Visual Diagram Guide

> **Visual companion to Module 03.**  
> Contains 10 detailed Mermaid diagrams illustrating the 4-layer vs. 5-layer stacks, protocol placement architecture, hop-by-hop router traversals, Wireshark frame dissection, and TTL traceroute mechanics.

---

## 1. TCP/IP 4-Layer DoD vs. 5-Layer Hybrid Model

> **What to notice:** The modern 5-layer hybrid model splits the monolithic "Network Access" layer into separate Data Link (L2) and Physical (L1) layers, reflecting real-world engineering.

```mermaid
flowchart LR
    subgraph DoD["Classic 4-Layer DoD Model"]
        D4["4. Application Layer<br/>(HTTP, DNS, SSH, SMTP)"]
        D3["3. Transport Layer (Host-to-Host)<br/>(TCP, UDP)"]
        D2["2. Internet Layer<br/>(IP, ICMP, IGMP)"]
        D1["1. Network Access Layer<br/>(Ethernet, Wi-Fi, Physical Medium)"]
        D4 --> D3 --> D2 --> D1
    end

    subgraph Hybrid["Modern 5-Layer Hybrid Model (GATE Standard)"]
        H5["5. Application Layer<br/>(Message: HTTP, DNS, DHCP)"]
        H4["4. Transport Layer<br/>(Segment: TCP, UDP)"]
        H3["3. Network Layer<br/>(Packet: IPv4, IPv6, ICMP)"]
        H2["2. Data Link Layer<br/>(Frame: Ethernet, Wi-Fi MAC)"]
        H1["1. Physical Layer<br/>(Bits: Copper, Fiber, Radio)"]
        H5 --> H4 --> H3 --> H2 --> H1
    end

    classDef dod fill:#fae8ff,stroke:#a21caf,stroke-width:2px;
    classDef hybrid fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;

    class D4,D3,D2,D1 dod;
    class H5,H4,H3,H2,H1 hybrid;
```

**How to read it:**
- The 4-layer DoD model was the historical standard (RFC 1122).
- Academic textbooks and GATE exams use the 5-layer hybrid model because hardware transceivers (L1) are physically distinct from MAC controllers (L2).

---

## 2. Complete Protocol Suite Architecture

> **What to notice:** The Internet Protocol (IP) sits at the center ("the hourglass waist"). All upper protocols funnel into IP; all lower media support IP.

```mermaid
flowchart TD
    subgraph App["Application Layer (Layer 5)"]
        HTTP["HTTP / HTTPS"]
        DNS["DNS"]
        DHCP["DHCP"]
        SSH["SSH"]
        BGP["BGP"]
        RIP["RIP"]
    end

    subgraph Trans["Transport Layer (Layer 4)"]
        TCP["🟦 TCP (Reliable Byte-Stream)"]
        UDP["🟩 UDP (Lightweight Datagram)"]
    end

    subgraph Net["Network Layer (Layer 3 - The Hourglass Waist)"]
        IP["🟨 IP (IPv4 & IPv6)"]
        ICMP["ICMP"]
        IGMP["IGMP"]
        OSPF["OSPF"]
        ARP["ARP (L2/L3 Glue)"]
    end

    subgraph Link["Data Link & Physical (Layers 2 & 1)"]
        Eth["Ethernet (IEEE 802.3)"]
        WiFi["Wi-Fi (IEEE 802.11)"]
        PPP["PPP / Fiber"]
    end

    HTTP --> TCP
    SSH --> TCP
    BGP --> TCP
    DNS --> UDP
    DNS --> TCP
    DHCP --> UDP
    RIP --> UDP

    TCP --> IP
    UDP --> IP
    OSPF --> IP
    ICMP -.-> IP
    IGMP -.-> IP

    IP --> Eth
    IP --> WiFi
    IP --> PPP
    ARP -.-> Eth
    ARP -.-> WiFi

    classDef app fill:#fae8ff,stroke:#a21caf,stroke-width:1px;
    classDef trans fill:#dcfce7,stroke:#15803d,stroke-width:2px;
    classDef net fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    classDef link fill:#e0f2fe,stroke:#0284c7,stroke-width:1px;

    class HTTP,DNS,DHCP,SSH,BGP,RIP app;
    class TCP,UDP trans;
    class IP,ICMP,IGMP,OSPF,ARP net;
    class Eth,WiFi,PPP link;
```

**How to read it:**
- **The Hourglass Concept:** There are hundreds of application protocols and dozens of physical media, but only **one** Internet Protocol uniting them.

---

## 3. Hop-by-Hop Packet Journey Across 3 Routers

> **What to notice:** MAC addresses are completely rewritten at every hop; Source and Destination IP addresses and Port numbers remain completely invariant.

```mermaid
sequenceDiagram
    autonumber
    actor HostA as 🟦 Host A<br/>IP: 192.168.1.10<br/>MAC: AA:AA:AA
    participant R1 as 🟨 Router 1<br/>In: BB:BB | Out: CC:CC
    participant R2 as 🟨 Router 2<br/>In: DD:DD | Out: EE:EE
    actor ServerB as 🟩 Server B<br/>IP: 172.16.0.50<br/>MAC: FF:FF:FF

    Note over HostA,R1: Hop 1 (Local Subnet 192.168.1.0/24)
    HostA->>R1: Frame 1: [DstMAC: BB, SrcMAC: AA] [DstIP: 172.16.0.50, SrcIP: 192.168.1.10] [DstPort: 443, SrcPort: 54321] [TTL: 64]
    Note over R1: R1 strips Frame 1. Decrements TTL=63. Route lookup selects WAN interface Out (CC).
    
    Note over R1,R2: Hop 2 (WAN Point-to-Point Link)
    R1->>R2: Frame 2: [DstMAC: DD, SrcMAC: CC] [DstIP: 172.16.0.50, SrcIP: 192.168.1.10] [DstPort: 443, SrcPort: 54321] [TTL: 63]
    Note over R2: R2 strips Frame 2. Decrements TTL=62. ARP lookup discovers Server B MAC (FF).

    Note over R2,ServerB: Hop 3 (Destination Subnet 172.16.0.0/24)
    R2->>ServerB: Frame 3: [DstMAC: FF, SrcMAC: EE] [DstIP: 172.16.0.50, SrcIP: 192.168.1.10] [DstPort: 443, SrcPort: 54321] [TTL: 62]
    Note over ServerB: Server B verifies DstMAC=FF, DstIP=172.16.0.50, delivers segment to TCP Port 443!
```

**How to read it:**
- **Source & Destination IP:** `192.168.1.10` and `172.16.0.50` never change.
- **Source & Destination Ports:** `54321` and `443` never change.
- **Source & Destination MACs:** Change on every single link (AA $\rightarrow$ BB, CC $\rightarrow$ DD, EE $\rightarrow$ FF).
- **TTL:** Decrements from 64 $\rightarrow$ 63 $\rightarrow$ 62.

---

## 4. The Fate-Sharing Architectural Model

> **What to notice:** Intermediate routers hold zero session state. If Router 2 crashes, Router 1 simply diverts packets to Router 3 without disconnecting the TCP session.

```mermaid
flowchart LR
    HostA["🟦 Client Host A<br/>(Maintains TCP State:<br/>Seq #, cwnd, timer)"] --> R1["🟨 Router 1"]
    
    R1 -->|Normal Path| R2["🟥 Router 2 (CRASHED!)"]
    R2 -.-> ServerB
    
    R1 ==>|Dynamic Reroute| R3["🟨 Router 3 (Alternate)"]
    R3 ==> ServerB["🟩 Server B<br/>(Maintains TCP State:<br/>Ack #, rwnd)"]

    classDef host fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    classDef rtr fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    classDef deadRtr fill:#ffe4e6,stroke:#e11d48,stroke-width:3px;

    class HostA,ServerB host;
    class R1,R3 rtr;
    class R2 deadRtr;
```

**How to read it:**
- Because routers are **stateless packet forwarders**, network failures do not terminate application connections. Endpoints handle retransmissions.

---

## 5. Wireshark-Style Layered Packet Dissection

> **What to notice:** Every packet on the wire consists of nested headers. Wireshark displays them from outer (physical/link) to inner (application).

```mermaid
flowchart TD
    subgraph FrameView["Wireshark Packet Dissection View"]
        direction TB
        F1["Frame 1: 1058 bytes on wire (8464 bits), 1058 bytes captured"]
        F2["Ethernet II, Src: 00:0c:29:1a:2b:3c, Dst: 00:50:56:e1:d2:c3 (14 Bytes)"]
        F3["Internet Protocol Version 4, Src: 192.168.1.10, Dst: 142.250.190.46 (20 Bytes)"]
        F4["Transmission Control Protocol, Src Port: 54321, Dst Port: 443, Seq: 1, Ack: 1 (20 Bytes)"]
        F5["Transport Layer Security (TLS 1.3 Record Layer: Encrypted Application Data: 1000 Bytes)"]
    end

    F1 --- F2 --- F3 --- F4 --- F5

    classDef f1 fill:#f8fafc,stroke:#64748b,stroke-width:1px;
    classDef f2 fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    classDef f3 fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    classDef f4 fill:#dcfce7,stroke:#15803d,stroke-width:2px;
    classDef f5 fill:#fae8ff,stroke:#a21caf,stroke-width:2px;

    class F1 f1;
    class F2 f2;
    class F3 f3;
    class F4 f4;
    class F5 f5;
```

**How to read it:**
- Blue is Layer 2 Ethernet; amber is Layer 3 IP; green is Layer 4 TCP; purple is Layer 7 Application/TLS.

---

## 6. How Traceroute Uses TTL Decrement and ICMP Time Exceeded

> **What to notice:** Traceroute deliberately forces routers to drop packets by setting TTL starting from 1, mapping every hop along the route.

```mermaid
sequenceDiagram
    autonumber
    actor Client as 🟦 Traceroute Client
    participant R1 as 🟨 Router 1 (Hop 1)
    participant R2 as 🟨 Router 2 (Hop 2)
    actor Target as 🟩 Destination Server

    Note over Client,Target: Probe 1: Send with TTL = 1
    Client->>R1: Packet (TTL = 1)
    Note over R1: TTL decremented to 0! Packet dropped.
    R1-->>Client: 🟥 ICMP Time Exceeded (Type 11, Code 0) from IP 192.168.1.1!
    Note over Client: Hop 1 identified: 192.168.1.1 (0.8 ms)

    Note over Client,Target: Probe 2: Send with TTL = 2
    Client->>R1: Packet (TTL = 2)
    R1->>R2: Packet (TTL decremented to 1)
    Note over R2: TTL decremented to 0! Packet dropped.
    R2-->>Client: 🟥 ICMP Time Exceeded (Type 11, Code 0) from IP 10.0.0.2!
    Note over Client: Hop 2 identified: 10.0.0.2 (14.2 ms)

    Note over Client,Target: Probe 3: Send with TTL = 3
    Client->>R1: Packet (TTL = 3)
    R1->>R2: Packet (TTL = 2)
    R2->>Target: Packet (TTL = 1)
    Target-->>Client: 🟩 ICMP Port Unreachable or Echo Reply!
    Note over Client: Target reached in 3 hops!
```

**How to read it:**
- Every router that drops a packet due to $\text{TTL} = 0$ is obligated by RFC 792 to notify the sender via an ICMP Time Exceeded packet, revealing its own IP address.

---

## 7. Address Resolution Protocol (ARP) Request & Reply

> **What to notice:** The ARP Request is an Ethernet broadcast (`FF:FF:FF:FF:FF:FF`) heard by all local nodes; the ARP Reply is a direct unicast.

```mermaid
flowchart TD
    subgraph LAN["Local Broadcast Domain (Subnet 192.168.1.0/24)"]
        HostA["🟦 Host A<br/>IP: 192.168.1.10<br/>MAC: AA:AA:AA"]
        SW(("🟪 Layer 2 Switch"))
        HostB["🟩 Host B<br/>IP: 192.168.1.20<br/>MAC: BB:BB:BB"]
        HostC["Host C<br/>IP: 192.168.1.30<br/>MAC: CC:CC:CC"]
    end

    HostA -->|1. ARP Request: 'Who has 192.168.1.20?'<br/>DstMAC: FF:FF:FF:FF:FF:FF (Broadcast)| SW
    SW -->|Floods Broadcast| HostB
    SW -->|Floods Broadcast| HostC
    HostC -->|Ignores: Not my IP| HostC
    HostB -->|2. ARP Reply: 'I have 192.168.1.20, my MAC is BB:BB:BB'<br/>DstMAC: AA:AA:AA (Unicast)| SW
    SW -->|Forwards Unicast| HostA

    classDef hostA fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    classDef hostB fill:#dcfce7,stroke:#15803d,stroke-width:2px;
    classDef sw fill:#fae8ff,stroke:#a21caf,stroke-width:2px;
    classDef hostC fill:#f8fafc,stroke:#64748b,stroke-width:1px;

    class HostA hostA;
    class HostB hostB;
    class SW sw;
    class HostC hostC;
```

**How to read it:**
- Host A caches Host B's MAC address in its ARP cache (`arp -a`) for future transmissions.

---

## 8. IPv4 Header vs. IPv6 Header Architecture

> **What to notice:** IPv6 has a clean, fixed 40-byte header. Checksum and router fragmentation fields were removed to accelerate ASIC processing.

```mermaid
flowchart TD
    subgraph IPv4["IPv4 Header (Variable: 20–60 Bytes)"]
        V4["Version (4b) | IHL (4b) | DSCP (6b) | ECN (2b) | Total Length (16b)"]
        ID["Identification (16b) | Flags (3b) | Fragment Offset (13b)"]
        TTL["Time to Live (8b) | Protocol (8b) | Header Checksum (16b)"]
        IP4_S["Source IPv4 Address (32 bits / 4 Bytes)"]
        IP4_D["Destination IPv4 Address (32 bits / 4 Bytes)"]
        OPT["Options (0–40 Bytes, variable padding)"]
        V4 --- ID --- TTL --- IP4_S --- IP4_D --- OPT
    end

    subgraph IPv6["IPv6 Header (Strictly Fixed: 40 Bytes)"]
        V6["Version (4b) | Traffic Class (8b) | Flow Label (20 bits)"]
        LEN["Payload Length (16b) | Next Header (8b) | Hop Limit (8b)"]
        IP6_S["Source IPv6 Address (128 bits / 16 Bytes)"]
        IP6_D["Destination IPv6 Address (128 bits / 16 Bytes)"]
        V6 --- LEN --- IP6_S --- IP6_D
    end

    classDef v4 fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    classDef v6 fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;

    class V4,ID,TTL,IP4_S,IP4_D,OPT v4;
    class V6,LEN,IP6_S,IP6_D v6;
```

**How to read it:**
- Notice the simplicity of IPv6: 8 fields vs. 14 in IPv4. Routers parse IPv6 in hardware with significantly lower CPU overhead.

---

## 9. The Complete URL Loading Lifecycle Across Protocols

> **What to notice:** A single web page request triggers four distinct protocols (DNS, ARP, TCP, HTTP) before the first byte of HTML renders.

```mermaid
sequenceDiagram
    autonumber
    actor User as 🟦 Browser (Client)
    participant DNS as 🟨 DNS Server (UDP 53)
    participant GW as 🟨 Default Gateway Router
    actor Web as 🟩 Web Server (TCP 443)

    Note over User,DNS: Phase 1: Name Resolution (Application Layer)
    User->>DNS: 1. DNS Query: 'What is the IP of example.com?' (UDP 53)
    DNS-->>User: 2. DNS Reply: '93.184.216.34'

    Note over User,GW: Phase 2: Link Layer MAC Resolution
    User->>GW: 3. ARP Request: 'Who has Default Gateway IP?' (L2 Broadcast)
    GW-->>User: 4. ARP Reply: Gateway MAC address

    Note over User,Web: Phase 3: Transport Connection Setup
    User->>Web: 5. TCP SYN (Port 443)
    Web-->>User: 6. TCP SYN-ACK
    User->>Web: 7. TCP ACK (Connection Established!)

    Note over User,Web: Phase 4: Application Request & Data Delivery
    User->>Web: 8. HTTP GET /index.html (over TLS)
    Web-->>User: 9. HTTP 200 OK (HTML Payload Delivered)
```

**How to read it:**
- If any one of these four phases fails, the user experiences a broken web page.

---

## 10. Connection-Oriented (TCP) vs. Connectionless (UDP) Demultiplexing

> **What to notice:** UDP demultiplexes using a 2-tuple (Dest IP, Dest Port); TCP demultiplexes using a full 4-tuple (Src IP, Src Port, Dst IP, Dst Port).

```mermaid
flowchart TD
    subgraph UDP_Demux["UDP Demultiplexing (2-Tuple)"]
        U1["Packet from Host A<br/>Src: 10.0.0.1:5001"] --> USock["UDP Socket Bound to Port 53"]
        U2["Packet from Host B<br/>Src: 10.0.0.2:8000"] --> USock
        USock --> DNSApp["DNS Server Process"]
    end

    subgraph TCP_Demux["TCP Demultiplexing (4-Tuple)"]
        T1["TCP Segment from Client 1<br/>(10.0.0.1:54321, 192.168.1.1:80)"] --> Sock1["Dedicated Socket 1"]
        T2["TCP Segment from Client 2<br/>(10.0.0.2:61000, 192.168.1.1:80)"] --> Sock2["Dedicated Socket 2"]
        Sock1 --> WebWorker1["Worker Thread 1"]
        Sock2 --> WebWorker2["Worker Thread 2"]
    end

    classDef udp fill:#dcfce7,stroke:#15803d,stroke-width:2px;
    classDef tcp fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;

    class U1,U2,USock,DNSApp udp;
    class T1,T2,Sock1,Sock2,WebWorker1,WebWorker2 tcp;
```

**How to read it:**
- Two different TCP clients connecting to port 80 are routed to two separate operating system sockets because their Source IP/Port differs.
