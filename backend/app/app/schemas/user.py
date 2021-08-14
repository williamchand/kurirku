from typing import Any, Optional

from pydantic import BaseModel, EmailStr

class UserPhotoBase(BaseModel):
    photo: str

    class Config:
        orm_mode = True

# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None




# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None



class UserPhotoCreate(UserPhotoBase):
    user_id: int
    photo: str

# Properties to receive via API on update
class UserPhotoUpdate(UserPhotoBase):
    photo: str

class UserInDBBase(UserBase):
    id: Optional[int] = None
    class Config:
        orm_mode = True



# Additional properties to return via API
class User(UserInDBBase):
    user_photo: UserPhotoBase = None
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
