import asyncio

from app.main import app
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from .terminal import choice_option, init_terminal, submit_form, login_user

console = Console()

table_init = Table(min_width=100)


async def run_app():
    while True:
        init_terminal()

        option = choice_option()

        if option == 1:  #noqa PLR2004
            user = await submit_form()

            

        elif option == 2:  #noqa PLR2004
            user_login = await login_user()

        else:
            break


if __name__ == '__main__':
    try:
        asyncio.run(run_app())

    except KeyboardInterrupt:
        print("\nAplicação encerrada pelo usuário.")

#python -m CLI.script
