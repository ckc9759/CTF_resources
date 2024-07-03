If the n of RSA is known and we can find even one of the factors, then we can decrypt the message of rsa using the following script.

```py
from Crypto.Util.number import *
n=3240340324348240233
p=3804273792473893
q=239483048902
e=65537
c=347230470394311
phi=(p-1)*(q-1)
d=inverse(e,phi)
m=pow(c,d,n)
print(long_to_bytes(m))

# Change the values n,e,c,p,q as per your need, rest remains the same
```
