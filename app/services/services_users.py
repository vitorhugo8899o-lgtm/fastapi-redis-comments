from fastapi import Depends, HTTPException
from app.redis_depends import get_redis
from app.schemas.users import UserCreate, UserLogin
from redis import asyncio as aioredis
from http import HTTPStatus
from typing import Annotated


r = Annotated[aioredis.Redis, Depends(get_redis)]


async def create_user(user:UserCreate,r:r):
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

        await pipe.sadd('users:all', id_user)

        await pipe.execute()

    return user_dict



async def login_user(r:r,user: UserLogin):
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
    return 'Usuario Logado!'

Login = Annotated[UserLogin, Depends(login_user)]



