#!/usr/bin/env python
# coding: utf-8

# # Type Casting

# In[2]:


type(90)


# In[4]:


type(45)


# In[6]:


type(73.6)


# In[8]:


type("String")


# In[10]:


p=12342


# In[11]:


p


# In[12]:


type(p)


# In[13]:


float(p)


# In[16]:


j=79.56


# In[17]:


type(j)


# In[18]:


int(j)


# In[19]:


str(j)


# In[20]:


k=float(j)


# In[21]:


k


# In[22]:


type(k)


# In[23]:


x="20"


# In[24]:


type(x)


# In[25]:


y=int(x)


# In[26]:


y


# print(y)

# In[27]:


type(y)


# Adding two numbers

# In[43]:


a=input("Enter the value of a=")
int(a)
b=input("Enter the value of b=")
int(b)
c=int(a)+int(b)
d=str(a)+str(b)
print("The answer is=",c)
print("The string answer is=",d)


# In[44]:


type(c)


# In[47]:


i=int(input('Enter the value of i='))
j=int(input("Enter the value of j="))
k=i+j
print("The answer is=",k)


# Area of Rectangle

# In[60]:


l=int(input("Enter the length="))
print('The length of rectangle is=',l)
b=int(input("Enter the breadth="))
print('the breadth of rectangle is=',b)
a=l*b
print("The area of rectangle is=",a)


# Area of Circle

# In[59]:


Radius=int(input("Enter the value of Radius"))
print(Radius)
pi=float(input('Enter the value of pi='))
c=pi*(Radius**2)
print("The area of circle is=",c)


# Area of Triangle

# In[57]:


Base=int(input("Enter the value of base="))
print(Base)
Height=int(input('Enter the value of height'))
print(Height)
c=(1/2)*(Base*Height)
print("The area of triangle=",c)


# In[66]:


v=346.399304


# In[67]:


type(v)


# In[68]:


round(v,2)


# In[ ]:




