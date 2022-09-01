#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


import numpy as np


# In[5]:


x=np.linspace(0,10,100)
y=np.sin(x)
z=np.cos(x)


# In[7]:


print(x)


# In[8]:


print(y)


# In[9]:


print(z)


# ### plot a data
# 

# In[11]:


plt.plot(x,y)
plt.show()


# In[12]:


plt.plot(y,z)
plt.show()


# In[13]:


plt.plot(x,z)
plt.show()


# In[4]:


import matplotlib.pyplot as plt
import numpy as np;
x=np.linspace(0,10,100)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y);
plt.xlabel("angle")
plt.ylabel("value")
plt.title("sine wave")
plt.show()


# In[11]:


#parabola
x=np.linspace(-10,10,20)
y=x**2
#parabola curve in red color - 'r'
#plt.plot(x,y,'r')
plt.plot(x,y,'g.')
plt.show()


# In[19]:


x=np.linspace(-5,5,50)
plt.plot(x,np.sin(x),'g-')
plt.plot(y,np.cos(x),'r--')
plt.show()


# In[21]:


#BAR PLOT
fig=plt.figure();
ax=fig.add_axes([0,0,1,1])
language=["english","spanish","judy","french","hindi"]
people=[100,200,121,32,47]
ax.bar(language,people)
plt.xlabel("no. of people")
plt.ylabel("language speaking")
plt.show()


# In[28]:


#PIE CHART
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
language=["english","spanish","judy","french","hindi"]
people=[100,200,121,32,47]
ax.pie(people,labels=language,autopct="%1.1f%%")
plt.show()


# In[33]:


x=np.linspace(0,10,50)
y=np.sin(x)
z=np.cos(x)
fig2=plt.figure()
ax=fig2.add_axes([0,0,1,1])
ax.scatter(x,y,color='r')
ax.scatter(x,z,color='y')
plt.show()


# In[37]:


#3d scatter plot

fig3=plt.figure()
ax=plt.axes(projection='3d')
z=20*np.random.random(100)
x=np.sin(z)
y=np.cos(z)
ax.scatter(x,y,z,c=z,cmap='Blues')
plt.show()


# In[ ]:




