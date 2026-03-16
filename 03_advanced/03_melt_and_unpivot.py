import pandas as pd

data = {
    "Student": ["A", "B", "C"],
    "Math": [85, 90, 78],
    "Science": [80, 88, 75]
}

df = pd.DataFrame(data)
melted = pd.melt(
    df,
    id_vars="Student",
    var_name="Subject",
    value_name="Marks"
)
print(melted)
