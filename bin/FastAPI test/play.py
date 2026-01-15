from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
    # return "HI"
    
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}

@app.get("/search")
def search(q: str, limit: int = 10):
    limit += 10
    return {"query": q, "limit": limit}


# GOOD STUFF
# ✔ JSON parsing
# ✔ Type checking
# ✔ Validation
# ✔ Docs generation
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/users")
def create_user(user: User):
    return user



# ASYNC
def some_async_call():
    return 

@app.get("/slow")
async def slow():
    await some_async_call()
    return {"done": True}
