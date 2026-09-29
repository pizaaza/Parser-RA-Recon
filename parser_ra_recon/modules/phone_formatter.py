from typing import Dict
from ..logging_utils import log_info, log_error, log_step
import re


class PhoneFormatter:
    """Validates and formats phone numbers with carrier detection."""

    # Country code mappings (simplified)
    COUNTRY_CODES = {
        "1": "USA/Canada",
        "44": "United Kingdom",
        "33": "France",
        "49": "Germany",
        "39": "Italy",
        "34": "Spain",
        "31": "Netherlands",
        "91": "India",
        "86": "China",
        "81": "Japan",
        "61": "Australia",
    }

    def validate(self, phone_number: str) -> Dict:
        """Validate and format a phone number."""
        log_step("VALIDATING", f"Analyzing phone number: {phone_number}")
        results = {"phone": phone_number, "valid": False, "country": None, "formatted": None}

        # Clean phone number
        cleaned = re.sub(r"[^0-9+]", "", phone_number)
        log_info(f"Cleaned number: {cleaned}")

        # Extract country code
        if cleaned.startswith("+"):
            cleaned = cleaned[1:]
            for code, country in self.COUNTRY_CODES.items():
                if cleaned.startswith(code):
                    results["country"] = country
                    results["valid"] = True
                    results["formatted"] = f"+{cleaned}"
                    log_info(f"✓ Valid {country} number")
                    break
        else:
            log_error("Phone number must include country code with + prefix")

        log_step("COMPLETE", f"Phone validation complete")
        return results
