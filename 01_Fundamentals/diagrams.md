# 01. Computer Networking Fundamentals — Visual Diagram Guide

> **Visual companion to Module 01.**  
> Contains 10 detailed Mermaid diagrams illustrating network topologies, failure scenarios, Internet tier hierarchy, switching comparisons, and latency timelines.

---

## 1. Five Components of Data Communication

> **What to notice:** Communication requires both endpoints, a transmission medium, and an agreed protocol syntax at both ends to interpret the message.

```mermaid
flowchart LR
    S["🟦 Sender<br/>(Transmitter)"] --- Medium["⬜ Transmission Medium<br/>(Cable / Fiber / Wireless Air)"]
    Medium --- R["🟩 Receiver<br/>(Destination)"]
    
    subgraph Data["Data In Transit"]
        M["Envelope / Message Payload"]
    end
    
    Medium -.- Data
    
    P1["🟨 Protocol Rules<br/>(Syntax & Semantics)"] -.-> S
    P2["🟨 Protocol Rules<br/>(Syntax & Semantics)"] -.-> R

    classDef sender fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    classDef receiver fill:#dcfce7,stroke:#15803d,stroke-width:2px;
    classDef medium fill:#f8fafc,stroke:#64748b,stroke-width:2px;
    classDef proto fill:#fef3c7,stroke:#d97706,stroke-width:1px;
    
    class S sender;
    class R receiver;
    class Medium medium;
    class P1,P2 proto;
```

**How to read it:**
- The blue box initiates communication; the green box accepts it.
- Without identical protocol rules at both ends, the receiver receives raw electrical pulses or radio noise without understanding the message structure.

---

## 2. Global Internet Hierarchy: Tiers and IXPs

> **What to notice:** Tier-1 ISPs never pay transit fees to each other; Tier-2 and Tier-3 ISPs pay upstream transit unless they peer directly at an IXP.

```mermaid
flowchart TD
    subgraph Tier1["Tier-1 Global Backbones (Transit-Free)"]
        T1_A["🟦 Lumen / AT&T"] <===>|Settlement-Free Peering| T1_B["🟦 Tata / Telia / NTT"]
    end

    subgraph IXP["Internet Exchange Point (IXP)"]
        IXP_Switch(("🟪 High-Speed Layer-2 Peering Switch Fabric"))
    end

    subgraph Tier2["Tier-2 National / Regional Providers"]
        T2_A["🟨 Regional ISP A<br/>(e.g., Airtel / Comcast)"]
        T2_B["🟨 Regional ISP B<br/>(e.g., Vodafone / BT)"]
    end

    subgraph Tier3["Tier-3 Local Access Providers"]
        T3_1["City Cable / Fiber Provider"]
        T3_2["University Campus Network"]
    end

    subgraph Endpoints["End Consumers"]
        Home["🟩 Home Broadband User"]
        DC["🟩 Cloud Data Center (AWS/Google)"]
    end

    T1_A -->|Paid Transit| T2_A
    T1_B -->|Paid Transit| T2_B
    T2_A <-->|Direct Peering| IXP_Switch
    T2_B <-->|Direct Peering| IXP_Switch
    T2_A -->|Customer Link| T3_1
    T2_B -->|Customer Link| T3_2
    T3_1 --> Home
    T3_2 --> DC

    classDef t1 fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    classDef t2 fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    classDef ixp fill:#fae8ff,stroke:#a21caf,stroke-width:2px;
    classDef endp fill:#dcfce7,stroke:#15803d,stroke-width:2px;

    class T1_A,T1_B t1;
    class T2_A,T2_B t2;
    class IXP_Switch ixp;
    class Home,DC endp;
```

**How to read it:**
- Tier-1 backbones have global reach through mutual peering.
- Tier-2 regional ISPs buy transit from Tier-1 but bypass transit costs for regional traffic by exchanging packets through an IXP peering fabric.

---

## 3. Bus Topology & Single Point of Failure

> **What to notice:** All devices share a single electrical copper wire; a cable severed anywhere kills signal propagation for every host on the line.

```mermaid
flowchart LR
    T1["Terminator (50Ω)"] --- N1["PC 1"]
    N1 --- N2["PC 2"]
    N2 -.->|❌ CABLE CUT HERE| N3["PC 3"]
    N3 --- N4["PC 4"]
    N4 --- T2["Terminator (50Ω)"]

    classDef activeNode fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    classDef deadNode fill:#ffe4e6,stroke:#e11d48,stroke-width:2px,stroke-dasharray: 5 5;
    classDef term fill:#64748b,stroke:#334155,stroke-width:1px,color:#fff;

    class N1,N2 activeNode;
    class N3,N4 deadNode;
    class T1,T2 term;
```

**How to read it:**
- When the bus is cut between PC 2 and PC 3, electrical impedance changes immediately. Signals reflect back, creating standing wave interference that brings down all nodes on both sides.

---

## 4. Star Topology: Normal vs. Central Switch Failure

> **What to notice:** Individual cable cuts only affect that specific node; however, a central switch failure collapses the entire LAN.

```mermaid
flowchart TD
    subgraph ScenarioA["Normal Operation: Single Host Failure"]
        SW1["🟨 Central Switch"] --- H1["🟦 Host 1 (OK)"]
        SW1 --- H2["🟦 Host 2 (OK)"]
        SW1 -.->|❌ Broken Cable| H3["🟥 Host 3 (Isolated)"]
        SW1 --- H4["🟦 Host 4 (OK)"]
    end

    subgraph ScenarioB["Catastrophic Failure: Switch Down"]
        SW2["🟥 Central Switch (DEAD)"] -.->|No link| H5["🟥 Host 1"]
        SW2 -.->|No link| H6["🟥 Host 2"]
        SW2 -.->|No link| H7["🟥 Host 3"]
        SW2 -.->|No link| H8["🟥 Host 4"]
    end

    classDef sw fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    classDef deadSw fill:#ffe4e6,stroke:#e11d48,stroke-width:3px;
    classDef okHost fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    classDef deadHost fill:#ffe4e6,stroke:#e11d48,stroke-width:2px;

    class SW1 sw;
    class SW2 deadSw;
    class H1,H2,H4 okHost;
    class H3,H5,H6,H7,H8 deadHost;
```

**How to read it:**
- **Scenario A:** If Host 3's Ethernet patch cord is unplugged, Hosts 1, 2, and 4 continue communicating at full speed.
- **Scenario B:** The central switch is the single point of failure (SPOF) for the star topology.

---

## 5. Ring Topology: Token Passing & Link Break

> **What to notice:** In a unidirectional ring, any broken link halts circulating tokens unless a dual counter-rotating ring (FDDI style) wraps around the fault.

```mermaid
flowchart LR
    A["🟦 Node A"] -->|Token| B["🟦 Node B"]
    B -->|Token| C["🟦 Node C"]
    C -.->|❌ Cut Link| D["🟥 Node D"]
    D -->|Blocked| A

    classDef nodeOK fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    classDef nodeBlocked fill:#ffe4e6,stroke:#e11d48,stroke-width:2px;

    class A,B,C nodeOK;
    class D nodeBlocked;
```

**How to read it:**
- A token is passed sequentially around the ring. Once the link between C and D is cut, the token cannot complete the circuit back to A, halting the entire network.

---

## 6. Full Mesh Topology (5 Nodes)

> **What to notice:** Every node has a direct link to all other 4 nodes. Number of duplex links = $\frac{5 \times 4}{2} = 10$.

```mermaid
flowchart TD
    N1["Node 1"] <---> N2["Node 2"]
    N1 <---> N3["Node 3"]
    N1 <---> N4["Node 4"]
    N1 <---> N5["Node 5"]

    N2 <---> N3
    N2 <---> N4
    N2 <---> N5

    N3 <---> N4
    N3 <---> N5

    N4 <---> N5

    classDef meshNode fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    class N1,N2,N3,N4,N5 meshNode;
```

**How to read it:**
- Each node requires $n-1 = 4$ network interface ports.
- Even if 3 links fail simultaneously, alternative paths remain open.

---

## 7. Hierarchical Tree Topology (Campus LAN)

> **What to notice:** Traffic flows up through Core and Distribution layers before descending to the destination Access switch.

```mermaid
flowchart TD
    subgraph Core["Core Layer (High-Speed Backbone)"]
        C1["🟪 Core Switch 1"] <===> C2["🟪 Core Switch 2"]
    end

    subgraph Distribution["Distribution Layer (Policy & Routing)"]
        D1["🟨 Building A Dist Switch"]
        D2["🟨 Building B Dist Switch"]
    end

    subgraph Access["Access Layer (Workstation Connectivity)"]
        A1["Access Switch Floor 1"]
        A2["Access Switch Floor 2"]
        A3["Access Switch Floor 1"]
    end

    C1 === D1
    C2 === D1
    C1 === D2
    C2 === D2

    D1 --- A1
    D1 --- A2
    D2 --- A3

    classDef core fill:#fae8ff,stroke:#a21caf,stroke-width:2px;
    classDef dist fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    classDef acc fill:#e0f2fe,stroke:#0284c7,stroke-width:1px;

    class C1,C2 core;
    class D1,D2 dist;
    class A1,A2,A3 acc;
```

