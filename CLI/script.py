import asyncio

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from .func_terminal import (
    change_info_user,
    create_comment,
    delete_comment,
    delete_user,
    get_all_liked,
    like_comment,
    list_comment,
    list_users,
    login_user,
    submit_form,
)
from .terminal import (
    cat_animation,
    choice_option,
    choice_option_login,
    init_terminal,
    loading_animation,
    screen_of_options,
)

console = Console()

table_init = Table(min_width=100)


async def run_app():
    while True:
        init_terminal()

        option = choice_option()

        if option == 1:  #noqa PLR2004
            await submit_form()

            await loading_animation('Criando nova conta...')
            console.clear()

        elif option == 2:  # Login
            user_login = await login_user()

            await loading_animation(f'Tentando logar na conta de {user_login['email']}....')

            if user_login is None:
                console.clear()
                continue

            while True:
                screen_of_options(user_login['email'])

                option = choice_option_login()

                if option == 1:
                    await change_info_user(user_login)
                    await loading_animation('Mudando informações....')
                    console.clear()
                    break

                elif option == 2:
                    await delete_user(user_login)
                    await loading_animation(f'Deletando usuário {user_login['email']}...')
                    console.clear()
                    break

                elif option == 3:
                    await list_users()
                    Prompt.ask("Deseja continuar?", choices={'s'})
                    console.clear()

                elif option == 4:
                    await create_comment(user_login)
                    await loading_animation('Criando comentario...')
                    console.clear()

                elif option == 5:
                    await list_comment()
                    Prompt.ask("Deseja continuar?", choices={'s'})
                    await asyncio.sleep(0.5)
                    console.clear()

                elif option == 6:
                    await like_comment(user_login)
                    await asyncio.sleep(2)
                    console.clear()

                elif option == 7:
                    await get_all_liked()
                    await asyncio.sleep(3)
                    console.clear()

                elif option == 8:
                    await delete_comment(user_login)
                    await loading_animation('Deletando comentario...')
                    console.clear()

                elif option == 9:
                    await loading_animation(f'Deslogando usuário {user_login['email']}...')
                    console.clear()
                    break
        else:
            console.print('Obrigado por usar o Redis social network, sinta-se a vontade para abrir uma issue no repositorio caso tenha alguma sugestão.\nGithub: https://github.com/vitorhugo8899o-lgtm/fastapi-redis-comments')

            await cat_animation()
            break


if __name__ == '__main__':
    try:
        asyncio.run(run_app())

    except KeyboardInterrupt:
        print("\nAplicação encerrada pelo usuário.")

# python -m CLI.script
