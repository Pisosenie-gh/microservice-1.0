


from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class MilitaryServiceAttitude(Base):
    __tablename__ = 'military_service_attitude'

    id = Column(Integer, primary_key=True, index=True)
    nameRu = Column(String)
    nameKz = Column(String)
    isActive = Column(Integer, default=1)

