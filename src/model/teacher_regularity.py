from sqlalchemy import Column, String, BigInteger, Float
from src.infra.db import Base

class TeacherRegularity(Base):
    __tablename__ = "teacher_regularity"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    adminitrative_dependencie = Column(String(255), nullable=False)
    average_regularity = Column(Float, nullable=False)
    school_name = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)

    def __repr__(self):
        return (
            f"<TeacherRegularity(id={self.id}, adminitrative_dependencie={self.adminitrative_dependencie}, "
            f"average_regularity={self.average_regularity}, school_name={self.school_name}, city={self.city})>"
        )
