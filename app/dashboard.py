import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Climate Trend Analyzer", layout="wide")

st.title("🌍 Climate Trend Analyzer Dashboard")

# Load dataset
df = pd.read_csv("data/climate_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Sidebar filters
st.sidebar.header("Filters")
year_min = df["Date"].dt.year.min()
year_max = df["Date"].dt.year.max()

year_range = st.sidebar.slider("Select Year Range", year_min, year_max, (year_min, year_max))

df_filtered = df[(df["Date"].dt.year >= year_range[0]) & (df["Date"].dt.year <= year_range[1])]

# ---- Temperature Trend ----
st.subheader("🌡️ Temperature Trend Over Time")

fig, ax = plt.subplots()
ax.plot(df_filtered["Date"], df_filtered["Temperature"], color="red")
ax.set_title("Temperature Trend")
ax.set_xlabel("Date")
ax.set_ylabel("Temperature")
st.pyplot(fig)

# ---- Rainfall ----
st.subheader("🌧️ Rainfall Trend")

fig2, ax2 = plt.subplots()
ax2.plot(df_filtered["Date"], df_filtered["Rainfall"], color="blue")
ax2.set_title("Rainfall Trend")
st.pyplot(fig2)

# ---- CO2 ----
st.subheader("🏭 CO₂ Trend")

fig3, ax3 = plt.subplots()
ax3.plot(df_filtered["Date"], df_filtered["CO2"], color="green")
ax3.set_title("CO₂ Levels Over Time")
st.pyplot(fig3)

# ---- Correlation ----
st.subheader("📊 Correlation Heatmap")

fig4, ax4 = plt.subplots()
sns.heatmap(df_filtered[["Temperature", "Rainfall", "CO2"]].corr(), annot=True, cmap="coolwarm", ax=ax4)
st.pyplot(fig4)

st.success("Dashboard Loaded Successfully 🚀")