from typing import List, Union, Dict, Any

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.replacement import Replacement
from app.schemas.replacement import ReplacementCreate, ReplacementUpdate, ReplacementPatch


class CRUDReplacement(CRUDBase[Replacement, ReplacementCreate, ReplacementUpdate]):
    def create(
        self, db: Session, *, obj_in: ReplacementCreate, id: int
    ) -> Replacement:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, replacedId=id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


    def patch(
        self,
        db: Session,
        *,
        db_obj: Replacement,
        obj_in: Union[ReplacementPatch, Dict[str, Any]]
    ) -> Replacement:
        obj_data = jsonable_encoder(db_obj)
        data_dict = obj_in.dict(exclude_unset=True)

        for key, value in data_dict.items():
            setattr(db_obj, key, value)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100, id: int
    ) -> List[Replacement]:
        return db.query(self.model).filter(Replacement.replacedId == id).offset(skip).limit(limit).all()


replacement = CRUDReplacement(Replacement)


