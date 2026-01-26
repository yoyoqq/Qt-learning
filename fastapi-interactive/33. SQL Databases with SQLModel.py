"""
Docstring for 33. SQL Databases with SQLModel


Key Field Configurations:

primary_key=True: Marks the field as the table's primary key
index=True: Creates a database index for faster queries
default=None: Allows the database to auto-generate values (especially for IDs)


🔧 Key Concepts
Multiple Models Pattern: Use different models for different purposes (security, validation)
Table Models: Classes with table=True represent database tables (Hero)
Data Models: Classes without table=True are for API contracts (HeroPublic, HeroCreate)
Model Inheritance: Use base classes to share common fields (HeroBase)
Response Models: Use response_model to control what data is returned to clients
Partial Updates: Use exclude_unset=True to update only provided fields
Database Engine: Manages database connections and should be created once
Sessions: Handle individual transactions and should be injected per request
Dependency Injection: Use Depends() to inject database sessions into endpoints
Query Builder: Use select() for complex database queries
Pagination: Implement with offset and limit parameters

 Best Practices
Multiple Models for Security: Never expose sensitive data like secret_name in public APIs
Use Response Models: Always specify response_model to control API responses
Model Inheritance: Use base models to avoid duplicating field definitions
Partial Updates: Use exclude_unset=True for PATCH operations to update only provided fields
Primary Key Required: Every table model must have a primary key field
Session Per Request: Use dependency injection for database sessions to ensure thread safety
Proper Error Handling: Always check if records exist before operations
Database Startup: Create tables during application startup with @app.on_event("startup")
Connection Arguments: Use check_same_thread=False for SQLite with FastAPI
Query Limits: Always limit query results to prevent performance issues
Transaction Management: Use session.commit() to save changes and session.refresh() to get updated data

"""
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

# TODO: Create the Hero base model with shared fields (name, age)
# This model contains fields that are shared across other models
# Hint: Use Field(index=True) for name and age fields
class HeroBase(SQLModel):
    pass  # Add name and age fields here

# TODO: Create the Hero table model with id and secret_name fields
# Remember to use table=True and proper Field configurations
# This is the actual database table model that inherits from HeroBase
class Hero(HeroBase, table=True):
    pass  # Add id (primary key) and secret_name fields

# TODO: Create the HeroPublic model for API responses (no secret_name)
# This model is returned to clients - excludes secret_name for security
# Hint: Inherit from HeroBase and add id field as required (int, not optional)
class HeroPublic(HeroBase):
    pass  # Add id field

# TODO: Create the HeroCreate model for creating heroes
# This model validates data from clients when creating heroes
# Hint: Inherit from HeroBase and add secret_name field
class HeroCreate(HeroBase):
    pass  # Add secret_name field

# TODO: Create the HeroUpdate model with optional fields for updates
# All fields are optional for partial updates (use None defaults)
class HeroUpdate(SQLModel):
    pass  # Add optional name, age, and secret_name fields

# TODO: Set up the database engine with SQLite
# Use check_same_thread=False for FastAPI compatibility
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# TODO: Create connect_args dictionary and engine
# Hint: connect_args = {"check_same_thread": False}
connect_args = None  # Replace with proper config
engine = None  # Replace with create_engine call

# TODO: Create a function to create database tables
# Hint: Use SQLModel.metadata.create_all(engine)
def create_db_and_tables():
    pass

# TODO: Create a session dependency using yield
# This ensures one session per request for thread safety
# Hint: Use 'with Session(engine) as session:' and yield the session
def get_session():
    pass

# Create the dependency annotation
SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

# TODO: Add startup event to create tables
# Hint: Call create_db_and_tables() function
@app.on_event("startup")
def on_startup():
    pass

# TODO: Create endpoint to add a new hero
# Use HeroCreate for input validation and HeroPublic for response
# Hint: Use Hero.model_validate(hero) to convert HeroCreate to Hero
@app.post("/heroes/", response_model=HeroPublic)
def create_hero(hero: HeroCreate, session: SessionDep):
    pass

# TODO: Create endpoint to read heroes with pagination
# Use response_model=list[HeroPublic] and Query(le=100) for limit
# Hint: Use session.exec(select(Hero).offset(offset).limit(limit)).all()
@app.get("/heroes/", response_model=list[HeroPublic])
def read_heroes(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    pass

# TODO: Create endpoint to read a single hero by ID
# Use response_model=HeroPublic and check if hero exists
# Hint: Use session.get(Hero, hero_id) and raise 404 if not found
@app.get("/heroes/{hero_id}", response_model=HeroPublic)
def read_hero(hero_id: int, session: SessionDep):
    pass

# TODO: Create endpoint to update a hero
# Use PATCH for partial updates with HeroUpdate model
# Hint: Use hero.model_dump(exclude_unset=True) and hero_db.sqlmodel_update(hero_data)
@app.patch("/heroes/{hero_id}", response_model=HeroPublic)
def update_hero(hero_id: int, hero: HeroUpdate, session: SessionDep):
    pass

# TODO: Create endpoint to delete a hero
# Check if hero exists, then delete and return {"ok": True}
# Hint: Use session.get(), session.delete(), and session.commit()
@app.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session: SessionDep):
    pass