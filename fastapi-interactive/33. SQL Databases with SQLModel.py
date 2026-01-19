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