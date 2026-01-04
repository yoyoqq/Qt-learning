from playground.database import users_db, items_db
from playground.schemas import UserCreate, ItemCreate, User, Item

# users 
def create_user(user: UserCreate) -> User:
    new_id = len(users_db) + 1
    user_obj = User(id=new_id, **user.model_dump())
    users_db.append(user_obj.model_dump())
    return user_obj

def get_users():
    return users_db

# Items
def create_item(item: ItemCreate) -> Item:
    new_id = len(items_db) + 1
    item_obj = Item(id=new_id, **item.dict())
    items_db.append(item_obj.dict())
    return item_obj

def get_items():
    return items_db