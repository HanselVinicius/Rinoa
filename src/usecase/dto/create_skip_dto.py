from datetime import date, datetime
from pydantic import BaseModel, Field

from src.model.skips import Skips

class CreateSkipDto(BaseModel): 
    name: str
    reason: str
    skip_date:  date = Field(..., description="Data da ausência (YYYY-MM-DD)")
    timestamp: datetime = Field(..., description="Data e hora do registro (ISO 8601)")
    secret: str
    
    def to_entity(self) -> Skips:
        ts = self.timestamp.replace(tzinfo=None)
        return Skips(
            name=self.name,
            reason=self.reason,
            skip_date=self.skip_date,
            timestamp=ts,
        )