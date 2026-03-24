from contextlib import asynccontextmanager

from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

from app.main import app


@asynccontextmanager
async def get_app_conection():
    async with LifespanManager(app) as manager:
        async with AsyncClient(
            transport=ASGITransport(app=manager.app),
            base_url='http://cli'
        ) as ac:
            yield ac
