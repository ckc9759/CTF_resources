### PEM FILE

---

[ASN.1 VS DER](https://www.cryptologie.net/article/260/asn1-vs-der-vs-pem-vs-x509-vs-pkcs7-vs/) 
[ASN and DER](https://letsencrypt.org/docs/a-warm-welcome-to-asn1-and-der/)

```py
-----BEGIN RSA PRIVATE KEY-----
MIIEow... base64 string
-----END RSA PRIVATE KEY-----
```

```py
from Crypto.PublicKey import RSA

RSA=RSA.importKey(open('private.pem').read())
# for .DER files, read the file in bytes !
print(RSA.n)
print(RSA.d)
```
