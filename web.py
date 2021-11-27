#!/usr/bin/env python
# coding: utf-8

# In[27]:


import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from time import *
from random import randint


# In[89]:



    url = "https://meitystartuphub.in/startups/startup-wall?search=&page="+str(page)+"&domain=&location=&stage=&type="


# In[90]:



    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    data = soup.find_all('div', attrs = {'class': 'text-center'})


# In[91]:



for link in soup.find_all('a'):
    print(link.get('href'))
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




