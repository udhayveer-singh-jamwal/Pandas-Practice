import pandas as pd

data = {
    "Employee": ["A", "B", "C", "D"],
    "Performance": [75, 90, 85, 80]
}

df = pd.DataFrame(data)
df_sorted = df.sort_values(by="Performance", ascending=False)
print("Sorted Data:\n", df_sorted)
