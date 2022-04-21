
from email.policy import default

from sqlalchemy import Column,  Integer, String


from app.db.base_class import Base


class LdapLogin(Base):
    __tablename__ = 'ldap_login'

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String)
    isActive = Column(Integer, default=1)
