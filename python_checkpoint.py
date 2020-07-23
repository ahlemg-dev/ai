#!/usr/bin/env python
# coding: utf-8

# In[1]:


#exo1
for x in range (2000,3201):
    if (x%7==0 and x%5!=0):
        print(x, end=" ")


# In[4]:


#exo2

try:
    x=int(input())
except ValueError:
    print("Please enter an integer value")
else:
    res=1
    y=x;
    while (x>=1):
        res=res*x
        x=x-1
    print("the factorial of ",y," is :",res)
    


# In[5]:


#exo3
try:
    x=int(input())
except ValueError:
    print("Please introduce an integer value higher or equal than 1")
else:
    DictRes= dict()
    if(x>0):
        for i in range(1,x):
            DictRes[i]=i*i
        DictRes[x]=x*x
        print(DictRes)
    else:
        print("Please introduce an integer value higher or equal than 1")


# In[ ]:



def missing_char(stri,pos):
    Str2=""
    stri=stri.strip()
    if Pos1<=0 or Pos1>=len(stri):
        print("index is out of range!!!")
    else:
        Str2=stri[0:Pos1]+stri[Pos1+1:len(stri)]
    return Str2

print("introduce a string: ")
Str1=str(input())
print("introduce the index of charater to delete: ")
try:
    Pos1=int(input())
except ValueError:
    print("The introduced index value is not correct!!!")
else:
    
        print("The new string is :",missing_char(Str1,Pos1))

