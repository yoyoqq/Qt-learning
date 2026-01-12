from fastapi import FastAPI
from app.routes import market
from app.ws import websocket 

app = FastAPI()

app.include_router(market.router, prefix="/market", tags=["market"])
app.include_router(websocket.router, prefix="/websocket", tags=["websocket"])

