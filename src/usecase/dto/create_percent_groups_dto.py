from pydantic import BaseModel
from src.model.percent_groups import PercentGroups

class CreatePercentGroupsDto(BaseModel):
    group_1: float | None = None
    group_2: float | None = None
    group_3: float | None = None
    group_4: float | None = None
    group_5: float | None = None

    def to_entity(self):
        return PercentGroups(
            group_1=self.group_1,
            group_2=self.group_2,
            group_3=self.group_3,
            group_4=self.group_4,
            group_5=self.group_5
        )
