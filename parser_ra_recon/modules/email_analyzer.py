from typing import Dict, Optional
from ..request_manager import RequestManager
from ..logging_utils import log_info, log_error, log_step


class EmailAnalyzer:
    """Checks if an email has been exposed in public data breaches."""

    def __init__(self, delay_min: float = 1.0, delay_max: float = 3.0):
        self.request_manager = RequestManager(delay_min, delay_max)
        self.breach_sources = [
            {"name": "Have I Been Pwned", "url": "https://haveibeenpwned.com/api/v3/breachedaccount/{}"},
            {"name": "Hunter.io", "url": "https://api.hunter.io/v2/email-verifier"},
        ]

    def check_email(self, email: str) -> Dict:
        """Check if email appears in public breach data."""
        log_step("ANALYZING", f"Checking email '{email}' against breach databases...")
        results = {"email": email, "breaches_found": 0, "breach_data": [], "verified": False}

        # Check Have I Been Pwned
        log_info("Querying Have I Been Pwned database...")
        try:
            url = self.breach_sources[0]["url"].format(email)
            response = self.request_manager.get(url, timeout=10)
            if response.status_code == 200:
                breaches = response.json()
                results["breaches_found"] += len(breaches)
                for breach in breaches:
                    results["breach_data"].append({
                        "source": breach.get("Name"),
                        "date": breach.get("BreachDate"),
                        "exposed_data": breach.get("DataClasses"),
                    })
                log_info(f"⚠ Email exposed in {len(breaches)} breach(es)")
            else:
                log_info("✓ Email not found in Have I Been Pwned")
        except Exception as e:
            log_error(f"Error checking Have I Been Pwned: {str(e)}")

        log_step("COMPLETE", f"Email analysis complete. Found in {results['breaches_found']} breach(es)")
        return results
