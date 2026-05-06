import pandas as pd
# Creating a Series from a list
data = [10, 20, 30, 40]
print(pd.Series(data))


import pandas as pd
data = [10, 20, 30, 40]
# Custom indices/Labels
indices = ['a', 'b', 'c', 'd']
# Making a Series with custom indices
print(pd.Series(data, index=indices))
