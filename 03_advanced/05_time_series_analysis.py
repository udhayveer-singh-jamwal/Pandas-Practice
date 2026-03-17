import pandas as pd

dates = pd.date_range("2025-01-01", periods=10)
data = {
    "Date": dates,
    "Sales": [1000, 1200, 1500, 1700, 1600, 1800, 2000, 2100, 2200, 2300]
}
df = pd.DataFrame(data)
df.set_index("Date", inplace=True)
monthly = df.resample("M").sum()
print("Daily Data:\n", df)
