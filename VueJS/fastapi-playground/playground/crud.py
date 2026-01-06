from playground.database import users_db, items_db, current_id
from playground.schemas import UserCreate, ItemCreate, User, Item
from fastapi import HTTPException

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
    global current_id
    new_item = Item(id=current_id, name=item.name, price=item.price)
    items_db.append(new_item.model_dump())
    current_id += 1
    return new_item

def get_items():
    return items_db

def delete_item(item_id: int):
    for i, item in enumerate(items_db):
        if item['id'] == item_id:
            items_db.pop(i)
            return {"message": "Item deleted"}
    
    raise HTTPException(status_code=404, detail="Item not found")

def update_item(item_id: int, updated_item: ItemCreate) -> dict:
    for i, db_item in enumerate(items_db):
        if db_item['id'] == item_id:
            db_item['name'] = updated_item.name
            db_item['price'] = updated_item.price
            return db_item
    
    raise HTTPException(status_code=404, detail="Item not found")
    