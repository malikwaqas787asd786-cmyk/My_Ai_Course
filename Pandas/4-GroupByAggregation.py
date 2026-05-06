import pandas as pd
data = {
    'Team': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B'],
    'Player': ['Ali', 'Sara', 'Ahmed', 'Hina', 'Usman', 'Zara', 'Bilal', 'Noor'],
    'Points': [10, 20, 15, 25, 30, 35, 40, 45]
}
df = pd.DataFrame(data)
print(df)
print("-------------------")
# Grouping by 'Team' and calculating the sum of 'Points'
grouped=df.groupby('Team')['Points'].sum()
print(grouped)
print("-------------------")

# Grouping by 'Team' and calculating the mean of 'Points'
grouped_mean=df.groupby('Team')['Points'].mean()
print(grouped_mean)
print("-------------------")

# Grouping by 'Team' and calculating multiple aggregations
grouped_multi=df.groupby('Team')['Points'].agg(['sum', 'mean', 'max'])
print(grouped_multi)