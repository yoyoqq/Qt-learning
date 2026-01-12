import asyncio
import polars as pl 

async def stream_ticks(df: pl.DataFrame, speed: float = 1.0):
    rows = df.iter_rows(named=True)

    prev_ts = None

    for row in rows: 
        ts = row["timestamp"]
        if prev_ts is not None:
            delta = (ts - prev_ts).total_seconds()
            await asyncio.sleep(max(delta / speed, 0))
    
        prev_ts = ts 
        yield row 
    