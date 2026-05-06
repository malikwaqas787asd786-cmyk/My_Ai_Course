import pandas as pd
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}
df = pd.DataFrame(data)
print(df)

import pandas as pd
data_list = [
    ['John', 28, 'New York', 65000],
    ['Anna', 34, 'Paris', 70000],
    ['Peter', 29, 'Berlin', 62000],
    ['Linda', 42, 'London', 85000]
]
df2 = pd.DataFrame(data_list)
columns = ["Name","Age","City","Salary"]
df2 = pd.DataFrame(data_list,columns =columns)
print(df2)

#Selecting and indexing of Columns
import pandas as pd
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}
print(pd.DataFrame(data)[['City','Salary']])

#Creating a new column in DataFrame
import pandas as pd
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}
df = pd.DataFrame(data)
df['Designation'] = ['Manager', 'Developer', 'Analyst', 'Director']
print(df)

#Removing a column from DataFrame
import pandas as pd
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}
df = pd.DataFrame(data)
df.drop('Salary', axis=1, inplace=True)
print(df)

#Selecting rows using loc and iloc
import pandas as pd
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}
df = pd.DataFrame(data)
# Using loc to select rows by label
print(df.loc[0])  # First row
print("-------------------")
# Using iloc to select rows by position
print(df.iloc[1])  # Second row

#Selecting Subset of rows and columns
import pandas as pd
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}
df = pd.DataFrame(data)
# Selecting subset of rows and columns using loc
print(df.loc[0:2, ['Name', 'City']])
print(df.loc[2:3, ['Name', 'Age']])

#Conditional Selection in DataFrame
import pandas as pd
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, 29, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London'],
    'Salary': [65000, 70000, 62000, 85000]
}
df = pd.DataFrame(data)
# Selecting rows where Age is greater than 30
print(df[df['Age'] > 30])
print("-------------------")
# Selecting rows where City is 'Paris' and Salary is greater than 60000
print(df[(df['City'] == 'Paris') & (df['Salary'] > 60000)])