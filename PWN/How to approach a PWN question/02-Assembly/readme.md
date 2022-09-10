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


