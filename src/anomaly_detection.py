import numpy as np

def detect_anomalies(df):

    # Temperature anomaly detection (statistical method)
    temp_mean = df["Temperature"].mean()
    temp_std = df["Temperature"].std()

    df["Temp_Anomaly"] = np.where(
        abs(df["Temperature"] - temp_mean) > 2 * temp_std,
        True,
        False
    )

    # Rainfall anomaly detection
    rain_mean = df["Rainfall"].mean()
    rain_std = df["Rainfall"].std()

    df["Rain_Anomaly"] = np.where(
        abs(df["Rainfall"] - rain_mean) > 2 * rain_std,
        True,
        False
    )

    return df