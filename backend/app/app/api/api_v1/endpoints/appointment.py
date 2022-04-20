from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/{id}/appointment/", response_model=List[schemas.Appointment])
def read_appointment(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    id: int = None

) -> Any:
    """
    <b>Возвращает массив записей назначений сотрудника</b>
    <br>Поддерживается ограничение результатов выдачи при помощи параметров <b>skip</b> и <b>limit</b>
    """

    appointment = crud.appointment.get_multi(db, skip=skip, limit=limit, id=id)


    return appointment


@router.post("/{id}/appointment/", response_model=schemas.Appointment)
def create_appointment(
    *,
    db: Session = Depends(deps.get_db),
    appointment_in: schemas.AppointmentCreate,
    id: int

) -> Any:
    """
    Добавление записи назначения
    """
    appointment = crud.appointment.create(db=db, obj_in=appointment_in, id=id)
    return appointment


@router.put("/appointment/{id}", response_model=schemas.Appointment)
def update_appointment(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    appointment_in: schemas.AppointmentUpdate,
) -> Any:
    """
    Обновление записи назначения
    """
    appointment = crud.appointment.get(db=db, id=id)
    if not appointment:
        raise HTTPException(status_code=404, detail="appointment {id} not found ".format(id=id))

    appointment = crud.appointment.update(db=db, db_obj=appointment, obj_in=appointment_in)
    return appointment


@router.get("/appointment/{id}", response_model=schemas.Appointment)
def read_appointment(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись назначения по его id
    """
    appointment = crud.appointment.get(db=db, id=id)
    if not appointment:
        raise HTTPException(status_code=404, detail="appointment {id} not found ".format(id=id))

    return appointment


@router.patch("/appointment/{id}", response_model=schemas.Appointment)
def patch_appointment(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    appointment_in: schemas.AppointmentPatch,
) -> Any:
    """
    Корректировка записи назначения
    """
    appointment = crud.appointment.get(db=db, id=id)
    if not appointment:
        raise HTTPException(status_code=404, detail="appointment {id} not found ".format(id=id))

    appointment = crud.appointment.patch(db=db, db_obj=appointment, obj_in=appointment_in)
    return appointment