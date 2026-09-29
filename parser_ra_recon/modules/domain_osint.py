from typing import Dict
from ..request_manager import RequestManager
from ..logging_utils import log_info, log_error, log_step


class DomainOSINT:
    """Performs OSINT on web domains using WHOIS and DNS data."""

    def __init__(self, delay_min: float = 1.0, delay_max: float = 3.0):
        self.request_manager = RequestManager(delay_min, delay_max)

    def lookup(self, domain: str) -> Dict:
        """Look up WHOIS and DNS information for a domain."""
        log_step("LOOKING UP", f"Querying WHOIS and DNS data for '{domain}'...")
        results = {"domain": domain, "whois": {}, "dns": {}, "nameservers": []}

        log_info("Fetching WHOIS information...")
        try:
            url = f"https://whois.arin.net/rest/net/{domain}/json"
            response = self.request_manager.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                results["whois"] = {
                    "registrar": data.get("handle"),
                    "description": data.get("comments"),
                }
                log_info("✓ WHOIS data retrieved")
        except Exception as e:
            log_error(f"Error fetching WHOIS: {str(e)}")

        log_info("Fetching DNS records...")
        try:
            url = f"https://dns.google/resolve?name={domain}"
            response = self.request_manager.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                results["dns"] = data.get("Answer", [])
                log_info(f"✓ Found {len(results['dns'])} DNS record(s)")
        except Exception as e:
            log_error(f"Error fetching DNS: {str(e)}")

        log_step("COMPLETE", f"Domain analysis complete for {domain}")
        return results
