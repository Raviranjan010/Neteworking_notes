# Network Devices - MCQs (30 Scenario-Based)

## Beginner Level (Questions 1-10)

**Q1.** At which OSI layer does a hub operate?
- A) Layer 1 - Physical
- B) Layer 2 - Data Link
- C) Layer 3 - Network
- D) Layer 4 - Transport

**Answer:** A
**Explanation:** Hubs operate at Layer 1 (Physical Layer). They simply repeat electrical signals to all ports without any intelligence or addressing.

---

**Q2.** What address does a switch use to forward frames?
- A) IP address
- B) MAC address
- C) Port number
- D) URL

**Answer:** B
**Explanation:** Switches operate at Layer 2 and use MAC addresses to make forwarding decisions. They maintain a MAC address table mapping MAC addresses to ports.

---

**Q3.** What address does a router use to forward packets?
- A) MAC address
- B) IP address
- C) Port number
- D) Email address

**Answer:** B
**Explanation:** Routers operate at Layer 3 (Network Layer) and use IP addresses to route packets between different networks using routing tables.

---

**Q4.** How many collision domains does an 8-port hub have?
- A) 1
- B) 4
- C) 8
- D) 16

**Answer:** A
**Explanation:** A hub creates a single collision domain. All ports share the same bandwidth and collisions can occur when multiple devices transmit simultaneously.

---

**Q5.** How many collision domains does an 8-port switch have?
- A) 1
- B) 4
- C) 8
- D) 16

**Answer:** C
**Explanation:** Each port on a switch is its own collision domain. An 8-port switch creates 8 separate collision domains, eliminating collisions.

---

**Q6.** What does VLAN stand for?
- A) Variable Local Area Network
- B) Virtual Local Area Network
- C) Verified Link Access Network
- D) Virtual Link Aggregation Network

**Answer:** B
**Explanation:** VLAN (Virtual Local Area Network) logically segments a physical switch into multiple broadcast domains.

---

**Q7.** Which device can connect different networks together?
- A) Hub
- B) Switch
- C) Router
- D) Repeater

**Answer:** C
**Explanation:** Routers connect different networks (different IP subnets) and route packets between them based on IP addresses.

---

**Q8.** What happens when a switch receives a frame with unknown destination MAC?
- A) Drops the frame
- B) Sends to all ports except source
- C) Sends to default gateway
- D) Requests MAC address

**Answer:** B
**Explanation:** When destination MAC is not in the MAC address table, switch floods the frame to all ports except the receiving port. This is how it learns where devices are.

---

**Q9.** Which device stops broadcast domains?
- A) Hub
- B) Switch
- C) Router
- D) Bridge

**Answer:** C
**Explanation:** Routers stop broadcast domains. Each router interface is a separate broadcast domain. Switches and hubs forward broadcasts.

---

**Q10.** What is the purpose of a trunk port?
- A) Connect to end devices
- B) Carry multiple VLANs between switches
- C) Provide internet access
- D) Connect to router only

**Answer:** B
**Explanation:** Trunk ports carry traffic for multiple VLANs between switches using 802.1Q tagging. Access ports carry single VLAN traffic to end devices.

---

## Intermediate Level (Questions 11-20)

**Q11.** How does a switch build its MAC address table?
- A) Administrator manually enters addresses
- B) Learns from source MAC addresses of incoming frames
- C) Downloads from DHCP server
- D) Uses ARP requests

**Answer:** B
**Explanation:** Switches automatically learn MAC addresses by examining the source MAC address of every incoming frame and recording which port it arrived on.

---

**Q12.** SCENARIO: Two switches need to carry traffic for VLANs 10, 20, and 30. How should they be connected?
- A) Three separate cables (one per VLAN)
- B) Single trunk link with 802.1Q tagging
- C) Through a hub
- D) Through a router

**Answer:** B
**Explanation:** A trunk link with 802.1Q tagging allows multiple VLANs to traverse a single physical connection. Each frame is tagged with VLAN ID.

---

**Q13.** What is the VLAN ID range for 802.1Q?
- A) 1-100
- B) 1-1024
- C) 1-4094
- D) 1-65535

**Answer:** C
**Explanation:** 802.1Q uses 12-bit VLAN ID field, allowing 4096 values (0-4095). VLAN 0 and 4095 reserved, usable range is 1-4094.

---

**Q14.** SCENARIO: PC in VLAN 10 needs to communicate with server in VLAN 20. What's required?
- A) Nothing, they're on same switch
- B) Router or Layer 3 switch for inter-VLAN routing
- C) Hub to connect VLANs
- D) Change VLAN membership

**Answer:** B
**Explanation:** Different VLANs are separate broadcast domains. Communication between VLANs requires routing (Layer 3 device) - either router or Layer 3 switch.

---

**Q15.** What is "Router on a Stick"?
- A) Router with wireless antenna
- B) Single router interface handling multiple VLANs via subinterfaces
- C) Router connected to stick-shaped antenna
- D) Backup router

**Answer:** B
**Explanation:** Router on a Stick uses a single physical interface with multiple logical subinterfaces (one per VLAN) connected to switch trunk port for inter-VLAN routing.

---

**Q16.** SCENARIO: Network experiencing broadcast storms. Best solution?
- A) Replace hubs with switches
- B) Implement VLANs to segment broadcast domains
- C) Add more hubs
- D) Increase bandwidth

**Answer:** B
**Explanation:** VLANs segment large broadcast domains into smaller ones, containing broadcast storms to single VLAN instead of affecting entire network.

---

**Q17.** Which switch port type should be used to connect a PC?
- A) Trunk port
- B) Access port
- C) Console port
- D) Uplink port

**Answer:** B
**Explanation:** Access ports connect end devices (PCs, printers) and carry traffic for single VLAN (untagged). Trunk ports connect switches and carry multiple VLANs.

---

**Q18.** What is the native VLAN in 802.1Q trunking?
- A) VLAN with highest priority
- B) VLAN that travels untagged on trunk
- C) Default VLAN 0
- D) Management VLAN only

**Answer:** B
**Explanation:** Native VLAN (default VLAN 1) travels untagged on trunk links. Both switches must agree on native VLAN or security issues occur.

---

**Q19.** SCENARIO: Switch MAC table is full. What happens to new MAC addresses?
- A) Switch stops working
- B) Frames with unknown MACs are flooded
- C) Oldest entries are removed
- D) New MACs are rejected

**Answer:** B
**Explanation:** When MAC table is full, switch can't learn new addresses. Frames to unknown destinations are flooded to all ports (like initial behavior). Eventually oldest entries age out.

---

**Q20.** What is the main advantage of Layer 3 switch over router?
- A) Cheaper
- B) Faster packet forwarding (hardware-based)
- C) More features
- D) Better security

**Answer:** B
**Explanation:** Layer 3 switches use hardware ASICs for routing, providing wire-speed routing performance. Routers typically use software-based routing (slower).

---

## Advanced Level (Questions 21-30) - Scenario-Based

**Q21.** SCENARIO: User in VLAN 10 can't reach server in VLAN 10 on different switch. Same switch VLAN 10 users work fine. Issue?
- A) Router down
- B) Trunk link missing or misconfigured between switches
- C) Firewall blocking
- D) Wrong IP address

**Answer:** B
**Explanation:** Same VLAN across different switches requires trunk link to carry VLAN traffic. If trunk missing/misconfigured, VLAN 10 can't pass between switches. Check: switchport mode trunk, allowed VLANs.

---

**Q22.** SCENARIO: Network has single point of failure at core switch. Solution?
- A) Buy bigger switch
- B) Implement redundant core switches with STP
- C) Add more access switches
- D) Use hub instead

**Answer:** B
**Explanation:** Redundant core switches with Spanning Tree Protocol (STP) provide failover. If one core fails, STP recalculates and uses backup path. Prevents single point of failure.

---

**Q23.** SCENARIO: User connects laptop to network port. Gets 169.254.x.x address. Can access local devices but not internet. Cause?
- A) Router down
- B) DHCP server unreachable, APIPA assigned
- C) DNS failure
- D) Firewall blocking

**Answer:** B
**Explanation:** 169.254.x.x is APIPA (Automatic Private IP Addressing). Assigned when DHCP server can't be reached. Local communication works but no gateway/internet access without proper DHCP configuration.

---

**Q24.** INTERVIEW: Why not use hubs in modern networks?
- A) Too expensive
- B) Security risk, collisions, poor performance
- C) Don't support high speeds
- D) Difficult to install

**Answer:** B
**Explanation:** Hubs broadcast to all ports (security risk), create single collision domain (performance issue), half-duplex only. Switches provide dedicated bandwidth per port, full-duplex, security through MAC learning.

---

**Q25.** SCENARIO: After adding new switch, network has loops and broadcast storms. Missing configuration?
- A) VLAN configuration
- B) Spanning Tree Protocol (STP)
- C) Routing protocol
- D) QoS

**Answer:** B
**Explanation:** STP prevents Layer 2 loops in redundant switch topologies. Without STP, broadcast frames circulate endlessly causing broadcast storms. STP blocks redundant paths, enables them if primary fails.

---

**Q26.** SCENARIO: VoIP phones and PCs share same switch ports. Phones in VLAN 100, PCs in VLAN 10. How configured?
- A) Two physical ports per desk
- B) Voice VLAN feature with tagged/untagged traffic
- C) Separate switches for phones
- D) Can't be done

**Answer:** B
**Explanation:** Switch voice VLAN feature allows phone (tagged VLAN 100) and PC (untagged VLAN 10) on same port. Phone tags its traffic, PC traffic untagged. Single cable, separate logical networks.

---

**Q27.** SCENARIO: Router interface shows "line protocol down". What does this mean?
- A) IP address misconfigured
- B) Layer 2 issue (cable, switch port, encapsulation mismatch)
- C) Routing protocol down
- D) Interface administratively shut down

**Answer:** B
**Explanation:** "Line protocol down" indicates Layer 2 problem. Could be: cable unplugged, switch port down, encapsulation mismatch (HDLC vs PPP), clock rate missing on serial. Check physical and data link layers.

---

**Q28.** INTERVIEW: Explain MAC address table aging.
- A) MAC addresses never expire
- B) Entries removed after timeout (default 300s) if no traffic seen
- C) Removed after 24 hours
- D) Only removed manually

**Answer:** B
**Explanation:** MAC table entries have aging timer (default 300 seconds/5 minutes). If no frames seen from MAC within timeout, entry removed. Prevents stale entries when devices move or disconnect.

---

**Q29.** SCENARIO: Company merging, need to connect two networks with overlapping IP ranges (both use 192.168.1.0/24). Solution?
- A) Direct connection
- B) NAT between networks
- C) Can't be done
- D) Change one network's IP scheme

**Answer:** B (temporary) or D (permanent)
**Explanation:** Overlapping IPs cause routing conflicts. Temporary: NAT one network. Permanent (best): Re-IP one network to different range (192.168.2.0/24). Plan addressing scheme properly.

---

**Q30.** INTERVIEW DEEP DIVE: Design network for 1000-user company with 5 departments.
```
A) Single flat network with one big switch
B) Hierarchical design with VLANs, redundant core, firewalls
C) Peer-to-peer network
D) All wireless
```

**Answer:** B
**Explanation:**
```
Hierarchical Design:
- Access Layer: 20-30 access switches (edge connectivity)
- Distribution Layer: 4-6 distribution switches (aggregation)
- Core Layer: 2 redundant core switches (high-speed backbone)

VLANs:
- VLAN 10-50: Departments (Sales, IT, HR, Finance, Marketing)
- VLAN 100: Servers
- VLAN 200: Management
- VLAN 300: Voice/VoIP

Security:
- Firewall at perimeter
- Inter-VLAN routing with ACLs
- 802.1X authentication

Redundancy:
- Dual core switches
- Multiple paths (STP)
- Redundant power supplies

Benefits: Scalable, secure, manageable, fault-tolerant
```

---

## Score Interpretation

- **27-30:** Excellent! Interview-ready network device knowledge
- **20-26:** Good. Practice more scenario-based troubleshooting
- **15-19:** Fair. Review VLANs and device differences
- **Below 15:** Re-study network devices fundamentals

## Interview Success Tips

1. **Know device differences deeply** - Hub vs Switch vs Router
2. **Understand MAC table learning** - Critical for switches
3. **VLANs are always asked** - Configuration, troubleshooting, design
4. **Know enterprise architecture** - Access-Distribution-Core model
5. **Be ready to design** - Given requirements, propose solution
6. **Troubleshooting methodology** - Layer-by-layer approach
