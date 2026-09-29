# Configuration Guide

## Overview

Parser RA Recon is configured via `parser_ra_recon/config.py`. You can adjust request delays, platform lists, and reporting options.

## Default Settings

### Request Throttling

```python
min_delay: float = 1.0  # Minimum seconds between requests
max_delay: float = 3.0  # Maximum seconds between requests
```

The tool randomly selects a delay within this range for each request to:
- Avoid detection as automated scraping
- Respect API rate limits
- Reduce the risk of being blocked

**Recommendation**: Keep at least 1-3 seconds. Shorter delays increase blocking risk.

### User-Agent Rotation

The tool maintains a list of realistic browser User-Agent strings:

```python
user_agents: List[str] = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36...",
    # ... more agents
]
```

Each request uses a random UA from this list to appear as different browsers.

### Platform Categories

```python
default_sites: Dict[str, List[str]] = {
    "socials": ["github.com", "reddit.com", "x.com", "youtube.com", ...],
    "gaming": ["steamcommunity.com", "epicgames.com", ...],
    "news": ["news.ycombinator.com", "techcrunch.com", ...],
    "nsfw": ["pornhub.com", "xvideos.com", ...],
}
```

Use these categories in the Username Scanner to focus scanning:

- `--socials`: Social media platforms only
- `--gaming`: Gaming platforms only
- `--news`: News aggregators only
- `--all`: All platforms
- `--nsfw`: Include adult sites (opt-in)

### Report Export Directory

```python
export_dir: str = "reports"
```

All Markdown reports are saved to this directory. It's created automatically if it doesn't exist.

## Customization Examples

### Example 1: Increase Request Delays (Stealth)

If you're concerned about rate limiting, increase delays:

```python
# In parser_ra_recon/config.py
min_delay: float = 3.0
max_delay: float = 8.0  # 3-8 second delays
```

### Example 2: Add Custom Platforms

Add a new platform to the scanner:

```python
default_sites: Dict[str, List[str]] = {
    "socials": [
        "github.com",
        "reddit.com",
        "mastodon.social",  # Add Mastodon
        # ...
    ],
}
```

Then update `parser_ra_recon/modules/username_scanner.py` to add the lookup logic for the new platform.

### Example 3: Custom Report Directory

```python
export_dir: str = "/var/audit/osint_reports"  # Custom path
```

### Example 4: Remove NSFW Category

If you don't need NSFW sites, remove them from the config:

```python
default_sites: Dict[str, List[str]] = {
    "socials": [...],
    "gaming": [...],
    "news": [...],
    # "nsfw" removed
}
```

## Advanced Configuration

### Request Manager Settings

Each module uses the `RequestManager` class. You can customize per-module:

```python
# In app.py or module instantiation
from parser_ra_recon.request_manager import RequestManager

# Conservative delays for stealth
request_manager = RequestManager(min_delay=5.0, max_delay=15.0)
```

### Logging Configuration

The logging system uses `rich` for colored terminal output. To customize:

```python
# In parser_ra_recon/logging_utils.py
from rich.console import Console

console = Console(force_terminal=True, width=100)  # Force width
```

## Performance Tuning

### Fast Mode (High Risk of Blocking)

```python
min_delay: float = 0.5
max_delay: float = 1.0
```

⚠️ **Warning**: Very short delays increase detection and blocking risk.

### Balanced Mode (Recommended)

```python
min_delay: float = 1.0
max_delay: float = 3.0  # Default
```

Good balance between speed and stealth.

### Stealth Mode (Low Risk of Blocking)

```python
min_delay: float = 5.0
max_delay: float = 10.0
```

Slow but very hard to detect as automated scanning.

## Timeout Settings

Individual module timeouts are hardcoded to 10-12 seconds per request:

```python
# In modules
response = self.request_manager.get(url, timeout=10)
```

To change globally, modify each module's `.get()` call.

## Environment Variables (Optional)

You can extend the config to read from environment variables:

```python
import os
from dataclasses import dataclass

@dataclass
class Settings:
    min_delay: float = float(os.getenv('MIN_DELAY', 1.0))
    max_delay: float = float(os.getenv('MAX_DELAY', 3.0))
    export_dir: str = os.getenv('EXPORT_DIR', 'reports')

settings = Settings()
```

Then run:

```bash
MIN_DELAY=2 MAX_DELAY=5 python app.py
```

## Recommendations

1. **Default settings are reasonable** for most use cases
2. **Increase delays if blocked** by services
3. **Use categories wisely** to avoid unnecessary requests
4. **Monitor logs** for errors or rate-limit warnings
5. **Document changes** if you customize settings

---

For more information, see [README.md](README.md)
