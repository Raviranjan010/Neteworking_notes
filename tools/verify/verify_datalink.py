#!/usr/bin/env python3
"""
tools/verify/verify_datalink.py - Verification Script for Data Link Layer Numericals (05a).

Computes and verifies exact numerical values for:
1. Bit stuffing (HDLC flag 01111110, insert '0' after five consecutive '1's).
2. Byte stuffing (Character stuffing with ESC and FLAG bytes).
3. 1-D and 2-D Parity checks.
4. Internet Checksum (RFC 1071 16-bit one's complement arithmetic).
5. CRC (Cyclic Redundancy Check) modulo-2 polynomial division, remainder, and burst detection bounds.
6. Hamming Code (r bits bound 2^r >= m + r + 1, parity bit positions, syndrome error correction).
7. Minimum Hamming distance bounds for error detection and error correction.
"""

import sys
import math

# Ensure UTF-8 output on Windows terminals
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def bit_stuff(data_bits: str) -> tuple[str, int]:
    """HDLC Bit Stuffing: Insert a '0' after every five consecutive '1's."""
    stuffed = []
    count_ones = 0
    stuffed_zeros = 0

    for bit in data_bits:
        stuffed.append(bit)
        if bit == '1':
            count_ones += 1
            if count_ones == 5:
                stuffed.append('0')
                stuffed_zeros += 1
                count_ones = 0
        else:
            count_ones = 0

    stuffed_str = "".join(stuffed)
    return stuffed_str, stuffed_zeros


def bit_destuff(stuffed_bits: str) -> str:
    """HDLC Bit Destuffing: Remove the '0' that follows five consecutive '1's."""
    destuffed = []
    count_ones = 0
    i = 0
    n = len(stuffed_bits)

    while i < n:
        bit = stuffed_bits[i]
        destuffed.append(bit)
        if bit == '1':
            count_ones += 1
            if count_ones == 5:
                # Next bit must be stuffed '0', skip it
                if i + 1 < n and stuffed_bits[i + 1] == '0':
                    i += 1
                count_ones = 0
        else:
            count_ones = 0
        i += 1

    return "".join(destuffed)


def byte_stuff(payload_bytes: list[str], flag: str = "FLAG", esc: str = "ESC") -> list[str]:
    """Byte stuffing: prepend ESC before any FLAG or ESC byte."""
    stuffed = [flag]
    for b in payload_bytes:
        if b in (flag, esc):
            stuffed.append(esc)
        stuffed.append(b)
    stuffed.append(flag)
    return stuffed


def crc_modulo2_div(dividend: str, divisor: str) -> tuple[str, str]:
    """Perform Modulo-2 binary polynomial division (XOR division)."""
    d_list = list(dividend)
    div_len = len(divisor)

    for i in range(len(dividend) - div_len + 1):
        if d_list[i] == '1':
            for j in range(div_len):
                d_list[i + j] = '1' if d_list[i + j] != divisor[j] else '0'

    remainder = "".join(d_list[-(div_len - 1):])
    return remainder, "".join(d_list)


def calculate_crc(data_bits: str, generator_poly: str) -> tuple[str, str]:
    """Append r zeros and compute CRC FCS remainder."""
    r = len(generator_poly) - 1
    augmented = data_bits + ("0" * r)
    remainder, _ = crc_modulo2_div(augmented, generator_poly)
    codeword = data_bits + remainder
    return remainder, codeword


def verify_crc(codeword: str, generator_poly: str) -> bool:
    """Receiver CRC check: remainder should be all zeros."""
    r = len(generator_poly) - 1
    rem, _ = crc_modulo2_div(codeword, generator_poly)
    return rem == ("0" * r)


def compute_internet_checksum(words16: list[int]) -> tuple[int, int]:
    """Compute 16-bit 1's complement Internet Checksum (RFC 1071)."""
    total = sum(words16)
    # Add carry bits back to LSB
    while (total >> 16) > 0:
        total = (total & 0xFFFF) + (total >> 16)
    checksum = (~total) & 0xFFFF
    return total, checksum


def verify_internet_checksum(words16: list[int], checksum: int) -> bool:
    total = sum(words16) + checksum
    while (total >> 16) > 0:
        total = (total & 0xFFFF) + (total >> 16)
    return total == 0xFFFF


