from contextlib import asynccontextmanager

from fastapi import FastAPI
from redis import asyncio as aioredis

from app.routers.comments import router_coments
from app.routers.users import router_users


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis = await aioredis.from_url(
        'redis://localhost', decode_responses=True
    )

    yield

    await app.state.redis.close()


app = FastAPI(lifespan=lifespan)

app.include_router(router_users)
app.include_router(router_coments)
