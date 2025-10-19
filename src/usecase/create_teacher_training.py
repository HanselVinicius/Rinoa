import os
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.usecase.dto.create_teacher_training_dto import CreateTeacherTrainingDto

class CreateTeacherTraining:
    async def execute(self, createTeacherTrainingDto:CreateTeacherTrainingDto, db: AsyncSession):

        if getattr(createTeacherTrainingDto, "secret", None) != os.getenv("SECRET_KEY", "dev_secret"):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect secret",
            )

        teacher_training_entity = createTeacherTrainingDto.to_entity(db=db)

        db.add(teacher_training_entity)
        await db.commit()
        await db.refresh(teacher_training_entity)

        return teacher_training_entity
