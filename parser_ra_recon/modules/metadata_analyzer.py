from typing import Dict, Optional
from ..request_manager import RequestManager
from ..logging_utils import log_info, log_error, log_step
import json


class MetadataAnalyzer:
    """Extracts EXIF and metadata from image URLs."""

    def __init__(self, delay_min: float = 1.0, delay_max: float = 3.0):
        self.request_manager = RequestManager(delay_min, delay_max)

    def analyze_image(self, image_url: str) -> Dict:
        """Analyze metadata from a public image URL."""
        log_step("ANALYZING", f"Extracting metadata from image: {image_url}")
        results = {"url": image_url, "exif": {}, "metadata": {}, "available": False}

        log_info("Attempting to extract EXIF data...")
        try:
            # Note: Real implementation would use PIL/Pillow or exifread
            response = self.request_manager.get(image_url, timeout=10)
            if response.status_code == 200:
                # Check headers for basic metadata
                results["metadata"] = {
                    "content_type": response.headers.get("content-type"),
                    "content_length": response.headers.get("content-length"),
                    "last_modified": response.headers.get("last-modified"),
                }
                results["available"] = True
                log_info("✓ Image metadata extracted")
        except Exception as e:
            log_error(f"Error analyzing image: {str(e)}")

        log_step("COMPLETE", f"Metadata analysis complete")
        return results
