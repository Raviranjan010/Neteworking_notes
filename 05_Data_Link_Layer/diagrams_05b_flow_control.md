# 05b. Flow Control & ARQ — Visual Diagram Suite

> **13 High-Yield Architectural and Timeline Sequence Diagrams illustrating normal flows, failure modes, lost frame/ACK recoveries, sliding window mechanics, and window overlap proofs.**

---

## 1. Stop-and-Wait ARQ: Normal Error-Free Flow

```mermaid
sequenceDiagram
    autonumber
    participant S as Sender
    participant R as Receiver

    Note over S: Prepare Frame 0
    S->>R: Frame 0 (Data)
    Note over S: Start Timer (RTT + margin)
    Note over R: CRC Valid -> Accept F0
    R-->>S: ACK 1 (Expecting Frame 1)
    Note over S: Stop Timer
    Note over S: Prepare Frame 1
    S->>R: Frame 1 (Data)
    Note over S: Start Timer
    Note over R: CRC Valid -> Accept F1
    R-->>S: ACK 0 (Expecting Frame 0)
    Note over S: Stop Timer
```

> **What to notice:**
> - Alternating sequence numbers $0$ and $1$ are sufficient for Stop-and-Wait.
> - The transmitter must remain completely idle for the entire round-trip propagation time ($2T_p$) between each frame.

---

## 2. Stop-and-Wait ARQ: Lost Data Frame Scenario

```mermaid
sequenceDiagram
    autonumber
    participant S as Sender
    participant R as Receiver

    S->>R: Frame 0
    Note over S: Start Retransmission Timer
    Note over R: Frame 0 Lost in Transit ❌
    Note over R: Receiver sits idle (unaware)
    Note over S: ⏱️ Timer Expires (Timeout)
    S->>R: Frame 0 (Retransmission)
    Note over S: Restart Timer
    Note over R: CRC Valid -> Accept Frame 0
    R-->>S: ACK 1 (Expecting Frame 1)
    Note over S: Stop Timer
```

> **What to notice:**
> - The receiver never sends a negative acknowledgment for an unreceived frame because it has no knowledge that a transmission occurred.
> - Recovery depends entirely on sender-side timer expiration.

---

## 3. Stop-and-Wait ARQ: Lost ACK Scenario

```mermaid
sequenceDiagram
    autonumber
    participant S as Sender
    participant R as Receiver

    S->>R: Frame 1
    Note over S: Start Timer
    Note over R: Frame 1 Received Safely
    R-->>S: ACK 0 (Lost in Transit ❌)
    Note over S: ⏱️ Timer Expires (Timeout)
    S->>R: Frame 1 (Duplicate Frame Sent)
    Note over R: Received Frame 1 again!
    Note over R: Duplicate detected via Seq No -> DISCARD payload
    R-->>S: ACK 0 (Re-send ACK 0)
    Note over S: ACK 0 Received -> Stop Timer
```

> **What to notice:**
> - The receiver must not deliver duplicate data to the network layer.
> - The receiver retransmits the acknowledgment to unblock the sender.

---

## 4. Stop-and-Wait ARQ: Delayed ACK / Premature Timeout

```mermaid
sequenceDiagram
    autonumber
    participant S as Sender
    participant R as Receiver

    S->>R: Frame 0
    Note over S: ⏱️ Timer too short -> Expires!
    S->>R: Frame 0 (Premature Retransmission)
    R-->>S: ACK 1 (Delayed Original ACK arrives)
    Note over S: Sender accepts ACK 1 -> Advances to Frame 1
    S->>R: Frame 1
    Note over R: Duplicate Frame 0 arrives -> DISCARD
    R-->>S: ACK 1 (Re-ACK 1)
    Note over R: Frame 1 arrives -> ACCEPT
    R-->>S: ACK 0 (ACK Frame 1)
```

> **What to notice:**
> - If timeout timers are set too aggressively, duplicate packets flood the link.
> - Sequence numbers prevent duplicate data from corrupting the stream.

---

## 5. Go-Back-N (GBN) ARQ: Normal Continuous Pipelined Flow ($W_s = 4$)

```mermaid
sequenceDiagram
    autonumber
    participant S as Sender (Ws = 4)
    participant R as Receiver (Wr = 1)

    Note over S: Window: [0, 1, 2, 3]
    S->>R: Frame 0
    S->>R: Frame 1
    S->>R: Frame 2
    S->>R: Frame 3
    Note over R: Receives F0 -> Slide to [1]
    R-->>S: ACK 1 (Expecting 1)
    Note over S: Window slides to [1, 2, 3, 4] -> Send F4
    S->>R: Frame 4
    Note over R: Receives F1 -> Slide to [2]
    R-->>S: ACK 2 (Expecting 2)
    Note over S: Window slides to [2, 3, 4, 5] -> Send F5
    S->>R: Frame 5
```

> **What to notice:**
> - The transmitter pipelines up to $W_s$ frames continuously without waiting for individual ACKs.
> - Receiver window $W_r = 1$ advances one frame at a time.

---

## 6. Go-Back-N (GBN) ARQ: Lost Frame & Cascading Discard

```mermaid
sequenceDiagram
    autonumber
    participant S as Sender (Ws = 4)
    participant R as Receiver (Wr = 1)

    S->>R: Frame 0 (Arrives OK)
    S->>R: Frame 1 (LOST in transit ❌)
    S->>R: Frame 2 (Arrives OK)
    S->>R: Frame 3 (Arrives OK)
    R-->>S: ACK 1 (Frame 0 confirmed)
    Note over R: Expecting 1, got 2 -> DISCARD Frame 2!
    R-->>S: ACK 1 (Re-send ACK 1)
    Note over R: Expecting 1, got 3 -> DISCARD Frame 3!
    R-->>S: ACK 1 (Re-send ACK 1)
    Note over S: ⏱️ Timer for Frame 1 EXPIRES!
    Note over S: Must "Go Back N": Retransmit 1, 2, 3
    S->>R: Frame 1 (Retransmit)
    S->>R: Frame 2 (Retransmit)
    S->>R: Frame 3 (Retransmit)
```

> **What to notice:**
> - Even though Frames 2 and 3 arrived completely undamaged, the receiver discarded them because $W_r = 1$.
> - All unacknowledged frames must be retransmitted, causing severe throughput loss on high-error links.

---

## 7. Go-Back-N (GBN) ARQ: Cumulative ACK Tolerance

```mermaid
sequenceDiagram
    autonumber
    participant S as Sender (Ws = 4)
    participant R as Receiver (Wr = 1)

    S->>R: Frame 0
    S->>R: Frame 1
    S->>R: Frame 2
    Note over R: F0 received -> Send ACK 1
    R-->>S: ACK 1 (LOST in transit ❌)
    Note over R: F1 received -> Send ACK 2
    R-->>S: ACK 2 (LOST in transit ❌)
    Note over R: F2 received -> Send ACK 3
    R-->>S: ACK 3 (Arrives safely!)
    Note over S: ACK 3 cumulatively confirms F0, F1, and F2!
    Note over S: Sender window advances by 3 full frames!
```

> **What to notice:**
> - Cumulative ACKs make GBN resilient to lost ACKs: as long as a later ACK arrives before timeout, earlier lost ACKs cause no retransmissions.

---

## 8. Selective Repeat (SR) ARQ: Normal Pipelined Flow ($W_s = 4, W_r = 4$)

```mermaid
sequenceDiagram
    autonumber
    participant S as Sender (Ws = 4)
    participant R as Receiver (Wr = 4)

    Note over S: Window: [0, 1, 2, 3]
    Note over R: Window: [0, 1, 2, 3]
    S->>R: Frame 0
    S->>R: Frame 1
    S->>R: Frame 2
    S->>R: Frame 3
    R-->>S: ACK 0 (Individual ACK)
    R-->>S: ACK 1 (Individual ACK)
    R-->>S: ACK 2 (Individual ACK)
    R-->>S: ACK 3 (Individual ACK)
    Note over S: Window slides to [4, 5, 6, 7]
    Note over R: Window slides to [4, 5, 6, 7]
```

> **What to notice:**
> - In Selective Repeat, acknowledgments are discrete/selective ($ACK_i$ or $SACK$).
> - Both sender and receiver maintain identical buffer capacities of $2^{k-1}$.

---

## 9. Selective Repeat (SR) ARQ: Single Frame Recovery via Out-of-Order Buffering

```mermaid
sequenceDiagram
    autonumber
    participant S as Sender (Ws = 4)
    participant R as Receiver (Wr = 4)

    S->>R: Frame 0 (Arrives OK)
    S->>R: Frame 1 (LOST in transit ❌)
    S->>R: Frame 2 (Arrives OK)
    S->>R: Frame 3 (Arrives OK)
    R-->>S: ACK 0
    Note over R: Buffer Frame 2 in slot 2
    R-->>S: ACK 2 (Selective ACK 2)
    Note over R: Buffer Frame 3 in slot 3
    R-->>S: ACK 3 (Selective ACK 3)
    Note over S: ⏱️ Timer for Frame 1 EXPIRES!
    Note over S: Retransmit ONLY Frame 1
    S->>R: Frame 1 (Retransmission)
    Note over R: Frame 1 arrives!
    Note over R: Release [F1, F2, F3] in-order to L3!
    R-->>S: ACK 1
    Note over R: Receiver window slides forward by 3!
```

> **What to notice:**
> - Frames 2 and 3 are never retransmitted!
> - Out-of-order frames are held in the receiver's window buffer until the missing frame arrives.

---

## 10. The GBN Overlapping Window Ambiguity Failure ($W_s = 2^k$)

```mermaid
sequenceDiagram
    autonumber
    participant S as Sender (Ws = 4, k = 2)
    participant R as Receiver (Wr = 1)

    Note over S,R: Catastrophic Case: Ws = 2^k = 4 with Modulo 4 Seq (0, 1, 2, 3)
    S->>R: Frame 0
    S->>R: Frame 1
    S->>R: Frame 2
    S->>R: Frame 3
    Note over R: All 4 frames received OK!
    Note over R: Receiver window slides to expect NEXT Frame 0!
    R-->>S: ACK 0 (All ACKs lost in transit ❌)
    Note over S: ⏱️ Timer expires for original Frame 0!
    S->>R: Frame 0 (Retransmit from Cycle 1)
    Note over R: Receiver sees Frame 0 arriving.
    Note over R: Receiver is waiting for Frame 0 of Cycle 2!
    Note over R: ❌ DISASTER: Old Frame 0 accepted as NEW Frame 0!
    Note over R: Undetected Duplicate Data delivered to user!
```

> **What to notice:**
> - When $W_s = 2^k$, the receiver cannot distinguish between an old retransmitted frame and a new frame from the next generation.
> - Setting $W_s \le 2^k - 1$ guarantees that the expected frame sequence number is never identical to the oldest pending unacknowledged frame.

---

## 11. The Selective Repeat Window Overlap Failure ($W_s > 2^{k-1}$)

```mermaid
sequenceDiagram
    autonumber
    participant S as Sender (Ws = 3, k = 2)
    participant R as Receiver (Wr = 3, k = 2)

    Note over S,R: Catastrophic Case: Ws = Wr = 3 > 2^(2-1) = 2 (Modulo 4: 0, 1, 2, 3)
    S->>R: Frame 0
    S->>R: Frame 1
    S->>R: Frame 2
    Note over R: Receives F0, F1, F2 OK!
    Note over R: Receiver window slides from [0, 1, 2] to [3, 0, 1]!
    R-->>S: ACKs 0, 1, 2 (All lost in transit ❌)
    Note over S: ⏱️ Timer expires for Frame 0!
    S->>R: Frame 0 (Retransmit from Generation 1)
    Note over R: Receiver checks current window: [3, 0, 1]
    Note over R: 0 is INSIDE the current window!
    Note over R: ❌ DISASTER: Old Frame 0 accepted as Frame 0 of Generation 2!
```

> **What to notice:**
> - In Selective Repeat, $W_s + W_r \le 2^k$ is mandatory. When $W_s = W_r$, the maximum allowable window size is strictly $2^{k-1}$.

---

## 12. Piggybacking Bidirectional Data Flow Timeline

```mermaid
sequenceDiagram
    autonumber
    participant NodeA as Node A
    participant NodeB as Node B

    Note over NodeA: Send Data A0 with ACK=None
    NodeA->>NodeB: Data Frame (Seq=0, ACK=None)
    Note over NodeB: B has return data to send!
    Note over NodeB: Embed ACK=1 into Data Frame B0
    NodeB->>NodeA: Data Frame (Seq=0, ACK=1)
    Note over NodeA: A receives B0 and confirms A0!
    Note over NodeA: A has no immediate data to send.
    Note over NodeA: Start Piggybacking Delayed ACK Timer ⏱️
    Note over NodeA: Timer expires without new data
    NodeA-->>NodeB: Standalone ACK (ACK=1)
```

> **What to notice:**
> - Piggybacking replaces standalone ACK frames with dual-purpose data frames, cutting link framing overhead by half.
> - A delayed ACK timer ensures that lone packets still receive timely confirmation if no return traffic exists.

---

## 13. Channel Utilization: Stop-and-Wait vs. Sliding Window

```mermaid
flowchart TD
    subgraph SW["Stop-and-Wait (a = 15, η = 3.2%)"]
        direction LR
        SW_Tx["[Frame 0] (8 ms)"] --- SW_Idle["[ IDLE / EMPTY PIPE: Waiting 240 ms for RTT ]"]
    end

    subgraph SWP["Sliding Window Pipelining (N = 31, η = 100%)"]
        direction LR
        SWP_F0["[F0]"] --- SWP_F1["[F1]"] --- SWP_F2["[F2]"] --- SWP_Dots["..."] --- SWP_F30["[F30]"]
    end

    classDef empty fill:#fee2e2,stroke:#ef4444,stroke-width:1px;
    classDef full fill:#dcfce7,stroke:#22c55e,stroke-width:1px;
    class SW_Idle empty;
    class SWP_F0,SWP_F1,SWP_F2,SWP_Dots,SWP_F30 full;
```

> **What to notice:**
> - When propagation delay dominates ($a \gg 1$), Stop-and-Wait leaves the transmission medium completely starved.
> - Pipelining saturates the pipe with $N = 1 + 2a$ frames, driving link efficiency to $100\%$.

---

## ⬅️ Navigation
- **Module Index:** [INDEX.md](../INDEX.md)
- **Conceptual Notes:** [notes_05b_flow_control.md](notes_05b_flow_control.md)
- **Solved Numericals:** [numericals_05b_flow_control.md](numericals_05b_flow_control.md)
- **Practice MCQs:** [mcqs.md](mcqs.md)
