from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.infra.dependencies import get_db
from src.usecase.create_teacher_regularity import CreateTeacherRegularity
from src.usecase.dto.create_teacher_regularity_dto import CreateTeacherRegularityDto

router = APIRouter()

@router.post("/teacher-regularity", status_code=201)
async def create_teacher_regularity(
    dto: CreateTeacherRegularityDto,
    db: AsyncSession = Depends(get_db)
):
    usecase = CreateTeacherRegularity()
    result = await usecase.execute(createTeacherRegularityDto=dto, db=db)
    return result
