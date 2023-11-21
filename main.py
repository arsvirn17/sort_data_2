import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('howpop_train.csv')

df.head(6).T

df.drop(filter(lambda c: c.endswith('_lognorm'), df.columns), axis=1, inplace=True)

df["published"] = pd.to_datetime(df.published, yearfirst=True)

df['year'] = [d.year for d in df.published]
df['month'] = [d.month for d in df.published]
df['day'] = [d.day for d in df.published]
df['dayofweek'] = [d.isoweekday() for d in df.published]
df['hour'] = [d.hour for d in df.published]

df.groupby(['year', 'month'])[['title']].count().sort_values('title', ascending=False).head()

df_march = df[(df['year'] == 2015) & (df['month'] == 3)]
df_march.groupby('day')[['title']].count().plot()

df_march.pivot_table(index='day', values='title', aggfunc='count', columns='domain').plot()

df_march[df_march['dayofweek'] == 6].pivot_table(index='day', values='title', aggfunc='count', columns='domain')

df.groupby('hour')[['views']].mean().sort_values('views', ascending=False).head()

df.groupby('hour')[['comments']].count().sort_values('comments', ascending=False).head()

df[df['domain'] == 'geektimes.ru'].sort_values('comments', ascending=False).head(1)

df[df['domain'] == 'habrahabr.ru'].groupby('hour')[['comments']].mean().plot()

df[df.author.isin(['@Mordatyj', '@Mithgol', '@alizar', '@ilya42'])].groupby('author')\
[['votes_minus']].mean().sort_values('votes_minus', ascending=False)

df[df['dayofweek'] == 1].groupby('hour')[['title']].count().sort_values('title', ascending=False).head()

df[df['dayofweek'] == 6].groupby('hour')[['title']].count().sort_values('title', ascending=False).head()