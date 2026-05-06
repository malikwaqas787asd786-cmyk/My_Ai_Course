#Merging 2 DataFrames using merge() function
import pandas as pd
employees = pd.DataFrame({
    'employee_id': [1, 2, 3, 4, 5],
    'name': ['John', 'Anna', 'Peter', 'Linda', 'Bob'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR']
})
# DataFrame 2: Salary information
salaries = pd.DataFrame({
    'employee_id': [1, 2, 3, 6, 7],
    'salary': [60000, 80000, 65000, 70000, 90000],
    'bonus': [5000, 10000, 7000, 8000, 12000]
})
# Merging the two DataFrames on 'employee_id'
merged_df1 = pd.merge(employees, salaries, on='employee_id', how='inner')
print("Inner Join:")
print(merged_df1)
merged_df2 = pd.merge(employees, salaries, on='employee_id', how='outer')
print("\nOuter Join:")
print(merged_df2)
merged_df3 = pd.merge(employees, salaries, on='employee_id', how='left')
print("\nLeft Join:")
print(merged_df3)
merged_df4 = pd.merge(employees, salaries, on='employee_id', how='right')
print("\nRight Join:")
print(merged_df4)


#Concatenating DataFrames using concat() function
import pandas as pd
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2'],
    'C': ['C0', 'C1', 'C2']
})
df2 = pd.DataFrame({
    'A': ['A3', 'A4', 'A5'],
    'B': ['B3', 'B4', 'B5'],
    'C': ['C3', 'C4', 'C5']
})

# Concatenating vertically (default)
concat_vertical = pd.concat([df1, df2])
print(concat_vertical)

# Concatenating horizontally
concat_horizontal = pd.concat([df1, df2], axis=1)
print(concat_horizontal)

#Joining DataFrames using join() function
import pandas as pd

# First DataFrame
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie']
}, index=[1, 2, 3])

# Second DataFrame
df2 = pd.DataFrame({
    'Score': [85, 90, 75]
}, index=[2, 3, 4])

# Joining df1 and df2 on their indices
joined_df1 = df1.join(df2)
print("Inner Join:")

print(joined_df1)
joined_df = df1.join(df2,how='outer')  # Outer join to include all indices
print(joined_df)