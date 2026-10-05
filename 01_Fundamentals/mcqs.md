# Computer Networking Fundamentals - MCQs

## Beginner Level (Questions 1-10)

**Q1.** What is a computer network?
- A) A single computer with multiple programs
- B) A collection of interconnected devices that can communicate
- C) A type of software
- D) A hardware component

**Answer:** B
**Explanation:** A computer network is a collection of interconnected devices (nodes) that can communicate and share resources with each other.

---

**Q2.** Which of the following is NOT a network type based on geographical coverage?
- A) LAN
- B) WAN
- C) MAN
- D) TCP

**Answer:** D
**Explanation:** TCP (Transmission Control Protocol) is a protocol, not a network type. LAN, WAN, and MAN are network types classified by coverage area.

---

**Q3.** What does PAN stand for?
- A) Public Area Network
- B) Personal Area Network
- C) Private Access Network
- D) Primary Area Network

**Answer:** B
**Explanation:** PAN stands for Personal Area Network, which covers a very small area (up to 10 meters) around an individual, like Bluetooth connections.

---

**Q4.** In which topology do all devices connect to a central device?
- A) Bus topology
- B) Ring topology
- C) Star topology
- D) Mesh topology

**Answer:** C
**Explanation:** In star topology, all devices (nodes) connect to a central device like a switch or hub. This is the most common topology today.

---

**Q5.** Which transmission mode allows data to flow in both directions but NOT simultaneously?
- A) Simplex
- B) Half-duplex
- C) Full-duplex
- D) Multiplex

**Answer:** B
**Explanation:** Half-duplex allows bidirectional communication, but only one direction at a time. Example: walkie-talkie.

---

**Q6.** What is bandwidth?
- A) The actual speed of data transfer
- B) The maximum data transfer capacity
- C) The time delay in transmission
- D) The number of devices in a network

**Answer:** B
**Explanation:** Bandwidth is the theoretical maximum data transfer capacity of a network, measured in bits per second (bps).

---

**Q7.** Which network covers a city-wide area?
- A) LAN
- B) MAN
- C) WAN
- D) PAN

**Answer:** B
**Explanation:** MAN (Metropolitan Area Network) covers a city or metropolitan area, typically 5-50 kilometers.

---

**Q8.** In the client-server model, what is the role of the server?
- A) Request services
- B) Provide services
- C) Both request and provide services
- D) Neither request nor provide services

**Answer:** B
**Explanation:** In client-server architecture, the server provides services/resources, while clients request and use those services.

---

**Q9.** Which topology has the highest reliability?
- A) Bus
- B) Star
- C) Ring
- D) Mesh

**Answer:** D
**Explanation:** Mesh topology has the highest reliability because there are multiple paths between devices. If one path fails, data can take alternative routes.

---

**Q10.** What is latency?
- A) Amount of data transferred
- B) Time delay in data transmission
- C) Network bandwidth
- D) Number of packets lost

**Answer:** B
**Explanation:** Latency is the time it takes for data to travel from source to destination, measured in milliseconds (ms).

---

## Intermediate Level (Questions 11-20)

**Q11.** Which of the following is an example of simplex transmission?
- A) Telephone conversation
- B) Walkie-talkie
- C) Keyboard to computer
- D) Video conferencing

**Answer:** C
**Explanation:** Keyboard to computer is simplex because data flows only in one direction (from keyboard to computer). The keyboard cannot receive data.

---

**Q12.** What is the main disadvantage of bus topology?
- A) Requires too much cable
- B) Difficult to install
- C) Single point of failure (main cable)
- D) Too expensive

**Answer:** C
**Explanation:** In bus topology, all devices share a single backbone cable. If this cable fails, the entire network goes down.

---

**Q13.** Throughput is always:
- A) Greater than bandwidth
- B) Equal to bandwidth
- C) Less than or equal to bandwidth
- D) Unrelated to bandwidth

**Answer:** C
**Explanation:** Throughput (actual data rate) is always less than or equal to bandwidth (theoretical maximum) due to overhead, congestion, and other factors.

---

**Q14.** Which network type would be most appropriate for connecting multiple office buildings in a city?
- A) PAN
- B) LAN
- C) MAN
- D) WAN

**Answer:** C
**Explanation:** MAN (Metropolitan Area Network) is designed for city-wide connectivity, making it ideal for connecting multiple buildings in a city.

---

**Q15.** In peer-to-peer (P2P) architecture:
- A) There is a dedicated server
- B) All devices are equal and can act as both client and server
- C) Only one device can share resources
- D) It requires special hardware

**Answer:** B
**Explanation:** In P2P networks, all devices (peers) are equal and can function as both clients (requesting resources) and servers (providing resources).

---

**Q16.** Which factor does NOT affect network throughput?
- A) Network congestion
- B) Transmission medium quality
- C) Number of protocols installed
- D) Distance between nodes

**Answer:** C
**Explanation:** The number of protocols installed doesn't directly affect throughput. Congestion, medium quality, and distance all impact actual data transfer rates.

---

**Q17.** What is the typical range of Bluetooth (PAN)?
- A) 100 meters
- B) 10 meters
- C) 1 kilometer
- D) 50 kilometers

