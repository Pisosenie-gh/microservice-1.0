
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import List, Dict, Any, Union

from app.crud.base import CRUDBase


from app.models.military_service_attitude import MilitaryServiceAttitude
from app.schemas.military_service_attitude import MilitaryServiceAttitudeCreate, MilitaryServiceAttitudeUpdate
from app.schemas.activity_patch import ActivityPatch


class CRUDMilitaryServiceAttitude(CRUDBase[MilitaryServiceAttitude, MilitaryServiceAttitudeCreate, MilitaryServiceAttitudeUpdate]):
    def create(
        self, db: Session, *, obj_in: MilitaryServiceAttitudeCreate
    ) -> MilitaryServiceAttitude:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj



military_service_attitude = CRUDMilitaryServiceAttitude(MilitaryServiceAttitude)


