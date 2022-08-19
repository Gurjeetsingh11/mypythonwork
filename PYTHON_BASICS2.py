#!/usr/bin/env python
# coding: utf-8

# In[54]:


"""LOOPS THROUGH LIST"""
#python for loop
list1=['apple', 'mango', 'BANANA', 'apple', 'mango', 'BANANA']
for i in list1:
    print(i)

#for loop using RANGE AND LEN
list1=['apple', 'mango', 'BANANA']
for i in range(len(list1)):
    print(list1[i])

#using while loop on lists
"""list1=['apple', 'mango', 'BANANA', 'apple', 'mango', 'BANANA']
i=0
while i<len(list1):
    print(list[i])
    i=i+1;"""

#using list comprehension
"""list1=['apple', 'mango', 'BANANA', 'apple', 'mango', 'BANANA']
(print(i) for i in list1)"""

#list comprehension
"""list1=['apple', 'BANANA', 'apple', 'mango', 'BANANA']
newlist=[]
for x in list1:
    if "" in x:
        newlist.append(x)
    print(newlist)"""

#list comprehension one liner
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "" in x]
print(newlist)

"""CONDITION"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x for x in fruits if x!="apple"]
print(newlist)

#with no if statement
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x for x in fruits]
print(newlist)

#USING range function
newlist=[x for x in range(10)]
print(newlist)

#range with conditions
newlist=[x for x in range(10) if x<5]
print(newlist)

#uppercase list 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x.upper() for x in fruits]
print(newlist)

#set all value as given in new list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=['hello' for x in fruits]
print(newlist)

#miscellaneous
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x if x!='banana' else 'orange' for x in fruits]
print(newlist)


# In[38]:


"""SORT LIST"""
list1=["apple","mango","grapes","jamun"]
list1.sort()
print(list1)

#numerical list sorting
numlist=[2,3,4,1,4,5]
numlist.sort()
print(numlist)

#sort descending
list1=["APPLE","mango","GRAPES","jamun"]
list1.sort(reverse=True)
print(list1)

#sort reverse
numlist=[2,3,4,1,4,5]
numlist.sort(reverse=True)
print(numlist)

#constumise your own sort
def mysort(n):
    return n-10
numlist=[2,3,4,1,4,5]
numlist.sort(key=mysort)
print(numlist)

#reverse order
list1=["APPLE","mango","GRAPES","jamun"]
list1.reverse()
print(list1)

"""COPY LIST"""
list1=["APPLE","mango","GRAPES","jamun"]
copylist=list1.copy()
print(copylist)

list1=["APPLE","mango","GRAPES","jamun"]
copylist=list(list1)
print(copylist)


""" JOIN TWO STRINGS """
list1=["APPLE","mango","GRAPES","jamun"]
list2=[1,2,3,4,5]
list3=list1+list2;
print(list3)

#using append

list1=["APPLE","mango","GRAPES","jamun"]
list2=[1,2,3,4,5]
list1.append(list2)
print(list1)

#using extend
list1=["APPLE","mango","GRAPES","jamun"]
list2=[1,2,3,4,5]
list1.extend(list2)
print(list1)


list1=["APPLE","mango","GRAPES","jamun"]
list2=[1,2,3,4,5]
#list1.insert(2,"hello");
#list1.pop()
#list1.clear()
#list1.remove("APPLE")
#list1.count(list1)
print(list1)


# In[ ]:





# In[ ]:




