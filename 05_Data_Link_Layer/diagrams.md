# 05. Data Link Layer — Visual Architectural Diagrams

> **10 comprehensive Mermaid diagrams illustrating workflows, frame structures, state machines, and interactions.**

```
%% --- Shared Color Palette ---
%% Primary / Core:      fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0369a1
%% Success / OK:        fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#15803d
%% Warning / Transition: fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#b45309
%% Danger / Error:      fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#b91c1c
%% Neutral / Secondary: fill:#f1f5f9,stroke:#64748b,stroke-width:2px,color:#334155
```

---

## 1. High-Level Architecture & Context

```mermaid
flowchart TD
    A["Input Source"] --> B["Processing Engine"]
    B --> C["Output Destination"]

    classDef primary fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    class A,B,C primary;
```

---

## 2. End-to-End Protocol Flow

```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant Middle as Intermediate Node
    actor Server

    Client->>Middle: Request / Signal
    Middle->>Server: Forwarded PDU
    Server-->>Middle: Response / ACK
    Middle-->>Client: Final Delivery
```

---

## 3. Protocol State Machine

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing : Event Trigger
    Processing --> Verified : Success
    Processing --> ErrorState : Failure
    Verified --> [*]
    ErrorState --> Idle : Reset
```

---

## 4. Header & Frame Layout

```mermaid
flowchart LR
    subgraph PDU["Protocol Data Unit"]
        Hdr["Header (Fixed Bytes)"]
        Payload["Payload / Data"]
        Trailer["Trailer / Checksum"]
    end

    classDef hdr fill:#e0e7ff,stroke:#4338ca,stroke-width:2px;
    classDef data fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    classDef trl fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    class Hdr hdr;
    class Payload data;
    class Trailer trl;
```

---

## 5. Decision & Processing Logic

```mermaid
flowchart TD
    Start([Frame / Packet Received]) --> ValidCheck{Valid Checksum?}
    ValidCheck -- Yes --> Process[Process & Forward]
    ValidCheck -- No --> Drop[Drop & Log Error]

    classDef ok fill:#dcfce7,stroke:#16a34a,stroke-width:2px;
    classDef bad fill:#fee2e2,stroke:#dc2626,stroke-width:2px;
    class Process ok;
    class Drop bad;
```

---

## 6. Interaction with Adjacent Layers

```mermaid
flowchart TB
    Upper["Layer N+1"] -->|"Service Data Unit (SDU)"| Current["Layer N"]
    Current -->|"Protocol Data Unit (PDU)"| Lower["Layer N-1"]

    classDef layer fill:#f8fafc,stroke:#64748b,stroke-width:2px;
    class Upper,Current,Lower layer;
```

---

## 7. Timing & Latency Breakdown

```mermaid
gantt
    title Packet Transmission & Propagation Timeline
    dateFormat X
    axisFormat %s ms
    section Sender
    Transmission Delay (L/R) :0, 10
    section Media
    Propagation Delay (d/v)  :10, 30
    section Receiver
    Processing & Queuing     :30, 35
```

---

## 8. Failure & Recovery Sequence

```mermaid
sequenceDiagram
    autonumber
    Sender->>Receiver: Packet Transmitted
    Note over Receiver: Packet Corrupted / Lost
    Sender->>Sender: Timeout Timer Expires
    Sender->>Receiver: Retransmit Packet
    Receiver-->>Sender: ACK Received
```

---

## 9. Topology / Deployment Mapping

```mermaid
graph LR
    H1["Host 1"] --- SW["Switch / Device"]
    H2["Host 2"] --- SW
    SW --- GW["Default Gateway Router"]

    classDef dev fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    class H1,H2,SW,GW dev;
```

---

## 10. Diagnostic & Troubleshooting Workflow

```mermaid
flowchart TD
    Issue[Issue Reported] --> CheckL1{Layer 1 Healthy?}
    CheckL1 -- No --> FixCable[Check Media / Cable]
    CheckL1 -- Yes --> CheckL2{Layer 2 Addressing?}
    CheckL2 -- No --> FixL2[Check Framing & ARP]
    CheckL2 -- Yes --> CheckUpper[Check L3/L4 Routing & Services]

    classDef step fill:#f1f5f9,stroke:#475569,stroke-width:2px;
    class Issue,FixCable,FixL2,CheckUpper step;
```

---

## ⬅️ Navigation
- **Module Overview:** [README.md](README.md)
- **Deep-Dive Notes:** [notes.md](notes.md)
- **Practice Questions:** [mcqs.md](mcqs.md)
- **Next Module:** [06_Network_Devices_and_LAN](../06_Network_Devices_and_LAN/README.md)
