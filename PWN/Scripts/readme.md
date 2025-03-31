### Finding offsets

---

Using pwndbg

```py
1. file binary
2. info func/ info registers
3. cyclic 100
4. run the program after copying
5. Find the last 4 bytes in RIP/EIP, sometimes RBP in ghidra
6. Use cyclic -l <>
7. Offset found
```
