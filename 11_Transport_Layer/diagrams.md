# Transport Layer - Diagrams & Visual Guides

## 1. TCP 3-Way Handshake - Step-by-Step Packet Flow

```
SCENARIO: Web Browser (Client) connecting to Web Server

CLIENT (Browser)                          SERVER (Apache/Nginx)
192.168.1.10:54321                        93.184.216.34:80
State: CLOSED                             State: LISTEN
   │                                          │
   │  STEP 1: SYN                            │
   │  "I want to connect!"                   │
   │  ──────────────────────────────────────▶│
   │  TCP Header:                            │
   │  - SYN=1, ACK=0                         │
   │  - Seq=100 (random)                     │
   │  - Ack=N/A                              │
   │  State: SYN_SENT                        │ State: LISTEN
   │                                          │
   │                                          │ Server allocates resources
   │                                          │
   │  STEP 2: SYN-ACK                        │
   │  "I acknowledge and want to connect!"   │
   │  ◀──────────────────────────────────────│
   │  TCP Header:                            │
   │  - SYN=1, ACK=1                         │
   │  - Seq=300 (random)                     │
   │  - Ack=101 (Client Seq + 1)             │
   │  State: SYN_SENT                        │ State: SYN_RECEIVED
   │                                          │
   │  Client verifies ACK                    │
   │  Connection parameters set              │
   │                                          │
   │  STEP 3: ACK                            │
   │  "Connection established!"              │
   │  ──────────────────────────────────────▶│
   │  TCP Header:                            │
   │  - SYN=0, ACK=1                         │
   │  - Seq=101                              │
   │  - Ack=301 (Server Seq + 1)             │
   │  State: ESTABLISHED                     │ State: ESTABLISHED
   │                                          │
   │                                          │
   │  ✓ CONNECTION ESTABLISHED               │
   │  ✓ Data transfer can begin              │
   │  ✓ Both sides ready                     │
   │                                          │
   │  [HTTP REQUEST]                         │
   │  "GET / HTTP/1.1"                       │
   │  ──────────────────────────────────────▶│
   │  Seq=101, Ack=301                       │
   │  [HTTP RESPONSE]                        │
   │  "HTTP/1.1 200 OK"                      │
   │  ◀──────────────────────────────────────│
   │  Seq=301, Ack=[depends on data size]    │
```

---

## 2. TCP 4-Way Connection Termination

```
CLIENT                               SERVER
State: ESTABLISHED                   State: ESTABLISHED
   │                                     │
   │  STEP 1: FIN                        │
   │  "I'm done sending data"            │
   │  ──────────────────────────────────▶│
   │  FIN=1, ACK=1                       │
   │  State: FIN_WAIT_1                  │ State: CLOSE_WAIT
   │                                     │
   │  STEP 2: ACK                        │
   │  "Acknowledged"                     │
   │  ◀──────────────────────────────────│
   │  ACK=1                              │
   │  State: FIN_WAIT_2                  │ State: CLOSE_WAIT
   │                                     │
   │                                     │ Server finishes sending data
   │                                     │ (may take time)
   │                                     │
   │  STEP 3: FIN                        │
   │  "I'm also done"                    │
   │  ◀──────────────────────────────────│
   │  FIN=1, ACK=1                       │
   │  State: TIME_WAIT                   │ State: LAST_ACK
   │                                     │
   │  STEP 4: ACK                        │
   │  "Goodbye!"                         │
   │  ──────────────────────────────────▶│
   │  ACK=1                              │
   │  State: TIME_WAIT (waits 2*MSL)     │ State: CLOSED
   │                                     │
   │  Wait 2*MSL (Max Segment Lifetime)  │
   │  Ensures all packets cleared        │
   │                                     │
   │  State: CLOSED                      │
   │                                     │
   ✓ CONNECTION FULLY CLOSED
```

---

## 3. TCP vs UDP Header Comparison

```
TCP HEADER (20-60 bytes):
┌─────────────────────────────────────────────────┐
│     Source Port (16)    │  Destination Port (16)│
├─────────────────────────┴───────────────────────┤
│           Sequence Number (32)                   │
├─────────────────────────────────────────────────┤
│         Acknowledgment Number (32)               │
├──────┬──────────┬───────────────────────────────┤
│ Data │ Reserved │ Flags: URG ACK PSH RST SYN FIN│
│ Off  │          │                               │
├──────┴──────────┴───────────────────────────────┤
│           Window Size (16)                       │
│     (Flow control)                               │
├─────────────────────────────────────────────────┤
│           Checksum (16)                          │
├─────────────────────────────────────────────────┤
│     Urgent Pointer (if URG=1)                    │
├─────────────────────────────────────────────────┤
│     Options (variable)                           │
├─────────────────────────────────────────────────┤
│     DATA (Application payload)                   │
└─────────────────────────────────────────────────┘

UDP HEADER (Only 8 bytes!):
┌─────────────────────────────────────────────────┐
│     Source Port (16)    │  Destination Port (16)│
├─────────────────────────┴───────────────────────┤
│           Length (16)                            │
├─────────────────────────────────────────────────┤
│           Checksum (16)                          │
├─────────────────────────────────────────────────┤
│     DATA (Application payload)                   │
└─────────────────────────────────────────────────┘

SIZE DIFFERENCE:
TCP: 20 bytes minimum (up to 60 with options)
UDP: 8 bytes fixed
TCP is 2.5-7.5x larger!
```

---

## 4. Port Number Ranges Visualization

```
PORT NUMBER SPACE (0-65535):

┌──────────────────────────────────────────────────┐
│ 0                    │  1023                     │
│ WELL-KNOWN PORTS     │                           │
│ (System/Privileged)  │                           │
│                      │                           │
│ 20    → FTP Data     │                           │
│ 21    → FTP Control  │                           │
│ 22    → SSH          │                           │
│ 23    → Telnet       │                           │
│ 25    → SMTP         │                           │
│ 53    → DNS          │                           │
│ 80    → HTTP         │                           │
│ 443   → HTTPS        │                           │
└──────────────────────┴───────────────────────────┘
┌──────────────────────────────────────────────────┐
│ 1024                 │  49151                    │
│ REGISTERED PORTS     │                           │
│ (User Applications)  │                           │
│                      │                           │
│ 3306  → MySQL        │                           │
│ 3389  → RDP          │                           │
│ 5432  → PostgreSQL   │                           │
│ 8080  → HTTP Alt     │                           │
│ 8443  → HTTPS Alt    │                           │
└──────────────────────┴───────────────────────────┘
┌──────────────────────────────────────────────────┐
│ 49512                │  65535                    │
│ DYNAMIC/PRIVATE      │                           │
│ (Ephemeral Ports)    │                           │
│                      │                           │
│ Assigned by OS       │                           │
│ for client           │                           │
│ connections          │                           │
│                      │                           │
│ Example: 54321       │                           │
│          54322       │                           │
│          49152       │                           │
└──────────────────────┴───────────────────────────┘
```

---

## 5. Multiplexing & Demultiplexing

```
SENDER SIDE (Multiplexing):

[Browser App]     [Email App]     [FTP App]
Port: 54321       Port: 54322     Port: 54323
     │                │               │
     │ HTTP data      │ SMTP data     │ FTP data
     └────────┬───────┴───────┬───────┘
              │               │
              ▼               ▼
         ┌─────────────────────────┐
         │   TRANSPORT LAYER       │
         │   (Multiplexing)        │
         │                         │
         │ Adds port numbers       │
         │ Combines into segments  │
         └───────────┬─────────────┘
                     │
                     ▼
              [NETWORK LAYER]
              Single IP stream


RECEIVER SIDE (Demultiplexing):

              [NETWORK LAYER]
              Receives IP packets
                     │
                     ▼
         ┌─────────────────────────┐
         │   TRANSPORT LAYER       │
         │   (Demultiplexing)      │
         │                         │
         │ Reads port numbers      │
         │ Sorts to correct apps   │
         └───────┬───────┬─────────┘
                 │       │         │
        Port 80  │  Port 25 │ Port 21
                 │       │         │
                 ▼       ▼         ▼
            [Web Server] [Mail] [FTP Srv]
            Process HTTP Process SMTP Process FTP
```

---

## 6. TCP Sliding Window - Flow Control

```
SCENARIO: Receiver has buffer size of 3000 bytes

TIME 1: Initial Window Advertisement
┌─────────────────────────────────────┐
│ RECEIVER: "My window = 3000 bytes"  │
└─────────────────────────────────────┘
         ◀──────────────────
         
SENDER can transmit up to 3000 bytes:

[Segment 1][Segment 2][Segment 3]
 1000 bytes 1000 bytes 1000 bytes
 └─────────────────────────┘
      Window Full (3000/3000)
      Must wait for ACK

TIME 2: Receiver Acknowledges
┌─────────────────────────────────────┐
│ RECEIVER: "ACK 3001, Window = 2000" │
│ (Processed 1000 bytes)              │
└─────────────────────────────────────┘
         ◀──────────────────

Window slides forward:

           [Segment 4][Segment 5]
            1000 bytes 1000 bytes
            └────────────┘
         Window (2000/2000)

TIME 3: If receiver is slow
┌─────────────────────────────────────┐
│ RECEIVER: "ACK 3001, Window = 0"    │
│ (Buffer full, can't process more)   │
└─────────────────────────────────────┘
         ◀──────────────────

SENDER MUST STOP!

[No data sent - waiting]
      Window = 0
      Blocked until window opens

KEY POINT:
Receiver controls sender's speed!
Prevents overwhelming slow receivers
```

---

## 7. TCP Congestion Control Phases

```
CONGESTION WINDOW (cwnd) OVER TIME:

Window Size
    ↑
    │                                   
    │        SLOW START Phase
    │        (Exponential growth)
    │        1 → 2 → 4 → 8 → 16 → 32
    │       /
    │      /
    │     /
    │    /                    CONGESTION AVOIDANCE Phase
    │   /                     (Linear growth)
    │  /                      32 → 33 → 34 → 35 → 36
    │ /                      /
    │/                      /
    │──────────────────────/────────── (ssthresh threshold)
    │                     /
    │                    /
    │                   / ← Packet Loss Detected!
    │                  /  (cwnd cut in half)
    │                 /   
    │                /    FAST RECOVERY
    │               /     (Gradual increase)
    │              /
    │             /
    └──────────────────────────────────────────→ Time

PHASE EXPLANATION:

1. SLOW START:
   - Start: cwnd = 1 MSS
   - Each RTT: cwnd doubles
   - Fast growth to find available bandwidth
   - Continues until ssthresh or loss

2. CONGESTION AVOIDANCE:
   - Reached threshold
   - Linear growth (add 1 MSS per RTT)
   - Conservative probing
   - Continues until loss

3. CONGESTION DETECTION:
   - Packet loss (timeout or 3 dup ACKs)
   - ssthresh = cwnd / 2
   - cwnd reset to 1 MSS (timeout)
   - OR cwnd = ssthresh (fast recovery)
   - Return to slow start or recovery
```

---

## 8. Real-World Connection States

```
TCP CONNECTION LIFECYCLE:

SERVER SIDE:
CLOSED → LISTEN → SYN_RECV → ESTABLISHED → CLOSE_WAIT → LAST_ACK → CLOSED

CLIENT SIDE:
CLOSED → SYN_SENT → ESTABLISHED → FIN_WAIT_1 → FIN_WAIT_2 → TIME_WAIT → CLOSED

STATE DIAGRAM:

        CLIENT                          SERVER
          │                               │
      CLOSED                          CLOSED
          │                               │
          │  Application calls listen()   │
          │                               │
          │                          LISTEN
          │                               │
          │  Application calls connect()  │
          │                               │
      SYN_SENT                            │
          │                               │
          │        SYN (seq=x)            │
          │ ─────────────────────────────▶│
          │                               │
          │                          SYN_RECV
          │                               │
          │      SYN-ACK (seq=y, ack=x+1) │
          │ ◀─────────────────────────────│
          │                               │
          │        ACK (ack=y+1)          │
          │ ─────────────────────────────▶│
          │                               │
      ESTABLISHED                     ESTABLISHED
          │                               │
          │     [DATA TRANSFER]           │
          │     ◀────────────▶            │
          │                               │
          │  Application calls close()    │
          │                               │
      FIN_WAIT_1                          │
          │                               │
          │        FIN                    │
          │ ─────────────────────────────▶│
          │                               │
      FIN_WAIT_2                     CLOSE_WAIT
          │                               │
          │        ACK                    │
          │ ◀─────────────────────────────│
          │                               │
          │                          Application calls close()
          │                               │
          │        FIN                    │
          │ ◀─────────────────────────────│
          │                               │
      TIME_WAIT                      LAST_ACK
          │                               │
          │        ACK                    │
          │ ─────────────────────────────▶│
          │                               │
          │                          CLOSED
          │                               │
      (Wait 2*MSL)
          │
      CLOSED
```

---

## 9. Troubleshooting Flowchart

```
PROBLEM: Can't connect to service on port X
         │
         ▼
┌─────────────────────────────┐
│ Step 1: Is service running? │
│ netstat -an | grep :X       │
│ Should see LISTEN state     │
└────────┬────────────────────┘
         │
    ┌────┴────┐
   YES       NO → Start the service!
    │
    ▼
┌─────────────────────────────┐
│ Step 2: Can you reach host? │
│ ping server_ip              │
└────────┬────────────────────┘
         │
    ┌────┴────┐
   YES       NO → Network issue, check routing
    │
    ▼
┌─────────────────────────────┐
│ Step 3: Test port           │
│ telnet server_ip X          │
│ OR                          │
│ nc -zv server_ip X          │
└────────┬────────────────────┘
         │
    ┌────┴────┐
   Success   Fail → Firewall blocking?
    │
    ▼
┌─────────────────────────────┐
│ Step 4: Capture packets     │
│ tcpdump port X              │
│ OR                          │
│ Wireshark                   │
└────────┬────────────────────┘
         │
         ▼
    What do you see?
         │
    ┌────┼────────────┐
    │    │            │
    ▼    ▼            ▼
  SYN   SYN sent    SYN-ACK
  only  no reply    received
    │    │            │
    │    │            │
    ▼    ▼            ▼
Server  Firewall   Client issue
sending  dropping  or network
RST      packets   problem
```

---

## 10. Quick Reference Tables

### Table 1: Common Port Numbers

```
┌──────┬────────┬──────────────────────────────┐
│ Port │ Proto  │ Service                      │
├──────┼────────┼──────────────────────────────┤
│ 20   │ TCP    │ FTP (Data transfer)          │
│ 21   │ TCP    │ FTP (Control/connection)     │
│ 22   │ TCP    │ SSH (Secure Shell)           │
│ 23   │ TCP    │ Telnet (Unencrypted)         │
│ 25   │ TCP    │ SMTP (Send email)            │
│ 53   │ UDP    │ DNS (Queries)                │
│ 53   │ TCP    │ DNS (Zone transfers)         │
│ 67   │ UDP    │ DHCP (Server)                │
│ 68   │ UDP    │ DHCP (Client)                │
│ 80   │ TCP    │ HTTP (Web)                   │
│ 110  │ TCP    │ POP3 (Email retrieval)       │
│ 143  │ TCP    │ IMAP (Email retrieval)       │
│ 443  │ TCP    │ HTTPS (Secure web)           │
│ 993  │ TCP    │ IMAPS (Secure IMAP)          │
│ 995  │ TCP    │ POP3S (Secure POP3)          │
│ 3306 │ TCP    │ MySQL database               │
│ 3389 │ TCP    │ RDP (Remote Desktop)         │
│ 5432 │ TCP    │ PostgreSQL database          │
│ 8080 │ TCP    │ HTTP Alternate               │
└──────┴────────┴──────────────────────────────┘
```

### Table 2: TCP Flags

```
┌──────┬──────────┬─────────────────────────────┐
│ Flag │ Name     │ Purpose                     │
├──────┼──────────┼─────────────────────────────┤
│ SYN  │ Synchron │ Start connection            │
│      │ ize      │                             │
├──────┼──────────┼─────────────────────────────┤
│ ACK  │ Acknowl  │ Acknowledge receipt         │
│      | edge     │                             │
├──────┼──────────┼─────────────────────────────┤
│ FIN  │ Finish   │ Graceful connection end     │
├──────┼──────────┼─────────────────────────────┤
│ RST  │ Reset    │ Abort connection            │
├──────┼──────────┼─────────────────────────────┤
│ PSH  │ Push     │ Deliver immediately         │
├──────┼──────────┼─────────────────────────────┤
│ URG  │ Urgent   │ Priority data               │
└──────┴──────────┴─────────────────────────────┘
```

---

## Quick Reference Summary

```
┌──────────────────────────────────────────────────┐
│       TRANSPORT LAYER CHEATSHEET                 │
├──────────────────────────────────────────────────┤
│ TCP: Reliable, connection-oriented, ordered     │
│ UDP: Fast, connectionless, no guarantees        │
│                                                  │
│ Ports: 0-1023 (Well-known), 1024-49151 (Reg)    │
│        49152-65535 (Dynamic/Ephemeral)          │
│                                                  │
│ Common: 22=SSH, 53=DNS, 80=HTTP, 443=HTTPS     │
│                                                  │
│ TCP Handshake: SYN → SYN-ACK → ACK              │
│ TCP Termination: FIN → ACK → FIN → ACK          │
│                                                  │
│ Flow Control: Sliding window                    │
│ Congestion Control: Slow start → Avoidance      │
│                                                  │
│ Socket = IP Address + Port Number               │
│                                                  │
│ Troubleshoot: netstat, telnet, tcpdump, Wireshark│
└──────────────────────────────────────────────────┘
```
