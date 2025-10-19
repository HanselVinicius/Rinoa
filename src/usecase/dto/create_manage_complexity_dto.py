from pydantic import BaseModel
from src.model.manage_complexity import ManageComplexity

class CreateManageComplexityDto(BaseModel):
    adminitrative_dependencie: str
    complexity_level: str
    school_name: str
    city: str
    secret: str


    def to_entity(self):
        return ManageComplexity(
            adminitrative_dependencie=self.adminitrative_dependencie,
            complexity_level=self.complexity_level,
            school_name=self.school_name,
            city=self.city
        )
