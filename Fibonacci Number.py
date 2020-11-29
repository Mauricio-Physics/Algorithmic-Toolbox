#!/usr/bin/env python
# coding: utf-8

# In[10]:


def calc_fib(n):
    
    Fib = [0] * (n+2)
    Fib[0] , Fib[1] = 0 , 1
    
    for j in range(2, n+1):
       
        Fib[j] = Fib[j-1] + Fib[j-2] 

    return print(Fib[n])

n = int(input())

calc_fib(n)


# In[ ]:





# In[ ]:




