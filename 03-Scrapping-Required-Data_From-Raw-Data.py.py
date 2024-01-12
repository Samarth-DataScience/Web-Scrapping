#!/usr/bin/env python
# coding: utf-8

# In[33]:


with open('smartprix_mobiles_100124','r', encoding = 'utf-8') as f:
    html = f.read()


# In[34]:


html


# In[35]:


from bs4 import BeautifulSoup


# In[36]:


import numpy as np
import pandas as pd


# In[37]:


soup = BeautifulSoup(html,'lxml')


# In[38]:


soup.prettify()


# In[39]:


containers = soup.find_all('div',{'class': 'sm-product has-tag has-features has-actions'})


# In[40]:


containers


# In[41]:


names = []

for i in containers:
    try:
        name_value = i.find('h2').text.strip()
        names.append(name_value)
    except AttributeError:
        names.append(None)

print("Extracted Names:", names)


# In[42]:


names


# In[43]:


len(names)


# In[44]:


price = []

for i in containers:
    try:
        price_value = i.find('span', {'class': 'price'}).text.strip()
        price.append(price_value)
    except AttributeError:
        price.append(None)

print("Extracted Prices:", price)


# In[45]:


price


# In[46]:


len(price)


# In[47]:


rating = []

rating_tags = soup.find_all('span', {'class': 'sm-rating'})

for i in rating_tags:
    try:
        rating_value = float(i['style'].split(':')[1].rstrip(';'))
        rating.append(rating_value)
    except (KeyError, IndexError, ValueError):
        rating.append(np.nan)

print("Extracted Ratings:", rating)


# In[48]:


rating


# In[49]:


import numpy as np

spec_score = []

for i in containers:
    div_tag = i.find('div', {'class': 'score rank-2-bg'})
    if div_tag:
        b_tag = div_tag.find('b')
        if b_tag:
            score_value = b_tag.text
            spec_score.append(score_value)
        else:
            spec_score.append(np.nan)
    else:
        spec_score.append(np.nan)

print("Extracted Spec Scores:", spec_score)


# In[50]:


connectivity = []
for i in containers:
    try:
        connectivity.append(i.find('ul',{'class':'sm-feat specs'}).find('li').text)
        
    except (KeyError, IndexError, ValueError):
        connectivity.append(np.nan)
        
print(connectivity)
    


# In[51]:


len(connectivity)


# In[52]:


processor = []

for i in containers:
    ul_tag = i.find('ul', {'class': 'sm-feat specs'})
    
    if ul_tag:
        li_tags = ul_tag.find_all('li')
        
        if len(li_tags) > 1:
            processor_value = li_tags[1].text.strip()
            processor.append(processor_value)
        else:
            processor.append(np.nan)
    else:
        processor.append(np.nan)

print("Extracted Processors:", processor)


# In[53]:


processor


# In[54]:


len(processor)


# In[55]:


storage = []
for i in containers:
    ul_tag = i.find('ul', {'class': 'sm-feat specs'})
    
    if ul_tag:
        li_tags = ul_tag.find_all('li')
        
        if len(li_tags) > 1:
            processor_value = li_tags[2].text.strip()
            storage.append(processor_value)
        else:
            storage.append(np.nan)
    else:
        storage.append(np.nan)

print("Extracted storages:", storage)


# In[56]:


storage


# In[57]:


battery = []
for i in containers:
    ul_tag = i.find('ul', {'class': 'sm-feat specs'})
    
    if ul_tag:
        li_tags = ul_tag.find_all('li')
        
        if len(li_tags) > 1:
            processor_value = li_tags[3].text.strip()
            battery.append(processor_value)
        else:
            battery.append(np.nan)
    else:
        battery.append(np.nan)

print("Extracted storages:", battery)


# In[58]:


charge = []
for i in soup.find_all('div',{'class':'sm-product has-tag has-features has-actions'}):
    x = i.find('ul',{'class':'sm-feat specs'}).find_all('li')
    charge.append(x[3].text)


# In[59]:


charge


# In[60]:


battery


# In[102]:


display = []
for i in soup.find_all('div',{'class':'sm-product has-tag has-features has-actions'}):
    x = i.find('ul',{'class':'sm-feat specs'}).find_all('li')
    display.append((x[4].text))


# In[103]:


display


# In[104]:


camera = []
for i in soup.find_all('div',{'class':'sm-product has-tag has-features has-actions'}):
    x = i.find('ul',{'class':'sm-feat specs'}).find_all('li')
    camera.append(x[5].text)


# In[105]:


camera


# In[81]:


len(camera)


# In[89]:


extra_storage = []
for i in soup.find_all('div',{'class':'sm-product has-tag has-features has-actions'}):
    try:
        x = i.find('ul',{'class':'sm-feat specs'}).find_all('li')
        extra_storage.append(x[6].text)
    except (KeyError, IndexError, ValueError):
        extra_storage.append(np.nan)
        


# In[90]:


extra_storage


# In[93]:


len(extra_storage)


# In[95]:


os = []
for i in soup.find_all('div',{'class':'sm-product has-tag has-features has-actions'}):
    try:
        x = i.find('ul',{'class':'sm-feat specs'}).find_all('li')
        os.append(x[7].text)
    except (KeyError, IndexError, ValueError):
        os.append(np.nan)


# In[96]:


os


# In[110]:


df = pd.DataFrame({
    'mobile_name' : names,
    'price' : price,
    'rating': rating,
    'specs_score': spec_score,
    'connectivity' : connectivity,
    'processor': processor,
    'storage': storage,
    'battery': battery,
    'display': display,
    'camera': camera,
    'extra_storage': extra_storage,
    'os': os
})


# In[111]:


df


# In[114]:


df.isnull().sum()


# In[116]:


df.head(3)


# In[119]:


df.dtypes


# In[120]:


# exporting the result
df.to_csv('mobiles.csv', index = False)


# In[121]:





# In[ ]:




