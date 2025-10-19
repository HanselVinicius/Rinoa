from pydantic import BaseModel
from src.usecase.dto.create_percent_groups_dto import CreatePercentGroupsDto
from src.model.elementary_school import ElementarySchool

class CreateElementarySchoolDto(BaseModel):
    total: CreatePercentGroupsDto
    initial_years: CreatePercentGroupsDto
    final_years: CreatePercentGroupsDto

    def to_entity(self, db):
        total = self.total.to_entity()
        initial = self.initial_years.to_entity()
        final = self.final_years.to_entity()

        db.add_all([total, initial, final])
        return ElementarySchool(
            total=total,
            initial_years=initial,
            final_years=final
        )
