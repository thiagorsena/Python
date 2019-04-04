import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

# Grafico tips do seaborn

# Le o arquivo e exibe as informações - arquivo tips ja vem na library
tips = sns.load_dataset("tips")
tips.info()
sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')
sns.pairplot(tips,hue='smoker',palette='coolwarm')
plt.show()


# Projeto 911

# Le o arquivo csv e exibe as informações
df = pd.read_csv("911.csv")
df.info()

# Conta quantos zipcode e cep existem
zipCount = df['zip'].value_counts()
twpCount = df['twp'].value_counts()
# print(zipCount.head(5))
# print(twpCount.head(5))

# Define o title unico de cada chamada
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
print(df['Reason'].value_counts())

# Plota o grafico por razao da chamada
sns.countplot(x='Reason', data=df, palette='viridis')
plt.show()

# Converte e define a hora, mes e dia
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day of Week'] = df['timeStamp'].apply(lambda x: x.dayofweek)

dmap = {0: 'Mon' ,1: 'Tue' ,2: 'Wed' ,3: 'Thu' ,4: 'Fri' ,5: 'Sat' ,6: 'Sun'}

df['Day of Week'] = df['Day of Week'].map(dmap)
print(df['Day of Week'].unique())

# Plota o grafico razao da chamada em cada dia da semana
sns.countplot(x='Day of Week', data=df, hue='Reason', palette='viridis')
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0)
plt.show()

# Conta quntas instancias tiveram cada clss
byMonth = df.groupby('Month').count()
byMonth['twp'].plot()
plt.show()

# Resta o index mes para que seja gerado o grafico linear
byMonth.reset_index()
sns.lmplot(x='Month', y='twp', data=byMonth.reset_index())
plt.show()
