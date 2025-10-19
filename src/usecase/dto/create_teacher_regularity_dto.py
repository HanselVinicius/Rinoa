from pydantic import BaseModel
from src.model.teacher_regularity import TeacherRegularity

class CreateTeacherRegularityDto(BaseModel):
    adminitrative_dependencie: str
    average_regularity: float
    school_name: str
    city: str
    secret: str


    def to_entity(self):
        return TeacherRegularity(
            adminitrative_dependencie=self.adminitrative_dependencie,
            average_regularity=self.average_regularity,
            school_name=self.school_name,
            city=self.city
        )