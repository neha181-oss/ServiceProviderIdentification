#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install phonenumbers


# In[4]:


import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier 
phone_number =phonenumbers.parse("+917032888630")
print(geocoder.description_for_number(phone_number,"en"))
print(carrier.name_for_number(phone_number,"en"))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




