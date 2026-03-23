from httpx import ASGITransport, AsyncClient
from app.main import app


async def get_app_conection():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url='http://cli'
    ) as ac:
        yield ac