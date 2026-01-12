from fastapi import APIRouter, WebSocket, Query
from datetime import datetime
from app.data.loader import load_ticks
from app.data.resample import resample_bars
from app.streaming.ticks import stream_ticks

router = APIRouter()

@router.websocket("/ws/market/data")
async def stream_market_data(
    ws: WebSocket,
    symbol: str = Query(...),           # these parameters come from the URL client 
    start_time: datetime = Query(...),
    end_time: datetime = Query(...),
    mode: str = Query("ticks"),
    bar_size: str | None = Query(None),
    speed: float = Query(1.0)
):
    await ws.accept()
    df = load_ticks(symbol, start_time, end_time)
    
    # resample if needed 
    if mode == "bars":
        if not bar_size:
            await ws.close(code=1003)
            return
        df = resample_bars(df, bar_size)
        time_col = "bar"
    else:
        time_col = "timestamp"
    
    try:
        async for row in stream_ticks(df, speed=speed):
            await ws.send_json({
                "timestamp": row[time_col].isoformat(),
                "open": row["open"],
                "high": row["high"],
                "low": row["low"],
                "close": row["close"],
                "volume": row["volume"],
                "trade_count": row["trade_count"],
                "vwap": row["vwap"],
            })
    except Exception as e:
        raise e
    finally:
        await ws.close()