import pandas as pd

data = {
    "Department": ["IT", "IT", "HR", "HR", "Finance"],
    "Employee": ["A", "B", "C", "D", "E"],
    "Salary": [60000, 80000, 50000, 55000, 70000]
}

df = pd.DataFrame(data)
df["Dept_Avg"] = df.groupby("Department")["Salary"].transform("mean")
df["Above_Avg"] = df["Salary"] > df["Dept_Avg"]
print(df)
