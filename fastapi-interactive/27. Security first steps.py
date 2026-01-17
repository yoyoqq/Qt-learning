"""
Docstring for 27. Security first steps

Let's imagine that you have your backend API in some domain and you have a frontend in another domain or in a different path of the same domain (or in a mobile application). You want to have a way for the frontend to authenticate with the backend, using a username and password.
We can use OAuth2 to build that with FastAPI. Let's use the tools provided by FastAPI to handle security.


This parameter tokenUrl="token" refers to a relative URL token that the client (frontend running in the user's browser) will use to send the username and password in order to get a token.
    from fastapi.security import OAuth2PasswordBearer
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    
Bearer Token: A token passed in the Authorization: Bearer <token> header
OAuth2PasswordBearer: FastAPI class that handles Bearer token extraction
tokenUrl: URL where clients send credentials to get tokens (declared but not implemented yet)
Security Dependency: Use Depends(oauth2_scheme) to protect endpoints
Automatic Documentation: FastAPI generates interactive docs with "Authorize" button
💡 Best Practices
Use relative URLs for tokenUrl to work with proxies
Don't implement actual token validation yet - this is just the first step
The oauth2_scheme is both a class instance and a callable dependency
Protected endpoints automatically get security documentation
"""

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated

app = FastAPI()

# TODO: Create OAuth2PasswordBearer instance
# Follow the official FastAPI pattern:
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# TODO: Create a protected endpoint that uses OAuth2 security
# Follow this pattern from the official docs:
#
# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}
#
# This will automatically:
# - Require Authorization header with Bearer token
# - Show "Authorize" button in FastAPI docs
# - Return 401 if no token provided

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    # TODO: Add the token parameter with proper typing
    # Use: token: Annotated[str, Depends(oauth2_scheme)]
    return {"token": token}

