from typing import Union, Dict, Any, List
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.internal_employee import InternalEmployee
from app.models.ldap_login import LdapLogin
from app.schemas.internal_employee import InternalEmployeeCreate, InternalEmployeeUpdate, InternalEmployeePatch

class CRUDInternalEmployee(CRUDBase[InternalEmployee, InternalEmployeeCreate, InternalEmployeeUpdate]):
    def create(
        self, db: Session, *, obj_in: InternalEmployeeCreate
    ) -> InternalEmployee:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj



    def patch(
        self,
        db: Session,
        *,
        db_obj: InternalEmployee,
        obj_in: Union[InternalEmployeePatch, Dict[str, Any]]
    ) -> InternalEmployee:
        data_dict = obj_in.dict(exclude_unset=True)

        for key, value in data_dict.items():
            setattr(db_obj, key, value)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_iin(
        self, db: Session, *, iin: str = ""
    ) -> List[InternalEmployee]:

        get_by_iin = (db.query(self.model)
                .filter(InternalEmployee.iin == iin)
                .all())
        return get_by_iin

    def get_by_iin_and_personnelNumber(
        self, db: Session, *, iin: str = "", personnelNumber: str = ""
    ) -> List[InternalEmployee]:
        get_by_iin_and_personal_number = (db.query(self.model).filter(InternalEmployee.iin == iin)
                    .filter(InternalEmployee.personnelNumber == personnelNumber)
                    .all())
        return get_by_iin_and_personal_number

    def get_by_iin_and_login(
        self, db: Session, *, iin: str = "", login: str = ""
    ) -> List[InternalEmployee]:
    
        get_by_iin_and_login = (db.query(self.model).join(LdapLogin).filter(LdapLogin.login == login)
                .filter(InternalEmployee.ldapLoginId == LdapLogin.id).filter(InternalEmployee.iin == iin)
                .all())

        return get_by_iin_and_login
        
    def get_by_personnelNumber(
        self, db: Session, *,  personnelNumber: str = ""
    ) -> List[InternalEmployee]:

        get_by_personnelNumber = (db.query(self.model)
                .filter(InternalEmployee.personnelNumber == personnelNumber)
                .all())
        return get_by_personnelNumber

    def get_by_personnelNumber_and_login(
        self, db: Session, *,  personnelNumber: str = "", login: str = ""
    ) -> List[InternalEmployee]:


        get_by_personnelNumber_and_login = (db.query(self.model).join(LdapLogin).filter(LdapLogin.login == login)
                .filter(InternalEmployee.ldapLoginId == LdapLogin.id).filter(InternalEmployee.personnelNumber == personnelNumber)
                .all())

        return get_by_personnelNumber_and_login

    def get_by_login(
            self, db: Session, *,  login: str = ""
        ) -> List[InternalEmployee]:
    
        get_by_login = (db.query(self.model).join(LdapLogin).filter(LdapLogin.login == login)
                .filter(InternalEmployee.ldapLoginId == LdapLogin.id)
                .all())

        return get_by_login


    def get_by_all(
            self, db: Session, *, iin: str = "", personnelNumber: str = "", login: str = ""
        ) -> List[InternalEmployee]:

        get_by_all = (db.query(self.model).join(LdapLogin).filter(LdapLogin.login == login)
                .filter(InternalEmployee.ldapLoginId == LdapLogin.id).filter(InternalEmployee.iin == iin)
                .filter(InternalEmployee.personnelNumber == personnelNumber).all())

        return get_by_all

internal_employee = CRUDInternalEmployee(InternalEmployee)


