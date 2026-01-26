from fastapi import FastAPI
from playground.routers import items, users, websocket, auth
from playground.security import security


app = FastAPI()


# allow use more endpoints with the same name with matching 
# be careful with the wildcards 
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# app.include_router(users.router, prefix="/users", tags=["Users"])       # path for query, tags for documentation
# app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(websocket.router, prefix="/websocket", tags=["websocket"])
# app.include_router(security.router)
# app.include_router(auth.router, prefix="/authenticateJWT", tags=["AUTH_JWT"])