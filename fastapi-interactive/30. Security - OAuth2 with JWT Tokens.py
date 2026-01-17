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
pwd_context = None

# TODO: Create OAuth2 scheme
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
oauth2_scheme = None

# TODO: Create Pydantic models following the official pattern
class Token(BaseModel):
    # TODO: Add access_token and token_type fields
    pass

class TokenData(BaseModel):
    # TODO: Add username field (Union[str, None] = None)
    pass

class User(BaseModel):
    # TODO: Add username, email, full_name, disabled fields
    pass

class UserInDB(User):
    # TODO: Add hashed_password field
    pass

# TODO: Create password functions
def verify_password(plain_password, hashed_password):
    # TODO: Use pwd_context.verify(plain_password, hashed_password)
    pass

def get_password_hash(password):
    # TODO: Use pwd_context.hash(password)
    pass

# TODO: Create user helper functions
def get_user(db, username: str):
    # TODO: Get user from database and return UserInDB instance
    pass

def authenticate_user(fake_db, username: str, password: str):
    # TODO: Get user and verify password, return user or False
    pass

# TODO: Create JWT token functions
def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    # TODO: Create JWT token with expiration using jwt.encode()
    pass

# TODO: Create get_current_user dependency
async def get_current_user():
    # TODO: Decode JWT token, extract username, get user from database
    # Handle InvalidTokenError and raise credentials_exception
    pass

# TODO: Create get_current_active_user dependency
async def get_current_active_user():
    # TODO: Check if user is not disabled
    pass

# TODO: Create /token endpoint
@app.post("/token")
async def login_for_access_token():
    # TODO: Authenticate user and return JWT token with expiration
    pass

# TODO: Create /users/me/ endpoint
@app.get("/users/me/")
async def read_users_me():
    # TODO: Return current user using JWT authentication
    pass

# TODO: Create /users/me/items/ endpoint
@app.get("/users/me/items/")
async def read_own_items():
    # TODO: Return user's items using JWT authentication
    pass
