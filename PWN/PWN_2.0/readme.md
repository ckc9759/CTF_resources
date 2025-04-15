### PWN 2.0

---

File <filename> -> ELF 64 - length of registers (8byte length registers, i.e rbp etc will be of 8 bytes length)
checksec <filename> -> File protections

```py
# RELRO -> Full relocation read-only
# NX enabled -> No code execution from stack or heao
# PIE enabled -> Position independent executable/code
# Canary -> Stack protection, detects stack smashing

NX enabled : The process mappings won't be writable ( W ) and executable ( X ) at the same time
No canary found : No stack canaries will be present, this protections is used to prevent the exploitation
of linear stack buffer overflows.
No PIE (0x400000) : The program mappings won't be affected by ASLR, only heap, imported libraries
and stack bases will be randomized.
Partial RELRO : The program is using lazy binding , which means that imported functions from
external libraries will be resolved only when called first. This implies that the GOT (Global Offset Table) will
remain writable during the execution of the program.
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

```py
# Finding the offset

from pwn import *
p = process("./filename")  # Or use remote(host, port) if given
p.sendline(cyclic(200))  # Send a pattern larger than expected buffer
p.wait()
core = p.corefile
print(cyclic_find(core.read(core.rsp, 4)))
```
