from http import HTTPStatus
from typing import Annotated

from fastapi import Depends, HTTPException
from redis import asyncio as aioredis

from app.redis_depends import get_redis
from app.schemas.comment import CommentUser
from app.schemas.users import UserLogin
from app.services.services_users import login_user

r = Annotated[aioredis.Redis, Depends(get_redis)]
Login = Annotated[UserLogin, Depends(login_user)]


async def create_comment(user: Login, comment: CommentUser, r: r) -> dict:
    id_comment = await r.incr('comment:count')

    comment_key = f'comment:{id_comment}'

    comment_dict = comment.model_dump()

    comment_dict['_id_user'] = user.id_user

    comment_dict['_email_user'] = user.email

    comment_dict['_id_comment'] = comment_key

    comment_dict['likes'] = 0

    async with r.pipeline(transaction=True) as pipe:
        await pipe.hset(comment_key, mapping=comment_dict)

        await pipe.rpush(
            'comments:list',
            f'comment:{id_comment}:message:{comment.comment}:email_user:{user.email}'
        )

        await pipe.execute()

    return comment_dict


async def get_comments(r: r, init: int, end: int):
    formatted_comments = []

    list_comment = await r.lrange('comments:list', init, end)

    for entry in list_comment:
        if isinstance(entry, bytes):
            entry = entry.decode('utf-8')

        parts = entry.split(':')

        comment_dict = {
            "id": parts[1],
            "message": parts[3],
            "email_user": parts[5]
        }

        formatted_comments.append(comment_dict)

    return formatted_comments


async def like_the_comment(user:Login,id_comment: int, r: r) -> str:

    liked = await r.sismember(f'comment:{id_comment}:likes_users', user.email)

    if liked:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Você já curtiu esse comentário'
        )

    async with r.pipeline(transaction=True) as pipe:
        await pipe.hget(f'comment:{id_comment}', 'likes')

        await pipe.hincrby(f'comment:{id_comment}', 'likes')

        await pipe.hget(f'comment:{id_comment}', 'likes')

        await pipe.sadd(f'comment:{id_comment}:likes_users', user.email)

        result = await pipe.execute()


    if not result[0]:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Comentário não encontrado'
        )

    return f'Comentário curtido: likes no comentário {result[2]}'

async def get_all_liked(r:r,id_comment:int):

    likes = await r.smembers(f'comment:{id_comment}:likes_users')

    result = await r.scard(f'comment:{id_comment}:likes_users')

    if not result:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Comentário não encontrado ou deletado.'
        )

    if result == 0:
        return 'Esse comentário não possui curtidas'

    return f'Total de curtidas: {result}. Pessoas que curtiram: {likes}'

async def delete_comment_user(user:Login,r:r,id_comment:int):

    comment_email = await r.hget(f'comment:{id_comment}','_email_user')

    if comment_email != user.email:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN,
            detail='O email não conhecide com o do comentário'
        )

    async with r.pipeline(transaction=True) as pipe:
        await r.delete(f'comment:{id_comment}')
        await pipe.delete(f'comment:{id_comment}:likes_users')

        result = await pipe.execute()
    
    if not result[0]:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Comentário não encontrado'
        )

    if not result[0]:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Comentário não encontrado'
        )

    
    return 'Comentário deletado.'