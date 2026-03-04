import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Salary": [60000, 45000, 70000, 50000, 55000, 80000],
    "Experience": [3, 5, 4, 6, 2, 7]
}
df = pd.DataFrame(data)
grouped = df.groupby("Department").agg({
    "Salary": ["mean", "max", "min"],
    "Experience": "mean"
})
print("Grouped Analysis:\n", grouped)
