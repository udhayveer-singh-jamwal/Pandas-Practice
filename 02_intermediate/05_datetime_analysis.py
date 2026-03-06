import pandas as pd

data = {
    "Date": pd.date_range(start="2025-01-01", periods=10, freq="M"),
    "Sales": [1000, 1200, 1500, 1700, 1600, 1800, 2000, 2100, 2200, 2300]
}

df = pd.DataFrame(data)
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
monthly_avg = df.groupby("Month")["Sales"].mean()
print("Data:\n", df)
print("Monthly Average:\n", monthly_avg)
