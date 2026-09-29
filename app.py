#!/usr/bin/env python3
"""
Parser RA Recon - Cross-Platform OSINT Framework
Risk Assessment reconnaissance tool for security professionals.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from parser_ra_recon.logging_utils import print_banner, log_info, log_error, log_step
from parser_ra_recon.tui import TUIInterface
from parser_ra_recon.modules.username_scanner import UsernameScanner
from parser_ra_recon.modules.email_analyzer import EmailAnalyzer
from parser_ra_recon.modules.ip_analyzer import IPAnalyzer
from parser_ra_recon.modules.domain_osint import DomainOSINT
from parser_ra_recon.modules.metadata_analyzer import MetadataAnalyzer
from parser_ra_recon.modules.phone_formatter import PhoneFormatter
from parser_ra_recon.modules.permutator import UsernamePermutator
from parser_ra_recon.modules.reporting import ReportGenerator
from parser_ra_recon.config import settings


class ParserRARecon:
    """Main application controller."""

    def __init__(self):
        self.tui = TUIInterface()
        self.username_scanner = UsernameScanner()
        self.email_analyzer = EmailAnalyzer()
        self.ip_analyzer = IPAnalyzer()
        self.domain_osint = DomainOSINT()
        self.metadata_analyzer = MetadataAnalyzer()
        self.phone_formatter = PhoneFormatter()
        self.permutator = UsernamePermutator()
        self.report_generator = ReportGenerator()
        self.findings = {}

    def run(self):
        """Main application loop."""
        print_banner()
        log_step("STARTED", "Parser RA Recon framework initialized")
        log_info("Ready to perform reconnaissance operations")

        while True:
            choice = self.tui.show_main_menu()

            if choice == "1":
                self.handle_username_scanner()
            elif choice == "2":
                self.handle_email_analyzer()
            elif choice == "3":
                self.handle_ip_analyzer()
            elif choice == "4":
                self.handle_domain_osint()
            elif choice == "5":
                self.handle_metadata_analyzer()
            elif choice == "6":
                self.handle_phone_formatter()
            elif choice == "7":
                self.handle_permutator()
            elif choice == "8":
                self.handle_breach_summary()
            elif choice == "9":
                log_step("SHUTDOWN", "Exiting Parser RA Recon")
                break

    def handle_username_scanner(self):
        """Handle username scanner operation."""
        try:
            username, category, nsfw = self.tui.show_username_scanner_menu()
            sites = self._get_sites_for_category(category, nsfw)
            
            log_step("SCANNING", f"Initiating username scan for '{username}'")
            results = self.username_scanner.scan(username, sites)
            
            self.findings["username_scan"] = results
            self.tui.display_results(results, f"USERNAME SCAN - {username}")
            
            self._ask_export(results, f"username_scan_{username}")
        except Exception as e:
            log_error(f"Username scanner error: {str(e)}")
        
        self.tui.pause()

    def handle_email_analyzer(self):
        """Handle email analyzer operation."""
        try:
            email = self.tui.show_email_analyzer_menu()
            
            log_step("ANALYZING", f"Checking email '{email}' against breach databases")
            results = self.email_analyzer.check_email(email)
            
            self.findings["email_analysis"] = results
            self.tui.display_results(results, f"EMAIL ANALYSIS - {email}")
            
            # Generate breach summary
            breach_summary = self.report_generator.generate_breach_summary(results)
            self.tui.display_results(breach_summary, f"BREACH SUMMARY - {email}")
            
            self._ask_export(results, f"email_analysis_{email}")
        except Exception as e:
            log_error(f"Email analyzer error: {str(e)}")
        
        self.tui.pause()

    def handle_ip_analyzer(self):
        """Handle IP analyzer operation."""
        try:
            ip_address = self.tui.show_ip_analyzer_menu()
            
            log_step("ANALYZING", f"Pulling geolocation and ISP data for {ip_address}")
            results = self.ip_analyzer.analyze(ip_address)
            
            self.findings["ip_analysis"] = results
            self.tui.display_results(results, f"IP ANALYSIS - {ip_address}")
            
            self._ask_export(results, f"ip_analysis_{ip_address}")
        except Exception as e:
            log_error(f"IP analyzer error: {str(e)}")
        
        self.tui.pause()

    def handle_domain_osint(self):
        """Handle domain OSINT operation."""
        try:
            domain = self.tui.show_domain_osint_menu()
            
            log_step("LOOKING UP", f"Querying WHOIS and DNS information for {domain}")
            results = self.domain_osint.lookup(domain)
            
            self.findings["domain_osint"] = results
            self.tui.display_results(results, f"DOMAIN OSINT - {domain}")
            
            self._ask_export(results, f"domain_osint_{domain}")
        except Exception as e:
            log_error(f"Domain OSINT error: {str(e)}")
        
        self.tui.pause()

    def handle_metadata_analyzer(self):
        """Handle metadata analyzer operation."""
        try:
            image_url = self.tui.show_metadata_analyzer_menu()
            
            log_step("ANALYZING", "Extracting EXIF and metadata from image")
            results = self.metadata_analyzer.analyze_image(image_url)
            
            self.findings["metadata_analysis"] = results
            self.tui.display_results(results, "IMAGE METADATA ANALYSIS")
            
            self._ask_export(results, "metadata_analysis")
        except Exception as e:
            log_error(f"Metadata analyzer error: {str(e)}")
        
        self.tui.pause()

    def handle_phone_formatter(self):
        """Handle phone formatter operation."""
        try:
            phone = self.tui.show_phone_formatter_menu()
            
            log_step("VALIDATING", "Analyzing phone number")
            results = self.phone_formatter.validate(phone)
            
            self.findings["phone_validation"] = results
            self.tui.display_results(results, "PHONE VALIDATION")
            
            self._ask_export(results, "phone_validation")
        except Exception as e:
            log_error(f"Phone formatter error: {str(e)}")
        
        self.tui.pause()

    def handle_permutator(self):
        """Handle username permutator operation."""
        try:
            username, max_variants = self.tui.show_permutator_menu()
            
            log_step("GENERATING", f"Creating username variants for '{username}'")
            variants = self.permutator.generate_variants(username, max_variants)
            
            results = {"base_username": username, "variants": variants}
            self.findings["permutation"] = results
            self.tui.display_results(results, "USERNAME PERMUTATIONS")
            
            self._ask_export(results, f"permutator_{username}")
        except Exception as e:
            log_error(f"Permutator error: {str(e)}")
        
        self.tui.pause()

    def handle_breach_summary(self):
        """Handle breach summary report generation."""
        if "email_analysis" not in self.findings:
            log_error("No email analysis data available. Run Email Analyzer first.")
            self.tui.pause()
            return
        
        try:
            breach_summary = self.report_generator.generate_breach_summary(
                self.findings["email_analysis"]
            )
            self.tui.display_results(breach_summary, "BREACH ALERT SUMMARY")
        except Exception as e:
            log_error(f"Breach summary error: {str(e)}")
        
        self.tui.pause()

    def _get_sites_for_category(self, category: str, include_nsfw: bool) -> list:
        """Get platform list based on category."""
        sites = []
        if category == "all":
            sites = [
                "github", "reddit", "twitter", "youtube", "twitch",
                "steamcommunity", "epicgames", "news.ycombinator"
            ]
        else:
            category_map = {
                "socials": ["github", "reddit", "twitter", "youtube", "twitch"],
                "gaming": ["steamcommunity", "epicgames"],
                "news": ["news.ycombinator"],
            }
            sites = category_map.get(category, [])
        
        if include_nsfw:
            sites.extend(["pornhub", "xvideos"])
        
        return sites

    def _ask_export(self, results: dict, filename_base: str):
        """Ask user if they want to export results."""
        from rich.prompt import Confirm
        if Confirm.ask("[bold cyan]Export results to Markdown?[/]", default=True):
            markdown = self.report_generator.generate_markdown(results, filename_base)
            filepath = self.report_generator.save_report(markdown, f"{filename_base}.md")
            if filepath:
                log_info(f"Report saved to {filepath}")


def main():
    """Entry point."""
    try:
        app = ParserRARecon()
        app.run()
    except KeyboardInterrupt:
        log_error("\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        log_error(f"Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
