#!/usr/bin/env python
# coding: utf-8


Line-1:

either run the below command 
get_ipython().system(' pip install beautifulsoup4')

 or if in jupyter or any other python compiler platforms directly runthe command
! pip install beautifulsoup

Line-2:

either run the below command 
get_ipython().system(' pip install requests')
 or if in jupyter or any other python compiler platforms directly runthe command
! pip install requests


Line-3:

import sys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd


Line-4:

try:
    page=requests.get('https://www.cricbuzz.com/')
except Exception as e:
    error_type, error_obj, error_info = sys.exc_info()
    print('Error from link',url)
    print(error_type, 'Line:', error_info.tb_lineno)
time.sleep(2)
soup=BeautifulSoup(page.text,'html.parser')
links=soup.find_all('div', attrs={"class":"cb-nws-intr"})


Line-5:

page


Line-6:

soup


Line-7:

links


Line-8:

for i in links:
    print(i.text)
    print("\n")







