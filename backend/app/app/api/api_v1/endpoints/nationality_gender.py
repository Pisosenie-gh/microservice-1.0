from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.NationalityGender])
def read_nationality_gender(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,

) -> Any:
    """
    Возвращает массив записей родов национальности
    """

    nationality_gender = crud.nationality_gender.get_multi(db, skip=skip, limit=limit)


    return nationality_gender


@router.post("/", response_model=schemas.NationalityGender)
def create_nationality_gender(
    *,
    db: Session = Depends(deps.get_db),
    nationality_gender_in: schemas.NationalityGenderCreate,

) -> Any:
    """
    Добавление записи родов национальности
    """
    nationality_gender = crud.nationality_gender.create(db=db, obj_in=nationality_gender_in)
    return nationality_gender


@router.put("/{id}", response_model=schemas.NationalityGender)
def update_nationality_gender(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    nationality_gender_in: schemas.NationalityGenderUpdate,
) -> Any:
    """
    Обновление записи родов национальности
    """
    nationality_gender = crud.nationality_gender.get(db=db, id=id)
    if not nationality_gender:
        raise HTTPException(status_code=404, detail="nationality_gender {id} not found ".format(id=id))

    nationality_gender = crud.nationality_gender.update(db=db, db_obj=nationality_gender, obj_in=nationality_gender_in)
    return nationality_gender


@router.get("/{id}", response_model=schemas.NationalityGender)
def read_nationality_gender(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись родов национальности по id
    """
    nationality_gender = crud.nationality_gender.get(db=db, id=id)
    if not nationality_gender:
        raise HTTPException(status_code=404, detail="nationality_gender {id} not found ".format(id=id))

    return nationality_gender


@router.patch("/{id}", response_model=schemas.NationalityGender)
def patch_nationality_gender(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    nationality_gender_in: schemas.ActivityPatch,
) -> Any:
    """
    Изменение статуса активности записи
    """
    nationality_gender = crud.nationality_gender.get(db=db, id=id)
    if not nationality_gender:
        raise HTTPException(status_code=404, detail="nationality_gender {id} not found ".format(id=id))

    nationality_gender = crud.nationality_gender.patch(db=db, db_obj=nationality_gender, obj_in=nationality_gender_in)
    return nationality_gender