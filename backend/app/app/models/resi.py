from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class Resi(Base):
    id = Column(Integer, primary_key=True, index=True)
    tracking_name = Column(String, index=True)
    driver_id = Column(Integer, ForeignKey("user.id"))
    redirect_url = Column(String, nullable=True)
    maps_url = Column(String, nullable=True)
    sending_address = Column(String, nullable=True)
    receiving_address = Column(String, nullable=True)
    sending_country = Column(String, nullable=True)
    receiving_country = Column(String, nullable=True)
    driver = relationship("User", back_populates="resiList")
