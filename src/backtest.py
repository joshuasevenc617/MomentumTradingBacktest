import pandas as pd


def backtest_signals(df: pd.DataFrame, initial_capital: float = 10000.0) -> pd.DataFrame:
    df = df.copy()

    if "Adj Close" not in df.columns:
        raise KeyError(
            "DataFrame missing 'Adj Close' column. Ensure your data is processed correctly.")

    if "signal" not in df.columns:
        raise KeyError(
            "DataFrame missing 'signal' column. Generate signals before backtesting.")

    df["daily_returns"] = df["Adj Close"].pct_change()

    df["strategy_return"] = df["daily_returns"] * df["signal"].shift(1)

    df["cum_strategy_return"] = (1.0 + df["strategy_return"]).cumprod()
    df["cum_market_return"] = (1.0 + df["daily_returns"]).cumprod()

    df["portfolio_value"] = initial_capital * df["cum_strategy_return"]

    return df


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


def save_data(df: pd.DataFrame, file_path: str) -> None:
    try:
        df.to_csv(file_path)
        print(f"Data saved successfully to {file_path}")
    except Exception as e:
        print(f"Error saving data to {file_path}: {e}")
        raise e


if __name__ == "__main__":
    input_file = "data/processed/AAPL_signals.csv"
    output_file = "data/processed/AAPL_backtest_result.csv"

    df = load_data(input_file)

    try:
        result_df = backtest_signals(df)
    except Exception as e:
        print(f"Error during backtesting: {e}")
        raise e

    save_data(result_df, output_file)

    final_value = result_df["portfolio_value"].iloc[-1]
    print(f"Final portfolio value: ${final_value:.2f}")
