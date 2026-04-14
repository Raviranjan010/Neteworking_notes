# TCP/IP Model - MCQs

## Beginner Level (Questions 1-10)

**Q1.** How many layers does the TCP/IP model have?
- A) 3
- B) 4
- C) 5
- D) 7

**Answer:** B
**Explanation:** The TCP/IP model has 4 layers: Application, Transport, Internet, and Network Access.

---

**Q2.** Which layer of TCP/IP model combines OSI layers 5, 6, and 7?
- A) Transport Layer
- B) Internet Layer
- C) Application Layer
- D) Network Access Layer

**Answer:** C
**Explanation:** The TCP/IP Application Layer combines the functions of OSI's Session, Presentation, and Application layers.

---

**Q3.** IP (Internet Protocol) operates at which TCP/IP layer?
- A) Application Layer
- B) Transport Layer
- C) Internet Layer
- D) Network Access Layer

**Answer:** C
**Explanation:** IP operates at the Internet Layer (Layer 2) of TCP/IP model, handling logical addressing and routing.

---

**Q4.** Which protocol is connection-oriented and reliable?
- A) UDP
- B) IP
- C) TCP
- D) HTTP

**Answer:** C
**Explanation:** TCP (Transmission Control Protocol) is connection-oriented (uses handshake) and reliable (guarantees delivery).

---

**Q5.** HTTP and FTP are protocols of which layer?
- A) Internet Layer
- B) Transport Layer
- C) Application Layer
- D) Network Access Layer

**Answer:** C
**Explanation:** HTTP, FTP, SMTP, DNS, and other user-facing protocols operate at the Application Layer.

---

**Q6.** What does TCP stand for?
- A) Transmission Control Protocol
- B) Transfer Communication Protocol
- C) Total Control Protocol
- D) Transmission Communication Process

**Answer:** A
**Explanation:** TCP stands for Transmission Control Protocol, the reliable transport protocol in TCP/IP suite.

---

**Q7.** Which layer handles MAC addresses in TCP/IP model?
- A) Application Layer
- B) Transport Layer
- C) Internet Layer
- D) Network Access Layer

**Answer:** D
**Explanation:** The Network Access Layer handles physical addressing (MAC addresses) and frame transmission.

---

**Q8.** UDP is faster than TCP because:
- A) It has more features
- B) It's connectionless and has less overhead
- C) It uses encryption
- D) It guarantees delivery

**Answer:** B
**Explanation:** UDP is connectionless (no handshake) and has minimal overhead, making it faster but unreliable.

---

**Q9.** Which organization developed the TCP/IP model?
- A) ISO
- B) IEEE
- C) U.S. Department of Defense (DARPA)
- D) Microsoft

**Answer:** C
**Explanation:** TCP/IP was developed by U.S. Department of Defense through DARPA in the 1960s.

---

**Q10.** DNS operates at which layer?
- A) Internet Layer
- B) Transport Layer
- C) Application Layer
- D) Network Access Layer

**Answer:** C
**Explanation:** DNS (Domain Name System) is an Application Layer protocol that resolves domain names to IP addresses.

---

## Intermediate Level (Questions 11-20)

**Q11.** Which statement about TCP/IP model is TRUE?
- A) It's only theoretical
- B) It's used by the Internet
- C) It has 7 layers
- D) It was developed after OSI model

**Answer:** B
**Explanation:** TCP/IP is the practical model actually used by the Internet and all modern networks.

---

**Q12.** ICMP (ping) operates at which layer?
- A) Application Layer
- B) Transport Layer
- C) Internet Layer
- D) Network Access Layer

**Answer:** C
**Explanation:** ICMP (Internet Control Message Protocol) operates at the Internet Layer for error reporting and diagnostics.

---

**Q13.** What is the data unit at the Internet Layer?
- A) Frame
- B) Segment
- C) Packet
- D) Bit

**Answer:** C
**Explanation:** At the Internet Layer, the data unit is called a packet (or datagram for IP).

---

**Q14.** Which protocol would you use for video streaming?
- A) TCP
- B) UDP
- C) IP
- D) HTTP

**Answer:** B
**Explanation:** UDP is preferred for video streaming because speed is more important than reliability. Lost frames are acceptable for real-time video.

---

**Q15.** ARP (Address Resolution Protocol) maps:
- A) Domain names to IP addresses
- B) IP addresses to MAC addresses
- C) MAC addresses to IP addresses
- D) Port numbers to applications

**Answer:** B
**Explanation:** ARP resolves IP addresses to MAC addresses for local network communication.

---

**Q16.** Which is NOT a function of the Transport Layer?
- A) Flow control
- B) Routing
- C) Error control
- D) Port addressing

**Answer:** B
**Explanation:** Routing is a function of the Internet Layer, not Transport Layer. Transport layer handles end-to-end delivery.

---

**Q17.** Why is TCP called "connection-oriented"?
- A) It connects cables
- B) It establishes a connection before data transfer
- C) It only works with wired connections
- D) It connects multiple computers

**Answer:** B
**Explanation:** TCP establishes a connection using 3-way handshake before any data is transferred, ensuring reliable communication.

---

**Q18.** Which TCP/IP layer corresponds to OSI's Network Layer?
- A) Application Layer
- B) Transport Layer
- C) Internet Layer
- D) Network Access Layer

**Answer:** C
**Explanation:** TCP/IP's Internet Layer corresponds to OSI's Network Layer (Layer 3), both handle routing and logical addressing.

---

**Q19.** Port numbers are used at which layer?
- A) Application Layer
- B) Transport Layer
- C) Internet Layer
- D) Network Access Layer

**Answer:** B
**Explanation:** Port numbers are used at the Transport Layer to identify specific applications or services.

---

**Q20.** What makes TCP reliable?
- A) It's faster
- B) Acknowledgments, retransmission, and sequencing
- C) It uses encryption
- D) It has fewer headers

**Answer:** B
**Explanation:** TCP ensures reliability through acknowledgments (ACKs), retransmission of lost packets, and sequence numbers for ordering.

---

## Advanced Level (Questions 21-30)

**Q21.** Why did TCP/IP succeed over OSI model?
- A) OSI was too expensive
- B) TCP/IP was implemented first and proved to work
- C) OSI had too few layers
- D) TCP/IP was developed by ISO

**Answer:** B
**Explanation:** TCP/IP was implemented before OSI was finalized, proved to work at scale, and became the foundation of the Internet.

---

**Q22.** Which statement about IP is TRUE?
- A) IP guarantees delivery
- B) IP is connection-oriented
- C) IP provides best-effort delivery
- D) IP handles port numbers

**Answer:** C
**Explanation:** IP provides "best-effort" delivery - it tries to deliver packets but doesn't guarantee success. Reliability is TCP's job.

---

**Q23.** In TCP/IP model, encryption typically happens at:
- A) Network Access Layer
- B) Internet Layer
- C) Transport or Application Layer
- D) Physical layer only

**Answer:** C
**Explanation:** In TCP/IP, encryption can happen at Transport layer (TLS) or Application layer (HTTPS, SSH), unlike OSI which has dedicated Presentation layer.

---

**Q24.** Which protocol suite does the Internet actually use?
- A) OSI model
- B) TCP/IP model
- C) Both equally
- D) Neither

**Answer:** B
**Explanation:** The Internet uses TCP/IP model. OSI is only a theoretical reference model for learning.

---

**Q25.** What is a socket in TCP/IP?
- A) Physical connector
- B) IP address + Port number combination
- C) Type of cable
- D) Network device

**Answer:** B
**Explanation:** A socket is the combination of IP address and port number (e.g., 192.168.1.10:80) that uniquely identifies a connection endpoint.

---

**Q26.** Which layer would handle fragmentation of large packets?
- A) Application Layer
- B) Transport Layer
- C) Internet Layer
- D) Network Access Layer

**Answer:** C
**Explanation:** The Internet Layer (IP) handles fragmentation when packets are too large for the underlying network's MTU.

---

**Q27.** Why is UDP called "connectionless"?
- A) It doesn't use cables
- B) It sends data without establishing connection first
- C) It can't connect to Internet
- D) It only works locally

**Answer:** B
**Explanation:** UDP sends datagrams without establishing a connection first (no handshake), making it faster but unreliable.

---

**Q28.** Which application would prefer TCP over UDP?
- A) Live video streaming
- B) Online gaming
- C) Email transmission
- D) VoIP calls

**Answer:** C
**Explanation:** Email requires reliable, complete delivery (TCP). Lost emails are unacceptable, unlike video/audio where some loss is tolerable.

---

**Q29.** The "best-effort delivery" concept means:
- A) Guaranteed delivery
- B) No attempt to deliver
- C) Try to deliver but no guarantees
- D) Deliver only important packets

**Answer:** C
**Explanation:** Best-effort means the network tries to deliver packets but doesn't guarantee success. IP is a best-effort protocol.

---

**Q30.** Which layer in TCP/IP is responsible for choosing the best path?
- A) Application Layer
- B) Transport Layer
- C) Internet Layer
- D) Network Access Layer

**Answer:** C
**Explanation:** The Internet Layer handles routing, which determines the best path for packets across multiple networks.

---

## Score Interpretation

- **27-30 Correct:** Excellent! Strong TCP/IP understanding. Proceed to next topic.
- **20-26 Correct:** Good. Review weak areas before moving forward.
- **15-19 Correct:** Fair. Re-read notes and focus on concepts you missed.
- **Below 15:** Review the entire topic before proceeding.
