#!/usr/bin/env python
# coding: utf-8

# In[20]:


#creating the function
def myfun():
    print("hello world")
myfun()


#PASSING PARAMETER IN FUNCTIONS
def myname(fname):
    print(fname+"singh")
myname("gurjeet ")
myname("surjeet ")

#PASSING MANY ARGUMENT
def myname(fname,lname):
    print(fname+" "+lname)
myname("manjeet","singh")

#PASSING * AS AN ARGUMENT
def myname(*fname):
    print("name is "+fname[1])
myname("ram","shyaam","dham")

#KEYWORD ARGUMENT
def func(n1,n2,n3):
    print("second name is "+n2)
func(n1="aram",n2="viram",n3="siram")

#DEFAULT PARAMETER VALUE
def func(country="india"):
    print(country)
func("brazil")
func()
func("germany")

#PASSING LIST AS AN ARGUMENT
def func(food):
    for x in food :
         print(x)
list1=["apple","banana","grapes"]
func(list1)

#return values
def func(x):
    return x*10
#func(10)
func(5)

#pass statement :function is empty no content in it put pass to avoid error
def myfunc():
    pass;


# In[9]:


"""LAMBDA FUNCTIONS"""
x=lambda a:a+5
print(x(10))

#pass many argument
x=lambda a,b:(a+b)*2
print(x(3,4))

#3 argument
x=lambda a,b,c:(a+b+c)
print(x(10,20,30))

#lambda function defined in function
def myfun(n):
    return lambda a:a*n;
x=myfun(10)
print(x(4))

#one more example
def myfun(n):
    return lambda a:a*n
x=myfun(10)
y=myfun(20)
print(x(5))
print(y(10))


# In[ ]:




