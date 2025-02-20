import os
import yfinance as yf
import pandas as pd
from typing import Optional


def fetch_data(ticker: str, start_date: str, end_date: str, save_path: str = "data/raw") -> Optional[pd.DataFrame]:
    os.makedirs(save_path, exist_ok=True)

    try:
        data = yf.download(ticker, start=start_date,
                           end=end_date, auto_adjust=False)
    except Exception as e:
        print(f"Error downloading data for {ticker}: {e}")
        return None

    if data is None or data.empty:
        print(f"No data for {ticker} between {start_date} and {end_date}.")
        return None

    file_name = f"{ticker}.csv"
    file_path = os.path.join(save_path, file_name)
    data.to_csv(file_path)

    print(f"Data for {ticker} saved to {file_path}")
    return data


if __name__ == "__main__":
    # fetch_data("AAPL", "2020-01-01", "2021-01-01")
    fetch_data("300760.SZ", "2023-01-01", "2025-01-01")