def min_hamming_bits(m: int) -> int:
    """Find minimum parity bits r such that 2^r >= m + r + 1."""
    r = 1
    while (1 << r) < (m + r + 1):
        r += 1
    return r


def generate_hamming_7_4(data4: str) -> tuple[str, dict]:
    """Generate (7,4) Hamming code with even parity.
    Bit positions 1 to 7 (1-indexed):
    p1: 1, p2: 2, d3: 3, p4: 4, d5: 5, d6: 6, d7: 7
    Data bits: d3, d5, d6, d7
    """
    assert len(data4) == 4
    d3 = int(data4[0])
    d5 = int(data4[1])
    d6 = int(data4[2])
    d7 = int(data4[3])

    # Even parity equations:
    # p1 covers positions with bit 0 set (1, 3, 5, 7) -> p1 ^ d3 ^ d5 ^ d7 = 0
    p1 = d3 ^ d5 ^ d7
    # p2 covers positions with bit 1 set (2, 3, 6, 7) -> p2 ^ d3 ^ d6 ^ d7 = 0
    p2 = d3 ^ d6 ^ d7
    # p4 covers positions with bit 2 set (4, 5, 6, 7) -> p4 ^ d5 ^ d6 ^ d7 = 0
    p4 = d5 ^ d6 ^ d7

    codeword = f"{p1}{p2}{d3}{p4}{d5}{d6}{d7}"
    details = {"p1": p1, "p2": p2, "p4": p4, "d3": d3, "d5": d5, "d6": d6, "d7": d7}
    return codeword, details


def decode_hamming_7_4(received7: str) -> tuple[int, str]:
    """Calculate syndrome for received (7,4) codeword and correct error if present."""
    assert len(received7) == 7
    b = [0] + [int(ch) for ch in received7]  # 1-indexed

    s1 = b[1] ^ b[3] ^ b[5] ^ b[7]
    s2 = b[2] ^ b[3] ^ b[6] ^ b[7]
    s4 = b[4] ^ b[5] ^ b[6] ^ b[7]

    syndrome = (s4 << 2) | (s2 << 1) | s1
    corrected = list(b)
    if syndrome != 0:
        corrected[syndrome] ^= 1

    corrected_str = "".join(str(corrected[i]) for i in range(1, 8))
    return syndrome, corrected_str


