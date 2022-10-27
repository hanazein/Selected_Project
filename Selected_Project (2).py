#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


dataframe=pd.read_csv("D:\\downloads\\archive (15).zip")
dataframe=dataframe.drop('id', axis=1)


# In[3]:


dataframe


# In[4]:


dataframe.describe()


# In[5]:


dataframe.isna().sum()


# In[6]:


dataframe.skew()


# In[7]:


dataframe.bmi.fillna(dataframe.bmi.mean(), inplace=True)
dataframe.isna().sum()


# In[8]:


dataframe["gender"].value_counts()
dataframe.drop(dataframe[dataframe['gender'] == 'Other'].index, inplace = True)
dataframe["gender"].value_counts()


# In[9]:


sns.heatmap(dataframe.corr())


# In[10]:


from pandas.api.types import is_string_dtype, is_numeric_dtype
for column in dataframe:
    plt.figure(column, figsize = (4.9,4.9))
    plt.title(column)
    if is_numeric_dtype(dataframe[column]):
        dataframe[column].plot(kind = 'hist')
    elif is_string_dtype(dataframe[column]):
        dataframe[column].value_counts()[:10].plot(kind = 'bar')


# In[11]:


num_list = []
cat_list = []

for column in dataframe:
 if is_numeric_dtype(dataframe[column]):
        num_list.append(column)
 elif is_string_dtype(dataframe[column]):
        cat_list.append(column)    

print('Numerical columns', num_list)
print('Categorical columns', cat_list)


# In[12]:


sns.pairplot(dataframe,height = 2.5, hue='stroke')


# In[13]:


df=dataframe


# In[14]:


for i in range(0, len(cat_list)):
    primary_cat = cat_list[i]
    for j in range(0, len(cat_list)):
        secondary_cat = cat_list[j]
        if secondary_cat != primary_cat:
            plt.figure (figsize = (5,5))
            chart = sns.countplot(
                data = df,
                x= primary_cat, 
                hue= secondary_cat,
                palette = 'Set2',
                order=df[primary_cat].value_counts().iloc[:10].index #show only TOP10
              )


# In[15]:


df_dummy = pd.get_dummies(df, columns=['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'])
df_dummy


# In[16]:


X = df_dummy.drop(['stroke'], axis=1)
y= df_dummy['stroke']
X.shape
y.shape



# In[ ]:





# In[ ]:




