#Finding Missing Data in a DataFrame
import numpy as np
import pandas as pd
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [1, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan],
    'D': [1, np.nan, np.nan, np.nan, 5]
}
df = pd.DataFrame(data)
print(df)
print("-------------------")
#Finding missing data using isna()
print(df.isna())
print("-------------------")
print(df.isna().sum())
print("-------------------")
print(df.isna().any())

import pandas as pd
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, None, 42],
    'City': ['New York', 'Paris', 'Berlin', None],
    'Salary': [65000, None, 62000, 85000]
}
df = pd.DataFrame(data)
print(df)
#Finding missing data using isnull() and notnull()
print(df.isnull())
#Finding non-missing data using notnull()
print(df.notnull())

#Removing Missing Data from a DataFrame
import pandas as pd
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 34, None, 42],
    'City': ['New York', 'Paris', 'Berlin', None],
    'Salary': [65000, None, 62000, 85000]
}
df = pd.DataFrame(data)
print(df)
print("-------------------")
#Removing rows with missing data using dropna()
df_cleaned = df.dropna()
print(df_cleaned)
print("-------------------")
print(df.dropna(thresh=3))  # Keep rows with at least 3 non-NA values

#Filling Missing Data in a DataFrame
import numpy as np
import pandas as pd
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [1, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan],
    'D': [1, np.nan, np.nan, np.nan, 5]
}
df = pd.DataFrame(data)
print(df)
print("-------------------")
#Filling missing data with a specific value using fillna()
df_filled = df.fillna(0)
print(df_filled)
print("-------------------")
values = {'A':0,'B':100,"C":300,'D':400}
print(df.fillna(value=values))
print("-------------------")
print(df.fillna(df.mean()))