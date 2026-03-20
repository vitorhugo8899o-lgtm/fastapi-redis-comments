from contextlib import asynccontextmanager

from fastapi import FastAPI
from redis import asyncio as aioredis


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis = await aioredis.from_url(
        "redis://localhost", decode_responses=True
    )

    yield

    await app.state.redis.close()


app = FastAPI(lifespan=lifespan)
