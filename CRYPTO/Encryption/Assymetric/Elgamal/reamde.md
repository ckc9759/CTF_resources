### Script

```py
def decrypt(c1, c2, x, p):
    pt_int = (c2 * pow(c1, p-1-x, p)) % p
    pt_bytes = pt_int.to_bytes((pt_int.bit_length() + 7) // 8, "big")
    return pt_bytes.decode()
```
