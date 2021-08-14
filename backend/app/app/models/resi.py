from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class Resi(Base):
        sa.column("id", sa.Integer),
        sa.column("tracking_name", sa.String),
        sa.column("driver_id", sa.Integer),
        sa.column("redirect_url", sa.String),
        sa.column("maps_url", sa.String),
        sa.column("sending_address", sa.String),
        sa.column("receiving_address", sa.String),
        sa.column("sending_country", sa.String),
        sa.column("receiving_country", sa.String),
    id = Column(Integer, primary_key=True, index=True)
    tracking_name = Column(String, index=True)
    email = Column(String, unique=True,  nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")
