from pydantic import BaseModel
from src.usecase.dto.create_teach_stages_dto import CreateTeachStagesDto
from src.model.teacher_training import TeacherTraining

class CreateTeacherTrainingDto(BaseModel):
    teach_stages: CreateTeachStagesDto
    adminitrative_dependencie: str
    school_name: str
    city: str
    secret: str

    def to_entity(self, db):
        stages_entity = self.teach_stages.to_entity(db=db)
        db.add(stages_entity)
        return TeacherTraining(
            teach_stages=stages_entity,
            adminitrative_dependencie=self.adminitrative_dependencie,
            school_name=self.school_name,
            city=self.city
        )
