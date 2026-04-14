# Application Layer - MCQs (30 Troubleshooting & Output-Based)

## Beginner Level (Questions 1-10)

**Q1.** What is the main function of DNS?
- A) Send emails
- B) Translate domain names to IP addresses
- C) Transfer files
- D) Encrypt web traffic

**Answer:** B
**Explanation:** DNS (Domain Name System) translates human-readable domain names (www.google.com) to machine-readable IP addresses (142.250.80.46).

---

**Q2.** Which port does HTTPS use?
- A) 80
- B) 443
- C) 8080
- D) 22

**Answer:** B
**Explanation:** HTTPS uses port 443. HTTP (unencrypted) uses port 80. Port 443 includes TLS/SSL encryption.

---

**Q3.** What does DHCP stand for?
- A) Dynamic Host Configuration Protocol
- B) Domain Host Control Protocol
- C) Dynamic Hyperlink Configuration Protocol
- D) Domain HyperText Control Protocol

**Answer:** A
**Explanation:** DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addresses and network configuration to devices.

---

**Q4.** Which protocol is used for sending emails?
- A) POP3
- B) IMAP
- C) SMTP
- D) HTTP

**Answer:** C
**Explanation:** SMTP (Simple Mail Transfer Protocol) is used for sending/transferring emails between servers. POP3 and IMAP are for retrieving emails.

---

**Q5.** What type of DNS record maps a domain to an IPv4 address?
- A) AAAA record
- B) MX record
- C) A record
- D) CNAME record

**Answer:** C
**Explanation:** A record maps a domain name to an IPv4 address. AAAA record maps to IPv6 address. MX record specifies mail servers.

---

**Q6.** Which email protocol keeps emails on the server?
- A) POP3
- B) SMTP
- C) IMAP
- D) HTTP

**Answer:** C
**Explanation:** IMAP (Internet Message Access Protocol) syncs with server and keeps emails on server. POP3 typically downloads and deletes from server.

---

**Q7.** What is the first step when you type a URL in browser?
- A) TCP handshake
- B) DNS resolution
- C) HTTP request
- D) TLS handshake

**Answer:** B
**Explanation:** First, browser must resolve the domain name to an IP address via DNS. Without IP, no connection can be established.

---

**Q8.** Which protocol uses UDP port 53?
- A) HTTP
- B) DHCP
- C) DNS
- D) SMTP

**Answer:** C
**Explanation:** DNS primarily uses UDP port 53 for queries (faster). TCP port 53 is used for zone transfers (larger data).

---

**Q9.** What does HTTP status code 404 mean?
- A) Server error
- B) Redirect
- C) Not Found
- D) Unauthorized

**Answer:** C
**Explanation:** 404 Not Found means the requested resource doesn't exist on the server. Common causes: wrong URL, deleted page, typo.

---

**Q10.** In DHCP, what does DORA stand for?
- A) Discover, Offer, Request, Acknowledge
- B) Domain, Organization, Registration, Access
- C) Data, Output, Response, Acknowledge
- D) Direct, Open, Route, Assign

**Answer:** A
**Explanation:** DHCP DORA process: Discover (client broadcasts) → Offer (server offers IP) → Request (client accepts) → Acknowledge (server confirms).

---

## Intermediate Level (Questions 11-20)

**Q11.** OUTPUT QUESTION: You run `nslookup google.com` and get:
```
Server: 8.8.8.8
Address: 142.250.80.46
```
What does this show?
- A) Your computer's IP address
- B) DNS server used and resolved IP for google.com
- C) Web server status
- D) Email server information

**Answer:** B
**Explanation:** nslookup shows DNS resolution results. Server 8.8.8.8 (Google DNS) was queried, and google.com resolves to 142.250.80.46.

---

**Q12.** What happens during TLS handshake?
- A) IP address assignment
- B) Encryption negotiation and certificate verification
- C) DNS resolution
- D) Email authentication

**Answer:** B
**Explanation:** TLS handshake establishes encrypted connection: client/server agree on TLS version, cipher suite, exchange certificates, verify authenticity, and generate session keys.

---

**Q13.** OUTPUT QUESTION: `dig example.com MX` returns:
```
example.com. 3600 IN MX 10 mail.example.com.
```
What does this mean?
- A) Web server location
- B) Mail server for example.com with priority 10
- C) DNS server address
- D) FTP server information

