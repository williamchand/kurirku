from typing import List
from datetime import  datetime
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.resi import Resi, UserResi, UserResiHistory
from app.schemas.resi import ResiCreate, ResiUpdate, UserResiCreate, UserResiUpdate


class CRUDResi(CRUDBase[Resi, ResiCreate, ResiUpdate]):
    # def create_with_owner(
    #     self, db: Session, *, obj_in: ItemCreate, owner_id: int
    # ) -> Item:
    #     obj_in_data = jsonable_encoder(obj_in)
    #     db_obj = self.model(**obj_in_data, owner_id=owner_id)
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj

    def get_resi_by_tracking_name(
        self, db: Session, *, tracking_name: int
    ) -> Resi:
        return (
            db.query(self.model)
            .filter(Resi.tracking_name == '#' + tracking_name)
            .first()
        )


resi = CRUDResi(Resi)

class CRUDUserResi(CRUDBase[UserResi, UserResiCreate, UserResiUpdate]):
    # def create_with_owner(
    #     self, db: Session, *, obj_in: ItemCreate, owner_id: int
    # ) -> Item:
    #     obj_in_data = jsonable_encoder(obj_in)
    #     db_obj = self.model(**obj_in_data, owner_id=owner_id)
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj

    def get_resi_by_user_id(
        self, db: Session, *, user_id: int
    ) -> List[UserResi]:
        return (
            db.query(self.model)
            .filter(UserResi.user_id == user_id).all()
        )

    def get_resi_by_driver_id(
        self, db: Session, *, driver_id: int
    ) -> List[UserResi]:
        return (
            db.query(self.model)
            .filter(UserResi.resi.has(driver_id=driver_id)).all()
        )


    def create_user_resi(
        self, db: Session, *, user_id: int, resi_id: int, retrieve_timestamp: datetime
    ) -> UserResi:
        obj_in_data = UserResi(
            user_id=user_id,
            resi_id=resi_id,
            retrieve_timestamp=retrieve_timestamp,
            user_resi_history=[UserResiHistory(status_id=1
            )]
        )
        db.add(obj_in_data)
        db.commit()
        db.refresh(obj_in_data)
        return obj_in_data

class CRUDUserResiHistory(CRUDBase[UserResiHistory, UserResiCreate, UserResiUpdate]):
    def get_latest_status_id(
        self, db: Session, *, user_resi_id: int
    ) -> UserResiHistory:
        return (
            db.query(self.model)
            .filter(UserResiHistory.user_resi_id == user_resi_id).order_by(UserResiHistory.status_id.desc()).first()
        )

    def update_resi_status(
        self, db: Session, *, user_resi_id: int, status_id: int
    ) -> UserResiHistory:
        obj_in_data = UserResiHistory(
            user_resi_id=user_resi_id,
            status_id=status_id,
        )
        db.add(obj_in_data)
        db.commit()
        db.refresh(obj_in_data)
        return obj_in_data

user_resi_history = CRUDUserResiHistory(UserResiHistory)
resi = CRUDResi(Resi)
user_resi = CRUDUserResi(UserResi)
