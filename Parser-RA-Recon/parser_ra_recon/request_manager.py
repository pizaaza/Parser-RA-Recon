import random
import time
from typing import Dict, Optional

import requests

from .config import settings


class RequestManager:
    def __init__(self, min_delay: float = None, max_delay: float = None):
        self.min_delay = min_delay if min_delay is not None else settings.min_delay
        self.max_delay = max_delay if max_delay is not None else settings.max_delay

    def get_random_user_agent(self) -> str:
        return random.choice(settings.user_agents)

    def throttle(self) -> None:
        time.sleep(random.uniform(self.min_delay, self.max_delay))

    def get(self, url: str, params: Optional[Dict] = None, timeout: int = 12) -> requests.Response:
        headers = {
            "User-Agent": self.get_random_user_agent(),
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
        }
        self.throttle()
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        return response

