import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Karan"],
    "Age": [23, 25, 22],
    "Salary": [40000, 50000, 35000]
}

df = pd.DataFrame(data)
df.rename(columns={"Salary": "Monthly_Salary"}, inplace=True)
print(df)
