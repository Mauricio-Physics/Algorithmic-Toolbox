#!/usr/bin/env python
# coding: utf-8

# In[2]:


a, b = [int(i) for i in input().split()]

def lcm(a, b):
    
    me = min(a,b)
    ma = max(a,b)
    
    while me != 0:
        
          res = ma % me
          ma = me
          me = res
            
    return print(int(abs(a*b)/ma))

lcm(a,b)


# In[ ]:




