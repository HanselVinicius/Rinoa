from datetime import date, datetime

from pydantic import BaseModel, Field

from src.model.abscenses import Abscenses


class CreateAbscenseDto(BaseModel):
    name: str
    absense_type: str
    absense_date: date = Field(..., description="Data da ausência (YYYY-MM-DD)")
    timestamp: datetime = Field(..., description="Data e hora do registro (ISO 8601)")
    secret: str

    def to_entity(self) -> Abscenses:
        ts = self.timestamp.replace(tzinfo=None)
        return Abscenses(
            name=self.name,
            absense_type=self.absense_type,
            absense_date=self.absense_date,
            timestamp=ts,
        )
