"""

use async for db, msg queues, apis and background tasks 
when doing network i/o

do not use when using CPU intensive jobs 
when need to request and wiat for a func such as s3 load

USE ON -> network calls, websockets 
"""
# Body - Multiple Parameters - Complete Tutorial
# Following the official FastAPI tutorial - all 5 concepts

from typing import Union
from fastapi import FastAPI, Path, Body, Query
from typing import Any
from pydantic import BaseModel

app = FastAPI()

# Pydantic models for request bodies
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None

# TODO 1: Mix Path, Query and body parameters
# Create endpoint PUT /items/{item_id}/basic
# Parameters: item_id (Path with validation), q (optional query), item (optional body)
# Use Path(title="The ID of the item to get", ge=0, le=1000) for item_id
# Return results dict with item_id, and conditionally add q and item if provided
@app.put("/items/{item_id}/basic")
def update_item(*,      # ! parameters are passed by name, not position
                item_id: int = Path(title="THe ID of the item to get", ge=0, le=1000), 
                q: str | None = None, 
                item: Union[str, None] = None):
    results: dict[str, Any] = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results
    

# TODO 2: Multiple body parameters (main concept)
# Create endpoint PUT /items/{item_id}
# Parameters: item_id (int), item (Item), user (User)
# Return: {"item_id": item_id, "item": item, "user": user}
@app.put("/items/{item_id}")
def get_item_id(item_id: int, item: Item, user: User):
    return {"item_id": item_id, "item": item, "user": user}

# TODO 3: Singular values in body
# ! COMING FROM THE JSON BODY() 
# Create endpoint PUT /items/{item_id}/importance
# Parameters: item_id, item (Item), user (User), importance (int = Body())
# Return: dict with all parameters
@app.put("/items/{item_id}/importance")
def put_importance(item_id: int, item: Item, user: User, importance: int = Body()):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results 

# TODO 4: Multiple body params and query
# Create endpoint PUT /items/{item_id}/full
# Parameters: item_id, item, user, importance (Body(gt=0)), q (optional query)
# Use * to force keyword-only arguments
# Return: dict with all params, conditionally add q
@app.put("/items/{item_id}/full")
def multiple_body(*, item_id: int, item: Item, user: User, importance: int = Body(gt=0), q: Union[str, None] = Query(None)):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results

# TODO 5: Embed single body parameter
# ! embed helps on -> the object being inside 
""" WIHT Embed(True) = {
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}"""
"""
OTHERWISE: WIHTOUT IT EXPETECT
{
    "name": "Foo",
    "description": "The pretender", 
    "price": 42.0,
    "tax": 3.2
}
"""
# Create endpoint PUT /items/{item_id}/embed
# Parameters: item_id, item (Item = Body(embed=True))
# Return: {"item_id": item_id, "item": item}
@app.put("/items/{item_id}/embed")
def embed(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results