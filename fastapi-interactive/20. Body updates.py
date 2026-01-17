"""

Critical Warning: Missing fields in PUT requests will use their model defaults, potentially overwriting valuable data. In the example above, the custom tax: 20.2 was lost and reverted to the default 10.5.
The HTTP PATCH method is designed for partial modifications. When you use PATCH, you're saying "only change these specific fields, leave everything else alone."
Use PUT when:
    You have the complete, updated resource
    You want to replace all fields intentionally
    You're implementing "save" functionality where users edit all fields
Use PATCH when:
    You only want to update specific fields
    You're implementing incremental updates
    You want to preserve existing data you don't have access to
    You're building mobile apps with limited bandwidth

exclude_unset Parameter: The secret to safe partial updates lies in Pydantic's exclude_unset parameter:


Use PUT for complete resource replacement
Use PATCH for partial updates to avoid data loss
Always validate that the resource exists before updating
Use exclude_unset=True to only get explicitly set fields
Handle 404 errors gracefully for non-existent resources
Use response_model to ensure consistent API responses


"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: float = 10.5

# Simulated database
items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5}
}

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    """Get an item by ID."""
    # TODO: Check if item exists, return 404 if not found
    if item_id not in items:
        raise HTTPException(404)
    # TODO: Return the item data
    return items[item_id]

@app.put("/items/{item_id}", response_model=Item)
async def update_item_with_put(item_id: str, item: Item):
    """Update an item completely (full replacement)."""
    # TODO: Check if item exists, return 404 if not found
    if item_id not in items:
        raise HTTPException(404, detail="Item not found")
    # TODO: Convert item to dict using jsonable_encoder and store in database
    items[item_id] = item.model_dump()
    # TODO: Return the encoded item
    return item 

@app.patch("/items/{item_id}", response_model=Item)
async def update_item_with_patch(item_id: str, item: Item):
    """Update an item partially (only provided fields)."""
    # TODO: Check if item exists, return 404 if not found
    if item_id not in items:
        raise HTTPException(404)
    # TODO: Get stored item and convert to Pydantic model
    stored_item = Item(**items[item_id])
    # TODO: Get only the fields that were set using item.dict(exclude_unset=True)
    update_data = item.model_dump(exclude_unset=True)
    # TODO: Create updated model using stored_item_model.copy(update=update_data)
    updated_item = stored_item.model_copy(update=update_data)
    # TODO: Store updated item using jsonable_encoder and return the model
    items[item_id] = updated_item.model_dump()

    return updated_item