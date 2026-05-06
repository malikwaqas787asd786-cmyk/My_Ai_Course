# Regression Plots 

# Importing Libraries
import seaborn as sns
import matplotlib.pyplot as plt 

# Loading Dataset
tips = sns.load_dataset("tips")
print(tips)

# Regresion Plot
sns.lmplot(x = 'total_bill',y = 'tip',data = tips)
plt.show()

sns.lmplot(x = 'total_bill',y = 'tip',data = tips,hue = 'sex')
plt.show()
   
sns.lmplot(x = 'total_bill',y = 'tip',data = tips,hue = 'sex',palette='coolwarm')
plt.show()

sns.lmplot(x = 'total_bill',y = 'tip',data = tips,hue = 'sex',palette='coolwarm',markers=['o','v'],
           scatter_kws={'s':50})
plt.show()