#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
#hamilton vs verstappen
#hamilton vs vettel in 2017 and 2018
#senna vs prost in 1989
#teammate battles in each race
#which constructor has had the most dnfs


# In[2]:


circuits_df = pd.read_csv("circuits.csv")


# In[3]:


circuits_df.head()


# In[8]:


circuits_df_sorted = circuits_df.sort_values('alt')
circuits_df_sorted.tail()


# In[34]:



circuits_df_sorted.plot(kind="bar",x="name",y="alt",figsize=(20,12),xlim=(-10,2500))


# In[92]:


constructors = pd.read_csv("constructors.csv")
results = pd.read_csv("results.csv")
status = pd.read_csv("status.csv")
races = pd.read_csv("races.csv")
lap_times = pd.read_csv("lap_times.csv")
races[races['year']==2021]


# In[142]:


def convert_time(x):
    return x/1000


# In[154]:


races_2021 = races[races['year']==2021]
joined_df = lap_times.join(races_2021.set_index('raceId'),how="left",on="raceId",lsuffix='lap')
hamver_times = joined_df[(joined_df['raceId']==1055) & ((joined_df['driverId'] == 1) | (joined_df['driverId']==822)) ]
hamver_times.head()
hamver_times['milliseconds'].apply(convert_time)
hamtimes = hamver_times[hamver_times['driverId']==1]
vertimes = hamver_times[hamver_times['driverId']==822]


# In[157]:


fig,ax = plt.subplots(figsize=(20,10),dpi=300)
ax.plot(hamtimes['lap'],hamtimes['milliseconds'].apply(convert_time),ls='--',label="HAM")
ax.plot(vertimes['lap'],vertimes['milliseconds'].apply(convert_time),label="BOT")
ax.legend()
ax.set_xlabel('Lap')
ax.set_ylabel('Time')
#hamver_times.plot(kind="line",x="lap",y="milliseconds")


# In[ ]:




