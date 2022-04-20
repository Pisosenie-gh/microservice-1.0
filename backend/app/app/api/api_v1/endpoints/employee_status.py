from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.EmployeeStatus])
def read_employee_status(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника статусов сотрудника
    """

    employee_status = crud.employee_status.get_multi(db, skip=skip, limit=limit)


    return employee_status

@router.get("/{id}", response_model=schemas.EmployeeStatus)
def read_employee_status(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника статуса сотрудника
    """
    employee_status = crud.employee_status.get(db=db, id=id)
    if not employee_status:
        raise HTTPException(status_code=404, detail="employee_status {id} not found ".format(id=id))

    return employee_status

