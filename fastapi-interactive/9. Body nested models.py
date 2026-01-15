"""
Docstring for 9. Body nested models


provide automatic validastion at every level 
type conversion 
clear error messages 

organize from simple to complex 

"""
# Body - Nested Models
# Learn to create complex nested data structures with FastAPI and Pydantic

from typing import Dict, List, Set, Union
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# TODO 1: Create the Image nested model
# Fields: url (HttpUrl), name (str)
class Image(BaseModel):
    # TODO: Add the fields
    url: HttpUrl
    name: str 

# TODO 2: Create the Item model with nested structures
# Fields:
# - name: str
# - description: Union[str, None] = None
# - price: float
# - tax: Union[float, None] = None
# - tags: Set[str] = set()  # Set of unique strings
# - image: Union[Image, None] = None  # Single nested model
class Item(BaseModel):
    # TODO: Add the fields with proper types
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    image: Union[Image, None] = None

# TODO 3: Create ItemWithImages model for lists of nested models
# Same as Item but with:
# - images: List[Image] = []  # List of nested models instead of single image
class ItemWithImages(BaseModel):
    # TODO: Add the fields
    images: List[Image] = [] 

# TODO 4: Create endpoints
# 1. PUT /items/{item_id} - update_item(item_id: int, item: Item)
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}
# 2. PUT /items/{item_id}/images - update_item_with_images(item_id: int, item: ItemWithImages)
@app.put("/items/{item_id}/images")
async def update_item_with_images(item_id: int, item: ItemWithImages):
    return {"item_id": item_id, "item": item}
# 3. POST /index-weights/ - create_index_weights(weights: Dict[int, float])
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights




class Address(BaseModel):
    street: str
    city: str
    country: str

class User(BaseModel):
    name: str
    email: str
    address: Address  # Simple nesting

class Order(BaseModel):
    id: int
    user: User        # Nested user
    items: List[Item] # List of nested items
    total: float
    
    
from pydantic import Field

class Item(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    tags: Set[str] = Field(max_items=10)  # Limit set size
    images: List[Image] = Field(max_items=5)  # Limit list size

class Item(BaseModel):
    name: str
    # Optional nested model
    image: Union[Image, None] = None
    # Required nested model
    category: Category
    # Optional list (can be empty)
    tags: List[str] = []