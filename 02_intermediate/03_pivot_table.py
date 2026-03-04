import pandas as pd
data = {
    "Region": ["North", "South", "North", "South", "North"],
    "Product": ["A", "A", "B", "B", "A"],
    "Sales": [100, 150, 200, 250, 120]
}
df = pd.DataFrame(data)
pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum"
)

print("Pivot Table:\n", pivot)
