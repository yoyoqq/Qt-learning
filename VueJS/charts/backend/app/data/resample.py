import polars as pl


def resample_bars(bars: pl.DataFrame, timeframe: str) -> pl.DataFrame:

    # ✅ 1m = already bars → just rename for consistency
    if timeframe == "1m":
        if "bar" not in bars.columns:
            bars = bars.with_columns(
                pl.col("timestamp").alias("bar")
            )
        return bars.sort("bar")

    # intraday
    if timeframe in {"5m", "15m", "1h"}:
        df = bars.with_columns(
            pl.col("timestamp").dt.truncate(timeframe).alias("bar")
        )

    elif timeframe == "1d":
        df = bars.with_columns(
            pl.col("timestamp").dt.date().alias("bar")
        )

    elif timeframe == "1w":
        df = bars.with_columns(
            pl.col("timestamp").dt.truncate("1w").alias("bar")
        )

    elif timeframe == "1mo":
        df = bars.with_columns(
            pl.col("timestamp")
            .dt.strftime("%Y-%m-01")
            .str.strptime(pl.Date)
            .alias("bar")
        )

    else:
        raise ValueError(f"Invalid timeframe: {timeframe}")

    return (
        df.group_by("bar")
        .agg([
            pl.col("open").first().alias("open"),
            pl.col("high").max().alias("high"),
            pl.col("low").min().alias("low"),
            pl.col("close").last().alias("close"),
            pl.col("volume").sum().alias("volume"),
            pl.col("trade_count").sum().alias("trade_count"),
            (
                (pl.col("vwap") * pl.col("volume")).sum()
                / pl.col("volume").sum()
            ).alias("vwap"),
        ])
        .sort("bar")
    )
