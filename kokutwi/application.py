from fastapi import FastAPI

from .containers import Container
from . import endpoints


def create_app() -> FastAPI:
    container = Container()
    container.wire(modules=[endpoints])

    app = FastAPI()
    app.container = container  # type: ignore
    app.include_router(endpoints.router)
    return app


app = create_app()
