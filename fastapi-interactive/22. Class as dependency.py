"""
Docstring for 22. Class as dependency

Callable Dependencies: Functions, classes, or any callable object can be dependencies
Class Dependencies: Provide better type support than dict-based dependencies
Parameter Analysis: FastAPI analyzes __init__ parameters for class dependencies
Type Annotations: Help editors provide better code completion and type checking
Dependency Shortcut: Depends() without parameters when the type annotation matches the class


Instead of writing:
    commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
...you can write:
    commons: Annotated[CommonQueryParams, Depends()]
"""


from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# TODO: Create a CommonQueryParams class with __init__ method
# that takes: q (str | None = None), skip (int = 0), limit (int = 100)
# Store these as self.q, self.skip, self.limit
class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        # TODO: Store the parameters as instance attributes
        self.q = q
        self.skip = skip 
        self.limit = limit


# TODO: Create GET /items/ endpoint using CommonQueryParams as dependency
# Use shortcut syntax: commons: Annotated[CommonQueryParams, Depends()]
# Return response dict with q (if provided) and sliced fake_items_db

@app.get("/items/")
async def read_items(
    commons: Annotated[CommonQueryParams, Depends()]
):
    items = fake_items_db[
        commons.skip : commons.skip + commons.limit
    ]

    response = {"items": items}

    if commons.q is not None:
        response["q"] = commons.q

    return response

# TODO: Create GET /users/ endpoint using explicit dependency syntax
# Use: commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
# Return same structure but with "items" key

@app.get("/users/")
async def read_users(
    commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
):
    users = fake_items_db[
        commons.skip : commons.skip + commons.limit
    ]

    response = {"items": users}

    if commons.q is not None:
        response["q"] = commons.q

    return response