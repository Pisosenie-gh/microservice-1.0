from typing import Any, List


from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from random import random
from app import crud, models, schemas
from app.api import deps
import logging



def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    file_handler = logging.FileHandler('././log/api.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

logger = setup_logger()



router = APIRouter()

@router.get("/", response_model=List[schemas.InternalEmployee])
def read_internal_employee(
    request: Request,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    iin: str = "", 
    personnelNumber: str = "",
    login: str = "",
    


) -> Any:
    """
    <b>Возвращает массив внутренних внешних сотрудников</b><br>Если не указан ни один из фильтрующих параметров (iin, login, personnel_number), 
    то возвращается полный список внешних сотрудников<br>Поддерживается ограничение результатов выдачи при помощи параметров <b>skip</b> и <b>limit</b>
    """

    try: 
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

        logger.info(f"GET url={request.url._url} , status_code = {status.HTTP_200_OK}" )
        return internal_employee

    except Exception as e: 
        
        logger.warning(f"GET url={request.url._url}, {e}")
        return {'message': str(e)}
    
    

@router.post("/", response_model=schemas.InternalEmployee)
def create_internal_employee(
    *,
    db: Session = Depends(deps.get_db),
    internal_employee_in: schemas.InternalEmployeeCreate,
    request: Request,

) -> Any:
    """
    Добавление записи внутреннего сотрудника

    """
    try: 
        internal_employee = crud.internal_employee.create(db=db, obj_in=internal_employee_in)
        
  
        logger.info(f"POST url={request.url._url} , status_code = {status.HTTP_201_CREATED}" )
        return internal_employee
    except Exception as e: 
        logger.warning(f"POST url={request.url._url}, {e}")
        return {'message': str(e)}
    
        


@router.put("/{id}", response_model=schemas.InternalEmployee)
def update_internal_employee(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    internal_employee_in: schemas.InternalEmployeeUpdate,
    request: Request,
) -> Any:
    """
    Обновление записи внутреннего сотрудника
    """
    try: 
        internal_employee = crud.internal_employee.get(db=db, id=id)
        if not internal_employee:
            logger.info(f"PUT url={request.url._url}, status_code = 404")
            raise HTTPException(status_code=404,  detail="internal_employee {id} not found ".format(id=id))

        internal_employee = crud.internal_employee.update(db=db, db_obj=internal_employee, obj_in=internal_employee_in)
        logger.info(f"PUT url={request.url._url} , status_code = {status.HTTP_200_OK}" )
        return internal_employee

    except Exception as e: 
        logger.warning(f"PUT url={request.url._url}, {e}")
        return {'message': str(e)}

@router.get("/{id}", response_model=schemas.InternalEmployee)
def read_internal_employee(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    request: Request,
) -> Any:
    """
    Возвращает запись внутреннего сотрудника по его id
    """
    try: 
        internal_employee = crud.internal_employee.get(db=db, id=id)
        if not internal_employee:
            logger.info(f"GET url={request.url._url}, status_code = 404")
            raise HTTPException(status_code=404,  detail="internal_employee {id} not found ".format(id=id))
        logger.info(f"GET url={request.url._url}, status_code = {status.HTTP_200_OK}")
        return internal_employee
    except Exception as e: 
        logger.warning(f"GET url={request.url._url}, {e}")
        return {'message': str(e)}

@router.patch("/{id}", response_model=schemas.InternalEmployee)
def patch_internal_employee(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    internal_employee_in: schemas.InternalEmployeePatch,
    request: Request,
) -> Any:
    """
    Корректировка записи внутреннего сотрудника
    """
    try: 
        internal_employee = crud.internal_employee.get(db=db, id=id)
        if not internal_employee:
            logger.info(f"PATCH url={request.url._url}, status_code = 404")
            raise HTTPException(status_code=404, detail="internal_employee {id} not found ".format(id=id))

        internal_employee = crud.internal_employee.patch(db=db, db_obj=internal_employee, obj_in=internal_employee_in)
        logger.info(f"PATCH url={request.url._url}, status_code = {status.HTTP_200_OK}")
        return internal_employee
    except Exception as e: 
        logger.warning(f"PATCH url={request.url._url}, {e}")
        return {'message': str(e)}