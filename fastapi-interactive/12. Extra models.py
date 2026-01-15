"""
Docstring for 12. Extra models

Create separate models for input, output, and database operations to maintain security and clarity
Use model inheritance to reduce code duplication while keeping models focused
Always filter sensitive data like passwords from output models using response_model
Use Union types when endpoints can legitimately return different model types
Include the most specific type first in Union declarations for better type checking




# ! can unpack pydantic model from the contents using model_dump()
def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
    return user_in_db

@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved
    
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password: str

from typing import Union

@app.get("/items/{item_id}")
async def read_item(item_id: str) -> Union[PlaneItem, CarItem]:
    # Return either a PlaneItem or CarItem based on logic
    pass
"""


# Extra Models
# Learn to create multiple related models for different use cases

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Union

app = FastAPI()

# TODO: Create three user models:
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None 
# 1. UserIn - for input data (includes password)
class UserIn(UserBase):
    password: str
# 2. UserOut - for output data (excludes password)  
class UserOut(UserBase):
    pass
# 3. UserInDB - for database storage (includes hashed_password)
class UserInDB(UserOut):
    hashed_password: str

# TODO: Create a fake password hasher function
# async def fake_password_hasher(raw_password: str):
#     return "supersecret" + raw_password
def fake_password_hasher(raw_password: str):
    return raw_password + "0" * 10

# TODO: Create a fake save user function that:
# - Takes a UserIn object
# - Hashes the password (remember to await the hasher!)
# - Creates a UserInDB object with the hashed password
# - Returns the UserInDB object
# async def fake_save_user(user_in: UserIn):
#     hashed_password = await fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
#     print("User saved! ..not really")
#     return user_in_db
# async def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.model_dump(), hashed_password=hashed_password)
#     return user_in_db

# TODO: Create a POST endpoint at "/user/" that:
# - Accepts UserIn data
# - Uses response_model=UserOut to filter the response
# - Calls fake_save_user and returns the result (remember to await it!)
# @app.post("/user/", response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = await fake_save_user(user_in)
#     return user_saved
def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(
        **user_in.model_dump(),
        # **user_in.model_dump(exclude={"password"}),
        hashed_password=hashed_password
    ) 
    return user_in_db

@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved