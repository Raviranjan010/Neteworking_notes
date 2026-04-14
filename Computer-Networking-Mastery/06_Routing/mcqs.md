# Routing - MCQs (30 Scenario-Based & Interview Questions)

## Beginner Level (Questions 1-10)

**Q1.** At which OSI layer do routers operate?
- A) Layer 1 - Physical
- B) Layer 2 - Data Link
- C) Layer 3 - Network
- D) Layer 4 - Transport

**Answer:** C
**Explanation:** Routers operate at Layer 3 (Network Layer) and make forwarding decisions based on IP addresses.

---

**Q2.** What does a router use to make forwarding decisions?
- A) MAC address
- B) Port number
- C) IP address
- D) URL

**Answer:** C
**Explanation:** Routers examine the destination IP address in packets and consult their routing table to determine where to forward them.

---

**Q3.** What is a routing table?
- A) A physical table in the router
- B) A database of known networks and how to reach them
- C) A list of connected devices
- D) A table of MAC addresses

**Answer:** B
**Explanation:** A routing table is a data structure that stores information about destination networks, next hops, metrics, and interfaces.

---

**Q4.** What is the metric in routing?
- A) The size of the packet
- B) The cost or preference of a route (lower is better)
- C) The number of routers
- D) The bandwidth of the link

**Answer:** B
**Explanation:** Metric represents the cost of a route. Different protocols use different metrics (hop count, bandwidth, delay). Lower metric = preferred route.

---

**Q5.** What is a default route?
- A) The first route in the table
- B) A catch-all route (0.0.0.0/0) for unknown destinations
- C) The fastest route
- D) The most expensive route

**Answer:** B
**Explanation:** Default route (0.0.0.0/0) is used when no specific route matches the destination. It's the "gateway of last resort" typically pointing to ISP.

---

**Q6.** Which routing type requires manual configuration?
- A) Dynamic routing
- B) Static routing
- C) Automatic routing
- D) Adaptive routing

**Answer:** B
**Explanation:** Static routing requires network administrator to manually configure each route. It doesn't change unless manually updated.

---

**Q7.** What is the maximum hop count in RIP?
- A) 10
- B) 15
- C) 25
- D) Unlimited

**Answer:** B
**Explanation:** RIP has a maximum hop count of 15. A destination 16 hops away is considered unreachable. This limits RIP to small networks.

---

**Q8.** What is convergence in routing?
- A) When routers turn on
- B) Time taken for all routers to agree on network topology after a change
- C) When routing tables are full
- D) When packets are lost

**Answer:** B
**Explanation:** Convergence is the time it takes for all routers to update their routing tables and agree on the network topology after a change (link failure, new network, etc.).

---

**Q9.** Which protocol uses hop count as its metric?
- A) OSPF
- B) RIP
- C) EIGRP
- D) BGP

**Answer:** B
**Explanation:** RIP (Routing Information Protocol) uses hop count as its metric, counting the number of routers a packet must pass through.

---

**Q10.** What happens to MAC addresses as a packet travels through routers?
- A) They stay the same
- B) They change at each hop
- C) They are deleted
- D) They are encrypted

**Answer:** B
**Explanation:** MAC addresses are used for local delivery only. At each router hop, source and destination MAC addresses are changed to match the current link.

---

## Intermediate Level (Questions 11-20)

**Q11.** What is Administrative Distance (AD)?
- A) The physical distance between routers
- B) A measure of trustworthiness of routing information source
- C) The number of administrators
- D) The router's priority

**Answer:** B
**Explanation:** AD is a value (0-255) that indicates how trustworthy a routing source is. Lower AD = more trusted. Used when multiple sources provide routes to same destination.

---

**Q12.** Which has the lowest (best) AD?
- A) OSPF (110)
- B) RIP (120)
- C) Static route (1)
- D) Connected interface (0)

**Answer:** D
**Explanation:** Connected interface has AD of 0 (most trusted), followed by static route (1), then dynamic protocols. Directly connected networks are always preferred.

