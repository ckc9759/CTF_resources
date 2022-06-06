### All about RSA 
---
RSA Encryption
---

Useful links: http://factordb.com/


Generally in such CTF challenges, we are given 'n' 'e' and 'c' in the challenge.

#### e is the public key...

```python
n is a modulus which is calculated using:
n=p*q
It is a link between public and private keys.
```

Then we have two more factors which is 'p' and 'q'.
With the help of p and q, we calculate phi.

```python
phi=(p-1)*(q-1)
```
The last parameter left is d.

for 'd' which is the **private key** , we need some scripting.

```python
from Crypto.Util.number import inverse
d=inverse(e,phi)
print(d)
```
For the parameter m, we do 
```python
m=pow(c,d,n)
print (hex(m)[2:-1].decode('hex'))
```

This gives us the flag in general cases.

### NOTE:
---
The trick with RSA is that e and d are related such that you can encrypt with either one and then decrypt it with the other.
For actual encryption you encrypt with the public key, so the private key is required for decryption.
But you can also "encrypt" it with your private key to sign the message - then everyone can "decrypt" it with your public key which verifies it was actually you who sent it.

