### PWN 

---

#### John-hammond

```py
dmesg | tail
```

#### Crypto-cat

[ironstone](https://ir0nstone.gitbook.io/notes/other/pwntools) and [nightmare](https://guyinatuxedo.github.io/)

```py
NO PIE - It means the executable file and server have the same coded source file and won't change each time the program loads. When Position Independent Executables (PIE) is enabled in an ELF (Executable and Linkable Format) file, it means that the executable is designed to be loaded into memory at any address and still execute correctly. 
NX ENABLED - We cannot inject our own shellcode to the stack and execute it.
NO STACK CANARY - We can overflow the buffer and there won't be any canaries.
PARTIAL RELRO - read and write availability.
```

```py
# Some commands
info func, disass main, break main, info stack, x, x/p, x $ebp, checksec

1. Buffer overflow basics - The program crashes if we fill the buffer and exceed it because the other important stack values like base pointer, return pointer etc gets overwritten.

2. Overwriting variables - Overflow buffer and overwrite the variable on stack. We can set the variable with a debugger if it's remote, otherwise pass a payload.

3. Ret2win - Redirect the execution to a win function.

```

```py
- Buffer Overflows: When a program writes more data than a buffer can hold, overwriting adjacent memory.
- Format String Vulnerabilities: Exploiting improper handling of format specifiers in functions like printf.
- Use-After-Free (UAF): Accessing memory after it has been freed.
- Heap Exploitation: Manipulating the program's heap memory for malicious purposes.
- Return-Oriented Programming (ROP): Chaining small instruction sequences to bypass protections like Data Execution Prevention (DEP).
```

