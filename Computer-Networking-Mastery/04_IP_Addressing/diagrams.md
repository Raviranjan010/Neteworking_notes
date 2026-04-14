# IP Addressing - Diagrams

## 1. IPv4 Address Structure

```
IPv4 Address: 192.168.1.10

┌─────────┬─────────┬─────────┬─────────┐
│  192    │  168    │    1    │   10    │
│ 8 bits  │ 8 bits  │ 8 bits  │ 8 bits  │
└─────────┴─────────┴─────────┴─────────┘
     │         │         │         │
   Octet 1   Octet 2   Octet 3   Octet 4

Binary: 11000000.10101000.00000001.00001010

Total: 32 bits = 4 bytes
```

---

## 2. IP Address Classes

```
CLASS A:  1.x.x.x  to  126.x.x.x
┌──────┬──────┬──────┬──────┐
│ Net  │ Host │ Host │ Host │
│      │      │      │      │
└──────┴──────┴──────┴──────┘
Supports: 16,777,214 hosts
Used by: Very large organizations

CLASS B:  128.x.x.x  to  191.x.x.x
┌──────┬──────┬──────┬──────┐
│ Net  │ Net  │ Host │ Host │
│      │      │      │      │
└──────┴──────┴──────┴──────┘
Supports: 65,534 hosts
Used by: Large organizations, universities

CLASS C:  192.x.x.x  to  223.x.x.x
┌──────┬──────┬──────┬──────┐
│ Net  │ Net  │ Net  │ Host │
│      │      │      │      │
└──────┴──────┴──────┴──────┘
Supports: 254 hosts
Used by: Small networks, homes

CLASS D:  224.x.x.x  to  239.x.x.x (Multicast)
CLASS E:  240.x.x.x  to  255.x.x.x (Experimental)
```

---

## 3. Subnet Mask Visualization

```
IP Address:    192.168.1.10
Subnet Mask:   255.255.255.0

┌─────────────────────────────────────────┐
│ IP:   192  .  168  .   1   .   10      │
│       11000000.10101000.00000001.00001010│
│ Mask: 255  .  255  . 255  .    0       │
│       11111111.11111111.11111111.00000000│
│       └────NETWORK────┘└──HOST──┘      │
└─────────────────────────────────────────┘

255 = Network portion (bits must match)
0   = Host portion (bits can vary)

Network Address: 192.168.1.0
Broadcast Address: 192.168.1.255
Usable Hosts: 192.168.1.1 to 192.168.1.254
```

---

## 4. Private vs Public IP Addresses

```
PRIVATE IP ADDRESSES (Internal Use Only):
┌────────────────────────────────────────┐
│ Class A: 10.0.0.0 - 10.255.255.255    │
│           (10.0.0.0/8)                 │
│                                        │
│ Class B: 172.16.0.0 - 172.31.255.255  │
│            (172.16.0.0/12)             │
│                                        │
│ Class C: 192.168.0.0 - 192.168.255.255│
│            (192.168.0.0/16)            │
│                                        │
│ ✗ Cannot access Internet directly      │
│ ✓ Free to use internally               │
│ ✓ Not routable on Internet             │
└────────────────────────────────────────┘

PUBLIC IP ADDRESSES (Internet):
┌────────────────────────────────────────┐
│ All other IP addresses                 │
│ (except special ranges)                │
│                                        │
│ Examples:                              │
│ 8.8.8.8 (Google DNS)                  │
│ 1.1.1.1 (Cloudflare DNS)              │
│                                        │
│ ✓ Globally unique                      │
│ ✓ Routable on Internet                 │
│ ✗ Must be allocated/purchased          │
└────────────────────────────────────────┘

NAT (Network Address Translation):
[Private Network] → [NAT Router] → [Internet]
192.168.1.10     → 203.0.113.5   → Web Server
```

---

## 5. Special IP Addresses

```
┌──────────────────────────────────────────┐
│ SPECIAL IP ADDRESSES                     │
├──────────────────────────────────────────┤
│ 127.0.0.1                                │
│ Loopback (localhost)                     │
│ "Talk to yourself"                       │
│ Used for testing                         │
├──────────────────────────────────────────┤
│ 0.0.0.0                                  │
│ Default/Unspecified address              │
│ "Any address"                            │
├──────────────────────────────────────────┤
│ 255.255.255.255                          │
│ Limited Broadcast                        │
│ "Send to everyone on local network"      │
├──────────────────────────────────────────┤
│ 169.254.x.x                              │
│ APIPA (Automatic Private IP)             │
│ "DHCP failed, self-assigned"             │
├──────────────────────────────────────────┤
│ 192.168.1.0                              │
│ Network Address                          │
│ "Identifies the network itself"          │
├──────────────────────────────────────────┤
│ 192.168.1.255                            │
│ Broadcast Address                        │
│ "Send to all hosts on network"           │
└──────────────────────────────────────────┘
```

---

## 6. IPv4 vs IPv6 Comparison

```
IPv4                          IPv6
┌──────────────────┐         ┌──────────────────┐
│ 32-bit address   │         │ 128-bit address  │
│                  │         │                  │
│ 192.168.1.1      │         │ 2001:0db8::1     │
│ (Dotted decimal) │         │ (Hexadecimal)    │
│                  │         │                  │
│ 4.3 billion      │         │ 3.4 × 10^38      │
│ addresses        │         │ addresses        │
│                  │         │                  │
│ 4 octets         │         │ 8 groups         │
│ 192.168.1.1      │         │ 2001:0db8:85a3:: │
│                  │         │ 8a2e:0370:7334   │
│                  │         │                  │
│ Has broadcast    │         │ No broadcast     │
│ Manual/DHCP      │         │ Auto-configure   │
│                  │         │                  │
│ Subnet masks     │         │ Prefix length    │
│ 255.255.255.0    │         │ /64, /48, etc.   │
└──────────────────┘         └──────────────────┘

IPv6 Simplification:
2001:0db8:0000:0000:0000:0000:0000:0001
↓ Remove leading zeros
2001:db8:0:0:0:0:0:1
↓ Replace consecutive zeros with ::
2001:db8::1
```

---

## 7. Network and Host Portions

```
Example: 192.168.1.10/24

Subnet Mask: 255.255.255.0 (/24)
             └──┬──┘ └─┬─┘
             Network Host

Binary:
IP:    11000000.10101000.00000001.00001010
Mask:  11111111.11111111.11111111.00000000
       └─────NETWORK─────┘└──HOST──┘

Network Address:  192.168.1.0   (host bits = 0)
First Usable:     192.168.1.1
Last Usable:      192.168.1.254
Broadcast:        192.168.1.255 (host bits = 1)

Total Hosts: 2^8 = 256
Usable Hosts: 256 - 2 = 254
```

---

## 8. Binary to Decimal Conversion

```
Bit Positions:  128  64  32  16  8   4   2   1

Example 1: 192
Binary:     1    1   0   0   0   0   0   0
Decimal:    128 + 64 = 192

Example 2: 168
Binary:     1    0   1   0   1   0   0   0
Decimal:    128 + 32 + 8 = 168

Example 3: 255
Binary:     1    1   1   1   1   1   1   1
Decimal:    128+64+32+16+8+4+2+1 = 255

Quick Reference:
0   = 00000000
128 = 10000000
192 = 11000000
224 = 11100000
240 = 11110000
248 = 11111000
252 = 11111100
254 = 11111110
255 = 11111111
```

---

## 9. Class Identification Flowchart

```
Given IP Address: A.B.C.D

Look at First Octet (A):

A = ?
│
├─ 1-126?   → Class A
│            Default Mask: 255.0.0.0 (/8)
│            Format: N.H.H.H
│
├─ 127?     → Loopback (Special)
│            Not usable for hosts
│
├─ 128-191? → Class B
│            Default Mask: 255.255.0.0 (/16)
│            Format: N.N.H.H
│
├─ 192-223? → Class C
│            Default Mask: 255.255.255.0 (/24)
│            Format: N.N.N.H
│
├─ 224-239? → Class D (Multicast)
│            Not for regular hosts
│
└─ 240-255? → Class E (Experimental)
             Reserved for research
```

---

## 10. IP Address Allocation Hierarchy

```
IANA (Internet Assigned Numbers Authority)
│
└─▶ Regional Internet Registries (RIRs)
    │
    ├─▶ ARIN (North America)
    ├─▶ RIPE NCC (Europe)
    ├─▶ APNIC (Asia-Pacific)
    ├─▶ LACNIC (Latin America)
    └─▶ AfriNIC (Africa)
        │
        └─▶ ISPs (Internet Service Providers)
            │
            └─▶ Organizations/Businesses
                │
                └─▶ End Users/Devices
```

---

## Quick Reference Tables

### Table 1: IP Classes Summary

| Class | Range | Networks | Hosts/Net | Default Mask | Use Case |
|-------|-------|----------|-----------|--------------|----------|
| **A** | 1-126 | 126 | 16.7M | 255.0.0.0 | Very large |
| **B** | 128-191 | 16,384 | 65,534 | 255.255.0.0 | Large |
| **C** | 192-223 | 2M+ | 254 | 255.255.255.0 | Small |
| **D** | 224-239 | - | - | - | Multicast |
| **E** | 240-255 | - | - | - | Experimental |

### Table 2: Private IP Ranges

| Class | Range | CIDR | Total Addresses |
|-------|-------|------|-----------------|
| **A** | 10.0.0.0 - 10.255.255.255 | /8 | 16,777,216 |
| **B** | 172.16.0.0 - 172.31.255.255 | /12 | 1,048,576 |
| **C** | 192.168.0.0 - 192.168.255.255 | /16 | 65,536 |

### Table 3: Special Addresses

| Address | Purpose |
|---------|---------|
| **127.0.0.1** | Loopback/localhost |
| **0.0.0.0** | Default/unspecified |
| **255.255.255.255** | Limited broadcast |
| **169.254.x.x** | APIPA (DHCP failure) |
| **x.x.x.0** | Network address |
| **x.x.x.255** | Broadcast address |

---

## Quick Reference Summary

```
┌──────────────────────────────────────────┐
│        IP ADDRESSING CHEATSHEET          │
├──────────────────────────────────────────┤
│ IPv4: 32-bit, dotted decimal            │
│ IPv6: 128-bit, hexadecimal              │
│                                          │
│ Classes: A(1-126), B(128-191), C(192-223)│
│ Private: 10.x, 172.16-31.x, 192.168.x   │
│ Special: 127.0.0.1 (loopback)           │
│          169.254.x.x (APIPA)            │
│                                          │
│ Subnet Mask: Defines network vs host     │
│ Network: Host bits = 0                   │
│ Broadcast: Host bits = 1                 │
└──────────────────────────────────────────┘
```