**How to read it:**
- Access switches connect directly to desktops.
- Distribution switches enforce security policies and routing between VLANs.
- Core switches provide fast, unthrottled transport between buildings.

---

## 8. Circuit Switching vs. Packet Switching (Timeline Comparison)

> **What to notice:** Circuit switching requires a dedicated round-trip setup delay before transmitting; packet switching starts transmitting immediately with per-hop store-and-forward delay.

```mermaid
sequenceDiagram
    autonumber
    actor S as 🟦 Sender
    participant SW1 as 🟨 Switch 1
    participant SW2 as 🟨 Switch 2
    actor R as 🟩 Receiver

    Note over S,R: === CIRCUIT SWITCHING (Dedicated Reservation) ===
    S->>SW1: 1. Setup Request
    SW1->>SW2: Setup Request (Reserve line)
    SW2->>R: Setup Request (Reserve line)
    R-->>SW2: 2. Setup Acknowledged
    SW2-->>SW1: Setup Acknowledged
    SW1-->>S: Connection Ready
    Note over S,R: Continuous Streaming (Zero Queuing Delay)
    S->>R: Continuous Data Stream (Bits flow across circuit)
    S->>R: 3. Teardown Circuit

    Note over S,R: === PACKET SWITCHING (Store-and-Forward) ===
    Note over S: Break data into Packets 1, 2, 3...
    S->>SW1: Packet 1 (L/R Transmission)
    SW1->>SW2: Packet 1 forwarded
    S->>SW1: Packet 2 (Pipelined transmission!)
    SW2->>R: Packet 1 delivered
    SW1->>SW2: Packet 2 forwarded
    S->>SW1: Packet 3
    SW2->>R: Packet 2 delivered
```

**How to read it:**
- In circuit switching, no data travels until step 2 completes.
- In packet switching, packet transmission is pipelined across switches, significantly speeding up bursty transfers.

---

## 9. The 4 Delay Components Across a Single Router Hop

> **What to notice:** Total node latency is the sum of two variable delays (queuing, processing) and two physical deterministic delays (transmission, propagation).

```mermaid
flowchart LR
    InPacket["Incoming Bits on Wire"] --> Proc["1. Processing Delay<br/>(Header check, checksum, route lookup)"]
    Proc --> Queue["2. Queuing Delay<br/>(Waiting in output buffer)"]
    Queue --> Trans["3. Transmission Delay<br/>(Clocking bits onto link: L / R)"]
    Trans --> Medium["4. Propagation Delay<br/>(Physical travel time: d / v)"]
    Medium --> NextRouter["Next Router Input"]

    classDef delay fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    classDef packet fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    class InPacket,NextRouter packet;
    class Proc,Queue,Trans,Medium delay;
```

**How to read it:**
- $D_{\text{proc}}$: Computational delay inside the CPU/ASIC ($\mu\text{s}$).
- $D_{\text{queue}}$: Congestion-dependent buffer delay ($0$ to seconds).
- $D_{\text{trans}}$: $L/R$ — pushes bits from memory into the wire.
- $D_{\text{prop}}$: $d/v$ — electromagnetic propagation across copper or glass.

---

## 10. Bandwidth-Delay Product (BDP) as a "Bit Pipe"

> **What to notice:** BDP represents the total volume of bits in flight filling the cable pipe before the first bit reaches the destination.

```mermaid
flowchart LR
    subgraph Pipe["Physical Link: BDP = Bandwidth (R) × Propagation Delay (Tp)"]
        direction LR
        B1["Bit 1 (Arriving at Receiver)"] --- B2["Bit 2"]
        B2 --- B3["Bit 3"]
        B3 --- B4["... Bits in Flight ..."]
        B4 --- Bn["Bit N (Just leaving Sender)"]
    end

    Sender["🟦 Sender<br/>(Clocking at R bps)"] --> Pipe
    Pipe --> Receiver["🟩 Receiver<br/>(Receiving at distance d)"]

    classDef sender fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    classDef receiver fill:#dcfce7,stroke:#15803d,stroke-width:2px;
    classDef pipe fill:#fef3c7,stroke:#d97706,stroke-width:2px;

    class Sender sender;
    class Receiver receiver;
    class Pipe pipe;
```

**How to read it:**
- If the link has high bandwidth (1 Gbps) and high delay (satellite or trans-Atlantic, 100 ms), the pipe holds millions of bits simultaneously.
- If the sender stops transmitting while waiting for an acknowledgment, this entire pipe empties, wasting available channel capacity.
