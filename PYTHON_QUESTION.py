#!/usr/bin/env python
# coding: utf-8

# In[7]:


num=[1,2,3,4,5,6,7,8]
sum=0
for i in num:
    sum=sum+i
print("sum of number is : ",sum)


# In[12]:


print(range(10))
print(list(range(10)))
print(list(range(2,8)))
print(list(range(2,20,3)))


# In[26]:


genre=["pop","rock","jazz"]
for i in range(len(genre)):
    print("i like ",genre[i])


# In[ ]:


#for-else without break
digit=[0,1,5]
for i in digit:
    print(i)
else:
    print("no items")


# In[41]:


student_name='soyu'
marks={'james':90 ,' jules':55 ,'Arthur':77}
for student in marks:
    if student==student_name:
        prin(marks[student])
        break;
else:
    print("no entry")


# In[43]:


list=["ABC",12],["BCD",23],["CDE",22],["DEF",67]
for i,num in list:
    print(i,num)


# In[51]:


items=[int,float,"gurjeet",5,3,4,76,12,23]
for item in items:
    if str(item).isnumeric()and item>6:
        print(item)


# In[54]:


n=int(input("enter the number for sum:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("sum is:",sum)


# In[58]:


num=0
while num<3:
    print("inside loop")
    num=num+1
else:
    print("outside loop")


# In[70]:


#break
""""for val in "string":
    if val=="i":
        break
    print(val)
print("end")"""

#continue
for val in "string":
    if val=="n":
        continue
    print(val)
print("end")


# In[86]:


"""for i in range(1,5):
    print(i)"""

"""fruits=["banana","apple","grapes","orange"]
for index,item in enumerate(fruits):
    print(index,item)"""

"""fruits=["banana","apple","grapes","oranges"]
for index,item in enumerate(fruits):
    print(f"fruit : {item} is at index : {index}")"""

"""colors=["red","green","blue","yellow","violet"]
for i in colors:
    print(i)
    if(i=="black"):
        break"""

colors=["red","green","blue","yellow"]
fruits=["banana","grapes","mango","litchi"]
for x in colors:
    for y in fruits:
        print(x,y)


# In[105]:


"""for i in range(4):
    print(i)
else:
    print("simple okk")"""

"""i=0
while(i<3):
    i=i+1
    print("hello block")
else:
    print("by block")"""

"""i=0
while(i==0):print("not valid");"""

"""for i in range(5):
    print(i)"""

"""list=["abc","bcd","cde","def"]
for index in range(len(list)):
    print(len(list))"""

numbers=[1,2,3,4,5]
mul=0
for i in numbers:
    mul=i*i;
    print(mul)
    
"""for i in range(1,6):
    for j in range(i):
        print(i,end=' ')
    print() """


# In[336]:


#program for for-loop
#1-10 print
"""for i in range(1,11):
    print(i)"""
#pattern
'''for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print('')'''
#calculate sum of number given by user
'''sum=0
num=int(input("enter the number for sum:"))
for i in range(1,num+1,1):
    sum+=i;
    print(sum)'''
#multiplication
'''num=2
for i in range(1,11):
    print(i*num)'''
#display number form list using for loop
'''num=[12,75,150,180,145,525,50]
for i in num:
    if i>500:
        break
    elif i>150:
        continue
    elif i%5==0:
        print(i)'''

#total number of digit in number
'''num=121232
count=0
while num!=0:
    num=num//10
    count=count+1
print(count)'''

#pattern
'''n=5
k=5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=" ")
    print("")'''

#print list in reverse order
'''list1=[100,23,32,12,45]
size=len(list1)-1
for i in range(size,-1,-1):
    print(list1[i])'''
# OR
'''list1=[12,232,23,43]
newlist=reversed(list1)
for i in newlist:
    print(i)'''

#print -10 - 1 using for  loop
'''for i in range(10): #for i in range (-10,0,1)
    print(i-10)     #print(i)'''

#use else block with for
'''for i in range(5):
    print(i)
else:
    print("Done")'''

#display prime number
'''for n in range(20,51):
    for i  in range(2,n):
        if n%i==0:
            break
    else:
        print(n)'''

#display fabnacci series
'''n1=0
n2=1
for i in range(10):
    print(n1)
    res=n1+n2
    n1=n2
    n2=res'''

#factorial
'''fact=1;
n=int(input("enter the number for factorial :"))
if n<0:
    print("factorial doesnot exist")
else:
    for i in range(1,n+1):
        fact=fact*i;
    print(fact)'''

#reverse of number
'''num=938947
rev=0
while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print(rev)'''

#display element from list at odd index
'''list1=[10,20,30,40,50,60,70,80,90,100]
for i in list1[1::2]:
    print(i)'''

#cube of given number
'''num=int(input("enter the number for cube"))
for i in range(num+1):
    cube=i*i*i
print("cube is:",cube)'''

#series upto nth term
'''n=5
s=2
ss=0
for i in range(0,n):
    ss=ss+s;
    s=s*10+2
    print(s,end="+")
print(ss)'''

#pattern
'''n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
for i in range(n,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print("\r")'''


                


# In[355]:


#Pattern question
'''n=5
for i in range(n):
    for j in range(i+1):
        print("*",end="  ")
    print(" ")'''
    
''' n=5
for i in range(n):
    for j in range(i,n):
        print("*",end="  ")
    print(" ")'''

'''n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end="  ")
    for j in range(i+1):
        print("*",end="  ")
    print("")'''

'''n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print("")'''

'''n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end="  ")
    for j in range(i):
        print("*",end="  ")
    for j in range(i+1):
        print("*",end="  ")
    print("")'''

'''n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print("")'''
        
'''n=5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end="  ")
    for j in range(i):
        print("*",end="  ")
    for j in range(i+1):
        print("*",end="  ")
    print("")
for i in range(n):
    for j in range(i+1):
        print(" ",end="  ")
    for j in range(i,n-1):
        print("*",end="  ")
    for j in range(i,n):
        print("*",end="  ")
    print("")'''



# In[384]:


'''for i in range(1,22):
    if i%2==0:
        print(i)'''
'''for i in range(1,20):
    if i%2!=0:
        print(i)'''
'''for i in range(20,0,-2):
        print(i)'''
'''n=int(input("enter the number for table :"))
for i in range(1,11):
    print(i*n)'''
'''num=int(input("enter the number: "))
p=1
while num>0:
    r=num%10
    p=p*r
    num=num//10
print("product of number is :",p)'''

"""fact=1
num=int(input("enter the number :"))
for i in range(1,num+1):
    fact=fact*i;
print(fact)"""

"""num=int(input("enter the number for sum: "))
s=0
while n>0:
    r=num%10
    s=s+r
    num=num//10
print(s)"""



# In[386]:


n=0
num=int(input("enter the number "))
for i in range(2,num):
    if num%i==


# In[ ]:




