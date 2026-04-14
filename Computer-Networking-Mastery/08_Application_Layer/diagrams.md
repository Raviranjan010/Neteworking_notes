# Application Layer - Diagrams & Visual Guides

## 1. DNS Resolution Flow - Complete Step-by-Step

```
USER TYPES: www.example.com

┌─────────────────────────────────────────────────────────┐
│ STEP 1: BROWSER CACHE                                   │
│ "Do I have recent DNS record?"                          │
│                                                         │
│ YES → Use cached IP (FAST!)                             │
│ NO  → Continue to Step 2                                │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 2: OS CACHE                                        │
│ Check operating system DNS cache                        │
│ Windows: ipconfig /displaydns                           │
│ Linux: systemd-resolve --statistics                     │
│                                                         │
│ YES → Use cached IP                                     │
│ NO  → Continue to Step 3                                │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 3: HOSTS FILE                                      │
│ Check local hosts file for manual mappings              │
│ Windows: C:\Windows\System32\drivers\etc\hosts          │
│ Linux/Mac: /etc/hosts                                   │
│                                                         │
│ Found → Use it                                          │
│ NO    → Continue to Step 4                              │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 4: RECURSIVE DNS RESOLVER (ISP DNS)                │
│ Your computer → ISP DNS Server (8.8.8.8 or ISP DNS)     │
│                                                         │
│ Query (UDP port 53):                                    │
│ "What is IP address for www.example.com?"               │
│                                                         │
│ ISP DNS checks its cache...                             │
│ NOT FOUND → Must query other servers                    │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 5: ROOT DNS SERVER                                 │
│ ISP DNS → Root Server (13 clusters worldwide)           │
│                                                         │
│ Query: "Who handles .com domains?"                      │
│                                                         │
│ Root Server Response:                                   │
│ "I don't know www.example.com IP, but here are          │
│  the .com TLD name servers:"                            │
│ a.gtld-servers.net                                      │
│ b.gtld-servers.net                                      │
│ ... (13 total)                                          │
│                                                         │
│ Returns: NS records for .com TLD servers                │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 6: TLD (TOP LEVEL DOMAIN) SERVER                   │
│ ISP DNS → .com TLD Server                               │
│                                                         │
│ Query: "Who handles example.com?"                       │
│                                                         │
│ TLD Server Response:                                    │
│ "I don't know www.example.com IP, but here are          │
│  the authoritative servers for example.com:"            │
│ ns1.example.com (IP: 192.168.1.10)                     │
│ ns2.example.com (IP: 192.168.1.11)                     │
│                                                         │
│ Returns: NS records for example.com domain              │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 7: AUTHORITATIVE NAME SERVER                       │
│ ISP DNS → ns1.example.com                               │
│                                                         │
│ Query: "What is IP for www.example.com?"                │
│                                                         │
│ Authoritative Server Response:                          │
│ "www.example.com = 93.184.216.34"                       │
│                                                         │
│ Returns: A record with IP address                       │
│ TTL: 3600 seconds (cache for 1 hour)                    │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 8: RESPONSE BACK TO USER                           │
│ ISP DNS → Your Computer                                 │
│                                                         │
│ "www.example.com = 93.184.216.34"                       │
│                                                         │
│ Your computer caches this result (TTL: 3600s)           │
│ Browser receives IP address                             │
│                                                         │
│ DNS Resolution Complete!                                │
│ Total time: 20-100ms (if not cached anywhere)           │
└─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────┐
│ STEP 9: BROWSER CONNECTS TO WEB SERVER                  │
│ Now browser has IP: 93.184.216.34                       │
│                                                         │
│ TCP 3-way handshake → TLS handshake → HTTP request      │
│                                                         │
│ Web page loads!                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 2. HTTP Request-Response Cycle

```
SCENARIO: User visits https://www.example.com/products

CLIENT (Browser)                          SERVER (Nginx/Apache)
192.168.1.10:54321                        93.184.216.34:443
   │                                          │
   │  1. DNS Resolution                        │
   │  www.example.com → 93.184.216.34         │
   │                                          │
   │  2. TCP Handshake (Port 443)             │
   │  SYN ──────────────────────────────────▶│
   │  ◀──────────────────────────────────────│ SYN-ACK
   │  ACK ──────────────────────────────────▶│
   │                                          │
   │  3. TLS Handshake (HTTPS)                │
   │  ClientHello ──────────────────────────▶│
   │  ◀──────────────────────────────────────│ ServerHello + Certificate
   │  Key Exchange                            │
   │  ✓ Secure channel established            │
   │                                          │
   │  4. HTTP Request (Encrypted)             │
   │  ──────────────────────────────────────▶│
   │  GET /products HTTP/1.1                  │
   │  Host: www.example.com                   │
   │  User-Agent: Mozilla/5.0...              │
   │  Accept: text/html                       │
   │  Cookie: session_id=abc123               │
   │                                          │
   │                                          │ 5. Server Processing
   │                                          │ - Parse request
   │                                          │ - Check authentication
   │                                          │ - Query database
   │                                          │ - Generate HTML
   │                                          │
   │  6. HTTP Response (Encrypted)            │
   │  ◀──────────────────────────────────────│
   │  HTTP/1.1 200 OK                         │
   │  Content-Type: text/html                 │
   │  Content-Length: 12345                   │
   │  Cache-Control: max-age=3600             │
   │                                          │
   │  <!DOCTYPE html>                         │
   │  <html>                                  │
   │  <head><title>Products</title></head>    │
   │  <body>...products...</body>             │
   │  </html>                                 │
   │                                          │
   │  7. Browser Renders Page                 │
   │  - Parse HTML                            │
   │  - Find CSS, JS, images                  │
   │  - Make additional HTTP requests         │
   │  - Render visually                       │
   │  - Execute JavaScript                    │
   │                                          │
   │  [Additional requests for resources]     │
   │  GET /css/style.css ───────────────────▶│
   │  ◀──────────────────────────────────────│ 200 OK (CSS)
   │  GET /js/app.js ───────────────────────▶│
   │  ◀──────────────────────────────────────│ 200 OK (JS)
   │  GET /images/logo.png ─────────────────▶│
   │  ◀──────────────────────────────────────│ 200 OK (Image)
   │                                          │
   │  ✓ Page Fully Loaded!                    │
   │                                          │
   │  8. Connection Handling                  │
   │  Keep-alive (stay open for more)         │
   │  OR                                      │
   │  FIN (close connection)                  │
```

---

## 3. HTTPS/TLS Handshake Detail

```
CLIENT                              SERVER
   │                                  │
   │  ClientHello                     │
   │  - TLS versions supported        │
   │  - Cipher suites list            │
   │  - Client random number          │
   │  - Session ID (if resuming)      │
   │  ──────────────────────────────▶│
   │                                  │
   │                                  │ Select TLS version
   │                                  │ Select cipher suite
   │                                  │
   │  ServerHello                     │
   │  - Chosen TLS version            │
   │  - Chosen cipher suite           │
   │  - Server random number          │
   │  - Session ID                    │
   │  ◀──────────────────────────────│
   │                                  │
   │  Certificate                     │
   │  - Server's SSL certificate      │
   │  - Certificate chain             │
   │  - Signed by CA                  │
   │  ◀──────────────────────────────│
   │                                  │
   │  Certificate Verify              │
   │  - Is CA trusted?                │
   │  - Certificate valid?            │
   │  - Domain matches?               │
   │  - Not expired?                  │
   │  ✓ Certificate accepted          │
   │                                  │
   │  Key Exchange                    │
   │  - Premaster secret              │
   │  - Encrypted with server's       │
   │    public key                    │
   │  ──────────────────────────────▶│
   │                                  │
   │  Both sides generate             │
   │  session keys from:              │
   │  - Client random                 │
   │  - Server random                 │
   │  - Premaster secret              │
   │                                  │
   │  ChangeCipherSpec                │
   │  "Switch to encrypted"           │
   │  ──────────────────────────────▶│
   │  ◀──────────────────────────────│ ChangeCipherSpec
   │                                  │
   │  Finished (encrypted)            │
   │  ──────────────────────────────▶│
   │  ◀──────────────────────────────│ Finished (encrypted)
   │                                  │
   │  ✓ Secure connection ready!      │
   │  All subsequent data encrypted   │
   │                                  │
   │  [HTTP Request (encrypted)]      │
   │  ──────────────────────────────▶│
   │  [HTTP Response (encrypted)]     │
   │  ◀──────────────────────────────│
