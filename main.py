#load data
import pandas as pd
import numpy as np # linear algebra

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

df=pd.read_csv("netflix_titles.csv")
#print first five records from CSV
#df.head()
#print(df.head())
#print info
#df.info()
#check if there are missing values
#print(df.isna().sum())

#Calculating Null Rate for better understanding and decision making

#Calculating Null Rate for better understanding and decision making

#for i in df.columns:
#    null_rate = (df[i].isna().sum()/len(df))*100
#    if null_rate > 0:
#        print("{}'s null rate is {}%".format(i, round(null_rate,2)))

# We fill up NAs in the 'Country' column with the most frequently occuring Country in the data
#print(df['country'].value_counts().to_frame())

#df['country'] = df['country'].fillna(df['country'].mode()[0])

#print(df['country'].isna().sum())

#print(df['date_added'].value_counts().to_frame())

#df['date_added']= df['date_added'].fillna(df['date_added'].mode()[0])
#print(df['date_added'].isna().sum())
#print rating is null
#print(df['rating'].value_counts().to_frame())

#df = df.drop(['director', 'cast'], axis=1)
#df.info()


df.Date = pd.datetime.now().date()

print(df.info())

plt.figure(figsize=(8, 6))

ax = sns.countplot(x='type', data=df, order=df['type'].value_counts().index)
plt.title("Comparision of # TV Shows and Movies")

for p in ax.patches:
    ax.text(p.get_x() + p.get_width() / 2., p.get_height(), '%d' % int(p.get_height()),
            fontsize=12, color='black', ha='center', va='bottom')

plt.show()






