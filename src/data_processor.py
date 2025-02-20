import pandas as pd


def process_data(file_path: str, output_file_path: str) -> None:
    df = pd.read_csv(file_path)

    df = df.iloc[2:, :]
    df.columns = ["Date", "Adj Close", "Close",
                  "High", "Low", "Open", "Volume"]

    df["Date"] = pd.to_datetime(df["Date"])
    df.reset_index(drop=True, inplace=True)

    for col in ["Open", "High", "Low", "Close", "Adj Close"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df.to_csv(output_file_path, index=False)


if __name__ == "__main__":
    input_file = "data/raw/300760.SZ.csv"
    output_file = "data/processed/300760.SZ.csv"

    process_data(input_file, output_file)
