#load data
import pandas as pd
import numpy as np # linear algebra

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go


df=pd.read_csv("netflix_titles.csv")
movies = df[df['type']== 'Movie']


# Movies by Genre

plt.figure(figsize=(16, 8))
ax5 = sns.countplot(x='listed_in', data=movies, order=movies['listed_in'].value_counts().head(10).index)
plt.title("Number of movies by genre")
plt.xticks(rotation=45)

for p in ax5.patches:
    ax5.text(p.get_x() + p.get_width() / 2., p.get_height(), '%d' % int(p.get_height()),
             fontsize=12, color='black', ha='center', va='bottom')

plt.show()