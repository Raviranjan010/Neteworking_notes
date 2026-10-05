# IP Addressing - MCQs (30 Questions)

## Beginner Level (Questions 1-10)

**Q1.** How many bits are in an IPv4 address?
- A) 16
- B) 32
- C) 64
- D) 128

**Answer:** B
**Explanation:** IPv4 addresses are 32-bit addresses, typically written as 4 octets in dotted decimal notation.

---

**Q2.** Which notation is used to represent IPv4 addresses?
- A) Hexadecimal
- B) Binary only
- C) Dotted decimal
- D) Octal

**Answer:** C
**Explanation:** IPv4 addresses use dotted decimal notation (e.g., 192.168.1.1), where each octet ranges from 0-255.

---

**Q3.** What is the range of values in each octet of an IPv4 address?
- A) 0-100
- B) 0-255
- C) 0-512
- D) 1-256

**Answer:** B
**Explanation:** Each octet is 8 bits, so it can represent values from 0 (00000000) to 255 (11111111).

---

**Q4.** Which IP address class supports the most hosts per network?
- A) Class A
- B) Class B
- C) Class C
- D) Class D

**Answer:** A
**Explanation:** Class A supports up to 16,777,214 hosts per network (2^24 - 2), the largest among all classes.

---

**Q5.** What is the loopback address?
- A) 192.168.1.1
- B) 10.0.0.1
- C) 127.0.0.1
- D) 255.255.255.0

**Answer:** C
**Explanation:** 127.0.0.1 is the loopback address (localhost) used to test network software on the local machine.

---

**Q6.** Which of the following is a private IP address?
- A) 8.8.8.8
- B) 172.32.0.1
- C) 192.168.1.10
- D) 200.100.50.1

**Answer:** C
**Explanation:** 192.168.0.0 to 192.168.255.255 is a private IP range. Other options are public IP addresses.

---

**Q7.** How many bits are in an IPv6 address?
- A) 32
- B) 64
- C) 96
- D) 128

**Answer:** D
**Explanation:** IPv6 uses 128-bit addresses, providing virtually unlimited unique addresses.

---

**Q8.** What is the default subnet mask for Class C?
- A) 255.0.0.0
- B) 255.255.0.0
- C) 255.255.255.0
- D) 255.255.255.255

**Answer:** C
**Explanation:** Class C uses 255.255.255.0 as default subnet mask, meaning first 3 octets are network portion.

---

**Q9.** Which IP class is used for multicasting?
- A) Class C
- B) Class D
- C) Class E
- D) Class A

**Answer:** B
**Explanation:** Class D (224.0.0.0 to 239.255.255.255) is reserved for multicasting (one-to-many communication).

---

**Q10.** What does APIPA stand for?
- A) Automatic Public IP Addressing
- B) Automatic Private IP Addressing
- C) Advanced Private IP Allocation
- D) Automated Protocol IP Addressing

**Answer:** B
**Explanation:** APIPA (Automatic Private IP Addressing) assigns addresses in 169.254.0.0 range when DHCP fails.

---

## Intermediate Level (Questions 11-20)

**Q11.** An IP address 150.100.50.25 belongs to which class?
- A) Class A
- B) Class B
- C) Class C
- D) Class D

**Answer:** B
**Explanation:** First octet is 150, which falls in range 128-191, making it a Class B address.

---

**Q12.** How many usable hosts are in a Class C network?
- A) 128
- B) 254
- C) 256
- D) 512

**Answer:** B
**Explanation:** Class C has 2^8 = 256 total addresses, minus 2 (network and broadcast) = 254 usable hosts.

---

**Q13.** Which private IP range belongs to Class A?
- A) 192.168.0.0/16
- B) 172.16.0.0/12
- C) 10.0.0.0/8
- D) 169.254.0.0/16

**Answer:** C
**Explanation:** 10.0.0.0 to 10.255.255.255 (10.0.0.0/8) is the Class A private IP range.

---

**Q14.** What is the binary representation of decimal 192?
- A) 10000000
- B) 11000000
- C) 11100000
- D) 10100000

**Answer:** B
**Explanation:** 192 = 128 + 64 = 11000000 in binary.

---

**Q15.** Why was IPv6 developed?
- A) To make addresses shorter
- B) IPv4 address exhaustion
- C) To replace TCP
- D) For better security only

**Answer:** B
**Explanation:** IPv4's 4.3 billion addresses were insufficient for global device growth, leading to IPv6 development.

---

**Q16.** Which address is used when DHCP server is unavailable?
- A) 127.0.0.1
- B) 10.0.0.1
- C) 169.254.x.x
- D) 192.168.1.1

**Answer:** C
**Explanation:** APIPA automatically assigns 169.254.x.x addresses when DHCP server cannot be reached.

---

**Q17.** In IPv6, how are addresses written?
- A) Dotted decimal
- B) Binary
- C) Hexadecimal with colons
- D) Octal

**Answer:** C
**Explanation:** IPv6 uses hexadecimal notation with 8 groups separated by colons (e.g., 2001:0db8::1).

---

**Q18.** What is the network address for 192.168.1.10/24?
- A) 192.168.1.0
- B) 192.168.1.1
- C) 192.168.1.255
- D) 192.168.1.10

**Answer:** A
**Explanation:** With /24 subnet mask (255.255.255.0), the network address is 192.168.1.0 (host bits set to 0).

---

**Q19.** Which statement about public IP addresses is TRUE?
- A) They are free to use
- B) They can be reused in different networks
- C) They must be globally unique
- D) They are assigned by manufacturers

**Answer:** C
**Explanation:** Public IP addresses must be globally unique and are allocated by Internet authorities/ISPs.

---

**Q20.** What is the broadcast address for 192.168.1.0/24?
- A) 192.168.1.0
- B) 192.168.1.1
- C) 192.168.1.254
- D) 192.168.1.255

**Answer:** D
**Explanation:** Broadcast address has all host bits set to 1. For /24 network, it's 192.168.1.255.

---

## Advanced Level (Questions 21-30)

**Q21.** How many total IPv4 addresses exist?
- A) 2^16
- B) 2^24
- C) 2^32
- D) 2^64

**Answer:** C
**Explanation:** IPv4 uses 32-bit addresses, so total addresses = 2^32 = 4,294,967,296 (approximately 4.3 billion).

---

**Q22.** Which IPv6 address represents the loopback address?
- A) ::1
- B) ::
- C) fe80::1
- D) 2001::1

**Answer:** A
**Explanation:** ::1 is the IPv6 loopback address, equivalent to 127.0.0.1 in IPv4.

---

**Q23.** Why can't private IP addresses communicate directly on the Internet?
- A) They are encrypted
- B) They are not globally routable
- C) They use different protocols
- D) They are slower

**Answer:** B
**Explanation:** Private IP addresses are not routable on the Internet. They require NAT (Network Address Translation) to access the Internet.

---

**Q24.** What is the purpose of the subnet mask?
- A) To encrypt IP addresses
- B) To identify network and host portions
- C) To compress addresses
- D) To convert binary to decimal

**Answer:** B
**Explanation:** Subnet mask distinguishes which bits represent the network portion and which represent the host portion.

---

**Q25.** Which simplification rule applies to IPv6 addresses?
- A) Remove all zeros
- B) Replace consecutive zeros with ::
- C) Use dots instead of colons
- D) Convert to decimal

**Answer:** B
**Explanation:** In IPv6, consecutive groups of zeros can be replaced with :: (only once per address).

---

**Q26.** An organization needs 1000 hosts. Which IP class is most appropriate?
- A) Class A
- B) Class B
- C) Class C
- D) Class D

**Answer:** B
**Explanation:** Class B supports 65,534 hosts, sufficient for 1000 hosts. Class C only supports 254 hosts (insufficient).

---

**Q27.** What happens if two devices on the same network have the same IP address?
- A) They share the address
- B) IP conflict occurs, communication fails
- C) One device automatically changes
- D) Nothing happens

**Answer:** B
**Explanation:** IP address conflicts cause communication problems for both devices. Each device must have a unique IP.

---

**Q28.** Which is NOT a valid IPv4 address?
- A) 192.168.1.1
- B) 10.0.0.1
- C) 256.100.50.25
- D) 172.16.0.1

**Answer:** C
**Explanation:** 256 is invalid because each octet must be 0-255. Valid range is 0-255 (8 bits).

---

**Q29.** What is the main advantage of IPv6 over IPv4?
- A) Simpler configuration
- B) Vastly more addresses
- C) Faster transmission
- D) Better encryption

**Answer:** B
**Explanation:** IPv6's main advantage is the enormous address space (2^128 addresses), solving IPv4 exhaustion.

---

**Q30.** In CIDR notation, what does /16 mean?
- A) 16 hosts
- B) 16 bits for network portion
- C) 16 networks
- D) 16-bit address

**Answer:** B
**Explanation:** /16 means first 16 bits are network portion (equivalent to subnet mask 255.255.0.0, Class B default).

---

## Score Interpretation

- **27-30:** Excellent! Strong IP addressing knowledge. Proceed to subnetting.
- **20-26:** Good. Review weak areas before moving forward.
- **15-19:** Fair. Re-read notes, practice binary conversion.
- **Below 15:** Review entire topic thoroughly.
