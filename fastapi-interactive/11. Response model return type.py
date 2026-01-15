
"""
Docstring for 11. Response model return type


create separate in/out models to avoid exposing sensitive data 
use return type annotations with response_model for better editor support and type checking 

"""




# Response Model - Return Type
# Learn to declare response models using return type annotations and response_model parameter

from typing import Any
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

# TODO: Create a POST endpoint at "/items/" that accepts an Item and returns it
# Use return type annotation -> Item to declare the response model
@app.post("/items/", response_model=Item)
async def creat(item: Item):
    return item

# TODO: Create a GET endpoint at "/items/" that returns a list of items
# Use return type annotation -> list[Item] to declare the response model
# Return this sample data:
# [
#     {"name": "Portal Gun", "price": 42.0},
#     {"name": "Plumbus", "price": 32.0},
# ]
@app.get("/items/", response_model=list[Item])
async def get_list_items():
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]
