#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4


# In[2]:


import requests


# In[4]:


re = requests.get('https://www.indiatoday.in/')
print(type(re))


# In[5]:


re.text


# In[6]:


soup = bs4.BeautifulSoup(re.text, 'lxml')
type(soup)


# In[9]:


news_box = soup.find('ul',{'class','itg-listing'})

all_news = news_box.find_all('a')

for news in all_news:
    print(news.text)


# In[ ]:




