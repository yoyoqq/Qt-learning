from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Any

# symbol	timestamp	open	high	low	close	volume	trade_count	vwap
class MarketRow(BaseModel):
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float
    trade_count: int
    vwap: float

class MarketResponse(BaseModel):
    symbol: str
    model: str
    bar_size: Optional[str]
    start_time: datetime
    end_time: datetime
    rows: List[MarketRow]
    count: int
    
class IndicatorSpec(BaseModel):
    name: str
    params: dict[str, Any] = {}

class MarketQuery(BaseModel):
    symbol: str
    start_time: datetime
    end_time: datetime
    mode: str = "bars"      # ticks | bars 
    bar_size: Optional[str] = "1s"
    indicators: Optional[List[IndicatorSpec]] = None
    limit: Optional[int] = 100_000
