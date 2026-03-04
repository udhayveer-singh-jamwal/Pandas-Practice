import pandas as pd

employees = pd.DataFrame({
    "EmpID": [1, 2, 3, 4],
    "Name": ["Aman", "Riya", "Karan", "Sneha"]
})
departments = pd.DataFrame({
    "EmpID": [1, 2, 4],
    "Department": ["IT", "HR", "Finance"]
})
merged = pd.merge(employees, departments, on="EmpID", how="left")
print("Employees:\n", employees)
print("\nDepartments:\n", departments)
print("\nMerged Data:\n", merged)
