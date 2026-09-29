from typing import Dict, Optional
from ..request_manager import RequestManager
from ..logging_utils import log_info, log_error, log_step


class IPAnalyzer:
    """Analyzes IP addresses for geolocation, ISP, and VPN/Proxy detection."""

    def __init__(self, delay_min: float = 1.0, delay_max: float = 3.0):
        self.request_manager = RequestManager(delay_min, delay_max)
        self.sources = [
            {"name": "ip-api.com", "url": "http://ip-api.com/json/{}"},
            {"name": "ipapi.co", "url": "https://ipapi.co/{}/json/"},
        ]

    def analyze(self, ip_address: str) -> Dict:
        """Analyze IP address for geolocation and metadata."""
        log_step("ANALYZING", f"Pulling metadata for IP '{ip_address}'...")
        results = {"ip": ip_address, "geolocation": {}, "isp": {}, "vpn_proxy": False}

        log_info("Querying IP geolocation databases...")
        try:
            url = self.sources[0]["url"].format(ip_address)
            response = self.request_manager.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                results["geolocation"] = {
                    "country": data.get("country"),
                    "city": data.get("city"),
                    "region": data.get("regionName"),
                    "latitude": data.get("lat"),
                    "longitude": data.get("lon"),
                    "timezone": data.get("timezone"),
                }
                results["isp"] = {
                    "org": data.get("org"),
                    "isp": data.get("isp"),
                    "asn": data.get("as"),
                }
                results["vpn_proxy"] = data.get("proxy", False)
                log_info(f"✓ Located in {results['geolocation']['city']}, {results['geolocation']['country']}")
                if results["vpn_proxy"]:
                    log_info(f"⚠ This IP is flagged as a VPN/Proxy node")
        except Exception as e:
            log_error(f"Error analyzing IP: {str(e)}")

        log_step("COMPLETE", f"IP analysis complete for {ip_address}")
        return results
