from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy import Enum as SAEnum
from enum import Enum as PyEnum
from sqlalchemy.orm import relationship
from app.db.database import Base

class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer,primary_key=True)
    