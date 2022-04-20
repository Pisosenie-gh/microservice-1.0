from typing import List, Any, Optional

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.employee_status import EmployeeStatus


class CRUDEmployeeStatus(CRUDBase[EmployeeStatus, None, None]):
    pass

employee_status = CRUDEmployeeStatus(EmployeeStatus)


