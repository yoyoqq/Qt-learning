from fastapi import APIRouter, HTTPException, Depends, Header, Cookie
from pydantic import BaseModel
from jose import jwt, JWTError # type: ignore
from datetime import datetime, timedelta

SECRET_KEY = "supersecret"
ALGORITHM = "HS256"

router = APIRouter(prefix="/auth", tags=["auth"])

class LoginRequest(BaseModel):
    email: str
    password: str

fake_users = {
    "test@example.com": {
        "email": "test@example.com",
        "hashed_password": "$2b$12$...",
    }
}

# with PINIA log in 
@router.post("/login")
def login(data: LoginRequest):
    print(f"Login attempt - Email: {data.email}, Password: {data.password}, Password type: {type(data.password)}")
    if data.email != "test@example.com" or data.password != "1234":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    payload = {
        "sub": data.email,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": token, "token_type": "bearer"}


# ? ONLY for cookie log in 
# def get_current_user(authorization: str = Header(...)):
#     if not authorization.startswith("Bearer "):
#         raise HTTPException(401)

#     token = authorization.split(" ")[1]
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload["sub"]
#     except:
#         raise HTTPException(401)
    
# ? LOG in with HTTPCookie 
def get_current_user(access_token: str = Cookie(None)):
    if not access_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401)
        else:
            return email
    except:
        raise HTTPException(status_code=401, detail="Invalid Token")
    
@router.get("/me")
def read_me(user=Depends(get_current_user)):
    return {"email": user}

ACCESS_TOKEN_EXPIRE_MINUTES = 60
def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

