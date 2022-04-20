from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.StaffUnitType])
def read_staff_unit_type(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника типов штатной единицы
    """

    staff_unit_type = crud.staff_unit_type.get_multi(db, skip=skip, limit=limit)


    return staff_unit_type

@router.get("/{id}", response_model=schemas.StaffUnitType)
def read_staff_unit_type(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника типов штатных единиц по id
    """
    staff_unit_type = crud.staff_unit_type.get(db=db, id=id)
    if not staff_unit_type:
        raise HTTPException(status_code=404, detail="staff_unit_type {id} not found ".format(id=id))
    return staff_unit_type