**Answer:** B
**Explanation:** MX (Mail Exchange) record shows mail server for the domain. Priority 10 (lower = higher priority). Email for example.com goes to mail.example.com.

---

**Q14.** Why does HTTP use TCP instead of UDP?
- A) HTTP needs speed
- B) HTTP requires reliable, complete data delivery
- C) UDP doesn't support port 80
- D) HTTP can't work with UDP

**Answer:** B
**Explanation:** HTTP needs reliable delivery - web pages must arrive complete and in order. TCP guarantees this with acknowledgments and retransmission. Missing part of a webpage breaks it.

---

**Q15.** OUTPUT QUESTION: Browser DevTools shows TTFB = 2 seconds. What's the issue?
- A) DNS is slow
- B) Server is slow to generate response
- C) Network bandwidth low
- D) Images are large

**Answer:** B
**Explanation:** TTFB (Time To First Byte) measures server response time. 2 seconds is slow. Indicates server-side processing delay (database queries, application logic, server load).

---

**Q16.** What is the difference between POP3 and IMAP?
- A) POP3 is faster
- B) IMAP syncs with server, POP3 downloads and deletes
- C) POP3 is more secure
- D) No difference

**Answer:** B
**Explanation:** IMAP keeps emails on server and syncs across devices. POP3 downloads emails to local device and typically deletes from server. IMAP better for multiple devices.

---

**Q17.** OUTPUT QUESTION: `ipconfig /all` shows:
```
DHCP Enabled: Yes
IP Address: 192.168.1.100
Lease Obtained: April 14, 2026 8:00 AM
Lease Expires: April 15, 2026 8:00 AM
```
What does this indicate?
- A) Static IP configuration
- B) DHCP-assigned IP with 24-hour lease
- C) DNS configuration error
- D) Network disconnected

**Answer:** B
**Explanation:** DHCP Enabled: Yes means IP was automatically assigned. 24-hour lease (8 AM to 8 AM next day). Client must renew before expiry or get new IP.

---

**Q18.** Which HTTP method should be used to update an existing resource?
- A) GET
- B) POST
- C) PUT
- D) DELETE

**Answer:** C
**Explanation:** PUT updates/replaces an existing resource. GET retrieves, POST creates new, DELETE removes. PUT is idempotent (same result if called multiple times).

---

**Q19.** What is a DNS CNAME record?
- A) Direct IP address mapping
- B) Alias from one domain to another
- C) Mail server record
- D) Text record

**Answer:** B
**Explanation:** CNAME (Canonical Name) creates an alias. Example: www.example.com CNAME → example.com. Changes to example.com's A record automatically apply to www.

---

**Q20.** OUTPUT QUESTION: `telnet mail.server.com 25` connects successfully. What does this prove?
- A) Email delivery working
- B) SMTP service is running and reachable
- C) DNS is configured
- D) User can send emails

**Answer:** B
**Explanation:** Successful telnet to port 25 proves SMTP service is running and network connectivity exists. Doesn't prove email delivery works (need to test actual SMTP transaction).

---

## Advanced Level (Questions 21-30) - Troubleshooting & Scenarios

**Q21.** TROUBLESHOOT: Website loads but images don't. Browser console shows 403 errors for images. Cause?
- A) DNS issue
- B) File permissions or access control blocking images
- C) Network connectivity
- D) SSL certificate

**Answer:** B
**Explanation:** 403 Forbidden means server understands request but refuses to fulfill it. Images exist but access denied. Check file permissions, .htaccess rules, or CDN configuration.

---

**Q22.** SCENARIO: After DNS server change, users report website unreachable. Most likely cause?
- A) Web server down
- B) DNS propagation delay or incorrect records on new server
- C) Network cable unplugged
- D) Browser cache

**Answer:** B
**Explanation:** DNS changes take time to propagate (TTL-dependent). New DNS server may have missing/incorrect records. Check: dig @new-dns-server domain.com. Compare with old server.

---

**Q23.** TROUBLESHOOT: Emails bouncing with "550 Mailbox not found". What's wrong?
- A) Mail server down
- B) Invalid recipient email address
- C) Network issue
- D) Spam filter

**Answer:** B
**Explanation:** 550 error with "Mailbox not found" means recipient email address doesn't exist on destination server. Verify email address spelling, check if user account exists.

---

**Q24.** INTERVIEW: Why does DNS use UDP for queries but TCP for zone transfers?
- A) UDP is more reliable
- B) UDP is faster for small queries, TCP needed for large zone data
- C) TCP doesn't support DNS
- D) Random design choice

**Answer:** B
**Explanation:** DNS queries are small (<512 bytes typically), UDP's speed advantage preferred. Zone transfers involve entire DNS database (large), requiring TCP's reliability and larger data capacity.

---

**Q25.** SCENARIO: Website works on WiFi but not on mobile data. Cause?
- A) Web server down
- B) DNS or routing issue specific to mobile carrier
- C) Browser problem
- D) SSL certificate

**Answer:** B
**Explanation:** Works on one network but not another indicates network-specific issue. Mobile carrier's DNS may not resolve correctly, or carrier blocking/routing issue. Test: ping/dig from mobile.

---

**Q26.** TROUBLESHOOT: Intermittent "Connection Reset by Peer" errors. Likely cause?
- A) DNS failure
- B) Server application crashing or firewall terminating connections
- C) Client browser issue
- D) SSL certificate expired

**Answer:** B
**Explanation:** "Connection Reset" (RST packet) means remote side abruptly closed connection. Causes: server crash, application error, firewall/IDS terminating connection, server overload.

---

**Q27.** OUTPUT QUESTION: HTTP response header shows:
```
Cache-Control: no-store
Pragma: no-cache
```
What does this mean?
- A) Page should be cached
- B) Page must not be cached anywhere
- C) Cache is full
- D) CDN is disabled

**Answer:** B
**Explanation:** no-store means don't store any part of response. no-cache (Pragma) for HTTP/1.0 compatibility. Used for sensitive data (banking, personal info) that shouldn't be cached.

---

**Q28.** SCENARIO: All users suddenly see "502 Bad Gateway". What happened?
- A) DNS failure
- B) Backend server down or not responding to reverse proxy/load balancer
- C) Client browser issue
- D) SSL certificate expired

**Answer:** B
**Explanation:** 502 Bad Gateway means reverse proxy/load balancer (Nginx, HAProxy) received invalid response or couldn't connect to backend application server. Check backend server status.

---

**Q29.** TROUBLESHOOT: DHCP clients getting 169.254.x.x addresses. What's wrong?
- A) DHCP server working normally
- B) DHCP server unreachable, clients using APIPA
- C) DNS misconfigured
- D) Network switch failure

**Answer:** B
**Explanation:** 169.254.x.x is APIPA (Automatic Private IP Addressing). Assigned when DHCP server can't be reached. Clients self-assign these addresses. Check DHCP server status, network connectivity.

---

**Q30.** INTERVIEW DEEP DIVE: Explain how HTTPS ensures security.
- A) It uses special ports
- B) TLS encrypts data, verifies server identity with certificates, ensures data integrity
- C) It's a different protocol from HTTP
- D) It uses firewalls

**Answer:** B
**Explanation:** HTTPS = HTTP + TLS. TLS provides: 1) Encryption (data can't be read by eavesdroppers), 2) Authentication (server certificate proves identity), 3) Integrity (data can't be modified in transit). Certificate signed by trusted CA, verified by browser.

---

## Score Interpretation

- **27-30:** Excellent! Interview-ready with strong troubleshooting skills
- **20-26:** Good. Practice more output-based analysis
- **15-19:** Fair. Review DNS, HTTP, and email protocols
- **Below 15:** Re-study Application Layer fundamentals

## Interview Preparation Tips

1. **Know complete flows** - URL to webpage, email delivery, DHCP process
2. **Understand DNS deeply** - Resolution process, record types, troubleshooting
3. **Memorize common ports** - Always asked in interviews
4. **Practice reading outputs** - dig, nslookup, browser DevTools, logs
5. **Know HTTP status codes** - 200, 301, 404, 500, 502, etc.
6. **Be ready to troubleshoot** - Step-by-step methodology for common issues
7. **Understand security** - TLS/SSL, certificates, HTTPS
