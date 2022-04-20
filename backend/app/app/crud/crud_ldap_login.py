
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from typing import Union, Dict, Any, List
from app.crud.base import CRUDBase

from app.schemas.internal_employee import InternalEmployeeAddLdap
from app.models.internal_employee import InternalEmployee
from app.models.ldap_login import LdapLogin
from app.schemas.ldap_login import LdapLoginCreate, LdapLoginUpdate

class CRUDLdapLogin(CRUDBase[LdapLogin, LdapLoginCreate, LdapLoginUpdate]):

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100, id:int
    ) -> List[LdapLogin]:
        get = (db.query(self.model).join(InternalEmployee).filter(InternalEmployee.id == id)
                .all())
        return get

    def patch_for_employee(
        self,
        db: Session,
        *,
        db_obj: InternalEmployee,
        obj_in: Union[InternalEmployeeAddLdap, Dict[str, Any]]
    ) -> InternalEmployee:
        data_dict = obj_in

        for key, value in data_dict.items():
            setattr(db_obj, key, value)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)


    def create(
        self, db: Session, *, obj_in: LdapLoginCreate, id:int
    ) -> LdapLogin:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        
        return db_obj


ldap_login = CRUDLdapLogin(LdapLogin)


