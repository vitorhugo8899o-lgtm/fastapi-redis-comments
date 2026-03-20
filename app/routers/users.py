from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from redis import asyncio as aioredis

from app.redis_depends import get_redis
from app.schemas.users import UserCreate

router_users = APIRouter(prefix='/users', tags=['Users'])
r = Annotated[aioredis.Redis, Depends(get_redis)]


@router_users.post('', status_code=201)
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

        await pipe.sadd('users:all', id_user)

        await pipe.execute()

    return user_dict
