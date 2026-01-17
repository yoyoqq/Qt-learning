"""
Docstring for 17. Handling errors


Use appropriate HTTP status codes (404 for not found, 400 for bad data)
Provide clear, helpful error messages in the detail field
Don't expose internal system information in error messages
Use custom exception handlers for application-specific errors
Consider security implications when returning error details

"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# Sample data (following official docs naming)
items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    # TODO: Check if item_id exists in items
    # If not found, raise HTTPException with status_code=404, detail="Item not found"
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    # If found, return {"item": items[item_id]}
    return {"item": items[item_id]}


@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    # TODO: Check if item_id exists in items
    # If not found, raise HTTPException with:
    #   - status_code=404
    #   - detail="Item not found" 
    #   - headers={"X-Error": "There goes my error"}
    # If found, return {"item": items[item_id]}
    if item_id not in items:
        raise HTTPException(
            status_code=404, detail="Item not found", headers={"X-Error": "There goes my error"}
        )
    # If found, return {"item": items[item_id]}
    return {"item": items[item_id]} 


# TODO: Create a custom exception class called UnicornException
# It should accept a name parameter in __init__
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


# TODO: Add a custom exception handler for UnicornException
# Use @app.exception_handler(UnicornException)
# Return JSONResponse with status_code=418 and message about the unicorn
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content= {"message": exc.name}
    )


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    # TODO: If name == "yolo", raise UnicornException(name=name)
    # Otherwise return {"unicorn_name": name}
    if name == "yolo":
        raise UnicornException(name=name) 
    return {"unicorn_name": name}