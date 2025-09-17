import os

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.model.abscenses import Abscenses
from src.usecase.dto.create_abscense_dto import CreateAbscenseDto


class CreateAbscense:

    async def execute(
        self, createAbscenseDto: CreateAbscenseDto, db: AsyncSession
    ) -> Abscenses:
        if createAbscenseDto.secret != os.getenv("SECRET_KEY", "dev_secret"):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect secret",
            )

        abscense_entity = createAbscenseDto.to_entity()
        db.add(abscense_entity)
        await db.commit()
        return abscense_entity
