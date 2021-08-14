from typing import Any, List, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from .user import User, UserBase
# Shared properties
class ResiBase(BaseModel):
    tracking_name: str
    item_name: Optional[str] = None
    redirect_url: Optional[str] = None
    maps_url: Optional[str] = None
    sending_address: Optional[str] = None
    receiving_address: Optional[str] = None
    sending_country: Optional[str] = None
    receiving_country: Optional[str] = None
    class Config:
        orm_mode = True



class ResiInDBBase(ResiBase):
    id: Optional[int] = None

class UserResiBase(BaseModel):
    retrieve_timestamp: datetime
    class Config:
        orm_mode = True

class UserResiInDBBase(UserResiBase):
    id: Optional[int] = None

# Additional properties to return via API
class Resi(ResiInDBBase):
    driver: User
    pass
class StatusBase(BaseModel):
    status: str
    class Config:
        orm_mode = True

class UserResiHistoryBase(BaseModel):
    status: StatusBase
    created_timestamp: datetime
    class Config:
        orm_mode = True

class UserResi(UserResiInDBBase):
    user_resi_history: List[UserResiHistoryBase]
    pass

# Properties to receive on item creation
class ResiCreate(ResiBase):
    pass


# Properties to receive on item update
class ResiUpdate(ResiBase):
    pass

# Properties to receive on item creation
class UserResiCreate(UserResiBase):
    pass


# Properties to receive on item update
class UserResiUpdate(UserResiBase):
    pass

# Properties to receive on item creation
class UserResiHistoryCreate(UserResiHistoryBase):
    pass


# Properties to receive on item update
class UserResiHistoryUpdate(UserResiHistoryBase):
    pass
class UserResiDetail(UserResi):
    user: User
    resi: Resi

class UserResiGet(UserResi):
    user: UserBase
    resi: ResiBase