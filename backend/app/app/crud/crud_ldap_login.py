
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase


from app.models.ldap_login import LdapLogin
from app.schemas.ldap_login import LdapLoginCreate, LdapLoginUpdate

class CRUDLdapLogin(CRUDBase[LdapLogin, LdapLoginCreate, LdapLoginUpdate]):
    def create(
        self, db: Session, *, obj_in: LdapLoginCreate
    ) -> LdapLogin:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


ldap_login = CRUDLdapLogin(LdapLogin)


