# Routing - Diagrams & Visual Guides

## 1. Complete Packet Flow Diagram

```
SCENARIO: PC-A (192.168.1.10/24) → PC-B (10.0.1.50/24)

PC-A                     Router-A                  Router-B                  PC-B
192.168.1.10          192.168.1.1/172.16.0.1    172.16.0.2/10.0.1.1      10.0.1.50
MAC:AA:AA             MAC:BB:BB / CC:CC         MAC:DD:DD / EE:EE         MAC:FF:FF
   │                      │                         │                        │
   │  STEP 1: PC-A checks │                         │                        │
   │  Destination subnet  │                         │                        │
   │  10.0.1.50 ≠ 192.168.1.x                     │                        │
   │  → Send to gateway!  │                         │                        │
   │                      │                         │                        │
   │  STEP 2: ARP for gateway MAC                   │                        │
   │  "Who has 192.168.1.1?"                       │                        │
   │  ─────────────────────▶                        │                        │
   │  "I'm 192.168.1.1, MAC:BB:BB"                 │                        │
   │  ◀─────────────────────                        │                        │
   │                      │                         │                        │
   │  STEP 3: Send Packet │                         │                        │
   │  ═══════════════════▶│                         │                        │
   │  IP: 192.168.1.10 → 10.0.1.50 (STAYS SAME!)   │                        │
   │  MAC: AA:AA → BB:BB  │                         │                        │
   │                      │                         │                        │
   │                      │  STEP 4: Router-A checks │                        │
   │                      │  routing table           │                        │
   │                      │  Dest: 10.0.1.50         │                        │
   │                      │  Next: 172.16.0.2        │                        │
   │                      │  ARP for Router-B MAC    │                        │
   │                      │                         │                        │
   │                      │  STEP 5: Forward Packet  │                        │
   │                      │  ═══════════════════════▶│                        │
   │                      │  IP: 192.168.1.10 → 10.0.1.50 (STILL SAME!)      │
   │                      │  MAC: CC:CC → DD:DD      │                        │
   │                      │  (Changed!)              │                        │
   │                      │                         │                        │
   │                      │                         │  STEP 6: Router-B checks│
   │                      │                         │  10.0.1.0/24 directly  │
   │                      │                         │  connected on eth2      │
   │                      │                         │  ARP for PC-B MAC       │
   │                      │                         │                         │
   │                      │                         │  STEP 7: Deliver to PC-B│
   │                      │                         │  ══════════════════════▶│
   │                      │                         │  IP: 192.168.1.10 → 10.0.1.50
   │                      │                         │  MAC: EE:EE → FF:FF     │
   │                      │                         │                         │
   │                      │                         │                    PC-B receives!
   │                      │                         │                    "This is for me!"

KEY INSIGHT:
IP addresses: 192.168.1.10 → 10.0.1.50 (CONSTANT throughout journey)
MAC addresses: Change at EVERY hop (local delivery only)
```

---

## 2. Routing Table Visualization

```
ROUTER-A ROUTING TABLE:

┌────────────────┬──────────────┬──────────────┬───────────┬────────┐
│ Dest Network   │ Subnet Mask  │ Next Hop     │ Interface │ Metric │
├────────────────┼──────────────┼──────────────┼───────────┼────────┤
│ 192.168.1.0    │ 255.255.255.0│ Direct       │ eth0      │ 0      │
│ 172.16.0.0     │ 255.255.0.0  │ Direct       │ eth1      │ 0      │
│ 10.0.0.0       │ 255.0.0.0    │ 172.16.0.2   │ eth1      │ 10     │
│ 10.0.1.0       │ 255.255.255.0│ 172.16.0.2   │ eth1      │ 10     │
│ 0.0.0.0        │ 0.0.0.0      │ 172.16.0.254 │ eth1      │ 1      │
└────────────────┴──────────────┴──────────────┴───────────┴────────┘

LEGEND:
Direct = Directly connected network
Next Hop = Router to forward packet to
Interface = Which port to use
Metric = Cost (lower = better)
0.0.0.0 = Default route (gateway of last resort)

DECISION PROCESS:
Packet arrives with destination 10.0.1.50
  ↓
Check routing table (longest prefix match):
  - 192.168.1.0? NO
  - 10.0.0.0? YES (matches)
  - 10.0.1.0? YES (more specific match!)
  ↓
Choose most specific match: 10.0.1.0/24
  ↓
Forward to: 172.16.0.2 via eth1
```

