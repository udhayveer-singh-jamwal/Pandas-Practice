import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [45, 78, 88, 32]
}

df = pd.DataFrame(data)
def result(marks):
    if marks >= 50:
        return "Pass"
    else:
        return "Fail"

df["Result"] = df["Marks"].apply(result)
print(df)
