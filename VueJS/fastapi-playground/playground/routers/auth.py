
from fastapi import APIRouter, Response, HTTPException, Depends
from playground.schemas import LoginRequest, UserCreate
from playground.security.security import create_access_token, get_current_user
from playground.database import users_db
from playground.crud import create_user

router = APIRouter()

@router.post("/signup")
def signup(user: UserCreate, response: Response):
    # Check if user already exists
    if any(u['email'] == user.email for u in users_db):
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = create_user(user)
    
    token = create_access_token({"sub": new_user.email})
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,  # Set to True in production with HTTPS
        samesite="lax",
        max_age=60 * 60
    )
    return {"message": "Signup successful"}

@router.post("/login")
def login(data: LoginRequest, response: Response):
    user = next((u for u in users_db if u['email'] == data.email and u['password'] == data.password), None)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": data.email})
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=60 * 60
    )
    return {"message": "Logged in"}

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    return {"message": "Logged out"}

@router.get("/me")
def read_me(user_email: str = Depends(get_current_user)):
    return {"email": user_email}