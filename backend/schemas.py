from pydantic import BaseModel

class PillBase(BaseModel):
    name: str
    dosage: str
    time: str

class PillCreate(PillBase):
    pass

class PillOut(PillBase):
    id: int

    class Config:
        orm_mode = True
