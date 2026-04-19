import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)

    # Convert date column
    df["Date"] = pd.to_datetime(df["Date"])

    # Sort by date
    df = df.sort_values("Date")

    # Handle missing values (if any)
    df = df.dropna()

    return df