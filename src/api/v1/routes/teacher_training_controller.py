from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.dependencies import get_db
from src.usecase.create_teacher_training import CreateTeacherTraining
from src.usecase.dto.create_teacher_training_dto import CreateTeacherTrainingDto

router = APIRouter()

@router.post("/teacher-training", status_code=201)
async def create_teacher_training(
    dto: CreateTeacherTrainingDto,
    db: AsyncSession = Depends(get_db)
):

    usecase = CreateTeacherTraining()
    result = await usecase.execute(createTeacherTrainingDto=dto, db=db)
    return result
