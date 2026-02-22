import pandas as pd

data = [10, 20, 30, 40, 50]
series = pd.Series(data, index=["a", "b", "c", "d", "e"])

print("Series:\n", series)
print("Values:", series.values)
print("Index:", series.index)
print("Access by label:", series["c"])
print("Access by position:", series.iloc[2])
series["c"] = 100
print("Updated Series:\n", series)
