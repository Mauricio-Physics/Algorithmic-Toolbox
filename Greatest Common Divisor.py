#!/usr/bin/env python
# coding: utf-8

# In[19]:


a, b = [int(i) for i in input().split()]

def gcd(a, b):
    
    me = min(a,b)
    ma = max(a,b)
    
    while me != 0:
        
          res = ma % me
          ma = me
          me = res
     
    return print(ma)

gcd(a,b)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




