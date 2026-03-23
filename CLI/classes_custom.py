from rich.prompt import Prompt, InvalidResponse
import re

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