---

**Q13.** How does OSPF calculate its metric?
- A) Hop count
- B) Based on bandwidth (cost)
- C) Number of routes
- D) Delay

**Answer:** B
**Explanation:** OSPF uses cost based on bandwidth. Cost = Reference Bandwidth / Interface Bandwidth. Higher bandwidth = lower cost = better path.

---

**Q14.** What is a routing loop?
- A) When a packet circles between routers endlessly
- B) When routing table is full
- C) When router restarts
- D) When routes are updated

**Answer:** A
**Explanation:** Routing loop occurs when packets cycle between routers in a loop due to incorrect routing information, never reaching destination. Prevented by TTL, split horizon, etc.

---

**Q15.** Which routing protocol is a link-state protocol?
- A) RIP
- B) OSPF
- C) BGP
- D) EIGRP (classic)

**Answer:** B
**Explanation:** OSPF is a link-state protocol where each router builds complete topology map. RIP is distance-vector, BGP is path-vector.

---

**Q16.** What is the TTL (Time To Live) field used for?
- A) To encrypt packets
- B) To prevent routing loops by limiting packet lifetime
- C) To prioritize traffic
- D) To compress data

**Answer:** B
**Explanation:** TTL is decremented at each router hop. When it reaches 0, packet is discarded. This prevents packets from circulating forever in routing loops.

---

**Q17.** In the packet flow, what changes at each router hop?
- A) Source and Destination IP addresses
- B) Source and Destination MAC addresses
- C) Both IP and MAC addresses
- D) Neither IP nor MAC addresses

**Answer:** B
**Explanation:** IP addresses remain constant end-to-end. MAC addresses change at each hop because they're used for local (link-by-link) delivery only.

---

**Q18.** What is a stub network?
- A) A network with multiple exit paths
- B) A network with only one exit path
- C) A wireless network
- D) A failed network

**Answer:** B
**Explanation:** A stub network has only one way in and out. Perfect candidate for static routing since there's no alternative path to consider.

---

**Q19.** Which routing protocol is used on the Internet between ISPs?
- A) OSPF
- B) RIP
- C) BGP
- D) EIGRP

**Answer:** C
**Explanation:** BGP (Border Gateway Protocol) is the exterior gateway protocol used to exchange routing information between autonomous systems (ISPs) on the Internet.

---

**Q20.** What is the purpose of Hello packets in OSPF?
- A) To send user data
- B) To discover neighbors and maintain adjacency
- C) To update routes
- D) To test connectivity

**Answer:** B
**Explanation:** OSPF Hello packets discover neighboring routers, establish adjacencies, and maintain relationships. If Hellos stop, neighbor is considered down.

---

## Advanced Level (Questions 21-30) - Interview Scenarios

**Q21.** SCENARIO: Router learns same network via OSPF (AD 110) and RIP (AD 120). Which route is installed?
- A) RIP route
- B) OSPF route
- C) Both routes
- D) Neither route

**Answer:** B
**Explanation:** Router chooses route with lowest AD. OSPF (110) < RIP (120), so OSPF route is installed in routing table.

---

**Q22.** TRICK QUESTION: PC-A (192.168.1.10/24) sends packet to PC-B (192.168.1.20/24). Both on same switch. How many router hops?
- A) 1 hop
- B) 2 hops
- C) 0 hops (no router needed)
- D) Depends on routing protocol

**Answer:** C
**Explanation:** Both devices are in same subnet (192.168.1.0/24). Communication happens at Layer 2 via switch using MAC addresses. No router involvement!

---

**Q23.** SCENARIO: Network 10.0.0.0/8. You need to reach 8.8.8.8. No specific route exists. What happens?
- A) Packet is dropped immediately
- B) Router uses default route (if configured)
- C) Router sends ICMP error
- D) Router broadcasts to find route

**Answer:** B
**Explanation:** If no specific route matches, router checks for default route (0.0.0.0/0). If present, packet is forwarded there. If no default route, packet dropped and ICMP "destination unreachable" sent.

---

**Q24.** SCENARIO: Router has these routes to 10.0.1.0/24:
- OSPF: cost 50
- Static: next-hop 172.16.0.2
- RIP: 3 hops
Which is preferred?
- A) OSPF
- B) Static
- C) RIP
- D) Load balance all three

**Answer:** B
**Explanation:** Compare AD first! Static (AD 1) < OSPF (AD 110) < RIP (AD 120). Static route wins regardless of metrics because it has lowest AD.

---

**Q25.** TRICK QUESTION: Why can't you ping 10.0.1.50 from 192.168.1.10 even though routing is correct?
- A) Wrong routing protocol
- B) NAT not configured or ACL blocking
- C) Wrong subnet mask
- D) Need BGP

**Answer:** B
**Explanation:** Even with correct routing, communication can fail due to: NAT not translating private IPs, ACLs (Access Control Lists) blocking ICMP, firewall rules, or asymmetric routing issues.

---

**Q26.** SCENARIO: OSPF network with Area 0 and Area 1. Link between them fails. What happens?
- A) Entire network fails
- B) Areas can't communicate, but internal routing works
- C) BGP takes over
- D) RIP automatically starts

**Answer:** B
**Explanation:** OSPF areas lose inter-area connectivity, but routers within each area still have full connectivity. This is why hierarchical design with areas is beneficial - limits failure scope.

---

**Q27.** INTERVIEW FAVORITE: Explain the difference between routing and forwarding.
- A) They are the same thing
- B) Routing = building routing table, Forwarding = sending packets based on table
- C) Routing is Layer 2, Forwarding is Layer 3
- D) Routing is slow, Forwarding is fast

**Answer:** B
**Explanation:** Routing (control plane) = learning routes and building routing table. Forwarding (data plane) = actual packet transmission using the routing table. Separation is key to router architecture.

---

**Q28.** SCENARIO: Two equal-cost paths to destination. Router behavior?
- A) Chooses first path only
- B) Load balances across both paths
- C) Uses both simultaneously for redundancy
- D) BGP decides

**Answer:** B
**Explanation:** Most routing protocols support equal-cost load balancing (ECMP). Router distributes traffic across both paths, typically per-packet or per-destination basis.

---

**Q29.** TRICK QUESTION: What's wrong? PC: IP=192.168.1.10/24, Gateway=192.168.2.1
- A) Nothing
- B) Gateway not in same subnet as PC
- C) Wrong IP class
- D) Invalid configuration

**Answer:** B
**Explanation:** PC is in 192.168.1.0/24 subnet, but gateway is 192.168.2.1 (different subnet). Gateway MUST be in same subnet as the device. Correct gateway would be 192.168.1.1.

---

**Q30.** INTERVIEW SCENARIO: Design routing for company with HQ and 50 branches.
- A) Static routing to all branches
- B) RIP everywhere
- C) OSPF with hierarchical design
- D) No routing needed

**Answer:** C
**Explanation:** For 50 branches: Static = unmanageable, RIP = too slow/limited. OSPF with hierarchical design (Area 0 for backbone, areas for regions) provides scalability, fast convergence, and manageability.

---

## Score Interpretation

- **27-30:** Excellent! Interview-ready routing knowledge
- **20-26:** Good. Practice scenario-based troubleshooting
- **15-19:** Fair. Review packet flow and protocol differences
- **Below 15:** Re-study routing fundamentals and packet flow

## Interview Success Tips

1. **Always explain packet flow** with MAC/IP address changes
2. **Know when to use static vs dynamic** routing
3. **Understand AD values** - they determine route preference
4. **Be ready to troubleshoot** step-by-step
5. **Mention real protocols** you understand (OSPF, BGP, etc.)
6. **Draw diagrams** if allowed - shows clear thinking
7. **Explain WHY**, not just WHAT - demonstrates deep understanding
