### Imp Guidelines to approach pwn questions.


Useful commands

`gdb -peda`

`pd main`

```python
1. To create a breakpoint in gdb peda use b* (hex value like 0x000000004011ca.
checksec --file <filename? command- It checks for the securities applied to the Binary.

2. If stack is not canary it hints towards buffer overflow.
info func for info of functions.




* Puts() statement - used to store or write something in stream. 
* Gets() statement- gives us the vulnerability as it take arbitrary input.A vulnerability function which takes input irrespective of it's size and hence has a potential overflow.
* Strcmp() statement - It is used to compare two strings.
* Strlen() - Length of string.

```
`x/s` - displays the argument to a hex value like x/s 0x40772.  

`checksec --file <filename>` - It is used to view the options which are enabled and disabled in a binary file.  

`Not stripped` - When we rev engineer the ELF file, we will be able to view the functions and it's properties. The strip command discards symbols from compiled object files.  

`NX disabled` - Injecting shellcode is allowed.  

`Stack - No canary found` - Buffer overflow   

`chmod +x` - ELF permissions enabled.  


---

* If we provide a very large input and get fail with segmentation fault, that means we can overflow the function.
* cyclic 100 - It is used to generate a random string of length 100.
* cyclic -l kaaa --> It can be used to find the offset.
* `Integer overflow` - Sometimes, in pwn challenge, we are asked an input which when overflowed (i.e outside the range value), we get the flag eventually.

---



