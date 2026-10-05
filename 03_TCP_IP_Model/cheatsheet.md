# 03. The TCP/IP Protocol Suite — One-Page Cheatsheet

> **Quick revision sheet for university exams, GATE CS/IT, and technical interview screens.**

---

## ⚡ TCP/IP Architectural Layers at a Glance

| Layer # (5-Layer) | Layer Name | DoD 4-Layer Equivalent | PDU | Key Protocols | Operating Devices / Entities |
|:---:|---|---|:---:|---|---|
| **5** | **Application** | Application | Data / Stream | HTTP(S), DNS, DHCP, SSH, SMTP, BGP, RIP | Browser, WAF, API Gateway, DNS Server |
| **4** | **Transport** | Host-to-Host | Segment (TCP) / Datagram (UDP) | TCP, UDP, SCTP, QUIC | OS Kernel TCP Stack, L4 Load Balancer |
| **3** | **Network (Internet)**| Internet | Packet / Datagram | IPv4, IPv6, ICMP, IGMP, OSPF, ARP, RARP | Router, Layer 3 Switch |
| **2** | **Data Link** | Network Access | Frame | Ethernet (802.3), Wi-Fi (802.11), PPP | Layer 2 Switch, Bridge, NIC |
| **1** | **Physical** | Network Access | Bit | 1000BASE-T, Fiber, Radio (RF) | Hub, Repeater, PHY Transceiver |

---

## 🧭 The Tricky Protocol-to-Layer Matrix

| Protocol | Function | Lower-Layer Transport Encapsulation | Official Architectural Layer |
|---|---|---|---|
| **ARP** | Resolves IPv4 $\rightarrow$ MAC | Direct Ethernet (`EtherType = 0x0806`) | **Layer 3 (Network Layer)** *(Note: in practice sits between L2 and L3)* |
| **RARP** | Resolves MAC $\rightarrow$ IPv4 | Direct Ethernet (`EtherType = 0x8035`) | **Layer 3 (Network Layer)** *(Note: legacy L3 resolution)* |
| **ICMP** | Diagnostics & error reporting | Direct IPv4 (`Protocol = 1`) | **Layer 3 (Network Layer)** |
| **IGMP** | Multicast group membership | Direct IPv4 (`Protocol = 2`) | **Layer 3 (Network Layer)** |
| **OSPF** | Link-state interior routing | Direct IPv4 (`Protocol = 89`) | **Layer 3 (Network Layer)** |
| **DHCP** | Dynamic IP configuration | UDP (Ports `67` server, `68` client) | **Layer 7 (Application)** providing L3 service |
| **DNS** | Domain name $\rightarrow$ IP resolution| UDP / TCP (Port `53`) | **Layer 7 (Application)** |
| **RIP** | Distance-vector interior routing| UDP (Port `520`) | **Layer 7 (Application)** providing L3 routing |
| **BGP** | Path-vector exterior routing | TCP (Port `179`) | **Layer 7 (Application)** providing L3 routing |

---

## 🔄 Packet Invariance: What Changes Across Router Hops?

```
Sender (Host A)  -->  [Router 1]  -->  [Router 2]  -->  Receiver (Host B)
```

| Packet Field | Layer | Changes Hop-by-Hop? | Behavior / Notes |
|---|:---:|:---:|---|
| **Payload Data** | L7–L4 | ❌ **NO** | End-to-end data integrity preserved. |
| **Source / Destination Port** | L4 | ❌ **NO** | Invariant end-to-end *(unless NAT/PAT is active)*. |
| **TCP Sequence / Ack #** | L4 | ❌ **NO** | Invariant end-to-end. |
| **Source / Destination IP** | L3 | ❌ **NO** | Invariant end-to-end *(unless NAT is active)*. |
| **IPv4 TTL / IPv6 Hop Limit**| L3 | ✅ **YES** | Decremented by 1 at each router hop; dropped if 0. |
| **IPv4 Header Checksum** | L3 | ✅ **YES** | Recomputed at each hop due to TTL decrement. |
| **Source MAC Address** | L2 | ✅ **YES** | Rewritten to the router's outgoing interface MAC. |
| **Destination MAC Address** | L2 | ✅ **YES** | Rewritten to next hop router's incoming MAC (or host MAC). |
| **Frame FCS (CRC-32)** | L2 | ✅ **YES** | Recomputed over the rewritten Ethernet frame header. |

---

## 🔢 Well-Known Numbers Quick Reference

### Layer 3 IP Protocol Numbers (Stored in IPv4 `Protocol` / IPv6 `Next Header`)
- **`1`**: ICMP
- **`2`**: IGMP
- **`6`**: TCP
- **`17`**: UDP
- **`89`**: OSPF

### Layer 4 Well-Known Port Numbers (IANA 0–1023)
- **`20 / 21`**: FTP (Data / Control)
- **`22`**: SSH / SFTP
- **`23`**: Telnet (insecure plain text)
- **`25`**: SMTP (Mail transfer)
- **`53`**: DNS (UDP for queries $\le$ 512B; TCP for zone transfers and large responses)
- **`67 / 68`**: DHCP (67 = Server, 68 = Client)
- **`80`**: HTTP
- **`110`**: POP3
- **`123`**: NTP (Network Time Protocol)
- **`143`**: IMAP
- **`161 / 162`**: SNMP (Queries / Traps)
- **`179`**: BGP
- **`443`**: HTTPS
- **`520`**: RIP

---

## ⚡ IPv4 vs IPv6 Header Comparison

| Property | IPv4 | IPv6 |
|---|---|---|
| **Address Length** | 32 bits (4 bytes) | 128 bits (16 bytes) |
| **Base Header Size** | Variable (20–60 bytes) | Fixed **40 bytes** |
| **Header Checksum** | Included (checked at every hop) | **Removed** (relies on L2 CRC + L4 Checksum) |
| **Fragmentation** | Performed by routers & sender | **Sender only** (via PMTUD; no router fragmentation) |
| **Local Broadcast** | Yes (`255.255.255.255`) | **Removed** (replaced by Multicast) |
| **Address Resolution** | ARP (L2 broadcast) | NDP (ICMPv6 multicast) |
| **Auto-configuration** | DHCP / Manual | SLAAC + DHCPv6 |

---

## 🛠️ Essential CLI Diagnostic Tools

| Command | Protocol Used | Underlying Mechanism / Purpose |
|---|---|---|
| `ping <ip>` | ICMP (Type 8 / 0) | Tests L3 end-to-end reachability and round-trip time. |
| `traceroute <ip>` *(Linux)* | UDP / ICMP | Sends TTL=1, 2, 3... to reveal intermediate router hops. |
| `tracert <ip>` *(Windows)* | ICMP Echo Request | Sends TTL=1, 2, 3... to reveal intermediate router hops. |
| `arp -a` | ARP | Displays the local OS cache of IP-to-MAC mappings. |
| `netstat -tuln` / `ss -tuln`| TCP / UDP | Lists all listening ports and established sockets. |
| `dig <host>` / `nslookup` | DNS (UDP/TCP 53) | Queries DNS nameservers for resource records (A, AAAA, MX). |
| `curl -Iv <url>` | HTTP/HTTPS | Inspects HTTP response headers, TLS handshake, and L7 status. |

---

## ⚠️ Top 5 Exam & Interview Traps

1. **"Ping uses UDP or TCP":** False! Ping uses **ICMP directly over IP** (Protocol 1). It has no transport layer ports.
2. **"Traceroute routers respond because of ping":** False! Routers respond with ICMP Type 11 because the probe packet's **TTL expired to 0** at their interface.
3. **"What layer does ARP belong to?":** For all standard exams (GATE, university curricula), the EXAM answer is strictly **Network Layer (Layer 3)** (enables L3 logical addressing). Real-world note: In practice, it sits between L2 and L3 (Layer 2.5) because it encapsulates directly into Ethernet frames (`EtherType 0x0806`) without an IP header.
4. **"Routers change IP addresses":** Standard IP routers **never** modify source or destination IP addresses. Only NAT/PAT routers do.
5. **"BGP and RIP are Layer 3 protocols":** Exam answer: **Application Layer** (BGP runs on TCP port 179; RIP runs on UDP port 520). Note: Functionally they compute routing paths for Layer 3, but their software implementation resides at Layer 7.
