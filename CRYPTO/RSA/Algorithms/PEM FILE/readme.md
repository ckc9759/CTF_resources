### PEM FILE

---

```py
-----BEGIN RSA PRIVATE KEY-----
MIIEow... base64 string
-----END RSA PRIVATE KEY-----
```

```py
from Crypto.PublicKey import RSA

RSA=RSA.importKey(open('private.pem').read())

print(RSA.n)
print(RSA.d)
```
