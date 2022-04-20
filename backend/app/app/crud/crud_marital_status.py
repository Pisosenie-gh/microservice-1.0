from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.marital_status import MaritalStatus
from app.schemas.marital_status import MaritalStatusCreate, MaritalStatusUpdate


class CRUDMaritalStatus(CRUDBase[MaritalStatus, MaritalStatusCreate, MaritalStatusUpdate]):
    def create(
        self, db: Session, *, obj_in: MaritalStatusCreate
    ) -> MaritalStatus:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


marital_status = CRUDMaritalStatus(MaritalStatus)


