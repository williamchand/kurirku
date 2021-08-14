from .crud_item import item
from .crud_resi import resi, user_resi, user_resi_history
from .crud_user import user, user_photo

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
