import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"]
}
df = pd.DataFrame(data)
counts = df["Department"].value_counts()
print("Department Distribution:\n", counts)
