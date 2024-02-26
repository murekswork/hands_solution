from typing import AsyncGenerator
from aiohttp import ClientSession


async def get_client() -> AsyncGenerator:
    async with ClientSession() as session:
        yield session
