# Computer Networking Fundamentals - Diagrams

## 1. Network Types by Coverage

```
┌─────────────────────────────────────────────────────────────────┐
│                    NETWORK COVERAGE SCALE                       │
└─────────────────────────────────────────────────────────────────┘

PAN          LAN              MAN                WAN
│            │                │                  │
▼            ▼                ▼                  ▼
┌────┐    ┌────────┐      ┌──────────┐      ┌────────────┐
│10m │    │ 1-2 km │      │ 5-50 km  │      │ Unlimited  │
└────┘    └────────┘      └──────────┘      └────────────┘
  │           │               │                 │
  ▼           ▼               ▼                 ▼
Bluetooth   Home/Office    City-wide         Country/Global
USB         Campus         Cable TV          Internet


EXAMPLES:

PAN:  [Phone]───[Earbuds]
      (You with your devices)

LAN:      [Switch]
          /  |   \
      [PC1][PC2][PC3]
      (Office/Home network)

MAN:    [Building A]═══[Building B]═══[Building C]
        (City-wide network)

WAN:    [New York]══════[London]══════[Tokyo]
        (Global network)
```

---

## 2. Network Topologies

### 2.1 Bus Topology

```
    ┌────────────────────────────────────────────┐
    │          BACKBONE CABLE                    │
    └────────────────────────────────────────────┘
         │        │        │        │
      ┌────┐   ┌────┐   ┌────┐   ┌────┐
      │PC1 │   │PC2 │   │PC3 │   │PC4 │
      └────┘   └────┘   └────┘   └────┘
      
      ═ Terminators at both ends prevent signal reflection

Data Flow: PC1 sends → travels both directions → all PCs receive
```

### 2.2 Star Topology

```
              ┌──────────┐
              │  SWITCH  │
              │  / HUB   │
              └────┬─────┘
                   │
          ┌────────┼────────┐
          │        │        │
       ┌────┐   ┌────┐   ┌────┐
       │PC1 │   │PC2 │   │PC3 │
       └────┘   └────┘   └────┘
       
Central device manages all communication
If PC2 fails → PC1 and PC3 still work
If Switch fails → entire network down
```

### 2.3 Ring Topology

```
        ┌──────┐
        │ PC1  │
        └──┬───┘
           │
        ┌──┴───┐
        │ PC4  │◄──── Data flows in ring
        └──┬───┘
           │
        ┌──┴───┐      ┌──────┐
        │ PC3  │─────▶│ PC2  │
        └──────┘      └──────┘
        
Unidirectional: One direction only
Bidirectional: Both directions (more reliable)
```

### 2.4 Mesh Topology

```
     Full Mesh (4 nodes):
     
     [A]════[B]
      ║ ╲  ╱ ║
      ║  ╲╱  ║
      ║  ╱╲  ║
      ║ ╱  ╲ ║
     [D]════[C]
     
Every node connects to every other node
Connections = n(n-1)/2 = 4(3)/2 = 6

     Partial Mesh:
     
     [A]════[B]
      ║      ║
      ║      ║
     [D]────[C]
     
Some nodes have multiple connections
```

### 2.5 Tree Topology

```
            [Root Switch]
            /           \
      [Switch A]     [Switch B]
      /    |    \     /    |    \
   [PC1][PC2][PC3] [PC4][PC5][PC6]
   
Hierarchical structure
Easy to expand by adding branches
```

### 2.6 Hybrid Topology

```
    Star-Bus Hybrid:
    
    [Switch1]═══[Backbone]═══[Switch2]
     /  |  \\                 /  |  \\
   PC1 PC2 PC3              PC4 PC5 PC6
   
Multiple star networks connected via bus
Common in real-world scenarios
```

---

## 3. Transmission Modes

### 3.1 Simplex (One-Way)

```
   [Sender] ──────────────────────▶ [Receiver]
   
   Examples:
   Keyboard ──────▶ Computer
   Computer ──────▶ Monitor
   Radio Tower ──▶ Radio
   
   Data flows in ONE direction only
```

### 3.2 Half-Duplex (Both Ways, Not Simultaneously)

```
   [Device A] ◀══════════════▶ [Device B]
   
   Time 1: A talks, B listens
   [A] ──────▶ [B]
   
   Time 2: B talks, A listens
   [A] ◀────── [B]
   
   NEVER both at same time
   
   Example: Walkie-Talkie
   "Over" means "your turn to talk"
```

### 3.3 Full-Duplex (Both Ways Simultaneously)

```
   [Device A] ◀══════════════▶ [Device B]
        ↕                          ↕
   Can send AND receive
   AT THE SAME TIME
   
   Example: Phone Call
   Both people can talk simultaneously
```

---

## 4. Network Architectures

### 4.1 Client-Server Model

```
         ┌─────────────┐
         │   SERVER    │
         │  (Powerful) │
         │             │
         │  - Websites │
         │  - Email    │
         │  - Files    │
         └──────┬──────┘
                │
       ┌────────┼────────┐
       │        │        │
    ┌────┐   ┌────┐   ┌────┐
    │Client│ │Client│ │Client│
    │  1  │ │  2  │ │  3  │
    └────┘   └────┘   └────┘
    
Clients REQUEST services
Server PROVIDES services

Real Example: Web Browsing
Browser (Client) → Request → Web Server
Browser (Client) ← Response ← Web Server
```

### 4.2 Peer-to-Peer (P2P) Model

```
   [Peer 1] ═══════ [Peer 2]
      ║                 ║
      ║                 ║
   [Peer 3] ═══════ [Peer 4]
   
All peers are EQUAL
Each can be client AND server
No central authority

Real Example: BitTorrent
- Download from multiple peers
- Upload to other peers
- Everyone shares
```

---

## 5. Bandwidth vs Throughput Visualization

```
BANDWIDTH (Theoretical Maximum):
┌──────────────────────────────────────┐
│  100 Mbps Internet Plan              │
│  Maximum Capacity: 100 Mbps          │
└──────────────────────────────────────┘

THROUGHPUT (Actual Performance):
┌──────────────────────────────────┐
│  Speed Test Result:              │
│  Download: 85 Mbps               │
│  Upload: 78 Mbps                 │
│  (Due to overhead, congestion)   │
└──────────────────────────────────┘

Analogy:
BANDWIDTH = Highway with 4 lanes (can handle 100 cars/min)
THROUGHPUT = Actual traffic (85 cars/min due to slowdowns)
```

---

## 6. Types of Network Delay

```
Message: [PC A] ──────────────────────▶ [PC B]

Total Delay = Propagation + Transmission + Processing + Queuing

1. TRANSMISSION DELAY:
   Time to push all bits onto the link
   ┌────────────────┐
   │ Pushing data   │
   │ onto cable     │
   └────────────────┘
   
2. PROPAGATION DELAY:
   Time for signal to travel through medium
   ───────────────────▶ (travel time)
   
3. PROCESSING DELAY:
   Router checks packet header
   ┌──────────────┐
   │ Router reads │
   │ header,      │
   │ decides path │
   └──────────────┘
   
4. QUEUING DELAY:
   Packet waits in router queue
   ┌──────────────┐
   │ Waiting in   │
   │ line...      │
   └──────────────┘
   
Real Example:
Sending email:
- Writing email = Transmission delay
- Email traveling through cables = Propagation delay
- Mail server processing = Processing delay
- Server busy, email waits = Queuing delay
```

---

## 7. Network Devices in Different Topologies

```
BUS TOPOLOGY:
PC1────PC2────PC3────PC4
  └──── Backbone Cable ────┘

STAR TOPOLOGY (Most Common):
         [Switch/Router]
          /    |    \\
       PC1    PC2    PC3
       
RING TOPOLOGY:
  PC1 ──▶ PC2 ──▶ PC3
   ▲               │
   └────── PC4 ◀───┘
   
MESH TOPOLOGY:
  PC1 ═══ PC2
   ║ ╲   ╱ ║
   ║  ╲ ╱  ║
   ║  ╱ ╲  ║
   ║ ╱   ╲ ║
  PC3 ═══ PC4
```

---

## 8. Real-World Network Example

```
HOME NETWORK (Star Topology):

              [Internet]
                  │
              [Modem]
                  │
              [Router]
             /   |   \\
          /      |      \\
       [Laptop] [Phone] [Smart TV]
          │
       [Printer]
       
Network Type: LAN
Topology: Star
Transmission: Full-duplex
Architecture: Client-Server (mostly)
```

---

## 9. Comparison Tables

### Table 1: Network Types Comparison

| Feature | PAN | LAN | MAN | WAN |
|---------|-----|-----|-----|-----|
| **Range** | 10m | 1-2 km | 5-50 km | Unlimited |
| **Speed** | Low | High | Medium | Low-Medium |
| **Cost** | Very Low | Low | Medium | High |
| **Example** | Bluetooth | Home WiFi | City network | Internet |
| **Ownership** | Individual | Single org | Single/Multiple | Multiple |

### Table 2: Topology Comparison

| Topology | Cost | Reliability | Scalability | Common Use |
|----------|------|-------------|-------------|------------|
| **Bus** | Very Low | Low | Low | Rare today |
| **Star** | Medium | Medium-High | High | Most common |
| **Ring** | Medium | Low | Low | Token Ring |
| **Mesh** | Very High | Very High | Medium | Critical systems |
| **Tree** | Medium-High | Medium | High | Large networks |
| **Hybrid** | Varies | High | High | Enterprise |

### Table 3: Transmission Modes Comparison

| Mode | Direction | Simultaneous? | Example |
|------|-----------|---------------|---------|
| **Simplex** | One-way | N/A | Keyboard |
| **Half-Duplex** | Both ways | No | Walkie-talkie |
| **Full-Duplex** | Both ways | Yes | Phone call |

### Table 4: Client-Server vs P2P

| Feature | Client-Server | P2P |
|---------|---------------|-----|
| **Architecture** | Centralized | Decentralized |
| **Control** | Central server | Distributed |
| **Cost** | Higher (server) | Lower |
| **Security** | Better | Weaker |
| **Scalability** | Good | Excellent |
| **Example** | Web, Email | BitTorrent, Blockchain |

---

## 10. Memory Aid Diagrams

### Network Types Memory Trick:
```
P  →  Personal     →  You (10m)
L  →  Local        →  Building (1-2km)
M  →  Metropolitan →  City (5-50km)
W  →  Wide         →  World (Unlimited)

Think: "People Love My Website"
       PAN, LAN, MAN, WAN
```

### Topology Visual Memory:
```
BUS:    ━━━━━━━━━━━━━━━━  (Single line)
        
STAR:       ⊙              (Center with rays)
           /|\\
          
RING:      ○               (Circle)
          
MESH:      ⊞               (Grid/Net)
          
TREE:      Y               (Branches)
          / \\
```

---

## Quick Reference Summary

```
┌─────────────────────────────────────────────────────┐
│         NETWORKING FUNDAMENTALS CHEATSHEET          │
├─────────────────────────────────────────────────────┤
│ Types:    PAN < LAN < MAN < WAN                    │
│ Topology: Star (most common), Mesh (most reliable) │
│ Modes:    Simplex, Half-Duplex, Full-Duplex        │
│ Arch:     Client-Server, P2P                       │
│ BW:       Capacity (theoretical max)               │
│ Through:  Actual speed achieved                    │
│ Latency:  Total delay (4 types)                    │
└─────────────────────────────────────────────────────┘
```
