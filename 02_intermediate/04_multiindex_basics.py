import pandas as pd
data = {
    "Region": ["North", "North", "South", "South"],
    "Year": [2024, 2025, 2024, 2025],
    "Sales": [1000, 1500, 1200, 1700]
}

df = pd.DataFrame(data)
multi = df.set_index(["Region", "Year"])
print("MultiIndex Data:\n", multi)
print("\nAccess North 2025:\n", multi.loc[("North", 2025)])
printf()
