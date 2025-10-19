from sqlalchemy import Column, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.db import Base

class ElementarySchool(Base):
    __tablename__ = "elementary_school"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)

    total_id = Column(BigInteger, ForeignKey("percent_groups.id"))
    initial_years_id = Column(BigInteger, ForeignKey("percent_groups.id"))
    final_years_id = Column(BigInteger, ForeignKey("percent_groups.id"))

    total = relationship("PercentGroups", foreign_keys=[total_id])
    initial_years = relationship("PercentGroups", foreign_keys=[initial_years_id])
    final_years = relationship("PercentGroups", foreign_keys=[final_years_id])
