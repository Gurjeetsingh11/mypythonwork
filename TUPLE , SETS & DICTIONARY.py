#!/usr/bin/env python
# coding: utf-8

# In[36]:


"""TUPLE"""
tuple1=("A","B","c")
print(tuple1)

#accessing tuple item
tuple1=("A","B","c")
print(tuple1[1])

#length of tuple
tuple1=("A","B","C","A","D")
print(len(tuple1))

#tuple type
tuple1=("A","B","C","A","D")
print(type(tuple1))

#tuple item - data type
tuple1=("apple","banana","grapes")
tuple2=(1,2,3,4)
tuple3=(True,False,True)

#constructor in tuple
tuple1=tuple(("Apple","banana","grapes"))
print(tuple1)

#indexing tuple
tuple1=("A","B","C","A","D")
print(tuple1[1:4])

#negative indexing
tuple1=("A","B","C","A","D")
print(tuple1[-1])

#negative range indexing
tuple1=("A","B","C","A","D")
print(tuple1[-4:-1])

#check if item exist or not
tuple1=("A","B","C","A","D")
if 'P' in tuple1:
    print("yes it is present")
else:
    print("not it is not present")
    
"""CHANGE TUPLE VALUES"""
tuple1=("A","B","C","A","D")
list1=list(tuple1)
list1[1]="X"
tuple1=tuple(list1)
print(tuple1)

#remove item in tuple first by coverting tupple to list then list to tuple
tuple1=("A","B","C","A","D")
list1=list(tuple1)
list1.remove("A")
tuple1=tuple(list1)
print(tuple1)

#delete tuple completely
tuple1=("A","B","C","A","D")
#del tuple1
print(tuple1)

"""UNPACK TUPLE"""
tuple1=("A","B","C","A","D")
(A,B,C,A,D)=tuple1
print(A)
print(B)


"""LOOP THROUGH TUPLE"""
tuple1=("A","B","C","A","D")
for i in tuple1:
    print(i)
    
#Loop through the index number    
tuple1=("C","A","D")
for i in range(len(tuple1)):
    print(tuple1[i])
    
#while loop with tuple
tuple1=("X","Y","Z","P")
i=0;
while(i<len(tuple1)):
    print(tuple1[i]);
    i=i+1
    
#join two tuple
tuple1=("A","B","C","A","D")
tuple2=(1,2,3,4)
tuple3=tuple1+tuple2
print(tuple3)

#multiply 2 tuple
tuple1=("A","B","C","A","D")
tuple2=tuple1*2;
print(tuple2)


# In[53]:


"""SET"""
set1={1,1,2,3}
print(set1)

#getlength
set1={1,2,3,4,5}
print(len(set1))

#set item in set
set1={"A","B","C","D"}
set2={1,2,3,4}
set3={True,False,True}

#type of set
print(type(set1))

#python Access item
set1={1,2,3,4}
for s in set1:
    print(s)

"""with strings"""
set1={"apple","banana","grapes"}
print("banana" in set1)

#add item
set1={1,2,3,4,5}
set1.add(7)
print(set1)

#add sets
set1={1,2,3,4}
set2={4,5,6,7}
set1.update(set2)
print(set1)

#remove element from set
set1={1,2,3,4}
set1.remove(3)
print(set1)

set1={1,2,3,4}
set1.discard(3)
print(set1)

#popping last item
set1={1,2,3,4}
set1.pop()
print(set1)

#clear set
set1={1,2,3,4,5}
set1.clear()
print(set1)

seet1={1,2,3,4}
#del seet1
print(seet1)

#loop sets
list1={1,2,3,4}
for x in list1:
    print(x)
    
#join set
set1={1,2,3,4}
set2={"A","B","C"}
set3=set1.union(set2)
print(set3)

set1={1,2,3,4}
set2={"A","B","C"}
set1.update(set2)
print(set1)


# In[2]:


"""DICTIONARY"""
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
print(dict1)

#access dictionary
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
print(dict1["name"])
print(dict1["age"])

#duplication are not allowed
dict1={"name":"gurjeet",
      "age":19,
      "year":2001,
      "name":"sunil"}
print(dict1)

#length of dictionary
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
print(len(dict1))

#also include list in it
dict1={"name":"gurjeet",
      "age":19,
      "year":2001,
      "mylist":["volleball","football","chess"]}
print(dict1)

#typeof 
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
print(type(dict1))

#access the dictionary item
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
print(dict1["name"])

#also get() method
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
print(dict1.get("age"))

#check if value exists or not
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
if "name" in dict1:
    print("yes it exists")
    print(dict1["name"])
else:
    print("no it does not exist")
    
#change values in the dictionary
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
dict1["age"]=20
print(dict1)

#update the dictionary
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
#dict1.update["year"]=2000
dict1.update({"year":2000})
print(dict1)

#ADD item in dictionary
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
#dict1["hobby"]="singing";
dict1.update({"hobby":"singing"})
print(dict1)

#poppig the dictionary values
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
dict1.pop("age")
print(dict1)

#randomly delete the item
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
dict1.popitem()
print(dict1)

#with del keyword
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
del dict1["name"]
print(dict1)

#clear dictionary
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
dict1.clear()
print(dict1)


# In[12]:


"""DICTIONARY MORE"""
#looping through dictionary
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
for x in dict1:
    print(x)

#print with values
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
for x in dict1:
    print(dict1[x])
    
#also use values to return value of dictionary
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
for x in dict1.values():
    print(x)

#using key to return the key of dictionary
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
for x in dict1.keys():
    print(x)

#using items to get
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
for x,y in dict1.items():
    print(x,y)

#copy the dictionary
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
newdict=dict1.copy()
print(newdict)

dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
newdict=dict(dict1)
print(newdict)

#nested dictionary
dict1={"name":"gurjeet",
      "age":19,
      "year":2001}
dict2={"name":"khush","age":20,"year":2002}
dict3={"name":"sharukh","age":30,"year":1990}
mydict={
    "dict1":dict1,"dict2":dict2,"dict3":dict3
}
print(mydict)


# In[ ]:




