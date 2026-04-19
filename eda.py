import pandas as pd
import matplotlib.pyplot as plt

def run_eda(df):

    print("\n📊 Dataset Info")
    print(df.info())

    print("\n📊 Statistical Summary")
    print(df.describe())

    # Temperature trend
    plt.figure(figsize=(12,5))
    plt.plot(df["Date"], df["Temperature"])
    plt.title("Temperature Trend Over Time")
    plt.xlabel("Year")
    plt.ylabel("Temperature (°C)")
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Rainfall trend
    plt.figure(figsize=(12,5))
    plt.plot(df["Date"], df["Rainfall"], color="green")
    plt.title("Rainfall Pattern Over Time")
    plt.xlabel("Year")
    plt.ylabel("Rainfall (mm)")
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # CO2 trend
    plt.figure(figsize=(12,5))
    plt.plot(df["Date"], df["CO2"], color="red")
    plt.title("CO2 Emissions Over Time")
    plt.xlabel("Year")
    plt.ylabel("CO2 Levels")
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()