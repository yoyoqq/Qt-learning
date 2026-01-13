"""
! PATH ALWAYS BEFORE QUERY OTHERWISE ERROR 
* can use * to allow any order ( * , Query, PATH...)

ge: Greater than or equal
gt: Greater than
le: Less than or equal
lt: Less than


Metadata and Documentation
    title: Parameter title in docs
    description: Parameter description
    deprecated: Mark parameter as deprecated
    include_in_schema: Include/exclude from OpenAPI schema
    example: Example value for documentation
    
    
use reasonable constraints 
add docs title/description 
use data types 

path before query  
import path 
constraints logical 
"""

# Path Parameters and Numeric Validations - Following Official FastAPI Tutorial
# Learn how to add validation constraints to path parameters

from fastapi import FastAPI, Path, Query
# TODO: Import Path and Query from fastapi

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Step 1: Add validation to path parameters
# TODO: Create a GET endpoint at "/items/{item_id}"
# TODO: Add parameter: item_id: int = Path(ge=1)
# TODO: Return: {"item_id": item_id}
# Hint: Path(ge=1) means the item_id must be greater than or equal to 1
@app.get("/items/{item_id}")
def get_items(item_id: int = Path(ge=1)):   # number >= 1 
    return {"item_id": item_id}

# Step 2: Combine Path and Query validations
# TODO: Create a GET endpoint at "/items/{item_id}/details"
# TODO: Add parameter: item_id: int = Path(ge=1, le=1000, description="The ID of the item")
# TODO: Add parameter: q: str | None = Query(default=None, max_length=50)
# TODO: Return: {"item_id": item_id, "q": q, "details": "Item details here"}
@app.get("/items/{item_id}/details")
def get_details(item_id: int = Path(ge=1, le=1000, description="The ID of the item"), q: str | None = Query(default=None, max_length=50)):
    return {"item_id": item_id, "q": q, "details": "Item details here"}

# Step 3: Add metadata to path parameters
# TODO: Create a GET endpoint at "/users/{user_id}"
# TODO: Add parameter: user_id: int = Path(title="User ID", description="The ID of the user to get", ge=1)
# TODO: Return: {"user_id": user_id, "message": f"User {user_id} profile"}
@app.get("/users/{user_id}")
def get_metadata(
    user_id: int = Path(title="User ID", description="The ID of the user to get", ge=1)
):
    return {"user_id": user_id, "message": f"User {user_id} profile"}


@app.get("/items/{item_id}")
def read_item( item_id: int = Path(title="Item ID", description="The ID of the item to get", ge=0, le=1000) ):
    return {"item_id": item_id}

# with full metadata 
@app.get("/products/{product_id}")
def get_product( product_id: int = Path( title="Product ID", description="The unique identifier for the product", example=42, ge=1, le=999999 ) ):
    return {"product_id": product_id}