```

---

## 4. Email Flow - Complete Journey

```
SENDER (Gmail)                    SMTP Servers                    RECIPIENT (Yahoo)
user@gmail.com                                                    user@yahoo.com
   │                                 │                                 │
   │  1. Compose Email               │                                 │
   │  To: user@yahoo.com             │                                 │
   │  Subject: Hello!                │                                 │
   │  [Click Send]                   │                                 │
   │                                 │                                 │
   │  2. SMTP to Gmail Server        │                                 │
   │  (Port 587 with auth)           │                                 │
   │  ─────────────────────────────▶│                                 │
   │  EHLO, AUTH, MAIL FROM,         │                                 │
   │  RCPT TO, DATA                  │                                 │
   │  Email queued on Gmail server   │                                 │
   │                                 │                                 │
   │                                 │  3. DNS MX Lookup               │
   │                                 │  Query: MX record for yahoo.com │
   │                                 │                                 │
   │                                 │  Response:                      │
   │                                 │  mta5.am0.yahoodns.net          │
   │                                 │  mta6.am0.yahoodns.net          │
   │                                 │                                 │
   │                                 │  4. SMTP Server-to-Server       │
   │                                 │  (Port 25)                      │
   │                                 │  ─────────────────────────────▶│
   │                                 │  EHLO, MAIL FROM,               │
   │                                 │  RCPT TO, DATA                  │
   │                                 │                                 │
   │                                 │                                 │ 5. Email Storage
   │                                 │                                 │ Yahoo stores in
   │                                 │                                 │ user's mailbox
   │                                 │                                 │
   │                                 │                                 │ 6. Email Retrieval
   │                                 │                                 │ User opens Yahoo Mail
   │                                 │                                 │ IMAP sync (Port 143)
   │                                 │                                 │ or POP3 (Port 110)
   │                                 │                                 │                                 │
   │                                 │                                 │ Email appears in inbox!
   │                                 │                                 │
   ✓ Email Sent!                     ✓ Email Delivered!                ✓ Email Received!
```

---

## 5. DHCP DORA Process

```
CLIENT (Laptop)                     DHCP SERVER
No IP Address Yet                   192.168.1.1
MAC: AA:BB:CC:11:22:33              Port: 67
Port: 68
   │                                  │
   │  D - DISCOVER (Broadcast)        │
   │  "Is there a DHCP server?"       │
   │                                  │
   │  Source IP: 0.0.0.0             │
   │  Dest IP: 255.255.255.255       │
   │  (Broadcast to entire network)   │
   │                                  │
   │  ──────────────────────────────▶│
   │  Client MAC: AA:BB:CC:11:22:33  │
   │  "Requesting IP configuration"   │
   │                                  │
   │                                  │ Server receives Discover
   │                                  │ Checks available IP pool
   │                                  │ Selects: 192.168.1.100
   │                                  │
   │  O - OFFER                       │
   │  ◀──────────────────────────────│
   │                                  │
   │  "I can offer you:"              │
   │  IP: 192.168.1.100               │
   │  Mask: 255.255.255.0             │
   │  Gateway: 192.168.1.1            │
   │  DNS: 8.8.8.8                    │
   │  Lease: 24 hours                 │
   │                                  │
   │  R - REQUEST (Broadcast)         │
   │  "I accept the offer!"           │
   │  ──────────────────────────────▶│
   │                                  │
   │  (Broadcast so other DHCP        │
   │   servers know offer accepted)   │
   │                                  │
   │                                  │ Server marks IP as allocated
   │                                  │
   │  A - ACKNOWLEDGMENT              │
   │  ◀──────────────────────────────│
   │                                  │
   │  "Acknowledged!"                 │
   │  "192.168.1.100 is yours"        │
   │  Lease starts now                │
   │                                  │
   │  Client configures interface     │
   │  with received settings          │
   │                                  │
   │  ✓ Network Ready!                │
   │  IP: 192.168.1.100               │
   │  Can now communicate on network  │
   │                                  │
   
LEASE RENEWAL TIMELINE:
0h        12h (50%)        21h (87.5%)     24h (100%)
│──────────│──────────────────│──────────────│
Obtained   T1 Timer          T2 Timer       Expired
           Renew from        Broadcast      Must renew
           original server   any server     or lose IP
```

---

## 6. HTTP Methods & Status Codes

```
HTTP METHODS:
┌─────────────────────────────────────────────────────┐
│ GET     → Retrieve data (safe, idempotent)          │
│         Example: GET /products                      │
│                                                      │
│ POST    → Submit data / Create resource             │
│         Example: POST /users (create new user)      │
│                                                      │
│ PUT     → Update/replace entire resource            │
│         Example: PUT /users/123 (replace user 123)  │
│                                                      │
│ PATCH   → Partial update                            │
│         Example: PATCH /users/123 (update email)    │
│                                                      │
│ DELETE  → Remove resource                           │
│         Example: DELETE /users/123                  │
│                                                      │
│ HEAD    → Get headers only (no body)                │
│         Example: Check if page exists               │
│                                                      │
│ OPTIONS → Get supported methods                     │
│         Example: CORS preflight                     │
└─────────────────────────────────────────────────────┘

HTTP STATUS CODES:
┌─────────────────────────────────────────────────────┐
│ 1xx - Informational                                 │
│     100 Continue                                    │
│                                                      │
│ 2xx - Success                                       │
│     200 OK (successful GET)                         │
│     201 Created (successful POST)                   │
│     204 No Content (successful DELETE)              │
│                                                      │
│ 3xx - Redirection                                   │
│     301 Moved Permanently                           │
│     302 Found (temporary redirect)                  │
│     304 Not Modified (use cache)                    │
│                                                      │
│ 4xx - Client Error                                  │
│     400 Bad Request                                 │
│     401 Unauthorized (need authentication)          │
│     403 Forbidden (access denied)                   │
│     404 Not Found                                   │
│     405 Method Not Allowed                          │
│                                                      │
│ 5xx - Server Error                                  │
│     500 Internal Server Error                       │
│     502 Bad Gateway                                 │
│     503 Service Unavailable                         │
│     504 Gateway Timeout                             │
└─────────────────────────────────────────────────────┘
```

---

## 7. DNS Record Types Visual Guide

```
DNS RECORD TYPES:

A Record (Address):
┌──────────────────────────────────┐
│ www.example.com → 93.184.216.34  │
│ Maps domain to IPv4 address      │
└──────────────────────────────────┘

AAAA Record (IPv6 Address):
┌──────────────────────────────────────────────┐
│ www.example.com → 2606:2800:220:1:248:...   │
│ Maps domain to IPv6 address                  │
└──────────────────────────────────────────────┘

CNAME Record (Canonical Name):
┌──────────────────────────────────┐
│ www.example.com → example.com    │
│ Alias to another domain          │
│ (Points to A record of target)   │
└──────────────────────────────────┘

MX Record (Mail Exchange):
┌──────────────────────────────────┐
│ example.com → mail.example.com   │
│ Priority: 10                     │
│ Specifies mail server(s)         │
└──────────────────────────────────┘

NS Record (Name Server):
┌──────────────────────────────────┐
│ example.com → ns1.example.com    │
│ Specifies authoritative DNS      │
└──────────────────────────────────┘

TXT Record (Text):
┌──────────────────────────────────┐
│ "v=spf1 include:_spf.google.com"│
│ SPF, DKIM, verification strings  │
└──────────────────────────────────┘

SOA Record (Start of Authority):
┌──────────────────────────────────┐
│ Primary NS, admin email,         │
│ serial, refresh, retry, expire   │
│ Zone administration info         │
└──────────────────────────────────┘

PTR Record (Pointer):
┌──────────────────────────────────┐
│ 34.216.184.93.in-addr.arpa       │
│ → www.example.com                │
│ Reverse DNS (IP to name)         │
└──────────────────────────────────┘
```

---

## 8. Application Layer Troubleshooting Flowchart

```
PROBLEM: Website Not Loading
         │
         ▼
┌─────────────────────────────┐
│ Step 1: DNS Resolution      │
│ nslookup domain.com         │
│ dig domain.com              │
└────────┬────────────────────┘
         │
    ┌────┴────┐
   Success   Fail → DNS issue!
    │          Check DNS servers
    │          Check domain expiry
    ▼
┌─────────────────────────────┐
│ Step 2: Network Reachability│
│ ping server_ip              │
└────────┬────────────────────┘
         │
    ┌────┴────┐
   Success   Fail → Network issue!
    │          Check routing, firewall
    ▼
┌─────────────────────────────┐
│ Step 3: Port Connectivity   │
│ telnet server_ip 80         │
│ nc -zv server_ip 443        │
└────────┬────────────────────┘
         │
    ┌────┴────┐
   Success   Fail → Service down or
    │          firewall blocking
    ▼
┌─────────────────────────────┐
│ Step 4: HTTP Request        │
│ curl -v https://domain.com  │
│ Check response code         │
└────────┬────────────────────┘
         │
    What response?
         │
    ┌────┼────────────┐
    │    │            │
    ▼    ▼            ▼
  200   4xx         5xx
  OK    Client      Server
  │     Error       Error
  │     │            │
  ▼     ▼            ▼
Works  Check       Check
but    request,    server
slow   auth,       logs,
       perms       backend
```

---

## 9. Quick Reference Tables

### Table 1: Common Application Layer Protocols

```
┌──────────┬──────┬──────┬──────────────────────────────────┐
│ Protocol │ Port │ Proto│ Description                      │
├──────────┼──────┼──────┼──────────────────────────────────┤
│ HTTP     │ 80   │ TCP  │ Web browsing (unencrypted)       │
│ HTTPS    │ 443  │ TCP  │ Web browsing (TLS encrypted)     │
│ DNS      │ 53   │ UDP  │ Name resolution                  │
│ DHCP     │ 67/68│ UDP  │ IP auto-configuration            │
│ SMTP     │ 25   │ TCP  │ Email transfer (server-to-server)│
│ SMTP     │ 587  │ TCP  │ Email submission (client-to-srv) │
│ POP3     │ 110  │ TCP  │ Email retrieval (download)       │
│ IMAP     │ 143  │ TCP  │ Email retrieval (sync)           │
│ FTP      │ 21   │ TCP  │ File transfer (control)          │
│ FTP      │ 20   │ TCP  │ File transfer (data)             │
│ SSH      │ 22   │ TCP  │ Secure remote access             │
│ Telnet   │ 23   │ TCP  │ Remote access (unencrypted)      │
│ NTP      │ 123  │ UDP  │ Time synchronization             │
│ SNMP     │ 161  │ UDP  │ Network monitoring               │
│ RDP      │ 3389 │ TCP  │ Remote Desktop Protocol          │
└──────────┴──────┴──────┴──────────────────────────────────┘
```

### Table 2: Browser Loading Timeline

```
┌─────────────────────────────────────────────────────────┐
│ TYPICAL WEB PAGE LOAD TIMELINE                          │
├─────────────────────────────────────────────────────────┤
│ 0ms     - User types URL                                │
│ 0-50ms  - DNS resolution (if not cached)                │
│ 50-100ms - TCP handshake (3-way)                        │
│ 100-150ms - TLS handshake (HTTPS)                       │
│ 150-200ms - HTTP request sent                           │
│ 200-500ms - Server processing                           │
│ 500-600ms - HTTP response received (TTFB)               │
│ 600-2000ms - Download HTML, CSS, JS, images             │
│ 2000-3000ms - Browser rendering                         │
│ 3000ms+ - JavaScript execution, page interactive        │
│                                                         │
│ TOTAL: 1-5 seconds (depends on page complexity)         │
└─────────────────────────────────────────────────────────┘
```

---

## Quick Reference Summary

```
┌──────────────────────────────────────────────────┐
│      APPLICATION LAYER CHEATSHEET                │
├──────────────────────────────────────────────────┤
│ DNS: Names → IPs (hierarchical resolution)      │
│ HTTP: Web requests (GET, POST, PUT, DELETE)     │
│ HTTPS: HTTP + TLS encryption (port 443)         │
│ SMTP: Send email (port 25, 587)                 │
│ POP3/IMAP: Retrieve email (110/143)             │
│ DHCP: Auto IP assignment (DORA process)         │
│                                                  │
│ DNS Records: A, AAAA, CNAME, MX, NS, TXT       │
│ HTTP Codes: 200 OK, 404 Not Found, 500 Error   │
│                                                  │
│ URL Load: DNS → TCP → TLS → HTTP → Render      │
│ Email Flow: SMTP → MX → SMTP → IMAP/POP3       │
│                                                  │
│ Troubleshoot: nslookup, dig, curl, telnet       │
└──────────────────────────────────────────────────┘
```
