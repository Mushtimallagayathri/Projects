#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip --version


# In[1]:


pip --version


# In[2]:


pip install pyshoteners


# In[3]:


import pyshorteners


# In[4]:


pip install pyshorteners


# In[5]:


import pyshorteners


# In[8]:


link = input("Enter URL to shorten: ")
shortener = pyshorteners.Shortener()         # Shortener function allows us to shorten the lenghty URL's
shorten_URL = shortener.tinyurl.short(link)  # tinyurl will create aliases for the redirected URL's, short 
print(shorten_URL)


# In[9]:





# In[13]:


import pyshorteners
link = input("Enter the url")
shorten_url = pyshorteners.Shortener().tinyurl.short(link)
print(shorten_URL)


# In[15]:


# If you want to shorten the URL, you need to have python and pip installed on your system.

# To install python go to (https://www.python.org/downloads/), by defualt pip will be available and after setup the installation.

# Check whether python and pip is installed successfully on your machine or not, type the below commands in command prompt.

      #1. To check the python installed or not, go to the python installed directory in command prompt and type python --version
      #2. To check pip installed or not, type pip --version.

# To shorten the URL, we need pyshorteners module to be installed and imported.

# To install the pyshortenrs module, type the provided command (pip install pyshorteners) or (pip3 install pyshorteners)

#After successful installation, import the module using import keyword.

     # import pyshorteners
    

    
#code to shorten the URL's.

import pyshorteners

long_URL = input("Enter the URL to shorten:  ")

shorten_URL = pyshorteners.Shortener().tinyurl.short(long_URL)

print(shorten_URL)


# In[ ]:




