#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install -r requirements.txt')


# In[5]:


import pandas as pd


# In[6]:


def DRI(age, sex):
    bmin = pd.read_csv('./diet_minimums.csv').set_index('Nutrition').iloc[:,2:]
    bmax = pd.read_csv('./diet_maximums.csv').set_index('Nutrition').iloc[:,2:]
    combined_df = pd.concat([bmin,-bmax])
    if sex == "Male":
        if age <=3:
            return combined_df.loc[:, 'C 1-3']
        if age>=4 and age<=8:
            return combined_df.loc[:, 'M 4-8']
        if age>=9 and age<=13:
            return combined_df.loc[:, 'M 9-13']
        if age>= 14 and age<=18:
            return combined_df.loc[:,'M 14-18']
        if age>=19 and age <= 30: 
            return combined_df.loc[:, 'M 19-30']
        if age>=31 and age<=50:
            return combined_df.loc[:, 'M 31-50']
        if age>=51:
            return combined_df.loc[:, 'M 51+']
    if sex == "Female":
        if age <=3:
            return combined_df.loc[:, 'C 1-3']
        if age>=4 and age<=8:
            return combined_df.loc[:, 'F 4-8']
        if age>=9 and age<=13:
            return combined_df.loc[:, 'F 9-13']
        if age>= 14 and age<=18:
            return combined_df.loc[:,'F 14-18']
        if age>=19 and age <= 30: 
            return combined_df.loc[:, 'F 19-30']
        if age>=31 and age<=50:
            return combined_df.loc[:, 'F 31-50']
        if age>=51:
            return combined_df.loc[:, 'F 51+']
DRI(25, 'Male')


# In[ ]:




