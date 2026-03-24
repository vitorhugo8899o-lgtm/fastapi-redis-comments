import json

from rich.console import Console
from rich.prompt import IntPrompt, Prompt

from CLI.classes_custom import EmailPrompt, PasswordPrompt, UsernamePrompt
from CLI.client_http import get_app_conection

console = Console()


async def submit_form():
    name = UsernamePrompt.ask("Digite seu [bold red]username[/]")
    email = EmailPrompt.ask("Digite seu [bold red]Email[/]")
    password = PasswordPrompt.ask("Digite sua [bold red]senha[/]", password=True)

    payload = {
        'name': f'{name}',
        'email': f'{email}',
        'password': f'{password}'
    }

    async with get_app_conection() as client:
        response = await client.post('/users', json=payload)

        data = response.json()

    console.print(f'Bem vindo {data['name']}!, você é o usuário de id:{data['id']}')
    console.print('Volto para o menu e realize o login!')


async def login_user():
    while True:
        console.print("[yellow]Digite 's' na escolha para voltar ao menu principal.[/]")
        email = EmailPrompt.ask("Digite seu [bold red]email[/]",)

        password = PasswordPrompt.ask("Digite sua [bold red]senha[/]", password=True)

        payload = {
            'email': f'{email}',
            'password': f'{password}'
        }

        async with get_app_conection() as client:
            response = await client.post('/users/login', json=payload)
            data = response.json()

        if response.status_code == 200:
            console.print("[green]Login realizado com sucesso![/]")
            return payload

        if 'detail' in data:
            console.print(f"[bold red]Erro:[/] {data['detail']}")
        else:
            console.print("[bold red]Credenciais inválidas. Tente novamente.[/]")

        choice = Prompt.ask("Deseja sair para o menu? escolha:", choices=['s', 'n'])

        if choice == 's':
            return None
        else:
            continue


async def change_info_user(user: dict):
    console.print('Digite as novas informações')

    name = UsernamePrompt.ask("Digite seu [bold red]username[/]")
    email = EmailPrompt.ask("Digite seu [bold red]Email[/]")
    password = PasswordPrompt.ask("Digite sua [bold red]senha[/]", password=True)

    submit_json = {
        "new_info": {
            'name': f'{name}',
            'email': f'{email}',
            'password': f'{password}'
        },
        "user": {
            "email": f"{user['email']}",
            "password": f"{user['password']}"
        }
    }

    async with get_app_conection() as client:
        response = await client.put('/users/me', json=submit_json)

    data = json.dumps(response.json())

    console.print_json(data)


async def delete_user(user: dict):
    payload = {
        "confirm": {
            "message": "Confirmo deletar minha conta"
        },
        "user": {
            "email": f"{user['email']}",
            "password": f"{user['password']}"
        }
    }

    async with get_app_conection() as client:
        response = await client.request('DELETE', '/users/me', json=payload)

    data = json.dumps(response.json())

    console.print_json(data)


async def list_users() -> None:

    console.print("[yellow]Caso deseje ver todos os usuários, digite 0 para o inicio e -1 para o final.[/]")

    init = IntPrompt.ask("Apartir de que usuario deseja buscar? inicio")

    end = IntPrompt.ask("Até que usuário deseja buscar? final")

    async with get_app_conection() as client:
        response = await client.get(f'/users?init={init}&end={end}')

    data = json.dumps(response.json())

    console.print_json(data)


async def create_comment(user: dict):
    while True:
        comment = Prompt.ask('Digite seu comentário')

        if len(comment) < 8:
            console.print("[yellow]O comentário deve conter no mínimo 8 caracteres!.[/]")
            continue

        break

    payload = {
        "comment": {
            "comment": f"{comment}"
        },
        "user": {
            "email": f"{user['email']}",
            "password": f"{user['password']}"
        }
    }

    async with get_app_conection() as client:
        response = await client.post('/comments', json=payload)

    data = json.dumps(response.json())

    console.print_json(data)


async def list_comment():
    console.print("[yellow]Caso deseje ver todos os contários, digite 0 para o inicio e -1 para o final.[/]")

    init = IntPrompt.ask("Apartir de que cometário deseja buscar? inicio")

    end = IntPrompt.ask("Até que comentário deseja buscar? final")

    async with get_app_conection() as client:
        response = await client.get(f'/comments?init={init}&end={end}')

    data = json.dumps(response.json())

    console.print_json(data)


async def like_comment(user: dict):
    payload = {
        'email': f'{user['email']}',
        'password': f'{user['password']}'
    }

    id_comment = IntPrompt.ask("Digite o id do comentário a ser curtido")

    async with get_app_conection() as client:
        response = await client.post(f'/comments/{id_comment}', json=payload)

    data = json.dumps(response.json())

    console.print_json(data)


async def get_all_liked():
    id_comment = IntPrompt.ask("Digite o id do comentário para ver quem curtiu este comentário")

    async with get_app_conection() as client:
        response = await client.post(f'/comments/{id_comment}/liked_list')

    data = json.dumps(response.json())

    console.print_json(data)


async def delete_comment(user: dict):
    id_comment = IntPrompt.ask("Digite o id do comentário a ser curtido")

    payload = {
        'email': f'{user['email']}',
        'password': f'{user['password']}'
    }

    async with get_app_conection() as client:
        response = await client.request('DELETE', f'/comments/{id_comment}', json=payload)

    data = json.dumps(response.json())

    console.print_json(data)
