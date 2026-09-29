# Usage Examples

## Scenario 1: Investigating a Suspicious Username

**Goal**: Find where a username appears online and what platforms host accounts under that name.

**Steps**:

1. Launch the app: `python app.py`
2. Select **1 - Username Scanner**
3. Enter username: `alice_security`
4. Select category: **socials** (Twitter, Reddit, YouTube, GitHub, etc.)
5. Include NSFW: **No**
6. Tool queries platforms and reports results:
   ```
   ┌──────────────────────────────────┐
   │ 🦊 USERNAME SCAN - alice_security │
   ├──────────────────────────────────┤
   │ username: alice_security          │
   │ found_on: github, reddit, youtube │
   │ profiles:                         │
   │   github: Found, profile URL      │
   │   reddit: Found, u/alice_security │
   │   youtube: Not found              │
   └──────────────────────────────────┘
   ```
7. Export to Markdown for documentation

---

## Scenario 2: Email Breach Check

**Goal**: Check if an email address appears in public breach databases.

**Steps**:

1. Select **2 - Email Analyzer**
2. Enter email: `contact@company.com`
3. Tool queries Have I Been Pwned and other sources
4. Results show:
   ```
   ┌─────────────────────────────────┐
   │ 🦊 EMAIL ANALYSIS               │
   ├─────────────────────────────────┤
   │ email: contact@company.com      │
   │ breaches_found: 2               │
   │ breach_data:                    │
   │   - source: LinkedIn            │
   │     date: 2021-06-22            │
   │   - source: Dropbox             │
   │     date: 2012-07-01            │
   └─────────────────────────────────┘
   ```
5. Auto-generated risk summary:
   ```
   RISK LEVEL: MEDIUM
   RECOMMENDATION: Email exposed in 2 breaches.
   Consider password changes on affected services.
   ```
6. Export findings

---

## Scenario 3: IP Geolocation Lookup

**Goal**: Determine the physical location and ISP of an IP address.

**Steps**:

1. Select **3 - IP Analyzer**
2. Enter IP: `8.8.8.8`
3. Tool queries geolocation services
4. Results:
   ```
   ┌─────────────────────────────────┐
   │ 🦊 IP ANALYSIS - 8.8.8.8        │
   ├─────────────────────────────────┤
   │ geolocation:                    │
   │   country: United States        │
   │   city: Mountain View           │
   │   region: California            │
   │   latitude: 37.386              │
   │   longitude: -122.084           │
   │   timezone: America/Los_Angeles │
   │ isp:                            │
   │   org: Google LLC               │
   │   isp: Google Public DNS        │
   │   asn: AS15169                  │
   │ vpn_proxy: False                │
   └─────────────────────────────────┘
   ```

---

## Scenario 4: Domain Intelligence Gathering

**Goal**: Gather WHOIS and DNS information about a domain.

**Steps**:

1. Select **4 - Domain OSINT**
2. Enter domain: `example.org`
3. Tool retrieves WHOIS and DNS records
4. Results include:
   - WHOIS registrar and contact info
   - DNS A, MX, NS records
   - Nameserver configuration
5. Export for audit documentation

---

## Scenario 5: Username Permutation for Extended Scanning

**Goal**: Generate alternative username variations to find accounts you might have missed.

**Steps**:

1. Select **7 - Username Permutator**
2. Enter base username: `john_doe`
3. Max variants: `30`
4. Tool generates variations:
   ```
   john_doe (original)
   john_doe_ (with underscore)
   john_doe. (with period)
   john_doe123 (with numbers)
   the_john_doe (with prefix)
   official_john_doe
   JOHN_DOE (uppercase)
   John_Doe (capitalized)
   ```
5. Take these variants and manually scan key platforms
6. Use results for follow-up investigation

---

## Scenario 6: Complete Audit Report Generation

**Goal**: Run multiple scans and compile findings into a single audit report.

**Steps**:

1. Run **Username Scanner** → Export to Markdown
2. Run **Email Analyzer** → Export to Markdown
3. Run **IP Analyzer** → Export to Markdown
4. Run **Domain OSINT** → Export to Markdown
5. Manually combine reports or create a summary document
6. All .md files are in `reports/` directory with timestamps

Example structure:
```
reports/
├── username_scan_suspect_2026-09-29_143022.md
├── email_analysis_suspect@email.com_2026-09-29_143040.md
├── ip_analysis_192.168.0.1_2026-09-29_143055.md
└── domain_osint_example.com_2026-09-29_143112.md
```

---

## Scenario 7: Phone Number Validation

**Goal**: Validate and extract country/carrier information from a phone number.

**Steps**:

1. Select **6 - Phone Formatter**
2. Enter phone: `+1 (555) 123-4567`
3. Tool cleans and validates:
   ```
   ┌──────────────────────────┐
   │ 🦊 PHONE VALIDATION      │
   ├──────────────────────────┤
   │ phone: +15551234567      │
   │ valid: True              │
   │ country: USA/Canada      │
   │ formatted: +15551234567  │
   └──────────────────────────┘
   ```

---

## Tips for Effective Use

1. **Always document**: Export every scan to build an audit trail
2. **Use categories**: Filter by `socials`, `gaming`, `news` to reduce noise
3. **Cross-reference**: Combine results from multiple modules for better context
4. **Respect delays**: The tool auto-throttles; don't bypass it
5. **Legal scope**: Only scan targets you have authorization to investigate

---

For more details, see [README.md](README.md) and [QUICKSTART.md](QUICKSTART.md)
