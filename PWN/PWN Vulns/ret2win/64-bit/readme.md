#### 64 bit

---

```py
We just need to find offset values to overflow the buffer and RBP to reach the RIP/Return address. For this, I use pattern create and pattern offset in gdb-peda and we check the register RBP register.
```

[downunderctf](https://corruptedprotocol.medium.com/downunderctf-2021-outbackdoor-pwn-ret2win-52e367bc497c)
