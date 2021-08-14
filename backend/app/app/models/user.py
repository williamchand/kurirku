from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base

if TYPE_CHECKING:
    from .resi import UserResi, Resi  # noqa: F401
    from .item import Item  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    user_photo = relationship("UserPhoto", back_populates="user")
    items = relationship("Item", back_populates="owner")
    driver_resi = relationship("Resi", back_populates="driver")
    user_resi = relationship("UserResi", back_populates="user")
    

class UserPhoto(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    photo = Column(String,  nullable=False)
    user = relationship("User", back_populates="user_photo")
    