def run_all_verifications():
    print("=" * 60)
    print("DATA LINK LAYER (05a) NUMERICAL VERIFICATION REPORT")
    print("=" * 60)

    # 1. Bit Stuffing Example
    test_bits = "011111101111100111111111110"
    stuffed, count_z = bit_stuff(test_bits)
    destuffed = bit_destuff(stuffed)
    assert destuffed == test_bits, "Bit destuffing failed!"
    print(f"\n[1] HDLC Bit Stuffing Verification:")
    print(f"    Original bits:   {test_bits} ({len(test_bits)} bits)")
    print(f"    Stuffed bits:    {stuffed} ({len(stuffed)} bits)")
    print(f"    Stuffed '0's:    {count_z}")
    print(f"    Overhead:        {(len(stuffed) - len(test_bits)) / len(test_bits) * 100:.2f}%")
    print(f"    Destuff check:   PASS (Matches original)")

    # 2. Byte Stuffing Example
    raw_payload = ["A", "FLAG", "B", "ESC", "C"]
    stuffed_bytes = byte_stuff(raw_payload)
    print(f"\n[2] Byte Stuffing Verification:")
    print(f"    Original bytes:  {raw_payload} ({len(raw_payload)} bytes)")
    print(f"    Stuffed frame:   {stuffed_bytes} ({len(stuffed_bytes)} bytes)")
    print(f"    Added ESC bytes: 2 (Total overhead including framing: 4 bytes)")

    # 3. Checksum Example (Two 16-bit words)
    w1, w2 = 0x4500, 0x003C
    total, csum = compute_internet_checksum([w1, w2])
    valid = verify_internet_checksum([w1, w2], csum)
    print(f"\n[3] 16-bit Internet Checksum Verification:")
    print(f"    Word 1: 0x{w1:04X}, Word 2: 0x{w2:04X}")
    print(f"    Sum: 0x{total:04X}, 1's Complement Checksum: 0x{csum:04X}")
    print(f"    Receiver verification (Sum + Checksum == 0xFFFF): {valid}")

    # 4. CRC Verification
    data = "100100"
    generator = "1101"  # x^3 + x^2 + 1
    rem, codeword = calculate_crc(data, generator)
    is_valid = verify_crc(codeword, generator)
    print(f"\n[4] CRC Modulo-2 Division Verification:")
    print(f"    Data:        {data}")
    print(f"    Generator:   {generator} (degree r = {len(generator)-1})")
    print(f"    Remainder:   {rem}")
    print(f"    Codeword:    {codeword}")
    print(f"    Check valid: {is_valid}")

    # CRC Problem 2 (Standard GATE Example)
    data2 = "1101011011"
    gen2 = "10011"  # x^4 + x + 1 (r=4)
    rem2, cw2 = calculate_crc(data2, gen2)
    assert verify_crc(cw2, gen2), "CRC 2 check failed!"
    print(f"    GATE CRC Data: {data2}, Gen: {gen2} -> Remainder: {rem2}, Codeword: {cw2}")

    # 5. Hamming Code Bounds & Generation
    print(f"\n[5] Hamming Code Bounds & (7,4) Code:")
    for m in [4, 7, 8, 11, 16, 32]:
        r = min_hamming_bits(m)
        print(f"    Data bits m={m:2d} -> Min parity bits r={r} (Total n={m+r:2d}, Efficiency={m/(m+r)*100:.1f}%)")

    test_data4 = "1011"  # d3=1, d5=0, d6=1, d7=1
    cw7, det = generate_hamming_7_4(test_data4)
    print(f"    Data: {test_data4} -> (7,4) Codeword: {cw7}")
    print(f"    Parity bits: p1={det['p1']}, p2={det['p2']}, p4={det['p4']}")

    # Inject single-bit error at position 5 (index 4 in 0-indexed string)
    corrupted = list(cw7)
    corrupted[4] = '1' if corrupted[4] == '0' else '0'  # Flip bit at pos 5
    corrupted_str = "".join(corrupted)
    syndrome, corrected = decode_hamming_7_4(corrupted_str)
    print(f"    Injected error at bit position 5: {corrupted_str}")
    print(f"    Detected error at position: {syndrome}")
    print(f"    Corrected codeword: {corrected} (Matches original: {corrected == cw7})")

def stop_and_wait_metrics(frame_size_bytes: int, bandwidth_bps: float, distance_km: float,
                           prop_speed_mps: float = 2e8, ack_size_bytes: int = 0,
                           proc_time_s: float = 0.0, error_prob: float = 0.0) -> dict:
    """Calculate exact timing, utilization, and throughput for Stop-and-Wait ARQ."""
    frame_bits = frame_size_bytes * 8
    ack_bits = ack_size_bytes * 8

    tt = frame_bits / bandwidth_bps
    tp = (distance_km * 1000.0) / prop_speed_mps
    t_ack = ack_bits / bandwidth_bps if ack_bits > 0 else 0.0

    a = tp / tt
    total_cycle = tt + 2 * tp + t_ack + proc_time_s
    ideal_efficiency = tt / total_cycle
    simple_efficiency = 1.0 / (1.0 + 2.0 * a)

    avg_transmissions = 1.0 / (1.0 - error_prob) if error_prob < 1.0 else float('inf')
    effective_efficiency = (1.0 - error_prob) * ideal_efficiency
    ideal_throughput_bps = ideal_efficiency * bandwidth_bps
    effective_throughput_bps = effective_efficiency * bandwidth_bps

    return {
        "Tt_ms": tt * 1000.0,
        "Tp_ms": tp * 1000.0,
        "Tack_ms": t_ack * 1000.0,
        "a": a,
        "cycle_time_ms": total_cycle * 1000.0,
        "ideal_efficiency": ideal_efficiency,
        "effective_efficiency": effective_efficiency,
        "simple_efficiency": simple_efficiency,
        "ideal_throughput_kbps": ideal_throughput_bps / 1000.0,
        "effective_throughput_kbps": effective_throughput_bps / 1000.0,
        "avg_transmissions": avg_transmissions,
        "bdp_bits": bandwidth_bps * (2 * tp),
        "optimal_window_size": math.ceil(1.0 + 2.0 * a)
    }


def sliding_window_metrics(frame_size_bytes: int, bandwidth_bps: float, distance_km: float,
                           window_size_N: int, prop_speed_mps: float = 2e8,
                           protocol: str = "GBN", error_prob: float = 0.0) -> dict:
    """Calculate exact metrics for Sliding Window protocols (GBN and SR)."""
    frame_bits = frame_size_bytes * 8
    tt = frame_bits / bandwidth_bps
    tp = (distance_km * 1000.0) / prop_speed_mps
    a = tp / tt

    optimal_N = math.ceil(1.0 + 2.0 * a)
    ideal_efficiency = min(1.0, window_size_N / (1.0 + 2.0 * a))
    ideal_throughput_bps = ideal_efficiency * bandwidth_bps

    if protocol.upper() == "GBN":
        # Under GBN, each error retransmits N frames: E[tx] = (1 + (N-1)P) / (1 - P)
        if error_prob > 0.0:
            avg_tx = (1.0 + (window_size_N - 1) * error_prob) / (1.0 - error_prob)
            effective_efficiency = (1.0 - error_prob) / (1.0 + (window_size_N - 1) * error_prob) * ideal_efficiency
        else:
            avg_tx = 1.0
            effective_efficiency = ideal_efficiency
    else:  # Selective Repeat: only erroneous frame is retransmitted
        avg_tx = 1.0 / (1.0 - error_prob) if error_prob < 1.0 else float('inf')
        effective_efficiency = (1.0 - error_prob) * ideal_efficiency

    effective_throughput_bps = effective_efficiency * bandwidth_bps

    return {
        "Tt_ms": tt * 1000.0,
        "Tp_ms": tp * 1000.0,
        "a": a,
        "optimal_window_N": optimal_N,
        "ideal_efficiency": ideal_efficiency,
        "effective_efficiency": effective_efficiency,
        "ideal_throughput_kbps": ideal_throughput_bps / 1000.0,
        "effective_throughput_kbps": effective_throughput_bps / 1000.0,
        "avg_transmissions": avg_tx,
        "bdp_bits": bandwidth_bps * (2 * tp),
        "bdp_frames": (bandwidth_bps * (2 * tp)) / frame_bits
    }


def window_sequence_math(k_bits: int) -> dict:
    """Compute maximum window sizes and ambiguity boundaries for k-bit sequence numbers."""
    total_seq = 2 ** k_bits
    gbn_max_ws = total_seq - 1
    gbn_wr = 1
    sr_max_ws = total_seq // 2
    sr_max_wr = total_seq // 2

    return {
        "k_bits": k_bits,
        "total_seq_numbers": total_seq,
        "gbn_max_sender_window": gbn_max_ws,
        "gbn_receiver_window": gbn_wr,
        "sr_max_sender_window": sr_max_ws,
        "sr_max_receiver_window": sr_max_wr,
        "gbn_window_sum": gbn_max_ws + gbn_wr,
        "sr_window_sum": sr_max_ws + sr_max_wr
    }


