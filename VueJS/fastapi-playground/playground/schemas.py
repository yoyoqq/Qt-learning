from pydantic import BaseModel

# Users 
class UserBase(BaseModel):
    name: str
    email: str 
    
class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

# Items     
class ItemBase(BaseModel):
    name: str
    price: float
    
class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int 

class LoginRequest(BaseModel):
    email: str
    password: str

