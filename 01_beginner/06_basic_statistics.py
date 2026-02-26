import pandas as pd

data = {
    "Sales": [1200, 1500, 1800, 2000, 1700, 1600]
}
df = pd.DataFrame(data)
print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Median:", df["Sales"].median())
print("Standard Deviation:", df["Sales"].std())
print("Variance:", df["Sales"].var())
