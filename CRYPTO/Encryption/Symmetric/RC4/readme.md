### N o T e S : 

---

A representative stream cipher.

- Stream cipher is a branch of symmetric key cipher. 
- XOR-based common encryption/decryption processing.

Example : 

```py
keystream_from RC4 = "afaofh34892u[tgpwonsl"
RC4_Ciphertext = "82y5329hrw2nfw8920"

plaintext = ""

for k,c in zip(keystream_from RC4, RC4_ciphertext):
   plaintext+=chr(ord(k)^ord(c))
print(plaintext)
```

### Importing ARC4

```py
from Crypto.Cipher import ARC4
```

