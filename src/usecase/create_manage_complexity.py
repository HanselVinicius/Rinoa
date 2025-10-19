import os
from fastapi import HTTPException, status

class CreateManageComplexity:
    async def execute(self, createManageComplexityDto, db):
        if getattr(createManageComplexityDto, "secret", None) != os.getenv("SECRET_KEY", "dev_secret"):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect secret",
            )

        entity = createManageComplexityDto.to_entity()
        db.add(entity)
        await db.commit()
        await db.refresh(entity)
        return entity
