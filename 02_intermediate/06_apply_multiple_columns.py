import pandas as pd

data = {
    "Math": [85, 90, 78],
    "Science": [80, 85, 75],
    "English": [88, 92, 70]
}
df = pd.DataFrame(data)
def grade(row):
    avg = (row["Math"] + row["Science"] + row["English"]) / 3
    if avg >= 85:
        return "A"
    elif avg >= 75:
        return "B"
    else:
        return "C"
df["Grade"] = df.apply(grade, axis=1)
print(df)
