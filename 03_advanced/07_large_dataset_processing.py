import pandas as pd

data = {
    "Region": ["North", "South", "East", "West"] * 1000,
    "Sales": [50000, 60000, 55000, 58000] * 1000
}
df = pd.DataFrame(data)
summary = df.groupby("Region").agg({
    "Sales": ["sum", "mean", "max"]
})
print(summary)
