import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [23, 30, 22, 28, 35],
    "Salary": [40000, 70000, 35000, 60000, 80000]
}
df = pd.DataFrame(data)
filtered = df[(df["Age"] > 25) & (df["Salary"] > 50000)]
print("Original Data:\n", df)
print("Filtered Data:\n", filtered)
