# 02. The OSI 7-Layer Model — Visual Diagram Guide

> **Visual companion to Module 02.**  
> Contains 10 detailed Mermaid diagrams illustrating the 7-layer stack, peer-to-peer virtual flow, byte-level encapsulation, firewall positioning, TLS placement, and diagnostic decision trees.

---

## 1. The 7-Layer OSI Architecture & Responsibility Stack

> **What to notice:** Layers 1–3 are physical network/link oriented; Layers 5–7 are host application oriented; Layer 4 is the end-to-end bridge.

```mermaid
flowchart TD
    subgraph Upper["Upper Layers (Software / Host Oriented)"]
        L7["7. Application Layer<br/>(Network Services to Apps: HTTP, DNS, SMTP)"]
        L6["6. Presentation Layer<br/>(Formatting, Syntax, Encoding, Compression)"]
        L5["5. Session Layer<br/>(Dialogue Control, Checkpoints, Session Auth)"]
    end

    subgraph Bridge["Heart of the Model (End-to-End Bridge)"]
        L4["4. Transport Layer<br/>(Reliability, Port Multiplexing, Flow Control: TCP/UDP)"]
    end

    subgraph Lower["Lower Layers (Network / Hardware Oriented)"]
        L3["3. Network Layer<br/>(Logical Addressing, Routing: IPv4/IPv6, Routers)"]
        L2["2. Data Link Layer<br/>(Framing, Physical MAC Addressing, Switches)"]
        L1["1. Physical Layer<br/>(Raw Bits, Voltage, Optical Pulses, Hubs/Cables)"]
    end

    L7 --> L6
    L6 --> L5
    L5 --> L4
    L4 --> L3
    L3 --> L2
    L2 --> L1

    classDef lUpper fill:#fae8ff,stroke:#a21caf,stroke-width:2px;
    classDef lBridge fill:#dcfce7,stroke:#15803d,stroke-width:2px;
    classDef lLower fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;

    class L7,L6,L5 lUpper;
    class L4 lBridge;
    class L3,L2,L1 lLower;
```

**How to read it:**
- When an application transmits data, execution flows from top (L7) to bottom (L1).
- When a packet arrives from the network wire, execution flows from bottom (L1) up to the application (L7).

---

## 2. Peer-to-Peer Virtual Flow vs. Actual Physical Flow

> **What to notice:** Logically, Layer $N$ on Host A communicates with Layer $N$ on Host B; physically, data must descend down to Layer 1, traverse the wire, and ascend up on the other side.

```mermaid
sequenceDiagram
    autonumber
    participant A_App as 🟦 Host A (Layer 7)
    participant A_Trans as 🟦 Host A (Layer 4)
    participant A_Net as 🟦 Host A (Layer 3)
    participant A_Phy as 🟦 Host A (Layer 1)
    participant Cable as ⬜ Physical Transmission Medium
    participant B_Phy as 🟩 Host B (Layer 1)
    participant B_Net as 🟩 Host B (Layer 3)
    participant B_Trans as 🟩 Host B (Layer 4)
    participant B_App as 🟩 Host B (Layer 7)

    Note over A_App,B_App: Logical Peer-to-Peer Communication (Virtual Flow)
    A_App->>A_Trans: 1. Push Application Data
    A_Trans->>A_Net: 2. Add TCP Header (Segment)
    A_Net->>A_Phy: 3. Add IP Header (Packet) & MAC (Frame)
    A_Phy->>Cable: 4. Transmit Raw Bits
    Cable->>B_Phy: 5. Bits arrive at receiver
    B_Phy->>B_Net: 6. Strip MAC (Frame verified)
    B_Net->>B_Trans: 7. Strip IP (Routed to host)
    B_Trans->>B_App: 8. Strip TCP (Delivered to target port)
    Note over A_Trans,B_Trans: TCP Handshake & ACKs exchange peer-to-peer state
```

**How to read it:**
- Blue nodes are the sender stack; green nodes are the receiver stack.
- The transport layer on Host A exchanges sequence numbers directly with the transport layer on Host B, independent of intermediate network switches.

---

## 3. Step-by-Step Encapsulation with Exact Byte Overheads

> **What to notice:** Each layer wraps the entire PDU from the layer above inside its own data payload field and adds header bytes.

```mermaid
flowchart TD
    subgraph Step1["Step 1: Application Layer (User Data)"]
        D1["Data Payload<br/>(HTTP Request: 1000 Bytes)"]
    end

    subgraph Step2["Step 2: Transport Layer (TCP Segment)"]
        H_TCP["TCP Header<br/>(20 Bytes)"] --- P_TCP["Data Payload (1000 Bytes)"]
    end

    subgraph Step3["Step 3: Network Layer (IPv4 Packet)"]
        H_IP["IPv4 Header<br/>(20 Bytes)"] --- P_IP["TCP Segment (1020 Bytes)"]
    end

    subgraph Step4["Step 4: Data Link Layer (Ethernet Frame)"]
        H_ETH["Ethernet Header<br/>(14 Bytes)"] --- P_ETH["IP Packet (1040 Bytes)"] --- T_ETH["FCS Trailer<br/>(4 Bytes CRC)"]
    end

    subgraph Step5["Step 5: Physical Layer (Bits on Wire)"]
        Bits["01001000 01100101 01101100 01101100 01101111 ... (1058 Total Bytes)"]
    end

    Step1 --> Step2
    Step2 --> Step3
    Step3 --> Step4
    Step4 --> Step5

    classDef data fill:#fae8ff,stroke:#a21caf,stroke-width:1px;
    classDef hdr fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    classDef trailer fill:#ffe4e6,stroke:#e11d48,stroke-width:2px;
    classDef bits fill:#f1f5f9,stroke:#64748b,stroke-width:2px;

    class D1,P_TCP,P_IP,P_ETH data;
    class H_TCP,H_IP,H_ETH hdr;
    class T_ETH trailer;
    class Bits bits;
```

**How to read it:**
- User payload = 1000 Bytes.
- TCP Segment = $1000 + 20 = 1020\text{ Bytes}$.
- IP Packet = $1020 + 20 = 1040\text{ Bytes}$.
- Ethernet Frame = $14 + 1040 + 4 = 1058\text{ Bytes}$ on physical wire.
- Wire efficiency = $\frac{1000}{1058} \approx 94.5\%$.

---

## 4. The Gateway Clarification: L3 Default Gateway vs. L7 API Gateway

> **What to notice:** The term "Gateway" is overloaded in computer science. Network engineers mean a Layer 3 router; software engineers mean a Layer 7 proxy.

```mermaid
flowchart TD
    subgraph L3_Scenario["Layer 3: Default Gateway (Router)"]
        H1["Host PC<br/>192.168.1.10"] -->|Sends IP Packet to non-local subnet| R1["🟨 Router / Default Gateway<br/>192.168.1.1"]
        R1 -->|Inspects IP Header only| WAN["Public Internet / WAN"]
    end

    subgraph L7_Scenario["Layer 7: Protocol / API Gateway (Proxy)"]
        Client["Web Browser / Mobile App"] -->|REST JSON Request over HTTPS| AGW["🟪 API Gateway (Kong / AWS API GW)<br/>Inspects Full HTTP Payload"]
        AGW -->|Protocol Translation: REST to gRPC| S1["Microservice A"]
        AGW -->|Authentication & Rate Limiting| S2["Microservice B"]
    end

    classDef rtr fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    classDef apigw fill:#fae8ff,stroke:#a21caf,stroke-width:2px;
    classDef node fill:#e0f2fe,stroke:#0284c7,stroke-width:1px;

    class R1 rtr;
    class AGW apigw;
    class H1,Client,S1,S2 node;
```

**How to read it:**
- A **Default Gateway** is a hardware router at Layer 3 responsible for forwarding packets outside the local broadcast domain.
- An **API/Protocol Gateway** operates at Layer 7, deeply inspecting payload data, translating message protocols, and managing API security tokens.

---

## 5. Where Does TLS/SSL Actually Sit?

> **What to notice:** TLS does not conform to the rigid 7-layer model; it operates as an intermediate security session layer between Layer 4 (TCP) and Layer 7 (HTTP).

```mermaid
flowchart TD
    App["Layer 7: Application Protocols<br/>(HTTP, SMTP, IMAP)"]
    
    subgraph SecurityShim["Intermediate Security Shim"]
        TLS["🔒 TLS 1.3 Record Protocol<br/>(Session Key Exchange, Payload Encryption/Decryption)"]
    end
    
    Trans["Layer 4: Transport Protocols<br/>(TCP - Transmission Control Protocol)"]
    Net["Layer 3: Network Protocols<br/>(IP - Internet Protocol)"]

    App -->|Plaintext HTTP stream| TLS
    TLS -->|Encrypted ciphertext records| Trans
    Trans --> Net

    classDef app fill:#fae8ff,stroke:#a21caf,stroke-width:2px;
    classDef tls fill:#fef3c7,stroke:#d97706,stroke-width:3px;
    classDef trans fill:#dcfce7,stroke:#15803d,stroke-width:2px;
    classDef net fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;

    class App app;
    class TLS tls;
    class Trans trans;
    class Net net;
```

**How to read it:**
- In textbook theory, encryption is assigned to Layer 6 (Presentation).
- In the real Internet, HTTP sends plaintext to TLS, which encrypts the payload into TLS records and hands them to TCP port 443.

---

## 6. Multi-Layer Firewall Architecture

> **What to notice:** Firewalls exist at Layer 3, Layer 4, and Layer 7, each analyzing deeper fields in the encapsulated packet.

```mermaid
flowchart TD
    P["Incoming Packet on Wire"] --> FW_L3{"Layer 3 Firewall<br/>(Packet Filter)"}
    
    FW_L3 -->|Drop if Source/Dest IP is Blacklisted| Drop1["🟥 Block Packet"]
    FW_L3 -->|Allowed IP| FW_L4{"Layer 4 Firewall<br/>(Stateful Inspection)"}
    
    FW_L4 -->|Drop if Port Closed or Invalid TCP Flags| Drop2["🟥 Block Packet"]
    FW_L4 -->|Valid Connection (e.g. Port 443)| FW_L7{"Layer 7 Firewall<br/>(WAF / Deep Packet Inspection)"}
    
    FW_L7 -->|Drop if SQL Injection or XSS in HTTP Body| Drop3["🟥 Block Request"]
    FW_L7 -->|Clean Application Payload| AppServer["🟩 Web Application Server"]

    classDef pass fill:#dcfce7,stroke:#15803d,stroke-width:2px;
    classDef block fill:#ffe4e6,stroke:#e11d48,stroke-width:2px;
    classDef fw fill:#fef3c7,stroke:#d97706,stroke-width:2px;

    class FW_L3,FW_L4,FW_L7 fw;
    class Drop1,Drop2,Drop3 block;
    class AppServer pass;
```

**How to read it:**
- **L3 Filter:** Checks IP headers (fastest, lowest CPU overhead).
- **L4 Stateful:** Tracks TCP state (SYN, ESTABLISHED) and port numbers.
- **L7 WAF:** Inspects full application text for attacks like SQL injection and cross-site scripting (slowest, highest CPU overhead).

---

## 7. Hop-by-Hop L2 Rewrite Across Intermediate Routers

> **What to notice:** IP addresses remain constant end-to-end; MAC addresses are rewritten at every single router hop!

```mermaid
sequenceDiagram
    autonumber
    actor HostA as 🟦 Host A<br/>IP: 10.0.0.1<br/>MAC: AA:AA
    participant R1 as 🟨 Router 1<br/>In: BB:BB | Out: CC:CC
    participant R2 as 🟨 Router 2<br/>In: DD:DD | Out: EE:EE
    actor HostB as 🟩 Host B<br/>IP: 20.0.0.1<br/>MAC: FF:FF

    Note over HostA,R1: Subnet 1 (10.0.0.0/24)
    HostA->>R1: Frame 1: [SrcMAC: AA, DstMAC: BB] [SrcIP: 10.0.0.1, DstIP: 20.0.0.1]
    Note over R1: R1 strips L2 Frame, inspects L3 IP, decrements TTL, selects outgoing interface
    Note over R1,R2: Subnet 2 (WAN Point-to-Point)
    R1->>R2: Frame 2: [SrcMAC: CC, DstMAC: DD] [SrcIP: 10.0.0.1, DstIP: 20.0.0.1]
    Note over R2: R2 strips L2 Frame, inspects L3 IP, decrements TTL, looks up Host B MAC via ARP
    Note over R2,HostB: Subnet 3 (20.0.0.0/24)
    R2->>HostB: Frame 3: [SrcMAC: EE, DstMAC: FF] [SrcIP: 10.0.0.1, DstIP: 20.0.0.1]
```

**How to read it:**
- At every router hop, the Layer 2 Ethernet header and FCS trailer are stripped and discarded.
- A brand-new Layer 2 frame is generated with the router's outgoing MAC as source and the next hop's MAC as destination.
- The inner Layer 3 IP packet (Source IP: 10.0.0.1, Destination IP: 20.0.0.1) remains unchanged (except TTL decrement).

---

## 8. Systematic Troubleshooting Flowchart (Divide-and-Conquer)

> **What to notice:** Start at Layer 3 with `ping` to immediately isolate whether the problem is physical/link-level or application/DNS-level.

