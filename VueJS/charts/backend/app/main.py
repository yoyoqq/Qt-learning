from fastapi import FastAPI
from app.schemas.tick import MarketResponse, MarketQuery

app = FastAPI()

@app.post("/market/data", response_model=MarketResponse)
def get_market_data(q: MarketQuery):
    """
    1. Load parquet by symbol 
    2. Filter timestamp 
    3. Aggregate bars 
    4. Compute VWAP / indicators 
    5. Return schema-safe response 
    """
    return MarketResponse(
        symbol=q.symbol,
        model=q.mode,
        bar_size=q.bar_size,
        start_time=q.start_time,
        end_time=q.end_time,
        rows=[],
        count=0 
    )




# app.router()
# class User(BaseModel):
#     name: str
#     surname: str
#     id: int
#     street: str
# app = FastAPI()
# @app.get("/")
# def main(user: User):
#     return user
# @app.get("")
# def hello(name: str, surname: str, id: str, street: str):
#     return {
#         "name": name,
#         "surname": surname,
#         "id": id,
#         "street": street
#     }
