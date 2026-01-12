from pydantic import BaseModel
from datetime import datetime, timezone
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
    symbol: str = "SPY"
    start_time: datetime = datetime(2023, 1, 2, 0, 0, tzinfo=timezone.utc)
    end_time: datetime = datetime(2023, 1, 5, 0, 0, tzinfo=timezone.utc)
    mode: str = "bars"      # ticks | bars 
    bar_size: Optional[str] = "5m"
    indicators: Optional[List[IndicatorSpec]] = None
    limit: Optional[int] = 100_000
