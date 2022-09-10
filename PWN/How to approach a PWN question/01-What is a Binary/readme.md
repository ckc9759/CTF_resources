### Binary

---

A binary is a compiled code. Binary exploitation is the process of exploiting a binary.

```py
REVERSE ENGINEERING

It is a process of finding out how something works and then attack and reverse it to get the desired output or flag in our case.
```

#### What is an Assembly

---

```cpp
When we write a code and try to run it, the file is read by a compiler which converts it to a sequence of instructions performed by the computer. 
The converted code is op code and is not human readable form.

This is where Assembly language comes in. 
It translates the computer instructions to a language whichcan be read by us.
```

#### Basic Elements of a Binary Executable

---

Every C program has 4 key compenents : 

- Stack
- Heap
- Registers
- Instructions

Memory is Allocated to the heap whenever functions like malloc or calloc are called or global and static variables are declared.

Registers are small storage areas in the processor used for storing memory addresses, values or anything represented using 8 bytes.

6 General Purpose Registers : 
```c
eax
ebx 
ecx
edx
esi
edi
```

3 Reserved Registers :
```c
ebp
esp
esi
```

Stack is a data structure comprised of elements that are added and removed using push and pop. (LIFO)
Stack grows towards a lower memory address.

EBP - Base pointer
ESP - Stack pointer

```py
mov -> arg1 arg2 (moves from arg1 to arg2)
mov -> eax, ebp
add -> arg1, arg2 (stores the sum in 1st arg)
Sub -> arg1,arg2 (subtracts and stores in 1st arg)
push and `pop` -> pushed and pops in stack
```

---

```cpp
EIP - Instruction pointer
cmp - Compares two values
jmp - Jumps to a ret add
call - push eip and jmp func
```

```cpp
mov si, sp ; Source Index       <- Question 3
So for this just moves the value of the Stack Pointer register into the Source Index register. In order to know what the value of si is after this, we need to know what the value of sp is. Looking up in the code, we see this on line 149:
```

---
