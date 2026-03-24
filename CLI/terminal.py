import asyncio

from rich.console import Console
from rich.live import Live
from rich.panel import Panel, Text
from rich.progress import Progress
from rich.prompt import IntPrompt
from rich.table import Table

console = Console()



CAT_FRAME_1 = r"""
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)
"""

CAT_FRAME_2 = r"""         --
      |\      _,,,---,,___-  -
      /,`.-'`'    -.  ;-;;,_ - 
     |,4-  ) )-,_. ,\ (  
    '---''(_/--'  `-'\_)
"""

FRAMES = [CAT_FRAME_1, CAT_FRAME_2]


def init_terminal():
    console.print(
    Panel(Text(
        'Redis social network', justify="center", style="red"),
        border_style='rgb(70,236,246)',
        width=100,
        )
    )

    table_init = Table(
        min_width=100,
        border_style="rgb(70,236,246)",
        header_style="bold red"
    )

    table_init.add_column("Operações", justify="center", no_wrap=True)
    table_init.add_row('1 - Criar conta', style="green")
    table_init.add_row('2 - Logar', style="rgb(72,210,244)")
    table_init.add_row('3 - Sair', style="red")

    console.print(table_init)


def choice_option():
    opcao = IntPrompt.ask(
        "Escolha uma operação",
        choices=["1", "2", "3"],
        show_choices=False,
    )

    return opcao


def screen_of_options(user: str):
    table_screen = Table(
        min_width=100,
        border_style="rgb(70,236,246)",
        header_style="bold red"
    )

    table_screen.add_column(f"O que deseja fazer, {user}?", justify="center", no_wrap=True)
    table_screen.add_row('1 - Mudar Informações de conta', style="yellow")
    table_screen.add_row('2 - Deletar Conta', style="red")
    table_screen.add_row('3 - Listar todos os usuários ativos', style="rgb(223,65,252)")
    table_screen.add_row('4 - Cria comentario', style="rgb(189,193,123)")
    table_screen.add_row('5 - Listar todos os cometarios', style="rgb(163,164,152)")
    table_screen.add_row('6 - Dar like em um contario', style="green")
    table_screen.add_row('7 - Ver lista de pessoas que curtiram um contario', style="rgb(84,232,149)")
    table_screen.add_row('8 - Deletar meu comentario', style="red")
    table_screen.add_row('9 - Sair', style="red")

    console.print(table_screen)


def choice_option_login():
    opcao = IntPrompt.ask(
        "Escolha uma operação",
        choices=["1", "2", "3", "4", "5", "6", "7", "8", "9"],
        show_choices=False,
    )

    return opcao


async def loading_animation(description: str):
    with Progress(transient=True) as progress:
        task = progress.add_task(f"[rgb(112,204,137)]{description}...", total=100)
        while not progress.finished:
            progress.update(task, advance=15)
            await asyncio.sleep(0.2)


async def cat_animation(duracao_segundos: int = 3):
    with Live(console=console, screen=False, refresh_per_second=4) as live:
        for _ in range(duracao_segundos * 4):
            for frame in FRAMES:
                conteudo = Panel(frame, title="[bold red]Deixe uma estrela para a tentaiva do gato", border_style="rgb(70,236,246)")
                live.update(conteudo)
                await asyncio.sleep(0.25)
