#!/usr/bin/env python
# coding: utf-8

# In[26]:


class Animal():
    
    def __init__(self):
        print("Animal Created")
        
    def what_am_i(self):
        print("I am an Animal")
        
    def eat(self):
        print("I am eating")


# In[34]:


class Dog(Animal):
    
    def __init_(self):
        Animal.__init__(self)
        print("Dog created")
        
    def what_am_i(self):
        print("I am a dog!")


# In[35]:


mydog = Dog()


# In[ ]:





# In[36]:


my_animal = Animal()


# In[37]:


my_animal.eat()


# In[38]:


my_animal.what_am_i()


# In[39]:


mydog.eat()


# In[40]:


mydog.what_am_i()


# In[ ]:





# In[ ]:





# In[ ]:





# In[41]:


class Dog():
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + " says woof!"


# In[42]:


class Cat():
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + " says meow!"


# In[43]:


junior = Dog("Junior")
senior = Cat("Senior")


# In[44]:


print(junior.speak())


# In[45]:


print(senior.speak())


# In[ ]:




