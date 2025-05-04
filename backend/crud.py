from models import Pill
from database import pills

def get_all_pills():
    return pills

def get_pill_by_id(pill_id: int):
    for pill in pills:
        if pill.id == pill_id:
            return pill
    return None

def create_pill(pill: Pill):
    pills.append(pill)
    return pill

def update_pill(pill_id: int, updated_pill: Pill):
    for index, p in enumerate(pills):
        if p.id == pill_id:
            pills[index] = updated_pill
            return updated_pill
    return None

def delete_pill(pill_id: int):
    for pill in pills:
        if pill.id == pill_id:
            pills.remove(pill)
            return True
    return False
