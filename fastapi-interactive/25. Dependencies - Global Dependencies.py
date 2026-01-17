from fastapi import Depends, FastAPI, Header, HTTPException
from typing_extensions import Annotated


# TODO: Create verify_token dependency that checks X-Token header
# Should raise HTTPException(status_code=400) if token != "fake-super-secret-token"
async def verify_token(x_token: Annotated[str, Header()]):
    # TODO: Check if x_token equals "fake-super-secret-token", raise HTTPException if not
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400)

# TODO: Create verify_key dependency that checks X-Key header
# Should raise HTTPException(status_code=400) if key != "fake-super-secret-key"  
# Should return the key value
async def verify_key(x_key: Annotated[str, Header()]):
    # TODO: Check if x_key equals "fake-super-secret-key", raise HTTPException if not
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400)
    # TODO: Return x_key
    return x_key
    


# TODO: Create FastAPI app with global dependencies
# Use: app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])
app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


# TODO: Create GET /items/ endpoint (no dependencies needed - they're global)
# Return: [{"item": "Portal Gun"}, {"item": "Plumbus"}]
@app.get("/items/")
async def read_items():
    # TODO: Return list of items
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


# TODO: Create GET /users/ endpoint (no dependencies needed - they're global)
# Return: [{"username": "Rick"}, {"username": "Morty"}]
@app.get("/users/")
async def read_users():
    # TODO: Return list of user
    return [{"username": "Rick"}, {"username": "Morty"}]