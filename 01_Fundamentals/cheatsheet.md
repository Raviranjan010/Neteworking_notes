# 01. Networking Fundamentals — One-Page Cheatsheet

> **Quick revision card for exams and last-minute interview refresh.**

---

## ⚡ Master Formulas at a Glance

| Metric | Formula | What It Depends On | Key Units |
|---|---|---|:---:|
| **Transmission Delay ($T_t$)** | $$T_t = \frac{L}{R}$$ | Packet Length ($L$), Bandwidth ($R$) | Seconds / ms |
| **Propagation Delay ($T_p$)** | $$T_p = \frac{d}{v}$$ | Distance ($d$), Signal Speed in Cable ($v \approx 2 \times 10^8\text{ m/s}$) | Seconds / ms |
| **Total Nodal Delay** | $$D = T_t + T_p + T_q + T_{\text{proc}}$$ | All four components | Seconds / ms |
| **Store-and-Forward Delay** | $$T = (k + N - 1) \frac{L}{R} + N \cdot T_p$$ | $k$ packets, $N$ identical hops of rate $R$ | Seconds |
| **Bandwidth-Delay Product** | $$\text{BDP} = R \times \text{RTT}$$ | Link Bandwidth ($R$) and Round-Trip Time | Bits or Bytes |
| **Mesh Topology Duplex Links** | $$N_{\text{links}} = \frac{n(n-1)}{2}$$ | Node count ($n$) | Cables |
| **Mesh Ports per Node** | $$P = n - 1$$ | Node count ($n$) | Hardware Ports |
| **Goodput** | $$\text{Goodput} = \text{Throughput} \times \frac{\text{Payload}}{\text{Total Wire Packet}}$$ | Protocol Header Overhead | Mbps / Gbps |

---

## 🗺️ Topologies Quick Summary

| Topology | Key Strength | Fatal Weakness | Single Point of Failure? | Cable Count |
|---|---|---|:---:|:---:|
| **Star** | Easy to scale, fault isolation | Central switch failure kills LAN | Yes (Central Switch) | $n$ |
| **Bus** | Low initial cable cost | Single cut or missing terminator kills all | Yes (Backbone Cable) | 1 continuous + taps |
| **Ring** | Deterministic access | Single break stops token circulation | Yes (Single Ring) | $n$ |
| **Full Mesh** | Extreme fault tolerance | Exponential cable explosion $O(n^2)$ | **No** | $\frac{n(n-1)}{2}$ |
| **Tree** | Hierarchical enterprise growth | Root switch failure breaks branches | Yes (Root Switch) | Tiered links |

---

## 🔄 Transmission Modes

- **Simplex:** One-way only (e.g., FM Radio, Keyboard $\rightarrow$ PC).
- **Half-Duplex:** Two-way, but alternating (e.g., Walkie-Talkies, 802.11 Wi-Fi, 10BASE2 coaxial).
- **Full-Duplex:** Two-way simultaneous (e.g., Switched Cat6 Ethernet, Mobile telephone calls).

---

## 🔀 Switching at a Glance

| Feature | Circuit Switching | Datagram Packet Switching |
|---|---|---|
| **Path Reservation** | Dedicated physical circuit before data transfer | No reservation; routed hop-by-hop |
| **Bandwidth** | Strictly reserved (wasted during silence) | Dynamic statistical multiplexing |
| **Delay Behavior** | High setup delay, zero queuing delay | Zero setup delay, variable queuing delay |
| **Delivery Order** | Guaranteed in-order | Can arrive out-of-order |
| **Best For** | Constant-bitrate voice calls | Bursty Internet data traffic |

---

## 🧠 Memory Tricks & Mnemonics

- **Network Scales:** *"Please Let Managers Work"* $\rightarrow$ **P**AN, **L**AN, **M**AN, **W**AN.
- **Protocol 3 Pillars:** **S-S-T** $\rightarrow$ **S**yntax (structure), **S**emantics (meaning), **T**iming (speed).
- **Delay Trap Rule:**
  - Need to push bits faster? Upgrade **Bandwidth** (reduces $T_t$).
  - Need signals to arrive faster over distance? Move closer or beat the **Speed of Light** (reduces $T_p$).

---

## 🎯 Top 5 Rapid-Fire Interview Answers

1. **Why does packet switching beat circuit switching?**  
   *Because Internet traffic is bursty; statistical multiplexing shares idle capacity across hundreds of users.*
2. **What is Bandwidth-Delay Product (BDP)?**  
   *The volume of bits in flight filling the cable pipe ($R \times \text{RTT}$); determines optimal TCP window size.*
3. **Difference between throughput and goodput?**  
   *Throughput is all bits on the wire; goodput is only useful application payload delivered without headers or drops.*
4. **How many links in a 10-node mesh?**  
   *$$\frac{10 \times 9}{2} = 45\text{ links}$$, and 9 ports per device.*
5. **What is Jitter?**  
   *The variance in packet arrival latency; smoothed out by receiver jitter buffers in VoIP and streaming.*
