### Coppersmith attack

---

```
The Coppersmith attack is a specialized attack in cryptography, particularly on RSA when small public exponents (like e=3) are used and certain conditions on the ciphertext and plaintext are met. It's typically used to recover small roots of a polynomial modulo an integer, and is a complex attack involving lattice reduction techniques like the Lenstra–Lenstra–Lovász (LLL) algorithm.
```

[Wikiwand](https://www.wikiwand.com/en/Coppersmith_method_)
[gitgit](https://gsdt.github.io/blog/2018/07/20/stereotyped-message-attack/)

```py
f(x) = m^e - c
We already knew parts of the message, so f(x) would be

f(x) = (M + m)^e - c
Coppersmith states that Coppersmith’s algorithm can be used to find this integer solution x(0): x(0) < N^(1/e).
```
