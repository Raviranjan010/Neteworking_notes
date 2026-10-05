# 05. Data Link Layer (Part A) — Visual Architectural Diagrams

> **12 comprehensive Mermaid diagrams illustrating framing mechanics, bit/byte stuffing, CRC division, and Hamming error correction.**

```
%% --- Shared Color Palette ---
%% Primary / Core:      fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0369a1
%% Success / OK:        fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#15803d
%% Warning / Transition: fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#b45309
%% Danger / Error:      fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#b91c1c
%% Neutral / Secondary: fill:#f1f5f9,stroke:#64748b,stroke-width:2px,color:#334155
```

---

## 1. IEEE 802 Sublayer Architecture (LLC vs. MAC)
*Notice how the LLC sublayer decouples upper network protocols from physical media technologies.*

```mermaid
flowchart TD
    L3["Network Layer Protocols<br/>(IPv4, IPv6, ARP)"]
    
    subgraph L2["Data Link Layer (Layer 2)"]
        LLC["Logical Link Control (LLC — IEEE 802.2)<br/>Multiplexing, Flow Control, Service Access Points"]
        
        subgraph MAC_Sub["MAC Sublayer"]
            Eth["Ethernet MAC<br/>(IEEE 802.3)"]
            WiFi["Wi-Fi MAC<br/>(IEEE 802.11)"]
            Other["Other Link MAC<br/>(802.15, LTE L2)"]
        end
    end

    subgraph L1["Physical Layer (Layer 1)"]
        PHY1["1000BASE-T / Optical Fiber"]
        PHY2["2.4 GHz / 5 GHz / 6 GHz RF"]
    end

    L3 --> LLC
    LLC --> Eth
    LLC --> WiFi
    LLC --> Other
    Eth --> PHY1
    WiFi --> PHY2

    classDef l3 fill:#e0e7ff,stroke:#4338ca,stroke-width:2px;
    classDef l2 fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    classDef l1 fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    class L3 l3;
    class LLC,Eth,WiFi,Other l2;
    class PHY1,PHY2 l1;
```

**How to Read It:**
- LLC handles logical multiplexing across diverse physical media.
- Ethernet and Wi-Fi run distinct MAC sublayers but present an identical LLC interface to IPv4/IPv6.

---

## 2. Character Count Framing Failure Cascade
*Notice how a single corrupted count byte permanently desynchronizes all subsequent frames.*

```mermaid
flowchart TD
    Original["Transmitted: [ 5 | A | B | C | D ] [ 4 | E | F | G ]"]
    Corrupt["Corrupted on wire: First byte 5 flips to 6"]
    RxRead["Receiver reads length 6: [ A, B, C, D, E ]"]
    CascadeError["Next byte read as length is 'F'! Receiver permanently desynchronized."]

    Original --> Corrupt --> RxRead --> CascadeError

    classDef bad fill:#fee2e2,stroke:#dc2626,stroke-width:2px;
    class Corrupt,CascadeError bad;
```

**How to Read It:**
- Character count has zero resilience against transmission errors; modern protocols use delimiter flags instead.

---

## 3. Byte Stuffing & Destuffing Pipeline
*Notice how the transmitter inserts ESC bytes to prevent data bytes from triggering frame delimiters.*

```mermaid
sequenceDiagram
    autonumber
    actor S as Sender Application
    participant TX as Link Transmitter
    participant Wire as Physical Channel
    participant RX as Link Receiver
    actor D as Destination Application

    S->>TX: Raw Data: [ A, FLAG, B, ESC, C ]
    Note over TX: Prepend ESC to FLAG -> [ESC, FLAG]<br/>Prepend ESC to ESC -> [ESC, ESC]
    TX->>Wire: Transmit: [ FLAG | A | ESC | FLAG | B | ESC | ESC | C | FLAG ]
    Wire->>RX: Received Stuffed Frame
    Note over RX: Strip Framing FLAGs.<br/>When ESC encountered, remove ESC and preserve next byte.
    RX->>D: Recovered Data: [ A, FLAG, B, ESC, C ]
```

**How to Read It:**
- Escape bytes guarantee data transparency for arbitrary 8-bit binary payloads.

---

## 4. HDLC Bit Stuffing State Machine
*Notice how the hardware detects five consecutive 1s and automatically inserts a 0.*

```mermaid
stateDiagram-v2
    [*] --> Idle: Init / Zero Received
    Idle --> One1: Read '1'
    One1 --> Two1: Read '1'
    Two1 --> Three1: Read '1'
    Three1 --> Four1: Read '1'
    Four1 --> Five1: Read '1'
    
    Five1 --> StuffZero: Auto-inject '0' (Bit Stuffing)
    StuffZero --> Idle: Continue transmission
    
    One1 --> Idle: Read '0'
    Two1 --> Idle: Read '0'
    Three1 --> Idle: Read '0'
    Four1 --> Idle: Read '0'
```

