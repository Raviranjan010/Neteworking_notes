# Network Devices - Complete Practical Guide with Enterprise Focus

## 1. Introduction

### 1.1 Why Do We Need Network Devices?

Network devices are the physical hardware that makes network communication possible. They connect devices, direct traffic, and enable communication across local and wide area networks.

**Real-World Analogy:** Network devices = Postal system infrastructure
- **Hub** = Town square announcement (everyone hears)
- **Switch** = Smart mail sorter (delivers to exact address)
- **Router** = Post office (sends mail to different cities)
- **Firewall** = Security checkpoint (inspects mail)

---

## 2. Core Network Devices - Deep Dive

### 2.1 Hub (Layer 1 - Physical Layer)

**What is a Hub?**
A hub is a basic networking device that connects multiple Ethernet devices, making them act as a single network segment.

**How It Works:**
```
Port 1 receives data → Hub copies to ALL other ports
No intelligence, just signal repetition
```

**Characteristics:**
```
Layer: Physical (Layer 1)
Intelligence: None (dumb device)
Forwarding: Broadcasts to all ports
Collision Domain: Single (all devices share)
Broadcast Domain: Single
Speed: Half-duplex
Use Today: Obsolete (replaced by switches)
```

**Example:**
```
Hub with 4 PCs:

PC-A sends to PC-B:
[PC-A] ──▶ [HUB] ──▶ [PC-B] ✓ (receives)
              │
              ├──▶ [PC-C] ✗ (unnecessary)
              │
              └──▶ [PC-D] ✗ (unnecessary)

ALL devices receive the data, even if not intended for them!
Creates security and performance issues.
```

**Problems with Hubs:**
- Security risk (everyone sees all traffic)
- Collisions (multiple devices transmitting)
- Wasted bandwidth
- No intelligence

---

### 2.2 Switch (Layer 2 - Data Link Layer)

**What is a Switch?**
A switch is an intelligent device that forwards frames based on MAC addresses, creating separate collision domains for each port.

**How It Works - MAC Address Learning:**

```
STEP 1: Switch starts with empty MAC table
┌─────────────────────────────────┐
│ MAC Address Table               │
│ (Empty initially)               │
│                                 │
│ MAC Address    │ Port           │
│ ───────────────┼──────          │
│                │                │
└─────────────────────────────────┘

STEP 2: PC-A (MAC: AA:AA) sends frame to PC-B (MAC: BB:BB)
Frame arrives on Port 1

Switch learns:
┌─────────────────────────────────┐
│ MAC Address Table               │
│                                 │
│ MAC Address    │ Port           │
│ ───────────────┼──────          │
│ AA:AA:AA:AA    │ Port 1         │ ← Learned!
│                │                │
└─────────────────────────────────┘

Destination BB:BB not in table → Flood to all ports except Port 1

STEP 3: PC-B responds, frame arrives on Port 2
Switch learns:
┌─────────────────────────────────┐
│ MAC Address Table               │
│                                 │
│ MAC Address    │ Port           │
│ ───────────────┼──────          │
│ AA:AA:AA:AA    │ Port 1         │
│ BB:BB:BB:BB    │ Port 2         │ ← Learned!
└─────────────────────────────────┘

STEP 4: Future communication
PC-A → PC-B: Switch knows BB:BB is on Port 2
Forwards ONLY to Port 2 (no flooding!)

Efficient, secure, intelligent!
```

**Characteristics:**
```
Layer: Data Link (Layer 2)
Intelligence: High (MAC address table)
Forwarding: Based on MAC addresses
Collision Domain: Per port (isolated)
Broadcast Domain: Single (unless VLANs)
Speed: Full-duplex
Use Today: Standard in all networks
```

