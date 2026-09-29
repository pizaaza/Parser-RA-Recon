from typing import List
from ..logging_utils import log_info, log_step


class UsernamePermutator:
    """Generates alternative variations of a username for discovery."""

    def __init__(self):
        self.suffixes = ["_", ".", "-", "123", "2024", "admin", "dev", "test"]
        self.prefixes = ["the_", "official_", "real_", "_", "mr_"]

    def generate_variants(self, username: str, max_variants: int = 20) -> List[str]:
        """Generate variations of a username."""
        log_step("GENERATING", f"Creating username variants for '{username}'...")
        variants = [username]  # Include original

        # Add suffix variants
        for suffix in self.suffixes:
            if len(variants) < max_variants:
                variants.append(f"{username}{suffix}")

        # Add prefix variants
        for prefix in self.prefixes:
            if len(variants) < max_variants:
                variants.append(f"{prefix}{username}")

        # Add case variants
        if len(variants) < max_variants:
            variants.append(username.upper())
        if len(variants) < max_variants:
            variants.append(username.capitalize())

        # Add number variants
        for num in ["1", "2", "3", "22", "69", "420"]:
            if len(variants) < max_variants:
                variants.append(f"{username}{num}")

        log_info(f"Generated {len(variants)} variant(s)")
        return variants[:max_variants]
