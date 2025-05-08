
from sqlalchemy.orm import Session
import models, schemas

def get_pills(db: Session):
    return db.query(models.Pill).all()

def get_pill(db: Session, pill_id: int):
    return db.query(models.Pill).filter(models.Pill.id == pill_id).first()

def create_pill(db: Session, pill: schemas.PillCreate):
    db_pill = models.Pill(**pill.dict())
    db.add(db_pill)
    db.commit()
    db.refresh(db_pill)
    return db_pill

def delete_pill(db: Session, pill_id: int):
    pill = db.query(models.Pill).filter(models.Pill.id == pill_id).first()
    if pill:
        db.delete(pill)
        db.commit()
    return pill


# from models import Pill
# from database import pills

# def get_all_pills():
#     return pills

# def get_pill_by_id(pill_id: int):
#     for pill in pills:
#         if pill.id == pill_id:
#             return pill
#     return None

# def create_pill(pill: Pill):
#     pills.append(pill)
#     return pill

# def update_pill(pill_id: int, updated_pill: Pill):
#     for index, p in enumerate(pills):
#         if p.id == pill_id:
#             pills[index] = updated_pill
#             return updated_pill
#     return None

# def delete_pill(pill_id: int):
#     for pill in pills:
#         if pill.id == pill_id:
#             pills.remove(pill)
#             return True
#     return False


