from fastapi import FastAPI

from src.routing.router import main_router

app = FastAPI()


def create_app() -> FastAPI:
    app.include_router(main_router)
    return app