from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.health import router as health_router
from api.v1.routes.extract_data import router as extract_data_router
from infra.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application startup: Loading resources...")
    yield
    print("Application shutdown: Releasing resources...")


def create_application() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        description="Rinoa Api",
        lifespan=lifespan,
    )

    app.include_router(
        router=health_router, prefix="/api/health", tags=["Health Check"]
    )

    app.include_router(
        router=extract_data_router, prefix="/api/v1", tags=["Data Extraction"]
    )

    return app


app = create_application()
