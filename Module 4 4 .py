#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[2]:



get_ipython().run_line_magic('sql', 'ibm_db_sa://rgq70481:fn35jzq003j%400wbs@dashdb-txn-sbox-yp-lon02-07.services.eu-gb.bluemix.net:50000/BLUDB')


# In[ ]:


import pandas
chicago_socioeconomic_data = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
get_ipython().run_line_magic('sql', 'PERSIST chicago_socioeconomic_data')


# In[4]:


get_ipython().run_line_magic('sql', 'SELECT * FROM chicago_socioeconomic_data limit 5;')


# In[5]:


get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM chicago_socioeconomic_data;')


# In[6]:


get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0;')


# In[7]:


get_ipython().run_line_magic('sql', 'SELECT MAX(hardship_index) from chicago_socioeconomic_data;')


# In[10]:


get_ipython().run_line_magic('sql', 'SELECT community_area_name from chicago_socioeconomic_data WHERE hardship_index= 98.0;')


# In[11]:


get_ipython().run_line_magic('sql', 'SELECT community_area_name from chicago_socioeconomic_data WHERE per_capita_income > 60000;')


# In[12]:


get_ipython().run_line_magic('sql', 'SELECT community_area_name from chicago_socioeconomic_data WHERE per_capita_income > 60.000;')


# In[13]:


get_ipython().run_line_magic('sql', 'SELECT community_area_name from chicago_socioeconomic_data WHERE per_capita_income_ > 60.000;')


# In[14]:


get_ipython().run_line_magic('sql', 'SELECT community_area_name from chicago_socioeconomic_data WHERE per_capita_income_ > 60000;')


# In[15]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

income_vs_hardship = get_ipython().run_line_magic('sql', 'SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;')
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())


# In[16]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

income_vs_poverty = get_ipython().run_line_magic('sql', 'SELECT per_capita_income_, percent_households_below_poverty FROM chicago_socioeconomic_data;')
plot = sns.jointplot(x='per_capita_income_',y='percent_households_below_poverty', data=income_vs_poverty.DataFrame())


# In[ ]:




