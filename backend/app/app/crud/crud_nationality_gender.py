
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.nationality_gender import NationalityGender
from app.schemas.nationality_gender import NationalityGenderCreate,NationalityGenderUpdate


class CRUDNationalityGender(CRUDBase[NationalityGender, NationalityGenderCreate, NationalityGenderUpdate]):
    def create(
        self, db: Session, *, obj_in: NationalityGenderCreate
    ) -> NationalityGender:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

nationality_gender = CRUDNationalityGender(NationalityGender)


