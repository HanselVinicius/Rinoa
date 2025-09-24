from sqlalchemy import BigInteger, Column, Date, DateTime, String

from src.infra.db import Base


class Skips(Base):
    __tablename__ = "skips"

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    skip_date = Column(Date, nullable=False)
    reason = Column(String(255), nullable=False)
    timestamp = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Skips(id={self.id}, name={self.name}, skip_date={self.skip_date}, reason={self.reason}, timestamp={self.timestamp})>"