"""
Docstring for 19. JSON compatible encoder

Use jsonable_encoder when storing Pydantic models in databases
Always convert datetime objects before JSON serialization
Remember that jsonable_encoder returns Python data structures, not JSON strings
The result can be used with Python's standard json.dumps()
"""
from datetime import datetime
from typing import Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Union[str, None] = None


app = FastAPI()


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    # TODO: Use jsonable_encoder to convert the Pydantic model to JSON-compatible format
    # TODO: Store the encoded item data in fake_db with the id as key
    # TODO: Return the encoded data to show it's working
    # Hint: json_compatible_item_data = jsonable_encoder(item)
    # Hint: fake_db[id] = json_compatible_item_data
    # Hint: return json_compatible_item_data
    # pass
    # json_comp = jsonable_encoder(item)
    json_comp = item.model_dump()
    fake_db[id] = json_comp
    return json_comp