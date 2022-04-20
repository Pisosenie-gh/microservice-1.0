from typing import Union, Dict, Any, List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.appointment import Appointment
from app.models.ldap_login import LdapLogin
from app.schemas.appointment import AppointmentCreate, AppointmentUpdate, AppointmentPatch

class CRUDAppointment(CRUDBase[Appointment, AppointmentCreate, AppointmentUpdate]):
    def create(
        self, db: Session, *, obj_in: AppointmentCreate, id: int 
    ) -> Appointment:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, employeeId=id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100, id: int
    ) -> List[Appointment]:
        return db.query(self.model).filter(Appointment.employeeId==id).offset(skip).limit(limit).all()

    def patch(
        self,
        db: Session,
        *,
        db_obj: Appointment,
        obj_in: Union[AppointmentPatch, Dict[str, Any]]
    ) -> Appointment:
        data_dict = obj_in.dict(exclude_unset=True)

        for key, value in data_dict.items():
            setattr(db_obj, key, value)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


appointment = CRUDAppointment(Appointment)


