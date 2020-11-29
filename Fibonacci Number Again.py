#!/usr/bin/env python
# coding: utf-8

# In[1]:


n, m = [int(i) for i in input().split()]


# In[ ]:


def calc_fib(n,m):
    
    Fib = [0] * (n+2)
    Fib[0] , Fib[1] = 0 , 1
    
    for j in range(2, n+1):
       
        Fib[j] = Fib[j-1] + Fib[j-2] 

    return print(Fib[n] % m)

calc_fib(n,m)


# In[ ]:




