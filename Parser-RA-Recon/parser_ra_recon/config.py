from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class Settings:
    min_delay: float = 1.0
    max_delay: float = 3.0
    user_agents: List[str] = field(default_factory=lambda: [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
    ])
    default_sites: Dict[str, List[str]] = field(default_factory=lambda: {
        "socials": ["github.com", "reddit.com", "x.com", "youtube.com", "twitch.tv", "instagram.com", "linkedin.com"],
        "gaming": ["steamcommunity.com", "battle.net", "playstation.com", "xbox.com", "epicgames.com"],
        "news": ["news.ycombinator.com", "wired.com", "techcrunch.com", "reddit.com"],
        "nsfw": ["pornhub.com", "xvideos.com", "reddit.com"],
    })
    max_results: int = 20
    export_dir: str = "reports"


settings = Settings()

