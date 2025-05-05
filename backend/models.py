from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String
from database import Base

class Pill(BaseModel):
    id: int
    name: str
    dosage: str
    time: str
    notes: Optional[str] = None

class Pill(Base):
    __tablename__ = "pills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    dosage = Column(String)
    time = Column(String)
    notes = Column(String, nullable=True)

