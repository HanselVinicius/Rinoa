import os
from fastapi import HTTPException, status

from src.usecase.dto.create_teacher_regularity_dto import CreateTeacherRegularityDto

class CreateTeacherRegularity:
    async def execute(self, createTeacherRegularityDto: CreateTeacherRegularityDto, db):
        if getattr(createTeacherRegularityDto, "secret", None) != os.getenv("SECRET_KEY", "dev_secret"):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect secret",
            )

        entity = createTeacherRegularityDto.to_entity()
        db.add(entity)
        await db.commit()
        await db.refresh(entity)
        return entity
