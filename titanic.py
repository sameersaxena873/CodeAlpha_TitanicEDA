import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Titanic-Dataset.csv")
sns.countplot(x="Survived",data=df)
plt.title("Kitne log survive hue vs nahi")
plt.xlabel("Survived(0=No,1=Yes)")
plt.ylabel("count")
plt.show()
sns.countplot(x="Sex",hue="Survived",data=df)
plt.title("Gender ke hisab se Survival")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.describe())