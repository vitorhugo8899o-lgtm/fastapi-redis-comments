from http import HTTPStatus
from typing import Annotated

from fastapi import Depends, HTTPException
from redis import asyncio as aioredis
from app.redis_depends import get_redis
from app.schemas.users import (
    MessageConfirme,
    ResponseLogin,
    UserCreate,
    UserLogin,
)


r = Annotated[aioredis.Redis, Depends(get_redis)]

async def create_user(user: UserCreate, r: r) -> dict:
    email_key = f'user:email:{user.email}'

    exist_email = await r.get(email_key)
    if exist_email:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Este email já está cadastrado.',
        )

    id_user = await r.incr('users:count')

    user_key = f'user:{id_user}'

    user_dict = user.model_dump()
    user_dict['id'] = id_user

    async with r.pipeline(transaction=True) as pipe:
        await pipe.hset(user_key, mapping=user_dict)

        await pipe.set(email_key, id_user)

        await pipe.lpush('users:list',f'user:{id_user}:user:{user.email}')

        await pipe.execute()

    return user_dict


async def login_user(r: r, user: UserLogin) -> ResponseLogin:
    exists = await r.get(f'user:email:{user.email}')

    async with r.pipeline(transaction=True) as pipe:
        # esperar ele executar para depois verificar os campos

        await pipe.hget(f'user:{exists}', 'email')

        await pipe.hget(f'user:{exists}', 'password')

        result = await pipe.execute()

    if not exists:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Email não está cadastrado.'
        )

    elif result[0] != user.email:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail='Email  incorreto'
        )

    elif result[1] != user.password:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail='senha incorreta'
        )
    return ResponseLogin(
        id_user=exists,
        email=user.email,
        message='Usuário Logado!'
    )


Login = Annotated[UserLogin, Depends(login_user)]


async def change_infos(new_info: UserCreate, r: r, login: Login) -> str:

    user_key = f'user:{login.id_user}'

    user_dict = new_info.model_dump()
    user_dict['id'] = user_key

    async with r.pipeline(transaction=True) as pipe:

        await pipe.hset(f'user:{login.id_user}', mapping=user_dict)

        await pipe.rename(
            f'user:email:{login.email}', f'user:email:{new_info.email}'
        )

        await pipe.execute()

    return f'Informações Atualizadas com Sucesso!, Bem vindo {new_info.name}'


async def delete_user(login: Login, confirm: MessageConfirme, r: r) -> str:

    user_key = f'user:{login.id_user}'

    async with r.pipeline(transaction=True) as pipe:
        await pipe.hdel(f'user:{user_key}', 'name', 'email', 'password')
        await pipe.delete(f'user:email:{login.email}')

        result = await pipe.execute()

    if result[0] is None:
        raise 'Erro ao deletar conjunto'
    elif result[1] is None:
        raise 'Erro ao deletar chave'

    return 'Conta deletada!'

async def get_users(r:r,init:int,end:int):
    result = await r.lrange('users:list',init,end)

    return result