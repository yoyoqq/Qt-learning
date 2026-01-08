
from fastapi import APIRouter, Response, HTTPException, Depends
from playground.schemas import LoginRequest
from playground.security.security import create_access_token, get_current_user

router = APIRouter()

# AUTH with JWT 
@router.post("/login")
def login(data: LoginRequest, response: Response):
    if data.email != "1234" or data.password != "1234":
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

    return {"message": "logged in"}

@router.get("/me")
def read_me(user_email: str = Depends(get_current_user)):
    return {"email": user_email}