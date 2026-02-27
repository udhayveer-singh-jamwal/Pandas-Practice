import pandas as pd

data = {
    "Name": ["A", "B", "A", "C", "B"],
    "Marks": [85, 90, 85, 78, 90]
}

df = pd.DataFrame(data)
duplicates = df.duplicated()
print("Duplicate Rows:\n", duplicates)
df_cleaned = df.drop_duplicates()
print("After Removing Duplicates:\n", df_cleaned)
