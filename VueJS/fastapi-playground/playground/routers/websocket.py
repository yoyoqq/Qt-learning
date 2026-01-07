from fastapi import FastAPI, WebSocket, APIRouter
import asyncio
from playground.database import items_db

router = APIRouter()

# ticks = [{"symbol": "AAPL", "price": 150}, {"symbol": "GOOG", "price": 2700}]
ticks = [
  {"id": 1, "name": "AAPL", "price": 150},
  {"id": 2, "name": "GOOG", "price": 2700}
]

@router.websocket("/")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        await ws.send_json(items_db)
        await asyncio.sleep(0.5)