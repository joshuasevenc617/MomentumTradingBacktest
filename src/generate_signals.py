import pandas as pd


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


def generate_signals(df: pd.DataFrame, short_window: int = 20, long_window: int = 50) -> pd.DataFrame:
    if "Adj Close" not in df.columns:
        raise KeyError(
            "DataFrame does not contain the 'Adj Close' column. Please check your data.")

    df["short_mavg"] = df["Adj Close"].rolling(
        window=short_window, min_periods=1).mean()
    df["long_mavg"] = df["Adj Close"].rolling(
        window=long_window, min_periods=1).mean()

    df["signal"] = 0
    df.loc[df["short_mavg"] > df["long_mavg"], "signal"] = 1

    df["positions"] = df["signal"].diff()

    return df


if __name__ == "__main__":
    input_file = "data/processed/AAPL.csv"
    output_file = "data/processed/AAPL_signals.csv"

    df = load_data(input_file)

    try:
        df_signals = generate_signals(df)
    except Exception as e:
        print(f"Error generating signals: {e}")
        raise e

    save_data(df_signals, output_file)
