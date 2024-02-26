import json
from typing import Dict
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from starlette.responses import JSONResponse

from src.services.service import Service

main_router = APIRouter()


@main_router.post('/api/v1/parse_numbers')
async def parse_data(data: list[str]):
    service = Service()
    result = await service.extract_numbers(data)
    return JSONResponse(status_code=200, content=result)


