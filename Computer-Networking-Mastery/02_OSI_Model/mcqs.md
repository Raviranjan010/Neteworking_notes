# OSI Model - MCQs

## Beginner Level (Questions 1-10)

**Q1.** How many layers does the OSI model have?
- A) 4
- B) 5
- C) 6
- D) 7

**Answer:** D
**Explanation:** The OSI model has 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application.

---

**Q2.** Which layer is responsible for routing packets?
- A) Data Link Layer
- B) Network Layer
- C) Transport Layer
- D) Session Layer

**Answer:** B
**Explanation:** The Network Layer (Layer 3) handles logical addressing (IP addresses) and routing packets between different networks.

---

**Q3.** What is the data unit at the Physical layer?
- A) Frame
- B) Packet
- C) Bit
- D) Segment

**Answer:** C
**Explanation:** The Physical layer transmits raw bits (0s and 1s) over the physical medium.

---

**Q4.** TCP and UDP operate at which layer?
- A) Network Layer
- B) Transport Layer
- C) Session Layer
- D) Application Layer

**Answer:** B
**Explanation:** TCP and UDP are Transport Layer (Layer 4) protocols that handle end-to-end communication.

---

**Q5.** MAC addresses are used at which layer?
- A) Physical Layer
- B) Data Link Layer
- C) Network Layer
- D) Transport Layer

**Answer:** B
**Explanation:** MAC (Media Access Control) addresses are physical addresses used at the Data Link Layer (Layer 2) for communication within the same network.

---

**Q6.** Which layer handles encryption and decryption?
- A) Application Layer
- B) Session Layer
- C) Presentation Layer
- D) Transport Layer

**Answer:** C
**Explanation:** The Presentation Layer (Layer 6) is responsible for data translation, encryption, decryption, and compression.

---

**Q7.** HTTP, FTP, and SMTP are protocols of which layer?
- A) Transport Layer
- B) Session Layer
- C) Presentation Layer
- D) Application Layer

**Answer:** D
**Explanation:** HTTP, FTP, SMTP, DNS, and other user-facing protocols operate at the Application Layer (Layer 7).

---

**Q8.** What does OSI stand for?
- A) Open System Integration
- B) Open Systems Interconnection
- C) Operational System Interface
- D) Organized System Interconnection

**Answer:** B
**Explanation:** OSI stands for Open Systems Interconnection, a standard developed by ISO in 1984.

---

**Q9.** Routers operate at which layer?
- A) Data Link Layer
- B) Network Layer
- C) Transport Layer
- D) Physical Layer

**Answer:** B
**Explanation:** Routers are Layer 3 (Network Layer) devices that use IP addresses to route packets between different networks.

---

**Q10.** Switches operate at which layer?
- A) Physical Layer
- B) Data Link Layer
- C) Network Layer
- D) Transport Layer

**Answer:** B
**Explanation:** Traditional switches are Layer 2 (Data Link Layer) devices that use MAC addresses to forward frames within the same network.

---

## Intermediate Level (Questions 11-20)

**Q11.** What is encapsulation?
- A) Removing headers from data
- B) Adding headers at each layer as data moves down
- C) Encrypting data
- D) Compressing data

**Answer:** B
**Explanation:** Encapsulation is the process where each OSI layer adds its own header (and sometimes trailer) to the data as it moves down from Layer 7 to Layer 1.

---

**Q12.** Which layer establishes, maintains, and terminates sessions?
- A) Transport Layer
- B) Session Layer
- C) Presentation Layer
- D) Application Layer

**Answer:** B
**Explanation:** The Session Layer (Layer 5) manages sessions (connections) between applications, including establishment, maintenance, and termination.

---

**Q13.** What is the correct order of data units from Layer 1 to Layer 4?
- A) Frame, Bit, Packet, Segment
- B) Bit, Frame, Packet, Segment
- C) Bit, Packet, Frame, Segment
- D) Segment, Packet, Frame, Bit

**Answer:** B
**Explanation:** Layer 1: Bit, Layer 2: Frame, Layer 3: Packet, Layer 4: Segment.

---

**Q14.** Which protocol provides unreliable, connectionless communication?
- A) TCP
- B) UDP
- C) HTTP
- D) IP

**Answer:** B
**Explanation:** UDP (User Datagram Protocol) is connectionless and unreliable (no guarantee of delivery), making it faster than TCP.

---

**Q15.** Port numbers are associated with which layer?
- A) Network Layer
- B) Transport Layer
- C) Session Layer
- D) Application Layer

**Answer:** B
**Explanation:** Port numbers are used at the Transport Layer to identify specific applications or services (e.g., port 80 for HTTP).

---

**Q16.** Which device operates at Layer 1?
- A) Router
- B) Switch
- C) Hub
- D) Bridge

**Answer:** C
**Explanation:** Hubs and repeaters operate at the Physical Layer (Layer 1), simply repeating signals without any intelligence.

---

**Q17.** What layer handles fragmentation of packets?
- A) Data Link Layer
- B) Network Layer
- C) Transport Layer
- D) Session Layer

**Answer:** B
**Explanation:** The Network Layer can fragment large packets into smaller ones if the next network has a smaller MTU (Maximum Transmission Unit).

