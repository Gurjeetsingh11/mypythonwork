#!/usr/bin/env python
# coding: utf-8

# In[20]:


"""IF ELSE"""
a=10
b=20
if b>a:
    print("a is greater than b")
else:
    print("b is greate than a")

#ELIF(else if)
a=10
b=10
if(a>b):
    print("a is greater")
elif(b>a):
    print("b is greater")
else:
    print("they are equal")

#shorthand if
a=20
b=10
if a>b : print("a is greater than b")
    
#shorthand if else
a=10
b=20
print("a") if a>b else print("b")

#AND keyword
a=20
b=10
c=30
if a>b and c<a and c>b:
    print("all condition are true")
else:
    print("sorry")

#OR KEYWORD
a=20
b=10
c=30
if a>b or b>c:
    print("true")
    
#NESTED IF
a=20
if a>10:
    print("true")
    if a>20:
        print("less than 20")
    else:
        print("sorry")
        
#pass statement
a=10
b=20
if b>a:
    pass


# In[7]:


"""WHILE LOOP"""
#while
i=1
while i<6:
    print(i)
    i+=1;
    
print("""""")

#break statement
i=1
while i<6:
    print(i)
    if(i==3):
        break;
    i+=1
    
print("""""")
#continue
i=1
while i<6:
    i+=1
    if(i==3):
        continue
    print(i)

print("""""")
#else statement
i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no loner less than 6")


# In[19]:


"""FOR LOOP"""
num=[1,2,3,]
for i in num:
    print(i);
    
#looping through string list
string=["aaa","bbb","ccc"]
for i in string:
    print(i)
    
#looping through string
s="gurjeet"
for i in s:
    print(i);

#break statement with for loop
num=[1,2,3,4,5]
for i in num:
    print(i)
    if(i==4):
        break;
        
#continue statement with for loop
num=[1,2,3,4,5]
for i in num:
    if(i==3):
        continue
    print(i);

#RANGE function
for i in range(6):
    print(i)
    
#DEFINED RANGE
for i in range(100,105):
    print(i)
    
#defing three range
for i in range(0,30,3):
    print(i)

#else in for loop
for x in range(1,6):
    print(x)
else :
    print("end")

#NEXTED FOR LOOPS
A=["red","green","blue"]
B=["apple","grapes","banana"]
for i in A:
    for j in B:
        print(i,j)
        
#PASS statement
for x in [1,2,3]:
    pass


# In[ ]:




