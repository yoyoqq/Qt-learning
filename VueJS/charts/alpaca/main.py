from datetime import datetime
from dateutil.relativedelta import relativedelta
import polars as pl

def month_range(start, end):
    cur = start.replace(day=1)
    while cur <= end:
        yield cur
        cur += relativedelta(months=1)


def load_ticks(symbol, start_ts, end_ts):
    paths = []

    for d in month_range(start_ts, end_ts):
        paths.append(
            f"s3://market-data/symbol={symbol}/year={d.year}/month={d.month:02d}.parquet"
        )

    df = pl.scan_parquet(
        paths,
        storage_options={
            "aws_access_key_id": "minioadmin",
            "aws_secret_access_key": "minioadmin",
            "endpoint_url": "http://localhost:9000",
        },
    )

    df = df.filter(
        (pl.col("timestamp") >= start_ts) &
        (pl.col("timestamp") <= end_ts)
    ).sort("timestamp")

    return df.collect()

import polars as pl

def resample_bars(bars: pl.DataFrame, timeframe: str) -> pl.DataFrame:
    """
    timeframe: "5m", "15m", "1h", "1d", "1w", "1mo"
    """

    if timeframe in {"5m", "15m", "1h"}:
        rule = {"5m": "5m", "15m": "15m", "1h": "1h"}[timeframe]
        df = bars.with_columns(pl.col("timestamp").dt.truncate(rule).alias("bar"))

    elif timeframe == "1d":
        df = bars.with_columns(pl.col("timestamp").dt.date().alias("bar"))

    elif timeframe == "1w":
        df = bars.with_columns(pl.col("timestamp").dt.truncate("1w").alias("bar"))

    elif timeframe == "1mo":
        df = bars.with_columns(
            pl.col("timestamp")
            .dt.strftime("%Y-%m-01")
            .str.strptime(pl.Date)
            .alias("bar")
        )

    else:
        raise ValueError("timeframe must be one of: 5m, 15m, 1h, 1d, 1w, 1mo")

    out = (
        df.group_by("bar")
        .agg([
            pl.col("open").first().alias("open"),
            pl.col("high").max().alias("high"),
            pl.col("low").min().alias("low"),
            pl.col("close").last().alias("close"),
            pl.col("volume").sum().alias("volume"),
            pl.col("trade_count").sum().alias("trade_count"),
            ((pl.col("vwap") * pl.col("volume")).sum() / pl.col("volume").sum()).alias("vwap"),
        ])
        .sort("bar")
    )

    return out
