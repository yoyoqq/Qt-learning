"""
Docstring for 32. CORS Middleware

Specify explicit origins instead of wildcards for production
Enable only necessary HTTP methods and headers
Use allow_credentials=True carefully with explicit origins
Consider security implications of CORS policies


CORSMiddleware Parameters
The following arguments are supported:

allow_origins: A list of origins that should be permitted to make cross-origin requests. E.g. ['https://example.org', 'https://www.example.org']. You can use ['*'] to allow any origin.
allow_origin_regex: A regex string to match against origins that should be permitted to make cross-origin requests.
allow_methods: A list of HTTP methods that should be allowed for cross-origin requests. Defaults to ['GET']. You can use ['*'] to allow all standard methods.
allow_headers: A list of HTTP request headers that should be supported for cross-origin requests. Defaults to []. You can use ['*'] to allow all headers.
allow_credentials: Indicate that cookies should be supported for cross-origin requests. Defaults to False. None of allow_origins, allow_methods and allow_headers can be set to ['*'] if allow_credentials is set to True.
expose_headers: Indicate any response headers that should be made accessible to the browser. Defaults to [].
max_age: Sets a maximum time in seconds for browsers to cache CORS responses. Defaults to 600.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# TODO: Create origins list following the official FastAPI pattern
origins = ["http://localhost.tiangolo.com", "https://localhost.tiangolo.com", "http://localhost", "http://localhost:8080"]

# TODO: Configure CORS middleware with appropriate settings
# Use app.add_middleware() with CORSMiddleware
# Set allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Item(BaseModel):
    name: str
    description: str = None

items = []

# TODO: Create root endpoint that returns {"message": "Hello World"}
# Use function name: main() (following official docs)
@app.get("/")
async def main():
    return {"message": "Hello World"}

# TODO: Create GET /items/ endpoint to return all items
@app.get("/items/")
async def get_items():
    return items

# TODO: Create POST /items/ endpoint to add new items
@app.post("/items/")
def create_items(item: Item):
    items.append(item)
    return item