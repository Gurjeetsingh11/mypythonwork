#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
mydataset= {
    "car":["BMW","FORD","SUV"],
    "year":[2012,2013,2015]
}
myvar=pd.DataFrame(mydataset)
print(myvar)


#checking the version of pandas
print(pd.__version__)


# In[9]:


#series in pandas
import pandas as pd
arr=[1,7,2]
myvar=pd.Series(arr)
print(myvar)
print(myvar[0])


# In[15]:


#creating the label
import pandas as pd
a=[1,2,3]
myvar=pd.Series(a,["X","Y","Z"])
print(myvar)

#key-value object as series

calories={"day1":302,"day2":300,"day3":300}
myvar=pd.Series(calories)
print(myvar)

#dataframes : is whole table
#series : is the column of table 


# In[27]:


""" DATAFRAMES """

import pandas as pd

analysis={"calories": [420, 380, 390,343,232,341],
  "duration": [50, 40, 45,23,55,34]}
myvar=pd.DataFrame(analysis)
print(myvar)

#LOC- LOCATE ROW
print(myvar.loc[1])
print(myvar.loc[[0,3]])


#name the indexes using function index with dataframe
analysis={"calories": [420, 380, 390,343,232,341],
  "duration": [50, 40, 45,23,55,34]}
myvar=pd.DataFrame(analysis,index=["day1","day2","day3","day4","day5","day6"])
print(myvar)

#LOCATE ROW
print(myvar.loc["day4"])


# In[ ]:


#ANALYSING THE DATAFRAMES
import pandas as pd

df=pd.read_csv('data.csv')
print(df);
print(df.head(10))
print(df.tail());
print(df.info())


""" CLEANING THE DATA """
removing the row->dropna
replace empty cell with value ->fillna
return the duplication in boolean format ->duplicated()
remove the duplicated ->drop_duplicates()

"""CORRELATION OF DATA"""
calculate the relationship among the column in data -> corr()

"""PLOTTING"""
pandas use plot() function for plotting the diagram
plt.show() to sow the plotted diagram

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()


#histogram
df["Duration"].plot(kind = 'hist')

