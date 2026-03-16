import pandas as pd

data = {
    "Region": ["North", "North", "South", "South"],
    "Product": ["A", "B", "A", "B"],
    "Sales": [1000, 1500, 2000, 1800]
}

df = pd.DataFrame(data)
pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc=["sum", "mean"]
)
print(pivot))
