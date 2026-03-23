from rich.console import Console
from rich.table import Table
from rich.panel import Panel, Text
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TaskProgressColumn,
)

from rich.prompt import Prompt, IntPrompt
import asyncio

from terminal import init_terminal, choice_option
from classes_custom import UsernamePrompt, EmailPrompt
console = Console()

table_init =  Table(min_width=100)

async def run_app():
    while True:
        init_terminal()
    
        option = choice_option()
        
        if option == 1:
                name = UsernamePrompt.ask("Digite seu [bold red]username[/]")
                email = EmailPrompt.ask("Digite seu [bold red]Email[/]")
        
        
        elif option == 2:
            return print('2')
        
        else:
            break
    


























if __name__ == '__main__':
    try:
        asyncio.run(run_app())
    except KeyboardInterrupt:
        print("\nAplicação encerrada pelo usuário.")