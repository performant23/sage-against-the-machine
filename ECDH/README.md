# Elliptic Curve Diffie-Hellman Key Exchange

This project implements the Elliptic Curve Diffie-Hellman (ECDH) key exchange protocol using the SageMath.

## Overview

The protocol is divided into stages:

1. **Defining the elliptic curve and a point on the curve**: We start by setting up a prime number `p` and an elliptic curve `E` over a finite field `GF(p)`. We also establish a point `G` on the curve.

2. **Choosing secret keys for each party**: Now, each party gets to pick their own secret key, `a` and `b`, which are basically just random numbers between `1` and `p-1`.

3. **Computing public keys for each party**: Next up, both parties calculate their public keys, `A` and `B`, by multiplying their secret key with the point `G` on the elliptic curve.

4. **Exchanging public keys and figuring out a shared secret**: Once the public keys are swapped, Party A works out `a * B` while Party B does `b * A`. Due to properties of elliptic curve multiplication, these two values end up being the same - `a * B = b * A`.

5. **Double-checking if the shared secrets match**: Lastly, the script does a quick comparison to see if the shared secrets computed by both parties are identical.