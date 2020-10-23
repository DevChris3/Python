#!/usr/bin/env python
# coding: utf-8

# In[31]:


class Car():
    
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    
    def __init__(self, make, color):
        
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.make = make
        self.color = color
        
    # OPERATIONS/Actions ----> Methods
    def drive(self):
        print("Zoooom! My car is a {}".format(self.make))


# In[32]:


my_car = Car('Honda', 'Yellow')


# In[33]:


type(my_car)


# In[34]:


my_car.make


# In[35]:


my_car.drive()


# In[ ]:





# In[ ]:





# In[ ]:





# In[36]:


class Circle():
    
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14
    
    def __init__(self, radius = 1):
        
        self.radius = radius
        
    # METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2
    


# In[37]:


# Instance of the Circle class
my_circle = Circle()


# In[38]:


my_circle.pi


# In[39]:


my_circle.radius


# In[41]:


my_circle.get_circumfrence()


# In[ ]:




