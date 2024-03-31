# Homomorphic Encryption and Secure Multi-party Computation

This project implements a homomorphic encryption scheme and a secure multi-party computation protocol using SageMath. 

## Overview

The script performs the following steps:

1. **Generate RSA keys for homomorphic encryption**: The script first generates RSA keys for homomorphic encryption.

2. **Encryption and decryption functions using RSA**: We define two utilities `encrypt` and `decrypt` for RSA encryption and decryption. 

3. **Homomorphic operations over encrypted data**: Then, we define helper functions for performing homomorphic addition and multiplication over encrypted data, respectively. These functions use the properties of RSA encryption to perform operations on encrypted data without decrypting it.

4. **Secure multi-party computation protocol using homomorphic encryption**: Then we implement `secure_mpc_protocol` that implements a secure multi-party computation protocol using homomorphic encryption. This function encrypts the inputs, performs homomorphic computation over the encrypted inputs, and then decrypts the result.

## Background

Homomorphic encryption is an advanced method of encrypting data that allows mathematical operations to be performed on the encrypted data itself. This means you can manipulate encrypted information without needing to decrypt it first, and when you do eventually decrypt it, the result matches what you would have obtained if you had performed the operations on the unencrypted data. It's a crucial feature for maintaining data privacy while still enabling useful computations.

Secure multi-party computation (MPC) is a branch of cryptography focused on enabling multiple parties to collaboratively compute a function over their respective inputs while keeping those inputs confidential. In simple terms, it allows different parties to work together on a task without revealing their private data to each other.

RSA (Rivest-Shamir-Adleman) is a foundational encryption algorithm widely used for secure communication over insecure channels. In RSA, each user has a pair of keys: a public key for encryption and a private key for decryption. The security of RSA relies on the computational difficulty of factoring large integers, known as the factoring problem.