from typing import Annotated

from fastapi import APIRouter, Depends
from redis import asyncio as aioredis

from app.redis_depends import get_redis
from app.schemas.users import ResponseLogin, UserCreate, UserLogin, MessageConfirme
from app.services.services_users import change_infos, create_user, login_user, delete_user

router_users = APIRouter(prefix='/users', tags=['Users'])
r = Annotated[aioredis.Redis, Depends(get_redis)]
Login = Annotated[UserLogin, Depends(login_user)]


@router_users.post('', status_code=201)
async def create(user: UserCreate, r: r) -> dict:
    return await create_user(user, r)


@router_users.post('/login', status_code=200)
async def login(user: UserLogin, r: r) -> ResponseLogin:
    return await login_user(r, user)


@router_users.put('/me', status_code=200)
async def infos_change(
    new_info: UserCreate, r: r,
    login: Login) -> str:

    return await change_infos(new_info, r, login)

@router_users.delete('/me',status_code=200)
async def delete_ac(login: Login,confirm:MessageConfirme, r:r):
    return await delete_user(login,confirm,r)