### N o T e S :

---

- Choose two primes p and q.
- Choose e where 1 < e < phi(n) and gcd(phi(n),e)=1
- 65537 is the most common used for e
- d = e-1(mod(phi(n))
- Now, we have the RSA key pair.
  - Public key exponent e for encryption
  - Private exponent d for decryption and parameters p and q are to be kept secret.

Signature : 

s = m^d(mod(n))
m = s^e(mod(n))

If we are given, (Sample)

```
n=2897471247204901
e=65537
p=3292305890382
ct=203209401949039890890289
```
Python script ;

```
q=n//p   #n=pq
phi=(p-1)*(q-1)
d=pow(e,-1,phi)
m=pow(ct,d,n)
print(hex(m))
print(bytes.fromhex(hex(m)[2:1]))



