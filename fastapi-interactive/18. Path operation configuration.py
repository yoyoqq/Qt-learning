"""
Docstring for 18. Path operation configuration

Always use status constants for better code readability
Group related endpoints with consistent tags
Use docstrings for complex endpoint descriptions
Mark deprecated endpoints instead of immediately removing them
Keep response descriptions specific and helpful


"""

from enum import Enum
from typing import Set, Union

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


class Tags(Enum):
    items = "items"
    users = "users"


# TODO: Create a POST endpoint for items with status.HTTP_201_CREATED status code
# @app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_itmem(item: Item):
    return item

# TODO: Create a GET endpoint for items with "items" tag
# @app.get("/items/", tags=["items"])
@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]

# TODO: Create a GET endpoint for users with "users" tag
# Use @app.get("/users/", tags=["users"])
@app.get("/users/", tags=["Users"])
async def get_users():
    return [{"username": "johndoe"}]


# TODO: Create a GET endpoint for elements with Tags.items enum tag
# Use @app.get("/elements/", tags=[Tags.items])
@app.get("/elements/", tags=[Tags.items])
async def get_elements():
    pass


# TODO: Create a POST endpoint with summary and description
# Use @app.post("/items-summary/", response_model=Item, summary="Create an item", description="...")
@app.post("/items-summary/", response_model=Item, summary="Create an item")
async def create_itemm(item: Item):
    return item


# TODO: Create a POST endpoint with docstring description
# Add a detailed docstring with markdown
# @app.post("/items-docstring/", response_model=Item, summary="Create an item")
@app.post("/items-docstring/", response_model=Item, summary="Create an item")
async def create_item(item: Item):
    """
    Docstring for create_item
    
    :param item: Description
    :type item: Item
    """
    return item 


# TODO: Create a deprecated GET endpoint for elements
# Use @app.get("/elements/", tags=["items"], deprecated=True)
@app.get("/elements/", tags=["items"], deprecated=True)
async def get_item():
    pass