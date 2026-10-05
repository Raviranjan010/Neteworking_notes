# Transport Layer - MCQs (30 Troubleshooting & Scenario-Based)

## Beginner Level (Questions 1-10)

**Q1.** What is the main function of the Transport Layer?
- A) Routing packets between networks
- B) End-to-end communication between applications
- C) Physical transmission of bits
- D) Data encryption

**Answer:** B
**Explanation:** Transport Layer provides end-to-end communication services between applications on different hosts, using port numbers to identify specific applications.

---

**Q2.** How many bits are in a port number?
- A) 8 bits
- B) 16 bits
- C) 32 bits
- D) 64 bits

**Answer:** B
**Explanation:** Port numbers are 16-bit values, ranging from 0 to 65535 (2^16 - 1).

---

**Q3.** Which port range is considered "Well-Known Ports"?
- A) 0-1023
- B) 1024-49151
- C) 49152-65535
- D) 0-255

**Answer:** A
**Explanation:** Well-known ports (0-1023) are reserved for system/privileged services like HTTP (80), FTP (21), SSH (22).

---

**Q4.** Which protocol is connection-oriented?
- A) UDP
- B) IP
- C) TCP
- D) ICMP

**Answer:** C
**Explanation:** TCP is connection-oriented, requiring a 3-way handshake before data transfer. UDP is connectionless.

---

**Q5.** What does TCP stand for?
- A) Transfer Control Protocol
- B) Transmission Control Protocol
- C) Total Communication Protocol
- D) Terminal Control Protocol

**Answer:** B
**Explanation:** TCP stands for Transmission Control Protocol, the reliable transport protocol.

---

**Q6.** How large is a UDP header?
- A) 8 bytes
- B) 20 bytes
- C) 32 bytes
- D) 64 bytes

**Answer:** A
**Explanation:** UDP header is only 8 bytes (Source Port, Dest Port, Length, Checksum - 2 bytes each), making it very lightweight.

---

**Q7.** Which flag initiates a TCP connection?
- A) ACK
- B) FIN
- C) SYN
- D) RST

**Answer:** C
**Explanation:** SYN (Synchronize) flag is set in the first packet of TCP 3-way handshake to initiate connection.

---

**Q8.** What port does HTTP use?
- A) 21
- B) 22
- C) 80
- D) 443

**Answer:** C
**Explanation:** HTTP uses port 80. HTTPS (secure) uses port 443.

---

**Q9.** What is a socket?
- A) Physical network connector
- B) IP address + Port number combination
- C) Type of cable
- D) Router interface

**Answer:** B
**Explanation:** A socket uniquely identifies a connection endpoint by combining IP address and port number (e.g., 192.168.1.10:80).

---

**Q10.** Which provides reliable delivery?
- A) UDP
- B) IP
- C) TCP
- D) Ethernet

**Answer:** C
**Explanation:** TCP guarantees reliable, ordered delivery with acknowledgments, retransmission, and error checking.

---

## Intermediate Level (Questions 11-20)

**Q11.** What is the purpose of TCP sliding window?
- A) Encryption
- B) Flow control
- C) Routing
- D) Error detection

**Answer:** B
**Explanation:** Sliding window is TCP's flow control mechanism, allowing receiver to control how much data sender can transmit before waiting for acknowledgment.

---

**Q12.** OUTPUT QUESTION: You run `netstat -an` and see: `TCP 192.168.1.10:54321 → 93.184.216.34:80 ESTABLISHED`. What does this mean?
- A) Connection attempt failed
- B) Active TCP connection between browser and web server
- C) UDP connection in progress
- D) Port scanning detected

**Answer:** B
**Explanation:** ESTABLISHED state means TCP 3-way handshake completed successfully. Port 54321 (ephemeral) is browser, port 80 is web server. Active data transfer can occur.

---

**Q13.** Why does DNS primarily use UDP instead of TCP?
- A) DNS needs reliability
- B) UDP is faster for simple queries
- C) DNS can't work with TCP
- D) UDP has better security

**Answer:** B
**Explanation:** DNS queries are simple request-response. UDP's speed advantage outweighs reliability needs. If response lost, client simply retries. TCP used only for zone transfers.

---

**Q14.** What happens when TCP receives duplicate ACKs?
- A) Connection terminated
- B) Fast retransmission triggered
- C) Window size doubled
- D) SYN sent again

**Answer:** B
**Explanation:** 3 duplicate ACKs indicate packet loss. TCP triggers fast retransmission without waiting for timeout, improving performance.

---

**Q15.** OUTPUT QUESTION: `tcpdump` shows: `IP 192.168.1.10.54321 > 93.184.216.34.80: Flags [S]`. What is this?
- A) Data transfer
- B) TCP SYN packet (connection initiation)
- C) Connection termination
- D) UDP packet

**Answer:** B
**Explanation:** Flags [S] indicates SYN flag set. This is the first packet of TCP 3-way handshake initiating connection to web server port 80.

---

**Q16.** What is TCP congestion control trying to prevent?
- A) Too many connections
- B) Network overload from too much data
- C) Port exhaustion
- D) Firewall issues

**Answer:** B
**Explanation:** Congestion control prevents senders from overwhelming network capacity, which causes packet loss and reduced throughput for everyone.

---

**Q17.** Which state indicates TCP connection is closing?
- A) ESTABLISHED
- B) LISTEN
- C) TIME_WAIT
- D) SYN_SENT

**Answer:** C
**Explanation:** TIME_WAIT occurs after connection closure, waiting to ensure all packets cleared. Prevents old packets from interfering with new connections.

---

**Q18.** Why is UDP preferred for video streaming?
- A) It guarantees delivery
- B) It's faster and lost frames are acceptable
- C) It has better quality
- D) It's more secure

**Answer:** B
**Explanation:** Video streaming prioritizes low latency over reliability. A lost frame causes minor glitch, but waiting for retransmission causes buffering. Real-time > perfect.

---

**Q19.** OUTPUT QUESTION: `netstat` shows many connections in SYN_RECV state. What might be happening?
- A) Normal operation
- B) Possible SYN flood attack
- C) DNS resolution
- D) File transfer

**Answer:** B
**Explanation:** Many SYN_RECV (half-open) connections indicate possible SYN flood attack. Attacker sends SYNs but never completes handshake, exhausting server resources.

---

**Q20.** What is the TCP sequence number used for?
- A) Encryption
- B) Tracking byte order and detecting duplicates
- C) Port identification
- D) Error correction

**Answer:** B
**Explanation:** Sequence numbers track each byte in the stream, ensuring ordered delivery, detecting duplicates, and enabling acknowledgment of received data.

---

## Advanced Level (Questions 21-30) - Troubleshooting & Scenarios

**Q21.** TROUBLESHOOT: User reports "Connection refused" when accessing web server. Most likely cause?
- A) Wrong IP address
- B) Web service not running on port 80
- C) Network cable unplugged
- D) DNS failure

**Answer:** B
**Explanation:** "Connection refused" means TCP SYN reached destination host, but no service listening on that port. RST packet sent back. Check if service is running: `netstat -an | grep :80`

---

**Q22.** SCENARIO: Web server has 10,000 connections in TIME_WAIT state. Impact?
- A) No impact, normal operation
- B) Port exhaustion, can't create new connections
- C) Increased security
- D) Faster performance

**Answer:** B
**Explanation:** TIME_WAIT connections still hold port resources. Too many can exhaust ephemeral ports, preventing new outbound connections. Solution: Tune TIME_WAIT duration or increase port range.

---

**Q23.** TROUBLESHOOT: Application slow but no packet loss. TCP window size = 0. What's the issue?
- A) Network congestion
- B) Receiver buffer full, sender blocked
- C) Firewall blocking
- D) DNS slow

**Answer:** B
**Explanation:** Window size 0 means receiver's buffer is full. Sender must wait until receiver processes data and advertises larger window. This is flow control working correctly, but indicates receiver bottleneck.

---

**Q24.** INTERVIEW: Why does TCP use 3-way handshake instead of 2-way?
- A) It's more secure
- B) Prevents old duplicate connections from causing confusion
- C) Required by protocol standard
- D) Allows encryption setup

**Answer:** B
**Explanation:** 3-way handshake prevents old duplicate SYN packets from establishing unintended connections. Both sides synchronize sequence numbers and confirm bidirectional communication works.

---

**Q25.** SCENARIO: Two applications on same host need to communicate with same server:port. How is this possible?
- A) Impossible, port conflict
- B) Different source (ephemeral) ports
- C) Different protocols
- D) Load balancing

**Answer:** B
**Explanation:** Each connection identified by 4-tuple: (Src IP, Src Port, Dst IP, Dst Port). Different ephemeral source ports allow multiple connections to same destination. Example: App1 uses :54321, App2 uses :54322, both to server:80.

---

**Q26.** TROUBLESHOOT: Intermittent connectivity, works after waiting. TCP retransmissions increasing. Cause?
- A) Port exhaustion
- B) Network congestion causing packet loss
- C) DNS issues
- D) Wrong subnet mask

**Answer:** B
**Explanation:** Increasing retransmissions indicate packet loss, typically from congestion. TCP's congestion control reduces window size, causing slowdown. Wait period allows network to clear. Use `tcpdump` to confirm retransmissions.

---

**Q27.** OUTPUT QUESTION: Wireshark shows: `TCP 192.168.1.10:54321 → 93.184.216.34:80 [FIN, ACK]`. What's happening?
- A) Connection starting
- B) Connection gracefully terminating
- C) Connection aborted
- D) Data transfer

**Answer:** B
**Explanation:** FIN flag indicates sender has no more data to send. This is graceful connection termination (4-way handshake). ACK acknowledges any pending data.

---

**Q28.** SCENARIO: Real-time gaming application experiencing lag. Currently using TCP. Solution?
- A) Increase TCP window size
- B) Switch to UDP
- C) Add more servers
- D) Compress data

**Answer:** B
**Explanation:** TCP's reliability mechanisms (retransmission, ordering) introduce latency unacceptable for real-time gaming. UDP provides lower latency, and game can implement custom reliability for critical data only.

---

**Q29.** TROUBLESHOOT: Server can accept connections but clients timeout. SYN packets leaving client, never reaching server. Cause?
- A) Server overloaded
- B) Firewall blocking SYN packets
- C) Port already in use
- D) Wrong protocol

**Answer:** B
**Explanation:** If SYNs never reach server, they're being dropped en route. Most likely firewall rule blocking inbound connections to that port. Check firewall rules on server and intermediate devices.

---

**Q30.** INTERVIEW DEEP DIVE: Explain TCP's slow start algorithm.
- A) Starts with full window, reduces on loss
- B) Starts with small window (1 MSS), doubles each RTT until threshold
- C) Starts with random window size
- D) Always uses fixed window

**Answer:** B
**Explanation:** Slow start begins with 1 Maximum Segment Size (MSS). Each RTT, window doubles (exponential growth): 1→2→4→8→16... Continues until reaching slow start threshold or packet loss detected. Prevents overwhelming network with sudden large traffic.

---

## Score Interpretation

- **27-30:** Excellent! Interview-ready with strong troubleshooting skills
- **20-26:** Good. Practice more output-based analysis
- **15-19:** Fair. Review TCP handshake and troubleshooting methods
- **Below 15:** Re-study Transport Layer fundamentals

## Interview Preparation Tips

1. **Memorize common ports** - Always asked in interviews
2. **Understand TCP handshake deeply** - Draw it if needed
3. **Know troubleshooting commands** - netstat, tcpdump, Wireshark
4. **Practice reading outputs** - netstat states, tcpdump flags
5. **Understand when to use TCP vs UDP** - Real-world scenarios
6. **Be ready to debug** - Step-by-step methodology
