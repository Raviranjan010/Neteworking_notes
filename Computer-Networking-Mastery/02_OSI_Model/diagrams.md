# OSI Model - Diagrams

## 1. Complete OSI Model Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    THE OSI MODEL                            │
│              (Open Systems Interconnection)                 │
└─────────────────────────────────────────────────────────────┘

Layer 7  ┌──────────────────────────────────────────┐
         │         APPLICATION LAYER                │
         │  • User interface                        │
         │  • Network services                      │
         │  • HTTP, FTP, SMTP, DNS                  │
         │  Data Unit: DATA                         │
         └──────────────────┬───────────────────────┘
                            │
Layer 6  ┌──────────────────▼───────────────────────┐
         │       PRESENTATION LAYER                 │
         │  • Encryption/Decryption                 │
         │  • Compression                           │
         │  • Data translation                      │
         │  Data Unit: DATA                         │
         └──────────────────┬───────────────────────┘
                            │
Layer 5  ┌──────────────────▼───────────────────────┐
         │         SESSION LAYER                    │
         │  • Session management                    │
         │  • Dialog control                        │
         │  • Synchronization                       │
         │  Data Unit: DATA                         │
         └──────────────────┬───────────────────────┘
                            │
Layer 4  ┌──────────────────▼───────────────────────┐
         │       TRANSPORT LAYER                    │
         │  • End-to-end delivery                   │
         │  • Flow control                          │
         │  • Error recovery                        │
         │  • TCP, UDP                              │
         │  Data Unit: SEGMENT                      │
         └──────────────────┬───────────────────────┘
                            │
Layer 3  ┌──────────────────▼───────────────────────┐
         │        NETWORK LAYER                     │
         │  • Logical addressing (IP)               │
         │  • Routing                               │
         │  • Packet forwarding                     │
         │  • IP, ICMP, ARP                         │
         │  Data Unit: PACKET                       │
         └──────────────────┬───────────────────────┘
                            │
Layer 2  ┌──────────────────▼───────────────────────┐
         │       DATA LINK LAYER                    │
         │  • Physical addressing (MAC)             │
         │  • Error detection                       │
         │  • Framing                               │
         │  • Ethernet, PPP                         │
         │  Data Unit: FRAME                        │
         └──────────────────┬───────────────────────┘
                            │
Layer 1  ┌──────────────────▼───────────────────────┐
         │        PHYSICAL LAYER                    │
         │  • Bit transmission                      │
         │  • Cables, connectors                    │
         │  • Signal levels                         │
         │  • Ethernet, USB                         │
         │  Data Unit: BIT                          │
         └──────────────────────────────────────────┘
```

---

## 2. Encapsulation Process (Sender Side)

```
USER DATA: "Hello, World!"
      │
      ▼
┌─────────────────────────────────────────┐
│ Layer 7: APPLICATION                    │
│ [HTTP Header] + "Hello, World!"         │
│ Adds: Request type, URL, etc.           │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ Layer 6: PRESENTATION                   │
│ [SSL Header] + [Encrypted Data]         │
│ Adds: Encryption, compression           │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ Layer 5: SESSION                        │
│ [Session Header] + Data                 │
│ Adds: Session ID, checkpoints           │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ Layer 4: TRANSPORT                      │
│ [TCP Header] + Data                     │
│ Adds: Source Port, Dest Port, Seq #     │
│ Called: SEGMENT                         │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ Layer 3: NETWORK                        │
│ [IP Header] + Segment                   │
│ Adds: Source IP, Dest IP                │
│ Called: PACKET                          │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ Layer 2: DATA LINK                      │
│ [MAC Header] + Packet + [FCS Trailer]   │
│ Adds: Source MAC, Dest MAC, CRC         │
│ Called: FRAME                           │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ Layer 1: PHYSICAL                       │
│ 01001000 01100101 01101100 01101100     │
│ Converts frame to bits for transmission │
│ Called: BITS                            │
└─────────────────────────────────────────┘
                   │
                   ▼
          [TRANSMITTED OVER NETWORK]
```

---

## 3. Decapsulation Process (Receiver Side)

```
          [BITS RECEIVED FROM NETWORK]
                   │
                   ▼
┌─────────────────────────────────────────┐
│ Layer 1: PHYSICAL                       │
│ Receives bits, converts to frame        │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ Layer 2: DATA LINK                      │
│ Removes MAC header & FCS trailer        │
│ Checks for errors using CRC             │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ Layer 3: NETWORK                        │
│ Removes IP header                       │
│ Reads destination IP                    │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ Layer 4: TRANSPORT                      │
│ Removes TCP header                      │
│ Reassembles segments, checks ports      │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ Layer 5: SESSION                        │
│ Removes session header                  │
│ Manages session state                   │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ Layer 6: PRESENTATION                   │
│ Removes encryption/compression          │
│ Decrypts and decompresses data          │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ Layer 7: APPLICATION                    │
│ Removes application header              │
│ Delivers original data to application   │
│ Output: "Hello, World!"                 │
└─────────────────────────────────────────┘
```

---

## 4. Peer-to-Peer Communication

```
SENDER COMPUTER                    RECEIVER COMPUTER
┌──────────────┐                  ┌──────────────┐
│ Layer 7 (L7) │◄─ Peer ────────►│ Layer 7 (L7) │
│     ↓        │   Communication │      ↑       │
│ Layer 6 (L6) │◄─ Peer ────────►│ Layer 6 (L6) │
│     ↓        │   Communication │      ↑       │
│ Layer 5 (L5) │◄─ Peer ────────►│ Layer 5 (L5) │
│     ↓        │   Communication │      ↑       │
│ Layer 4 (L4) │◄─ Peer ────────►│ Layer 4 (L4) │
│     ↓        │   Communication │      ↑       │
│ Layer 3 (L3) │◄─ Peer ────────►│ Layer 3 (L3) │
│     ↓        │   Communication │      ↑       │
│ Layer 2 (L2) │◄─ Peer ────────►│ Layer 2 (L2) │
│     ↓        │   Communication │      ↑       │
│ Layer 1 (L1) │═════════════════►│ Layer 1 (L1) │
└──────────────┘   Physical       └──────────────┘
                   Transmission

KEY POINT:
Each layer communicates logically with its peer layer
Physical transmission only happens at Layer 1
```

---

## 5. Data Flow Example: Sending an Email

```
┌─────────────────────────────────────────────────────────┐
│ SENDER: Sending Email (user@example.com)                │
└─────────────────────────────────────────────────────────┘

Layer 7:  [SMTP: "SEND MAIL TO: recipient@example.com"]
            ↓
Layer 6:  [Encrypt with SSL/TLS]
            ↓
Layer 5:  [Start email session]
            ↓
Layer 4:  [TCP: Source Port 49152, Dest Port 25 (SMTP)]
            ↓ Adds TCP Header
Layer 3:  [IP: 192.168.1.10 → 74.125.200.108]
            ↓ Adds IP Header
Layer 2:  [MAC: AA:BB:CC:11:22:33 → AA:BB:CC:44:55:66]
            ↓ Adds MAC Header + FCS
Layer 1:  [01001011 11010010 01010101 ...]
            ↓
══════════════════════════════════════════════════════════
                    TRANSMITTED OVER INTERNET
══════════════════════════════════════════════════════════
            ↓
┌─────────────────────────────────────────────────────────┐
│ RECEIVER: Email Server Receives                         │
└─────────────────────────────────────────────────────────┘

Layer 1:  [Bits received]
            ↓
Layer 2:  [Remove MAC header, check FCS]
            ↓
Layer 3:  [Remove IP header, check destination]
            ↓
Layer 4:  [Remove TCP header, reassemble, port 25]
            ↓
Layer 5:  [Maintain session]
            ↓
Layer 6:  [Decrypt email content]
            ↓
Layer 7:  [SMTP: Deliver email to recipient's mailbox]
```

---

## 6. Devices at Each Layer

```
Layer 7  ┌──────────────────────────────────┐
         │ Gateway (Application Gateway)    │
         └──────────────────────────────────┘
              │
Layer 6      │
         ┌────┴─────────────────────────────┐
         │ Gateway                          │
         └──────────────────────────────────┘
              │
Layer 5      │
         ┌────┴─────────────────────────────┐
         │ Gateway                          │
         └──────────────────────────────────┘
              │
Layer 4  ┌────┴─────────────────────────────┐
         │ Firewall (Stateful)              │
         └──────────────────────────────────┘
              │
Layer 3  ┌────┴─────────────────────────────┐
         │ Router, Layer 3 Switch           │
         └──────────────────────────────────┘
              │
Layer 2  ┌────┴─────────────────────────────┐
         │ Switch, Bridge                   │
         └──────────────────────────────────┘
              │
Layer 1  ┌────┴─────────────────────────────┐
         │ Hub, Repeater, Cables            │
         └──────────────────────────────────┘
```

---

## 7. OSI Model Quick Reference Table

```
┌──────┬──────────────┬──────────┬─────────────────┬──────────────┐
│Layer │ Name         │ Data Unit│ Key Protocols   │ Devices      │
├──────┼──────────────┼──────────┼─────────────────┼──────────────┤
│  7   │ Application  │ Data     │ HTTP,FTP,SMTP   │ Gateway      │
│      │              │          │ DNS,DHCP,SSH    │              │
├──────┼──────────────┼──────────┼─────────────────┼──────────────┤
│  6   │ Presentation │ Data     │ SSL/TLS,        │ Gateway      │
│      │              │          │ JPEG,ASCII      │              │
├──────┼──────────────┼──────────┼─────────────────┼──────────────┤
│  5   │ Session      │ Data     │ NetBIOS,RPC     │ Gateway      │
├──────┼──────────────┼──────────┼─────────────────┼──────────────┤
│  4   │ Transport    │ Segment  │ TCP,UDP         │ Firewall     │
├──────┼──────────────┼──────────┼─────────────────┼──────────────┤
│  3   │ Network      │ Packet   │ IP,ICMP,ARP     │ Router       │
│      │              │          │ OSPF,BGP        │              │
├──────┼──────────────┼──────────┼─────────────────┼──────────────┤
│  2   │ Data Link    │ Frame    │ Ethernet,PPP    │ Switch       │
│      │              │          │                 │ Bridge       │
├──────┼──────────────┼──────────┼─────────────────┼──────────────┤
│  1   │ Physical     │ Bit      │ Ethernet,USB    │ Hub          │
│      │              │          │ DSL,Bluetooth   │ Repeater     │
└──────┴──────────────┴──────────┴─────────────────┴──────────────┘
```

---

## 8. Layer Functions Visual Summary

```
Layer 7  APPLICATION     → What you SEE (browser, email)
   ↑
Layer 6  PRESENTATION    → How it LOOKS (encryption, format)
   ↑
Layer 5  SESSION         → When to TALK (connection management)
   ↑
Layer 4  TRANSPORT       → How MUCH & HOW FAST (reliability)
   ↑
Layer 3  NETWORK         → WHICH PATH (routing, IP addresses)
   ↑
Layer 2  DATA LINK       → WHO NEXT (MAC addresses, frames)
   ↑
Layer 1  PHYSICAL        → ACTUAL BITS (cables, signals)

Upper Layers (5-7): Focus on APPLICATION needs
Middle Layer (4):   BRIDGE between application and network
Lower Layers (1-3): Focus on DATA TRANSMISSION
```

---

## 9. TCP vs UDP at Transport Layer

```
TCP (Transmission Control Protocol):
┌─────────────────────────────────────┐
│ 1. Connection-oriented              │
│    (3-way handshake)                │
│                                     │
│ 2. Reliable                         │
│    (guaranteed delivery)            │
│                                     │
│ 3. Ordered                          │
│    (sequence numbers)               │
│                                     │
│ 4. Flow control                     │
│    (sliding window)                 │
│                                     │
│ 5. Slower but dependable            │
│                                     │
│ Use: Web, Email, File Transfer      │
└─────────────────────────────────────┘

UDP (User Datagram Protocol):
┌─────────────────────────────────────┐
│ 1. Connectionless                   │
│    (no handshake)                   │
│                                     │
│ 2. Unreliable                       │
│    (best effort)                    │
│                                     │
│ 3. No ordering                      │
│                                     │
│ 4. No flow control                  │
│                                     │
│ 5. Faster but unreliable            │
│                                     │
│ Use: Video streaming, Gaming, DNS   │
└─────────────────────────────────────┘
```

---

## 10. Memory Aids

### Mnemonic (Bottom to Top - 1 to 7):
```
P  → Please
D  → Do
N  → Not
T  → Throw
S  → Sausage
P  → Pizza
A  → Away

Physical → Data Link → Network → Transport → Session → Presentation → Application
```

### Mnemonic (Top to Bottom - 7 to 1):
```
A  → All
P  → People
S  → Seem
T  → To
N  → Need
D  → Data
P  → Processing

Application → Presentation → Session → Transport → Network → Data Link → Physical
```

### Data Units Memory:
```
Layer 1: BITS         → "Basic Information Transmission System"
Layer 2: FRAMES       → "Frames Really Are Medium-sized Entities"
Layer 3: PACKETS      → "Packets Are Core Knowledge for Exams"
Layer 4: SEGMENTS     → "Segments Enable Good Movement of Network Traffic & Segments"
Layer 5-7: DATA       → "Data At The Application"
```

---

## Quick Reference Summary

```
┌──────────────────────────────────────────────────────┐
│              OSI MODEL CHEATSHEET                    │
├──────────────────────────────────────────────────────┤
│ 7 Layers: Physical, Data Link, Network, Transport,   │
│           Session, Presentation, Application         │
│                                                      │
│ Data Units: Bits → Frames → Packets → Segments → Data│
│                                                      │
│ Key Devices: Hub(L1), Switch(L2), Router(L3),        │
│              Firewall(L4), Gateway(L7)               │
│                                                      │
│ Key Protocols: TCP/UDP(L4), IP(L3), HTTP/FTP(L7)    │
│                                                      │
│ Process: Encapsulation (down), Decapsulation (up)    │
└──────────────────────────────────────────────────────┘
```
