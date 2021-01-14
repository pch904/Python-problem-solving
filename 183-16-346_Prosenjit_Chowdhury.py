#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# get_ipython().run_line_magic('matplotlib', 'inline')

# In[3]:


dtframe = pd.read_csv("CONVENIENT_global_confirmed_cases.csv")
dtframe
dtframe = dtframe.iloc[1:]
dtframe

# In[5]:


df = dtframe[['Australia', 'Canada', 'China', 'Denmark', 'France',
              'Netherlands', 'United Kingdom']]
df.head(10)

# In[6]:


dtframe['confirmed_globally'] = dtframe.sum(axis=1)

# In[7]:


dtframe.confirmed_globally

# In[8]:


confirmedvictims = dtframe['confirmed_globally'].sum()
confirmedvictims

# In[9]:


epidemics = pd.DataFrame({
    'epidemic': ['SARS', 'EBOLA', 'MERS', 'H1N1'],
    'start_year': [2003, 2004, 2012, 2009],
    'end_year': [2004, 2006, 2017, 2010],
    'confirmed': [8096, 28646, 2494, 6724149],
    'deaths': [774, 11323, 858, 19654]

})

# In[10]:


epidemics

# In[12]:


Covid19 = {'epidemic': 'COVID-19', 'start_year': 2019, 'end_year': 2020, 'confirmed': confirmedvictims,
           'deaths': 1388051}
epidemics = epidemics.append(Covid19, ignore_index=True)

# In[13]:


epidemics

# In[14]:


epidemics['Mortlity'] = epidemics['confirmed'] / epidemics['deaths'] * 100

# In[15]:


epidemics

# In[16]:


fig = plt.figure(figsize=(8, 3))
ax = fig.add_axes([0, 1, 1, 1])
ax.bar(epidemics.epidemic, epidemics.Mortlity)

# In[ ]:




