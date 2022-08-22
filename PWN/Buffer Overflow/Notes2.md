### N o T e S

---

An anomally where a program, while writing data to buffer, overruns the buffer's boundary and overwrites adjacent memory locations.

What can we do with a buffer overflow :

- Change the local variable's value
- Change the return address of a function
- Inject shellcode and jump to it


### Stack buffer overflow

We can find the return adress of a function using a decompiler like ghidra or using readelf or objdump.



