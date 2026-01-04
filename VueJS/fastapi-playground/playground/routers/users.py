from fastapi import APIRouter
from playground.schemas import UserCreate
from playground.crud import create_user, get_users

router = APIRouter()    # group path ops 

@router.get("/")
def list_users():
    return get_users()

@router.post("/")
def add_user(user: UserCreate):
    return create_user(user)