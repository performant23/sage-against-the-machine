#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sage.crypto.util import random_prime


# In[2]:


# Generate RSA keys for homomorphic encryption
p = random_prime(2^512)  
q = random_prime(2^512)
N = p * q  
phi_N = (p - 1) * (q - 1)
e = random_prime(phi_N)
d = inverse_mod(e, phi_N)  


# In[3]:


# Encryption using RSA
def encrypt(m, e, N):
    return pow(m, e, N)  

def decrypt(c, d, N):
    return pow(c, d, N)


# In[4]:


# Homomorphic addition and multiplication over encrypted data
def homomorphic_addition(c1, c2, N):
    return (c1 * c2) % N

def homomorphic_multiplication(c1, c2, N):
    return (c1 * c2) % N


# In[5]:


# Multi-party computation protocol
def secure_mpc_protocol(inputs, e, N):
    encrypted_inputs = [encrypt(input, e, N) for input in inputs]
    result = encrypted_inputs[0]
    for i in range(1, len(encrypted_inputs)):
        result = homomorphic_addition(result, encrypted_inputs[i], N)  
    decrypted_result = decrypt(result, d, N)
    
    return decrypted_result


# In[6]:


# Tester Code

inputs = [123, 456, 789]
result = secure_mpc_protocol(inputs, e, N)
print("Result of secure multi-party computation:", result)

#Output: Result of secure multi-party computation: 44253432