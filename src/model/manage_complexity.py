from sqlalchemy import Column, String, BigInteger
from src.infra.db import Base

class ManageComplexity(Base):
    __tablename__ = "manage_complexity"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    adminitrative_dependencie = Column(String(255), nullable=False)
    complexity_level = Column(String(255), nullable=False)
    school_name = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)

    def __repr__(self):
        return (
            f"<ManageComplexity(id={self.id}, adminitrative_dependencie={self.adminitrative_dependencie}, "
            f"complexity_level={self.complexity_level}, school_name={self.school_name}, city={self.city})>"
        )
