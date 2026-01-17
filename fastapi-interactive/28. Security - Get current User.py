"""
Docstring for 28. Security - Get current User

Create separate user models for different contexts (UserInDB vs User response)
Use meaningful function names like get_current_user
Leverage FastAPI's dependency injection for security concerns
Keep security logic separate from business logic
Use type annotations for better development experience


"""

from typing import Union
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing_extensions import Annotated

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# TODO: Create a User model using Pydantic
# Follow the official FastAPI pattern:
class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

# TODO: Create a fake_decode_token function
# Follow the official pattern:
# def fake_decode_token(token):
#     return User(
#         username=token + "fakedecoded", 
#         email="john@example.com", 
#         full_name="John Doe"
#     )
    
def fake_decode_token(token):
    # TODO: Return a User instance with decoded token data
    return User(
        username = token + "fakedecoded",
        email="john@example.com",
        full_name="John Doe"
    )

# TODO: Create get_current_user dependency
# Follow the official pattern:
# async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
#     user = fake_decode_token(token)
#     return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    # TODO: Add token parameter and implement user decoding
    user = fake_decode_token(token)
    return user

# TODO: Create /users/me endpoint
# Follow the official pattern:
# @app.get("/users/me")
# async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
#     return current_user
@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user