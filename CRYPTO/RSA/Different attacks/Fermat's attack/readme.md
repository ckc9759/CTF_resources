### Fermat's attack on RSA

---

Use this when p and q are relatively close to each other.

```py
def fermatfactor(N):
       if N <= 0: return [N]
       if is_even(N): return [2,N/2]
       a = ceil(sqrt(N))
       while not is_square(a^2-N):
         a = a + 1
       b = sqrt(a^2-N)
       return [a - b,a + b]

def fermat_factors(n):
    assert n % 2 != 0
    a = gmpy2.isqrt(n)
    b2 = gmpy2.square(a) - n
    while not gmpy2.is_square(b2):
        a += 1
        b2 = gmpy2.square(a) - n
    factor1 = a + gmpy2.isqrt(b2)
    factor2 = a - gmpy2.isqrt(b2)
    return int(factor1), int(factor2)
```

```sage
# sage code
r = isqrt(int(n))

R = Zmod(n)
P.<x, y> = PolynomialRing(R)
bounds = (2^600, 2^300)
f = (r+x)*(r+y) - n

f_roots = small_roots(f, bounds)


for p0, q0 in f_roots:
  p, q = r + p0, r + q0
  phi = (p-1)*(q-1)
  d = inverse_mod(e, phi)
  print(long_to_bytes(pow(c, d, n)))
```
