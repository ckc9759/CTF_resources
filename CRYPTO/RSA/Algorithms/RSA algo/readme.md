### Readme

---

RSA algo is an assymetric cryptography algorithm.


```py
Assymetric --> 2 keys private and public key.

The concept of RSA is that it is hard to factorise a large integer.

Public key --> N, which is a product of 2 large prime numbers `p` and `q`.

The private key is also derived from the two prime numbers p and q.
```

#### Algorithm

```py
Select two prime numbers p and q
n = p * q

We need a small exponent e in range (1,phi)

Public key is made of n and e

# e must be co prime to n

Private key generation 

phi = (p-1)*(q-1) --> TOTIENT FUNCTION
d = inverse(e,phi) or d=pow(e,-1,phi)

Or e*d = 1 mod (phi)
```

---

Example --> 

```py
Let's suppose our msg ="HI"
We convert it into bytes.
H=8 and I=9

ciphertext ct = (89^e)%n or 89^e mod n

enc data = 1394

Decryption : 

Dec = *(ct)^d)%n or ct^d mod n

dec=89 which converted to strinngs gives "Hi" back.
```










