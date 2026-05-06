# Matrix Plot

# Importing Libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Loading Dataset
flights=sns.load_dataset('flights')
print(flights)
tips=sns.load_dataset('tips')
print(tips)

tipscorr  =tips[['total_bill','tip','size']]
print(tipscorr)
tipscorr.corr()

# Heat Map
sns.heatmap(tipscorr.corr(),annot=True)
plt.show()

# Cluster Map
sns.clustermap(tipscorr.corr(),annot=True)
plt.show()

# Pivot Table Heat Map
pvtflights=flights.pivot_table(values='passengers',index='month',columns='year')
print(pvtflights)
sns.heatmap(pvtflights)
plt.show()