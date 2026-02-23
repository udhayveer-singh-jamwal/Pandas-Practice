import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)
df["Bonus"] = df["Marks"] * 0.05
df["Total"] = df["Marks"] + df["Bonus"]
df["Grade"] = df["Marks"].apply(lambda x: "A" if x >= 85 else "B")
print(df)
