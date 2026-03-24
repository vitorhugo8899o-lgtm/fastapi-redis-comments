import re

from rich.prompt import InvalidResponse, Prompt


class UsernamePrompt(Prompt):

    def process_response(self, value: str) -> str:
        retorno = super().process_response(value)

        if len(retorno) < 5:
            raise InvalidResponse("[bold red]Erro:[/] O username deve ter pelo menos 5 caracteres.")

        if not any(char.islower() for char in retorno):
            raise InvalidResponse("[bold red]Erro:[/] O username deve ter pelo menos uma letra minúscula.")

        if not any(char.isupper() for char in retorno):
            raise InvalidResponse("[bold red]Erro:[/] O username deve ter pelo menos uma letra maiúscula.")

        return retorno


class EmailPrompt(Prompt):

    def process_response(self, value):
        retorno = super().process_response(value)

        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

        if not re.match(email_regex, retorno):
            raise InvalidResponse("[bold red]Erro:[/] E-mail inválido! Use o formato nome@dominio.com")

        return retorno


class PasswordPrompt(Prompt):

    def process_response(self, value):
        retorno = super().process_response(value)

        password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&+\-]).+$"

        if len(retorno) < 8:
            raise InvalidResponse("[bold red]Erro:[/] Sua senha deve conter no mínimo 8 caracteres!")

        if not re.match(password_regex, retorno):
            raise InvalidResponse(
                "[bold red]Erro:[/] Sua senha deve conter pelo menos uma letra maiúscula, "
                "uma minúscula, um número e um caractere especial (ex: @, $, !, %, *, #, ?, &, +, -)."
            )

        return retorno
