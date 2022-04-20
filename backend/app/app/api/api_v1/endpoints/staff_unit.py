from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/{id}/staff-unit/", response_model=List[schemas.StaffUnit])
def read_staff_unit(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    id: int = 0

) -> Any:
    """
    Возвращает массив записей  данных штатных единиц
    """

    staff_unit = crud.staff_unit.get_multi(db, skip=skip, limit=limit)


    return staff_unit



@router.post("/{id}/staff-unit/", response_model=schemas.StaffUnit)
def create_staff_unit(
    *,
    db: Session = Depends(deps.get_db),
    grade_in: schemas.StaffUnitCreate,

) -> Any:
    """
    Добавление записи штатной единицы
    """
    staff_unit = crud.staff_unit.create(db=db, obj_in=grade_in)
    return staff_unit


@router.put("/staff-unit/{id}", response_model=schemas.StaffUnit)
def update_staff_unit(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    grade_in: schemas.StaffUnitUpdate,
) -> Any:
    """
    Обновление записи штатной единицы
    """
    staff_unit = crud.staff_unit.get(db=db, id=id)
    if not staff_unit:
        raise HTTPException(status_code=404, detail="staff_unit {id} not found ".format(id=id))

    staff_unit = crud.staff_unit.update(db=db, db_obj=staff_unit, obj_in=grade_in)
    return staff_unit


@router.get("/staff-unit/{id}", response_model=schemas.StaffUnit)
def read_staff_unit(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись данных штатных единиц
    """
    staff_unit = crud.staff_unit.get(db=db, id=id)
    if not staff_unit:
        raise HTTPException(status_code=404, detail="staff_unit {id} not found ".format(id=id))

    return staff_unit


@router.patch("/staff-unit/{id}", response_model=schemas.StaffUnit)
def patch_staff_unit(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    staff_unit_in: schemas.ActivityPatch,
) -> Any:
    """
    Изменение статуса активности записи
    """
    staff_unit = crud.staff_unit.get(db=db, id=id)
    if not staff_unit:
        raise HTTPException(status_code=404, detail="staff_unit {id} not found ".format(id=id))

    staff_unit = crud.staff_unit.patch(db=db, db_obj=staff_unit, obj_in=staff_unit_in)
    return staff_unit