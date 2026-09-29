# Quick Start Guide

## Setup (30 seconds)

### Windows

```bash
git clone https://github.com/pizaaza/Parser-RA-Recon.git
cd Parser-RA-Recon
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

### Linux/macOS

```bash
git clone https://github.com/pizaaza/Parser-RA-Recon.git
cd Parser-RA-Recon
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## First Run

The app starts with a banner and main menu:

```
┌─────────────────────────────────────────────────────────┐
│  Parser RA Recon - Risk Assessment OSINT Framework      │
│                                                         │
│  1. Username Scanner                                    ���
│  2. Email Analyzer                                      │
│  3. IP Analyzer                                         │
│  4. Domain OSINT                                        │
│  5. Metadata Analyzer                                   │
│  6. Phone Formatter                                     │
│  7. Username Permutator                                 │
│  8. Breach Summary Report                               │
│  9. Exit                                                │
└─────────────────────────────────────────────────────────┘
```

Select an option and follow the prompts.

## Common Tasks

### Check if a username exists across platforms

1. Select **1 - Username Scanner**
2. Enter the username
3. Choose category: `socials`, `gaming`, `news`, or `all`
4. Confirm if you want NSFW sites included
5. View results in the fox camera frame
6. Choose to export as Markdown

### Check if an email was in a breach

1. Select **2 - Email Analyzer**
2. Enter the email address
3. Tool queries public breach databases
4. View breach count and details
5. See automated risk score (LOW, MEDIUM, HIGH, CRITICAL)
6. Export findings if needed

### Find where an IP is located

1. Select **3 - IP Analyzer**
2. Enter the IP address
3. Get geolocation (country, city, timezone)
4. See ISP and ASN information
5. Check if flagged as VPN/Proxy

### Generate username variations

1. Select **7 - Username Permutator**
2. Enter base username
3. Set max variants (default 20)
4. Get list of permutations with prefixes, suffixes, numbers
5. Use for additional scanning or documentation

## Report Export

After each scan, you'll be prompted to export results as Markdown.

Reports are saved to the `reports/` directory with timestamps.

Example filenames:
- `username_scan_john_doe.md`
- `email_analysis_user@example.com.md`
- `ip_analysis_192.168.1.1.md`

## Rate Limiting

The tool automatically:

- Delays requests between 1-3 seconds (configurable in `config.py`)
- Randomizes User-Agent strings
- Respects API rate limits

This prevents blocking and reduces detection.

## Tips

- **Batch operations**: Run multiple scans and export all reports, then review together
- **Combine results**: Use permutator to generate variants, then scan each variant
- **Document findings**: Export Markdown reports for audit trails
- **Respect rate limits**: Don't scan the same target repeatedly in quick succession

## Troubleshooting

### "ModuleNotFoundError: No module named 'rich'"

Missing dependencies. Reinstall:

```bash
pip install -r requirements.txt
```

### API calls timing out or failing

Some external services may be rate-limited or temporarily unavailable. The tool will log errors clearly. Try again later.

### Reports directory not found

The app creates the `reports/` directory automatically on first export.

## Configuration

Edit `parser_ra_recon/config.py` to customize:

- Request delay range (min_delay, max_delay)
- Platform list by category
- Report export location

---

For detailed documentation, see [README.md](README.md)
