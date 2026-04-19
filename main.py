from src.preprocessing import load_and_clean_data
from src.eda import run_eda
from src.trend_analysis import add_trend_features
from src.anomaly_detection import detect_anomalies

# Load dataset
df = load_and_clean_data("data/climate_data.csv")

# EDA (graphs)
run_eda(df)

# Trend analysis
df = add_trend_features(df)

# Anomaly detection
df = detect_anomalies(df)

# Show anomalies
print("\n🚨 Climate Anomalies Detected:")
print(df[df["Temp_Anomaly"] == True][["Date", "Temperature"]])

print("\n🚨 Rainfall Anomalies Detected:")
print(df[df["Rain_Anomaly"] == True][["Date", "Rainfall"]])