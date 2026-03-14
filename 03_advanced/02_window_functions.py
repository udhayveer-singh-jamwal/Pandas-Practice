import pandas as pd

data = {
    "Department": ["IT", "IT", "HR", "HR", "IT"],
    "Employee": ["A", "B", "C", "D", "E"],
    "Salary": [60000, 80000, 50000, 55000, 75000]
}
df = pd.DataFrame(data)
df["Rank"] = df.groupby("Department")["Salary"].rank(ascending=False)
print(df.sort_values(["Department", "Rank"]))
