
from datetime import datetime
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.text import Text
import CSGOStats

player = CSGOStats.CSGOStats("FootSX")
player.refresh_all_informations()

def get_content(informations):

    return f"[b]{informations}[/b]\n[yellow]{player.informations_overview[informations]}"


console = Console()

user_renderables = [Panel(get_content(info), expand=True) for info in player.informations_overview]
console.print(Columns(user_renderables))
