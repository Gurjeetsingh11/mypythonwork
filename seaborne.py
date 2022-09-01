#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[4]:


#total bill vs tip dataset thorgh dataset present on seaborn
tips=sns.load_dataset('tips')
tips.head()


# In[11]:


#set theme in sns
sns.set_theme()


# In[8]:


sns.relplot(data=tips,x='total_bill',y='tip',col='time',hue='smoker',style='smoker',size='size')


# In[12]:


iris=sns.load_dataset('iris')


# In[13]:


iris.head()


# In[19]:


#scatter plot int the iris dataset using seaborn library

sns.scatterplot(data=iris,x='sepal_length',y='sepal_width',hue='species')


# In[21]:


sns.scatterplot(data=iris,x='sepal_width',y='petal_width',hue='species')


# ##LOADING TITANIC DATASET

# In[22]:


titanic=sns.load_dataset('titanic')


# In[23]:


titanic.head(10)


# In[28]:


titanic.shape

#count plot 
# In[26]:


sns.countplot(x='embarked',data=titanic)


# In[29]:


sns.countplot(x='survived',data=titanic)

# BARCHART
# In[31]:


sns.barplot(data=titanic,x='sex',y='survived',hue='class')


# In[39]:


#house price dataset using sklearn library
from sklearn.datasets import load_boston
house_boston=load_boston()
house=pd.DataFrame(house_boston.data,columns=house_boston.feature_names)
house['PRICE']=house_boston.target


# In[41]:


#numpy format
print(house)


# In[40]:


house.head(10)

#DISTRIBUTION PLOT
# In[43]:


sns.distplot(house['PRICE'])


# In[44]:


correlation=house.corr()


# In[54]:


plt.figure(figsize=(10,10))
sns.heatmap(correlation,cbar=True,square=True,fmt='.1f',annot_kws={'size':8},cmap="Blues")


# In[ ]:




