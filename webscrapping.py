#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system(' pip install beautifulsoup4')


# In[3]:


get_ipython().system(' pip install requests')


# In[5]:


import sys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[16]:


try:
    page=requests.get('https://www.cricbuzz.com/')
except Exception as e:
    error_type, error_obj, error_info = sys.exc_info()
    print('Error from link',url)
    print(error_type, 'Line:', error_info.tb_lineno)
time.sleep(2)
soup=BeautifulSoup(page.text,'html.parser')
links=soup.find_all('div', attrs={"class":"cb-nws-intr"})


# In[17]:


page


# In[18]:


soup


# In[19]:


links


# In[20]:


for i in links:
    print(i.text)
    print("\n")


# In[ ]:




