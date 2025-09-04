from sqlalchemy import BigInteger, Column, Date, String

from infra.db import Base


class Abscenses(Base):
    __tablename__ = "abscenses"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    absense_type = Column(String(255), nullable=False)
    absense_date = Column(Date, nullable=False)

    def __repr__(self):
        return f"<Abscenses(id={self.id}, name={self.name}, absense_type={self.absense_type}, absense_date={self.absense_date})>"
