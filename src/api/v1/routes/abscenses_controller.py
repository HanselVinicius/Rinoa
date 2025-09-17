from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.dependencies import get_db
from src.usecase.create_abscense import CreateAbscense
from src.usecase.dto.create_abscense_dto import CreateAbscenseDto

router = APIRouter()


@router.post("/abscenses", status_code=201)
async def create_abscense(
    createAbscenseDto: CreateAbscenseDto, db: AsyncSession = Depends(get_db)
):
    createAbscense = CreateAbscense()
    result = await createAbscense.execute(createAbscenseDto=createAbscenseDto, db=db)
    return result
