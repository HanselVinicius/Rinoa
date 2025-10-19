from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.health import router as health_router
from src.api.v1.routes.abscenses_controller import router as abscenses_router
from src.api.v1.routes.skips_controller import router as skips_router
from src.api.v1.routes.create_teacher_regularity_controller import router as teacher_regularity_router
from src.api.v1.routes.create_manage_complexity_controller import router as manage_complexity
from src.api.v1.routes.teacher_training_controller import router as teacher_training

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
    
    app.include_router(
        router=teacher_regularity_router,prefix="/api/v1",tags=['teacher_regularity']
    )

    app.include_router(
        router=manage_complexity,prefix='/api/v1',tags=['manage_complexity']
    )
    
    app.include_router(
        router=teacher_training,prefix='/api/v1',tags=['teacher_training']
    )

    return app


app = create_application()
