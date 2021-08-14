from typing import TYPE_CHECKING
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
import datetime

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Resi(Base):
    __tablename__ = 'resi'
    id = Column(Integer, primary_key=True, index=True)
    tracking_name = Column(String, index=True)
    driver_id = Column(Integer, ForeignKey("user.id"))
    redirect_url = Column(String, nullable=True)
    maps_url = Column(String, nullable=True)
    sending_address = Column(String, nullable=True)
    receiving_address = Column(String, nullable=True)
    sending_country = Column(String, nullable=True)
    receiving_country = Column(String, nullable=True)
    driver = relationship("User", back_populates="driver_resi")
    resi_user = relationship("UserResi", back_populates="resi")

class UserResi(Base):
    __tablename__ = 'user_resi'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    resi_id = Column(Integer, ForeignKey("resi.id"))
    user = relationship("User", back_populates="user_resi")
    resi = relationship("Resi", back_populates="resi_user")
    user_resi_history = relationship("UserResiHistory", back_populates="user_resi")

class StatusResi(Base):
    __tablename__ = 'status_resi'
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, nullable=False)
    
class UserResiHistory(Base):
    __tablename__ = 'user_resi_history'
    id = Column(Integer, primary_key=True, index=True)
    user_resi_id = Column(Integer, ForeignKey("user_resi.id"), nullable=False)
    status_id = Column(Integer, ForeignKey("status_resi.id"), nullable=False)
    created_timestamp = Column(TIMESTAMP, default=datetime.datetime.utcnow, nullable=False)
    user_resi = relationship("UserResi", back_populates="user_resi_history")
    status = relationship("StatusResi")
    