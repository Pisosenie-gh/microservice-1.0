from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.MilitaryServiceAttitude])
def read_military_service_attitude(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей отношений к воинской службе
    """

    military_service_attitude = crud.military_service_attitude.get_multi(db, skip=skip, limit=limit)


    return military_service_attitude



@router.post("/", response_model=schemas.MilitaryServiceAttitude)
def create_military_service_attitude(
    *,
    db: Session = Depends(deps.get_db),
    grade_in: schemas.MilitaryServiceAttitudeCreate,

) -> Any:
    """
    Добавление записи отношений к воинской службе
    """
    military_service_attitude = crud.military_service_attitude.create(db=db, obj_in=grade_in)
    return military_service_attitude


@router.put("/{id}", response_model=schemas.MilitaryServiceAttitude)
def update_military_service_attitude(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    grade_in: schemas.MilitaryServiceAttitudeUpdate,
) -> Any:
    """
    Обновление записи отношений к воинской службе
    """
    military_service_attitude = crud.military_service_attitude.get(db=db, id=id)
    if not military_service_attitude:
        raise HTTPException(status_code=404, detail="military_service_attitude {id} not found ".format(id=id))

    military_service_attitude = crud.military_service_attitude.update(db=db, db_obj=military_service_attitude, obj_in=grade_in)
    return military_service_attitude


@router.get("/{id}", response_model=schemas.MilitaryServiceAttitude)
def read_military_service_attitude(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись отношений к воинской службе по id
    """
    military_service_attitude = crud.military_service_attitude.get(db=db, id=id)
    if not military_service_attitude:
        raise HTTPException(status_code=404, detail="military_service_attitude {id} not found ".format(id=id))

    return military_service_attitude


@router.patch("/{id}", response_model=schemas.MilitaryServiceAttitude)
def patch_military_service_attitude(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    military_service_attitude_in: schemas.ActivityPatch,
) -> Any:
    """
    Изменение статуса активности записи
    """
    military_service_attitude = crud.military_service_attitude.get(db=db, id=id)
    if not military_service_attitude:
        raise HTTPException(status_code=404, detail="military_service_attitude {id} not found ".format(id=id))

    military_service_attitude = crud.military_service_attitude.patch(db=db, db_obj=military_service_attitude, obj_in=military_service_attitude_in)
    return military_service_attitude