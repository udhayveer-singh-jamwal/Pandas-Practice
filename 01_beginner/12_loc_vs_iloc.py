import pandas as pd

data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [45, 78, 88, 32]
}
df = pd.DataFrame(data)
print("Using loc:\n", df.loc[1:2])
print("Using iloc:\n",df.iloc[1:3])
print("Single value using loc:", df.loc[0, "Marks"])
print("Single value using iloc:", df.iloc[0, 1])
