"""

use descriptive model names (class names)
add field description -> Field(..., description="XXXXXXXX")

import basemodel to all fastapi 
do not use optional anymore use e.g.     str | None = None 
use Model Parameter -> create new class for it 
use post for creating 


Automatic Validation
    Reads the request body as JSON
    Validates the data against your Pydantic model
    Converts to the appropriate types
    Creates an instance of your model
    Passes it to your function
    Error Handling

"""
# Request Body - Following the Official FastAPI Tutorial
# Learn how to handle POST requests with data in the request body

from fastapi import FastAPI
from pydantic import BaseModel, Field
# TODO: Import BaseModel from pydantic

app = FastAPI()

# Step 1: Create a Pydantic model (from official tutorial)
# TODO: Create a class called 'Item' that inherits from BaseModel
# TODO: Add these fields:
#   - name: str
#   - description: str | None = None
#   - price: float
#   - tax: float | None = None
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# Step 2: Use the model in a POST endpoint
# TODO: Create a POST endpoint at "/items/"
# TODO: Add parameter: item: Item
# TODO: Return the item (FastAPI will serialize it automatically)
@app.post("/items/")
def create_item(item: Item):
    return item

# Step 3: Use the model with additional data
# TODO: Create a POST endpoint at "/items/{item_id}"
# TODO: Add path parameter: item_id: int
# TODO: Add body parameter: item: Item
# TODO: Return: {"item_id": item_id, **item.dict()}
@app.post("/items/{item_id}")
def post_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


# Pydantic features 
# 1. field validation 
class Itemm(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(None, max_length=500)
    price: float = Field(..., gt=0)  # Greater than 0
    tax: float | None = Field(None, ge=0)  # Greater than or equal to 0
    
# 2. nested models 
class Image(BaseModel):
    url: str
    name: str

class Itemmm(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []
    images: list[Image] | None = None
    

# 3. Model configuration 
class Itemmmmm(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    
    # ONLY USED IN DOCS
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }
        