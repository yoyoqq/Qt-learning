from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import auth_router, users, tweets, websocket

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Twitter Clone API",
    description="A comprehensive Twitter-like API with CRUD operations, authentication, WebSockets, and more",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router.router)
app.include_router(users.router)
app.include_router(tweets.router)
app.include_router(websocket.router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Twitter Clone API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "auth": "/auth",
            "users": "/users",
            "tweets": "/tweets",
            "websocket": "/ws"
        }
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is running"}