**Switch Types:**
```
Unmanaged Switch:
- Plug and play
- No configuration
- Home/small office
- Example: 8-port desktop switch

Managed Switch:
- Configurable (VLANs, QoS, security)
- Enterprise use
- SNMP monitoring
- Example: Cisco Catalyst series

PoE Switch (Power over Ethernet):
- Provides power + data
- IP cameras, phones, APs
- No separate power needed
```

---

### 2.3 Router (Layer 3 - Network Layer)

**What is a Router?**
A router connects different networks together and forwards packets based on IP addresses using routing tables.

**How It Works:**
```
Router has multiple interfaces, each in different network:

Interface 1: 192.168.1.1/24 (Network A)
Interface 2: 10.0.0.1/24 (Network B)
Interface 3: 203.0.113.1/30 (Internet)

Routing Table:
┌────────────────┬──────────────┬──────────────┐
│ Destination    │ Next Hop     │ Interface    │
├────────────────┼──────────────┼──────────────┤
│ 192.168.1.0/24 │ Direct       │ eth0         │
│ 10.0.0.0/24    │ Direct       │ eth1         │
│ 0.0.0.0/0      │ 203.0.113.2  │ eth2         │
└────────────────┴──────────────┴──────────────┘

Packet from 192.168.1.10 → 8.8.8.8:
1. Arrives on eth0
2. Check routing table
3. Match: 0.0.0.0/0 (default route)
4. Forward to 203.0.113.2 via eth2
5. NAT translation (private → public IP)
```

**Characteristics:**
```
Layer: Network (Layer 3)
Intelligence: Very High (routing protocols)
Forwarding: Based on IP addresses
Collision Domain: Per interface
Broadcast Domain: Per interface (isolates broadcasts)
Functions: Routing, NAT, firewall, QoS
Use Today: Essential for all networks
```

---

### 2.4 Hub vs Switch vs Router - Deep Comparison

```
┌────────────────────┬──────────────┬──────────────┬──────────────┐
│ Feature            │ Hub          │ Switch       │ Router       │
├────────────────────┼──────────────┼──────────────┼──────────────┤
│ OSI Layer          │ Layer 1      │ Layer 2      │ Layer 3      │
│                    │ (Physical)   │ (Data Link)  │ (Network)    │
├────────────────────┼──────────────┼──────────────┼──────────────┤
│ Addressing         │ None         │ MAC Address  │ IP Address   │
├────────────────────┼──────────────┼──────────────┼──────────────┤
│ Intelligence       │ None (dumb)  │ High         │ Very High    │
├────────────────────┼──────────────┼──────────────┼──────────────┤
│ Forwarding Method  │ All ports    │ MAC table    │ Routing table│
├────────────────────┼──────────────┼──────────────┼──────────────┤
│ Collision Domain   │ 1 (shared)   │ Per port     │ Per interface│
├────────────────────┼──────────────┼──────────────┼──────────────┤
│ Broadcast Domain   │ 1            │ 1 (unless    │ Per interface│
│                    │              │ VLANs)       │              │
├────────────────────┼──────────────┼──────────────┼──────────────┤
│ Duplex             │ Half-duplex  │ Full-duplex  │ Full-duplex  │
├────────────────────┼──────────────┼──────────────┼──────────────┤
│ Speed              │ 10/100 Mbps  │ 100M/1G/10G  │ 1G/10G/40G+  │
├────────────────────┼──────────────┼──────────────┼──────────────┤
│ Security           │ Very Low     │ Medium       │ High         │
│                    │ (sees all)   │ (MAC filter) │ (ACLs, FW)   │
├────────────────────┼──────────────┼──────────────┼──────────────┤
│ Cost               │ Cheap        │ Moderate     │ Expensive    │
├────────────────────┼──────────────┼──────────────┼──────────────┤
│ Use Case           │ Obsolete     │ LAN internal │ Between      │
│                    │              │              │ networks     │
├────────────────────┼──────────────┼──────────────┼──────────────┤
│ Broadcast Handling │ Forwards all │ Forwards all │ Stops (unless│
│                    │              │              │ configured)  │
└────────────────────┴──────────────┴──────────────┴──────────────┘

ANALOGY:
Hub    = Town crier (everyone hears everything)
Switch = Smart mailroom (delivers to exact room)
Router = Post office (sends to different cities)
```

