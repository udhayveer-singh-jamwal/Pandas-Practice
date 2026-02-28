import pandas as pd

data = {
    "Name": ["aman", "riya", "karan"],
    "Email": ["aman@gmail.com", "riya@yahoo.com", "karan@gmail.com"]
}
df = pd.DataFrame(data)
df["Name"] = df["Name"].str.capitalize()
df["Domain"] = df["Email"].str.split("@").str[1]
gmail_users = df[df["Domain"] == "gmail.com"]
print(df)
print("\nGmail Users:\n", gmail_users)
