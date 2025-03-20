### PWN 2.0

---

File <filename> -> ELF 64 - length of registers (8byte length registers, i.e rbp etc will be of 8 bytes length)
checksec <filename> -> File protections

```py
# RELRO -> Full relocation read-only
# NX enabled -> No code execution from stack or heao
# PIE enabled -> Position independent executable/code
# Canary -> Stack protection, detects stack smashing
```

```py
call setup -> calls a function
cmp dword -> compares
jne -> jump not equal
Dword -> Double word 4 bytes
Qword -> Quad word 8 bytes
```

```py
# ldd <filename>
# ASLR -> randomizes addresses of memory segments i.e. heap and stack -> making difficult of vuln inorder to execute shellcode
# shellcode -> arbitrary code execution
```

```py
context.binary = binary = "./filename"
context.log_level = "debug"
```

#### Understanding registers

```py
rsp -> top of stack
rbp -> base of stack
rip -> instruction pointer

64 bit architechture -> rdi, rsi, rdx, rcx, r8, r9, then stack
```
