#!/usr/bin/env python
# coding: utf-8

# In[10]:


""" PYTHON BASICS """
#print("hii")
a=1
b="gurjeet"
print(a);
print(b);


# In[20]:


"""TYPE CasTING"""
a=2
b=4.5
x=str(a)
y=int(b)
print(x,y)
print(type(x),type(y),type(a),type(b))

a="abc"
b='abc'
print(a,b)


# In[34]:


"""VARIABLE EXAMPLES"""
myVariable="gurjeet"
MyVariable="gurjeet"
my_variable="gurjeet"

#assign multiple value to multiple variable
a,b,c="hii","hello","holla";
print(a,b,c)

#assign single value to multiple variable
a=b=c="hii there"
print(a,b,c)

#unpacking the collection
fruits=["apple","oranges","grapes"]
a,b,c=fruits

print("this is variable a value :",a)
print(a,b,c)

a=23
b="gurjeet"
# error :  print(a+b) string and integer canot be concatenated instead , is used
print(a,b)

#GLOBAL VARIABLE
#defined inside the function
x="awesome"
def myfunc():
    print(x,"global variable locally defined")
myfunc()

#defined outside the function
x="awesome"
def func():
    print(x,"locally defined inside function");
func()
print(x,"globally defined outside function")

# variable defining using global variable
def func():
    global x
    x="global"
    print(x,"-global but defined inside function ")
func()
print(x,"also used after the calling function as well")


# In[43]:


""" DATATYPE IN PYTHON """
a=1;
b=-238928392
c=21211212
print(type(a),type(b),type(c))

a=-21.3222121
b=2.2
print(type(a),type(b))

a="gurjeet"
print(type(a))

a=[1,2,3]
print(type(a))

a=(1,2,3)
print(type(a))


# In[1]:


#strings in python
a="hii we are working on python strings"
print(a);
print(type(a))

#printing multiple lines
b="""this is a multiple line paragraph so we are using triple quotation marks """
print(b)

#toget length of strings
print(len(a),len(b))

#array with strings
a="hello world we are using python"
print(a[1]);

#looping through strings
for i in "gur":
    print(i)

#check sentence present or not
a="hello world we are using python"
print("hello" in a)

#using if statement with strings
st="hello world we are using python"
if "gurjeet" in st:
    print("this is python")

a="hello world we are using python"
print("gurjeet" not in a)


# In[24]:


"""STRING SLICING"""
b="HELLO WORLD"
#indexing 
print(b[1:5])

#indexing from start
print(b[:5])

#indexing to end
print(b[6:])

#negative indexing
print(b[-5:-3])

"""MODIFY STRINGS"""

a="hello WORLD"

#upper case 
print(a.upper())

#lower case 
print(a.lower())

#remove whitespace
print(a.strip())

#replace string
print(a.replace('h','s'))

#split string
print(a.split("ello"))

"""STRING CONCATENATION"""
a="hello"
b=" world"
print(a+b)

"""FORMAT STRINGS"""
a=12
b=56
c=45000
word="i want {} items having item number {} for {} rs";
print(word.format(a,b,c))


# In[43]:


"""BOOLEAN VALUES"""
print(10>9)
print(10==9)
print(9>10)
a=10
b=30
if(a>b):
    print("a is greater")
print("b is greater")
print(bool("HELLO"))
print(bool(10))
print(bool(["jii","gjgj","ejej"]))
print(bool(None))
print(bool(0))
print(bool({}))
print(bool([]))

class myclass():
    def __len__(self):
        return 0;
myobj=myclass()
print(bool(myobj))

def myfun():
    return False
print(myfun())

#check if instance or not
x=20
print(x,int)


# In[68]:


"""LISTS"""
mylist=["apple","grapes","oranges"]
print(mylist)

#allow duplicates
mylist=["apple","grapes","oranges","apple","oranges"]
print(mylist)

#length of list
mylist=["apple","grapes","oranges","apple","oranges"]
print(len(mylist))

#list constructor
mylist=list(["apple","oranges","grapes"])
print(mylist)

#accessing elements of list
list1=["apple","grapes","oranges","banana","guava","watermelon","mellon"]
print(list1[4])

#negative indexes
print(list1[-1])

#range of index
print(list1[2:5])

#range of negative index
print(list1[-5:-2])

#check if element exist or not
if "sajna" in list1:
    print("yes it exist")
else:
    print("sorry wrong choice")
    
#change list items
mylist=["apple","grapes","oranges","apple","oranges"]
mylist[1]="mango"
print(mylist)

#change range of item
mylist=["apple","grapes","oranges","apple","oranges"]
mylist[1:4]=["black","green"]
print(mylist)

#change second and third value by replacing it with one values
mylist=["apple","grapes","oranges","apple","oranges"]
mylist[1:3]=["watermellon"]
print(mylist)

#insert item without replacing the current elements
mylist=["apple","grapes","oranges","apple","oranges"]
mylist.insert(2,"mango")
print(mylist)


#APPEND
list1=["apple","mango","BANANA"]
list1.append("guava")
print(list1)

#EXTENDS
list1=["apple","mango","BANANA"]
list2=["guava","grapes","melon"]
list1.extend(list1)
print(list1)

#EXTEND WITH TUPLE
list1=["apple","mango","BANANA"]
list2=("guava","grapes","melon")
list1.extend(list2)
print(list1)

#REMOVE FROM LIST
list1=['apple', 'mango', 'BANANA', 'guava', 'grapes', 'melon']
list1.remove('apple')
print(list1)

#REMOVE FROM INDEX
list1=['apple', 'mango', 'BANANA', 'guava', 'grapes', 'melon']
list1.pop(4)
print(list1)

#DELETE KEY WORD IS USED FOR INDEX DELETION AS WELL
list1=['apple', 'mango', 'BANANA', 'guava', 'grapes', 'melon']
del list1[2]
print(list1)

#DELETE WHOLE LIST
list2=("guava","grapes","melon")
del list2
#print(list2)

#CLEAR THE LIST
list1=['apple', 'mango', 'BANANA', 'guava', 'grapes', 'melon']
list1.clear()
print(list1)





