import pandas as pd
import numpy as np


def calculate_performance_metrics(df: pd.DataFrame) -> dict:
    if "portfolio_value" not in df.columns:
        raise KeyError(
            "DataFrame missing 'portfolio_value' column.")
    if "daily_return" not in df.columns:
        df["daily_return"] = df["portfolio_value"].pct_change().fillna(0)

    cumulative_return = df["portfolio_value"].iloc[-1] / \
        df["portfolio_value"].iloc[0] - 1

    avg_daily_return = df["daily_return"].mean()
    std_daily_return = df["daily_return"].std()
    sharpe_ratio = (avg_daily_return / std_daily_return) * \
        np.sqrt(252) if std_daily_return != 0 else np.nan

    df["peak"] = df["portfolio_value"].cummax()
    df["drawdown"] = (df["portfolio_value"] - df["peak"]) / df["peak"]
    max_drawdown = df["drawdown"].min()

    return {
        "cumulative_return": cumulative_return,
        "sharp_ratio": sharpe_ratio,
        "max_drawdown": max_drawdown,
    }


def load_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path, index_col=0)
        print(f"Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError as e:
        print(
            f"Error: the file {file_path} could not be found. Please check the path.")
        raise e
    except Exception as e:
        print(f"An unexpected error occurred while loading the data: {e}")
        raise e


if __name__ == "__main__":
    # input_file = "data/processed/AAPL_backtest_result.csv"
    input_file = "data/processed/300760.SZ_backtest_result.csv"

    try:
        df = load_data(input_file)
    except Exception as e:
        print(f"Error loading backtest results: {e}")
        raise e

    metrics = calculate_performance_metrics(df)
    print("Performance metrics:")
    for k, v in metrics.items():
        if "return" in k or "drawdown" in k:
            print(f"{k}: {v:.2%}")
        else:
            print(f"{k}: {v}")
