from rich.console import Console
from rich.panel import Panel, Text
from rich.prompt import IntPrompt
from rich.table import Table
from CLI.classes_custom import EmailPrompt, UsernamePrompt, PasswordPrompt
from CLI.client_http import get_app_conection


console = Console()
table_init = Table(min_width=100)



def init_terminal():
    console.print(
    Panel(Text(
        'Redis social network', justify="center", style="red"),
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
        choices=["1", "2", "3"],
        show_choices=False,
    )

    return opcao


async def submit_form():
    name = UsernamePrompt.ask("Digite seu [bold red]username[/]")
    email = EmailPrompt.ask("Digite seu [bold red]Email[/]")
    password = PasswordPrompt.ask("Digite sua [bold red]senha[/]",password=True)

    payload = {
        'name':f'{name}',
        'email':f'{email}',
        'password':f'{password}'
    }

    async with get_app_conection() as client:
        response = await client.post('/users', json=payload)

        data = response.json()

    console.print(f'Bem vindo {data['name']}!, você é o usuário de id:{data['id']}')

    return data

async def login_user():
    email = EmailPrompt.ask("Digite seu [bold red]email[/]")
    password = PasswordPrompt.ask("Digite seu [bold red]senha[/]")

    payload = {
        'email':f'{email}',
        'password':f'{password}'
        }
    async with get_app_conection() as client:
        response = await client.post('/users/login',json=payload)

    console.print(response.json()['message'])

    return payload

