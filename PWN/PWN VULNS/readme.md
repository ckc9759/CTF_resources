### PWN 

---

#### Crypto-cat

[ironstone](https://ir0nstone.gitbook.io/notes/other/pwntools) and [nightmare](https://guyinatuxedo.github.io/)

```py
Stack :
NX :
PIE : When Position Independent Executables (PIE) is enabled in an ELF (Executable and Linkable Format) file, it means that the executable is designed to be loaded into memory at any address and still execute correctly. 
RELRO :
RWX :
```


```py
# Some commands
info func, disass main, break main, info stack, x, x/p, x $ebp, checksec

1. Buffer overflow basics - The program crashes if we fill the buffer and exceed it because the other important stack values like base pointer, return pointer etc gets overwritten.

2. Overwriting variables - Overflow buffer and overwrite the variable on stack. We can set the variable with a debugger if it's remote, otherwise pass a payload.

3. Ret2win - Redirect the execution to a win function.

```
