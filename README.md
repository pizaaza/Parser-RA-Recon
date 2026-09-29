# Parser RA Recon

Parser RA Recon (Risk Assessment Recon) is a cross-platform terminal-based OSINT framework for authorized audits, threat research, and open-source intelligence collection. It is designed to be lightweight, modular, and usable from both Windows and Linux terminals.

This project is intended for legitimate security assessment, audit workflows, and authorized research. It is not a defensive breach-prevention tool and should be used only on targets and datasets that the operator is legally allowed to analyze.

## Features

- Terminal UI dashboard with rich styling and startup ASCII banner
- Username scanning across public platforms
- Email exposure checks against public breach references
- IP geolocation and ISP analysis
- Domain WHOIS and DNS lookups
- Metadata extraction for public image URLs
- Phone number validation and formatting
- Username variational generation
- Breach alert summary and risk scoring
- Markdown report export
- Anti-rate-limiting request pacing and randomized user-agent selection

## Legal and Ethical Notice

Use this tool only in contexts that comply with local laws, organizational policies, and applicable privacy frameworks.

- authorized audits only
- no unauthorized access to private systems
- no mass abuse or harassment
- no targeting of personal data outside the scope of a lawful investigation
- no deceptive or malicious activity

If you do not have explicit authorization, do not use this project against a person, company, domain, or service.

## Project Goals

This project is focused on:

- reconnaissance support for vetted investigative workflows
- public data discovery for compliance and audit purposes
- triage and collection of open-source intelligence
- structured report generation for review and documentation

It is not intended to serve as a personal data breach monitoring service or a consumer safety tool.

## Requirements

Python 3.9+

Installed dependencies:

- requests
- rich

## Supported Platforms

The framework is structured to support modules such as:

- GitHub
- Reddit
- YouTube
- Twitch
- Twitter/X-style social profiles
- gaming-related directories
- public web domains
- image metadata checks

Some modules rely on publicly available endpoints and may require internet access and rate-aware request handling.

## Installation

### Windows

1. Open PowerShell or Command Prompt.
2. Clone the repository:

   git clone https://github.com/pizaaza/Parser-RA-Recon.git

3. Change into the project directory:

   cd Parser-RA-Recon

4. Create a virtual environment:

   python -m venv .venv

5. Activate the environment:

   .venv\Scripts\Activate.ps1

6. Install dependencies:

   python -m pip install --upgrade pip
   python -m pip install requests rich

### Linux / macOS

1. Open a terminal.
2. Clone the repository:

   git clone https://github.com/pizaaza/Parser-RA-Recon.git

3. Change into the project directory:

   cd Parser-RA-Recon

4. Create a virtual environment:

   python3 -m venv .venv

5. Activate it:

   source .venv/bin/activate

6. Install dependencies:

   python -m pip install --upgrade pip
   python -m pip install requests rich

## Running the Tool

From the project root, run:

python app.py

Or, if you are in a venv:

python app.py

The app will launch the Rich-based TUI menu and show the startup banner.

## Main Menu Options

1. Username Scanner
2. Email Analyzer
3. IP Analyzer
4. Domain OSINT
5. Metadata Analyzer
6. Phone Formatter
7. Username Permutator
8. Breach Summary Report
9. Exit

## Example Workflow

- Scan a username across social and gaming systems
- Check an email address against breach references
- Inspect a target IP for location and ISP metadata
- Review a domain for WHOIS and DNS hints
- Export report findings to Markdown

## Reporting

The app can export findings to Markdown reports in the reports folder. This produces a readable summary for audits, investigations, or team review.

## Project Structure

Parser-RA-Recon/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── parser_ra_recon/
│   ├── __init__.py
│   ├── config.py
│   ├── logging_utils.py
│   ├── request_manager.py
│   ├── tui.py
│   └── modules/
│       ├── __init__.py
│       ├── username_scanner.py
│       ├── email_analyzer.py
│       ├── ip_analyzer.py
│       ├── domain_osint.py
│       ├── metadata_analyzer.py
│       ├── phone_formatter.py
│       ├── permutator.py
│       └── reporting.py

## Notes

- This framework is intentionally modular so it can be extended with additional sources or custom checks.
- Many public sources have rate limits or access restrictions; the request manager includes pacing and random user-agent rotation to reduce blocking risk.
- Some modules are best-effort and depend on the availability and reliability of third-party public services.

## Disclaimer

This project is designed for legitimate audit, investigation, and public-data discovery scenarios under lawful authority. It is not a breach-prevention product and should not be interpreted as a security guarantee or protective monitoring service.

Use responsibly and within legal boundaries.
