#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sage.all import *
from sage.functions.log import log


# In[6]:


n = var('n')
lam = var('lam')
mu = var('mu')
rho = lam / mu


# In[7]:


# Recurrence Relation for P(n) - Just for reference (not used since the result can be calculated from closed_form directly)
def P(n):
    if n == 0:
        return 1 - rho
    elif n == 1:
        return rho * (1 - rho)
    else:
        return rho * P(n-1)


# In[11]:


# Closed-form Expression for P(n)
closed_form_P = rho**n * (1 - rho)

print("Closed-form expression for P(n):", closed_form_P)
# Output - Closed-form expression for P(n): -(lam/mu)^n*(lam/mu - 1)


# In[12]:


# Expected Number of Customers (L) and Expected Waiting Time (W)

L = sum(n * closed_form_P, n, 0, oo)
print("Expected number of customers in the system (L):", L.simplify())

W = L / (lam * (1 - rho))
print("Expected waiting time in the queue (W):", W.simplify())

# Output
# Expected number of customers in the system (L): -lam/(lam - mu)
# Expected waiting time in the queue (W): 1/((lam - mu)*(lam/mu - 1))
