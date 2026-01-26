
"""

app/
├── __init__.py          # Makes 'app' a Python package
├── main.py             # Main application entry point
├── dependencies.py     # Shared dependencies
├── routers/            # Route modules
│   ├── __init__.py     # Makes 'routers' a subpackage
│   ├── users.py        # User-related routes
│   └── items.py        # Item-related routes
└── internal/           # Internal modules
    ├── __init__.py     # Makes 'internal' a subpackage
    └── admin.py        # Admin-only routes
    
APIRouter is like a "mini FastAPI" that you can use to organize related routes:

🔧 Key Concepts
APIRouter: Organizes related routes into modules
Package Structure: Use __init__.py files to create Python packages
Relative Imports: Navigate between modules using . and .. syntax
Router Inclusion: Use app.include_router() to add routers to your main app
Dependency Sharing: Apply dependencies at app, router, or route level
💡 Best Practices
Group Related Routes: Put related functionality in the same router
Use Prefixes: Apply common URL prefixes at the router level
Share Dependencies: Define common dependencies once and reuse them
Organize by Feature: Structure your code by business logic, not technical layers
Keep Main App Simple: The main app should primarily orchestrate routers

"""

from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/users/")
async def get_users():
    return [{"username": "user1"}, {"username": "user2"}]

router = APIRouter(
    prefix="/items",           # All routes get this prefix
    tags=["items"],           # OpenAPI tags for documentation
    dependencies=[Depends(auth)], # Applied to all routes
    responses={404: {"description": "Not found"}},
)


from fastapi import FastAPI
from .routers import users, items

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)


# 4. Relative Imports
# Use relative imports to access modules within your package:
# From app/routers/items.py
from ..dependencies import get_token_header  # Go up one level
from . import users  # Same level

# 5. Dependencies Across Modules
# Dependencies can be shared across the entire application or specific routers:
# Global dependencies (applied to all routes)
app = FastAPI(dependencies=[Depends(global_dep)])

# Router-specific dependencies
router = APIRouter(dependencies=[Depends(router_dep)])

# Route-specific dependencies
@router.get("/", dependencies=[Depends(route_dep)])
async def get_items():
    pass


# =================================
# PROBLEM SOLUTION CODE 
# =================================

# TODO: Import the necessary modules
# Hint: You need FastAPI, Depends, and the modules we created
from fastapi import FastAPI

# TODO: Import dependencies from our dependencies module
# from .dependencies import get_query_token, get_token_header
from .dependencies import get_query_token, get_token_header

# TODO: Import routers from our routers package
# from .routers import items, users
from .routers import items, users

# TODO: Import admin router from internal package
# from .internal import admin
from .internal import admin

# TODO: Create FastAPI app with global dependencies
# Hint: Use dependencies=[Depends(get_query_token)] to apply to all routes
app = FastAPI(dependencies=[Depends(get_query_token)])

# TODO: Include the users router
# Hint: Use app.include_router(users.router)
app.include_router(users.router)

# TODO: Include the items router
# Hint: Use app.include_router(items.router)
app.include_router(items.router)

# TODO: Include the admin router with configuration
# Hint: Use prefix="/admin", tags=["admin"], dependencies=[Depends(get_token_header)], 
# and responses={418: {"description": "I'm a teapot"}}
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418:{"description": "I'm a teapot"}}
)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
