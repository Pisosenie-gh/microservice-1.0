from typing import List, Any, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.staff_unit_type import StaffUnitType


class CRUDStaffUnitType(CRUDBase[StaffUnitType, None, None]):
    pass

staff_unit_type = CRUDStaffUnitType(StaffUnitType)


