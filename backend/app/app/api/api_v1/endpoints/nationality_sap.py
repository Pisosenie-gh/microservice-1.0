from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.NationalitySap])
def read_nationality_sap(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей справочника национальности SAP
    """

    nationality_sap = crud.nationality_sap.get_multi(db, skip=skip, limit=limit)


    return nationality_sap


@router.post("/", response_model=schemas.NationalitySap)
def create_nationality_sap(
    *,
    db: Session = Depends(deps.get_db),
    nationality_sap_in: schemas.NationalitySapCreate,

) -> Any:
    """
    Добавление записи справочника национальности SAP
    """
    nationality_sap = crud.nationality_sap.create(db=db, obj_in=nationality_sap_in)
    return nationality_sap


@router.put("/{id}", response_model=schemas.NationalitySap)
def update_nationality_sap(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    nationality_sap_in: schemas.NationalitySapUpdate,
) -> Any:
    """
    Обновление записи справочника национальности SAP
    """
    nationality_sap = crud.nationality_sap.get(db=db, id=id)
    if not nationality_sap:
        raise HTTPException(status_code=404, detail="nationality_sap {id} not found ".format(id=id))

    nationality_sap = crud.nationality_sap.update(db=db, db_obj=nationality_sap, obj_in=nationality_sap_in)
    return nationality_sap


@router.get("/{id}", response_model=schemas.NationalitySap)
def read_nationality_sap(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись справочника национальности SAP по id
    """
    nationality_sap = crud.nationality_sap.get(db=db, id=id)
    if not nationality_sap:
        raise HTTPException(status_code=404, detail="nationality_sap {id} not found ".format(id=id))

    return nationality_sap


@router.patch("/{id}", response_model=schemas.NationalitySap)
def patch_nationality_sap(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    nationality_sap_in: schemas.ActivityPatch,
) -> Any:
    """
    Изменение статуса активности записи
    """
    nationality_sap = crud.nationality_sap.get(db=db, id=id)
    if not nationality_sap:
        raise HTTPException(status_code=404, detail="nationality_sap {id} not found ".format(id=id))

    nationality_sap = crud.nationality_sap.patch(db=db, db_obj=nationality_sap, obj_in=nationality_sap_in)
    return nationality_sap