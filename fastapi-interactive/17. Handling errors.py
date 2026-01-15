from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Sample data (following official docs naming)
items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    # TODO: Check if item_id exists in items
    # If not found, raise HTTPException with status_code=404, detail="Item not found"
    # If found, return {"item": items[item_id]}
    pass


@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    # TODO: Check if item_id exists in items
    # If not found, raise HTTPException with:
    #   - status_code=404
    #   - detail="Item not found" 
    #   - headers={"X-Error": "There goes my error"}
    # If found, return {"item": items[item_id]}
    pass


# TODO: Create a custom exception class called UnicornException
# It should accept a name parameter in __init__
class UnicornException(Exception):
    pass


# TODO: Add a custom exception handler for UnicornException
# Use @app.exception_handler(UnicornException)
# Return JSONResponse with status_code=418 and message about the unicorn
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    pass


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    # TODO: If name == "yolo", raise UnicornException(name=name)
    # Otherwise return {"unicorn_name": name}
    pass