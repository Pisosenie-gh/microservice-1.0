from typing import Any, List


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.InternalEmployee])
def read_internal_employee(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    iin: str = "", 
    personnelNumber: str = "",
    login: str = ""

) -> Any:
    """
    <b>Возвращает массив внутренних внешних сотрудников</b><br>Если не указан ни один из фильтрующих параметров (iin, login, personnel_number), 
    то возвращается полный список внешних сотрудников<br>Поддерживается ограничение результатов выдачи при помощи параметров <b>skip</b> и <b>limit</b>
    """
    if iin is not None and iin is not "" :
        if (personnelNumber is "" or personnelNumber is None) and (login is "" or login is None):
            internal_employee = crud.internal_employee.get_by_iin(db, iin=iin)
            return internal_employee
        elif (personnelNumber is not None and personnelNumber is not "") and (login is "" or login is None):
            internal_employee = crud.internal_employee.get_by_iin_and_personnelNumber(db, iin=iin, personnelNumber=personnelNumber)
            return internal_employee            
        elif (login is not None and login is not "") and (personnelNumber is "" or personnelNumber is None):
            internal_employee = crud.internal_employee.get_by_iin_and_login(db, iin=iin, login=login)
            return internal_employee              
    
        else:
            internal_employee = crud.internal_employee.get_by_all(db, iin=iin, login=login, personnelNumber=personnelNumber)
            return internal_employee

    elif personnelNumber is not None and personnelNumber is not "" :

        if login is "" or login is None:
            internal_employee = crud.internal_employee.get_by_personnelNumber(db, personnelNumber=personnelNumber)
            return internal_employee

        elif login is not None and login is not "":
            internal_employee = crud.internal_employee.get_by_personnelNumber_and_login(db, personnelNumber=personnelNumber, login=login)
            return internal_employee   

    elif login is not None and login is not "" :
        internal_employee = crud.internal_employee.get_by_login(db, login=login)
        return internal_employee

    else:
        internal_employee = crud.internal_employee.get_multi(db, skip=skip, limit=limit)


    return internal_employee

@router.post("/", response_model=schemas.InternalEmployee)
def create_internal_employee(
    *,
    db: Session = Depends(deps.get_db),
    internal_employee_in: schemas.InternalEmployeeCreate,

) -> Any:
    """
    Добавление записи грейдов
    """
    internal_employee = crud.internal_employee.create(db=db, obj_in=internal_employee_in)
    return internal_employee


@router.put("/{id}", response_model=schemas.InternalEmployee)
def update_internal_employee(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    internal_employee_in: schemas.InternalEmployeeUpdate,
) -> Any:
    """
    Обновление записи грейдов
    """
    internal_employee = crud.internal_employee.get(db=db, id=id)
    if not internal_employee:
        raise HTTPException(status_code=404,  detail="internal_employee {id} not found ".format(id=id))

    internal_employee = crud.internal_employee.update(db=db, db_obj=internal_employee, obj_in=internal_employee_in)
    return internal_employee


@router.get("/{id}", response_model=schemas.InternalEmployee)
def read_internal_employee(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись грейдов по id
    """
    internal_employee = crud.internal_employee.get(db=db, id=id)
    if not internal_employee:
        raise HTTPException(status_code=404,  detail="internal_employee {id} not found ".format(id=id))

    return internal_employee


@router.patch("/{id}", response_model=schemas.InternalEmployee)
def patch_internal_employee(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    internal_employee_in: schemas.InternalEmployeePatch,
) -> Any:
    """
    Изменение статуса активности записи
    """
    internal_employee = crud.internal_employee.get(db=db, id=id)
    if not internal_employee:
        raise HTTPException(status_code=404, detail="internal_employee {id} not found ".format(id=id))

    internal_employee = crud.internal_employee.patch(db=db, db_obj=internal_employee, obj_in=internal_employee_in)
    return internal_employee