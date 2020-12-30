#!/usr/bin/env python
# coding: utf-8

# In[4]:


### Assignment of Tasks

# Task3
""" #task3
def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    x = a[] #wrtie your code here
    return x

    Expected Output:
     [35,  70, 105, 140, 175, 210, 245, 280, 315, 350, 385, 420, 455,
       490, 525, 560, 595, 630, 665, 700, 735, 770, 805, 840, 875, 910,
       945, 980] 
     """

a = np.arange(1, 100*10+1).reshape((100,10))
x = a[(a %35) == 0] #wrtie your code here
x


# In[2]:


#Task 9
import numpy as np
a=np.arange(2,102,2)
a


# In[3]:


#task5
import numpy as np
z = np.zeros((5,5))#wrtie your code here
z


# In[10]:


#task6
# Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively
import numpy as np

arr = np.zeros(10) 
arr[[4, 7]] = [10, 20] #wrtie your code here


arr


# In[21]:


"""
#task7
def function7():
    #  Create an array of zeros with the same shape and type as X. Dont use reshape method
    x = np.arange(4, dtype=np.int64)
  
    return np.zeros(x.shape, dtype=x.dtype) #write your code here

    
    Expected Output:
          array([0, 0, 0, 0], dtype=int64)
    """ 

import numpy as np
x = np.arange(4, dtype=np.int64)
y = np.zeros(x.shape, dtype=x.dtype) 
y


# In[1]:


"""
#task8
def function8():
    # Create a new array of 2x5 uints, filled with 6.
    
    x = #write your code here
  
    return x

   Expected Output:
              array([[6, 6, 6, 6, 6],
                     [6, 6, 6, 6, 6]], dtype=uint32)
     """ 

 # Create a new array of 2x5 uints, filled with 6.

import numpy as np

x = #write your code here
x = np.arange(4, dtype=np.int64)
y = np.zeros(x.shape, dtype=x.dtype) 


# In[3]:


""""
# Task no 1
def function1():
    # create 2d array from 1,12 range 
    # dimension should be 6row 2 columns  
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods  
    x =  np.arange(1,13).reshape((6,2)) 

    return x
    
    expected output:
    [[ 1  2]
    [ 3  4]
    [ 5  6]
    [ 7  8]
    [ 9 10]
    [11 12]]"""
import numpy as np
x = np.array([6,2])
x = np.arange(1,13).reshape((6,2))
print(x)


# In[8]:


''''# Task2
def function2():
    #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be start from 10 and end with 36 (both included)
    # Hint: dtype, reshape 

    x = np.arange(1,28,dtype=np.float64).reshape((3,3,3))     #wrtie your code here

    return x
    
    Expected: out put
array([[[10., 11., 12.],
        [13., 14., 15.],
        [16., 17., 18.]],
       [[19., 20., 21.],
        [22., 23., 24.],
        [25., 26., 27.]],
       [[28., 29., 30.],
        [31., 32., 33.],
        [34., 35., 36.]]])    

'''
    
import numpy as np
x = np.arange(10,37,dtype=np.float64).reshape((3,3,3))
print(x)


# In[ ]:




