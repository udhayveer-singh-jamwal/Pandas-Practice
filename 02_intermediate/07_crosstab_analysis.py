import pandas as pd
data = {
    "Gender": ["M", "F", "M", "F", "M", "F"],
    "Department": ["IT", "HR", "Finance", "IT", "HR", "Finance"]
}
df = pd.DataFrame(data)
cross = pd.crosstab(df["Gender"], df["Department"])
print("Crosstab Analysis:\n", cross)
