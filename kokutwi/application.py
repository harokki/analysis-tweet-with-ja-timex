from fastapi import FastAPI

from . import endpoints
from .containers import Container


def create_app() -> FastAPI:
    container = Container()
    container.wire(modules=[endpoints])

    app = FastAPI()
    app.container = container  # type: ignore
    app.include_router(endpoints.router)
    return app


app = create_app()