---

## 3. Static vs Dynamic Routing Comparison

```
STATIC ROUTING:
┌─────────────────────────────────────────┐
│ Manual Configuration                    │
│                                         │
│ Router(config)#                         │
│ ip route 10.0.1.0 255.255.255.0        │
│          172.16.0.2                     │
│                                         │
│ Pros:                                   │
│ ✓ Simple (small networks)               │
│ ✓ No CPU overhead                       │
│ ✓ Predictable                           │
│ ✓ Secure                                │
│                                         │
│ Cons:                                   │
│ ✗ Doesn't adapt to failures             │
│ ✗ Manual updates needed                 │
│ ✗ Not scalable                          │
│ ✗ No automatic failover                 │
│                                         │
│ Best for: Stub networks, default routes │
└─────────────────────────────────────────┘

DYNAMIC ROUTING:
┌─────────────────────────────────────────┐
│ Automatic Learning (OSPF Example)       │
│                                         │
│ Router(config)#                         │
│ router ospf 1                           │
│ network 10.0.0.0 0.255.255.255 area 0  │
│                                         │
│ Routers exchange information            │
│ automatically!                          │
│                                         │
│ Pros:                                   │
│ ✓ Automatic route learning              │
│ ✓ Adapts to topology changes            │
│ ✓ Scalable                              │
│ ✓ Automatic failover                    │
│ ✓ Load balancing                        │
│                                         │
│ Cons:                                   │
│ ✗ Complex configuration                 │
│ ✗ Uses CPU/memory                       │
│ ✗ Consumes bandwidth                    │
│ ✗ Security concerns                     │
│                                         │
│ Best for: Medium/large networks         │
└─────────────────────────────────────────┘
```

---

## 4. Routing Protocol Comparison Chart

```
┌────────────────────────────────────────────────────────────────────────┐
│                    ROUTING PROTOCOL COMPARISON                         │
├──────────┬──────────┬──────────┬──────────┬──────────┬─────────────────┤
│ Feature  │ RIP      │ OSPF     │ EIGRP    │ BGP      │ Static          │
├──────────┼──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ Type     │ Distance │ Link     │ Advanced │ Path     │ Manual          │
│          │ Vector   │ State    │ Distance │ Vector   │ Configuration   │
│          │          │          │ Vector   │          │                 │
├──────────┼──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ Metric   │ Hop Count│ Cost     │ Composite│ Path     │ N/A             │
│          │          │(Bandwidth)│(BW,Dly, │ Attributes│                │
│          │          │          │ Rel,Load)│          │                 │
├──────────┼──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ Max Hops │ 15       │ Unlimited│ Unlimited│ Unlimited│ N/A             │
├──────────┼──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ Converge │ Slow     │ Fast     │ Fast     │ Variable │ Instant         │
│ Speed    │(minutes) │(seconds) │(seconds) │          │ (but manual)    │
├──────────┼──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ AD       │ 120      │ 110      │ 90       │ 20/200   │ 1               │
├──────────┼──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ Standard │ Open     │ Open     │ Cisco    │ Open     │ N/A             │
│          │          │          │(now part)│          │                 │
├──────────┼──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ Scope    │ Small    │ Large    │ Medium   │ Internet │ Very Small      │
│          │ Networks │ Enterprise│Enterprise│ Scale    │                 │
├──────────┼──────────┼──────────┼──────────┼──────────┼─────────────────┤
│ Use Case │ Legacy   │ Most     │ Cisco    │ Between  │ Stub networks,  │
│          │ Networks │ common   │ shops    │ ISPs     │ default routes  │
└──────────┴──────────┴──────────┴──────────┴──────────┴─────────────────┘
```

---

## 5. OSPF Operation Step-by-Step

