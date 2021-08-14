# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.item import Item
from app.models.user import User, UserPhoto
from app.models.resi import Resi, UserResi, StatusResi, UserResiHistory

