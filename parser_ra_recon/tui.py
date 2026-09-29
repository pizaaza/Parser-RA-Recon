from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.text import Text
from typing import Dict, List, Optional
from .logging_utils import log_info, log_error, log_step

console = Console()


class FoxCamera:
    """Stylized box framing for target data visualization."""

    @staticmethod
    def frame_data(data: Dict, title: str = "TARGET DATA") -> Panel:
        """Frame data in a styled box with title."""
        content = ""
        for key, value in data.items():
            if isinstance(value, dict):
                content += f"[bold cyan]{key}[/]:\n"
                for k, v in value.items():
                    content += f"  [yellow]{k}[/]: {v}\n"
            elif isinstance(value, list):
                content += f"[bold cyan]{key}[/]: {', '.join(str(v) for v in value)}\n"
            else:
                content += f"[bold cyan]{key}[/]: {value}\n"

        return Panel(
            content,
            title=f"[bold magenta]🦊 {title}[/]" ,
            border_style="magenta",
            expand=False,
        )


class TUIInterface:
    """Terminal User Interface for Parser RA Recon."""

    def __init__(self):
        self.console = console

    def show_main_menu(self) -> str:
        """Display main menu and get user choice."""
        self.console.clear()
        self.console.print(
            Panel(
                "[bold cyan]Parser RA Recon - Risk Assessment OSINT Framework[/]\n"
                "[yellow]1.[/] Username Scanner\n"
                "[yellow]2.[/] Email Analyzer\n"
                "[yellow]3.[/] IP Analyzer\n"
                "[yellow]4.[/] Domain OSINT\n"
                "[yellow]5.[/] Metadata Analyzer\n"
                "[yellow]6.[/] Phone Formatter\n"
                "[yellow]7.[/] Username Permutator\n"
                "[yellow]8.[/] Breach Summary Report\n"
                "[yellow]9.[/] Exit\n",
                title="[bold magenta]MAIN MENU[/]",
                border_style="magenta",
            )
        )
        return Prompt.ask("[bold]Select option[/]", choices=["1", "2", "3", "4", "5", "6", "7", "8", "9"])

    def show_username_scanner_menu(self) -> tuple:
        """Get username scanner inputs."""
        username = Prompt.ask("[bold cyan]Enter target username[/]")
        
        self.console.print(
            "[bold yellow]Available categories:[/]\n"
            "  [cyan]socials[/] - Social media platforms\n"
            "  [cyan]gaming[/] - Gaming platforms\n"
            "  [cyan]news[/] - News aggregators\n"
            "  [cyan]all[/] - All platforms"
        )
        category = Prompt.ask("[bold cyan]Select category[/]", default="all", choices=["socials", "gaming", "news", "all"])
        
        nsfw = Confirm.ask("[bold cyan]Include NSFW sites?[/]", default=False)
        
        return username, category, nsfw

    def show_email_analyzer_menu(self) -> str:
        """Get email analyzer input."""
        email = Prompt.ask("[bold cyan]Enter target email address[/]")
        return email

    def show_ip_analyzer_menu(self) -> str:
        """Get IP analyzer input."""
        ip_address = Prompt.ask("[bold cyan]Enter target IP address[/]")
        return ip_address

    def show_domain_osint_menu(self) -> str:
        """Get domain OSINT input."""
        domain = Prompt.ask("[bold cyan]Enter target domain[/]")
        return domain

    def show_metadata_analyzer_menu(self) -> str:
        """Get image URL for metadata analysis."""
        image_url = Prompt.ask("[bold cyan]Enter public image URL[/]")
        return image_url

    def show_phone_formatter_menu(self) -> str:
        """Get phone number for validation."""
        phone = Prompt.ask("[bold cyan]Enter phone number (with country code, e.g., +1234567890)[/]")
        return phone

    def show_permutator_menu(self) -> tuple:
        """Get permutator inputs."""
        username = Prompt.ask("[bold cyan]Enter base username[/]")
        max_variants = Prompt.ask("[bold cyan]Max variants to generate[/]", default="20")
        try:
            max_variants = int(max_variants)
        except ValueError:
            max_variants = 20
        return username, max_variants

    def display_results(self, results: Dict, title: str = "RESULTS") -> None:
        """Display results in formatted panel."""
        panel = FoxCamera.frame_data(results, title)
        self.console.print(panel)

    def display_table(self, data: List[Dict], title: str = "RESULTS") -> None:
        """Display results in table format."""
        if not data:
            log_error("No data to display")
            return

        table = Table(title=title, border_style="magenta")
        
        # Add columns from first row
        for key in data[0].keys():
            table.add_column(key, style="cyan")
        
        # Add rows
        for row in data:
            table.add_row(*[str(v) for v in row.values()])
        
        self.console.print(table)

    def pause(self) -> None:
        """Pause and wait for user input."""
        Prompt.ask("[bold yellow]Press Enter to continue[/]")