**How to Read It:**
- The pattern of six consecutive $1$s (`01111110`) is reserved exclusively for frame boundary delimiters.

---

## 5. 2-Dimensional Parity Grid Error Detection & Correction
*Notice how the intersection of row and column parity errors pinpoints the exact corrupted bit.*

```mermaid
flowchart TD
    subgraph Grid["2D Parity Matrix"]
        R1["Row 1: [ 1  0  1  1 ] -> Row Parity: 1"]
        R2["Row 2: [ 0  X  1  0 ] -> Row Parity: 0 (PARITY ERROR!)"]
        R3["Row 3: [ 1  1  0  1 ] -> Row Parity: 1"]
        Col["Col Par: [ 0  ERR 0  0 ]"]
    end

    R2 --> Locate["Intersection: Row 2, Column 2"]
    Col --> Locate
    Locate --> Flip["Invert bit at (Row 2, Col 2): 0 <-> 1 (Bit Corrected!)"]

    classDef err fill:#fee2e2,stroke:#dc2626,stroke-width:2px;
    classDef fix fill:#dcfce7,stroke:#16a34a,stroke-width:2px;
    class R2,Col err;
    class Flip fix;
```

**How to Read It:**
- 2D parity detects up to 3 errors and provides single-bit forward error correction.

---

## 6. Internet Checksum Generation & Verification Flow
*Notice how end-around carry preserves carry bits in 1's complement arithmetic.*

```mermaid
flowchart TD
    W["16-bit Data Words (W1, W2, ... Wn)"] --> Sum["Sum all 16-bit Words"]
    Sum --> CarryCheck{Carry out of Bit 15?}
    CarryCheck -- Yes --> Wrap["Add carry bit to LSB (End-Around Carry)"]
    Wrap --> CarryCheck
    CarryCheck -- No --> Invert["Bitwise NOT (One's Complement)"]
    Invert --> Checksum["16-bit Checksum Transmitted"]

    subgraph Receiver["Receiver Check"]
        RxSum["Sum all words + Checksum"] --> RxCheck{Result == 0xFFFF?}
        RxCheck -- Yes --> OK["Packet Error-Free"]
        RxCheck -- No --> Drop["Discard Corrupted Packet"]
    end

    Checksum --> RxSum

    classDef ok fill:#dcfce7,stroke:#16a34a,stroke-width:2px;
    classDef bad fill:#fee2e2,stroke:#dc2626,stroke-width:2px;
    class OK ok;
    class Drop bad;
```

**How to Read It:**
- If no bit errors occurred, summing the data and the checksum yields all 1s (`0xFFFF`).

---

## 7. CRC Modulo-2 Polynomial Division Architecture
*Notice how polynomial division is executed entirely with XOR operations without borrows.*

```mermaid
flowchart LR
    Data["Data Bits D(x)<br/>(k bits)"] --> AppendZeros["Append r Zeros<br/>D(x) * x^r"]
    AppendZeros --> XORDiv["Modulo-2 XOR Long Division<br/>Divided by Generator G(x) (r+1 bits)"]
    XORDiv --> Rem["Remainder R(x)<br/>(r bits = FCS)"]
    Rem --> Codeword["Transmitted Codeword T(x)<br/>[ Data (k bits) | FCS (r bits) ]"]

    classDef prim fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    class Data,AppendZeros,XORDiv,Rem,Codeword prim;
```

**How to Read It:**
- The degree of the generator polynomial determines the exact number of appended zero bits.

---

## 8. Hardware Linear Feedback Shift Register (LFSR) for CRC
*Notice how hardware shift registers compute 32-bit CRC at line rate using XOR gates.*

```mermaid
flowchart LR
    BitIn([Serial Bit In]) --> XOR1((XOR))
    XOR1 --> FF0["Flip-Flop 0"]
    FF0 --> FF1["Flip-Flop 1"]
    FF1 --> XOR2((XOR))
    XOR2 --> FF2["Flip-Flop 2"]
    FF2 --> Out([Feedback Line])
    Out --> XOR1
    Out --> XOR2

    classDef reg fill:#f1f5f9,stroke:#475569,stroke-width:2px;
    class FF0,FF1,FF2 reg;
```

**How to Read It:**
- Tap positions correspond directly to non-zero coefficients of the generator polynomial $G(x)$.

---

## 9. Hamming Distance Geometric Codeword Sphere Model
*Notice why error correction requires twice the distance of error detection.*

```mermaid
flowchart TD
    subgraph DetModel["Detection: d_min >= d + 1"]
        C1["Valid Codeword A"] ---|"Distance d"| Corrupt["Corrupted Vector"]
        Corrupt ---|"Distance 1"| C2["Valid Codeword B"]
    end

    subgraph CorrModel["Correction: d_min >= 2t + 1"]
        SphereA["Sphere A around Codeword A (Radius t)"]
        Disjoint["Non-overlapping Boundary"]
        SphereB["Sphere B around Codeword B (Radius t)"]
        SphereA --- Disjoint --- SphereB
    end

    classDef c fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    class C1,C2,SphereA,SphereB c;
```

**How to Read It:**
- Error correction demands non-intersecting spheres of radius $t$ centered on valid codewords.

---

## 10. Hamming(7,4) Bit Position & Coverage Matrix
*Notice how parity bits sit at powers of 2 ($1, 2, 4$) and cover specific data bit combinations.*

```mermaid
flowchart TB
    subgraph Bits["Codeword Bit Positions (1 to 7)"]
        P1["Bit 1: P1 (001)"]
        P2["Bit 2: P2 (010)"]
        D3["Bit 3: D3 (011)"]
        P4["Bit 4: P4 (100)"]
        D5["Bit 5: D5 (101)"]
        D6["Bit 6: D6 (110)"]
        D7["Bit 7: D7 (111)"]
    end

    P1 -.->|Covers| D3
    P1 -.->|Covers| D5
    P1 -.->|Covers| D7

    P2 -.->|Covers| D3
    P2 -.->|Covers| D6
    P2 -.->|Covers| D7

    P4 -.->|Covers| D5
    P4 -.->|Covers| D6
    P4 -.->|Covers| D7

    classDef p fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    classDef d fill:#e0f2fe,stroke:#0284c7,stroke-width:2px;
    class P1,P2,P4 p;
    class D3,D5,D6,D7 d;
```

**How to Read It:**
- Data bit 7 ($111_2$) is checked by all three parity bits because $1, 2,$ and $4$ are all in its binary expansion.

---

## 11. Syndrome Decoding & Error Location Flow
*Notice how evaluating parity checks produces a binary integer pointing to the corrupted bit.*

```mermaid
flowchart TD
    RxBits["Received Codeword: [r1, r2, r3, r4, r5, r6, r7]"] --> SynCalc["Compute Syndrome:<br/>s1 = r1 ^ r3 ^ r5 ^ r7<br/>s2 = r2 ^ r3 ^ r6 ^ r7<br/>s4 = r4 ^ r5 ^ r6 ^ r7"]
    SynCalc --> SynVec["Syndrome S = (s4 s2 s1)_2"]
    SynVec --> CheckZero{S == 0?}
    CheckZero -- Yes --> Valid["No Error Detected -> Extract Data Bits"]
    CheckZero -- No --> ErrorPos["Error at Bit Position S!"]
    ErrorPos --> FlipBit["Flip Bit r_S (0 <-> 1) -> Data Recovered"]

    classDef ok fill:#dcfce7,stroke:#16a34a,stroke-width:2px;
    classDef err fill:#fee2e2,stroke:#dc2626,stroke-width:2px;
    class Valid ok;
    class ErrorPos,FlipBit err;
```

**How to Read It:**
- If $S = 5$ (`101`), bit 5 flipped during transmission. Inverting bit 5 restores the original payload.

---

## 12. Link-Layer Diagnostic Workflow for CRC Errors
*Notice the systematic physical-to-logical troubleshooting path for link-layer errors.*

```mermaid
flowchart TD
    Alert["High FCS / CRC Error Counter on Switch Port"] --> CableCheck{Replace Patch Cable?}
    CableCheck -- Fixed --> BadCable["Root Cause: Damaged RJ45 or Optical Fiber Bend"]
    CableCheck -- Persists --> DuplexCheck{Duplex Mismatch?<br/>(Half vs Full)}
    DuplexCheck -- Yes --> FixDuplex["Fix Duplex Setting on Interface"]
    DuplexCheck -- No --> CheckEMI{Near High-Voltage Motor / EMI?}
    CheckEMI -- Yes --> Shield["Install Shielded STP / Re-route Cable"]
    CheckEMI -- No --> PortASIC["Faulty Switch Port Transceiver ASIC"]

    classDef warn fill:#fef3c7,stroke:#d97706,stroke-width:2px;
    class Alert,CableCheck,DuplexCheck,CheckEMI warn;
```

**How to Read It:**
- CRC errors indicate physical layer corruption before frame processing at Layer 2.

---

## ⬅️ Navigation
- **Module Overview:** [README.md](README.md)
- **Deep-Dive Notes:** [notes.md](notes.md)
- **Solved Numericals:** [numericals.md](numericals.md)
- **Practice Questions:** [mcqs.md](mcqs.md)
- **Next Sub-step:** [05b Flow Control & ARQ](../05_Data_Link_Layer/)
