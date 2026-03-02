import pandas as pd

data = {
    "Student": ["A", "B", "C", "D"],
    "Marks": [35, 78, 48, 90]
}
df = pd.DataFrame(data)
df.loc[df["Marks"] < 50, "Marks"] = 50
df["Status"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")
print(df)
