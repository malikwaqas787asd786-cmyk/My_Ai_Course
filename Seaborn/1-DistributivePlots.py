import matplotlib.pyplot as plt
import seaborn as sns
df=sns.load_dataset('tips')
print(df)
print(df['size'].unique())

# Displot/Histplot
sns.displot(df['total_bill'],kde=True)
plt.show()

sns.displot(df['size'])
plt.show()

sns.histplot(df['total_bill'],kde=True)
plt.show()

plt.subplot(1,2,1)
sns.histplot(df['total_bill'],bins=20,kde=True)
plt.subplot(1,2,2)
sns.histplot(df['tip'],bins=20,kde=True)
plt.show()

# Joint Plot 
sns.jointplot(x='total_bill',y='tip',data=df,kind='scatter')
sns.jointplot(x='total_bill',y='tip',data=df,kind='kde')
sns.jointplot(x='total_bill',y='tip',data=df,kind='hex')
sns.jointplot(x='total_bill',y='tip',data=df,kind='reg')
plt.show()

#Pair Plot
sns.pairplot(df,hue='sex')
plt.show()
