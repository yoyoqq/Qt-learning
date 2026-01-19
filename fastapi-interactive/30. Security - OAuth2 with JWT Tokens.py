"""
Docstring for 30. Security - OAuth2 with JWT Tokens


💡 Best Practices
Security Considerations
Secret Key: Use a strong, randomly generated secret key
Token Expiration: Set reasonable expiration times (15-30 minutes)
HTTPS Only: Always use HTTPS in production
Password Strength: Enforce strong password requirements
Token Management
Refresh Tokens: Implement refresh tokens for better UX
Token Revocation: Consider token blacklisting for logout
Scope Limitations: Use scopes to limit token permissions
Error Handling
Consistent Responses: Return consistent error messages
No Information Leakage: Don't reveal whether username or password is wrong
Rate Limiting: Implement rate limiting on authentication endpoints
🧪 Testing Your Implementation
Step-by-Step Testing Workflow
Get a Token First

Run the /token endpoint with username johndoe and password secret
Copy the access_token from the response
Set the Token in Test Endpoints Tab

Go to the "Test Endpoints" tab
Click the 🔐 Auth button (top right)
Paste the token you copied from step 1
The button will turn green when token is active
Test Protected Endpoints

Click on /users/me/ or /users/me/items/
Click "Test" - the token will be automatically added!
Protected endpoints should return 200 with user data
Run All Tests

Click "Run Tests" button - it will also use your token!
The tests will automatically get a fresh token and use it for protected endpoints
Verify Authentication Works

Protected endpoints should return 200 with user data
Without a token, they should return 401 Unauthorized
🔄 Complete Authentication Flow
1. POST /token → Get JWT token
2. Copy token from response
3. Set token in Test Endpoints tab (🔐 Auth button)
4. GET /users/me/ → Automatically uses Bearer token
5. GET /users/me/items/ → Automatically uses Bearer token
6. Run Tests → Automatically gets fresh token and tests all endpoints
💡 Pro Tip: The token expires after 30 minutes, so you may need to get a new one if testing takes a while!
"""
from datetime import datetime, timedelta, timezone
from typing import Union

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel
from typing_extensions import Annotated
from pwlib import PasswordHash

# JWT configuration - following official FastAPI pattern
# to get a string like this run: openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Sample users database with bcrypt hashed passwords (provided)
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

app = FastAPI()

# TODO: Create password context using CryptContext
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 

# TODO: Create OAuth2 scheme
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

password_hash = PasswordHash.recommended

# TODO: Create Pydantic models following the official pattern
class Token(BaseModel):
    # TODO: Add access_token and token_type fields
    acess_token: str
    token_type: str

class TokenData(BaseModel):
    # TODO: Add username field (Union[str, None] = None)
    # username = Union[str, None] = None        # ! Union is for describing a type, not creating a value 
    username: str | None = None


class User(BaseModel):
    # TODO: Add username, email, full_name, disabled fields
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    # TODO: Add hashed_password field
    hashed_password: str 

# TODO: Create password functions
def verify_password(plain_password, hashed_password):
    # TODO: Use pwd_context.verify(plain_password, hashed_password)
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    # TODO: Use pwd_context.hash(password)
    return password_hash.hash(password)

# TODO: Create user helper functions
def get_user(db, username: str):
    # TODO: Get user from database and return UserInDB instance
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    # TODO: Get user and verify password, return user or False
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# TODO: Create JWT token functions
def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    # TODO: Create JWT token with expiration using jwt.encode()
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM=ALGORITHM)
    return encoded_jwt 

# TODO: Create get_current_user dependency
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    # TODO: Decode JWT token, extract username, get user from database
    # Handle InvalidTokenError and raise credentials_exception
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user 

# TODO: Create get_current_active_user dependency
async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)],):
    # TODO: Check if user is not disabled
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# TODO: Create /token endpoint
@app.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],):
    # TODO: Authenticate user and return JWT token with expiration
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

# TODO: Create /users/me/ endpoint
@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user

# TODO: Create /users/me/items/ endpoint
@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]
