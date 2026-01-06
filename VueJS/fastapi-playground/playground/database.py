# app/database.py
from typing import List
from pydantic import BaseModel
import json
import os

# Simulating a database with lists
users_db: List[dict] = []
items_db: List[dict] = []
current_id = 0

# Load items from file if exists
ITEMS_FILE = 'items.json'
if os.path.exists(ITEMS_FILE):
    with open(ITEMS_FILE, 'r') as f:
        items_db = json.load(f)
    # Set current_id to next available
    if items_db:
        current_id = max(item['id'] for item in items_db) + 1
