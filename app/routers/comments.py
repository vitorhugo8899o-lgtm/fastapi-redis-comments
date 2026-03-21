from typing import Annotated

from fastapi import APIRouter, Depends
from redis import asyncio as aioredis

from app.redis_depends import get_redis

router_coments = APIRouter(prefix='/comments',tags=['Comments'])

r = Annotated[aioredis.Redis, Depends(get_redis)]

@router_coments.post('',status_code=201)
async def create_comment():
    pass