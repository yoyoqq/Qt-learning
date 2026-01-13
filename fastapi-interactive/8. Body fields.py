"""
Field works the same way as Query, Path, and Body - it accepts the same validation parameters:
    Validation constraints: gt, ge, lt, le, min_length, max_length, etc.
    Metadata: title, description, example, etc.
    Default values: default, default_factory



"""

# Body - Fields
# Learn to add validation and metadata to Pydantic model fields

from typing import Union
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# TODO: Create the Item model with Field validation
# Use Field() to add validation and metadata to model attributes:
# - name: str (no Field needed for simple required fields)
# - description: Union[str, None] with Field(default=None, title="The description of the item", max_length=300)
# - price: float with Field(gt=0, description="The price must be greater than zero")
# - tax: Union[float, None] = None (no Field needed)

class Item(BaseModel):
    # TODO: Add the fields with proper Field() validation
    name: str
    description: Union[str, None] = Field(default=None, title="Description of the item", max_length=300)
    price: float = Field(gt=0, description="Price must be greater than zero")
    tax: Union[float, None] = None # optional field 

# TODO: Create the update_item endpoint
# - PUT /items/{item_id}
# - Parameters: item_id (int), item (Item = Body(embed=True))
# - Return: {"item_id": item_id, "item": item}
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    return {"item_id": item_id, "item": item}



"""
class Item(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0, le=1000000)  # Positive, reasonable max
    quantity: int = Field(ge=1, le=1000)    # At least 1, reasonable max
    email: str = Field(regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    
    
class User(BaseModel):
    username: str = Field(
        title="Username",
        description="Unique identifier for the user",
        min_length=3,
        max_length=50,
        example="johndoe"
    )
    age: int = Field(
        title="Age", 
        description="Age in years",
        ge=0,
        le=150,
        example=25
    )
    

class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None,
        title="Item Description", 
        max_length=500
    )
    is_active: bool = Field(default=True, description="Whether item is active")
    
    
"""