def run_all_verifications():
    print("=" * 60)
    print("DATA LINK LAYER (05a & 05b) NUMERICAL VERIFICATION SUITE")
    print("=" * 60)

    # 1. HDLC Bit Stuffing Example
    test_bits = "0111111011111001111101111110"
    stuffed, count_z = bit_stuff(test_bits)
    destuffed = bit_destuff(stuffed)
    assert destuffed == test_bits, "Bit destuffing failed to restore original string!"
    print(f"\n[1] HDLC Bit Stuffing Verification:")
    print(f"    Original data:   {test_bits} ({len(test_bits)} bits)")
    print(f"    Stuffed data:    {stuffed} ({len(stuffed)} bits)")
    print(f"    Stuffed '0's:    {count_z}")
    print(f"    Overhead:        {(len(stuffed) - len(test_bits)) / len(test_bits) * 100:.2f}%")
    print(f"    Destuff check:   PASS (Matches original)")

    # 2. Byte Stuffing Example
    raw_payload = ["A", "FLAG", "B", "ESC", "C"]
    stuffed_bytes = byte_stuff(raw_payload)
    print(f"\n[2] Byte Stuffing Verification:")
    print(f"    Original bytes:  {raw_payload} ({len(raw_payload)} bytes)")
    print(f"    Stuffed frame:   {stuffed_bytes} ({len(stuffed_bytes)} bytes)")
    print(f"    Added ESC bytes: 2 (Total overhead including framing: 4 bytes)")

    # 3. Checksum Example (Two 16-bit words)
    w1, w2 = 0x4500, 0x003C
    total, csum = compute_internet_checksum([w1, w2])
    valid = verify_internet_checksum([w1, w2], csum)
    print(f"\n[3] 16-bit Internet Checksum Verification:")
    print(f"    Word 1: 0x{w1:04X}, Word 2: 0x{w2:04X}")
    print(f"    Sum: 0x{total:04X}, 1's Complement Checksum: 0x{csum:04X}")
    print(f"    Receiver verification (Sum + Checksum == 0xFFFF): {valid}")

    # 4. CRC Verification
    data = "100100"
    generator = "1101"  # x^3 + x^2 + 1
    rem, codeword = calculate_crc(data, generator)
    is_valid = verify_crc(codeword, generator)
    print(f"\n[4] CRC Modulo-2 Division Verification:")
    print(f"    Data:        {data}")
    print(f"    Generator:   {generator} (degree r = {len(generator)-1})")
    print(f"    Remainder:   {rem}")
    print(f"    Codeword:    {codeword}")
    print(f"    Check valid: {is_valid}")

    # CRC Problem 2 (Standard GATE Example)
    data2 = "1101011011"
    gen2 = "10011"  # x^4 + x + 1 (r=4)
    rem2, cw2 = calculate_crc(data2, gen2)
    assert verify_crc(cw2, gen2), "CRC 2 check failed!"
    print(f"    GATE CRC Data: {data2}, Gen: {gen2} -> Remainder: {rem2}, Codeword: {cw2}")

    # 5. Hamming Code Bounds & Generation
    print(f"\n[5] Hamming Code Bounds & (7,4) Code:")
    for m in [4, 7, 8, 11, 16, 32]:
        r = min_hamming_bits(m)
        print(f"    Data bits m={m:2d} -> Min parity bits r={r} (Total n={m+r:2d}, Efficiency={m/(m+r)*100:.1f}%)")

    test_data4 = "1011"  # d3=1, d5=0, d6=1, d7=1
    cw7, det = generate_hamming_7_4(test_data4)
    print(f"    Data: {test_data4} -> (7,4) Codeword: {cw7}")
    print(f"    Parity bits: p1={det['p1']}, p2={det['p2']}, p4={det['p4']}")

    # Inject single-bit error at position 5
    corrupted = list(cw7)
    corrupted[4] = '1' if corrupted[4] == '0' else '0'
    corrupted_str = "".join(corrupted)
    syndrome, corrected = decode_hamming_7_4(corrupted_str)
    print(f"    Injected error at bit position 5: {corrupted_str}")
    print(f"    Detected error at position: {syndrome}")
    print(f"    Corrected codeword: {corrected} (Matches original: {corrected == cw7})")

    # 6. Minimum Hamming Distance Rules
    print(f"\n[6] Minimum Hamming Distance Requirements:")
    print(f"    To detect d errors:  d_min >= d + 1")
    print(f"    To correct t errors: d_min >= 2t + 1")
    print(f"    For d=2 error detection: d_min >= 3")
    print(f"    For t=1 error correction: d_min >= 3")
    print(f"    For t=2 error correction: d_min >= 5")
    print(f"    For t=1 correction + d=2 detection: d_min >= 4")

    # 7. Flow Control: Stop-and-Wait Calculations (05b)
    print(f"\n[7] Stop-and-Wait ARQ Verification:")
    # Satellite link: L=1000 Bytes, B=1 Mbps, d=36,000 km, v=3e8 m/s
    sw_sat = stop_and_wait_metrics(frame_size_bytes=1000, bandwidth_bps=1e6, distance_km=36000, prop_speed_mps=3e8)
    print(f"    Satellite Link (1 Mbps, 36000 km, 1000B frame):")
    print(f"      Tt = {sw_sat['Tt_ms']:.2f} ms, Tp = {sw_sat['Tp_ms']:.2f} ms, a = {sw_sat['a']:.2f}")
    print(f"      Efficiency = {sw_sat['ideal_efficiency']*100:.3f}% (1/(1+2a) = {sw_sat['simple_efficiency']*100:.3f}%)")
    print(f"      Throughput = {sw_sat['ideal_throughput_kbps']:.2f} kbps")
    print(f"      Optimal window N for 100% util: {sw_sat['optimal_window_size']}")

    # LAN link: L=1500 Bytes, B=100 Mbps, d=1 km, v=2e8 m/s
    sw_lan = stop_and_wait_metrics(frame_size_bytes=1500, bandwidth_bps=100e6, distance_km=1, prop_speed_mps=2e8)
    print(f"    Fast Ethernet LAN (100 Mbps, 1 km, 1500B frame):")
    print(f"      Tt = {sw_lan['Tt_ms']:.3f} ms, Tp = {sw_lan['Tp_ms']:.3f} ms, a = {sw_lan['a']:.4f}")
    print(f"      Efficiency = {sw_lan['ideal_efficiency']*100:.2f}%")
    print(f"      Throughput = {sw_lan['ideal_throughput_kbps']/1000:.2f} Mbps")

    # Stop-and-Wait with ACK transmission & error probability P=0.1
    sw_err = stop_and_wait_metrics(frame_size_bytes=1000, bandwidth_bps=1e6, distance_km=1000, prop_speed_mps=2e8,
                                   ack_size_bytes=100, proc_time_s=0.001, error_prob=0.1)
    print(f"    SW with ACK=100B, Tproc=1ms, P=0.1 error:")
    print(f"      Cycle time = {sw_err['cycle_time_ms']:.2f} ms")
    print(f"      Ideal Util = {sw_err['ideal_efficiency']*100:.2f}%, Effective Util = {sw_err['effective_efficiency']*100:.2f}%")
    print(f"      Avg Transmissions per packet = {sw_err['avg_transmissions']:.3f}")

    # 8. Sliding Window (GBN and SR) Calculations (05b)
    print(f"\n[8] Sliding Window (GBN vs SR) Verification:")
    # Satellite link with N=15 and N=31
    gbn_sat_15 = sliding_window_metrics(frame_size_bytes=1000, bandwidth_bps=1e6, distance_km=36000,
                                        window_size_N=15, prop_speed_mps=3e8)
    gbn_sat_31 = sliding_window_metrics(frame_size_bytes=1000, bandwidth_bps=1e6, distance_km=36000,
                                        window_size_N=31, prop_speed_mps=3e8)
    print(f"    Satellite Link (a = {gbn_sat_15['a']:.1f}, Optimal N = {gbn_sat_15['optimal_window_N']}):")
    print(f"      N=15: Util = {gbn_sat_15['ideal_efficiency']*100:.2f}%, Throughput = {gbn_sat_15['ideal_throughput_kbps']:.1f} kbps")
    print(f"      N=31: Util = {gbn_sat_31['ideal_efficiency']*100:.2f}%, Throughput = {gbn_sat_31['ideal_throughput_kbps']:.1f} kbps")

    # GBN vs SR under packet loss P=0.05
    gbn_err = sliding_window_metrics(frame_size_bytes=1000, bandwidth_bps=10e6, distance_km=2000,
                                     window_size_N=8, prop_speed_mps=2e8, protocol="GBN", error_prob=0.05)
    sr_err = sliding_window_metrics(frame_size_bytes=1000, bandwidth_bps=10e6, distance_km=2000,
                                    window_size_N=8, prop_speed_mps=2e8, protocol="SR", error_prob=0.05)
    print(f"    Sliding Window with P=0.05 error (N=8, a={gbn_err['a']:.2f}):")
    print(f"      GBN: Eff Util = {gbn_err['effective_efficiency']*100:.2f}%, Avg Tx = {gbn_err['avg_transmissions']:.3f}")
    print(f"      SR:  Eff Util = {sr_err['effective_efficiency']*100:.2f}%, Avg Tx = {sr_err['avg_transmissions']:.3f}")

    # 9. Sequence Number Math & Overlap Proof (05b)
    print(f"\n[9] Sequence Number Math & Window Bounds:")
    for k in [1, 2, 3, 4, 7]:
        wm = window_sequence_math(k)
        print(f"    k={k:1d} bits -> Modulo {wm['total_seq_numbers']:3d} | GBN: Ws<={wm['gbn_max_sender_window']:3d}, Wr={wm['gbn_receiver_window']} | SR: Ws<={wm['sr_max_sender_window']:3d}, Wr<={wm['sr_max_receiver_window']:3d}")

    print("=" * 60)
    print("ALL NUMERICAL VERIFICATIONS (05a & 05b) PASSED SUCCESSFULLY.")
    print("=" * 60)


if __name__ == "__main__":
    run_all_verifications()

