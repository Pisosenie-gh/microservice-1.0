
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.staff_unit import StaffUnit
from app.schemas.staff_unit import StaffUnitCreate, StaffUnitUpdate


class CRUDStaffUnit(CRUDBase[StaffUnit, StaffUnitCreate, StaffUnitUpdate]):
    def create(
        self, db: Session, *, obj_in: StaffUnitCreate
    ) -> StaffUnit:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj



staff_unit = CRUDStaffUnit(StaffUnit)


