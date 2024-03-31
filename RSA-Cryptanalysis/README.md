# RSA-Cryptanalysis

This project analyzes the security of RSA encryption with different key sizes and encryption exponents. The script uses the SageMath library for its computations.

## Overview

The script is divided into four parts:

1. **Generate RSA key pair and encrypt a message**: We generate an RSA key pair and encrypts a message using a small encryption exponent (3). It uses the `random_prime` function from SageMath to generate two prime numbers `p` and `q`, and then calculates the modulus `n` and the totient `phi`. The encryption exponent `e` is chosen to be small and the decryption exponent `d` is computed using the Extended Euclidean Algorithm.

2. **Low-exponent attack**: Then we attempt to recover the plaintext from the ciphertext using a low-exponent attack. It iterates over all possible messages `m` from 0 to `n-1`, and checks if `m^e mod n` equals the ciphertext. If a match is found, the attack was successful and it returns the corresponding plaintext `m`.

3. **Wiener's attack**: Here we attempt to recover the private key using Wiener's attack. It calculates `a` and `b` such that `a/b` is a good rational approximation of `e/d`, and then uses the `rational_reconstruction` function from SageMath to recover `d`.

4. **Security analysis**: Here we perform a security analysis for different key sizes and encryption exponents. It generates RSA key pairs for each combination of key size and encryption exponent, and then tests the effectiveness of the low-exponent attack and Wiener's attack against these key pairs.


Using sagemath allows us to work with large numbers (sage supports arbitrary precision arithmetic), it provides efficient algorithms for modular arithmetic (this is central to RSA - we use it to calculate `m^e mod n` efficiently) and provides easily usable functions like `rational_construction` for finding a good approximation of `e/d`

