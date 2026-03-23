from rich.console import Console
from rich.table import Table

from rich.panel import Panel, Text

from rich.prompt import Prompt, IntPrompt


console = Console()
table_init =  Table(min_width=100)

def init_terminal():
    console.print(
    Panel(Text(
        'Redis social network',justify="center",style="red"),
        border_style='magenta',
        width=100, 
        )
    )

    table_init.add_column("Operações", justify="center", no_wrap=True)

    table_init.add_row('1 - Criar conta', style="green")

    table_init.add_row('2 - Logar', style="magenta")

    table_init.add_row('3 - Sair', style="red")

    console.print(table_init)

def choice_option():
    opcao = IntPrompt.ask(
        "Escolha uma operação", 
        choices=["1", "2","3"], 
        show_choices=False,
    )

    return opcao