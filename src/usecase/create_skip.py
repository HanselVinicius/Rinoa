from sqlalchemy.ext.asyncio import AsyncSession
import os

from fastapi import HTTPException, status
from src.usecase.dto.create_skip_dto import CreateSkipDto

class CreateSkip:

    async def execute(self, createSkipDto: CreateSkipDto, db: AsyncSession):
        if createSkipDto.secret != os.getenv("SECRET_KEY", "dev_secret"):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect secret",
            )
        skip_entity = createSkipDto.to_entity()
        db.add(skip_entity)
        await db.commit()
        return skip_entity