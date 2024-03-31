#!/usr/bin/env python
# coding: utf-8

# In[8]:


from sage.arith.misc import random_prime, xgcd, rational_reconstruction
from sage.rings.rational_field import QQ


# In[9]:


# Encrypt a message based on RSA key pair
bit_length = 256 
p = random_prime(2**(bit_length//2 - 1), lbound=2**(bit_length//2 - 2), proof=False)
q = random_prime(2**(bit_length//2 - 1), lbound=2**(bit_length//2 - 2), proof=False)
n = p * q
phi = (p - 1) * (q - 1)

e = 3
d = xgcd(e, phi)[1] % phi

message = 56987854
ciphertext = power_mod(message, e, n)
print("Ciphertext:", ciphertext)
# Output - Ciphertext: 185074638163037193511864

# In[10]:


#Low-exponent attack
def low_exponent_attack(ciphertext, e, n):
    for m in range(n):
        if power_mod(m, e, n) == ciphertext:
            return m
    return None

plaintext = low_exponent_attack(ciphertext, e, n)
if plaintext is not None:
    print("Low-exponent attack successful, retrieved: ", plaintext)
else:
    print("Low-exponent attack failed.")

#Output - Low-exponent attack successful, retrieved:  56987854

# In[15]:


#Wiener's attack
def wiener_attack(e, n):
    cf = continued_fraction(e/n)
    convergents = cf.convergents()
    
    for frac in convergents:
        k, d_candidate = frac.numerator(), frac.denominator()
        if k == 0:
            continue
        phi = (e * d_candidate - 1) // k
        a = n - phi + 1
        if (a ** 2 - 4 * n).is_square():
            return d_candidate
        
    return None

x = var('x')
d_wiener = wiener_attack(e, n)
if d_wiener is not None:
    print("Wiener's attack successful, retrieved private key: ", d_wiener)
else:
    print("Wiener's attack failed.")

# Output: Wiener's attack failed.

# In[16]:


# Security analysis
def rsa_security_analysis(bit_lengths, exponents):
    for bit_length in bit_lengths:
        for e in exponents:
            p = random_prime(2**(bit_length//2 - 1), lbound=2**(bit_length//2 - 2), proof=False)
            q = random_prime(2**(bit_length//2 - 1), lbound=2**(bit_length//2 - 2), proof=False)
            n = p * q
            phi = (p - 1) * (q - 1)
            d = xgcd(e, phi)[1] % phi

            ciphertext = power_mod(message, e, n)
            plaintext_low_exp = low_exponent_attack(ciphertext, e, n)
            d_wiener = wiener_attack(e, n)

            print("Key size:", bit_length, "bits, e:", e)
            if plaintext_low_exp is not None and plaintext_low_exp == message:
                print("Low-exponent attack succeeded")
            else:
                print("Low-exponent attack failed")
                
            if d_wiener is not None and d_wiener == d:
                print("Wiener's attack succeeded")
            else:
                print("Wiener's attack failed")
                
            print("-" * 20)

bit_lengths = [64, 128]
exponents = [3, 5, 17]
rsa_security_analysis(bit_lengths, exponents)

# Output
# Key size: 64 bits, e: 3
# Low-exponent attack succeeded
# Wiener's attack failed
# --------------------
# Key size: 64 bits, e: 5
# Low-exponent attack succeeded
# Wiener's attack failed
# --------------------
# Key size: 64 bits, e: 17
# Low-exponent attack succeeded
# Wiener's attack failed
# --------------------
# Key size: 128 bits, e: 3
# Low-exponent attack succeeded
# Wiener's attack failed
# --------------------
# Key size: 128 bits, e: 5
# Low-exponent attack succeeded
# Wiener's attack failed
# --------------------
# Key size: 128 bits, e: 17
# Low-exponent attack succeeded
# Wiener's attack failed
# --------------------