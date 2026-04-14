# Subnetting - MCQs (30 Scenario-Based & Interview Questions)

## Beginner Level (Questions 1-10)

**Q1.** What is the main purpose of subnetting?
- A) To increase internet speed
- B) To divide a large network into smaller networks
- C) To encrypt network traffic
- D) To assign IP addresses automatically

**Answer:** B
**Explanation:** Subnetting divides a large network into smaller, manageable subnetworks to reduce broadcast traffic, improve security, and optimize IP usage.

---

**Q2.** How many usable hosts are in a /24 subnet?
- A) 128
- B) 254
- C) 256
- D) 512

**Answer:** B
**Explanation:** /24 has 8 host bits (32-24=8). Total hosts: 2^8 = 256. Usable: 256 - 2 = 254 (subtract network and broadcast addresses).

---

**Q3.** What does CIDR /26 represent?
- A) 26 hosts
- B) 26 network bits
- C) 26 subnets
- D) 26-bit MAC address

**Answer:** B
**Explanation:** CIDR /26 means 26 bits are used for the network portion, leaving 6 bits for hosts (32-26=6).

---

**Q4.** Which subnet mask equals /25?
- A) 255.255.255.0
- B) 255.255.255.128
- C) 255.255.255.192
- D) 255.255.255.224

**Answer:** B
**Explanation:** /25 = 25 ones in binary = 11111111.11111111.11111111.10000000 = 255.255.255.128

---

**Q5.** What is VLSM?
- A) Very Large Subnet Mask
- B) Variable Length Subnet Mask
- C) Virtual LAN Subnet Manager
- D) Variable Local Subnet Method

**Answer:** B
**Explanation:** VLSM (Variable Length Subnet Mask) allows different subnet masks within the same network for efficient IP allocation.

---

**Q6.** How many subnets are created when borrowing 3 bits?
- A) 3
- B) 6
- C) 8
- D) 16

**Answer:** C
**Explanation:** Number of subnets = 2^n where n = borrowed bits. 2^3 = 8 subnets.

---

**Q7.** What is the broadcast address for 192.168.1.0/24?
- A) 192.168.1.0
- B) 192.168.1.1
- C) 192.168.1.254
- D) 192.168.1.255

**Answer:** D
**Explanation:** In a /24 network, the last address (all host bits set to 1) is the broadcast address: 192.168.1.255.

---

**Q8.** Which formula calculates usable hosts?
- A) 2^n
- B) 2^n - 1
- C) 2^n - 2
- D) 2^(n-2)

**Answer:** C
**Explanation:** Usable hosts = 2^n - 2, where n = host bits. Subtract 2 for network address and broadcast address.

---

**Q9.** What is the increment for subnet mask 255.255.255.224?
- A) 16
- B) 32
- C) 64
- D) 128

**Answer:** B
**Explanation:** Increment = 256 - interesting octet = 256 - 224 = 32.

---

**Q10.** Why do we subtract 2 when calculating usable hosts?
- A) For router and switch
- B) For network and broadcast addresses
- C) For primary and backup
- D) For TCP and UDP

**Answer:** B
**Explanation:** The first address is the network address and the last is the broadcast address, neither can be assigned to hosts.

---

## Intermediate Level (Questions 11-20)

**Q11.** A company needs 5 subnets from 192.168.10.0/24. What CIDR should they use?
- A) /25
- B) /26
- C) /27
- D) /28

**Answer:** C
**Explanation:** Need 5 subnets. 2^2=4 (not enough), 2^3=8 (enough). Borrow 3 bits: /24+3 = /27. This creates 8 subnets with 30 hosts each.

---

**Q12.** What is the usable IP range for 10.0.0.0/30?
- A) 10.0.0.1 - 10.0.0.2
- B) 10.0.0.0 - 10.0.0.3
- C) 10.0.0.1 - 10.0.0.14
- D) 10.0.0.1 - 10.0.0.254

**Answer:** A
**Explanation:** /30 has 2 host bits (32-30=2). Network: 10.0.0.0, Usable: 10.0.0.1-10.0.0.2, Broadcast: 10.0.0.3. Commonly used for point-to-point links.

---

**Q13.** Which scenario requires VLSM?
- A) All departments have same number of hosts
- B) Different departments have different host requirements
- C) Only one subnet is needed
- D) Using public IP addresses

**Answer:** B
**Explanation:** VLSM is needed when different subnets require different numbers of hosts, allowing efficient IP allocation based on actual needs.

---

**Q14.** You have 172.16.0.0/16. How can you create 16 equal subnets?
- A) /17
- B) /18
- C) /20
- D) /24

**Answer:** C
**Explanation:** Need 16 subnets: 2^4=16, borrow 4 bits. New mask: /16+4 = /20. Each subnet has 2^12-2 = 4094 hosts.

---

**Q15.** Device IP: 192.168.5.75/27. Which subnet does it belong to?
- A) 192.168.5.0
- B) 192.168.5.32
- C) 192.168.5.64
- D) 192.168.5.96

**Answer:** C
**Explanation:** /27 = 255.255.255.224. Increment: 256-224=32. Subnets: .0, .32, .64, .96... 75 falls in .64 subnet (range: .64-.95).

---

**Q16.** What is the maximum number of usable hosts in /28?
- A) 8
- B) 14
- C) 16
- D) 30

**Answer:** B
**Explanation:** /28 has 4 host bits (32-28=4). Hosts: 2^4 = 16. Usable: 16-2 = 14 hosts.

---

**Q17.** An organization has these requirements: 60 hosts, 25 hosts, 10 hosts. Which VLSM allocation is correct?
- A) /26, /27, /28
- B) /25, /26, /27
C) /24, /25, /26
- D) /27, /28, /29

**Answer:** A
**Explanation:** 60 hosts needs /26 (62 hosts), 25 hosts needs /27 (30 hosts), 10 hosts needs /28 (14 hosts). Always allocate largest first.

---

**Q18.** Two devices: 10.1.1.50/26 and 10.1.1.100/26. Can they communicate directly?
- A) Yes, same network
- B) No, different subnets
- C) Yes, if they have same subnet mask
- D) No, different IP classes

**Answer:** B
**Explanation:** /26 increment is 64. First device in .0 subnet (0-63), second in .64 subnet (64-127). Different subnets require a router.

---

**Q19.** What is the subnet mask for a point-to-point WAN link (2 hosts)?
- A) /24
- B) /28
- C) /30
- D) /32

**Answer:** C
**Explanation:** /30 provides exactly 2 usable hosts (2^2-2=2), perfect for point-to-point links. Minimizes IP waste.

---

**Q20.** How many bits must you borrow to create at least 20 subnets?
- A) 3 bits
- B) 4 bits
- C) 5 bits
- D) 6 bits

**Answer:** C
**Explanation:** 2^4=16 (not enough), 2^5=32 (enough). Need to borrow 5 bits to get at least 20 subnets.

---

## Advanced Level (Questions 21-30) - Interview Scenarios

**Q21.** SCENARIO: Network 192.168.1.0/24. Departments: Sales (50), IT (25), HR (10), Reception (2). Design efficient VLSM scheme.
- A) All /26
- B) /26, /27, /28, /30
- C) /25, /26, /27, /28
- D) /27, /27, /27, /27

**Answer:** B
**Explanation:** Sales (50): /26 (62 hosts), IT (25): /27 (30 hosts), HR (10): /28 (14 hosts), Reception (2): /30 (2 hosts). Most efficient allocation.

---

**Q22.** TRICK QUESTION: Is 192.168.1.0/24 the same network as 192.168.1.0/25?
- A) Yes, same IP range
- B) No, different subnet sizes
- C) Yes, if subnet-zero is enabled
- D) No, different IP classes

**Answer:** B
**Explanation:** Different CIDR means different networks! /24 = 1 subnet with 254 hosts. /25 = 2 subnets with 126 hosts each. Subnet mask changes everything!

---

**Q23.** SCENARIO: User at 10.0.1.50/24 can't reach server at 10.0.2.50/24. Both connected to same switch. What's the issue?
- A) Wrong subnet mask
- B) Different subnets need a router
- C) IP conflict
- D) Cable problem

**Answer:** B
**Explanation:** 10.0.1.x and 10.0.2.x are different subnets. Even on same physical switch, different subnets require a router for communication.

---

**Q24.** TRICK QUESTION: How many hosts in 172.16.0.0/31?
- A) 0
- B) 2
- C) 1
- D) 254

**Answer:** B (Modern) or A (Traditional)
**Explanation:** Traditionally /31 had 0 usable hosts (2^1-2=0). Modern networks use /31 for point-to-point links (RFC 3021), giving 2 usable hosts. Interviewers test if you know both!

---

**Q25.** SCENARIO: ISP allocated you 203.0.113.0/26. You need 4 subnets. Is this possible?
- A) Yes, use /28
- B) No, not enough addresses
- C) Yes, use /24
- D) No, need public IP

**Answer:** A
**Explanation:** /26 has 64 addresses. Can create 4 subnets by borrowing 2 more bits: /28. Each /28 subnet has 14 hosts. 4×14=56 usable from 62 available.

---

**Q26.** TRICK QUESTION: What's wrong with this configuration?
IP: 192.168.1.100, Mask: 255.255.255.0, Gateway: 192.168.2.1
- A) Nothing wrong
- B) Gateway not in same subnet
- C) Wrong IP class
- D) Invalid subnet mask

**Answer:** B
**Explanation:** With /24 mask, device is in 192.168.1.0/24 subnet. Gateway 192.168.2.1 is in different subnet! Gateway must be in same subnet as device.

---

**Q27.** SCENARIO: You need to summarize these networks: 192.168.0.0/24, 192.168.1.0/24, 192.168.2.0/24, 192.168.3.0/24. What's the summary route?
- A) 192.168.0.0/22
- B) 192.168.0.0/23
- C) 192.168.0.0/24
- D) 192.168.0.0/21

**Answer:** A
**Explanation:** These 4 consecutive /24 networks can be summarized as 192.168.0.0/22. /22 covers 192.168.0.0 through 192.168.3.255 (1022 hosts).

---

**Q28.** TRICK QUESTION: If subnet mask is 255.255.255.248, how many subnets were created from a /24?
- A) 8
- B) 16
- C) 32
- D) 64

**Answer:** C
**Explanation:** /24 to /29 (248) = borrowed 5 bits. 2^5 = 32 subnets created. Each has 6 usable hosts (2^3-2=6).

---

**Q29.** SCENARIO: Company uses 10.0.0.0/8. Branch office needs 500 hosts. Most efficient subnet?
- A) /22
- B) /23
- C) /24
- D) /25

**Answer:** B
**Explanation:** 500 hosts needs 2^9=512 (closest power of 2). Host bits = 9, so network bits = 32-9 = 23. Use /23, providing 510 usable hosts.

---

**Q30.** INTERVIEW FAVORITE: Explain subnetting to a non-technical person.
- A) "It's dividing networks using binary mathematics"
- B) "Like dividing a pizza into slices for different people"
- C) "It's about IP address classes"
- D) "It's configuring routers"

**Answer:** B
**Explanation:** Interviewers test communication skills! Best answer: "Like dividing a large pizza (network) into slices (subnets) so each department gets their own portion without interfering with others."

---

## Score Interpretation

- **27-30:** Excellent! Interview-ready subnetting skills
- **20-26:** Good. Practice scenario-based problems
- **15-19:** Fair. Review VLSM and calculation methods
- **Below 15:** Re-study fundamentals, practice daily

## Interview Preparation Tips

1. **Practice calculations** until they're automatic (under 30 seconds)
2. **Understand VLSM deeply** - always allocate largest first
3. **Know common CIDR values** by heart
4. **Be ready for trick questions** about subnet masks
5. **Explain your thinking process** during interviews
6. **Draw it out** if stuck - shows methodical approach
