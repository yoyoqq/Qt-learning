"""

The Query function allows you to add metadata and validation constraints to query parameters.
Query(
    default=...,      # required or default value
    *,                # everything after is keyword-only
    alias=...,
    min_length=...,
    max_length=...,
    regex=...,
    ge=..., gt=...,
    le=..., lt=...,

    description=...,
    title=...,
    example=...,
    deprecated=...
    
)

    default -> None (optional)
                ... (required)
                
    
    required: q: str | None
    optinal:  q: str | None = None 
              q: str | None = Query(None)



min_length: Minimum string length
max_length: Maximum string length
regex: Regular expression pattern
ge: Greater than or equal (numbers)
le: Less than or equal (numbers)
gt: Greater than (numbers)
lt: Less than (numbers)
Metadata and Documentation
description: Parameter description in docs
deprecated: Mark parameter as deprecated
include_in_schema: Include/exclude from OpenAPI schema
example: Example value for documentation


use meaningful contraints 
add helpful descriptions 
use appropieta defaults 
unrealistic constraints 
"""


# Query Parameters and String Validations - Following Official FastAPI Tutorial
# Learn how to add validation and constraints to query parameters

from fastapi import FastAPI, Query
# TODO: Import Query from fastapi

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# Step 1: Add validation to query parameters
# TODO: Create a GET endpoint at "/items/"
# TODO: Add parameter: q: str | None = Query(default=None, max_length=50)
# TODO: Return items filtered by q if provided, or all items if q is None
# Hint: Use Query() instead of just setting default values
@app.get("/items/")
def get_items(q: str | None = Query(default=None, max_length=50)):  # max 50 chars 
    results = []
    # if q is provided filter by name, else return all items
    if q:
        results = [item for item in fake_items_db if q.lower() in item["item_name"].lower()]
    else:
        results = fake_items_db
    return {"results": results}

# Step 2: Add more validation constraints  
# TODO: Create a GET endpoint at "/items/search/"
# TODO: Add parameter: q: str = Query(min_length=3, max_length=50, description="Search query")
# TODO: Add parameter: limit: int = Query(10, ge=1, le=100, description="Maximum number of items")
# TODO: Return: {"query": q, "limit": limit, "results": [...]}
# Hint: ge=1 means "greater than or equal to 1"
@app.get("/items/search/")
def search_items(
    q: str = Query(min_length=3, max_length=50, description="Search Query"), 
    limit: int = Query(10, ge=1, le=100, description="Maximum number of items")
    ):
    return {"query": q, "limit": limit, "results": q[:limit]}
    