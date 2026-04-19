import pandas as pd

def add_trend_features(df):

    # Moving average (smooth climate trend)
    df["Temp_MA"] = df["Temperature"].rolling(window=6).mean()
    df["Rain_MA"] = df["Rainfall"].rolling(window=6).mean()
    df["CO2_MA"] = df["CO2"].rolling(window=6).mean()

    return df