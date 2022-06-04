### All about RSA 
---
RSA Encryption
---

Useful links: http://factordb.com/


Generally in such CTF challenges, we are given 'n' 'e' and 'c' in the challenge.

```python
n=p*q
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
print(hex(m)[2:-1].decode('hex'))
```

This gives us the flag in general cases.
