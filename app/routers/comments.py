from typing import Annotated

from fastapi import APIRouter, Depends, Query
from redis import asyncio as aioredis

from app.redis_depends import get_redis
from app.schemas.comment import CommentUser
from app.schemas.users import UserLogin, Filter
from app.services.services_comment import create_comment, get_comments
from app.services.services_users import login_user

router_coments = APIRouter(prefix='/comments', tags=['Comments'])

r = Annotated[aioredis.Redis, Depends(get_redis)]
Login = Annotated[UserLogin, Depends(login_user)]


@router_coments.post('', status_code=201)
async def comment(user: Login, comment: CommentUser, r: r) -> dict:
    return await create_comment(user, comment, r)

@router_coments.get('',status_code=200)
async def list_comments(r:r,filter_comment: Annotated[Filter, Query()]):
    return await get_comments(r,filter_comment.init,filter_comment.end)
