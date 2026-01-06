from fastapi import APIRouter, HTTPException
from playground.schemas import ItemCreate
from playground.crud import create_item, get_items, delete_item, update_item
# from schemas import Item, ItemCreate 
# from items import get_items, create_item


router = APIRouter(
    # prefix="items",
    # tags=["items"]
)

@router.get("/")
def list_items():
    return get_items()

@router.post("/")
def add_item(item: ItemCreate):
    return create_item(item)

@router.delete("/{item_id}")
def remove_item(item_id: int):
    return delete_item(item_id)

@router.put("/{item_id}")
def edit_item(item_id: int, item: ItemCreate):
    return update_item(item_id, item)

    
# In-memory items for demo
# items_db = [
#     {"id": 1, "name": "Item 1", "price": 10},
#     {"id": 2, "name": "Item 2", "price": 20},
# ]

# # DELETE endpoint
# @router.delete("/{item_id}")  # <- This must match exactly
# def delete_item(item_id: int):
#     for i, item in enumerate(items_db):
#         if item["id"] == item_id:
#             items_db.pop(i)
#             return {"message": "Item deleted"}
#     raise HTTPException(status_code=404, detail="Item not found")

