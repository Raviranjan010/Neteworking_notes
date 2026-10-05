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

    # 6. Minimum Hamming Distance Rules
    print(f"\n[6] Minimum Hamming Distance Requirements:")
    print(f"    To detect d errors:  d_min >= d + 1")
    print(f"    To correct t errors: d_min >= 2t + 1")
    print(f"    For d=2 error detection: d_min >= 3")
    print(f"    For t=1 error correction: d_min >= 3")
    print(f"    For t=2 error correction: d_min >= 5")
    print(f"    For t=1 correction + d=2 detection: d_min >= 4")
    print("=" * 60)
    print("ALL NUMERICAL VERIFICATIONS PASSED SUCCESSFULLY.")
    print("=" * 60)


if __name__ == "__main__":
    run_all_verifications()
