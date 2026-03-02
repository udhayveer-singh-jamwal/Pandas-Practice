import pandas as pd
data = {
    "City": ["Delhi", "Mumbai", "Delhi", "Chennai", "Mumbai"],
    "Sales": [50000, 75000, 60000, 45000, 80000]
}
df = pd.DataFrame(data)
city_total = df.groupby("City")["Sales"].sum()
print("Total Sales by City:\n", city_total)
