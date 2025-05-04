from fastapi import APIRouter, HTTPException
from typing import List
from models import Pill
import crud

router = APIRouter()

@router.get("/pills", response_model=List[Pill])
def get_pills():
    return crud.get_all_pills()

@router.get("/pills/{pill_id}", response_model=Pill)
def get_pill(pill_id: int):
    pill = crud.get_pill_by_id(pill_id)
    if pill:
        return pill
    raise HTTPException(status_code=404, detail="Pill not found")

@router.post("/pills", response_model=Pill)
def create_new_pill(pill: Pill):
    return crud.create_pill(pill)

@router.put("/pills/{pill_id}", response_model=Pill)
def update_existing_pill(pill_id: int, pill: Pill):
    updated = crud.update_pill(pill_id, pill)
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="Pill not found")

@router.delete("/pills/{pill_id}")
def delete_existing_pill(pill_id: int):
    success = crud.delete_pill(pill_id)
    if success:
        return {"message": "Pill deleted"}
    raise HTTPException(status_code=404, detail="Pill not found")