**Answer:** B
**Explanation:** Bluetooth typically has a range of up to 10 meters, making it suitable for Personal Area Networks (PAN).

---

**Q18.** Which topology is most cost-effective for a small network?
- A) Full mesh
- B) Bus
- C) Tree
- D) Hybrid

**Answer:** B
**Explanation:** Bus topology is the most cost-effective as it requires the least amount of cable and simple installation, though it's rarely used today.

---

**Q19.** The Internet is an example of:
- A) LAN
- B) MAN
- C) WAN
- D) PAN

**Answer:** C
**Explanation:** The Internet is the largest example of a WAN (Wide Area Network), connecting millions of networks worldwide across unlimited geographical areas.

---

**Q20.** Which type of delay occurs when a packet waits in a router's queue?
- A) Propagation delay
- B) Transmission delay
- C) Processing delay
- D) Queuing delay

**Answer:** D
**Explanation:** Queuing delay is the time a packet spends waiting in a router's queue before it can be processed and forwarded.

---

## Advanced Level (Questions 21-30)

**Q21.** In a full mesh topology with 6 nodes, how many connections are required?
- A) 6
- B) 12
- C) 15
- D) 30

**Answer:** C
**Explanation:** Formula for full mesh: n(n-1)/2 where n is the number of nodes. For 6 nodes: 6(5)/2 = 15 connections.

---

**Q22.** Which combination of delays determines the total latency in a network?
- A) Only propagation delay
- B) Propagation + transmission delay
- C) Propagation + transmission + processing + queuing delay
- D) Only queuing delay

**Answer:** C
**Explanation:** Total latency = Propagation delay (travel time) + Transmission delay (pushing bits) + Processing delay (router processing) + Queuing delay (waiting time).

---

**Q23.** A network uses star topology. If the central switch fails, what happens?
- A) Only one node is affected
- B) Half the network goes down
- C) The entire network goes down
- D) Nothing happens, it's fault-tolerant

**Answer:** C
**Explanation:** In star topology, the central switch is a single point of failure. If it fails, all connected devices lose network connectivity.

---

**Q24.** Why is full-duplex more efficient than half-duplex?
- A) It uses less bandwidth
- B) It allows simultaneous two-way communication
- C) It requires fewer cables
- D) It's cheaper to implement

**Answer:** B
**Explanation:** Full-duplex allows data to flow in both directions simultaneously (like a phone call), effectively doubling the communication capacity compared to half-duplex.

---

**Q25.** Which statement about hybrid topology is TRUE?
- A) It's only theoretical, not used in practice
- B) It combines two or more different topologies
- C) It's the cheapest topology
- D) It's less reliable than single topologies

**Answer:** B
**Explanation:** Hybrid topology combines two or more different topologies to leverage their advantages. Most real-world enterprise networks use hybrid topologies.

---

**Q26.** If a network has high bandwidth but high latency, what user experience would result?
- A) Fast file downloads but slow website loading
- B) Slow everything
- C) Fast everything
- D) Fast website loading but slow downloads

**Answer:** A
**Explanation:** High bandwidth allows large data transfers (fast downloads), but high latency causes delays in initial connections (slow website loading).

---

**Q27.** In which scenario would you choose P2P over client-server?
- A) Corporate email system
- B) E-commerce website
- C) File sharing among friends
- D) Bank ATM network

**Answer:** C
**Explanation:** P2P is suitable for decentralized file sharing where no central authority is needed. Corporate systems require centralized control (client-server).

---

**Q28.** What is the main reason star topology is more popular than bus topology?
- A) It uses less cable
- B) Better fault isolation and easier management
- C) It's faster
- D) It doesn't require a central device

**Answer:** B
**Explanation:** Star topology provides better fault isolation (one node failure doesn't affect others) and is easier to manage and troubleshoot compared to bus topology.

---

**Q29.** Which factor would cause throughput to be significantly lower than bandwidth?
- A) Using fiber optic cables
- B) Network congestion with many users
- C) Short distance between nodes
- D) Using modern protocols

**Answer:** B
**Explanation:** Network congestion causes packets to queue, be dropped, or retransmitted, significantly reducing actual throughput compared to theoretical bandwidth.

---

**Q30.** A company has offices in New York, London, and Tokyo. What type of network connects all three offices?
- A) LAN
- B) MAN
- C) WAN
- D) PAN

**Answer:** C
**Explanation:** Connecting offices across different countries requires a WAN (Wide Area Network), which spans unlimited geographical distances using technologies like leased lines, satellites, or the internet.

---

## Score Interpretation

- **27-30 Correct:** Excellent! You have strong fundamentals. Move to next topic.
- **20-26 Correct:** Good understanding. Review weak areas before proceeding.
- **15-19 Correct:** Fair. Re-read the notes and focus on misunderstood concepts.
- **Below 15:** Needs significant review. Go back to notes.md and study again.

---

## Tips for Using These MCQs

1. **First attempt:** Try without looking at answers
2. **Score yourself:** Be honest about your knowledge
3. **Review explanations:** Read ALL explanations, even for correct answers
4. **Note weak areas:** Mark questions you got wrong
5. **Retake after review:** Try again after studying weak topics
6. **Explain aloud:** Try explaining why each answer is correct
