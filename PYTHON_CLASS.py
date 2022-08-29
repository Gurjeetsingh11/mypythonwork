#!/usr/bin/env python
# coding: utf-8

# In[24]:


""" CREATING CLASS AND OBJECT"""
"""class myclass:
    x=10;
obj=myclass()
print(obj.x)
"""

#using init function with class

"""class myclass:
    def __init__(self,age,name):
        self.name=name;
        self.age=age;
obj=myclass(12,"abc");
print(obj.age)
print(obj.name)
"""
#function in class 
""" class myclass:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def func(self):
        print("hello "+self.name+"your age is: ",self.age)
obj=myclass("gurjeet",12)
obj.func()   """

#delte object 
class myclass:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def func(self):
        print("hello "+self.name+"your age is: ",self.age)
obj=myclass("gurjeet",12)
obj.func() 
del obj


# In[38]:


""" INHERITANCE """
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

"""class children(Person):
    def __init__(self,age,names):
        self.age=age;
        self.names=names;
    def call(self):
        print("name is :"+names,age)

obj=children(12,"aha")
obj.call();"""


# In[43]:


global x
def myfun():
    x=200
    print(x);
myfun()
print(x)


# In[ ]:




