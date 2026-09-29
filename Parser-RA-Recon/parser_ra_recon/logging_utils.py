import random
import time
from typing import Optional

from rich.console import Console
from rich.text import Text


console = Console()


def log_info(message: str) -> None:
    console.print(f"[bold cyan]INFO:[/] {message}")


def log_warning(message: str) -> None:
    console.print(f"[bold yellow]WARN:[/] {message}")


def log_error(message: str) -> None:
    console.print(f"[bold red]ERROR:[/] {message}")


def log_step(step: str, detail: str) -> None:
    console.print(Text(f"{step}: {detail}", style="bold bright_white"))


def random_delay(min_delay: float = 1.0, max_delay: float = 3.0) -> None:
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)


def print_banner() -> None:
    banner = r"""
    ____  ____  __  __   ___   ___   ___   ___      __    __  ____   _____   ____
   / __ \/ __ \/ / / /  / _ \ / _ \ / _ \ / _ \    / /   / / / __ \ / ___/  / __ \
  / /_/ / /_/ / /_/ /  /  _//  _//  _//  _//  _/   / /   / / / /_/ / \___ \  / /_/ /
 / ____/ _, _/ __  /  / /  / /  / /  / /  / /    / /___/ /_/ __  /  ___/ / / _, _/
/_/   /_/ |_|/_/ /_/  /_/  /_/  /_/  /_/  /_/    /_____/____/_/ /_/  /____/ /_/ |_|

       ____  ____  ______      ______   ______  ____   ___    ______  ____  ___
      / __ \/ __ \/ ____/     /_  __/  /_  __/ / __ \ /   |  / __ \/ __ \/   |
     / /_/ / /_/ / /___        / /     / /   / /_/ // /| | / /_/ / /_/ / /| |
    / ____/ _, _/ ___/       / /     / /   / _, _/ / ___ |/ __  / __  / ___ |
   /_/   /_/ |_|/____/       /_/     /_/   /_/ |_|/_/  |_/_/ /_/_/ /_/_/____/|

        [bold bright_magenta]Parser RA Recon[/bold bright_magenta] - Risk Assessment OSINT Framework
    """
    console.print(banner)

