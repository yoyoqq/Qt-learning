from dateutil.relativedelta import relativedelta
import polars as pl


def month_range(start, end):
    cur = start.replace(day=1)
    while cur <= end:
        yield cur
        cur += relativedelta(months=1)


def load_ticks(symbol: str, start_ts, end_ts, limit: int = 1000) -> pl.DataFrame:
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
            "endpoint_url": "http://localhost:9100",
        },
    )

    df = (
        df.filter(
            (pl.col("timestamp") >= start_ts) &
            (pl.col("timestamp") <= end_ts)
        )
        .sort("timestamp", descending=True)
    )

    # df = df.sort("bar", descending=True).limit(limit)
    # return df.collect()
    
    return df.limit(limit).collect()
