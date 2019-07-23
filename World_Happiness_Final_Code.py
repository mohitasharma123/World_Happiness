#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as plt
import folium as fl
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


# In[2]:


data = pd.read_csv("C:\Users\Kunal\Desktop\mohita\Kaggle Project\world-happiness-report-2019.csv")
#data


# In[3]:


#Calculating number of missing values
data.isnull().sum()


# In[4]:


##Data Cleaning and renaming
data.fillna(0)
df = pd.DataFrame(data)
df
df.columns=['Country','Life Satisfaction','Std of Ladder','Positive affect','Negative affect','Social support','Freedom','Corruption','Generosity','Log of GDP per capita','Healthy life expectancy']
df.head()


# In[20]:


positive_affect = df.groupby(['Country','Positive affect']).sum()
positive_affect = positive_affect.sort_values(by='Positive affect',ascending= True).reset_index()
positive_affect = positive_affect.head(10)
positive_affect
#sns.barplot(x='Country', y= 'Positive affect', data= positive_affect)


# In[7]:


negative_affect = df.groupby(['Country','Negative affect']).sum()
negative_affect = negative_affect.sort_values(by='Negative affect',ascending= True).reset_index()
negative_affect = negative_affect.tail(5)
negative_affect
sns.barplot(x='Country', y= 'Negative affect', data= negative_affect)


# In[106]:


cor = df.corr(method='kendall')
#cor
ht_mp= sns.heatmap(data=cor,cmap= "Blues", annot = True, linewidths= 0.3)


# In[41]:


data_diagram = dict(type = 'choropleth', 
           locations = df['Country'],
           locationmode = 'country names',
           z = df['Life Satisfaction'], 
           text = df['Country'],
           colorbar = {'title':'Ladder'},
           colorscale = "Blues")
layout = dict(title = 'Life satisfaction ladder 2019', geo = dict(showframe = False,projection = {'type': 'mercator'}))
choromap = go.Figure(data = [data_diagram], layout=layout)
iplot(choromap)


# In[ ]:




