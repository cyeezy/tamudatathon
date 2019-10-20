
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\chris\Downloads\equip_failures_training_set.csv\equip_failures_training_set.csv")
df = pd.DataFrame(df)


# In[2]:


for (columnName,columnData) in df.iteritems():
   df[columnName] = pd.to_numeric(df[columnName], errors='coerce')
   


# In[3]:


df=df.fillna(df.mean())


# In[4]:


type(df.sensor2_measure[2])


# In[5]:


df.sensor2_measure[2]


# In[6]:


df.sensor2_measure.mean()


# In[ ]:


df

