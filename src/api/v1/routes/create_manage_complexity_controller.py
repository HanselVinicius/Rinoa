from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.infra.dependencies import get_db
from src.usecase.create_manage_complexity import CreateManageComplexity
from src.usecase.dto.create_manage_complexity_dto import CreateManageComplexityDto

router = APIRouter()

@router.post("/manage-complexity", status_code=201)
async def create_manage_complexity(
    dto: CreateManageComplexityDto,
    db: AsyncSession = Depends(get_db)
):
    usecase = CreateManageComplexity()
    result = await usecase.execute(createManageComplexityDto=dto, db=db)
    return result
