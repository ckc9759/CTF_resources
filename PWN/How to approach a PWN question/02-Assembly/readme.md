### Assembly

We are given assembly code also known as binary executable in CTFs.

Now, we use decompilers such as Ghidra to find out what it thinks the C code was.

Different types of processors can run different types of assembly code.

```c
rbp - Base pointer, points to the base of stack frame.

rsp - Stack pointer, points to the top of stack frame.

rip - Instruction pointer, points to the instruction to be executed.
```

Mov instruction

```
mov rax,[rdx] --> Moves the value pointed by rdx to rax ([] acts as dereferencing)
```

`Objdump` - Used for looking at the assembly code.

---

## GDB - Debugger

```py
A debugger is a software which allows us to perform various types of analysis of a running process in a file.

Breakpoints are places in the program where GDB will know to stop execution to allow you to examine the contents of the stack.

We can use `info func` and `disass <name of function` to view functions and disassemble them.

We can view contents of a registry using x/s.

We can create a breakpoint using b* mem add.
```
---

## Ghidra
```py
Ghidra is an open sourced decompiler.
```

## Pwntools
```py
Pwntools is a python ctf library for rapid exploit developement.

USING PWNTOOLS : 

from pwn import *
target = remote("github.com",9123) // connecting to a server
target = process("./chall") // run a binary
gdb.attach(target) //attaching gdb to a process
target.send(x) //sending x to the target
target.sendline(x) //send x followed by a newline character
print target.recvline() // print a single line of text
print target.recvline("out") // print a single line of text upto string out
p64(x) // little endian format
target.interactive() // interact directly with target.

---
Thank you
