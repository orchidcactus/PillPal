from pydantic import BaseModel
from typing import Optional

class Pill(BaseModel):
    id: int
    name: str
    dosage: str
    time: str
    notes: Optional[str] = None
