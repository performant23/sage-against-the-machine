#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sage.all import *


# In[2]:


# Defining the elliptic curve and a point on the curve
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
E = EllipticCurve(GF(p), [0, 7])
G = E.lift_x(55066263022277343669578718895168534326250603453777594175500187360389116729240)


# In[3]:


# Choosing a secret key
a = randint(1, p-1)
b = randint(1, p-1)

# Computing a public key
A = a * G
B = b * G


# In[4]:


# Exchange public keys and compute a shared secret
shared_secret_A = a * B
shared_secret_B = b * A

if shared_secret_A == shared_secret_B:
    print("The shared secrets match!")
else:
    print("The shared secrets do not match!")

#Output - The shared secrets match!