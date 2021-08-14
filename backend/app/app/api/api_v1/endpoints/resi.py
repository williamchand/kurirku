from datetime import timedelta
from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core import security
from app.core.config import settings

router = APIRouter()

@router.get("/{tracking_name}", response_model=schemas.Resi)
def resi_details(
    tracking_name: str,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve items.
    """
    resi_detail = crud.resi.get_resi_by_tracking_name(
        db=db, tracking_name=tracking_name
    )
    return resi_detail


@router.put("/{tracking_name}", response_model=schemas.UserResi)
def resi_details(
    tracking_name: str,
    user_resi_in: schemas.UserResiUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve items.
    """
    resi_detail = crud.resi.get_resi_by_tracking_name(
        db=db, tracking_name=tracking_name
    )
    user_resi = crud.user_resi.create_user_resi(
        db=db,user_id=current_user.id,resi_id=resi_detail.id, retrieve_timestamp=user_resi_in.retrieve_timestamp
    )
    return user_resi


@router.get("/history/{user_resi_id}", response_model=schemas.UserResiDetail)
def resi_details(
    user_resi_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve resi details.
    """
    resi_detail = crud.user_resi.get(db, id=user_resi_id)
    return resi_detail


@router.get("/user/history/", response_model=List[schemas.UserResiGet])
def resi_details(
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve resi details.
    """
    resi_detail = crud.user_resi.get_resi_by_user_id(db, user_id=current_user.id)
    return resi_detail

@router.get("/driver/history/", response_model=List[schemas.UserResiGet])
def resi_details(
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve resi details.
    """
    resi_detail = crud.user_resi.get_resi_by_driver_id(db, driver_id=current_user.id)
    return resi_detail


@router.put("/driver/history/{user_resi_id}", response_model=schemas.UserResiDetail)
def resi_details(
    user_resi_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve resi details.
    """
    user_history_status = crud.user_resi_history.get_latest_status_id(db, user_resi_id=user_resi_id)
    if user_history_status and user_history_status.status_id < 4:
        crud.user_resi_history.update_resi_status(db, user_resi_id=user_resi_id, status_id=user_history_status.status_id + 1)
    resi_detail = crud.user_resi.get(db, id=user_resi_id)
    return resi_detail