```mermaid
flowchart TD
    Start["User Reports: Cannot Access Website"] --> PingGW{"Can you ping the Default Gateway IP?"}
    
    PingGW -- No --> CheckL1{"Are physical link lights ON on NIC/Router?"}
    CheckL1 -- No --> FixL1["Fix L1: Reconnect cable, replace patch cord, check power"]
    CheckL1 -- Yes --> CheckL2["Check L2: Verify VLAN assignment, check ARP cache, fix duplex mismatch"]
    
    PingGW -- Yes --> PingExt{"Can you ping external IP 8.8.8.8?"}
    PingExt -- No --> FixL3["Fix L3: Routing table issue, default route missing, ISP outage"]
    
    PingExt -- Yes --> PingDNS{"Can you resolve domain name (e.g. nslookup google.com)?"}
    PingDNS -- No --> FixDNS["Fix L7 (DNS): Check DNS server IP in /etc/resolv.conf or DHCP"]
    
    PingDNS -- Yes --> CheckPort{"Can you establish TCP connection (curl -v / telnet port 443)?"}
    CheckPort -- No --> FixL4["Fix L4: Firewall blocking port, server process not listening"]
    CheckPort -- Yes --> FixL7["Fix L7: Web server HTTP error (500/502), TLS cert expired"]

    classDef test fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    classDef fix fill:#ffe4e6,stroke:#e11d48,stroke-width:2px;
    classDef ok fill:#dcfce7,stroke:#15803d,stroke-width:2px;

    class PingGW,PingExt,PingDNS,CheckPort,CheckL1 test;
    class FixL1,CheckL2,FixL3,FixDNS,FixL4,FixL7 fix;
```

**How to read it:**
- Pinging the default gateway immediately verifies Layers 1, 2, and local Layer 3.
- If ping succeeds by IP but fails by hostname, the network stack is completely fine; the issue is strictly Layer 7 DNS resolution.

---

## 9. OSI Model vs. TCP/IP Protocol Suite Layer Alignment

> **What to notice:** TCP/IP collapses OSI Layers 5, 6, and 7 into a single Application layer, and collapses Layers 1 and 2 into Network Access in the 4-layer model.

```mermaid
flowchart LR
    subgraph OSI["OSI 7-Layer Model"]
        direction TB
        O7["7. Application"]
        O6["6. Presentation"]
        O5["5. Session"]
        O4["4. Transport"]
        O3["3. Network"]
        O2["2. Data Link"]
        O1["1. Physical"]
    end

    subgraph TCPIP["TCP/IP 5-Layer Hybrid Model"]
        direction TB
        T5["5. Application Layer<br/>(HTTP, DNS, SSH, SMTP)"]
        T4["4. Transport Layer<br/>(TCP, UDP)"]
        T3["3. Network / Internet Layer<br/>(IPv4, IPv6, ICMP)"]
        T2["2. Data Link Layer<br/>(Ethernet, Wi-Fi MAC)"]
        T1["1. Physical Layer<br/>(Cables, Connectors, Signaling)"]
    end

    O7 --> T5
    O6 --> T5
    O5 --> T5
    O4 --> T4
    O3 --> T3
    O2 --> T2
    O1 --> T1

    classDef osi fill:#fae8ff,stroke:#a21caf,stroke-width:2px;
    classDef tcp fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;

    class O7,O6,O5,O4,O3,O2,O1 osi;
    class T5,T4,T3,T2,T1 tcp;
```

**How to read it:**
- The 5-layer hybrid model is the modern standard used in computer science textbooks (Kurose & Ross, Tanenbaum) and the GATE CS/IT syllabus.

---

## 10. Device Layer Mapping Across the Stack

> **What to notice:** Devices operate at a primary layer, but also implement all layers beneath it to physically transmit signals.

```mermaid
flowchart TD
    subgraph L7_Dev["Layer 7 Devices"]
        D7["Web Application Firewall (WAF)<br/>Reverse Proxy (Nginx)<br/>API Gateway"]
    end

    subgraph L4_Dev["Layer 4 Devices"]
        D4["Stateful Inspection Firewall<br/>L4 Load Balancer (HAProxy, AWS NLB)"]
    end

    subgraph L3_Dev["Layer 3 Devices"]
        D3["Router<br/>Layer 3 Multilayer Switch"]
    end

    subgraph L2_Dev["Layer 2 Devices"]
        D2["Layer 2 Switch<br/>Network Bridge"]
    end

    subgraph L1_Dev["Layer 1 Devices"]
        D1["Multiport Hub<br/>Repeater<br/>Transceiver / Media Converter"]
    end

    D7 --> D4
    D4 --> D3
    D3 --> D2
    D2 --> D1

    classDef d7 fill:#fae8ff,stroke:#a21caf,stroke-width:2px;
    classDef d4 fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    classDef d3 fill:#dcfce7,stroke:#15803d,stroke-width:2px;
    classDef d2 fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    classDef d1 fill:#f1f5f9,stroke:#64748b,stroke-width:2px;

    class D7 d7;
    class D4 d4;
    class D3 d3;
    class D2 d2;
    class D1 d1;
```

**How to read it:**
- A router is a Layer 3 device, but its physical Ethernet ports implement Layer 2 MAC addressing and Layer 1 physical transceivers.
