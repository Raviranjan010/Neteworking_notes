# TCP/IP Model - Diagrams

## 1. TCP/IP Model Complete Diagram

```
┌─────────────────────────────────────────────────────────┐
│                TCP/IP MODEL (4 Layers)                  │
│        (Transmission Control Protocol/Internet Protocol)│
└─────────────────────────────────────────────────────────┘

Layer 4  ┌──────────────────────────────────────────┐
         │       APPLICATION LAYER                  │
         │  • HTTP, FTP, SMTP, DNS, DHCP, SSH       │
         │  • User interface & network services     │
         │  • Data representation & session mgmt    │
         │  Combines OSI Layers 5, 6, 7             │
         │  Data Unit: DATA                         │
         └──────────────────┬───────────────────────┘
                            │
Layer 3  ┌──────────────────▼───────────────────────┐
         │       TRANSPORT LAYER                    │
         │  • TCP, UDP                              │
         │  • End-to-end delivery                   │
         │  • Flow control & error recovery         │
         │  • Port addressing                       │
         │  Data Unit: SEGMENT (TCP) / DATAGRAM     │
         └──────────────────┬───────────────────────┘
                            │
Layer 2  ┌──────────────────▼───────────────────────┐
         │        INTERNET LAYER                    │
         │  • IP (IPv4, IPv6)                       │
         │  • ICMP, ARP, IGMP                       │
         │  • Logical addressing & routing          │
         │  • Best-effort delivery                  │
         │  Data Unit: PACKET                       │
         └──────────────────┬───────────────────────┘
                            │
Layer 1  ┌──────────────────▼───────────────────────┐
         │     NETWORK ACCESS LAYER                 │
         │  • Ethernet, WiFi, PPP                   │
         │  • Physical transmission                 │
         │  • MAC addressing                        │
         │  • Framing & error detection             │
         │  Combines OSI Layers 1, 2                │
         │  Data Unit: FRAME                        │
         └──────────────────────────────────────────┘
```

---

## 2. OSI vs TCP/IP Model Comparison

```
OSI MODEL                  TCP/IP MODEL              PROTOCOLS
(Theoretical)              (Practical)
                                                                 
┌──────────────┐          ┌──────────────┐         
│ 7.Application│          │              │ HTTP, FTP,
│ 6.Presentation│────────▶│ 4.Application│ SMTP, DNS,
│ 5.Session    │          │              │ SSH, DHCP
├──────────────┤          ├──────────────┤         
│ 4.Transport  │────────▶│ 3.Transport  │ TCP, UDP
├──────────────┤          ├──────────────┤         
│ 3.Network    │────────▶│ 2.Internet   │ IP, ICMP,
│              │          │              │ ARP
├──────────────┤          ├──────────────┤         
│ 2.Data Link  │          │              │ Ethernet,
│ 1.Physical   │────────▶│ 1.Network    │ WiFi, PPP
│              │          │   Access     │
└──────────────┘          └──────────────┘         

7 Layers                   4 Layers
```

---

## 3. TCP/IP Protocol Stack

```
┌─────────────────────────────────────────────────────┐
│           APPLICATION LAYER                         │
│  ┌─────┬──────┬─────┬──────┬─────┬──────┬─────┐    │
│  │HTTP │HTTPS │ FTP │ SMTP │ DNS │ DHCP │ SSH │    │
│  └─────┴──────┴─────┴──────┴─────┴──────┴─────┘    │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│           TRANSPORT LAYER                           │
│  ┌────────────────────┬──────────────────────────┐  │
│  │        TCP         │          UDP             │  │
│  │  • Connection-     │  • Connectionless        │  │
│  │    oriented        │  • Unreliable            │  │
│  │  • Reliable        │  • Fast                  │  │
│  │  • Ordered         │  • No overhead           │  │
│  └────────────────────┴──────────────────────────┘  │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│           INTERNET LAYER                            │
│  ┌──────────────────────────────────────────────┐   │
│  │              IP (IPv4/IPv6)                  │   │
│  │  • Logical addressing                        │   │
│  │  • Routing                                   │   │
│  │  • Best-effort delivery                      │   │
│  ├──────────┬──────────┬────────────────────────┤   │
│  │  ICMP    │   ARP    │  IGMP                  │   │
│  └──────────┴──────────┴────────────────────────┘   │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│         NETWORK ACCESS LAYER                        │
│  ┌────────┬──────┬─────┬──────────┬──────────────┐  │
│  │Ethernet│ WiFi │ PPP │FrameRelay│     ATM      │  │
│  └────────┴──────┴─────┴──────────┴──────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

## 4. Data Flow in TCP/IP Model

```
SENDER SIDE (Encapsulation):

User Message: "GET /index.html"
      │
      ▼
┌─────────────────────────────────────┐
│ APPLICATION LAYER                   │
│ [HTTP Header] + Message             │
│ Adds: Request type, URL, version    │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ TRANSPORT LAYER (TCP)               │
│ [TCP Header] + Data                 │
│ Adds: Source Port, Dest Port (80)   │
│ Data Unit: SEGMENT                  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ INTERNET LAYER (IP)                 │
│ [IP Header] + Segment               │
│ Adds: Source IP, Dest IP            │
│ Data Unit: PACKET                   │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ NETWORK ACCESS LAYER (Ethernet)     │
│ [MAC Header] + Packet + [FCS]       │
│ Adds: Source MAC, Dest MAC          │
│ Data Unit: FRAME                    │
└──────────────┬──────────────────────┘
               │
               ▼
        Bits on wire: 01101001...

═══════════════════════════════════════
        INTERNET TRANSMISSION
═══════════════════════════════════════

               ▼
RECEIVER SIDE (Decapsulation):

┌─────────────────────────────────────┐
│ NETWORK ACCESS LAYER                │
│ Receives frame, checks MAC address  │
│ Removes MAC header                  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ INTERNET LAYER                      │
│ Checks IP address                   │
│ Removes IP header                   │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ TRANSPORT LAYER                     │
│ Checks port number (80 → HTTP)      │
│ Removes TCP header                  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│ APPLICATION LAYER                   │
│ HTTP server processes request       │
│ Delivers: "GET /index.html"         │
└─────────────────────────────────────┘
```

---

## 5. TCP vs UDP Comparison

```
TCP (Transmission Control Protocol)
┌──────────────────────────────────────┐
│ ✓ Connection-oriented                │
│   - 3-way handshake                  │
│   - SYN → SYN-ACK → ACK              │
│                                      │
│ ✓ Reliable                           │
│   - Acknowledgments                  │
│   - Retransmission                   │
│   - Error checking                   │
│                                      │
│ ✓ Ordered                            │
│   - Sequence numbers                 │
│   - Reassembly at receiver           │
│                                      │
│ ✓ Flow control                       │
│   - Sliding window                   │
│   - Congestion control               │
│                                      │
│ ✗ Slower                             │
│ ✗ More overhead                      │
│                                      │
│ Used by: HTTP, FTP, SMTP, SSH        │
└──────────────────────────────────────┘

UDP (User Datagram Protocol)
┌──────────────────────────────────────┐
│ ✓ Connectionless                     │
│   - No handshake                     │
│   - Just send                        │
│                                      │
│ ✓ Unreliable                         │
│   - No guarantees                    │
│   - Best effort                      │
│                                      │
│ ✓ No ordering                        │
│   - Fire and forget                  │
│                                      │
│ ✓ No flow control                    │
│                                      │
│ ✓ Faster                             │
│ ✓ Less overhead                      │
│                                      │
│ Used by: DNS, DHCP, Streaming, VoIP  │
│        Online Gaming                 │
└──────────────────────────────────────┘
```

---

## 6. Real-World Example: Web Browsing

```
User types: www.google.com

APPLICATION LAYER:
  Browser creates HTTP request
  DNS resolves: www.google.com → 142.250.80.46
  
TRANSPORT LAYER:
  TCP connection to port 80 (or 443 for HTTPS)
  3-way handshake: SYN → SYN-ACK → ACK
  Segments created with port numbers
  
INTERNET LAYER:
  IP adds addresses: 192.168.1.10 → 142.250.80.46
  Routes through internet routers
  Packets may take different paths
  
NETWORK ACCESS:
  Ethernet frames with MAC addresses
  Physical transmission via WiFi/cable
  
[Request reaches Google server]

Google server processes and sends response
(reverse encapsulation/decapsulation)

User sees Google homepage!
```

---

## 7. Layer Functions Summary

```
APPLICATION LAYER (What user sees)
├─ User interface
├─ Network services
├─ Data formatting
└─ Protocols: HTTP, FTP, SMTP, DNS

TRANSPORT LAYER (How data is delivered)
├─ End-to-end connection
├─ Reliability (TCP) or Speed (UDP)
├─ Port numbers
└─ Flow control

INTERNET LAYER (Where data goes)
├─ IP addressing
├─ Routing
├─ Best path selection
└─ Protocols: IP, ICMP, ARP

NETWORK ACCESS (Physical transmission)
├─ Hardware addressing (MAC)
├─ Physical media
├─ Frame creation
└─ Protocols: Ethernet, WiFi
```

---

## 8. Address Types at Each Layer

```
APPLICATION LAYER:
  URLs: www.example.com
  Email: user@example.com
  
TRANSPORT LAYER:
  Port Numbers: 80 (HTTP), 443 (HTTPS), 25 (SMTP)
  Socket: 192.168.1.10:80
  
INTERNET LAYER:
  IP Addresses: 192.168.1.10 (IPv4)
                2001:db8::1 (IPv6)
  
NETWORK ACCESS LAYER:
  MAC Addresses: 00:1A:2B:3C:4D:5E
  Physical: Ethernet cable, WiFi signal
```

---

## 9. Quick Reference Tables

### Table 1: TCP/IP Layers Overview

| Layer | Main Function | Key Protocols | Data Unit |
|-------|--------------|---------------|-----------|
| **Application** | User services | HTTP, FTP, DNS | Data |
| **Transport** | End-to-end delivery | TCP, UDP | Segment |
| **Internet** | Routing, addressing | IP, ICMP, ARP | Packet |
| **Network Access** | Physical transmission | Ethernet, WiFi | Frame |

### Table 2: OSI to TCP/IP Mapping

| TCP/IP Layer | OSI Layers | Description |
|--------------|------------|-------------|
| **Application** | 7, 6, 5 | User interface, encryption, sessions |
| **Transport** | 4 | Reliable/fast delivery |
| **Internet** | 3 | Routing and logical addressing |
| **Network Access** | 2, 1 | Physical transmission and MAC |

### Table 3: Protocol Classification

| Protocol | TCP/IP Layer | Transport Used | Purpose |
|----------|--------------|----------------|---------|
| **HTTP** | Application | TCP (80) | Web browsing |
| **HTTPS** | Application | TCP (443) | Secure web |
| **FTP** | Application | TCP (20,21) | File transfer |
| **SMTP** | Application | TCP (25) | Email sending |
| **DNS** | Application | UDP (53) | Name resolution |
| **DHCP** | Application | UDP (67,68) | IP assignment |
| **TCP** | Transport | - | Reliable delivery |
| **UDP** | Transport | - | Fast delivery |
| **IP** | Internet | - | Logical addressing |
| **ICMP** | Internet | - | Diagnostics (ping) |
| **ARP** | Internet | - | IP to MAC mapping |
| **Ethernet** | Network Access | - | Wired LAN |
| **WiFi** | Network Access | - | Wireless LAN |

---

## 10. Memory Aids

### TCP/IP Layers (Top to Bottom):
```
A  → All
P  → People (Transport sounds like "porter")
I  → In
N  → Networks

Application → Transport → Internet → Network Access
```

### When to Use TCP vs UDP:
```
Use TCP when:
  ✓ Data must arrive completely
  ✓ Order matters
  ✓ Examples: Web, Email, Files

Use UDP when:
  ✓ Speed is critical
  ✓ Some loss is acceptable
  ✓ Examples: Video, Voice, Gaming
```

### Common Port Numbers:
```
21   → FTP
22   → SSH
25   → SMTP
53   → DNS
80   → HTTP
110  → POP3
143  → IMAP
443  → HTTPS
```

---

## Quick Reference Summary

```
┌──────────────────────────────────────────────────┐
│          TCP/IP MODEL CHEATSHEET                 │
├──────────────────────────────────────────────────┤
│ 4 Layers: Application, Transport, Internet,      │
│           Network Access                         │
│                                                  │
│ TCP: Reliable, connection-oriented, slower       │
│ UDP: Fast, connectionless, unreliable            │
│                                                  │
│ Internet uses TCP/IP, not OSI                    │
│                                                  │
│ Key Protocols: HTTP(TCP:80), DNS(UDP:53),        │
│                IP, TCP, UDP, Ethernet            │
│                                                  │
│ Addresses: URL → Port → IP → MAC                 │
└──────────────────────────────────────────────────┘
```
