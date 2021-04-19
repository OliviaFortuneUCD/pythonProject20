# Let's try to get a distribution of movies produced by country - Top 10
#load data
import pandas as pd
import numpy as np # linear algebra

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go


import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

df=pd.read_csv("netflix_titles.csv")

movies = df[df['type'] == 'Movie']

plt.figure(figsize=(12, 8))
ax2 = sns.countplot(x='country', data=movies, order=movies['country'].value_counts().head(10).index)
plt.title("Number of movies produced by each country")

for p in ax2.patches:
    ax2.text(p.get_x() + p.get_width() / 2., p.get_height(), '%d' % int(p.get_height()),
             fontsize=12, color='black', ha='center', va='bottom')

plt.show()