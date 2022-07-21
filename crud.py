from sqlalchemy.orm import Session

from models import ItemModel
from schemas import Item

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ItemModel).offset(skip).limit(limit).all()