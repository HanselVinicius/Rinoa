from sqlalchemy import Column, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.db import Base

class TeacherTraining(Base):
    __tablename__ = "teacher_training"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    teach_stages_id = Column(BigInteger, ForeignKey("teach_stages.id"))

    adminitrative_dependencie = Column(String(255), nullable=False)
    school_name = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)

    teach_stages = relationship("TeachStages", foreign_keys=[teach_stages_id])