---

## 3. VLAN (Virtual Local Area Network)

### 3.1 What is VLAN?

A VLAN is a logical segmentation of a physical switch into multiple broadcast domains. It allows you to create separate networks on the same physical hardware.

**Why VLANs Exist:**

**Without VLANs:**
```
Single flat network:
- All devices in same broadcast domain
- Broadcast storms affect everyone
- No security between departments
- Difficult to manage
```

**With VLANs:**
```
Logical segmentation:
- VLAN 10: Sales Department
- VLAN 20: IT Department
- VLAN 30: HR Department
- Each VLAN = separate broadcast domain
- Security isolation
- Easy to manage
```

### 3.2 How VLANs Work

```
PHYSICAL SWITCH with 3 VLANs:

Ports 1-8:   VLAN 10 (Sales) - 192.168.10.0/24
Ports 9-16:  VLAN 20 (IT)     - 192.168.20.0/24
Ports 17-24: VLAN 30 (HR)     - 192.168.30.0/24

┌──────────────────────────────────────────┐
│          MANAGED SWITCH                  │
│                                          │
│  [P1][P2][P3]...[P9][P10]...[P17][P18]  │
│   │   │   │      │   │       │   │       │
│  Sales   Sales     IT  IT      HR  HR    │
│                                          │
│  VLAN 10      │    VLAN 20   │ VLAN 30   │
│  (Blue)       │    (Green)   │ (Red)     │
│                                          │
│ Broadcast domains isolated!              │
│ Sales broadcast ≠ IT broadcast           │
└──────────────────────────────────────────┘

VLAN TAGGING (802.1Q):
When frame travels between switches (trunk port):

Normal Frame:
┌─────────────────────────────┐
│ Dest MAC │ Src MAC │ Data   │
└─────────────────────────────┘

802.1Q Tagged Frame:
┌──────────────────────────────────────┐
│ Dest MAC │ Src MAC │ VLAN TAG│ Data │
│                   │ (12-bit)│       │
│                   │ VLAN ID │       │
│                   │ 1-4094  │       │
└──────────────────────────────────────┘

Tag tells receiving switch which VLAN frame belongs to
```

### 3.3 Inter-VLAN Routing

**Problem:** Devices in different VLANs can't communicate (separate broadcast domains)

**Solution:** Router or Layer 3 Switch

```
VLAN 10 (Sales) → Need to reach → VLAN 20 (IT)

┌─────────────────────────────────────────┐
│ Layer 3 Switch or Router                │
│                                         │
│ Interface VLAN 10: 192.168.10.1/24     │
│ Interface VLAN 20: 192.168.20.1/24     │
│                                         │
│ Routing table:                          │
│ 192.168.10.0/24 → Direct (VLAN 10)     │
│ 192.168.20.0/24 → Direct (VLAN 20)     │
└─────────────────────────────────────────┘

Sales PC (192.168.10.10) → IT Server (192.168.20.50):
1. PC checks: Different subnet!
2. Send to default gateway (192.168.10.1)
3. Router receives on VLAN 10 interface
4. Routes to VLAN 20 interface
5. Delivers to IT Server

This is called "Router on a Stick" or Layer 3 switching
```

---

## 4. 🚀 Real Network Architecture

### Enterprise Network Design

