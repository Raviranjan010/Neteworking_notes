# 02. The OSI 7-Layer Model — One-Page Cheatsheet

> **Quick revision sheet for university exams, GATE, and technical interview screens.**

---

## ⚡ The 7 Layers at a Glance

| # | Layer Name | PDU | Primary Function | Addressing | Operating Devices | Key Protocols |
|:---:|---|:---:|---|:---:|---|---|
| **7** | **Application** | Data | User network services & UI | URI / URL | WAF, API Gateway, Reverse Proxy | HTTP, HTTPS, DNS, DHCP, SSH, SMTP, BGP, RIP |
| **6** | **Presentation** | Data | Syntax, encryption, compression | Syntax tags | OS Runtimes, Middleware | JSON, XML, ASCII, UTF-8, JPEG, gzip |
| **5** | **Session** | Data | Dialog control & checkpoints | Sockets / Session IDs | OS Network Subsystem | RPC, NetBIOS, SOCKS5 |
| **4** | **Transport** | Segment / Datagram | End-to-end reliability & ports | 16-bit Port (0–65535) | L4 Firewall, L4 Load Balancer | TCP, UDP, SCTP, QUIC |
| **3** | **Network** | Packet | Routing & logical addressing | 32-bit IP / 128-bit IPv6 | Router, Layer 3 Switch | IPv4, IPv6, ICMP, IGMP, ARP, RARP, OSPF |
| **2** | **Data Link** | Frame | Hop-to-hop framing & error check | 48-bit MAC Address | Layer 2 Switch, Bridge, NIC | Ethernet (802.3), Wi-Fi (802.11 MAC) |
| **1** | **Physical** | Bit | Raw bit signaling over media | None | Multiport Hub, Repeater, Modem | 1000BASE-T, Cables, Fiber, RJ45 |

---

## 📦 Encapsulation Overhead Breakdown

| Layer | Header / Trailer Added | Size | Key Fields Contained |
|---|---|:---:|---|
| **L4 (Transport)** | TCP Header | **20 Bytes** (up to 60) | Src/Dst Port, Seq #, Ack #, Flags (SYN/ACK/FIN), Window |
| **L4 (Transport)** | UDP Header | **8 Bytes** (fixed) | Src/Dst Port, Length, Checksum |
| **L3 (Network)** | IPv4 Header | **20 Bytes** (up to 60) | Version, IHL, Total Length, TTL, Protocol, Src/Dst IP |
| **L3 (Network)** | IPv6 Header | **40 Bytes** (fixed) | Version, Traffic Class, Flow Label, Next Header, Src/Dst IP |
| **L2 (Data Link)** | Ethernet II Header | **14 Bytes** | Destination MAC (6B), Source MAC (6B), EtherType (2B) |
| **L2 (Data Link)** | Ethernet FCS Trailer | **4 Bytes** | 32-bit CRC Error Checksum |

> **Total Overhead for TCP/IPv4 over Ethernet:**  
> $$14\text{ (Eth Hdr)} + 20\text{ (IP)} + 20\text{ (TCP)} + 4\text{ (Eth Trailer)} = 58\text{ Bytes}$$

---

## 🧠 Mnemonics & Memory Tricks

- **Layer Order (Bottom $\rightarrow$ Top, 1 to 7):**  
  **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way  
  *(Physical, Data Link, Network, Transport, Session, Presentation, Application)*
- **Layer Order (Top $\rightarrow$ Bottom, 7 to 1):**  
  **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing  
  *(Application, Presentation, Session, Transport, Network, Data Link, Physical)*
- **PDU Order (Bottom $\rightarrow$ Top):**  
  **B**ig **F**rogs **P**ound **S**weet **D**esserts  
  *(**B**its $\rightarrow$ **F**rames $\rightarrow$ **P**ackets $\rightarrow$ **S**egments $\rightarrow$ **D**ata)*

---

## ⚠️ Top 5 Conceptual Traps

1. **"Gateway = L7 device":** Misleading. A **Default Gateway** is a Layer 3 router. An **API/Protocol Gateway** is a Layer 7 proxy.
2. **"TLS = Layer 6":** In reality, TLS operates as an intermediate security session layer between Layer 4 (TCP) and Layer 7 (HTTP).
3. **"Firewall = Layer 4":** Firewalls exist at L3 (packet filter), L4 (stateful inspection), and L7 (WAF).
4. **"MAC changes vs. IP changes":** When crossing routers, **MAC addresses are rewritten at every hop**; IP addresses remain unchanged end-to-end.
5. **"Ping test":** Pinging by IP tests Layers 1, 2, and 3. If IP ping works but domain ping fails, the problem is strictly **Layer 7 DNS**.

---

## 🎯 Systematic Troubleshooting Decision Tree

```
1. Ping Default Gateway (192.168.1.1)
   ├── Fails?  ──> Check L1 (Cable/Lights) ──> Check L2 (VLAN/ARP) ──> Check L3 (Subnet Mask)
   └── Passes? ──> Layers 1, 2, and 3 are 100% HEALTHY!
                   │
2. Ping External IP (8.8.8.8)
   ├── Fails?  ──> L3 Default Route / ISP Outage
   └── Passes? ──> External L3 routing is HEALTHY!
                   │
3. Test DNS Resolution (nslookup google.com)
   ├── Fails?  ──> Layer 7 DNS failure (/etc/resolv.conf)
   └── Passes? ──> DNS is HEALTHY!
                   │
4. Test TCP Port Connection (curl -v / telnet host 443)
   ├── Fails?  ──> Layer 4 Firewall blocking port or web daemon stopped
   └── Passes? ──> Check Layer 7 HTTP Status Codes (500/502/404)
```
