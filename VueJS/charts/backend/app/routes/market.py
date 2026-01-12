from fastapi import FastAPI
from app.schemas.tick import MarketResponse, MarketQuery, MarketRow
from app.data.loader import load_ticks
from app.data.resample import resample_bars
from fastapi import APIRouter

router = APIRouter()

@router.post("/market/data", response_model=MarketResponse)
def get_market_data(q: MarketQuery):
    # 1. Load ticks from S3 (MinIO)
    df = load_ticks(
        symbol=q.symbol,
        start_ts=q.start_time,
        end_ts=q.end_time,
    )
    # 2. Resample if needed
    if q.mode == "bars":
        if not q.bar_size:
            raise ValueError("bar_size required for bars mode")
        df = resample_bars(df, q.bar_size)
        time_col = "bar"
    else:
        time_col = "timestamp"

    # 3. Convert to response rows
    rows = [
        MarketRow(
            timestamp=row[time_col],
            open=row["open"],
            high=row["high"],
            low=row["low"],
            close=row["close"],
            volume=row["volume"],
            trade_count=row["trade_count"],
            vwap=row["vwap"],
        )
        for row in df.iter_rows(named=True)
    ]

    # 4. Return schema-safe response
    return MarketResponse(
        symbol=q.symbol,
        model=q.mode,
        bar_size=q.bar_size,
        start_time=q.start_time,
        end_time=q.end_time,
        rows=rows,
        count=len(rows),
    )
