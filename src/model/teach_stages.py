from sqlalchemy import Column, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.db import Base

class TeachStages(Base):
    __tablename__ = "teach_stages"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    early_education_id = Column(BigInteger, ForeignKey("percent_groups.id"))
    elementary_school_id = Column(BigInteger, ForeignKey("elementary_school.id"))
    middle_school_id = Column(BigInteger, ForeignKey("percent_groups.id"))
    eja_id = Column(BigInteger, ForeignKey("percent_groups.id"))

    early_education = relationship("PercentGroups", foreign_keys=[early_education_id])
    elementary_school = relationship("ElementarySchool", foreign_keys=[elementary_school_id])
    middle_school = relationship("PercentGroups", foreign_keys=[middle_school_id])
    eja = relationship("PercentGroups", foreign_keys=[eja_id])
