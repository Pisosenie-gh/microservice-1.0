from typing import List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.position import Position
from app.schemas.position import PositionCreate, PositionUpdate, PositionCreate

class CRUDPosition(CRUDBase[Position, PositionCreate, PositionUpdate]):
    def create(
        self, db: Session, *, obj_in: PositionCreate
    ) -> Position:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


position = CRUDPosition(Position)


