### Diffie hellman

---

Eg : Alice and bob use dh exchange algo. p=13, g=5. Alice bob choose numbers as 7,3. Generated key was used as shift for Caesar cipher. 

```py
A=g^a mod p
B=g^b mod p

s=B^a mod p
s=A^b mod p

s - shared secret
```
```py
For the finite field with p = 28151 find the smallest element g which is a primitive element of Fp.
GF(28151).primitive_element()
```
