
"""
Docstring for 10. Extra data types


automatic data conversion from incoming requests 
data conversion for response data 

    Universally Unique Identifier, common as an ID in databases and systems.
    In requests/responses: Represented as a str
    Example: "550e8400-e29b-41d4-a716-446655440000"

    In requests/responses: Represented as a str
    Example: "550e8400-e29b-41d4-a716-446655440000"
    📅 datetime.datetime
    Python datetime.datetime objects.

    In requests/responses: Represented as ISO 8601 format string
    Example: "2008-09-15T15:53:00+05:00"
    📆 datetime.date
    Python datetime.date objects.

    In requests/responses: Represented as ISO 8601 date string
    Example: "2008-09-15"
    ⏰ datetime.time
    Python datetime.time objects.

    In requests/responses: Represented as ISO 8601 time string
    Example: "14:23:55.003"
    ⏱️ datetime.timedelta
    Python datetime.timedelta objects.

    In requests/responses: Represented as float of total seconds
    Example: 3600 (for 1 hour)
    Alternative: ISO 8601 time diff encoding (see Pydantic docs)


"""




# Extra Data Types
# Learn to use advanced Python data types with FastAPI

from datetime import datetime, time, timedelta
from typing import Annotated, Union         # ! use Annotated 
from uuid import UUID
from fastapi import Body, FastAPI

"""
from typing import Annotated

# Modern approach (recommended)
start_datetime: Annotated[datetime, Body()]

# Older approach (still works)
start_datetime: datetime = Body()

"""

app = FastAPI()

# TODO: Create the read_items endpoint
# Endpoint: PUT /items/{item_id}
# Parameters:
# - item_id: UUID (path parameter)
# - start_datetime: Annotated[datetime, Body()]
# - end_datetime: Annotated[datetime, Body()]
# - process_after: Annotated[timedelta, Body()]
# - repeat_at: Annotated[Union[time, None], Body()] = None
#
# Inside the function:
# - Calculate start_process = start_datetime + process_after
# - Calculate duration = end_datetime - start_process
# - Return dict with all parameters plus calculated values
@app.put("/items/{item_id}")
# async def read_items(item_id: UUID, start_datetime: Annotated[datetime, Body()], end_datetime: Annotated[datetime, Body()], process_after: Annotated[datetime, Body()], repeat_at: datetime = Body()):
async def read_items( item_id: UUID, start_datetime: Annotated[datetime, Body()], end_datetime: Annotated[datetime, Body()], process_after: Annotated[timedelta, Body()], repeat_at: Annotated[Union[time, None], Body()] = None, ):

    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }
    