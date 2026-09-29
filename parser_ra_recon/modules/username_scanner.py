from typing import Dict, List, Optional
from ..request_manager import RequestManager
from ..logging_utils import log_info, log_error, log_step


class UsernameScanner:
    """Scans for username existence across multiple platforms."""

    def __init__(self, delay_min: float = 1.0, delay_max: float = 3.0):
        self.request_manager = RequestManager(delay_min, delay_max)
        self.platforms = {
            "github": {"url": "https://api.github.com/users/{}", "key": "login"},
            "reddit": {"url": "https://www.reddit.com/user/{}/about.json", "key": "name"},
            "twitter": {"url": "https://api.twitter.com/2/users/by/username/{}", "key": "username"},
            "youtube": {"url": "https://www.youtube.com/@{}", "check": "profile"},
            "twitch": {"url": "https://api.twitch.tv/kraken/users?login={}", "key": "name"},
        }

    def scan(self, username: str, sites: Optional[List[str]] = None) -> Dict:
        """Scan for username across specified platforms."""
        log_step("SCANNING", f"Looking up username '{username}' across platforms...")
        results = {"username": username, "found_on": [], "profiles": {}}

        targets = sites if sites else list(self.platforms.keys())

        for platform in targets:
            if platform not in self.platforms:
                log_error(f"Platform '{platform}' not supported")
                continue

            log_info(f"Checking {platform}...")
            try:
                platform_data = self.platforms[platform]
                url = platform_data["url"].format(username)
                response = self.request_manager.get(url, timeout=10)

                if response.status_code == 200:
                    results["found_on"].append(platform)
                    results["profiles"][platform] = {
                        "url": url,
                        "status": "found",
                        "data": response.json() if "json" in response.headers.get("content-type", "") else None,
                    }
                    log_info(f"✓ Found on {platform}")
                else:
                    results["profiles"][platform] = {"status": "not_found"}
            except Exception as e:
                log_error(f"Error checking {platform}: {str(e)}")
                results["profiles"][platform] = {"status": "error", "error": str(e)}

        log_step("COMPLETE", f"Found '{username}' on {len(results['found_on'])} platform(s)")
        return results
