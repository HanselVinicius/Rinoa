from pydantic import BaseModel
from src.usecase.dto.create_percent_groups_dto import CreatePercentGroupsDto
from src.usecase.dto.create_elementary_school_dto import CreateElementarySchoolDto
from src.model.teach_stages import TeachStages

class CreateTeachStagesDto(BaseModel):
    early_education: CreatePercentGroupsDto
    elementary_school: CreateElementarySchoolDto
    middle_school: CreatePercentGroupsDto
    eja: CreatePercentGroupsDto

    def to_entity(self, db):

        early = self.early_education.to_entity()
        middle = self.middle_school.to_entity()
        eja = self.eja.to_entity()
        elementary = self.elementary_school.to_entity(db=db)

        db.add_all([early, middle, eja])
        return TeachStages(
            early_education=early,
            elementary_school=elementary,
            middle_school=middle,
            eja=eja
        )
