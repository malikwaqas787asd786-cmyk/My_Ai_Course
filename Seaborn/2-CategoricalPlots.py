# Categorical Plots

# Importing Libraries 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

# Importing Dataset
df=sns.load_dataset("tips")
print(df)
  
# Countplot
sns.countplot(df['sex'])
plt.show()
sns.countplot(x=df['sex'])
plt.show()
sns.countplot(x=df['sex'],hue=df['smoker'])
plt.show()

# Barplot
sns.barplot(x=df['sex'],y=df['total_bill'])
plt.show()
sns.barplot(x=df['sex'],y=df['tip'],estimator=np.sum)
plt.show()

# Boxplot 
sns.boxplot(x='day',y='total_bill',data=df)
plt.show()
sns.boxplot(x='day',y='total_bill',data=df,palette='rainbow')
plt.show()

# Violinplot
sns.violinplot(x='day',y='total_bill',data=df)
plt.show()

# Stripplot 
sns.stripplot(x='day',y='total_bill',data=df)
plt.show()

# Swarmplot
sns.swarmplot(x='day',y='total_bill',data=df)
plt.show()

# Violinplot and Swarmplot
sns.swarmplot(x='day',y='total_bill',data=df)
sns.violinplot(x='day',y='total_bill',data=df)
plt.show()
