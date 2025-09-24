from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.dependencies import get_db
from src.usecase.dto.create_skip_dto import CreateSkipDto
from src.usecase.create_skip import CreateSkip

router = APIRouter()


@router.post("/skips", status_code=201)
async def create_skips(
    createSkipDto: CreateSkipDto,
    db: AsyncSession = Depends(get_db)
):
    createSkip = CreateSkip()
    result = await createSkip.execute(createSkipDto=createSkipDto, db=db)
    return result
