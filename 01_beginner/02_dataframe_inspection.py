import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Karan", "Sneha", "Rahul"],
    "Age": [23, 25, 22, 24, 26],
    "Salary": [40000, 50000, 35000, 60000, 45000]
}

df = pd.DataFrame(data)
print("First 3 rows:\n", df.head(3))
print("\nLast 2 rows:\n", df.tail(2))
print("\nShape:", df.shape)
print("\nColumns:", df.columns)
print("\nData Types:\n", df.dtypes)
print("\nSummary Statistics:\n", df.describe())
