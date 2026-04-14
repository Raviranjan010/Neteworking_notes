# Subnetting - Diagrams & Visual Guides

## 1. Subnetting Process Flowchart

```
START: Given Network (e.g., 192.168.1.0/24)
         │
         ▼
┌─────────────────────────────────┐
│ Step 1: Identify Requirements   │
│ - How many subnets needed?      │
│ - How many hosts per subnet?    │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ Step 2: Calculate Bits to Borrow│
│ For subnets: 2^n ≥ required     │
│ For hosts: 2^h - 2 ≥ required   │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ Step 3: Determine New CIDR      │
│ New CIDR = Old CIDR + borrowed  │
│ Example: /24 + 2 = /26          │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ Step 4: Calculate Subnet Mask   │
│ Convert CIDR to decimal         │
│ /26 = 255.255.255.192           │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ Step 5: Find Increment          │
│ Increment = 256 - interesting   │
│ 256 - 192 = 64                  │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ Step 6: List All Subnets        │
│ Start at 0, add increment       │
│ .0, .64, .128, .192             │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│ Step 7: Identify Ranges         │
│ Network, Usable, Broadcast      │
└─────────────────────────────────┘
```

---

## 2. Bit Borrowing Visualization

```
ORIGINAL NETWORK: 192.168.1.0/24

Last Octet Binary:
NNNNNNNN HHHHHHHH  (N=Network, H=Host)
00000000 00000000  (0 = Network address)

Total: 8 host bits → 2^8 - 2 = 254 hosts


BORROW 2 BITS FOR SUBNETTING:

NNNNNNNN NNHHHHHH  (Borrowed 2 bits)
11000000 = 192     (New subnet mask last octet)

Network bits: 24 + 2 = 26 (/26)
Host bits: 6
Subnets: 2^2 = 4
Hosts per subnet: 2^6 - 2 = 62


BORROW 3 BITS:

NNNNNNNN NNNHHHHH
11100000 = 224

Network bits: 24 + 3 = 27 (/27)
Host bits: 5
Subnets: 2^3 = 8
Hosts per subnet: 2^5 - 2 = 30


BORROW 4 BITS:

NNNNNNNN NNNNHHHH
11110000 = 240

Network bits: 24 + 4 = 28 (/28)
Host bits: 4
Subnets: 2^4 = 16
Hosts per subnet: 2^4 - 2 = 14
```

---

## 3. Subnet Breakdown Visual Example

```
NETWORK: 192.168.1.0/24 → Divide into 4 subnets (/26)

Entire /24 Network (256 addresses):
┌──────────────────────────────────────────────────┐
│ 192.168.1.0                                .255  │
│ └──────────────────────────────────────────────┘ │
│ 254 usable hosts                                 │
└──────────────────────────────────────────────────┘


After Subnetting (/26):

Subnet 1:
┌─────────────────────┐
│ .0    │       │ .63 │
│ Net   │ 62    │ Bcast│
│       │ Hosts │      │
└─────────────────────┘
Usable: .1 - .62

Subnet 2:
┌─────────────────────┐
│ .64   │       │ .127│
│ Net   │ 62    │ Bcast│
│       │ Hosts │      │
└─────────────────────┘
Usable: .65 - .126

Subnet 3:
┌─────────────────────┐
│ .128  │       │ .191│
│ Net   │ 62    │ Bcast│
│       │ Hosts │      │
└─────────────────────┘
Usable: .129 - .190

Subnet 4:
┌─────────────────────┐
│ .192  │       │ .255│
│ Net   │ 62    │ Bcast│
│       │ Hosts │      │
└─────────────────────┘
Usable: .193 - .254

Increment: 64 (distance between subnets)
```

---

## 4. VLSM Allocation Example

```
BASE NETWORK: 192.168.10.0/24 (254 hosts available)

REQUIREMENTS:
- Sales: 100 hosts
- IT: 50 hosts
- HR: 25 hosts
- WAN Links: 2 hosts each (×3)


VLSM ALLOCATION (Largest to Smallest):

1. SALES (100 hosts) → Need /25 (126 hosts)
┌──────────────────────────────────────────┐
│ 192.168.10.0/25                          │
│ Range: .1 - .126                         │
│ [████████████████░░░░░░░░░░░░░░░░░░░░░░] │
│ Used: 126/254                            │
└──────────────────────────────────────────┘

2. IT (50 hosts) → Need /26 (62 hosts)
┌──────────────────────────────────────────┐
│ 192.168.10.128/26                        │
│ Range: .129 - .190                       │
│ [░░░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░] │
│ Used: 62/254                             │
└──────────────────────────────────────────┘

3. HR (25 hosts) → Need /27 (30 hosts)
┌──────────────────────────────────────────┐
│ 192.168.10.192/27                        │
│ Range: .193 - .222                       │
│ [░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░] │
│ Used: 30/254                             │
└──────────────────────────────────────────┘

4. WAN Link 1 (2 hosts) → /30
┌──────────────────────────────────────────┐
│ 192.168.10.224/30                        │
│ Range: .225 - .226                       │
│ [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░] │
└──────────────────────────────────────────┘

5. WAN Link 2 (2 hosts) → /30
┌──────────────────────────────────────────┐
│ 192.168.10.228/30                        │
│ Range: .229 - .230                       │
│ [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░] │
└──────────────────────────────────────────┘

6. WAN Link 3 (2 hosts) → /30
┌──────────────────────────────────────────┐
│ 192.168.10.232/30                        │
│ Range: .233 - .234                       │
│ [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░] │
└──────────────────────────────────────────┘

REMAINING: 192.168.10.236 - 192.168.10.255 (20 addresses for future)

EFFICIENCY: Used 222 out of 254 addresses = 87% utilization
```

---

## 5. CIDR Quick Reference Chart

```
┌─────────────────────────────────────────────────────────┐
│              CIDR TO HOSTS REFERENCE                    │
├──────┬──────────────┬───────┬──────────┬────────────────┤
│ CIDR │ Subnet Mask  │ Hosts │ Subnets  │ Common Use     │
│      │              │       │ from /24 │                │
├──────┼──────────────┼───────┼──────────┼────────────────┤
│ /24  │ 255.255.255.0│  254  │    1     │ Small office   │
│ /25  │ 255.255.255.128│ 126 │    2     │ Department     │
│ /26  │ 255.255.255.192│  62  │    4     │ Team           │
│ /27  │ 255.255.255.224│  30  │    8     │ Small team     │
│ /28  │ 255.255.255.240│  14  │   16     │ Point-to-point │
│ /29  │ 255.255.255.248│   6  │   32     │ WAN link       │
│ /30  │ 255.255.255.252│   2  │   64     │ Router link    │
│ /31  │ 255.255.255.254│   2* │  128     │ Special P2P    │
│ /32  │ 255.255.255.255│   1  │  256     │ Single host    │
└──────┴──────────────┴───────┴──────────┴────────────────┘

* /31 traditionally 0 hosts, modern use 2 hosts (RFC 3021)

PATTERN: Each step down halves the hosts!
254 → 126 → 62 → 30 → 14 → 6 → 2
```

---

## 6. Subnet Calculation Visual Method

```
PROBLEM: 172.16.0.0/20 - Find subnet details

Step 1: Identify interesting octet
/20 = 255.255.240.0
            ↑
      Interesting octet (not 255 or 0)

Step 2: Calculate increment
256 - 240 = 16

Step 3: List subnets (in 3rd octet)
┌──────────────────────────────────────┐
│ 172.16.0.0/20    (0-15 in 3rd oct)  │
│ 172.16.16.0/20   (16-31)            │
│ 172.16.32.0/20   (32-47)            │
│ 172.16.48.0/20   (48-63)            │
│ ...continues by 16s...               │
│ 172.16.240.0/20  (240-255)          │
└──────────────────────────────────────┘

Step 4: Example subnet breakdown
172.16.32.0/20:
  Network:   172.16.32.0
  First:     172.16.32.1
  Last:      172.16.47.254
  Broadcast: 172.16.47.255
  Hosts:     2^12 - 2 = 4094
```

---

## 7. Binary to Decimal Shortcut Visual

```
LAST OCTET SUBNET MASK VALUES:

Binary      Decimal  CIDR   Increment  Hosts
────────────────────────────────────────────
00000000    0        /24    256        254
10000000    128      /25    128        126
11000000    192      /26    64         62
11100000    224      /27    32         30
11110000    240      /28    16         14
11111000    248      /29    8          6
11111100    252      /30    4          2
11111110    254      /31    2          2
11111111    255      /32    1          1

MEMORY PATTERN:
Each additional 1 bit:
- Doubles the subnets
- Halves the hosts
- Halves the increment
```

---

## 8. Real-World Office Subnet Design

```
COMPANY NETWORK DESIGN:
Base: 10.0.0.0/16 (65,534 hosts available)

Building Layout:
┌─────────────────────────────────────────────┐
│                 ROUTER                      │
│              (10.0.0.1)                     │
│                 │                           │
│        ┌────────┼────────┐                 │
│        │        │        │                 │
│     Floor 1  Floor 2  Floor 3              │
│     Switch   Switch   Switch               │
└─────────────────────────────────────────────┘

SUBNET ALLOCATION:

Floor 1 - Sales (200 hosts):
┌────────────────────────────────────┐
│ 10.0.1.0/24                        │
│ 254 hosts available                │
│ Range: 10.0.1.1 - 10.0.1.254      │
│ Gateway: 10.0.1.1                  │
└────────────────────────────────────┘

Floor 2 - IT & Engineering (100 hosts):
┌────────────────────────────────────┐
│ 10.0.2.0/25                        │
│ 126 hosts available                │
│ Range: 10.0.2.1 - 10.0.2.126      │
│ Gateway: 10.0.2.1                  │
└────────────────────────────────────┘

Floor 3 - Management (50 hosts):
┌────────────────────────────────────┐
│ 10.0.2.128/26                      │
│ 62 hosts available                 │
│ Range: 10.0.2.129 - 10.0.2.190    │
│ Gateway: 10.0.2.129                │
└────────────────────────────────────┘

Server Room (30 hosts):
┌────────────────────────────────────┐
│ 10.0.3.0/27                        │
│ 30 hosts available                 │
│ Range: 10.0.3.1 - 10.0.3.30       │
│ Gateway: 10.0.3.1                  │
└────────────────────────────────────┘

Total Used: ~380 hosts from 65,534 available
Efficiency: Can expand as needed!
```

---

## 9. Troubleshooting Subnet Issues Flowchart

```
PROBLEM: Device can't reach another device
         │
         ▼
┌─────────────────────────────┐
│ Check IP addresses          │
│ Check subnet masks          │
└──────────┬──────────────────┘
           │
           ▼
    Are they in same subnet?
         │
    ┌────┴────┐
   YES       NO
    │         │
    ▼         ▼
┌───────┐  ┌──────────────────┐
│Check  │  │Need router!      │
│switch/│  │- Is router       │
│cables │  │  configured?     │
└───┬───┘  │- Is gateway      │
    │      │  correct?        │
    │      └──────────────────┘
    │
    ▼
Same VLAN?
    │
┌───┴───┐
YES    NO
│       │
▼       ▼
Check  Configure
ARP    VLAN routing
table
```

---

## 10. Comparison Tables

### Table 1: FLSM vs VLSM

```
┌─────────────────────┬──────────────────────┬──────────────────────┐
│ Feature             │ FLSM                 │ VLSM                 │
├─────────────────────┼──────────────────────┼──────────────────────┤
│ Subnet Sizes        │ All same size        │ Different sizes      │
│ IP Efficiency       │ Wasteful             │ Optimal              │
│ Complexity          │ Simple               │ More complex         │
│ Use Case            │ Equal departments    │ Varied needs         │
│ Example             │ All /26              │ /26, /27, /28, /30  │
│ IP Waste            │ High                 │ Minimal              │
└─────────────────────┴──────────────────────┴──────────────────────┘
```

### Table 2: Common Subnetting Scenarios

```
┌──────────────────────┬─────────┬──────────┬──────────────┐
│ Scenario             │ CIDR    │ Hosts    │ Use Case     │
├──────────────────────┼─────────┼──────────┼──────────────┤
│ Home Network         │ /24     │ 254      │ Typical home │
│ Small Office         │ /25     │ 126      │ Small business│
│ Department           │ /26     │ 62       │ Team/Dept    │
│ Workgroup            │ /27     │ 30       │ Small team   │
│ Server Room          │ /28     │ 14       │ Few servers  │
│ Point-to-Point       │ /30     │ 2        │ WAN link     │
│ Single Host          │ /32     │ 1        │ Loopback     │
└──────────────────────┴─────────┴──────────┴──────────────┘
```

---

## Quick Reference Summary

```
┌──────────────────────────────────────────────────┐
│          SUBNETTING QUICK GUIDE                  │
├──────────────────────────────────────────────────┤
│ Steps: Requirements → Borrow bits → New CIDR    │
│        → Mask → Increment → List subnets         │
│                                                  │
│ Formula: Hosts = 2^h - 2                         │
│          Subnets = 2^n                           │
│          Increment = 256 - interesting octet     │
│                                                  │
│ Common: /24=254, /26=62, /28=14, /30=2          │
│                                                  │
│ VLSM Rule: Allocate largest subnets first!       │
│                                                  │
│ Trick: Gateway must be in same subnet as device  │
└──────────────────────────────────────────────────┘
```
