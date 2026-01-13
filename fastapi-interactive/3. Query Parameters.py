"""
PATH & QUERY parameters 
query -> optional parameters, it comes after the ? symbol
        set to None if not using 

use meaningful default values, when it is optinal put vals when its a feature 
use type hints 
handle optional parameters properly, use if cases if needed when None     
syntax: str | None = None

"""

# Query Parameters - Following the Official FastAPI Tutorial
# Learn how to handle optional parameters in URLs

from fastapi import FastAPI

app = FastAPI()

# Step 1: Create an endpoint with query parameters
# TODO: Create a GET endpoint at "/items/"
# TODO: Add function parameters: skip: int = 0, limit: int = 10
# TODO: Return: {"skip": skip, "limit": limit}
# Hint: Function parameters become query parameters automatically!
@app.get("/items/")
def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

# Step 2: Combine path and query parameters (from official tutorial)
# TODO: Create a GET endpoint at "/items/{item_id}"
# TODO: Add path parameter: item_id
# TODO: Add query parameter: q: str | None = None
# TODO: Return: {"item_id": item_id, "q": q}
# Hint: Mix path parameters {item_id} with query parameters 
@app.get("/items/{item_id}")
def get_items(item_id, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/items/{item_id}")
def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

@app.get("/users/")
def read_users(skip: int = 0, limit: int = 10, active: bool = True):
    # In a real app, you'd filter from a database
    return {
        "skip": skip,
        "limit": limit, 
        "active_only": active,
        "message": f"Showing {limit} users, skipping {skip}, active: {active}"
    }

@app.get("/search/")
def search_items(q: str):  # Required - no default value
    return {"query": q, "results": []}

@app.get("/products/")
def get_products( category: str = "all", min_price: float = 0.0, max_price: float = 1000.0, in_stock: bool = True ):
    return {
        "category": category,
        "price_range": [min_price, max_price],
        "in_stock_only": in_stock
    }