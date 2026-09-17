from fastapi import FastAPI

from src.api.check import router as health_router
from src.config import settings


def create_application() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        debug=settings.DEBUG,
    )

    app.include_router(health_router, prefix=settings.API_PREFIX)

    return app


app = create_application()