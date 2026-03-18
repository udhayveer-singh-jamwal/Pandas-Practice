import pandas as pd
data = {
    "Sales": [1000, 1200, 1500, 1700, 1600, 1800, 2000]
}
df = pd.DataFrame(data)
df["Rolling_Mean"] = df["Sales"].rolling(window=3).mean()
df["Rolling_Max"] = df["Sales"].rolling(window=3).max()
print(df)
