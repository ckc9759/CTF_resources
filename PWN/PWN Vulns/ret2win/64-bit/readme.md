#### 64 bit

---

```py
We just need to find offset values to overflow the buffer and RBP to reach the RIP/Return address.
For this, I use pattern create and pattern offset in gdb-peda and we check the register RBP register.
We check this value [RBP] in the pattern we gave and add 8 to get the offset value to reach the RIP/Return address.
```

[downunderctf](https://corruptedprotocol.medium.com/downunderctf-2021-outbackdoor-pwn-ret2win-52e367bc497c)
