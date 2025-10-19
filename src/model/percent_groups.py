from sqlalchemy import Column, Float, BigInteger, ForeignKey
from src.infra.db import Base

class PercentGroups(Base):
    __tablename__ = "percent_groups"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    group_1 = Column(Float)
    group_2 = Column(Float)
    group_3 = Column(Float)
    group_4 = Column(Float)
    group_5 = Column(Float)
