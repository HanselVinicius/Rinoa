from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.health import router as health_router
from src.api.v1.routes.abscenses_controller import router as abscenses_router
from src.api.v1.routes.skips_controller import router as skips_router

from src.infra.config import settings


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
        router=abscenses_router, prefix="/api/v1", tags=["abscenses"]
    )
    
    app.include_router(
        router=skips_router, prefix="/api/v1", tags=["skips"]
    )

    return app


app = create_application()
