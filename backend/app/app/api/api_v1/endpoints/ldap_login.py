from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/{id}/ldap_login/", response_model=List[schemas.LdapLogin])
def read_ldap_login(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    id: int = None

) -> Any:
    """
    <b>Возвращает массив записей назначений сотрудника</b>
    <br>Поддерживается ограничение результатов выдачи при помощи параметров <b>skip</b> и <b>limit</b>
    """

    ldap_login = crud.ldap_login.get_multi(db, skip=skip, limit=limit, id=id)


    return ldap_login


@router.post("/{id}/ldap_login/", response_model=schemas.LdapLogin)
def create_ldap_login(
    *,
    db: Session = Depends(deps.get_db),
    ldap_login_in: schemas.LdapLoginCreate,
    id: int

) -> Any:
    """
    Добавление записи назначения
    """
    ldap_login = crud.ldap_login.create(db=db, obj_in=ldap_login_in, id=id)

    employee = crud.internal_employee.get(db=db, id=id)
    if not employee:
        raise HTTPException(status_code=404, detail="employee {id} not found ".format(id=id))

    employee = crud.ldap_login.patch_for_employee(db=db, db_obj=employee, obj_in={'ldapLoginId': ldap_login.id})


    return ldap_login


@router.put("/ldap_login/{id}", response_model=schemas.LdapLogin)
def update_ldap_login(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    ldap_login_in: schemas.LdapLoginUpdate,
) -> Any:
    """
    Обновление записи назначения
    """
    ldap_login = crud.ldap_login.get(db=db, id=id)
    if not ldap_login:
        raise HTTPException(status_code=404, detail="ldap_login {id} not found ".format(id=id))

    ldap_login = crud.ldap_login.update(db=db, db_obj=ldap_login, obj_in=ldap_login_in)
    return ldap_login


@router.get("/ldap_login/{id}", response_model=schemas.LdapLogin)
def read_ldap_login(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Возвращает запись назначения по его id
    """
    ldap_login = crud.ldap_login.get(db=db, id=id)
    if not ldap_login:
        raise HTTPException(status_code=404, detail="ldap_login {id} not found ".format(id=id))

    return ldap_login


@router.patch("/ldap_login/{id}", response_model=schemas.LdapLogin)
def patch_ldap_login(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    ldap_login_in: schemas.ActivityPatch,
) -> Any:
    """
    Корректировка записи назначения
    """
    ldap_login = crud.ldap_login.get(db=db, id=id)
    if not ldap_login:
        raise HTTPException(status_code=404, detail="ldap_login {id} not found ".format(id=id))

    ldap_login = crud.ldap_login.patch(db=db, db_obj=ldap_login, obj_in=ldap_login_in)
    return ldap_login