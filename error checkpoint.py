#!/usr/bin/env python
# coding: utf-8

# In[1]:


##the error is located in mylist[6]. the index is out of range and therefore it will result in an 
## index error message saying 'list index out of range'
try:
    mylist=[14, "hello", 967]
    mylist[6]
except:
    print('Index out of range')
    


# In[5]:


## the pandas module and the numpy module is not spelt correctly, it conatians uppercase which shouldn't be there
## It will result in an error saying 'No module named pandas'
try:
    import Pandas
    import NumPy
except:
    print('No module named Pandas')


# In[10]:


## the print statement should start and end with lowercase letters and it the value inside the print statement
## should be enclosed in a bracket
try:
    Print("python errors")
except:
    print('invalid syntax')


# In[11]:


## the variable = mydictionary does not have any key with the value 'True', that's why it would return an error
try:
    mydictionnary={True:"hello",False:"bye", '3':"python"}
    mydictionnary['True']
except:
    print('No key with the value True')


# In[15]:


## the code will return an error message because there should be an indentation in the while loop
try:
    i=14
    while i<78:
        print(i)
        i+=1
except:
    print('indentation error')


# In[17]:


## the program below will result in an error because the list only has 3 indexes but the next() method is called 4 times
try:
    it=iter([1,2,3])
    next(it)
    next(it)
    next(it)
    next(it)
except:
    print('stopiteration')


# In[20]:


## the code below will not run because a string and an integer cannot be added together so it will result in an error
try:
    '15'+15
except:
    print('TypeError')


# In[21]:


## the code will not run because the method int() only takes numbers as an argument not strings or floats
try:
    int('python')
except:
    print('Value error')


# In[23]:


## the code below is invalid beause the word python is not defined
try:
    python
except:
    print('name error')


# In[ ]:


## the code below will result in an error because zero is trying to divide a number greater than it
try:
    x=19/0
except:
    print('ZeroDivisionError')

