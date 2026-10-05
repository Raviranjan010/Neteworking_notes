"""
Verification script for 01_Fundamentals numericals and MCQs.
Run this script to produce the ground-truth calculations for:
- Transmission delay (Tt = L / R)
- Propagation delay (Tp = d / v)
- End-to-end delay over N packet-switched store-and-forward links
- Bandwidth-Delay Product (BDP)
- Mesh topology link and port counts: n*(n-1)/2
- Packet switching vs Circuit switching transmission times
- Throughput and Goodput with protocol header overhead
"""

import math

def transmission_delay(L_bytes, R_bps):
    """L in bytes, R in bits/second. Returns delay in seconds."""
    L_bits = L_bytes * 8
    return L_bits / R_bps

def propagation_delay(d_meters, v_mps=2e8):
    """d in meters, v in m/s (default 2*10^8 m/s in copper/fiber). Returns delay in seconds."""
    return d_meters / v_mps

def mesh_links(n):
    """Number of duplex links in full mesh of n nodes."""
    return n * (n - 1) // 2

def mesh_ports_per_node(n):
    return n - 1

def bdp_bits(R_bps, rtt_seconds):
    """Bandwidth-Delay Product in bits."""
    return R_bps * rtt_seconds

def packet_switching_delay(num_packets, packet_size_bytes, link_rate_bps, num_links, prop_delay_per_link_sec):
    """
    Store-and-forward packet switching delay over N identical links:
    Time = (k + N - 1) * Tt + N * Tp
    """
    Tt = transmission_delay(packet_size_bytes, link_rate_bps)
    return (num_packets + num_links - 1) * Tt + num_links * prop_delay_per_link_sec

def circuit_switching_delay(setup_time_sec, message_size_bytes, link_rate_bps, prop_delay_total_sec):
    """
    Circuit switching:
    Time = T_setup + Tt + Tp
    """
    Tt = transmission_delay(message_size_bytes, link_rate_bps)
    return setup_time_sec + Tt + prop_delay_total_sec

def goodput(throughput_bps, payload_bytes, total_packet_bytes):
    """Goodput = Throughput * (Payload / Total Packet Size)"""
    return throughput_bps * (payload_bytes / total_packet_bytes)


def run_all_verifications():
    print("=" * 60)
    print("01_FUNDAMENTALS VERIFIED NUMERICALS")
    print("=" * 60)

    # Problem 1: Basic Tt and Tp
    # File of 2 MB sent over 10 Mbps link, distance 2000 km, v = 2*10^8 m/s
    p1_L = 2 * 1024 * 1024  # 2 MB in bytes = 2097152 bytes (or decimal 2*10^6 bytes? Let's verify both)
    # Using standard networking decimal 2 MB = 2 * 10^6 bytes
    p1_L_dec = 2_000_000
    p1_R = 10_000_000 # 10 Mbps
    p1_Tt = transmission_delay(p1_L_dec, p1_R)
    p1_d = 2_000_000 # 2000 km = 2*10^6 m
    p1_v = 2e8
    p1_Tp = propagation_delay(p1_d, p1_v)
    print(f"P1: Tt = {p1_Tt:.4f} s ({p1_Tt*1000:.1f} ms), Tp = {p1_Tp:.4f} s ({p1_Tp*1000:.1f} ms)")
    print(f"P1 Total Latency (ignoring queuing/proc) = {(p1_Tt + p1_Tp)*1000:.1f} ms")

    # Problem 2: Small packet voice sample
    # Voice packet 64 bytes over 1 Gbps link, d = 10 km
    p2_Tt = transmission_delay(64, 1_000_000_000)
    p2_Tp = propagation_delay(10_000, 2e8)
    print(f"P2 (VoIP): Tt = {p2_Tt*1e6:.2f} microseconds, Tp = {p2_Tp*1e6:.2f} microseconds")

    # Problem 3: Store-and-forward packet switching vs message switching
    # Message of 1,000,000 bytes (1 MB) sent over 3 hops (4 nodes, 3 links).
    # Each link rate R = 10 Mbps (10,000,000 bps). Prop delay negligible.
    # Case A: Message switching (entire 1 MB forwarded hop-by-hop)
    msg_delay_3_hops = 3 * transmission_delay(1_000_000, 10_000_000)
    # Case B: Packet switching with packets of 1,000 bytes (1000 packets)
    pkt_delay_3_hops = packet_switching_delay(1000, 1000, 10_000_000, 3, 0)
    print(f"P3: Message switching delay = {msg_delay_3_hops:.4f} s")
    print(f"P3: Packet switching delay = {pkt_delay_3_hops:.4f} s")
    print(f"P3 speedup ratio = {msg_delay_3_hops / pkt_delay_3_hops:.2f}x faster")

    # Problem 4: Bandwidth-Delay Product
    # Link: 100 Mbps, RTT = 50 ms (0.050 s)
    p4_bdp = bdp_bits(100_000_000, 0.050)
    p4_bdp_bytes = p4_bdp / 8
    print(f"P4: BDP = {p4_bdp:,.0f} bits ({p4_bdp_bytes:,.0f} bytes, {p4_bdp_bytes/1024:.2f} KiB or {p4_bdp_bytes/1e6:.2f} MB)")

    # Problem 5: Mesh topology
    # Network of 20 computers
    p5_links = mesh_links(20)
    p5_ports = mesh_ports_per_node(20)
    print(f"P5 (Full Mesh of 20 nodes): Links = {p5_links}, Ports per device = {p5_ports}, Total ports = {20 * p5_ports}")

    # Problem 6: Circuit vs Packet switching
    # 5 MB file over 4 links (3 intermediate switches). R = 50 Mbps.
    # Circuit switching: Setup time = 200 ms (0.2 s). Total prop delay = 20 ms (0.02 s).
    # Packet switching: Packet size = 1500 bytes (5 MB / 1500 = 3334 packets). Header = 40 bytes per packet.
    # Total data per packet = 1500 bytes. Number of packets = ceil(5,000,000 / 1460) = 3425 packets.
    p6_circ = circuit_switching_delay(0.200, 5_000_000, 50_000_000, 0.020)
    # Packet switching: 3425 packets of 1500 bytes over 4 links
    p6_pkt = packet_switching_delay(3425, 1500, 50_000_000, 4, 0.005)
    print(f"P6: Circuit switching total = {p6_circ:.4f} s")
    print(f"P6: Packet switching total = {p6_pkt:.4f} s")

    # Problem 7: Throughput vs Goodput
    # Link throughput = 100 Mbps.
    # Packet size = 1500 bytes, IP header = 20 bytes, TCP header = 20 bytes, Ethernet overhead = 18 bytes.
    # User data payload = 1460 bytes. Total on wire = 1518 bytes.
    p7_goodput = goodput(100_000_000, 1460, 1518)
    print(f"P7: Goodput = {p7_goodput / 1e6:.2f} Mbps (Efficiency = {1460/1518*100:.2f}%)")

    # Problem 8: End-to-end delay with Queuing and Processing
    # 2 routers (3 links). Each link = 10 Mbps, 100 km (v = 2e8 m/s).
    # Packet size = 1250 bytes (10,000 bits).
    # Processing delay per router = 20 microseconds.
    # Queuing delay: router 1 queue has 2 packets ahead; router 2 queue has 1 packet ahead.
    p8_Tt = 10_000 / 10_000_000 # 1 ms per link
    p8_Tp = 100_000 / 2e8 # 0.5 ms per link
    p8_Tproc = 2 * 0.000020 # 2 routers * 20 us = 40 us
    # Queuing delay: Router 1 waits for 2 packets to transmit = 2 * Tt = 2 ms
    # Router 2 waits for 1 packet to transmit = 1 * Tt = 1 ms
    p8_Tq = 2 * 0.001 + 1 * 0.001 # 3 ms
    p8_total = 3 * p8_Tt + 3 * p8_Tp + p8_Tproc + p8_Tq
    print(f"P8: Total delay with queues and processing = {p8_total*1000:.3f} ms")

    # Problem 9: Equal Tt and Tp condition (GATE standard)
    # At what distance does propagation delay equal transmission delay for a 1000-byte packet on 100 Mbps link? (v = 2*10^8 m/s)
    # Tt = 8000 / 10^8 = 8 * 10^-5 s = 80 microseconds
    # Tp = d / v = 80 us => d = 80 * 10^-6 * 2 * 10^8 = 16,000 meters = 16 km
    p9_Tt = transmission_delay(1000, 100_000_000)
    p9_d = p9_Tt * 2e8
    print(f"P9: Distance where Tt == Tp for 1000 B at 100 Mbps = {p9_d/1000:.2f} km")

    # Problem 10: Full mesh vs Star cable requirements
    # 10 computers:
    # Full mesh requires n(n-1)/2 = 45 cables.
    # Star requires n = 10 cables.
    print(f"P10: 10 computers -> Mesh: {mesh_links(10)} cables; Star: 10 cables.")

    print("=" * 60)
    print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY.")
    print("=" * 60)

if __name__ == "__main__":
    run_all_verifications()
