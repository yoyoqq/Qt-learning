"""
Docstring for 29. Security - Simple OAuth2

The OAuth2PasswordRequestForm is a class dependency that declares a form body with:

The username
The password
An optional scope field as a big string, composed of strings separated by spaces
An optional grant_type
🔧 Key Concepts
Form Data Authentication: OAuth2 password flow requires form data, not JSON
Token Endpoint: Returns access tokens in standardized format
Password Verification: Check hashed passwords (never store plaintext)
User Status: Verify user is active before granting access
Bearer Tokens: Use "Bearer" token type for authorization headers

Always hash passwords, never store plaintext
Return consistent error messages for security
Include WWW-Authenticate header for 401 responses
Validate user is active before granting access
Use proper OAuth2 response format
"""

from typing import Union
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing_extensions import Annotated

# Fake users database (provided)
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

# Fake password hashing function (provided)
def fake_hash_password(password: str):
    return "fakehashed" + password

# TODO: Create OAuth2PasswordBearer scheme
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# TODO: Create User models following the official pattern
class User(BaseModel):
    # TODO: Add username, email, full_name, disabled fields
    username: str 
    email: str
    full_name: str
    disabled: bool

class UserInDB(User):
    # TODO: Add hashed_password field
    hashed_password: str

# TODO: Create helper functions (provided pattern)
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all - just for demo
    user = get_user(fake_users_db, token)
    return user

# TODO: Create get_current_user dependency
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    # TODO: Add token parameter and implement user lookup
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user

# TODO: Create get_current_active_user dependency  
async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    # TODO: Add current_user parameter and check if user is active
    if current_user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return current_user

# TODO: Create /token endpoint for login
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    # TODO: Add form_data parameter and implement authentication
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400)
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect password")
    return {"access_token": user.username, "token_type": "bearer"}

# TODO: Create /users/me endpoint
@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    # TODO: Add current_user parameter and return user
    return current_user