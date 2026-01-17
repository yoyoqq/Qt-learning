"""
Docstring for 24. Dependencies - Path Operation Decorators

Security checks without needing user data in function
Header validation for API keys or custom headers
Request logging or monitoring
Rate limiting or quota checks


Use decorator dependencies when you don't need the return value
Combine with function parameters when you need some dependency values
Reuse existing dependencies - the same dependency function can be used in both places
Handle exceptions - dependencies can still raise HTTPExceptions
Editor-friendly - avoids unused parameter warnings

"""


from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException

app = FastAPI()


# TODO: Create verify_token dependency that checks X-Token header
# Should raise HTTPException(status_code=400) if token != "fake-super-secret-token"
async def verify_token(x_token: Annotated[str, Header()]):
    # TODO: Check if x_token equals "fake-super-secret-token", raise HTTPException if not
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")



# TODO: Create verify_key dependency that checks X-Key header  
# Should raise HTTPException(status_code=400) if key != "fake-super-secret-key"
# Should return the key value
async def verify_key(x_key: Annotated[str, Header()]):
    # TODO: Check if x_key equals "fake-super-secret-key", raise HTTPException if not
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400)
    # TODO: Return x_key
    return x_key

# TODO: Create GET /items/ endpoint with both verify_token and verify_key in dependencies parameter
# Use: dependencies=[Depends(verify_token), Depends(verify_key)]
# Return: [{"item": "Foo"}, {"item": "Bar"}]
@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    # TODO: Return list of items
    return [{"item": "Foo"}, {"item": "Bar"}] 