---

**Q18.** Error detection using CRC happens at which layer?
- A) Physical Layer
- B) Data Link Layer
- C) Network Layer
- D) Transport Layer

**Answer:** B
**Explanation:** The Data Link Layer uses CRC (Cyclic Redundancy Check) in the frame trailer to detect errors during transmission.

---

**Q19.** Which layer converts data into standard formats like ASCII or JPEG?
- A) Application Layer
- B) Session Layer
- C) Presentation Layer
- D) Transport Layer

**Answer:** C
**Explanation:** The Presentation Layer handles data translation, encoding, and format conversion (ASCII, JPEG, MPEG, etc.).

---

**Q20.** What is the main function of the Transport Layer?
- A) Routing
- B) Physical addressing
- C) End-to-end reliable delivery
- D) Data encryption

**Answer:** C
**Explanation:** The Transport Layer ensures complete, reliable end-to-end data delivery with flow control, error control, and sequencing.

---

## Advanced Level (Questions 21-30)

**Q21.** In the OSI model, which layer communication is called "peer-to-peer"?
- A) Only Application layer
- B) Only Physical layer
- C) Each layer communicates with its corresponding layer on the receiving device
- D) Only Transport layer

**Answer:** C
**Explanation:** Each layer on the sender communicates logically with the same layer on the receiver (peer-to-peer communication), even though data physically flows vertically through layers.

---

**Q22.** Why does each layer add a header?
- A) To make data larger
- B) To provide layer-specific control information
- C) For encryption purposes
- D) To slow down transmission

**Answer:** B
**Explanation:** Each layer adds a header containing control information it needs (addresses, sequence numbers, error checking, etc.) to perform its functions.

---

**Q23.** Which statement about TCP is TRUE?
- A) Connectionless and unreliable
- B) Connection-oriented and reliable
- C) Connectionless and reliable
- D) Connection-oriented and unreliable

**Answer:** B
**Explanation:** TCP is connection-oriented (uses 3-way handshake) and reliable (guarantees delivery, ordering, and error recovery).

---

**Q24.** When data travels up the layers at the receiver, what happens?
- A) Headers are added
- B) Headers are removed (decapsulation)
- C) Data is encrypted
- D) Data is compressed

**Answer:** B
**Explanation:** At the receiver, data travels up the layers and each layer removes the header added by its peer layer (decapsulation).

---

**Q25.** Which layer would you troubleshoot if a website URL doesn't resolve to an IP address?
- A) Network Layer
- B) Transport Layer
- C) Application Layer
- D) Physical Layer

**Answer:** C
**Explanation:** DNS resolution happens at the Application Layer. If URLs don't resolve to IPs, it's a DNS (Application Layer) issue.

---

**Q26.** What is the relationship between OSI model and real-world networking?
- A) All networks strictly follow OSI model
- B) Real networks use TCP/IP model, OSI is a reference
- C) OSI model is outdated and useless
- D) OSI model is only for wireless networks

**Answer:** B
**Explanation:** Real-world networks use the TCP/IP model (4 layers). The OSI model is a conceptual reference for understanding and troubleshooting.

---

**Q27.** Flow control is primarily a function of which layer?
- A) Network Layer
- B) Transport Layer
- C) Session Layer
- D) Data Link Layer

**Answer:** B
**Explanation:** While both Transport and Data Link layers perform flow control, it's primarily a Transport Layer function (TCP sliding window mechanism).

---

**Q28.** Which layer determines the best physical path for data?
- A) Physical Layer
- B) Data Link Layer
- C) Network Layer
- D) Transport Layer

**Answer:** C
**Explanation:** The Network Layer handles routing, which determines the best logical path across multiple networks from source to destination.

---

**Q29.** SSL/TLS encryption in HTTPS happens at which layer(s)?
- A) Only Presentation Layer
- B) Only Application Layer
- C) Both Presentation and Application Layer
- D) Transport Layer

**Answer:** C
**Explanation:** SSL/TLS can be viewed as operating at both Presentation Layer (encryption) and Application Layer (HTTPS protocol implementation).

---

**Q30.** If two computers can't communicate because they use different email protocols, which layer is the problem?
- A) Transport Layer
- B) Session Layer
- C) Presentation Layer
- D) Application Layer

**Answer:** D
**Explanation:** Email protocols (SMTP, POP3, IMAP) operate at the Application Layer. Incompatibility at this layer prevents proper communication.

---

## Score Interpretation

- **27-30 Correct:** Excellent! Strong OSI model understanding. Move to next topic.
- **20-26 Correct:** Good. Review weak areas before proceeding.
- **15-19 Correct:** Fair. Re-read notes and focus on misunderstood concepts.
- **Below 15:** Review the entire topic thoroughly before moving forward.

---

## Study Tips for OSI Model

1. **Memorize the order** using mnemonics
2. **Know the data unit** for each layer
3. **Understand what each layer DOES** (not just its name)
4. **Learn key protocols** for each layer
5. **Know which devices** operate at which layers
6. **Practice encapsulation** with real examples
7. **Relate to TCP/IP model** for practical understanding