```
OSPF NEIGHBOR FORMATION & ROUTE CALCULATION:

STEP 1: DOWN STATE
Router A                    Router B
  │                           │
  │  Just started OSPF        │
  │                           │

STEP 2: INIT STATE (Hello Sent)
  │─── Hello ────────────────▶│
  │  "I'm Router A"           │
  │                           │

STEP 3: TWO-WAY STATE (Bidirectional)
  │◀─── Hello ────────────────│
  │  "I see you, Router A"    │
  │                           │
  │  Neighbors discovered!    │
  │                           │

STEP 4: EXSTART/EXCHANGE (LSA Exchange)
  │─── DBD (Database Desc) ──▶│
  │◀── DBD ───────────────────│
  │  "Here's what I know"     │
  │                           │

STEP 5: LOADING (Request Missing Info)
  │─── LSR (Link State Req) ─▶│
  │◀── LSU (Link State Update)│
  │  "Tell me more about X"   │
  │                           │

STEP 6: FULL STATE (Adjacency Complete)
  │                           │
  │  Full Adjacency!          │
  │  Both have complete LSDB  │
  │                           │

STEP 7: SPF CALCULATION
  │
  ├─ Run Dijkstra's algorithm
  ├─ Calculate shortest paths
  ├─ Build routing table
  └─ Install best routes

STEP 8: MAINTENANCE
  │
  ├─ Periodic Hello packets (every 10s)
  ├─ If Hellos stop → Neighbor down
  └─ Triggered updates on changes
```

---

## 6. Real-World ISP Routing Example

```
HOME USER CONNECTING TO WEBSITE:

[Your PC]          [Home Router]        [ISP]            [Internet]
192.168.1.10    WAN:203.0.113.5      203.0.113.1      93.184.216.34
                LAN:192.168.1.1                       (example.com)
                    │
                    │
PACKET FLOW:

1. PC creates packet:
   Source IP: 192.168.1.10
   Dest IP: 93.184.216.34
   Dest MAC: Home Router's MAC

2. Home Router receives, performs NAT:
   Source IP: 192.168.1.10 → 203.0.113.5 (NAT!)
   Dest IP: 93.184.216.34
   Forwards to ISP

3. ISP Router:
   Has route to 93.184.216.34 via Internet
   Forwards through multiple ISP routers

4. Internet Routers (BGP):
   Each router checks routing table
   Forwards closer to destination
   May traverse 10-20 routers!

5. Web Server receives:
   Source IP: 203.0.113.5 (your public IP)
   Dest IP: 93.184.216.34
   
6. Response (reverse path):
   Web server → ... → ISP → Your Router
   Router NATs back: 203.0.113.5 → 192.168.1.10
   Delivers to your PC

TOTAL JOURNEY: PC → Home Router → ISP → 10-20 Internet Routers → Web Server
```

---

## 7. Routing Decision Flowchart

```
PACKET ARRIVES AT ROUTER
         │
         ▼
┌─────────────────────────┐
│ Read destination IP     │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ Check routing table     │
│ (longest prefix match)  │
└────────┬────────────────┘
         │
         ▼
    Route found?
         │
    ┌────┴────┐
   YES       NO
    │         │
    │         ▼
    │    ┌─────────────────┐
    │    │ Default route?  │
    │    └────┬────────────┘
    │         │
    │    ┌────┴────┐
    │   YES       NO
    │    │         │
    │    │         ▼
    │    │    Drop packet
    │    │    Send ICMP
    │    │    unreachable
    │    │
    ▼    ▼
┌─────────────────────────┐
│ Get next hop & interface│
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ Decrement TTL           │
│ (if 0, drop packet)     │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ ARP for next hop MAC    │
│ (if not in cache)       │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ Update frame:           │
│ - Source MAC = this router
│ - Dest MAC = next hop   │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│ Forward packet out      │
│ appropriate interface   │
└─────────────────────────┘
```

---

## 8. Network Topology with Routing

```
COMPLETE NETWORK EXAMPLE:

                    [Internet Cloud]
                         │
                         │ BGP
                         │
                   [Edge Router]
                  203.0.113.1/30
                         │
                         │ Static default route
                         │
              ┌──────────┴──────────┐
              │                     │
        [Core Router 1]      [Core Router 2]
        10.0.0.1/30          10.0.0.2/30
              │                     │
              │ OSPF Area 0         │ OSPF Area 0
              │                     │
    ┌─────────┼─────────┐   ┌───────┼─────────┐
    │         │         │   │       │         │
[Dist-A]  [Dist-B]  [Dist-C] [Dist-D] [Dist-E] [Dist-F]
  │         │         │       │       │         │
OSPF      OSPF      OSPF     OSPF    OSPF      OSPF
Area 1    Area 1    Area 2   Area 2  Area 3    Area 3
  │         │         │       │       │         │
[Access] [Access] [Access] [Access] [Access] [Access]
  │         │         │       │       │         │
Users    Users    Users   Users   Users    Users

ROUTING DESIGN:
- Edge to ISP: BGP or static
- Core to Edge: Static or OSPF
- Core routers: OSPF Area 0 (backbone)
- Distribution: OSPF areas for segmentation
- Access: Switches (Layer 2, no routing)

BENEFITS:
- Hierarchical design
- Fast convergence
- Scalable
- Easy to troubleshoot
- Fault isolation
```

---

## 9. Troubleshooting Routing Issues

```
TROUBLESHOOTING FLOWCHART:

Problem: Can't reach remote network
         │
         ▼
┌─────────────────────────────┐
│ Step 1: Check local config  │
│ - IP address correct?       │
│ - Subnet mask correct?      │
│ - Default gateway set?      │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│ Step 2: Ping default gateway│
│ Success?                    │
└────────┬────────────────────┘
         │
    ┌────┴────┐
   YES       NO → Fix local connectivity
    │
    ▼
┌─────────────────────────────┐
│ Step 3: traceroute          │
│ Where does it stop?         │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│ Step 4: Check router        │
│ - Routing table correct?    │
│ - Interfaces up?            │
│ - Routing protocol working? │
└────────┬────────────────────┘
         │
    ┌────┴────┐
   Found     Not Found
   Issue     │
    │        ▼
    │   ┌─────────────────────┐
    │   │ Check neighbors     │
    │   │ - OSPF adjacency?   │
    │   │ - Route learned?    │
    │   └─────────────────────┘
    │
    ▼
Fix and test!
```

---

## 10. Quick Reference Tables

### Table 1: Common Administrative Distances

```
┌──────────────────────────────┬────┐
│ Route Source                 │ AD │
├──────────────────────────────┼────┤
│ Connected interface          │ 0  │
│ Static route                 │ 1  │
│ EIGRP summary route          │ 5  │
│ External BGP (eBGP)         │ 20 │
│ Internal EIGRP              │ 90 │
│ OSPF                        │ 110│
│ IS-IS                       │ 115│
│ RIP                         │ 120│
│ External EIGRP              │ 170│
│ Internal BGP (iBGP)         │ 200│
└──────────────────────────────┴────┘
```

### Table 2: When to Use Which Routing

```
┌──────────────────────┬────────────────────────────────────┐
│ Scenario             │ Recommended Solution               │
├──────────────────────┼────────────────────────────────────┤
│ Home network         │ Static default route to ISP        │
│ Small office (1-2 routers)│ Static routing                │
│ Medium company       │ OSPF or EIGRP                      │
│ Large enterprise     │ OSPF with multiple areas           │
│ Multiple sites       │ OSPF, EIGRP, or BGP                │
│ ISP/Internet         │ BGP                                │
│ Stub network         │ Static routing                     │
│ Cisco-only environment│ EIGRP                              │
│ Multi-vendor         │ OSPF (open standard)               │
└──────────────────────┴────────────────────────────────────┘
```

---

## Quick Reference Summary

```
┌──────────────────────────────────────────────────┐
│            ROUTING CHEATSHEET                    │
├──────────────────────────────────────────────────┤
│ Router = Layer 3 device, uses IP addresses      │
│                                                  │
│ Packet Flow:                                     │
│ - IP addresses stay same end-to-end             │
│ - MAC addresses change at each hop              │
│                                                  │
│ Static: Manual, simple, not scalable            │
│ Dynamic: Automatic, adaptive, scalable          │
│                                                  │
│ RIP: Hop count, max 15, slow                    │
│ OSPF: Bandwidth cost, fast, most common         │
│ BGP: Internet routing between ISPs              │
│                                                  │
│ AD: Lower = more trusted                        │
│ Connected(0) < Static(1) < OSPF(110) < RIP(120) │
│                                                  │
│ Troubleshoot: ping → traceroute → check routes  │
└──────────────────────────────────────────────────┘
```
