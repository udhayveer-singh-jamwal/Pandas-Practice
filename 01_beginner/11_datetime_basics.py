import pandas as pd

data = {
    "Date": ["2025-01-01", "2025-02-15", "2025-03-20"],
    "Sales": [1000, 1500, 2000]
}

df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
print(df)
