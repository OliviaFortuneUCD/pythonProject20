#load data
import pandas as pd


df=pd.read_csv("netflix_titles.csv")

df = df.append (['Test', 'Test1'])
df.info()

print(df.values)