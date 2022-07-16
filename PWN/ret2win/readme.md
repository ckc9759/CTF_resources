### N o T e S

---

- First two steps, add permissions using chmod  +x file name.  
- Then, check the options and protections enabled using checksec --file.  
- Aim of the pwn challenge is generally to overflow the buffer and overwrite the return address.
- It redirects the program towards a function which outputs the flag.

```py
NO PIE - It means the executable file and server have the same coded source file and won't change each time the program loads.
NX ENABLED - We cannot inject our own shellcode to the stack and execute it.
NO STACK CANARY - We can overflow the buffer and there won't be any canaries.
PARTIAL RELRO - read and write availability.
```

---

Use Ghidra and GDB. 

```py
PUTS - It displays some output just like printf.
GETS - It reads some data just like scang.

