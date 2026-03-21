from app.services.services_users import login_user, create_user

from typing import Annotated

from fastapi import APIRouter, Depends
from redis import asyncio as aioredis
from app.redis_depends import get_redis
from app.schemas.users import UserCreate, UserLogin

router_users = APIRouter(prefix='/users', tags=['Users'])
r = Annotated[aioredis.Redis, Depends(get_redis)]
Login = Annotated[UserLogin, Depends(login_user)]

@router_users.post('', status_code=201)
async def create(user: UserCreate, r: r) -> dict:
    return create_user(user,r)
    

@router_users.post('/login', status_code=200)
async def login(user: UserLogin, r: r) -> str:
    return login_user(r,user)
    

