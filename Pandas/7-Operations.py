#Operations
import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
})
print(df1.shape)
print(df1.columns)
print(df1.info())
print(df1.describe())
print(df1['A'] + 10)

#DataFrame Applying Functions
import pandas as pd
df = pd.DataFrame({
    "Marks": [50, 70, 90]
})
def grade(x):
    if x >= 80:
        return "A"
    elif x >= 60:
        return "B"
    else:
        return "C"
df["Grade"] = df["Marks"].apply(grade)
print(df)