from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, crud
from database import SessionLocal

# from typing import List
# from models import Pill
print("pill_routes.py loaded")

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/pills", response_model=list[schemas.PillOut])
def read_pills(db: Session = Depends(get_db)):
    return crud.get_pills(db)

@router.get("/pills/{pill_id}", response_model=schemas.PillOut)
def read_pill(pill_id: int, db: Session = Depends(get_db)):
    db_pill = crud.get_pill(db, pill_id)
    if db_pill is None:
        raise HTTPException(status_code=404, detail="Pill not found")
    return db_pill

@router.post("/pills", response_model=schemas.PillOut)
def create_pill(pill: schemas.PillCreate, db: Session = Depends(get_db)):
    return crud.create_pill(db, pill)

@router.delete("/pills/{pill_id}")
def delete_pill(pill_id: int, db: Session = Depends(get_db)):
    pill = crud.delete_pill(db, pill_id)
    if not pill:
        raise HTTPException(status_code=404, detail="Pill not found")
    return {"ok": True}


# @router.get("/pills", response_model=List[Pill])
# def get_pills():
#     return crud.get_all_pills()

# @router.get("/pills/{pill_id}", response_model=Pill)
# def get_pill(pill_id: int):
#     pill = crud.get_pill_by_id(pill_id)
#     if pill:
#         return pill
#     raise HTTPException(status_code=404, detail="Pill not found")

# @router.post("/pills", response_model=Pill)
# def create_new_pill(pill: Pill):
#     return crud.create_pill(pill)

# @router.put("/pills/{pill_id}", response_model=Pill)
# def update_existing_pill(pill_id: int, pill: Pill):
#     updated = crud.update_pill(pill_id, pill)
#     if updated:
#         return updated
#     raise HTTPException(status_code=404, detail="Pill not found")

# @router.delete("/pills/{pill_id}")
# def delete_existing_pill(pill_id: int):
#     success = crud.delete_pill(pill_id)
#     if success:
#         return {"message": "Pill deleted"}
#     raise HTTPException(status_code=404, detail="Pill not found")