```
                    [INTERNET]
                        │
                        │ ISP Connection
                        │
                  ┌─────────────┐
                  │ Edge Router │ 192.168.1.1
                  │ (NAT, FW)   │ 203.0.113.5 (Public)
                  └──────┬──────┘
                         │
                         │ DMZ (Demilitarized Zone)
                         │
                  ┌─────────────┐
                  │  Firewall   │ Stateful inspection
                  │             │ ACLs, NAT, VPN
                  └──────┬──────┘
                         │
                         │ Core Network
                         │
              ┌──────────┴──────────┐
              │                     │
        ┌──────────┐         ┌──────────┐
        │ Core     │         │ Core     │
        │ Switch 1 │─────────│ Switch 2 │ (Redundancy)
        │ (L3)     │         │ (L3)     │
        └────┬─────┘         └────┬─────┘
             │                     │
      ┌──────┼──────┐       ┌──────┼──────┐
      │      │      │       │      │      │
   ┌────┐┌────┐┌────┐  ┌────┐┌────┐┌────┐
   │Dist││Dist││Dist│  │Dist││Dist││Dist│
   │ Sw ││ Sw ││ Sw │  │ Sw ││ Sw ││ Sw │
   │ 1  ││ 2  ││ 3  │  │ 4  ││ 5  ││ 6  │
   └─┬──┘└─┬──┘└─┬──┘  └─┬──┘└─┬──┘└─┬──┘
     │     │     │       │     │     │
   Access  Access Access Access Access Access
   Switches (Multiple per floor/building)
     │       │      │       │      │      │
   [PCs]   [PCs]  [PCs]   [PCs]  [PCs]  [PCs]
   
VLAN DESIGN:
- VLAN 10: Sales (192.168.10.0/24)
- VLAN 20: IT (192.168.20.0/24)
- VLAN 30: HR (192.168.30.0/24)
- VLAN 40: Management (192.168.40.0/24)
- VLAN 50: Servers (192.168.50.0/24)
- VLAN 100: Voice/VoIP (192.168.100.0/24)
- VLAN 999: Native/Default

TRAFFIC FLOW:
PC in VLAN 10 → Internet:
Access Switch → Dist Switch → Core Switch → Firewall → Router → Internet

PC in VLAN 10 → Server in VLAN 50:
Access Switch → Dist Switch → Core Switch (L3 routing) → Server

KEY FEATURES:
- Redundancy (dual core switches)
- VLAN segmentation (security)
- Inter-VLAN routing (Layer 3)
- Firewall (security policies)
- NAT (private to public IP)
- QoS (voice priority)
- Monitoring (SNMP, NetFlow)
```

---

## 5. Other Network Devices

### 5.1 Bridge (Layer 2)

```
Purpose: Connect two network segments
Function: Filter traffic based on MAC addresses
Modern Use: Integrated into switches
Historical: Used before switches became cheap

Example:
Segment A ──[BRIDGE]── Segment B
Bridge learns MACs on both sides
Forwards only necessary traffic
```

### 5.2 Wireless Access Point (WAP)

```
Purpose: Connect wireless devices to wired network
Layer: Layer 2 (acts like switch for WiFi)
Standards: 802.11a/b/g/n/ac/ax (WiFi 6)
Functions:
- Convert radio signals to Ethernet
- SSID broadcasting
- Security (WPA2/WPA3)
- Client association

Example:
[Wireless Devices] ←→ [WAP] ←→ [Switch] ←→ [Network]
```

### 5.3 Firewall (Layer 3-7)

```
Purpose: Security device that filters traffic
Types:
- Packet filtering (Layer 3-4)
- Stateful inspection (Layer 4)
- Application firewall (Layer 7)
- Next-gen firewall (NGFW)

Functions:
- Allow/deny based on rules
- NAT
- VPN termination
- Intrusion prevention (IPS)
- Deep packet inspection

Placed at: Network perimeter, between zones
```

### 5.4 Load Balancer (Layer 4-7)

```
Purpose: Distribute traffic across multiple servers
Why: High availability, scalability, performance

Example:
            ┌─[Server 1]
[Users] ──▶│──[Server 2]
            └─[Server 3]

Load balancer distributes requests
If Server 2 fails, traffic goes to 1 & 3
Users never see downtime
```

---

## 6. Complete Packet Flow Through Devices

```
SCENARIO: PC in Sales (VLAN 10) accesses web server

PC (192.168.10.10) → www.example.com (93.184.216.34)

Step 1: PC creates packet
- Source IP: 192.168.10.10
- Dest IP: 93.184.216.34
- Source MAC: PC's MAC
- Dest MAC: Default gateway (switch VLAN 10 interface)

Step 2: Access Switch (Layer 2)
- Receives frame on port
- Checks MAC address table
- Forwards to distribution switch (trunk port with VLAN 10 tag)

Step 3: Distribution Switch (Layer 2/3)
- Receives tagged frame
- Forwards to core switch via trunk

Step 4: Core Switch (Layer 3)
- Receives frame, sees destination is external
- Routes to firewall (default route)
- Changes source MAC to its MAC, dest MAC to firewall

Step 5: Firewall (Layer 3-7)
- Checks security policies
- Is this traffic allowed? (Yes, outbound HTTP)
- Performs NAT: 192.168.10.10 → 203.0.113.5
- Forwards to edge router

Step 6: Edge Router (Layer 3)
- Checks routing table
- Default route points to ISP
- Forwards to ISP gateway

Step 7: Internet
- Packets traverse multiple routers
- Reach web server at 93.184.216.34

Return path (reverse):
Web server → ISP → Router → Firewall (reverse NAT) → Core → Dist → Access → PC
```

---

## 7. Key Terms Explained

| Term | Definition | Example |
|------|-----------|---------|
| **MAC Table** | Switch database of MAC addresses and ports | AA:BB:CC → Port 1 |
| **Routing Table** | Router database of networks and next hops | 10.0.0.0/8 → 192.168.1.1 |
| **VLAN** | Virtual LAN (logical segmentation) | VLAN 10 = Sales |
| **Trunk Port** | Carries multiple VLANs (tagged) | Switch-to-switch link |
| **Access Port** | Single VLAN (untagged) | PC connection |
| **Collision Domain** | Area where collisions can occur | Hub = 1, Switch = per port |
| **Broadcast Domain** | Area where broadcasts reach | Router stops broadcasts |
| **NAT** | Network Address Translation | Private → Public IP |
| **DMZ** | Demilitarized Zone (semi-trusted) | Public servers |

---

## 8. Advantages of Modern Network Design

1. **Hierarchical Structure** - Access → Distribution → Core
2. **Redundancy** - No single point of failure
3. **VLAN Segmentation** - Security and performance
4. **Scalability** - Easy to add users/devices
5. **Manageability** - Organized, documented
6. **Security** - Firewalls, ACLs, isolation
7. **Performance** - Full-duplex, high bandwidth

---

## 9. Summary

- Hub: Layer 1, broadcasts to all, obsolete
- Switch: Layer 2, forwards based on MAC, standard
- Router: Layer 3, forwards based on IP, connects networks
- VLANs: Logical segmentation for security and performance
- Enterprise networks use hierarchical design (Access-Dist-Core)
- Firewalls provide security at network perimeter
- Modern networks use switches and routers, not hubs
- Understanding device functions is crucial for network design
- Packet flow changes MAC addresses at each hop, IP addresses stay same

**Next Step:** Learn Network Security (Topic 10) to understand how to protect these networks.

---

## Quick Revision Checklist

- [ ] Can explain hub vs switch vs router differences
- [ ] Understand MAC address table learning process
- [ ] Know what VLANs are and why they're used
- [ ] Can describe enterprise network architecture
- [ ] Understand packet flow through multiple devices
- [ ] Know collision vs broadcast domains
- [ ] Can explain trunk vs access ports
- [ ] Understand role of each device in real network

**Mastery Check:** Can you trace a packet from a PC through access switch, distribution switch, core switch, firewall, router, to the internet, explaining what each device does? If yes, you've mastered network devices!
